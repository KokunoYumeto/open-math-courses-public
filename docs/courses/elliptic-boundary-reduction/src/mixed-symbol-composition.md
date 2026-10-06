# Composition of mixed symbols with two different remainder estimates

This lesson proves the two composition assertions on the original mixed symbol spaces, with all four orders real and all position-variable estimates global. It uses the quadratic-multiplier estimates in Sections 7–8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md), the distributional quantization identities of Section 4 of [Two measuring scales, one Weyl product](weyl-metric-products.md) and Section 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md), and the Schwartz operator argument of Sections 3–5 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md). Every metric, weight, parameter, and domain verification needed to apply those results is supplied below. No positive frequency-decay exponent in every direction is assumed merely because the symbols are mixed symbols.

The Fourier convention is
\(\widehat u(\xi)=\int e^{-ix\cdot\xi}u(x)\,dx\), with inverse coefficient \((2\pi)^{-n}\), and \(D_j=-i\partial_j\). Fourier inversion on Schwartz space, its tempered-distribution extension, the corresponding kernel correspondence, ordinary Lebesgue integration and differentiation rules, and the already proved course Gauss theorem are the explicit entry mathematics. The proof does not claim to supply those general foundations again.

## 1. The symbols, their topology, and the exact target

Fix \(n\geq1\) and fixed finite-dimensional complex Hermitian spaces \(E_0,E_1,E_2\). A symbol \(a\) takes values in \(\operatorname{Hom}(E_1,E_2)\), and \(b\) in \(\operatorname{Hom}(E_0,E_1)\); their displayed product is in \(\operatorname{Hom}(E_0,E_2)\). Operator norms are used throughout, so \(\|ab\|\leq\|a\|\|b\|\). Square matrix symbols are included without a change of convention.

