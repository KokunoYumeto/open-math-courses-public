# Why the cuspidal spectrum is discrete

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Author self-check complete. Public domain (CC0).*

The modular surface has a cusp of finite area and unbounded height. Finite area alone does not make its convolution operators compact. What supplies compactness on cusp forms is cancellation: the part of the kernel that survives at great height has a constant Fourier term, and a cusp form integrates to zero against that term. We will construct a bounded replacement kernel, prove its quantitative decay, and use positive compact operators to obtain a discrete representation spectrum with finite multiplicities.

We use the adèles, determinant decomposition, principal congruence components and Haar measures from Adèles for GL₂ and strong approximation. The distinction between a function and a section with central character is as in From modular forms to adelic functions. We assume the Hilbert-space spectral theorem, elementary Fourier analysis on a circle and on the real line, and the construction of an operator from a closed nonnegative quadratic form. Short proofs of the compactness and local regularity facts needed below are included. Section 4 proves arithmetic finiteness for rational GL₂ at fixed finite level, compact type and cofinite enveloping-centre ideal, including uniform local estimates, cusp Fourier decay and the fixed-weight compact resolvent. It then derives the smoothing and rapid-decay statements used in the automorphic-module lesson.

All Hilbert-space assertions have a fixed **unitary** central character \(\omega\). Write

\[
X=G(\mathbb Q)Z(\mathbb A)\backslash G(\mathbb A),\qquad G=\mathrm{GL}_2,
\qquad H=L^2(X,\omega).
\]

An element of \(H\) is represented on the rational quotient with \(u(gz)=\omega(z)u(g)\). Its absolute value descends to \(X\). The preceding lesson on adèles gives \(\operatorname{vol}(X)=\pi/3\) for our measures. For
\(f\in C_c^\infty(G(\mathbb A))=C_c^\infty(G(\mathbb R))\otimes C_c^\infty(G(\mathbb A_f))\), an algebraic tensor product, put

\[
R(f)u(g)=\int_{G(\mathbb A)}f(t)u(gt)\,dt.
\tag{1.1}
\]

A finite linear combination of decomposable kernels suffices throughout.

## 1. The cuspidal Hilbert space and cusp coordinates

Let \(n(t)=\begin{pmatrix}1&t\\ 0&1\end{pmatrix}\). The constant term is initially a locally square-integrable function on \(G(\mathbb A)\):

\[
C_Nu(g)=\int_{\mathbb Q\backslash\mathbb A}u(n(t)g)\,dt.
\tag{1.2}
\]

The additive quotient has volume one. For measurable functions this equation is understood almost everywhere, or equivalently as an equation of distributions. Define \(H_{\rm cusp}=\ker C_N\).

**Lemma 1.1.** This is a closed, right-invariant subspace of \(H\). Constant terms commute with right convolution. If \(u\in H_{\rm cusp}\), then \(R(f)u\) is smooth and its constant term vanishes everywhere.

**Proof.** Choose the compact representative set \([0,1]\times\widehat{\mathbb Z}\) for the additive quotient, allowing the measure-zero duplication at its boundary. If \(B\) is a compact subset of the central quotient of the adelic group, the products \(n(t)B\) lie in a compact subset. On such a set the pullback of an \(L^2\) function on \(X\) has its \(L^2\) norm bounded by a constant times its quotient norm. Indeed the rational projective group is discrete, and only finitely many of its translates of a compact set can meet that set: their ratios lie in a fixed compact set intersected with that discrete group. One can also check discreteness directly with the integral primitive matrices used below; near the identity their finite determinant is a unit and their real entries isolate the identity.

Cauchy–Schwarz in (1.2), followed by integration over \(B\), consequently gives
\(\|C_Nu\|_{L^2(B)}\leq c_B\|u\|_H\).
The intersection of the kernels of these local bounded maps, over a compact exhaustion, is closed. Right translations commute with the integral, so it is invariant. For compactly supported convolution, Fubini gives

\[
C_N(R(f)u)(g)=\int f(t)C_Nu(gt)\,dt.
\tag{1.3}
\]

Local square integrability and the compact domains justify this identity first against compact test functions and then almost everywhere. Convolution by \(f\) is smooth at infinity and has an open finite stabilizer. To see its smooth representative directly, periodize its compact kernel on the rational quotient: on compact coordinate sets the periodized sum and each differentiated sum are finite, and their rows are square integrable. Differentiation and local Sobolev bounds therefore give a smooth representative. Its constant term is smooth; if it vanishes almost everywhere it vanishes everywhere. \(\square\)

**Lemma 1.2 — reduction and cusp charts.** Modulo the centre and the rational group, representatives lie in a Siegel set with bounded unipotent coordinate, compact finite coordinate and real height \(y\geq\sqrt3/2\). At every fixed finite level, a finite cover of the quotient consists of finitely many congruence surfaces with their compact rotation fibres. Each such surface has a compact core and finitely many cusp regions

\[
\sigma\{x+iy:0\leq x<w,\ y>Y_0\},\qquad \sigma\in\mathrm{SL}_2(\mathbb Z),
\tag{1.4}
\]

where \(w\) is a positive integer. On a sufficiently deep principal congruence cover one may take \(w=M\) at every cusp.

**Proof.** The level-one determinant decomposition leaves a real positive matrix and a finite maximal compact factor. Remove its positive scalar and write the real matrix as

\[
s(x+iy)r(\theta),\qquad
s(x+iy)=\begin{pmatrix}\sqrt y&x/\sqrt y\\ 0&1/\sqrt y\end{pmatrix}.
\]

The modular fundamental region established in the prerequisite has \(|x|\leq1/2\) and \(y\geq\sqrt3/2\). This proves the level-one assertion; it uses that prerequisite reduction rather than repeating its classical proof.

An open finite level contains a principal \(K(M)\) after intersecting with the maximal compact. The principal determinant components from the first lesson are finite and their real groups are \(\Gamma(M)\). A finite-index congruence subgroup has a fundamental set made from finitely many translates of the modular region. Their portions below any fixed cusp height form a compact core. Group the remaining translates by the rational cusp to which they carry infinity; the integral translations within each group give a strip whose width is the translation stabilizer. There are finitely many groups. The congruence condition makes that width a positive integer. For \(\Gamma(M)\), normality under \(\mathrm{SL}_2(\mathbb Z)\) and the condition \(n(w)\equiv I\pmod M\) give width \(M\).

