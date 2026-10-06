# Real-line Fourier filters and local division

*Fresh local proof, GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

These are real-line lemmas, not a claim about arbitrary locally compact groups. Actual earlier inputs are [SC-2–9](OA-FLOW-SC.md#sc-02), FF scalar interchange and FF-1/2, the norm-integral and separation proofs in CF Section 1, and the full [SF spectral calculus](OA-FLOW-SF.md#oa-flow.sf.sf1). In particular FF-2 proves Fourier uniqueness and the unitary inverse transform, rather than assuming inversion. The free primary route is [Connes (1973), Definitions 2.1.1–2.1.2 and Lemmas 2.1.3–2.1.6, printed pp.170–174](https://numdam.org/article/ASENS_1973_4_6_2_133_0.pdf#page=39). All harmonic statements used below are proved here at those scalar inputs.

The convention throughout is

<a id="equation-rf1"></a>

\[
 \widehat f(r)=\int_{\mathbb R}f(t)e^{itr}\,dt,
 \qquad k_\chi(t)=\frac1{2\pi}\int_{\mathbb R}\chi(r)e^{-itr}\,dr.
 \tag{RF1}
\]
Thus a time orbit \(e^{itr_0}x\) has spectral parameter \(r_0\). Inner products are linear in the first variable.

Exact individual earlier proof locators: [OA-FLOW.SC.2](OA-FLOW-SC.md#sc-02), [OA-FLOW.SC.3](OA-FLOW-SC.md#sc-03), [OA-FLOW.SC.4](OA-FLOW-SC.md#sc-04), [OA-FLOW.SC.5](OA-FLOW-SC.md#sc-05), [OA-FLOW.SC.6](OA-FLOW-SC.md#sc-06), [OA-FLOW.SC.7](OA-FLOW-SC.md#sc-07), [OA-FLOW.SC.8](OA-FLOW-SC.md#sc-08), [OA-FLOW.SC.9](OA-FLOW-SC.md#sc-09), OA-FLOW.FF.1, OA-FLOW.FF.2, OA-FLOW.FF.3, [OA-FLOW.SF.SF0](OA-FLOW-SF.md#oa-flow.sf.sf0), [OA-FLOW.SF.SB0](OA-FLOW-SF.md#oa-flow.sf.sb0), [OA-FLOW.SF.SB1](OA-FLOW-SF.md#oa-flow.sf.sb1), [OA-FLOW.SF.SB2](OA-FLOW-SF.md#oa-flow.sf.sb2), [OA-FLOW.SF.SB3](OA-FLOW-SF.md#oa-flow.sf.sb3), [OA-FLOW.SF.SB4](OA-FLOW-SF.md#oa-flow.sf.sb4), [OA-FLOW.SF.SB5](OA-FLOW-SF.md#oa-flow.sf.sb5), [OA-FLOW.SF.SB6](OA-FLOW-SF.md#oa-flow.sf.sb6), [OA-FLOW.SF.SF1](OA-FLOW-SF.md#oa-flow.sf.sf1), [OA-FLOW.SF.SF2](OA-FLOW-SF.md#oa-flow.sf.sf2), OA-FLOW.CF.1.

<a id="oa-flow.rf.1"></a><a id="rf-1"></a>

## RF-1. Smooth cutoffs, inversion and partitions

Smooth compactly supported bumps can be constructed explicitly. The function \(b(s)=e^{-1/(1-s^2)}\) for \(|s|<1\), extended by zero elsewhere, is smooth: each derivative inside the interval is a finite sum of a rational power of \(1-s^2\), a polynomial in \(s\), and the same exponential. Every such term tends to zero at the endpoints, because \(e^u\) dominates every fixed power of \(u\) by its elementary series. Induction gives the full smooth extension. Translation, positive dilation and finite sums therefore give bumps positive on smaller intervals and supported in any specified larger open intervals.

If a compact set \(K\) is covered by open sets \(O_i\), finitely many such bumps \(b_j\), with supports in assigned \(O_{i(j)}\), have sum \(D>0\) on a neighborhood of \(K\). For \(\chi\in C_c^\infty(\mathbb R)\) supported in \(K\), define \(\chi_j=\chi b_j/D\) there and extend by zero off \(D>0\). These are smooth compact functions, because the support of \(\chi\) is separated from the zero set of \(D\); they sum to \(\chi\) and are subordinate to the cover. A smooth cutoff equal to one near a compact \(K\) and supported in an open neighborhood \(O\) is obtained from such a \(D\) by composing with a smooth scalar step that is zero near zero and one above half its positive minimum on \(K\). A smooth step follows by integrating and normalizing the bump \(b\). These constructions prove every finite partition used below.

For \(\chi\in C_c^\infty\), differentiation under its compact integral and repeated integration by parts give

<a id="equation-rf2"></a>

\[
 |k_\chi(t)|\leq\frac{\|\chi\|_1}{2\pi},\qquad
 |t|^m|k_\chi(t)|\leq\frac{\|\chi^{(m)}\|_1}{2\pi}
 \quad(m\geq1).
 \tag{RF2}
\]
The boundary terms vanish, since all derivatives are zero outside a compact interval. In particular \(k_\chi\in L^1\cap L^2\); its derivatives have the same decay after applying this argument to \((-ir)^j\chi(r)\). FF-2's inverse identity on \(L^2\), with its explicit normalization, gives \(\widehat{k_\chi}=\chi\) almost everywhere. Both sides are continuous, the left by scalar DCT; hence equality holds everywhere. Also \(\int k_\chi=\chi(0)\).

For \(f,g\in L^1\), scalar interchange gives \(\|f*g\|_1\leq\|f\|_1\|g\|_1\), associativity, commutativity and
\(\widehat{f*g}=\widehat f\widehat g\). The transforms are continuous. FF-2's uniqueness proves equality of two \(L^1\) functions when their transforms agree; it applies to complex functions as well. The translation \(f_s(t)=f(t-s)\) has transform \(e^{isr}\widehat f(r)\). Modulation \(e^{ict}f(t)\) has transform \(\widehat f(r+c)\), and
\(\widehat{\overline f}(r)=\overline{\widehat f(-r)}\). All follow by an absolutely convergent substitution.

<a id="oa-flow.rf.2"></a><a id="rf-2"></a>

## RF-2. Local division in the convolution algebra

If \(f\in L^1\) and \(c=\widehat f(r_0)\ne0\), there is an open interval \(V\ni r_0\) such that for every \(\psi\in C_c^\infty(V)\) there is \(h\in L^1\) with

<a id="equation-rf3"></a>

\[
 f*h=k_\psi.
 \tag{RF3}
\]
Here is a direct proof, including the local inversion step. Choose \(\chi\in C_c^\infty\) equal to one near zero, and put
\[
 \chi_\delta(r)=\chi((r-r_0)/\delta),\qquad
 k_\delta(t)=\delta e^{-ir_0t}k_\chi(\delta t),\qquad
 b_\delta=f*k_\delta-c k_\delta.
\]
For fixed \(s\),
\[
 \|k_\delta(\,\cdot-s)-e^{ir_0s}k_\delta\|_1
 =\|k_\chi(\,\cdot-\delta s)-k_\chi\|_1\longrightarrow0.
\]
This is FF-1's actual \(L^1\) translation continuity. The norm is at most \(2\|k_\chi\|_1\), so scalar DCT against \(|f(s)|\) gives \(\|b_\delta\|_1\to0\). Fix \(\delta\) with \(\|b_\delta\|_1<|c|\).

Adjoin a formal convolution identity \(\delta_0\) to \(L^1\), with norm \(\|a\delta_0+g\|=|a|+\|g\|_1\). The convolution bound proves this is a unital Banach algebra; its transform is \(a+\widehat g\). The series

<a id="equation-rf4"></a>

\[
 (c\delta_0+b_\delta)^{-1}
 =c^{-1}\sum_{n=0}^{\infty}(-c^{-1}b_\delta)^{*n}
 \tag{RF4}
\]
converges in that norm; multiplying its finite partial sums and letting their geometric remainder tend to zero proves it is the inverse. No Wiener theorem is imported.

Choose \(V\) so that \(\chi_\delta=1\) there. Set
\(h=(c\delta_0+b_\delta)^{-1}*k_\psi\in L^1\).
The transform of the denominator is \(c+(\widehat f-c)\chi_\delta\), equal to \(\widehat f\) on \(V\) and nowhere zero because it has the inverse ([RF4](OA-FLOW-RF.md#equation-rf4)). Consequently \(\widehat{f*h}=\psi\) everywhere, since \(\psi\) is supported in \(V\). Fourier uniqueness proves ([RF3](OA-FLOW-RF.md#equation-rf3)). This proves only the needed local division; it asserts no synthesis theorem for arbitrary closed sets.

<a id="oa-flow.rf.3"></a><a id="rf-3"></a>

## RF-3. Approximate identities with compact frequency support

Choose \(\chi\in C_c^\infty\) with \(\chi(0)=1\), and put \(k_n(t)=n k_\chi(nt)\). Then

<a id="equation-rf5"></a>

\[
 \widehat{k_n}(r)=\chi(r/n),\quad
 \int k_n=1,\quad \|k_n\|_1=\|k_\chi\|_1,
 \quad\int_{|t|>a}|k_n(t)|\,dt\longrightarrow0\quad(a>0).
 \tag{RF5}
\]
The last statement is the integrable-tail estimate after substitution. It follows, by splitting the integral into \(|t|<a\) and its complement, that \(k_n*F\to F\) in \(L^1\) for every \(F\in L^1\). The bound on the small part uses translation continuity, and the complement uses \(2\|F\|_1\). The same splitting shows \(\int k_n(t)c(t)dt\to c(0)\) for every bounded function continuous at zero.

A **positive** version is available for bounded strong-operator limits. Choose a nonzero \(u\in C_c^\infty\), put \(l=k_u\), and set

<a id="equation-rf6"></a>

\[
 k(t)=\frac{|l(t)|^2}{\|l\|_2^2},\qquad k_\varepsilon(t)=\varepsilon^{-1}k(t/\varepsilon).
 \tag{RF6}
\]
These are nonnegative integrable functions of integral one. The denominator is positive by [RF-1](OA-FLOW-RF.md#oa-flow.rf.1) and Fourier uniqueness. Define \(\widetilde u(r)=\overline{u(-r)}\). Absolute integration over the two compact frequency supports gives

<a id="equation-rf7"></a>

\[
 |l(t)|^2=\frac1{2\pi}k_{u*\widetilde u}(t),\qquad
 \widehat k(r)=\frac{(u*\widetilde u)(r)}{2\pi\|l\|_2^2}.
 \tag{RF7}
\]
The convolution on the right is smooth with compact support, by differentiation under a compact integral. [RF-1](OA-FLOW-RF.md#oa-flow.rf.1) justifies its inverse and hence the stated transform; no product-transform theorem beyond this calculation is assumed. Therefore each \(k_\varepsilon\) has compact Fourier support, and \(\widehat{k_\varepsilon}(r)=\widehat k(\varepsilon r)\). These probability densities concentrate at zero as \(\varepsilon\downarrow0\) by the same tail substitution as in ([RF5](OA-FLOW-RF.md#equation-rf5)).

<a id="oa-flow.rf.4"></a><a id="rf-4"></a>

## RF-4. The scalar product calculation used for algebra spectra

Let \(f=k_\phi\) and \(g=k_\psi\), with \(\phi,\psi\in C_c^\infty\), and for real \(w\) define
\(F_w(v)=f(v)g(v+w)\). This is in \(L^1\), since \(f,g\in L^2\) and the scalar Cauchy–Schwarz inequality gives \(\|F_w\|_1\leq\|f\|_2\|g\|_2\). Directly from the two compact inverse integrals,

<a id="equation-rf8"></a>

\[
 F_w=k_{H_w},\qquad
 H_w(q)=\frac1{2\pi}\int\phi(r)\psi(q-r)e^{-i(q-r)w}\,dr.
 \tag{RF8}
\]
Indeed expand the right inverse integral, set \(s=q-r\), and interchange the compact absolute integrals. The result is exactly \(f(v)g(v+w)\). The function \(H_w\) is smooth with compact support contained in
\(\operatorname{supp}\phi+\operatorname{supp}\psi\), so [RF-1](OA-FLOW-RF.md#oa-flow.rf.1) gives \(\widehat{F_w}=H_w\).

If \(h\in L^1\) has transform zero on this sum, then \(h*F_w=0\) in \(L^1\) for each \(w\), by [RF-1](OA-FLOW-RF.md#oa-flow.rf.1)'s convolution identity and uniqueness. Moreover
\[
 K(v,w)=\int h(t)f(v-t)g(v+w-t)\,dt
\]
is jointly integrable in \((v,w)\), with integral of its absolute value at most \(\|h\|_1\|f\|_1\|g\|_1\). This follows by three applications of scalar interchange and translations. For almost every \((v,w)\) this is the convolution \((h*F_w)(v)\), hence it vanishes almost everywhere. These are the exact Fubini and zero-kernel facts used in the operator product proof.

<a id="oa-flow.rf.5"></a><a id="rf-5"></a>

## RF-5. A full spectral generator for every strongly continuous unitary group

Let \((U_t)_{t\in\mathbb R}\) be a strongly continuous unitary group on an arbitrary Hilbert space. The vector integral

<a id="equation-rf9"></a>

\[
 R\xi=\int_0^\infty e^{-t}U_t\xi\,dt
 \tag{RF9}
\]
exists by the norm-integral proof, with \(\|R\|\leq1\); no separability of the whole space is needed, since each continuous orbit is separable. Its adjoint is the same integral with \(U_{-t}\). The operators commute with all \(U_s\) and with each other. Absolute scalar interchange and splitting the quadrant into \(t\geq s\) and \(s\geq t\) give

<a id="equation-rf10"></a>

\[
 RR^*=R^*R=\tfrac12(R+R^*).
 \tag{RF10}
\]
For example, on \(t\geq s\), set \(r=t-s\); the remaining integral \(\int_0^\infty e^{-2s}ds=1/2\) gives \(R/2\). The other half gives \(R^*/2\), and the diagonal has measure zero.

For every real \(s\),

<a id="equation-rf11"></a>

\[
 U_sR\xi=e^s\int_s^\infty e^{-t}U_t\xi\,dt,
 \qquad \frac d{ds}U_sR\xi=U_s(R\xi-\xi).
 \tag{RF11}
\]
The identity is substitution; the derivative follows from the norm fundamental theorem on finite intervals and the integrable tail. If \(R\xi=0\), the derivative at zero gives \(\xi=0\). The same argument for \(R^*\) with the reversed group proves its injectivity, so \(R\) has dense range.

Put \(V=I-2R\). Equation ([RF10](OA-FLOW-RF.md#equation-rf10)) gives \(VV^*=V^*V=I\), and \(\ker(I-V)=0\). Apply SF's full unitary Borel calculus to the real function
\[
 a(z)=i\frac{1+z}{1-z}\quad(z\in\mathbb T\setminus\{1\}).
\]
The missing point has zero spectral projection by \(\ker(I-V)=0\). Thus \(A=a(V)\) is a densely defined self-adjoint operator. The pointwise identities in that calculus give

<a id="equation-rf12"></a>

\[
 R=(I-iA)^{-1},\qquad D(A)=\operatorname{ran}R,\qquad
 iA=I-R^{-1}\text{ on }D(A).
 \tag{RF12}
\]
Commutation with \(U_s\) transports through the spectral calculus, so \(U_s\) preserves \(D(A)\) and commutes there with \(A\). For \(\eta\in D(A)\), ([RF11](OA-FLOW-RF.md#equation-rf11)) says \(\frac d{ds}U_s\eta=iAU_s\eta\). SF's spectral DCT gives the corresponding derivative of \(e^{-isA}\) on the same domain. Expanding a difference quotient and using unitarity proves that \(e^{-isA}U_s\eta\) has derivative zero; the norm fundamental theorem makes it constant. Density yields

<a id="equation-rf13"></a>

\[
 U_s=e^{isA}\quad(s\in\mathbb R).
 \tag{RF13}
\]
Every domain in this construction is explicitly supplied by SF. Uniqueness also follows: any self-adjoint generator of the same group has the same Laplace resolvent ([RF9](OA-FLOW-RF.md#equation-rf9)), hence the same domain and value by ([RF12](OA-FLOW-RF.md#equation-rf12)).

For \(h\in L^1\), scalar interchange against spectral matrix coefficients now proves
\(\int h(t)U_tdt=\widehat h(A)\), as a bounded strong vector integral. Its norm is at most \(\|h\|_1\). The interchange is justified by the total variation bound on each spectral matrix coefficient, obtained by Cauchy–Schwarz from its two finite positive spectral measures. This closes the generator and filtering passage needed for a general invariant GNS implementation.