Write \(\xi=(\xi',\xi_n)\) and retain

\[
R(\xi)=1+|\xi|,\qquad T(\xi')=1+|\xi'|,
\qquad W_{p,q;\alpha}=R^{p-\alpha_n}T^{q-|\alpha'|}.
\tag{MC1}
\]

For \(n=1\), \(\xi'\in\mathbb R^0\), \(T=1\), and \(\alpha'\) is empty. For every \(p,q\in\mathbb R\), the space \(S^{p,q}\) consists of smooth functions on all of \(\mathbb R_x^n\times\mathbb R_\xi^n\) such that

\[
p_{p,q,L}(f)=\max_{|\alpha|+|\beta|\leq L}
\sup_{x,\xi}\frac{\|\partial_x^\beta\partial_\xi^\alpha f(x,\xi)\|}
{R(\xi)^{p-\alpha_n}T(\xi')^{q-|\alpha'|}}<\infty
\qquad(L\geq0).
\tag{MC2}
\]

No weight is differentiated; the lack of differentiability of \(1+|\xi|\) at the origin is irrelevant to this definition and the estimates below. These seminorms define a Fréchet space: a Cauchy sequence has derivatives uniformly convergent on every compact set; the fundamental theorem of calculus on coordinate segments identifies the successive derivatives of the limit; passing to limits in every weighted bound then gives convergence in (MC2). The product rule gives a continuous bilinear pointwise product \(S^{p,q}\times S^{r,s}\to S^{p+r,q+s}\), because the exponents of each of the two weights add exactly in each Leibniz term. This multiplication preserves the order of the two matrix factors.

**Theorem.** Let \(m,m',\mu,\mu'\in\mathbb R\), \(a\in S^{m,m'}\), and \(b\in S^{\mu,\mu'}\). There is a unique mixed symbol \(c\) representing their left operator composition, and

\[
\begin{gathered}
\operatorname{Op}(a)\operatorname{Op}(b)=\operatorname{Op}(c),
\qquad c\in S^{m+\mu,m'+\mu'},\\
c-ab\in S^{m+\mu,m'+\mu'-1}.
\end{gathered}
\tag{MC3}
\]

The operator equality holds on \(\mathcal S\) and on \(\mathcal S'\), with the continuous extensions constructed below. If in addition

\[
\partial_{\xi_j}a\in S^{m-1,m'}\qquad(1\leq j\leq n),
\tag{MC4}
\]

then the same actual remainder, without changing \(c\), satisfies

\[
c-ab\in S^{m+\mu-1,m'+\mu'}.
\tag{MC5}
\]

Every asserted map has finite input-seminorm bounds. More precisely, for each output order \(L\) some finite \(J\) and \(C_L\), depending only on the fixed orders, dimensions, and derivative order, satisfy

\[
\begin{aligned}
p_{m+\mu,m'+\mu',L}(c)
&\leq C_Lp_{m,m',J}(a)p_{\mu,\mu',J}(b),\\
p_{m+\mu,m'+\mu'-1,L}(c-ab)
&\leq C_Lp_{m,m',J}(a)p_{\mu,\mu',J}(b),\\
p_{m+\mu-1,m'+\mu',L}(c-ab)
&\leq C_L\sum_{j=1}^n p_{m-1,m',J}(\partial_{\xi_j}a)
                         p_{\mu,\mu',J+1}(b)
\quad\text{under (MC4)}.
\end{aligned}
\tag{MC6}
\]

The integer \(J\) can be enlarged to accommodate the finite derivative shifts used in a displayed inequality. No bound requires an infinite collection of seminorms for a fixed output seminorm. Constants in the last line use the actual strengthened seminorms from (MC4); those seminorms are not inferred from the original class.

## 2. Exact comparison with bracket weights and metric symbols

Let \(R_0=(1+|\xi|^2)^{1/2}\), \(T_0=(1+|\xi'|^2)^{1/2}\). Since
\(1+r^2\leq(1+r)^2\leq2(1+r^2)\) for \(r\geq0\), both \(R/R_0\) and \(T/T_0\) lie in \([1,\sqrt2]\). For real \(u=p-\alpha_n\), \(v=q-|\alpha'|\), and \(t_+=\max(t,0)\), \(t_-=\max(-t,0)\), taking the appropriate positive or negative powers gives

\[
2^{-(u_-+v_-)/2}R_0^uT_0^v
\leq R^uT^v
\leq2^{(u_++v_+)/2}R_0^uT_0^v.
\tag{MC7}
\]

For a fixed derivative, division gives the two seminorm comparisons
\(\|f\|_{R,T}\leq2^{(u_-+v_-)/2}\|f\|_{R_0,T_0}\) and
\(\|f\|_{R_0,T_0}\leq2^{(u_++v_+)/2}\|f\|_{R,T}\).
Thus the identity on the same smooth functions is a continuous linear bijection with continuous inverse between the two presentations. It preserves pointwise multiplication, all derivatives, and left quantization, because none of those operations or arguments is changed. It therefore transfers (MC3)–(MC6) with the explicitly displayed constants for each derivative, including all negative orders. In dimension one the factors involving \(v\) can be omitted because \(T=T_0=1\). This is precisely the weight morphism proved in Section 1 of [Inverting mixed symbols without commuting matrix factors](mixed-symbol-inversion.md); it does not replace the original weights silently.

Define the positive quadratic metric and weight on phase space by

\[
g_{(x,\xi)}(v,w)=|v|^2+T(\xi')^{-2}|w'|^2+R(\xi)^{-2}w_n^2,
\qquad M_{p,q}(x,\xi)=R(\xi)^pT(\xi')^q.
\tag{MC8}
\]

The metric definition of \(S(M_{p,q},g)\) uses all multilinear directional derivatives, divided by \(M_{p,q}\) and by the product of the corresponding metric lengths. It equals \(S^{p,q}\) with an exact seminorm comparison. A coordinate direction has length one in an \(x_j\) direction, \(T^{-1}\) in a tangential frequency direction, and \(R^{-1}\) in the normal frequency direction. Hence a coordinate derivative bound follows from the directional bound with constant one. Conversely, for \(g\)-unit directions \(V_1,\ldots,V_k\), expand the derivative in the scaled coordinate frame
\((\partial_{x_1},\ldots,\partial_{x_n},T\partial_{\xi_1},\ldots,T\partial_{\xi_{n-1}},R\partial_{\xi_n})\)
at the fixed observation point. Each vector of coefficients has Euclidean length at most one and sum of absolute values at most \(\sqrt{2n}\). The multilinear expansion is consequently bounded by \((2n)^{k/2}M_{p,q}p_{p,q,k}(f)\). The scales are fixed numbers at that point, so this calculation does not differentiate the metric. We have proved the identity map and its inverse between the two symbol topologies, including the dimension-dependent directional constants.

We verify every structural hypothesis. Both \(R\) and \(T\) are 1-Lipschitz in their respective frequency variables. If \(g_X(Y-X)^{1/2}\leq\epsilon\), then the tangential difference is at most \(\epsilon T_X\), the normal difference at most \(\epsilon R_X\), and the full frequency difference at most \(\sqrt2\epsilon R_X\), since \(T_X\leq R_X\). For \(\epsilon\leq1/4\), both ratios \(R_Y/R_X,T_Y/T_X\) lie between \(1/2\) and \(3/2\). The frequency coefficients of the metrics are therefore comparable with a factor at most four, while the base coefficient remains one. This proves slow variation. Each weight \(R^pT^q\) and its reciprocal is locally comparable with factor at most \(2^{|p|+|q|}\), proving local metric continuity of the weight.

For arbitrary frequencies \(\xi,\eta\), the triangle inequality gives

\[
\max\left(\frac{R(\xi)}{R(\eta)},\frac{R(\eta)}{R(\xi)},
          \frac{T(\xi')}{T(\eta')},\frac{T(\eta')}{T(\xi')}\right)
\leq1+|\xi-\eta|.
\tag{MC9}
\]

For example \(R(\xi)\leq R(\eta)+|\xi-\eta|\leq R(\eta)(1+|\xi-\eta|)\), since \(R(\eta)\geq1\); the other ratios follow in the same way. With the standard symplectic form \(\sigma((v,w),(v_1,w_1))=w\cdot v_1-w_1\cdot v\), direct quadratic duality gives

\[
g_X^\sigma(v,w)=T_X^2|v'|^2+R_X^2v_n^2+|w|^2.
\tag{MC10}
\]

Its displacement term dominates \(|\xi-\eta|^2\), at either base point. Combining (MC9) with \((1+d)^2\leq2(1+d^2)\) proves
\(g_Y\leq2g_X(1+g_Y^\sigma(X-Y))\)
and
\(M_{p,q}(Y)\leq2^{(|p|+|q|)/2}M_{p,q}(X)(1+g_Y^\sigma(X-Y))^{(|p|+|q|)/2}\).
The same estimates apply to reciprocal weights. These are the exact symplectic temperateness conditions, with finite exponents and constants for every real \(p,q\).

The uncertainty parameter \(h_g=\sup(g/g^\sigma)^{1/2}\) is \(T^{-1}\) if \(n\geq2\), because \(T\leq R\), and is \(R^{-1}\) if \(n=1\). It is at most one. Thus the same-metric instance of Section 7 of [Two measuring scales, one Weyl product](weyl-metric-products.md) applies without a missing compatibility condition: Section 3 of [Two measuring scales, one Weyl product](weyl-metric-products.md) proves that the cross tests are automatic when both metrics equal the same symplectically temperate metric. It yields the Weyl symbol product with remainder in \(S(M_{m,m'}M_{\mu,\mu'}h_g,g)\). This confirms the metric meaning of the first gain. That theorem alone only established the operator product for Schwartz symbols; Section 6 below proves the required common-domain identity for the present global mixed symbols. The stronger gain in (MC5) needs the parameter argument below rather than an assertion about the ordinary value of \(h_g\).

## 3. A uniform quadratic multiplier on the transformed variables

Use \(z=(y,\eta)\in\mathbb R^{2n}\), with the same metric (MC8), now based on \(\eta\). For the Fourier-dual variables \((p_y,p_\eta)\), set

\[
A_t(p_y,p_\eta)=t\,p_y\cdot p_\eta,\qquad
T_t=\exp(i t\langle D_y,D_\eta\rangle),\qquad -1\leq t\leq1.
\tag{MC11}
\]

The symmetric map for this quadratic form is \(t/2\) times the swap of the two blocks. For \(t\ne0\), the phase-dual form in the convention of Section 1 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) is therefore

\[
g_z^{A_t}(v,w)=\frac4{t^2}
\left(T(\eta')^2|v'|^2+R(\eta)^2v_n^2+|w|^2\right),
\qquad
h_t(z)=\begin{cases}|t|/(2T(\eta')),&n\geq2,\\|t|/(2R(\eta)),&n=1.\end{cases}
\tag{MC12}
\]

Indeed substituting the swap into \(g_z(B(p_y,p_\eta))\) gives
\(t^2(|p_\eta|^2+T^{-2}|p_y'|^2+R^{-2}p_{y,n}^2)/4\);
dualizing this diagonal positive form gives the first formula. The second is its maximal coordinate ratio with (MC8). Thus \(g_z\leq g_z^{A_t}\).

The dual displacement in (MC12) dominates \(4|\eta-\zeta|^2\) for every \(0<|t|\leq1\). Consequently the very same ratio estimate (MC9) proves both conditions G13 of Section 5 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) uniformly in \(t\), globally at every observation point \(z\). The metric exponent can be one and the weight exponent \((|p|+|q|)/2\); the constants in the preceding section remain valid. Slow variation and local weight continuity do not depend on \(t\) at all. At \(t=0\) the multiplier is the identity, treated directly rather than through a zero positive weight.

Apply Sections 7–8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) with \(E_0=\mathbb R^{2n}\) and weight \(R(\eta)^pT(\eta')^q\). Their constants and finite derivative orders depend only on the structural constants and dimension, which have just been made uniform for \(0<|t|\leq1\). In each fixed output seminorm this gives

\[
\begin{aligned}
p_{p,q,L}(T_tu)&\leq C_Lp_{p,q,J_L}(u),\\
p_{p,q,L}(T_tu-u)&\leq C_L|t|p_{p,q,J_L}(u),\\
p_{p,q,L}(T_tu-u-it\langle D_y,D_\eta\rangle u)
&\leq C_Lt^2p_{p,q,J_L}(u).
\end{aligned}
\tag{MC13}
\]

The second and third follow from their sharper remainder weights \(M h_t\) and \(M h_t^2\), using \(h_t\leq|t|/2\). The directional-to-coordinate comparison from Section 2 supplies exactly the seminorms written here. All three bounds include \(t=0\) by their direct identities. To pass the scalar Gauss estimate to matrices, apply it to each scalar function \(\langle u(\cdot)v,w\rangle\) for fixed unit vectors \(v,w\) in the corresponding Hermitian spaces. Each of its derivative seminorms is bounded by the matrix seminorm. Taking the supremum over those vectors gives the operator-norm estimate, with the same constant. This proves the finite-dimensional extension without interchanging matrix factors.

For precision about the meaning of this extension, any mixed symbol has polynomial growth in \(\eta\), uniformly in \(y\), and hence defines a tempered distribution. Choose smooth compact cutoffs \(\chi_y,\chi_\eta\), both equal to one near the origin, and multiply by \(\chi_y(y/j)\chi_\eta(\eta/j)\) for integers \(j\geq1\). They remain in a bounded mixed-symbol set. To verify this, a frequency cutoff derivative with multiindex \(\alpha\) has magnitude at most a fixed derivative constant times \(j^{-|\alpha|}\) and is supported where \(|\eta|\leq Cj\), for a fixed \(C\). On that support,
\(R^{\alpha_n}T^{|\alpha'|}\leq(1+C)^{|\alpha|}j^{|\alpha|}\),
so its magnitude is at most its fixed constant times \(R^{-\alpha_n}T^{-|\alpha'|}\). The zero-order cutoff is bounded as well. Base cutoff derivatives are uniformly bounded because \(j^{-1}\leq1\). The product rule proves every required seminorm bound. These approximants converge locally smoothly and in tempered distributions, the latter by their common polynomial bound and the rapid decrease of any Schwartz test function. Their Gauss limits converge locally smoothly by Section 7 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md), while their quadratic multipliers converge in tempered distributions because that Fourier multiplier acts continuously there. The two limits agree as distributions on each compact set and hence globally. Thus \(T_t\) here is exactly its distributional Fourier multiplier, not an unrelated extension.

It follows that \(T_sT_t=T_{s+t}\) whenever the parameters in use are finite; for \(|s|,|t|,|s+t|\leq1\), all three maps have the bounds already proved. In particular, for small \(h\),
\(T_{t+h}u-T_tu=T_t(T_hu-u)\), using bounds on a fixed finite parameter interval if an endpoint is crossed. The same computation (MC12) with \(|t|\leq2\) still gives \(h_t\leq1\) and uniform structural constants, so no new theorem is needed at the endpoints. Equations (MC13) give continuity and, from the third bound, differentiation in the Fréchet symbol topology:

\[
\frac{d}{dt}T_tu=T_t\bigl(i\langle D_y,D_\eta\rangle u\bigr).
\tag{MC14}
\]

The differentiation is valid in every output seminorm; each estimate uses only finitely many input seminorms. This proves parameter continuity at zero and the uniform bounds required for integration over the entire closed parameter interval.

## 4. The parameter-dependent product before restricting to the diagonal

Define

\[
F(x,\xi;y,\eta)=a(x,\eta)b(y,\xi),\qquad
\mathcal B_t(x,\xi;y,\eta)=T_t^{(y,\eta)}F(x,\xi;y,\eta).
\tag{MC15}
\]

Here \((x,\xi)\) are parameters, and \(T_t\) acts only on the indicated \((y,\eta)\) variables. At fixed parameters the transformed-variable weight is
\(R(\eta)^mT(\eta')^{m'}R(\xi)^\mu T(\xi')^{\mu'}\).
The last two factors are positive constants with respect to the transformed variables, so they do not change any metric or weight structural constant. Product differentiation in the transformed variables gives derivatives of \(a\) in \(\eta\) followed by derivatives of \(b\) in \(y\), with the displayed matrix order unchanged. Thus all source seminorms required by Section 3 are bounded by a finite product of seminorms of \(a,b\).

The exact pre-diagonal derivative estimate, for arbitrary multiindices \(\alpha,\beta,\gamma,\delta\), is

\[
\begin{split}
&\|\partial_x^\beta\partial_\xi^\alpha
     \partial_\eta^\gamma\partial_y^\delta\mathcal B_t(x,\xi;y,\eta)\|\\
&\quad\leq C\,p_{m,m',J}(a)p_{\mu,\mu',J}(b)
R(\eta)^{m-\gamma_n}T(\eta')^{m'-|\gamma'|}
R(\xi)^{\mu-\alpha_n}T(\xi')^{\mu'-|\alpha'|},
\qquad 0\leq t\leq1.
\end{split}
\tag{MC16}
\]

To prove every part of this estimate, commute \(\partial_y^\delta\partial_\eta^\gamma\) with the constant-coefficient multiplier, first for compactly supported functions and then by its distributional continuity. Their application to \(F\) gives exactly
\((\partial_x^\beta\partial_\eta^\gamma a)(x,\eta)
(\partial_y^\delta\partial_\xi^\alpha b)(y,\xi)\), with the matrix product in its original order. The first factor has transformed weight \(R(\eta)^{m-\gamma_n}T(\eta')^{m'-|\gamma'|}\); the second has the fixed parameter factor in (MC16), with no cost for its \(\delta\) base derivatives. Apply (MC13) with those exact shifted real exponents, using Section 2 for coordinate derivatives if needed. This proves (MC16).

The parameter derivatives in (MC16) are actual derivatives, not formal labels. On any compact parameter set, the map \((x,\xi)\mapsto F(x,\xi;\cdot,\cdot)\) is smooth into the Fréchet space with weight \(R(\eta)^mT(\eta')^{m'}\). For example Taylor's formula in one parameter with its integral remainder, measured in any source seminorm, bounds the difference-quotient error by \(|h|\) times a finite supremum of the corresponding next two parameter derivatives on a compact parameter neighborhood. Those derivative bounds follow directly from (MC2); the fixed \(\xi\) factors are bounded there. Induction over derivatives proves the smoothness assertion. Continuous linear application of \(T_t\) therefore commutes with all parameter derivatives. The uniform estimates (MC13) and the same argument give joint local continuity of every such derivative with respect to \(t\), including \(t=0\). They also justify (MC14) with parameters present.

Set

\[
C_t(a,b)(x,\xi)=\mathcal B_t(x,\xi;x,\xi),\qquad
c=C_1(a,b),\qquad C_0(a,b)=ab.
\tag{MC17}
\]

Differentiation of the diagonal restriction replaces each base derivative by \(\partial_x+\partial_y\) and each frequency derivative by \(\partial_\xi+\partial_\eta\). Expand these sums with their binomial coefficients. For a total frequency derivative \(\kappa=\alpha+\gamma\), the exponents in (MC16) add on the diagonal to
\(m+\mu-\kappa_n\) and \(m'+\mu'-|\kappa'|\). The total base derivative causes no weight cost. There are finitely many terms, each bounded by (MC16), so

\[
\sup_{0\leq t\leq1}p_{m+\mu,m'+\mu',L}(C_t(a,b))
\leq C_Lp_{m,m',J}(a)p_{\mu,\mu',J}(b).
\tag{MC18}
\]

The same argument proves bounded-set local smooth continuity of these products in both factors, by the corresponding Gauss property and the locally uniform derivative bounds. For fixed inputs the parameter curve is also continuous in every target symbol seminorm: apply the semigroup identity and the second bound in (MC13) to each of the differentiated terms used in (MC16), obtaining a bound \(C_L|t-s|p_{m,m',J}(a)p_{\mu,\mu',J}(b)\) for the target seminorm of \(C_t(a,b)-C_s(a,b)\). The unchanged parameter weight factors cancel exactly as in (MC18). This works for arbitrary shifted orders as well, so it supplies continuity in every remainder space used below. The bounded-input local continuity assertion does not assert compact-support density in the full symbol topology.

## 5. The exact first remainder and both distinct order gains

Apply (MC14) to (MC15). Since the derivatives in \(y\) only hit \(b\) and those in \(\eta\) only hit \(a\), the convention \(D=-i\partial\) gives the exact identity

\[
i\langle D_y,D_\eta\rangle F
=\sum_{j=1}^n(\partial_{\eta_j}a)(x,\eta)
                 (D_{y_j}b)(y,\xi).
\tag{MC19}
\]

Indeed \(i(-i)(-i)=-i\), the coefficient of the derivative on \(b\) in the right side. The fundamental theorem of calculus in (MC14), followed by the diagonal restriction, therefore yields

\[
c-ab=\sum_{j=1}^n\int_0^1 C_t(\partial_{\xi_j}a,D_{x_j}b)\,dt.
\tag{MC20}
\]

The integral is an integral of smooth functions with derivatives locally uniformly continuous in \(t\), and all symbol seminorms have uniform majorants. Its coordinate derivatives can consequently be taken under the integral, and integration of each uniform bound proves the corresponding symbol estimate. Equivalently, Riemann sums converge in each relevant seminorm by the parameter continuity already proved and completeness; (MC20) has the same value by pointwise convergence. Thus no parameter endpoint or interchange of derivatives with an unestimated oscillatory integral is left implicit.

For \(j<n\), the original definition gives \(\partial_{\xi_j}a\in S^{m,m'-1}\) with exact derivative seminorm identities. For \(j=n\), it gives \(\partial_{\xi_n}a\in S^{m-1,m'}\). The latter space embeds continuously in \(S^{m,m'-1}\) with constant one for every identical derivative: the ratio of its derivative weight to the latter weight is \(T/R\leq1\). Each \(D_{x_j}b\) is in \(S^{\mu,\mu'}\), with one extra source derivative and a scalar of modulus one. Apply (MC18) to every summand of (MC20) in these spaces. The resulting weight is \(R^{m+\mu}T^{m'+\mu'-1}\), proving the second assertion of (MC3) and the second line of (MC6).

Under (MC4), every summand instead has its first factor in \(S^{m-1,m'}\). Applying exactly the same uniform product theorem now yields \(R^{m+\mu-1}T^{m'+\mu'}\), proving (MC5) and the third line of (MC6). These two results concern the same exact expression (MC20). For \(n=1\), the tangential factor is one, so the first remainder statement does not assert a gain; (MC4) then follows automatically from the normal derivative rule and gives the actual one-order gain in the only frequency variable.

Here is also the physical-space Taylor identity requested by the composition problem, with its sign and parameter dependence connected to (MC20). For Schwartz inputs, Fourier inversion for (MC11), or evaluation on Fourier exponentials followed by their absolutely convergent Fourier superposition, gives for \(t>0\)

\[
C_t(a,b)(x,\xi)=(2\pi)^{-n}
\operatorname{Os}\iint e^{-iz\cdot\eta}
a(x,\xi+\eta)b(x+t z,\xi)\,dz\,d\eta.
\tag{MC21}
\]

The kernel before the substitution \(y=x+t z\) is
\((2\pi t)^{-n}e^{-i(y-x)\cdot(\zeta-\xi)/t}\), and its Jacobian \(t^n\) cancels that coefficient to give (MC21). The normalization and sign can be checked on \(e^{i(p_y\cdot y+p_\eta\cdot\eta)}\): the resulting factor is \(e^{itp_y\cdot p_\eta}\), exactly (MC11). At \(t=0\), the Fourier delta identity in \(z\) gives the product \(ab\). For general mixed inputs the notation \(\operatorname{Os}\) in (MC21) means the unique bounded-set limit of these Gauss evaluations, whose existence, derivative bounds, and continuity including \(t=0\) were proved in Sections 3–4. It does not denote an unproved ordinary double integral.

For all points \(x,y,\xi\), ordinary Taylor integration gives precisely

\[
b(x,\xi)-b(y,\xi)
=\sum_j(x_j-y_j)\int_0^1
\partial_{x_j}b(y+s(x-y),\xi)\,ds.
\tag{MC22}
\]

Subtracting \(ab\) from the \(t=1\) formula and writing the opposite difference produces
\(b(x+z,\xi)-b(x,\xi)=\sum_jz_j\int_0^1\partial_{x_j}b(x+t z,\xi)\,dt\), after reversing the segment parameter if starting from (MC22). Since \(z_je^{-iz\cdot\eta}=i\partial_{\eta_j}e^{-iz\cdot\eta}\), integration by parts places \(-i\partial_{\eta_j}\) on the first factor, and hence \(D_{x_j}=-i\partial_{x_j}\) on the second in the final displayed product. This recovers (MC20) with the first factor \(\partial_{\xi_j}a\) on the left. For general mixed symbols, this manipulation is justified by the already proved multiplier identity (MC14) and its bounded approximations; (MC18) is the uniform estimate for the entire Taylor parameter family. Thus the spatial Taylor route and the quadratic-multiplier route are the same proved map, with no unproved parameter-dependent composition assumption.

## 6. The operator identity on its full stated domain

For any mixed symbol \(a\), every derivative has polynomial frequency growth uniformly in \(x\). For example \(R^mT^{m'}\leq R^{m_++m'_+}\), and differentiation only lowers these exponents. Define left quantization on vector-valued Schwartz functions by

\[
\operatorname{Op}(a)u(x)=(2\pi)^{-n}\int
e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi.
\tag{MC23}
\]

This integral and all its base derivatives are absolutely convergent. To control a Schwartz seminorm \(\sup_x\|x^\gamma\partial_x^\beta\operatorname{Op}(a)u(x)\|\), first expand \(\partial_x^\beta\), which produces only finitely many base derivatives of \(a\) and polynomial frequency factors. Transfer \(x^\gamma\) from the exponential by integration by parts in \(\xi\). Each term contains finitely many derivatives of \(a\), one polynomial, and a derivative of \(\widehat u\). Choose a Schwartz seminorm of \(\widehat u\) whose negative weight exceeds the polynomial growth plus \(n+1\); the integrand is then bounded by a constant times an integrable negative power of \(R\), uniformly in \(x\). Boundary terms vanish by that same decay. This proves a finite-seminorm bound and continuity \(\operatorname{Op}(a):\mathcal S(E_1)\to\mathcal S(E_2)\), jointly in the symbol and the input. This is the proof of Section 3 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) applied to the actual polynomial bounds here; it does not place the mixed class inside an inapplicable classical positive-\(\rho\) symbol class.

For Schwartz symbols, Fubini applied to the two Fourier integrals, as in Section 5 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md), gives the left composition symbol

\[
c(x,\xi)=(2\pi)^{-n}\iint
e^{i(x-y)\cdot(\eta-\xi)}a(x,\eta)b(y,\xi)\,dy\,d\eta
=C_1(a,b)(x,\xi).
\tag{MC24}
\]

Absolute convergence holds for these symbol inputs in the relevant integrations. Equation (MC24) is also (MC21) at \(t=1\), by \(z=y-x\) and the frequency shift. The phase is therefore the left-quantization phase, not the Weyl phase.

Choose smooth compact cutoffs in both variables tending to one, and let \(a_k,b_k\) be their products with \(a,b\). The cutoff bounds proved in Section 3 show that the symbols remain bounded in their original mixed classes and converge locally smoothly. Their products \(c_k=C_1(a_k,b_k)\) remain bounded in the target mixed class and converge locally smoothly to \(c\), by Section 4. For any fixed \(u\in\mathcal S\), the operators of all three sequences converge on \(u\) in Schwartz space. To see this explicitly, their integrals and derivatives converge locally in \(x\) by dominated convergence and the uniform polynomial bounds. The preceding Schwartz estimates uniformly bound every output Schwartz seminorm. Outside a large base ball, a seminorm with one higher power of \(1+|x|\) makes the tail uniformly small; inside that ball the local smooth convergence applies. This proves convergence in each Schwartz seminorm.

Joint continuity also controls the varying inner input in a product: for every target Schwartz seminorm, the uniformly bounded symbols \(a_k\) give a common finite collection of input seminorms. Thus
\(\operatorname{Op}(a_k)(\operatorname{Op}(b_k)u-\operatorname{Op}(b)u)\to0\),
while \((\operatorname{Op}(a_k)-\operatorname{Op}(a))\operatorname{Op}(b)u\to0\).
Passing to the limit in the Schwartz-symbol identities proves (MC3) as an operator identity on \(\mathcal S\).

We also supply the adjoint domain needed for \(\mathcal S'\). The distributional kernel identity proved in Section 3 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md), equation E13, gives

\[
a^\dagger=\exp(i\langle D_x,D_\xi\rangle)(a^*),
\qquad
\langle\operatorname{Op}(a)u,v\rangle
=\langle u,\operatorname{Op}(a^\dagger)v\rangle
\quad(u,v\in\mathcal S),
\tag{MC25}
\]

with inner products linear in the first variable. That identity is an identity of tempered kernels and applies to our polynomially growing symbols. The multiplier in (MC25) is exactly (MC11) at \(t=1\), on the full \((x,\xi)\) phase space with (MC8), so Section 3 proves \(a^\dagger\in S^{m,m'}\). Its Schwartz action is continuous by (MC23). Transposition of that action, using the adjoint pairing, therefore defines a continuous action of \(\operatorname{Op}(a)\) on \(\mathcal S'\). It agrees with (MC23) on Schwartz functions by (MC25).

The identity on \(\mathcal S\) implies that the adjoint of \(\operatorname{Op}(c)\) there equals the reversed composition of these continuous Schwartz adjoints: test it against two arbitrary Schwartz functions and use (MC25) twice. Transposing that identity proves \(\operatorname{Op}(a)\operatorname{Op}(b)=\operatorname{Op}(c)\) on \(\mathcal S'\). Both compositions are defined because each factor is continuous on the indicated common domain.

Finally, the left symbol-to-kernel map is injective: take the partial inverse Fourier transform in \(\xi\) and then the invertible linear substitution \(z=x-y\), as in Section 3 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md), E12. Reversing these two operations recovers the symbol distribution uniquely from the kernel. The tempered kernel correspondence identifies the operator with its kernel; hence another symbol giving the same operator has the same kernel and is equal to \(c\). This proves the claimed uniqueness. The same argument shows that this left composition is associative and has the constant identity matrix as its unit whenever the matrix sizes are compatible, although neither fact is needed for the remainder estimates.

There is an exact map to the already proved Weyl product, not merely a similarity of its estimates. On full phase space write \(Q_s=\exp(is\langle D_x,D_\xi\rangle)\), and put \(a_W=Q_{-1/2}a\), \(b_W=Q_{-1/2}b\). Section 3 makes each \(Q_s\), for the parameters used here, a continuous bijection of every mixed class with inverse \(Q_{-s}\). The kernel quantization identity Section 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md), W40, gives \(\operatorname{Op}_{1/2}(a_W)=\operatorname{Op}_0(a)\), with that exact negative half-parameter. The identity for \(b\) is the same. We then have

\[
C_1(a,b)=Q_{1/2}\bigl((Q_{-1/2}a)\mathbin{\#}(Q_{-1/2}b)\bigr).
\tag{MC25a}
\]

For Schwartz symbols this follows from the proved Weyl product identity and W40, followed by left-kernel injectivity. For arbitrary mixed symbols, take the compact approximants already used above. Their \(Q_{-1/2}\) images are Schwartz, remain bounded in their exact mixed classes, and converge locally smoothly to \(a_W,b_W\), by the Gauss theorem. Section 7 of [Two measuring scales, one Weyl product](weyl-metric-products.md) gives bounded local smooth convergence of their Weyl products in the metric class identified in Section 2. Applying \(Q_{1/2}\), and comparing with the bounded local limit of \(C_1(a_k,b_k)\), proves (MC25a) for the actual symbols. This argument proves the exact correspondence before invoking any operator-composition claim for arbitrary metrics.

It also gives a second proof of the first remainder estimate. The Gauss remainder at parameter \(\pm1/2\) gives \(a_W-a\in S^{m,m'-1}\), \(b_W-b\in S^{\mu,\mu'-1}\), and \((Q_{1/2}-I)f\in S^{p,q-1}\) for \(f\in S^{p,q}\); in dimension one the proved normal gain embeds in those statements. The Weyl theorem gives \(a_W\#b_W-a_Wb_W\in S^{m+\mu,m'+\mu'-1}\). In (MC25a), split the difference from \(ab\) into
\(Q_{1/2}(a_W\#b_W-a_Wb_W)+(Q_{1/2}-I)(a_Wb_W)+(a_W-a)b_W+a(b_W-b)\).
Each term has the claimed lower tangential order by the already proved product and quantization bounds, and the factors remain in their given order. The stronger remainder continues to follow from (MC20), which keeps the improvement on the first factor's frequency derivatives. Thus the left construction and the existing Weyl calculus are related by a proved, explicit quantization isomorphism on the full classes used here.

## 7. An exact product showing the necessity of the stronger hypothesis

For a fixed \(v\in\mathbb R^n\), a constant matrix \(B\), and a frequency-dependent symbol \(a(\xi)\), Fourier modulation gives the exact identity

\[
C_1(a,e^{iv\cdot x}B)(x,\xi)=e^{iv\cdot x}a(\xi+v)B.
\tag{MC26}
\]

Indeed the Fourier transform of \(e^{iv\cdot x}Bu(x)\) is \(B\widehat u(\xi-v)\); substitution into (MC23) and a frequency translation give (MC26) on Schwartz inputs, then kernel injectivity gives the symbol identity. This verifies the sign of the frequency shift as well as the matrix order.

Take \(n\geq2\), scalar symbols, and a smooth function \(\kappa\) on \(\mathbb R^{n-1}\) equal to one on \(|\zeta|\leq1/2\), equal to zero on \(|\zeta|\geq1\), and between zero and one. For a completely specified construction, put \(h(s)=e^{-1/s}\) for \(s>0\) and zero for \(s\leq0\), and set
\(\kappa(\zeta)=h(1-|\zeta|^2)/(h(1-|\zeta|^2)+h(|\zeta|^2-1/4))\).
The denominator is positive because its two positive regions cover all possible \(|\zeta|^2\). All derivatives of \(h\) from the right at zero are polynomial powers of \(s^{-1}\) times \(e^{-1/s}\), and tend to zero, so the function and cutoff are smooth. Define

\[
\varphi(\zeta)=\tfrac12\zeta_1\kappa(\zeta),\qquad
a(\xi)=2+\varphi(\xi'),\qquad
b(x,\xi)=e^{ix_1/4},\qquad v=\tfrac14 e_1.
\tag{MC27}
\]

Both symbols belong to \(S^{0,0}\). For \(a\), positive tangential derivatives are compactly supported in \(\xi'\), positive normal derivatives vanish, and every position derivative vanishes; these facts verify every estimate (MC2), while \(|a|\leq5/2\). For \(b\), all position derivatives are bounded and all positive frequency derivatives vanish.

Equation (MC26) gives
\(c-ab=e^{ix_1/4}(\varphi(\xi'+e_1/4)-\varphi(\xi'))\).
This is in \(S^{0,-1}\): every tangential derivative has fixed compact tangential support, every normal derivative vanishes, and all position derivatives are uniformly bounded, so each of its defining weighted suprema is finite. At \(\xi'=0\), its value is exactly \(e^{ix_1/4}/8\), independently of \(\xi_n\). Membership in \(S^{-1,0}\) would require \(1/8\leq C/(1+|\xi_n|)\) for all \(\xi_n\), which is impossible. The strengthened hypothesis fails as well, since \(\partial_{\xi_1}a(0,\xi_n)=1/2\) is independent of \(\xi_n\). Thus the first remainder theorem cannot be replaced by the stronger one without its actual extra assumption.

## 8. Solved exercise with noncommuting matrices and a sharp total-order gain

**Exercise.** Let
\(A=\begin{pmatrix}0&1\\0&0\end{pmatrix}\),
\(B=\begin{pmatrix}0&0\\1&0\end{pmatrix}\),
and for any \(n\geq1\) set \(a(x,\xi)=\xi_n^2A\), \(b(x,\xi)=e^{ix_n}B\).
Verify all hypotheses with \((m,m',\mu,\mu')=(2,0,0,0)\), compute \(c\) and its exact remainder, and determine whether the improved remainder can be lowered to \(S^{1-\epsilon,0}\) for any \(\epsilon>0\).

**Solution.** Since \(\|A\|=\|B\|=1\), \(\|a\|\leq R^2\); its only nonzero positive frequency derivatives are \(\partial_{\xi_n}a=2\xi_nA\) and \(\partial_{\xi_n}^2a=2A\), with bounds \(2R\) and \(2\). Every tangential or position derivative vanishes. Thus \(a\in S^{2,0}\). Its normal first derivative lies in \(S^{1,0}\) by those same two bounds, and all other first frequency derivatives are zero, so (MC4) holds. Every position derivative of \(b\) has norm at most one and every positive frequency derivative vanishes, proving \(b\in S^{0,0}\).

Here \(AB=\operatorname{diag}(1,0)\), whereas \(BA=\operatorname{diag}(0,1)\). From (MC26),

\[
c=e^{ix_n}(\xi_n+1)^2AB,\qquad
ab=e^{ix_n}\xi_n^2AB,\qquad
c-ab=e^{ix_n}(2\xi_n+1)AB.
\tag{MC28}
\]

The remainder belongs to \(S^{1,0}\): its value is bounded by \(3R\), its sole nonzero frequency derivative is \(2e^{ix_n}AB\) in the normal direction, all higher frequency derivatives vanish, and every position derivative has the same magnitude bounds. The formula also keeps the original matrix product \(AB\); replacing it by \(BA\) would give a different operator and a different symbol.

Along \(\xi'=0\) and \(\xi_n\to+\infty\), the zero-order ratio for \(S^{1-\epsilon,0}\) is
\((2\xi_n+1)/(1+\xi_n)^{1-\epsilon}\), which diverges. To verify divergence without an asymptotic abbreviation, for \(\xi_n\geq1\), \(2\xi_n+1\geq1+\xi_n\), so that ratio is at least \((1+\xi_n)^\epsilon\to\infty\). Thus no such better order is guaranteed. Finally \(D_{x_n}b=b\), so the first correction from (MC19) is \(2\xi_ne^{ix_n}AB\); the constant term in (MC28) is the next polynomial correction. This independently checks the signs against the differential product rule. The improved one-order remainder estimate is sharp in total frequency order on this example.

## Prerequisites

Prerequisites are Sections 7–8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) for quadratic multiplier bounds; Sections 3, 4, 7 and 8 of [Two measuring scales, one Weyl product](weyl-metric-products.md) for metric products and quantization; Section 3 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) for tempered kernels; and Section 1 of [Inverting mixed symbols without commuting matrix factors](mixed-symbol-inversion.md) for the two frequency-weight conventions. Section 6 proves the Schwartz and tempered-distribution operator arguments used here.

## References