These sufficiently high strips are disjoint in the quotient. If a matrix relating two strip representatives has nonzero lower-left entry \(c\), then
\(\operatorname{Im}(\gamma z)=y/|cz+d|^2\leq1/(c^2y)\).
It cannot take two points of height greater than one to each other. Matrices with \(c=0\) are exactly the cusp stabilizers already used to select the width. Compact rotations supply the remaining real coordinate. Quotienting by finite scalar units identifies finitely many pieces, possibly with unitary character phases. Lifting to the finite cover gives ordinary congruence functions, with these finite identifications imposed afterwards. \(\square\)

For a cusp function at finite level, its integral over the \(x\)-coordinate in each chart is zero, at each fixed \(y\) and rotation. This is the full adelic condition (1.2), not only a test at the cusp infinity of the level-one component. To verify it, choose \(D\) with the conjugated finite unipotents \(n(D\widehat{\mathbb Z})\) in the level stabilizer, and use the additive fundamental set \([0,D)\times D\widehat{\mathbb Z}\). Its integral is the real period average. Passing to a principal cover or a larger period retains the zero average.

## 2. The arithmetic shape of the convolution kernel

We give the finite-place details before the Fourier estimate. They ensure that the argument applies to all finite levels and central characters.

Integrate the kernel against the centre:

\[
F_\omega(t)=\int_{Z(\mathbb A)}f(zt)\omega(z)\,dz.
\tag{2.1}
\]

It satisfies \(F_\omega(zt)=\omega(z)^{-1}F_\omega(t)\), and is supported on a compact subset of the projective adelic group. Formula (1.1) is consequently represented by the periodized kernel

\[
K_f(g,h)=\sum_{\gamma\in G(\mathbb Q)/Z(\mathbb Q)}F_\omega(g^{-1}\gamma h).
\tag{2.2}
\]

The central equivariance in the two variables makes \(K_f(g,h)u(h)\) well defined under the quotient integration. For a decomposable \(f\), (2.1) separates into its real and finite central integrals. Both integrals are absolutely convergent on their compact intersections with central fibres.

Choose a principal level \(K(M)\), with \(M\geq3\), under which the finite kernel is bi-invariant, and sufficiently deep that \(\omega\) is trivial on scalar units congruent to one modulo \(M\). Such a level exists by local constancy and compact support. The operator factors through the orthogonal projection onto the \(K(M)\)-fixed space. The finite cover in Lemma 1.2 has finitely many components; the extra finite scalar identifications are finite averages with character coefficients of absolute value one. We may prove estimates on the cover and then apply those finite averages.

**Lemma 2.1 — primitive matrices.** On this cover, each matrix entry of (2.2) is a sum of kernels of the following form. Represent a rational projective matrix by a primitive integer matrix
\(\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), unique up to sign, and put \(D=\det\gamma\ne0\). Only finitely many positive or negative integers \(D\) contribute. Its real argument can be normalized to \(\gamma/\sqrt{|D|}\); the remaining coefficient \(\kappa(\gamma)\) is bounded and depends locally constantly on its finite entries. After choosing cusp coordinates, these assertions still hold. For \(c=0\), the pairs \((a,d)\) are finite in number and the coefficient as a function of the integer \(b\) is periodic modulo some positive integer \(L\).

**Proof.** Clear denominators and divide the common integer content to obtain the primitive representative. At every prime at least one entry is a unit. A compact subset of the finite projective group has bounded Cartan distance at a finite set of primes, and lies in the projective maximal compact at all remaining primes. In elementary matrix terms, normalize a local representative so that its largest entry has absolute value one. Its determinant then has valuation bounded on that compact set. This assertion follows by taking a compact lift in finitely many projective coordinate charts and using continuity of the determinant and inverse. For our primitive integer representative the normalization is already in place. Therefore

\[
v_p(D)=0\quad(p\notin S),\qquad 0\leq v_p(D)\leq e_p\quad(p\in S)
\tag{2.3}
\]

for a fixed finite set \(S\) and fixed integers \(e_p\). Thus \(|D|\) divides a fixed integer. The finite component representatives can be taken in \(G(\widehat{\mathbb Z})\); multiplying by them or by integral cusp matrices preserves the minimum entry valuation and changes the determinant only by a finite unit. Hence the same argument applies in every component and cusp chart.

At infinity replacing \(\gamma\) by \(\gamma/\sqrt{|D|}\) changes the central integral by the scalar \(\omega_\infty(\sqrt{|D|})^{-1}\). It has absolute value one and depends only on one of the finitely many \(D\). Absorb it into the finite coefficient. Boundedness of that coefficient follows from continuity on the compact set of finite integral matrices with the indicated determinants; their inverses have bounded denominators by (2.3).

When \(c=0\), the equation \(ad=D\) gives finitely many integer pairs, with \(a,d\ne0\). For a fixed pair, allowing \(b\in\widehat{\mathbb Z}\) gives a compact family of finite invertible matrices. The locally constant coefficient on this family is constant on cosets of \(L\widehat{\mathbb Z}\) for some \(L\). The condition that the matrix be primitive is \(\gcd(a,b,d)=1\), which is also periodic in \(b\). Enlarge \(L\) to include that condition. Choosing one sign, for example \(d>0\) when \(c=0\), changes neither finiteness nor periodicity. These observations prove the lemma, including the unitary phases from finite scalar identifications. \(\square\)

On compact portions of two real components the sum (2.2) is uniformly finite: normalized real support bounds all entries of \(\gamma/\sqrt{|D|}\), and the determinant list is finite. Thus its kernel and its real derivatives are uniformly bounded there.

## 3. The basic estimate, with the constant mode removed

**Theorem 3.1 — GL₂ basic estimate.** For every \(f\in C_c^\infty(G(\mathbb A))\), its restriction to \(H_{\rm cusp}\) has a measurable modified kernel \(\widetilde K_f\) bounded on the product of Siegel sets. In cusp coordinates, for every \(A>0\),

\[
|\widetilde K_f(g,h)|\leq C_{f,A}\,y(g)^{-A}
\quad\text{when }y(g)\text{ is sufficiently large}.
\tag{3.1}
\]

In the high rows its support has \(c_f y(g)\leq y(h)\leq C_f y(g)\). It represents \(R(f)\) on cusp functions; its removed part integrates to zero against them. Consequently

\[
|R(f)u(g)|\leq C'_{f,A}\,y(g)^{-A}\|u\|_2
\qquad(u\in H_{\rm cusp}).
\tag{3.2}
\]

