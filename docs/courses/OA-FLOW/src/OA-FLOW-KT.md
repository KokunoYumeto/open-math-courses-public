# The KMS strip and a complete analytic finite-star core

*Fresh local reconstruction, GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

Let \(\varphi\) be a faithful normal semifinite weight on an arbitrary von Neumann algebra \(M\). There is no separability hypothesis. Use the linear-first GNS inner product, \(N=\mathfrak n_\varphi\), \(A=N\cap N^*\), the finite linear extension \(\varphi_0\), and the recovered closed operator \(S=J\Delta^{1/2}\), with \(S\Lambda(x)=\Lambda(x^*)\) on \(A\). Write \(U_t=\Delta^{it}\) and \(\sigma_t=\sigma_t^\varphi\).

The actual inputs are [GW-1–5](OA-FLOW-GW.md#oa-flow.gw.1), [WR-3–5](OA-FLOW-WR.md#wr-3), [MW-4](OA-FLOW-MW.md#mw-4), the normal-weight bounded graph and lower semicontinuity in [EW-2–3](OA-FLOW-EW.md#ew-2) with [the required normality hypothesis](OA-FLOW-EW.md#ew-2), [CP01–06](OA-FLOW-CP.md#oa-flow.cp.1), [SF, SB-0–6 and SF-3–4](OA-FLOW-SF.md#oa-flow.sf.sf0), and [FF-1](OA-FLOW-FF.md#oa-flow.ff.2) with its precisely linked scalar foundations. All uses of unbounded powers below refer to the actual spectral calculus with domains, not a formal complex power rule.

For free human context see [Hiai, §2.2 and §7.1(C), printed pp.17–19 and 64](https://arxiv.org/pdf/2004.02383v1). The local proofs below reconstruct the spectral, integral and domain steps; the assertions and omitted details in the notes are not imported as proofs. The first theorem is existence of the KMS strip. Uniqueness of the automorphism group is a separate theorem.

Actual earlier proof ranges: [OA-FLOW.GW.1](OA-FLOW-GW.md#oa-flow.gw.1), [OA-FLOW.GW.2](OA-FLOW-GW.md#oa-flow.gw.2), [OA-FLOW.GW.3](OA-FLOW-GW.md#oa-flow.gw.3), [OA-FLOW.GW.4](OA-FLOW-GW.md#oa-flow.gw.4), [OA-FLOW.GW.5](OA-FLOW-GW.md#oa-flow.gw.5), [OA-FLOW.WR.1](OA-FLOW-WR.md#oa-flow.wr.1), [OA-FLOW.WR.2](OA-FLOW-WR.md#oa-flow.wr.2), [OA-FLOW.WR.3](OA-FLOW-WR.md#oa-flow.wr.3), [OA-FLOW.WR.4](OA-FLOW-WR.md#oa-flow.wr.4), [OA-FLOW.WR.5](OA-FLOW-WR.md#oa-flow.wr.5), [OA-FLOW.MW.4](OA-FLOW-MW.md#oa-flow.mw.4), [OA-FLOW.NF.5](OA-FLOW-NF.md#oa-flow.nf.5), [OA-FLOW.EW.2](OA-FLOW-EW.md#oa-flow.ew.2), [OA-FLOW.EW.3](OA-FLOW-EW.md#oa-flow.ew.3), [OA-FLOW.EW.5](OA-FLOW-EW.md#oa-flow.ew.5), [OA-FLOW.CP.1](OA-FLOW-CP.md#oa-flow.cp.1), [OA-FLOW.CP.2](OA-FLOW-CP.md#oa-flow.cp.2), [OA-FLOW.CP.3](OA-FLOW-CP.md#oa-flow.cp.3), [OA-FLOW.CP.4](OA-FLOW-CP.md#oa-flow.cp.4), [OA-FLOW.CP.5](OA-FLOW-CP.md#oa-flow.cp.5), [OA-FLOW.CP.6](OA-FLOW-CP.md#oa-flow.cp.6), [OA-FLOW.SF.SF0](OA-FLOW-SF.md#oa-flow.sf.sf0), [OA-FLOW.SF.SB0](OA-FLOW-SF.md#oa-flow.sf.sb0), [OA-FLOW.SF.SB1](OA-FLOW-SF.md#oa-flow.sf.sb1), [OA-FLOW.SF.SB2](OA-FLOW-SF.md#oa-flow.sf.sb2), [OA-FLOW.SF.SB3](OA-FLOW-SF.md#oa-flow.sf.sb3), [OA-FLOW.SF.SB4](OA-FLOW-SF.md#oa-flow.sf.sb4), [OA-FLOW.SF.SB5](OA-FLOW-SF.md#oa-flow.sf.sb5), [OA-FLOW.SF.SB6](OA-FLOW-SF.md#oa-flow.sf.sb6), [OA-FLOW.SF.SF3](OA-FLOW-SF.md#oa-flow.sf.sf3), [OA-FLOW.SF.SF4](OA-FLOW-SF.md#oa-flow.sf.sf4), [OA-FLOW.FF.1](OA-FLOW-FF.md#oa-flow.ff.1), [OA-FLOW.FF.2](OA-FLOW-FF.md#oa-flow.ff.2), [OA-FLOW.CF.1](OA-FLOW-CF.md#oa-flow.cf.1), [OA-FLOW.CF.6](OA-FLOW-CF.md#oa-flow.cf.6), [OA-FLOW.CF.7](OA-FLOW-CF.md#oa-flow.cf.7), [OA-FLOW.CF.8](OA-FLOW-CF.md#oa-flow.cf.8), [OA-FLOW.SC.4](OA-FLOW-SC.md#sc-04), [OA-FLOW.SC.5](OA-FLOW-SC.md#sc-05), [OA-FLOW.SC.8](OA-FLOW-SC.md#sc-08), [OA-FLOW.SC.9](OA-FLOW-SC.md#sc-09). The spectral domains, continuous-vector integrals, Gaussian scalar interchange and rectangle/circle complex-analysis arguments are complete in those earlier readers.

<a id="oa-flow.kt.1"></a><a id="kt-1"></a>

## KT-1. A closed-strip spectral coefficient with exact bounds

For \(\xi,\eta\in D(\Delta^{1/2})\), put \(p_n=1_{[1/n,n]}(\Delta)\) and
\[
F_n(z)=\langle \Delta^{iz}p_n\xi,p_n\eta\rangle.
\]
Every \(F_n\) is entire: on the indicated compact spectral interval the exponential power series and each derivative converge uniformly on compact sets of \(z\). The interval increases to the whole positive spectrum, because \(\Delta\) is injective.

Write \(z=t-is\), \(t\in\mathbb R\), \(0\leq s\leq1\). Spectral calculus and Cauchy–Schwarz give
\[
F_n(t-is)
=\langle U_t\Delta^{s/2}p_n\xi,\Delta^{s/2}p_n\eta\rangle.
\tag{KT1}
\]
The functions \(F_n\) converge uniformly on the whole closed strip \(-1\leq\operatorname{Im}z\leq0\). Indeed, for \(m\geq n\), the difference is the coefficient on \(p_m-p_n\), of absolute value at most
\[
\left(\int_{\lambda\notin[1/n,n]}(1+\lambda)\,d\mu_\xi(\lambda)\right)^{1/2}
\left(\int_{\lambda\notin[1/n,n]}(1+\lambda)\,d\mu_\eta(\lambda)\right)^{1/2},
\tag{KT2}
\]
where \(\mu_\xi(B)=\|1_B(\Delta)\xi\|^2\). Both finite tails tend to zero by the scalar convergence theorem. The bound follows from \(\lambda^s\leq1+\lambda\); orthogonality of the spectral cutoffs removes cross terms.

Let \(F_{\xi,\eta}\) be this uniform limit. It is continuous on the closed strip and holomorphic inside: uniform convergence on each rectangle passes the zero boundary integral to the limit, and the proved rectangular Morera criterion [SF-4](OA-FLOW-SF.md#oa-flow.sf.sf4) applies. Formula (KT1) passes to the limit, including both edges. In particular,
\[
\begin{aligned}
F_{\xi,\eta}(t)&=\langle U_t\xi,\eta\rangle,\\
F_{\xi,\eta}(t-i)&=\langle U_t\Delta^{1/2}\xi,\Delta^{1/2}\eta\rangle.
\end{aligned}
\tag{KT3}
\]
No vector \(\Delta\xi\) or \(\Delta\eta\) is required at the lower edge.

The exact log-convex estimate is
\[
|F_{\xi,\eta}(t-is)|
\leq
(\|\xi\|\|\eta\|)^{1-s}
(\|\Delta^{1/2}\xi\|\|\Delta^{1/2}\eta\|)^s.
\tag{KT4}
\]
To verify the scalar step without importing interpolation, for nonzero \(\xi\) normalize \(\mu_\xi\) to a probability and put \(m=\|\Delta^{1/2}\xi\|^2/\|\xi\|^2>0\). Concavity, or direct differentiation, gives \(r^s\leq(1-s)+sr\) for \(r\geq0\), \(0<s<1\). Apply this to \(r=\lambda/m\) and integrate:
\(\int\lambda^s\,d\mu_\xi\leq\|\xi\|^{2(1-s)}\|\Delta^{1/2}\xi\|^{2s}\).
The same estimate for \(\eta\) and Cauchy–Schwarz in (KT1) prove (KT4). Zero vectors and the endpoints follow directly. Injectivity of \(\Delta\) handles the possible zero value of \(m\).

The function is uniquely determined by its continuous real-edge values: the difference of two such holomorphic continuous functions, zero on a real interval, extends by zero across that interval by [SF-4](OA-FLOW-SF.md#oa-flow.sf.sf4)'s local rectangular argument; the identity theorem makes it zero throughout the strip. This uniqueness does not require a growth assumption beyond the continuity just stated.

<a id="oa-flow.kt.2"></a><a id="kt-2"></a>

## KT-2. The full finite-star KMS identities and the sign convention

For \(x,y\in A\), define \(F_{x,y}=F_{\Lambda(x),\Lambda(y)}\). [MW-4](OA-FLOW-MW.md#oa-flow.mw.4) gives \(\Lambda(\sigma_t(x))=U_t\Lambda(x)\) and preserves \(A\). At the real edge,
\[
F_{x,y}(t)=\varphi_0(y^*\sigma_t(x)).
\]
At the other edge, antiunitarity of \(J\), and the actual finite-star identities, give
\[
\begin{aligned}
F_{x,y}(t-i)
&=\langle\Delta^{1/2}U_t\Lambda(x),\Delta^{1/2}\Lambda(y)\rangle\\
&=\langle S\Lambda(y),S U_t\Lambda(x)\rangle\\
&=\langle\Lambda(y^*),\Lambda(\sigma_t(x)^*)\rangle\\
&=\varphi_0(\sigma_t(x)y^*).
\end{aligned}
\tag{KT5}
\]
Every product displayed belongs to \(\mathfrak m_\varphi=\operatorname{span}N^*N\), since both factors come from \(A\). No extension of \(\varphi_0\) outside its finite algebra is used.

In the usual upper-strip convention, for \(a,b\in A\) put
\[
G_{a,b}(z)=F_{a,b^*}(z-i),\qquad 0\leq\operatorname{Im}z\leq1.
\]
Then \(G_{a,b}\) is bounded and continuous on the closed strip, holomorphic in its interior, and
\[
G_{a,b}(t)=\varphi_0(\sigma_t(a)b),\qquad
G_{a,b}(t+i)=\varphi_0(b\sigma_t(a)).
\tag{KT6}
\]
Thus the convention \(U_t=\Delta^{it}\) gives the upper strip with precisely this order of the two products. Formula (KT4) supplies the uniform bound from the four finite numbers
\(\|\Lambda(a)\|,\|\Lambda(a^*)\|,\|\Lambda(b)\|,\|\Lambda(b^*)\|\).

If \(\varphi\) is a faithful normal state, then \(A=M\), and
\[
\sup_{0\leq\operatorname{Im}z\leq1}|G_{a,b}(z)|
\leq\|a\|\|b\|\qquad(a,b\in M).
\tag{KT7}
\]
For a finite positive functional of mass \(c\), the bound is \(c\|a\|\|b\|\). The arbitrary-weight statement remains exactly (KT6) on its complete finite-star algebra.

<a id="oa-flow.kt.3"></a><a id="kt-3"></a>

## KT-3. Gaussian smoothing inside every finite domain

For \(x\in M\), \(n\geq1\), and \(z\in\mathbb C\), define
\[
x_n(z)=\sqrt{\frac n\pi}
 \int_{\mathbb R}e^{-n(t-z)^2}\sigma_t(x)\,dt.
\tag{KT8}
\]
This is an ultraweak integral with an explicit meaning: for \(f\in M_*\), evaluate it as the scalar integral of \(f(\sigma_t(x))\). These evaluations form a bounded linear functional on \(M_*\), of norm at most
\[
e^{n(\operatorname{Im}z)^2}\|x\|.
\tag{KT9}
\]
The identification \(M=(M_*)^*\) proved in CP01–06 supplies a unique element of \(M\). The bound follows from the Gaussian normalization [FF-1](OA-FLOW-FF.md#oa-flow.ff.2) and
\(\left|e^{-n(t-z)^2}\right|=e^{n(\operatorname{Im}z)^2}e^{-n(t-\operatorname{Re}z)^2}\).

The map \(z\mapsto x_n(z)\) is norm entire. On a compact \(z\)-set, the kernel's first two complex derivatives are bounded by an integrable multiple of a polynomial in \(|t|\) times \(e^{-nt^2/2}\). Taylor's integral remainder on a line segment therefore makes the difference quotient converge in scalar \(L^1\). The integral norm bound transfers that convergence to \(M\). This also proves norm continuity of every derivative.

Normality of \(\sigma_s\) permits passage through the ultraweak integral; real translation of \(t\) and adjoints give
\[
\sigma_s(x_n(z))=x_n(z+s),\qquad
x_n(z)^*=(x^*)_n(\bar z).
\tag{KT10}
\]
Also \(x_n(0)\to x\) strongly*, with \(\|x_n(0)\|\leq\|x\|\). For each concrete vector, split the probability integral into a neighborhood of zero, where the strong* continuous orbit differs little from \(x\), and its complement, where the norm difference is at most \(2\|x\|\). The Gaussian tail tends to zero. Testing the ultraweak integral against vector functionals identifies its action with this continuous-vector integral; [SF-3](OA-FLOW-SF.md#oa-flow.sf.sf3) supplies that integral on an arbitrary Hilbert space.

If \(x\in N\), all the elements in (KT8) remain in \(N\), and
\[
\Lambda(x_n(z))
=\sqrt{\frac n\pi}\int_{\mathbb R}e^{-n(t-z)^2}U_t\Lambda(x)\,dt.
\tag{KT11}
\]
Here are the closure details. Use compact-interval Riemann sums and then integrable tails for both integrals. The operator sums lie in \(N\); their norms are uniformly bounded by a fixed constant greater than \(e^{n(\operatorname{Im}z)^2}\|x\|\), and converge ultraweakly to \(x_n(z)\). Their GNS vectors converge in norm to the right side of (KT11), because \(U_t\Lambda(x)\) is continuous and bounded. Meshes can be chosen on each expanding compact interval to approximate the kernel's absolute integral as well, preserving the stated common norm bound. The bounded GNS graph is ultraweak-times-weak closed by [EW-3](OA-FLOW-EW.md#oa-flow.ew.3), so its limit is exactly (KT11). This argument does not assume that the GNS map is bounded on the operator norm unit ball.

For \(x\in A\), apply the same argument to \(x^*\) and use (KT10); thus \(x_n(z)\in A\). At \(z=0\), the same approximate-identity estimate yields
\[
\Lambda(x_n(0))\to\Lambda(x),\qquad
\Lambda(x_n(0)^*)\to\Lambda(x^*).
\tag{KT12}
\]

<a id="oa-flow.kt.4"></a><a id="kt-4"></a>

## KT-4. All powers and a dense analytic algebra

Let \(L=\log\Delta\), defined by the injective spectral calculus. Formula FF1 and translation give, first for real \(z\), then for all complex \(z\) by the scalar identity theorem,
\[
\sqrt{\frac n\pi}\int_{\mathbb R}e^{-n(t-z)^2}e^{itq}\,dt
=e^{-q^2/(4n)}e^{izq}\qquad(q\in\mathbb R).
\tag{KT13}
\]
Both sides are entire in \(z\); the same local Gaussian bounds justify differentiation of the integral. Applying spectral projections \(1_{[-k,k]}(L)\) to (KT11) proves the multiplier identity on compact spectral intervals, by uniform scalar approximation and the bounded continuous-vector integral. Then let \(k\to\infty\). The multiplier \(e^{-q^2/(4n)}e^{izq}\) is bounded on the whole real line, so spectral dominated convergence proves
\[
\Lambda(x_n(z))=e^{-L^2/(4n)}e^{izL}\Lambda(x).
\tag{KT14}
\]
The right side means the single bounded multiplier just displayed; it does not first apply the possibly undefined \(e^{izL}\) to \(\Lambda(x)\).

For every real \(r\), multiplication by \(e^{rq}\) still leaves a bounded Gaussian multiplier. The exact domains and identity are therefore
\[
\Lambda(x_n(z))\in D(\Delta^r),\qquad
\Delta^r\Lambda(x_n(z))=\Lambda(x_n(z-ir)).
\tag{KT15}
\]
In particular the full GNS orbit of each Gaussian is entire.

Let \(\mathcal T\) be the algebra generated by the elements \(x_n(z)\) with \(x\in A\), \(n\geq1\), \(z\in\mathbb C\), without adjoining an identity that might have infinite weight. It is a \*-subalgebra of \(A\), invariant under all entire translations \(\sigma_w\). On generators put \(\sigma_w(x_n(z))=x_n(z+w)\), and on sums and products use sums and products of these norm-entire functions. This is well defined: any relation is zero for real \(w\), by the already defined automorphisms, and scalar testing plus the identity theorem makes it zero for every \(w\). Thus
\[
\sigma_w(ab)=\sigma_w(a)\sigma_w(b),\qquad
\sigma_w(a)^*=\sigma_{\bar w}(a^*),\qquad
\sigma_w\sigma_z(a)=\sigma_{w+z}(a)
\tag{KT16}
\]
on \(\mathcal T\).

For a product, the GNS identity
\(\Lambda(\sigma_z(a)\sigma_z(b))=\pi(\sigma_z(a))\Lambda(\sigma_z(b))\)
shows that its GNS orbit is norm entire; the same argument handles sums and stars. It also has every spectral power, with
\[
\Lambda(\sigma_z(a))=\Delta^{iz}\Lambda(a),\qquad
\Delta^r\Lambda(a)=\Lambda(\sigma_{-ir}(a))
\quad(a\in\mathcal T).
\tag{KT17}
\]
For completeness, this extension from the generators does not assume a rule for unbounded products. Apply \(1_{[-k,k]}(L)\) to the entire GNS orbit. On real \(z\), it equals \(e^{izL}1_{[-k,k]}(L)\Lambda(a)\) by [MW-4](OA-FLOW-MW.md#oa-flow.mw.4). The vector identity theorem, proved by scalar inner products and the scalar theorem, extends this equality to complex \(z\). The left side converges in \(H\) as \(k\to\infty\); the spectral domain criterion gives exactly (KT17).

The set \(\Lambda(\mathcal T)\) is a graph core for \(S\): (KT12) approximates each \(\Lambda(x)\), \(x\in A\), together with its \(S\)-image, and WR gives that \(\Lambda(A)\) is a core for \(S\). In fact it is a core for every \(\Delta^r\), \(r\in\mathbb R\). Given \(\xi\in D(\Delta^r)\), first apply the bounded Gaussian multiplier \(g_n(L)=e^{-L^2/(4n)}\), obtaining graph convergence to \(\xi\). For fixed \(n\), approximate \(\xi\) by \(\Lambda(x_j)\), \(x_j\in A\). Both \(g_n(L)\) and \(\Delta^r g_n(L)\) are bounded, so
\(g_n(L)\Lambda(x_j)=\Lambda((x_j)_n(0))\)
approximates \(g_n(L)\xi\) in the \(\Delta^r\)-graph norm. This two-stage approximation proves the assertion without requiring the original approximants to lie in \(D(\Delta^r)\).

Finally \(\mathcal T\) is strongly* dense in \(M\), with bounded approximation. GW supplies finite positive contractions \(u_i\uparrow1\); \(u_i x u_i\in\mathfrak m_\varphi\subset A\), \(\|u_i x u_i\|\leq\|x\|\), and these converge strongly* to \(x\). Gaussian approximation (KT10) then approximates each of them by elements of \(\mathcal T\) with the same norm bound. For any specified strong* neighborhood choose \(i\) and then a Gaussian index; the neighborhood-directed choices give the claimed bounded net.

If \(a\in\mathcal T\) and \(b\in A\), the lower-strip coefficient is the actual entire finite expression
\[
F_{a,b}(z)=\varphi_0(b^*\sigma_z(a))
\quad(-1\leq\operatorname{Im}z\leq0).
\tag{KT18}
\]
This follows from (KT17) and spectral cutoff convergence. In particular
\(\varphi_0(b^*\sigma_{-i}(a))=\varphi_0(ab^*)\).

<a id="oa-flow.kt.5"></a><a id="kt-5"></a>

## KT-5. The trace criterion on the entire positive cone

The modular group is trivial if and only if
\[
\varphi(x^*x)=\varphi(xx^*)\qquad(x\in M),
\tag{KT19}
\]
including infinite values.

Suppose first that \(\sigma_t=\mathrm{id}\). For \(x\in A\), the real boundary of \(F_{x,x}\) is constant. [KT-1](OA-FLOW-KT.md#kt-1)'s boundary uniqueness makes the strip constant, so (KT5) gives
\(\varphi(x^*x)=\varphi(xx^*)\).
For general \(x\in N\), the elements \(u_i x\in\mathfrak m_\varphi\subset A\) satisfy
\[
\varphi(u_i xx^*u_i)
=\varphi(x^*u_i^2x)\leq\varphi(x^*x).
\]
The positive elements on the left converge boundedly strongly, hence ultraweakly, to \(xx^*\). EW lower semicontinuity therefore gives
\(\varphi(xx^*)\leq\varphi(x^*x)\).
Apply the same reasoning to \(x^*\) once its value is finite. If either initial side is finite this proves equality; if both are infinite equality is immediate. This establishes (KT19) on all of \(M\).

Conversely assume (KT19). Then \(S\) is isometric on its dense initial domain \(\Lambda(A)\). Its closure is an everywhere defined conjugate-linear isometry: graph completion of an isometry is defined on the norm closure of that domain. Since \(S^2=1\) on the dense core, continuity extends this identity to all of \(H\), so \(S\) is antiunitary. Hence \(S^*S=\Delta=I\). MW then gives \(\sigma_t=\mathrm{id}\).

These proofs establish the full finite-star KMS existence theorem, an explicitly integrated analytic core with all real powers, and the whole-cone trace criterion. They assert neither a natural-cone standard form nor an operator-valued weight theorem.