**Proof.** Work on the finite principal cover just constructed; finite sums and unitary averages will preserve all bounds. Choose coordinates in a row cusp and a column cusp, conjugating by their integral cusp matrices. Put \(g=s(x+iy)r(\theta)\), \(h=s(x'+iy')r(\theta')\), with bounded strip coordinates and \(y,y'\geq y_0>0\). Compact real projective support gives a uniform bound \(C\) on the entries of the normalized argument, after removing the rotations. Its lower-left entry is

\[
\frac{c\sqrt{yy'}}{\sqrt{|D|}}.
\tag{3.3}
\]

Since \(c\) is an integer and \(|D|\) ranges over a finite set, a sufficiently high row \(y\) forces \(c=0\), for every \(y'\geq y_0\). With \(c=0\), the diagonal entries are
\(a\sqrt{y'/y}/\sqrt{|D|}\) and \(d\sqrt{y/y'}/\sqrt{|D|}\).
The nonzero integers \(a,d\), again in a finite list, force \(y'/y\) into a fixed compact subinterval of \((0,\infty)\). In particular a sufficiently high row can meet only the full strip part of a column cusp. Conversely, a bounded row cannot meet columns of arbitrarily great height: (3.3) first forces \(c=0\), and then the diagonal bounds exclude such columns. Thus all the remaining bounded rows have their kernel supported in bounded columns, where the preceding compact-region count applies.

It remains to treat a high row. Fix \(D,a,d\), a residue class \(b=r+Lm\) from Lemma 2.1, and the two rotations. Put \(\rho=\sqrt{y'/y}\), which varies in a compact interval. The real kernel as a function of the upper-right entry has the form

\[
h_\rho(v)=F_{\infty,\omega}\left(
r(-\theta)\begin{pmatrix}a\rho/\sqrt{|D|}&v\\0&d/(\rho\sqrt{|D|})\end{pmatrix}r(\theta')
\right).
\]

These are smooth functions supported in a fixed bounded \(v\)-interval. All their \(v\)-derivatives are bounded uniformly in \(\rho\) and the rotations, since the parameters range over compact sets. The upper-right entry of \(g^{-1}(\gamma/\sqrt{|D|})h\) is
\((a x'+b-dx)/\sqrt{|D|yy'}\).
Define

\[
Q=\frac{\sqrt{|D|yy'}}{L},\qquad t=\frac{a x'+r-dx}{L}.
\]

The sum along this progression is its constant finite coefficient times

\[
\sum_{m\in\mathbb Z}h_\rho\left(\frac{m+t}{Q}\right)
=Q\sum_{n\in\mathbb Z}\widehat h_\rho(nQ)e^{2\pi int},
\quad
\widehat h_\rho(\xi)=\int_\mathbb R h_\rho(v)e^{-2\pi i\xi v}\,dv.
\tag{3.4}
\]

This is ordinary real Poisson summation. For completeness, periodize the smooth compactly supported function of \((m+t)/Q\) as a smooth one-periodic function of \(t\). Integration over one period, followed by the substitution \(v=(m+t)/Q\), gives its \(n\)-th Fourier coefficient \(Q\widehat h_\rho(nQ)\). Repeated integration by parts makes that Fourier series absolutely and uniformly convergent, proving (3.4).

For every integer \(B\geq0\), integration by parts and the uniform derivative bounds give
\(|\widehat h_\rho(\xi)|\leq C_B(1+|\xi|)^{-B}\).
For \(B>1\) and \(Q\geq1\), the nonzero modes in (3.4) consequently satisfy

\[
\left|Q\sum_{n\ne0}\widehat h_\rho(nQ)e^{2\pi int}\right|
\leq C_B Q^{1-B}\sum_{n\ne0}|n|^{-B}.
\tag{3.5}
\]

Both frequency signs occur. Cuspidality has removed only the zero frequency. Because \(Q\) is comparable to \(y\), (3.5) is \(O_B(y^{1-B})\).

The omitted zero mode is \(Q\widehat h_\rho(0)\). It is independent of \(x'\), even when the finite coefficient depends on the residue class \(r\). Integrating it against a cusp function over the complete column strip therefore gives zero at each fixed \(y',\theta'\). Subtract these zero modes in high rows, and leave the original kernel in the bounded rows. The high-row support remains in the same height-ratio interval: outside it the real kernel is zero for every upper-right parameter, so its Fourier transform is zero as well. The sum has finitely many determinant, diagonal, residue and component choices. Equations (3.5) and the bounded-row count prove (3.1), with any requested \(A\) obtained by increasing \(B\). This constructs the asserted measurable kernel. The cutoff between high and bounded rows need not be smooth; no derivative of that cutoff is used.

On the cover the quotient volume is finite. Cauchy–Schwarz in the column variable gives (3.2). Finite scalar averages and the finite-level projection are bounded finite sums and preserve the kernel bound; transporting the result back to \(X\) gives a bounded kernel representative there. All central-character factors used in this transport have absolute value one. For a general algebraic tensor sum, add its finitely many estimates. \(\square\)

The same construction works with every differentiated compact kernel. It therefore controls all real derivatives of \(R(f)u\). It also works on a moderate-growth cusp function before square integrability is known. If such a function is \(O((y')^r)\) on the relevant strips, the high-row integral has \(y'\) comparable to \(y\). Its column measure is \(O(y^{-1})\), since the density is \(dx'\,dy'/(y')^2\) and the strip width and rotations are bounded. Multiplying this measure by (3.5) and the growth bound gives \(O(y^{r-B})\). Thus convolution of a moderate-growth cusp function is rapidly decreasing as well. These integrals converge on each height window, and the subtracted zero-mode integrals are exactly zero; this argument does not assume the function was already in \(L^2\).

## 4. Arithmetic finiteness and rapid decay

An automorphic form here is smooth, finite under the real maximal compact and a finite compact open, finite under the centre of the enveloping algebra, and of polynomial group growth. A cusp form additionally has (1.2) zero for every \(g\).

**Lemma — uniform local elliptic bounds.** On a rotation weight \(k\), the Casimir is
\[
\Delta_k=-y^2(\partial_x^2+\partial_y^2)+iky\partial_x.
\]
If a smooth function \(f\) satisfies \(P(\Delta_k)f=0\), for a fixed nonzero polynomial \(P\), and \(|f(x,y)|\leq Cy^N\) in a cusp, then every derivative formed from \(y\partial_x,y\partial_y\) has the same polynomial exponent there, with a constant depending on the derivative.

**Proof.** Put \(d=\deg P\). If \(d=0\), the equation forces \(f=0\); otherwise \(d\geq1\). At height \(y_0\), use \(u=(x-x_0)/y_0,\ v=y/y_0\). On a fixed box with \(1/2<v<2\), the operator becomes
\[
-v^2(\partial_u^2+\partial_v^2)+ikv\partial_u.
\]
All its coefficients and their derivatives are bounded independently of \(x_0,y_0\); the principal symbol of \(P(\Delta_k)\), of order \(2d\), is a nonzero constant times \(v^{2d}|\xi|^{2d}\), bounded away from zero on the unit frequency sphere.

Here are the interior estimates needed for this observation. For a compactly supported function in a Euclidean box, the Fourier transform gives
\[
\|h\|_{H^{r+2d}}
\leq C_r(\|(-\Delta_{\mathrm E})^dh\|_{H^r}+\|h\|_2).
\]
It also gives
\(\|h\|_{H^{r+2d-1}}\leq\epsilon\|h\|_{H^{r+2d}}+C_{\epsilon,r}\|h\|_2\):
split the frequency integral at a sufficiently large radius. Freeze the principal coefficients on small boxes. Their oscillation multiplies the highest norm by an arbitrarily small constant, which is absorbed in the left side of the first estimate. Lower-order terms, derivatives of coefficients and cutoff commutators are absorbed using the second estimate. Nested cutoffs give the interior \(H^{2d}\) estimate from the \(L^2\) norm and the equation; applying the same calculation to successive derivatives gives all interior Sobolev orders. To spell out the cutoff step, for nested boxes \(B_b\supset B_a\) this calculation gives, on solutions, \(N(B_a)\leq\theta N(B_b)+C_\theta(b-a)^{-A}\|f\|_{L^2(B)}\), where \(N\) is the desired Sobolev norm and \(A\) is fixed. Take increasing boxes with gaps proportional to \(2^{-j}\) and closure still inside \(B\), and choose \(\theta<2^{-A}\). Iteration sums a convergent geometric series; the remaining outer norm is multiplied by \(\theta^j\) and tends to zero because \(f\) is smooth on that fixed closure. This gives the claimed interior bound at each order. The boxes, coefficient bounds and constants are uniform here. Fourier Cauchy–Schwarz then bounds any derivative at their centers by \(C_r\|f\|_{L^2}\) on the larger box, since \(H^s\) controls \(r\) derivatives for \(s>r+1\) in two dimensions.

The given pointwise growth bounds that rescaled \(L^2\) norm by \(C'y_0^N\). Scaled derivatives at the center are precisely the indicated hyperbolic derivatives, up to lower-order terms with bounded coefficients. This proves the claim. The calculation takes place on the upper-half-plane lift, so the shrinking injectivity radius of a cusp does not affect it. \(\square\)

**Lemma — the nonconstant cusp modes.** Under the hypotheses of the preceding lemma, the nonzero Fourier modes of \(f\), and all their real derivatives, decrease faster than every power of \(y\).

**Proof.** Factor \(P\) into powers of its distinct roots. Bézout identities for those coprime powers split \(f\) into a finite sum of functions satisfying \((\Delta_k-\lambda)^d f=0\). They are polynomial differential expressions in the original \(f\), so the preceding lemma gives polynomial growth for them and their derivatives.

For one such function put \(f_j=(\Delta_k-\lambda)^jf\), \(0\leq j<d\), with \(f_d=0\). In a cusp of width \(w\), expand in \(e^{2\pi inx/w}\). If \(a_{j,n}(y)\) is the coefficient, set
\[
t=\log y,\qquad u_{j,n}(t)=e^{-t/2}a_{j,n}(e^t),
\qquad \kappa_n=2\pi n/w.
\]
Direct differentiation of the Fourier equation gives
\[
-u_{j,n}''+
\left(\tfrac14+\kappa_n^2e^{2t}-k\kappa_ne^t\right)u_{j,n}
=\lambda u_{j,n}+u_{j+1,n}.
\]
For \(n\ne0\), write \(u_n=(u_{0,n},\ldots,u_{d-1,n})\) and \(r_n=\|u_n\|\). Wherever \(r_n>0\), differentiating its norm and using Cauchy–Schwarz gives
\[
r_n''\geq
\left(\tfrac14+\kappa_n^2e^{2t}
             -k\kappa_ne^t-|\lambda|-1\right)r_n.
\]
The shift matrix has norm at most one. Choose \(Y=e^{t_0}\) sufficiently large, independently of \(n\ne0\), so the coefficient is at least \(\kappa_n^2e^{2t}/2\). Choose a fixed \(a>0\) small enough that both
\[
h_\pm(t)=\exp(\pm a|\kappa_n|(e^t-Y))
\]
satisfy \(h_\pm''\leq \kappa_n^2e^{2t}h_\pm/2\) for \(t\geq t_0\). This is immediate from their second derivatives once \(a^2<1/2\) and the minimum \(|\kappa_n|Y\) is large.

On \([t_0,T]\), compare \(r_n\) with
\(r_n(t_0)h_-(t)+\eta_T h_+(t)\), where
\(\eta_T=r_n(T)/h_+(T)\). At both endpoints the latter is at least \(r_n\). A positive interior maximum of their difference is impossible: there \(r_n>0\), and the two differential inequalities force its second derivative to be strictly positive. Polynomial growth gives \(\eta_T\to0\). Therefore
\[
|u_{j,n}(t)|
\leq r_n(t_0)\exp(-a|\kappa_n|(e^t-Y)).
\]
The Fourier coefficients at the fixed height \(Y\) are bounded uniformly in \(n\). Summing this geometric bound shows that the nonconstant part of \(f\) is \(O(y^{1/2}e^{-cy})\) for \(y\geq2Y\), with \(c>0\). It satisfies the same polynomial differential equation: averaging in \(x\) commutes with \(\Delta_k\). Applying the local estimates to this nonconstant part on boxes with comparable heights proves rapid decrease of every scaled derivative. Rotation derivatives multiply a weight vector by a fixed integer, and all real group derivatives are combinations of these scaled derivatives. This proves the lemma. \(\square\)

**Lemma — the compact cuspidal resolvent at a fixed weight.** At a fixed finite level, unitary central character and rotation weight \(k\), the cuspidal realization of \(\Delta_k\) is self-adjoint, bounded below, and has compact resolvent. Each polynomial \(P\) has a finite-dimensional kernel there.

**Proof.** Work on the finite principal-congruence cover of Lemma 1.2. Let \(H,S,J_0\) be the real special-linear generators in the modular-lift lesson, with \(J_0\) the rotation derivative. Integration by parts gives the nonnegative form
\[
q_k(u)=\tfrac14(\|R(H)u\|_2^2+\|R(S)u\|_2^2).
\]
Its differential operator is \(\Delta_k+k^2/4\): the Casimir is
\(-\tfrac14(R(H)^2+R(S)^2-R(J_0)^2)\), and \(R(J_0)u=iku\).
In cusp coordinates the form is the integral of
\[
|y\partial_yf|^2+
|y\partial_xf-ikf/2|^2
\]
against \(dx\,dy/y^2\). Its norm, after adjoining a constant times \(\|f\|_2^2\), is equivalent to the ordinary first-derivative form norm.

The cusp projection commutes with the unitary right group action, hence with its closed real generators and their domains. It preserves the fixed level and weight. Thus restricting this closed form to the cusp space gives a reducing closed form. Its domain is dense: the compact approximate identities, followed by weight projection, have smooth cusp images rapidly decreasing with all derivatives by Section 3. This uses only that section's \(L^2\) kernel estimate, not arithmetic finiteness.

Zero cusp average gives the circle Poincaré estimate
\[
\int_{y>R}|f|^2\,\frac{dx\,dy}{y^2}
\leq \frac{w^2}{4\pi^2R^2}
             \int_{y>R}|\partial_xf|^2\,dx\,dy.
\]
Consequently a bounded form ball has uniformly small cusp tails. On a compact core, cut off in finitely many coordinate charts and extend to Euclidean tori. Bounded first-derivative norms make the sum of squared Fourier coefficients outside a frequency ball uniformly small; the coefficients inside it lie in a bounded finite-dimensional set. This proves compactness on the core, and the tail estimate proves compactness of the full form embedding. Finite components, unitary identifications and character phases preserve it.

The form resolvent maps a Hilbert unit ball to a bounded form ball, by Riesz representation. It is therefore compact and self-adjoint. The compact spectral theorem gives finite-dimensional eigenspaces and no finite accumulation of eigenvalues. Subtracting \(k^2/4\) gives the asserted operator \(\Delta_k\). The reducing-form argument, or integration against compact coordinate tests, identifies it with the stated differential operator. A polynomial has only finitely many roots, so its kernel is the finite sum of the corresponding eigenspaces. This extends the weight-zero argument in Section 6 without a representation-theoretic admissibility assumption. \(\square\)

**Theorem — arithmetic finiteness for GL₂ over \(\mathbb Q\).** Fix a compact open finite level \(J\), a finite packet of real compact types, and a cofinite ideal \(I\) in the enveloping centre. The space of automorphic forms fixed by \(J\), of those types, and annihilated by \(I\), is finite dimensional.

**Proof.** A principal congruence cover gives finitely many real congruence components and cusps. The type packet gives finitely many rotation weights. Cofiniteness of \(I\) supplies a nonzero polynomial in the scalar real derivative and one in the Casimir: powers of either generator are linearly dependent modulo \(I\).

We first remove the scalar direction. The positive central variable satisfies a fixed constant-coefficient ordinary differential equation. Its solutions are finite sums \(e^{\lambda t}t^j\), with finitely many \(\lambda,j\). Finitely many evaluations in that variable recover their coefficient functions through an invertible evaluation matrix; linear independence of the exponential polynomials supplies such a matrix. Those coefficient functions retain smoothness, finite level and polynomial growth, and satisfy the fixed Casimir polynomial. The compact central action factors through a finite quotient at the fixed level, so it also gives only finitely many character choices. Extend each coefficient from the norm-one slice using that compact unitary character and trivial positive scalar action. These finite reductions are injective. It therefore suffices to prove finiteness for a fixed unitary central character, component and rotation weight.

Let \(P(\Delta_k)f=0\). At a cusp, the zero Fourier coefficient satisfies
\[
P(-y^2\,d^2/dy^2)a_0(y)=0.
\]
This ordinary equation has order \(2\deg P\), with nonzero leading coefficient for \(y>0\). Its solution space is finite dimensional; equivalently, after \(t=\log y\), it is a constant-coefficient equation. Map \(f\) to this solution at each of the finitely many cusps.

The kernel of this map has zero constant terms. This is the full adelic cuspidal condition: use the period realization of the unipotent integral in Lemma 1.2 at each rational cusp and component. A zero solution in the cusp interval is zero for all positive heights by uniqueness of the ordinary equation, so the integral vanishes for every group argument. The nonconstant-mode lemma then makes \(f\) and all its real derivatives rapidly decreasing. They belong to \(L^2\), and integration by parts, with cutoffs whose tails tend to zero, puts \(f\) in the domain of every required power of the cuspidal operator. Thus \(P(\Delta_k)f=0\) holds in its self-adjoint realization. The compact-resolvent lemma makes this kernel finite dimensional.

The image of the constant-term map lies in a finite sum of finite-dimensional ordinary solution spaces, and its kernel is finite dimensional. Choosing lifts of a basis of its image proves that its domain is finite dimensional. Reassemble the finitely many weights, components and central coefficient functions. This proves the theorem. \(\square\)

This is the rational GL₂ arithmetic finiteness statement used in this course. Harish-Chandra's general theorem, in the formulation of Getz–Hahn, Theorem 6.3.2, remains the original reference; the complete specialized proof needed here has been supplied above.


**Lemma 4.1 — a reproducing kernel.** Every automorphic form \(\phi\) is fixed by some smooth compact convolution: \(\phi=R(f_0)\phi\). All its real derivatives have a common polynomial-growth exponent.

**Proof.** Put \(\phi\) in the finite-dimensional space \(E\) supplied by the arithmetic-finiteness theorem just proved. Take a smooth real approximate identity averaged under conjugation by the real compact group, and at finite places the normalized characteristic function of \(J\). Call these kernels \(h_n\). Convolution preserves the given compact types because it commutes with compact translations; it preserves \(J\)-invariance by bi-\(J\)-invariance, and preserves the central ideal because central differential operators commute with convolution. It preserves moderate growth since its integration variable ranges over a compact set and the group height is submultiplicative. These verifications show \(R(h_n)E\subset E\) without first assuming bounds on derivatives of elements of \(E\).

The restrictions \(R(h_n)|_E\) converge to the identity. Indeed finitely many point evaluations separate the finite-dimensional function space \(E\); approximate-identity convergence at those points proves convergence of every entry of its matrix. Choose \(n\) for which \(A=R(h_n)|_E\) is invertible. Cayley–Hamilton expresses \(A^{-1}=q(A)\) as a polynomial. Then \(\phi=Aq(A)\phi\), a finite linear combination of positive convolution powers of \(h_n\) applied to \(\phi\). Their sum is a smooth compact \(f_0\), proving the identity.

Differentiating that identity differentiates its compact kernel. Each real differential operator \(D\) gives \(D\phi=R(f_D)\phi\) with a smooth compact \(f_D\). Its growth is bounded by the original exponent of \(\phi\), with a new constant depending on \(D\). This also proves stability under Lie differentiation: its compact type packet is finite by the finite adjoint orbit of a differential operator, and the same central ideal annihilates it. Constant terms commute with these derivatives by compact-domain integration. \(\square\)

**Theorem 4.2 — rapid decay.** Every automorphic cusp form is rapidly decreasing on every Siegel set in the central-normalized slice. Every real derivative has the same property. In particular a cusp form with fixed unitary central character belongs to \(H_{\rm cusp}\).

**Proof for unitary central character.** Apply Lemma 4.1 to \(\phi\), and the moderate-growth version of Theorem 3.1 to \(R(f_0)\phi=\phi\). Its exponent \(r\) is fixed, whereas \(B\) can be increased arbitrarily. Thus \(|\phi(g)|\leq C_Ay(g)^{-A}\) for every \(A>0\) on the Siegel set. Applying the same kernel argument to \(f_D\) proves the derivative assertion. The bound on a compact core is automatic. Absolute square integrability follows from finite quotient volume, or directly from the cusp density. Its constant term is zero by assumption, so it lies in \(H_{\rm cusp}\).

**Reduction for the general central-finite case.** We include this step so that rapid decay is not restricted silently to unitary forms. The compact part of \(\mathbb A^\times/\mathbb Q^\times\) is \(\widehat{\mathbb Z}^{\times}\), by the idèle decomposition in the modular-lift lesson. Its central action on a finite-level form factors through a finite quotient. Decompose into its finitely many character spaces. Along the positive real scalar \(e^tI\), the central-finiteness condition is a constant-coefficient differential equation \(p(\partial_t)\phi=0\). Its solutions are finite sums of \(e^{\lambda t}t^j\), with \(\lambda\) a root of \(p\) and \(j\) below its multiplicity. This assertion follows by successively solving \((\partial_t-\lambda)u=0\) and its powers, or by the usual factorization of a constant-coefficient equation.

Put \(\delta(g)=|\det g|_{\mathbb A}^{1/2}>0\), and \(g^1=g/\delta(g)I_\infty\). The product formula makes this construction rational-invariant. On the norm-one slice we can therefore write

\[
\phi(g)=\sum_{\lambda,j}\delta(g)^\lambda\bigl(\log\delta(g)\bigr)^j b_{\lambda,j}(g^1).
\tag{4.1}
\]

The coefficient functions can be obtained from finitely many evaluations at positive central scalars by an invertible exponential-polynomial evaluation matrix. Such a matrix exists because the distinct exponential-polynomial solutions are linearly independent. Hence they retain smoothness, finite compact type, polynomial growth and cuspidality. The latter follows also because unipotent multiplication has determinant norm one. A nonzero polynomial \(q(\Omega)\) belongs to the original cofinite central ideal: powers of \(\Omega\) are linearly dependent modulo that ideal. Central evaluations commute with \(\Omega\), so the same polynomial annihilates every coefficient. This is the required cofinite special-linear infinitesimal ideal.

Extend a coefficient to the whole group by
\(\delta(g)^{i\operatorname{Im}\lambda}b_{\lambda,j}(g^1)\).
It now has a fixed unitary central character: the finite-unit character already has finite order, and the positive scalar has the indicated purely imaginary exponent. It is an automorphic cusp form; its central derivative is scalar and its special-linear central ideal is cofinite. Polynomial growth is preserved because both \(\delta(g)\) and its inverse are bounded by powers of the matrix-and-inverse group height. Apply the unitary case just proved to each coefficient. On the Siegel representatives of Section 1, \(\delta(g)=1\), so (4.1) is a finite sum of rapidly decreasing coefficients. This proves the general case. Derivatives are automorphic cusp forms by Lemma 4.1, so the same reasoning proves their rapid decrease. \(\square\)

The Fourier estimate in Section 3 treats all smooth cusp functions and both nonzero frequency signs. Holomorphicity is not an assumption there. For a holomorphic cusp expansion \(\sum a_ne^{2\pi inz/w}\), a bound at height \(y_0\) gives \(|a_n|\leq C e^{2\pi ny_0/w}\), not a bound on \(a_n\) itself. At heights greater than \(y_0\), the resulting geometric series does give exponential decay. This special argument explains the holomorphic case but does not replace the proof for Maass forms.

## 5. Compact convolution and the representation spectrum

**Theorem 5.1.** Every \(R(f)|_{H_{\rm cusp}}\), for \(f\in C_c^\infty(G(\mathbb A))\), is Hilbert–Schmidt, and hence compact.

**Proof.** The modified kernel of Theorem 3.1 is bounded on the finite-volume quotient, after its finite-level identifications. Its square integral on the product is finite. An integral operator with such a kernel is Hilbert–Schmidt: for an orthonormal basis \((e_j)\), Parseval in the column variable gives

\[
\sum_j\|Te_j\|_2^2
=\int_X\sum_j|\langle K(x,\cdot),\overline{e_j}\rangle|^2dx
=\int_{X\times X}|K(x,y)|^2dx\,dy.
\tag{5.1}
\]

One may first use finite partial sums and then monotone convergence. If the kernel has been constructed on the finite principal cover, apply its finite averages and restrict to the closed subspace representing \(H\). These bounded finite identifications preserve the Hilbert–Schmidt property. The finite-level projection extends the operator by zero on its orthogonal complement, so it is Hilbert–Schmidt on the full cuspidal space as well. Compactness follows by approximating the square-integrable kernel by finite sums of product functions, whose operators have finite rank; their operator norm error is bounded by their kernel \(L^2\) error. \(\square\)

**Theorem 5.2 — discreteness and finite multiplicity.** The right regular representation has a Hilbert direct sum decomposition

\[
H_{\rm cusp}=\widehat\bigoplus_\pi m(\pi)\,\mathcal H_\pi,
\qquad m(\pi)<\infty,
\tag{5.2}
\]

into irreducible unitary adelic representations with central character \(\omega\).

**Proof.** Choose a compact smooth approximate identity \(h_n\) on the group, with shrinking support and integral one. At finite places use normalized compact-open averages. Right convolution converges strongly to the identity in any strongly continuous unitary representation: integrate \(\|R(t)v-v\|\) over its shrinking support. Put \(T_n=R(h_n)^*R(h_n)\). It too converges strongly to the identity. It is positive and compact on \(H_{\rm cusp}\), since its convolution kernel is again smooth compact. Positivity guarantees a nonzero eigenvalue when its restriction to a nonzero invariant closed subspace is nonzero.

Let \(W\ne0\) be such a subspace. Some \(T_n|_W\) is nonzero. Choose a positive eigenvalue \(\lambda\) and its nonzero finite-dimensional eigenspace \(E_\lambda\subset W\). Among the nonzero intersections of \(E_\lambda\) with closed invariant subspaces of \(W\), choose one \(M\) of smallest dimension. Pick \(0\ne v\in M\), and let \(P\) be the closed invariant space generated by \(v\). It is contained in the subspace that supplied \(M\), and \(P\cap E_\lambda\) is nonzero; minimality therefore gives \(P\cap E_\lambda=M\).

If \(Q\) is a closed invariant subspace of \(P\), its orthogonal complement is invariant by unitarity. Their orthogonal projections commute with all group operators, hence with \(T_n\) and its spectral projections. Consequently
\(M=(Q\cap E_\lambda)\oplus(Q^\perp\cap E_\lambda)\).
Every nonzero summand has dimension at least \(\dim M\), so exactly one is nonzero and it is all of \(M\). The cyclic vector \(v\) lies in that summand, forcing \(P\) to lie in the corresponding subspace. Thus \(Q=0\) or \(Q=P\). This proves that every nonzero invariant closed subspace contains an irreducible one.

Choose a maximal orthogonal family of irreducible closed subspaces. The orthogonal complement of their Hilbert sum would, if nonzero, contain another irreducible one, a contradiction. Their sum is all of \(H_{\rm cusp}\). Separability makes the family countable.

Finally fix an irreducible \(\pi\) that occurs. Some positive compact \(T_n\) is nonzero on it, and has a positive eigenvalue there. In every equivalent copy it has that same eigenvalue. Infinitely many copies would give an infinite-dimensional eigenspace of the compact \(T_n\) on \(H_{\rm cusp}\), which is impossible. This proves \(m(\pi)<\infty\). \(\square\)

This argument does not assume that the convolution operators commute. It uses a positive compact approximate identity and the invariant orthogonal complements supplied by unitarity. The statement concerns the cuspidal restriction. The zero mode that we removed is present in the full regular space; the Eisenstein-series lesson will identify the continuous spectrum it produces.

## 6. The modular Laplacian as an example

With trivial central character, at level one and real rotation type zero, cusp vectors are functions on \(\mathrm{SL}_2(\mathbb Z)\backslash\mathbb H\) with zero horocycle averages. Their nonnegative Laplacian is

\[
\Delta=-y^2(\partial_x^2+\partial_y^2),\qquad
q(u)=\int\bigl(|u_x|^2+|u_y|^2\bigr)\,dx\,dy.
\tag{6.1}
\]

**Proposition 6.1.** On this cuspidal subspace the Laplacian has compact resolvent. It has an orthonormal basis of smooth cusp eigenfunctions, with finite-dimensional eigenspaces and eigenvalues tending to infinity if the space is infinite dimensional. A nonzero cusp eigenfunction has positive eigenvalue.

**Proof.** At a cusp of width \(w\), the zero-average circle Poincaré inequality follows immediately from its Fourier coefficients:
\(\int_0^w|u|^2dx\leq(w/2\pi)^2\int_0^w|u_x|^2dx\).
Therefore

\[
\int_{y>Y}|u|^2\frac{dx\,dy}{y^2}
\leq\frac{w^2}{4\pi^2Y^2}\int_{y>Y}|u_x|^2dx\,dy
\leq\frac{w^2}{4\pi^2Y^2}q(u).
\tag{6.2}
\]

A bounded set in the form norm \(\|u\|_2^2+q(u)\) thus has uniformly small tails. On the compact core its \(H^1\) norms in finitely many coordinate charts are bounded, and its \(L^2\) restrictions are precompact. To see this last assertion without an extra compactness theorem, insert chart cutoffs and expand on fixed coordinate boxes in Fourier series. The \(H^1\) bound controls the sum of squared Fourier coefficients weighted by \(1+|n|^2\), so the \(L^2\) tail beyond \(|n|>R\) is \(O(R^{-2})\). The finitely many remaining coefficients have a convergent subsequence. Finite charts and then (6.2) give a convergent subsequence globally. Finite orbifold points can be treated on their finite smooth covers.

The restricted Dirichlet form is closed and densely defined. Closedness follows from the closedness of weak first derivatives in the full form domain. Density follows, for example, by the approximate identities of Section 5 projected to rotation type zero: their smooth cusp outputs are rapidly decreasing by Section 3, with all derivatives, and hence have finite form norm.

We must also identify its operator with the differential Laplacian, rather than infer this from tests restricted to cusp functions. Let \(P_c\) be the orthogonal projection onto the full adelic cuspidal space. Right invariance and unitarity imply that \(P_c\) commutes with every right group translation and with the finite-level and rotation projections. It commutes with the closed infinitesimal generators too: apply it to the difference quotients defining a generator. For
\(H=\operatorname{diag}(1,-1)\) and \(S=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}\), the type-zero Dirichlet form, viewed on the rotation bundle, is

\[
q(u)=\tfrac14\bigl(\|R(H)u\|_2^2+\|R(S)u\|_2^2\bigr).
\tag{6.3}
\]

At rotation zero the two fields are \(2y\partial_y\) and \(2y\partial_x\); changing rotation rotates this pair orthogonally, so (6.3) holds after integration over the normalized rotation fibre. Its weak-derivative domain is precisely the usual first-order form domain in (6.1). Commutation with these generators shows that \(P_c\) preserves that domain and that its range and kernel are orthogonal for both the norm and the form. Thus the restricted form is a reducing part of the full form. If a cusp vector satisfies a weak eigenfunction equation against cusp form-domain tests, it satisfies the same equation against every full form-domain test: decompose that test by \(P_c\), and use form orthogonality for the complementary part. Compactly supported coordinate tests are among these tests. The associated operator is consequently the differential cusp Laplacian.

By Riesz representation in the form Hilbert space, its resolvent \((\Delta+1)^{-1}\) maps the unit ball of \(L^2\) to a bounded form ball. The embedding just proved compact makes that resolvent compact. The compact self-adjoint spectral theorem gives the asserted eigenbasis and finite eigenspaces.

We check smoothness of the weak eigenfunctions locally. On a rectangle in \(\mathbb H\) away from \(y=0\), the equation is the distributional equation
\((\partial_x^2+\partial_y^2)u=-\lambda y^{-2}u\).
Initially \(u\) is locally \(H^1\). For a compact cutoff \(\eta\), the Euclidean Laplacian of \(\eta u\) is in \(L^2\), by the product rule and this equation. The Euclidean Fourier transform then gives \(\eta u\in H^2\), since \((1+|\xi|^2)^2\) is bounded by a constant times \(1+|\xi|^4\). Repeating with nested cutoffs, smooth multiplication by \(y^{-2}\) and the product rule improves local regularity by one derivative at every step. All local Sobolev orders are obtained. Fourier Cauchy–Schwarz makes \(H^m\) embed into \(C^r\) when \(m>r+1\) in two dimensions, so \(u\) is smooth. Its zero average persists from the closed cuspidal condition.

If \(\lambda=0\), the form equation gives \(q(u)=0\), so both derivatives vanish and \(u\) is constant on the connected modular surface. A constant with zero cusp average is zero. Thus nonzero cusp eigenfunctions have positive eigenvalue. \(\square\)

The tail inequality also isolates the role of cuspidality: without the zero-average hypothesis a function constant in \(x\) has no \(x\)-derivative, and (6.2) does not control its escaping mass. The full spectral analysis will retain that channel rather than discard it.

## 7. Exercises with complete solutions

**Exercise 7.1 — Hilbert–Schmidt compactness.** Let \(K\in L^2(Y\times Y)\) on a separable \(L^2\) measure space. Prove that its integral operator is compact. Prove the same assertion for a restriction to a closed invariant subspace.

**Solution 7.1.** Finite sums \(K_m(x,y)=\sum_{j=1}^{r_m}a_j(x)b_j(y)\) are dense in the product \(L^2\) space. This follows by approximating measurable functions by rectangular simple functions, or from the product orthonormal basis. Their integral operators have finite-dimensional ranges. Cauchy–Schwarz in \(y\), followed by integration in \(x\), gives \(\|T_K-T_{K_m}\|_{\rm op}\leq\|K-K_m\|_2\). Thus \(T_K\) is an operator-norm limit of finite-rank operators and is compact. For a closed invariant subspace \(V\), restrict these operators and, if necessary, compose with its orthogonal projection: the finite ranks remain finite and the same norm convergence holds. Formula (5.1), or an orthonormal basis of \(V\) extended to one of the ambient space, also proves the Hilbert–Schmidt bound for the restriction.

**Exercise 7.2 — Siegel representatives.** Deduce a Siegel set for the rational adelic quotient from the positive-real determinant decomposition and the modular fundamental region. Then explain why a deeper finite level requires only finitely many additional cusp charts.

**Solution 7.2.** Write \(g=\gamma g_\infty k_f\) with \(\gamma\in G(\mathbb Q)\), \(g_\infty\) of positive determinant and \(k_f\) in the finite maximal compact. Divide \(g_\infty\) by its positive scalar square root of the determinant and use its Iwasawa coordinates \(s(x+iy)r(\theta)\). An integral rational special-linear matrix reduces \(x+iy\) to the prerequisite fundamental region, so \(|x|\leq1/2\), \(y\geq\sqrt3/2\). Rotations and the finite maximal compact are compact. These representatives give the required Siegel set. A compact open level contains \(K(M)\); the determinant classes modulo \(\det K(M)\) are finite, and its real components have \(\Gamma(M)\). Finitely many cosets of that congruence group in the modular group give finitely many translates of the region. Grouping their upper ends by rational cusp gives precisely the strips of Lemma 1.2, and the truncated parts give a compact core.

**Exercise 7.3 — constant terms and convolution.** For a smooth cusp function, show \(C_N(R(f)\phi)=R(f)(C_N\phi)\). Explain the correct domain of the constant term and extend the identity to \(L^2\) cusp vectors.

**Solution 7.3.** Substitute (1.1) into (1.2). The unipotent quotient and the support of \(f\) are compact, so the smooth integrand is absolutely integrable at each fixed \(g\). Fubini gives
\(\int f(t)\int_{\mathbb Q\backslash\mathbb A}\phi(n(s)gt)ds\,dt\), the required identity. The constant term is a function on the appropriate unipotent quotient, or on the group with its left-unipotent invariance; it is not an ordinary function on the original rational quotient obtained from a global left-unipotent group action. For an \(L^2\) vector, the local bounds in Lemma 1.1 justify Fubini after integration against a compact test function. Thus the identity holds as a distribution, and the convolution has a smooth representative whose constant term is everywhere zero.

**Exercise 7.4 — prove the basic estimate.** Work on a principal congruence cover. Starting with a primitive rational projective matrix and a compact smooth kernel, prove the determinant bound, eliminate nonzero lower-left entries in a high row, and estimate the periodized upper-right sum after removing its zero mode. State the conclusion for arbitrary finite level and unitary central character.

**Solution 7.4.** The primitive integer representative has minimum entry valuation zero at every prime. Compact finite projective support bounds its determinant valuations, and gives valuation zero outside a fixed finite set. Hence its determinant \(D\) belongs to a finite list. In cusp coordinates the lower-left entry of the normalized real argument is \(c\sqrt{yy'}/\sqrt{|D|}\). Since \(c\in\mathbb Z\), \(y'\geq y_0>0\), and real support bounds that entry, all sufficiently large \(y\) force \(c=0\). Now \(ad=D\), so \(a,d\) have finitely many possibilities. Bounding both diagonal entries makes \(y'/y\) range over a compact interval. The finite coefficient of \(b\) is periodic modulo \(L\), by local constancy on the compact family \(b\in\widehat{\mathbb Z}\) and the periodic primitivity condition.

On each progression \(b=r+Lm\), write the real sum as \(\sum_m h((m+t)/Q)\), where \(Q=\sqrt{|D|yy'}/L\) is comparable to \(y\). Poisson summation gives \(Q\sum_n\widehat h(nQ)e^{2\pi int}\). The zero term is independent of the column strip coordinate and integrates to zero against a cusp form. The derivative bounds of the compact smooth family give \(|\widehat h(\xi)|\leq C_B(1+|\xi|)^{-B}\), uniformly in the height ratio and rotations. Thus the remainder is bounded by \(C_BQ^{1-B}\sum_{n\ne0}|n|^{-B}\), for \(B>1\). Increasing \(B\) gives every inverse power of \(y\). Bounded rows meet only bounded columns, where the arithmetic sum is uniformly finite. This proves the bounded modified kernel on the whole fundamental set.

For arbitrary finite level, choose a common principal level fixing the finite kernel on both sides and the finite scalar character. There are finitely many real components and scalar identifications. Summing their estimates and averaging their unitary character phases gives the same bound. By Cauchy–Schwarz it implies \(|R(f)u(g)|\leq C_A y(g)^{-A}\|u\|_2\); by square-integrating the bounded kernel it implies the Hilbert–Schmidt property. These steps supply the full GL₂ argument, including the finite-place and central-character hypotheses.

## References

- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, §§6.2–6.3, 9.2–9.4 and 9.6–9.7. The [author's graduate-text page](https://sites.duke.edu/jgetz/graduate-text/) provides the reference. The general reductive-group basic estimate uses Fourier analysis on unipotent radicals. Here the proof is specialized to primitive GL₂ matrices and real arithmetic progressions.
- P. Deligne, *Formes modulaires et représentations de GL(2)* (1973), §1.3, for the relation between all classical cusp expansions and the adelic constant term.
- The prerequisite adèlic lesson, Theorems 4.1–4.2 and Section 5, for rational determinant decomposition, congruence components and finite quotient volume. The modular fundamental-domain proof belongs to the modular-form prerequisite identified there.
