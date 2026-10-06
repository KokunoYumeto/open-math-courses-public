# Natural cones for arbitrary faithful normal semifinite weights

*Fresh local proof, GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

Inner products are linear in the first variable. Let \(\varphi\) be a faithful normal semifinite weight on an arbitrary von Neumann algebra \(M\). Use its actual [GW](OA-FLOW-GW.md#oa-flow.gw.1), [NF](OA-FLOW-NF.md#oa-flow.nf.5), [WR](OA-FLOW-WR.md#oa-flow.wr.4) and [MW](OA-FLOW-MW.md#oa-flow.mw.1) construction. Identify \(M\) with its faithful normal GNS image on \(H\), using [ST-2](OA-FLOW-ST12.md#oa-flow.st.2). Put \(N=N_\varphi\), \(\mathcal A=\Lambda(N\cap N^*)\), \(S=J\Delta^{1/2}\), \(F=S^*=J\Delta^{-1/2}\), and \(j(x)=JxJ\). All domains and full bounded-vector identifications are those of WR, [HA-R](OA-FLOW-HA-R.md#oa-flow.ha-r.4) and [WH-04, Sections 2–4](OA-FLOW-WH04.md#oa-flow.wh04.2).

Other actual inputs are the closed-form representation [FF-4](OA-FLOW-FF.md#oa-flow.ff.5), the complete spectral proof [SF, SB-0–6](OA-FLOW-SF.md#oa-flow.sf.sb0), [KT-3/4](OA-FLOW-KT.md#oa-flow.kt.3)'s Gaussian analytic core, and the whole finite-ideal analytic right-multiplication identity [GF-1](OA-FLOW-WS.md#oa-flow.weight-sum.gf1). The latter is used only for multiplication by bounded entire elements; no normal-weight sum decomposition is an input here.

The freely accessible human route is [Hiai, Theorem 3.2 and Lemma 3.3, printed pp.20–22](https://arxiv.org/pdf/2004.02383v1#page=20), stated there in the faithful-state setting. We prove the full finite-ideal version below. In particular the positive-extension step and its covariance are supplied locally, and no cyclic vector for \(1\), separability, or faithful-state reduction is assumed.

<a id="oa-flow.nc.1"></a><a id="nc-1"></a>

Exact additional locators: [WH04 Section2](OA-FLOW-WH04.md#oa-flow.wh04.2), [WH04 Section3](OA-FLOW-WH04.md#oa-flow.wh04.3), [WH04 Section4](OA-FLOW-WH04.md#oa-flow.wh04.4), [FF-1 Gaussian integral](OA-FLOW-FF.md#oa-flow.ff.2), [KT-4 analytic core](OA-FLOW-KT.md#oa-flow.kt.4). The linked GF-1 result is only its full finite-ideal right-multiplication proof.

## NC-1. The positive symmetric extension needed for cone duality

Let \(T_0:D_0\to H\) be a densely defined linear operator with \(\langle T_0x,x\rangle\geq0\). Polarization proves symmetry and the Cauchy–Schwarz inequality for the form \(q_0(x,y)=\langle T_0x,y\rangle\). Complete \(D_0\) for the Hilbert norm

<a id="equation-nc1"></a>

\[
 \|x\|_V^2=\|x\|^2+q_0(x,x).
 \tag{NC1}
\]
Its inclusion into \(H\) extends to a contraction \(i:V\to H\). This extension is injective. Indeed, if \(x_n\to v\) in \(V\) and \(x_n\to0\) in \(H\), then, for \(y\in D_0\),
\[
 \langle x_n,y\rangle_V
 =\langle x_n,y+T_0y\rangle_H\longrightarrow0.
\]
Thus \(v\) is orthogonal in \(V\) to the dense subspace \(D_0\), and \(v=0\). On \(i(V)\) define the form transported from
\(\langle v,w\rangle_V-\langle i(v),i(w)\rangle_H\).
It is nonnegative, has graph norm exactly \(\|\cdot\|_V\), is densely defined and closed. [FF-4](OA-FLOW-FF.md#oa-flow.ff.5) supplies a positive self-adjoint operator \(T\) with this form.

It extends \(T_0\) on its full initial domain. For \(x\in D_0\), the equality
\(q_0(x,y)=\langle T_0x,y\rangle\) extends by graph-norm continuity from \(y\in D_0\) to every \(y\in i(V)\); [FF-4](OA-FLOW-FF.md#oa-flow.ff.5)'s form-operator criterion, explicitly proved in [HA-R4](OA-FLOW-HA-R.md#oa-flow.ha-r.4), gives \(x\in D(T)\) and \(Tx=T_0x\).

If a unitary \(u\) preserves \(D_0\) in both directions and commutes with \(T_0\) there, it acts unitarily on \(V\), intertwining \(i\). Consequently it commutes with \(ii^*\), the resolvent and all spectral projections of \(T\), by [FF-4](OA-FLOW-FF.md#oa-flow.ff.5) and SF. Thus if all unitaries of a von Neumann algebra \(L\) have this property, \(T\) is affiliated with \(L'\). This proves the precise covariant positive extension we shall use.

<a id="oa-flow.nc.2"></a><a id="nc-2"></a>

## NC-2. Two full finite-ideal cones are dual

Write \(B_l=\Lambda(N)\) and \(\lambda_{\Lambda(x)}=x\), by [WR-4](OA-FLOW-WR.md#oa-flow.wr.4). Define

<a id="equation-nc2"></a>

\[
 C_l=\overline{\{\Lambda(a):a\in M_+,\ \varphi(a)<\infty\}}.
 \tag{NC2}
\]
Every vector displayed belongs to \(\Lambda(N)\), since \(a^2\leq\|a\|a\). This is a closed convex cone. It is also the closure of the positive bounded vectors
\(\{\xi\in B_l:\lambda_\xi\geq0\}\).
For that assertion write \(\xi=\Lambda(a)\), \(a\geq0\), \(\varphi(a^2)<\infty\), and put

<a id="equation-nc3"></a>

\[
 a_\epsilon=a^2(a+\epsilon)^{-1},\qquad
 \varphi(a_\epsilon)\leq\epsilon^{-1}\varphi(a^2),\qquad
 \Lambda(a_\epsilon)=a(a+\epsilon)^{-1}\Lambda(a).
 \tag{NC3}
\]
The last vectors tend to \(\Lambda(a)\): the bounded functions increase to the support projection of \(a\), and its complementary projection kills \(\Lambda(a)\) because it kills \(a\). The cone in ([NC2](OA-FLOW-NC.md#equation-nc2)) is precisely the set of algebra squares \(b^\#b\), \(b\in\mathcal A\), before closure: for one direction use \(b=\Lambda(x)\), and for the other use \(x=a^{1/2}\).

For the full right algebra \(\mathcal D=B_r\cap D(F)\), put

<a id="equation-nc4"></a>

\[
 C_r=\overline{\{\eta\in B_r:R_\eta\geq0\}}.
 \tag{NC4}
\]
The full WF/WR opposite weight \(\rho\) on \(M'\) has finite ideal \(I_r=R(B_r)\) and vector map \(\theta(R_\eta)=\eta\). Applying the same positive cutoff argument to \(\rho\) shows that ([NC4](OA-FLOW-NC.md#equation-nc4)) is the closed cone generated by \((Fb)b\), \(b\in\mathcal D\), with the right algebra product of HA-R. More explicitly, for \(R_\eta=t\geq0\), the vector
\(\eta_\epsilon=t(t+\epsilon)^{-1}\eta\) has multiplier \(t^2(t+\epsilon)^{-1}\). This multiplier has finite \(\rho\)-value, since it is at most \(\epsilon^{-1}t^2\). Its positive square root lies in \(I_r\cap I_r^*\), so its vector \(b\in\mathcal D\) gives \(\eta_\epsilon=(Fb)b\). The kernel projection of \(t\) kills \(\eta\), by injectivity of the full multiplier map, so \(\eta_\epsilon\to\eta\). [MW-1](OA-FLOW-MW.md#oa-flow.mw.1)'s whole-vector identities give

<a id="equation-nc5"></a>

\[
 JC_l=C_r,\qquad JC_r=C_l.
 \tag{NC5}
\]
This uses the full opposite GNS identification already proved for a faithful n.s.f. input; it does not use NO's possibly proper range for a general normal input.

For \(a\in\mathcal A,b\in\mathcal D\), the Hilbert adjoint and mixed-product identities give

<a id="equation-nc6"></a>

\[
 \langle a^\#a,(Fb)b\rangle
 =\langle a,\lambda_aR_bFb\rangle
 =\langle R_b^*a,\lambda_aFb\rangle
 =\|\lambda_aFb\|^2\geq0.
 \tag{NC6}
\]
Consequently \(C_r\subseteq C_l^\vee\), where the dual means that the complex inner product is a nonnegative real number at every cone vector.

For the reverse inclusion take \(\eta\in C_l^\vee\). **Use the entire left ideal**, rather than just its finite-star intersection: on \(\Lambda(N)\) define

<a id="equation-nc7"></a>

\[
 T_0\Lambda(x)=x\eta.
 \tag{NC7}
\]
Its quadratic value is \(\langle x\eta,\Lambda(x)\rangle=\langle\eta,\Lambda(x^*x)\rangle\geq0\). Thus [NC-1](OA-FLOW-NC.md#oa-flow.nc.1) applies. Every unitary \(u\in M\) preserves \(\Lambda(N)\) in both directions, and \(T_0u=uT_0\) there. Obtain a positive self-adjoint extension \(T\) affiliated with \(M'\).

Let \(f_n=1_{[0,n]}(T)\) and \(\eta_n=f_n\eta\). For every \(x\in N\),
\[
 x\eta_n=f_nx\eta=f_nT\Lambda(x)=(Tf_n)\Lambda(x).
\]
Hence \(\eta_n\in B_r\) and \(R_{\eta_n}=Tf_n\geq0\). Since \(f_n\to I\) strongly, \(\eta_n\to\eta\), proving \(\eta\in C_r\). Therefore \(C_l^\vee=C_r\). Applying \(J\), which conjugates inner products and preserves real nonnegativity, and using ([NC5](OA-FLOW-NC.md#equation-nc5)), gives the other equality:

<a id="equation-nc8"></a>

\[
 C_l^\vee=C_r,\qquad C_r^\vee=C_l.
 \tag{NC8}
\]
No complex-cone bipolar theorem has been assumed.

<a id="oa-flow.nc.3"></a><a id="nc-3"></a>

## NC-3. The quarter-power cone is self-dual

Every positive bounded left vector is fixed by \(S\), by the full adjoint-intersection criterion of WR/HA-R. Since \(S\) is closed, every \(\xi\in C_l\) lies in \(D(S)\) and satisfies \(S\xi=\xi\). Thus

<a id="equation-nc9"></a>

\[
 C_l\subset D(\Delta^{1/2}),\quad
 \Delta^{1/2}\xi=J\xi,\quad
 C_r=\Delta^{1/2}C_l\subset D(\Delta^{-1/2}).
 \tag{NC9}
\]
Define

<a id="equation-nc10"></a>

\[
 P=\overline{\Delta^{1/4}C_l}
   =\overline{\Delta^{-1/4}C_r}.
 \tag{NC10}
\]
These expressions are well defined by the full spectral domains, and equal by ([NC9](OA-FLOW-NC.md#equation-nc9)). The cone is closed and convex. Antiunitary spectral transport and ([NC9](OA-FLOW-NC.md#equation-nc9)) give \(J\Delta^{1/4}\xi=\Delta^{1/4}\xi\) on \(C_l\), so \(J\) fixes \(P\) pointwise.

MW covariance preserves positive bounded multipliers and hence both \(C_l,C_r\). Therefore \(\Delta^{it}P=P\). For \(G_n=\exp(-(\log\Delta)^2/n)\), the Gaussian formula from [FF-1](OA-FLOW-FF.md#oa-flow.ff.2) expresses \(G_n\) as an integral of \(\Delta^{it}\) against a positive probability density. Compact Riemann sums and their norm limits show

<a id="equation-nc11"></a>

\[
 G_nP\subseteq P,\quad G_n^*=G_n,\quad
 G_n\to I\text{ strongly},\quad
 G_nH\subseteq\bigcap_{r\in\mathbb R}D(\Delta^r).
 \tag{NC11}
\]
The last assertion follows because \(e^{rs-s^2/n}\) is bounded on the real line, for every real \(r\). The Gaussian integral is vectorwise; no separability of \(H\) is needed.

For \(\xi\in C_l,\eta\in C_r\), spectral graph cutoffs prove

<a id="equation-nc12"></a>

\[
 \langle\Delta^{1/4}\xi,\Delta^{-1/4}\eta\rangle
 =\langle\xi,\eta\rangle\geq0.
 \tag{NC12}
\]
Indeed the identity holds on compact spectral bands and both transformed vectors converge in norm by their stated domains. This and ([NC10](OA-FLOW-NC.md#equation-nc10)) imply \(P\subseteq P^\vee\).

Conversely let \(\zeta\in P^\vee\). Then \(G_n\zeta\in P^\vee\), because \(G_n\) is self-adjoint and preserves \(P\). For every \(\xi\in C_l\),
\[
 \langle\xi,\Delta^{1/4}G_n\zeta\rangle
 =\langle\Delta^{1/4}\xi,G_n\zeta\rangle\geq0.
\]
[NC-2](OA-FLOW-NC.md#oa-flow.nc.2) gives \(\Delta^{1/4}G_n\zeta\in C_r\). Its negative quarter power is \(G_n\zeta\), by the exact spectral product domains, so \(G_n\zeta\in P\). Passing to the norm limit proves

<a id="equation-nc13"></a>

\[
 P=P^\vee.
 \tag{NC13}
\]

<a id="oa-flow.nc.4"></a><a id="nc-4"></a>

## NC-4. Algebra action and the central axiom

We prove \(xj(x)P\subseteq P\) for all \(x\in M\). First let \(x\) be a bounded entire modular element and let \(a\geq0\), \(a\in N\), be obtained by Gaussian smoothing of a positive element of \(N\). KT gives its complete power-domain identity \(\Delta^{1/4}\Lambda(a)=\Lambda(\sigma_{-i/4}(a))\).

[GF-1](OA-FLOW-WS.md#oa-flow.weight-sum.gf1), with the exact half-shift sign, gives on the whole \(N\)

<a id="equation-nc14"></a>

\[
 j(x)\Lambda(z)=\Lambda(z\,\sigma_{-i/2}(x^*)).
 \tag{NC14}
\]
For clarity, apply its identity
\(\Lambda(zv^*)=J\sigma_{-i/2}(v)J\Lambda(z)\)
to \(v=\sigma_{i/2}(x)\); then \(v^*=\sigma_{-i/2}(x^*)\).
Put \(y=\sigma_{i/4}(x)\). The product \(yay^*\) belongs to \(N\) by this full right-multiplication result, is positive, and is entire with the corresponding vector power identities. The latter follow either from KT's spectral cutoff argument for products or by applying ([NC14](OA-FLOW-NC.md#equation-nc14)) and the bounded entire orbits to the Gaussian vector on each compact spectral band. Hence

<a id="equation-nc15"></a>

\[
 xj(x)\Delta^{1/4}\Lambda(a)
 =\Lambda(x\,\sigma_{-i/4}(a)\,\sigma_{-i/2}(x^*))
 =\Delta^{1/4}\Lambda(yay^*)\in P.
 \tag{NC15}
\]
There is also a direct domain check for the last equality. The vector-valued function
\[
 V(z)=\sigma_z(y)\,j(\sigma_{\bar z-i/2}(y))\,
             \Lambda(\sigma_z(a))
\]
is entire: the second operator-valued factor is holomorphic because \(j\) is conjugate linear, and all factors are bounded on each compact subset of the complex plane. Formula ([NC14](OA-FLOW-NC.md#equation-nc14)) identifies it with \(\Lambda(\sigma_z(yay^*))\), including finite-ideal membership, and \(V(t)=\Delta^{it}\Lambda(yay^*)\) for real \(t\). After applying a compact spectral projection of \(\log\Delta\), analytic continuation gives the same equality for every complex \(z\). The finite norm of \(V(-i/4)\) bounds the increasing squared spectral integrals, proving \(\Lambda(yay^*)\in D(\Delta^{1/4})\) and the displayed equality on the full domain.

The positive Gaussian smoothings \(a_n\) of any positive \(a\in N\) satisfy \(\Lambda(a_n)\to\Lambda(a)\) and \(S\Lambda(a_n)=\Lambda(a_n)\). Therefore
\[
 \|\Delta^{1/4}(\Lambda(a_n)-\Lambda(a))\|^2
 \leq\|\Lambda(a_n)-\Lambda(a)\|\,
       \|\Delta^{1/2}(\Lambda(a_n)-\Lambda(a))\|
 =\|\Lambda(a_n)-\Lambda(a)\|^2\to0.
\]
They generate a dense subset of \(P\) by [NC-2](OA-FLOW-NC.md#oa-flow.nc.2)/3. Thus ([NC15](OA-FLOW-NC.md#equation-nc15)) holds on all of \(P\) for entire \(x\). Finally the positive Gaussian regularizations \(x_n\) of an arbitrary bounded \(x\) are entire, uniformly bounded and converge strongly together with their adjoints. The bounded operators \(x_nj(x_n)\) converge strongly to \(xj(x)\); closedness of \(P\) gives the required action.

For a central self-adjoint \(z\in M\), centrality and the finite-star core give \(Sz=zS\) on \(D(S)\); taking adjoints gives the same commutation with \(F\). Thus \(z\) commutes with the full positive product \(\Delta\) and its resolvents. It commutes with \(\Delta^{1/2}\), and \(S=J\Delta^{1/2}\) then implies \(Jz=zJ\) on the dense range of \(\Delta^{1/2}\), hence everywhere. Splitting a general central element into self-adjoint real and imaginary parts proves

<a id="equation-nc16"></a>

\[
 JzJ=z^*\quad(z\in Z(M)).
 \tag{NC16}
\]
Along with the already proved \(JMJ=M'\), equations ([NC13](OA-FLOW-NC.md#equation-nc13)), ([NC16](OA-FLOW-NC.md#equation-nc16)), the pointwise \(J\)-fixing and \(xj(x)\)-invariance establish **all standard-form axioms** on this arbitrary-weight GNS Hilbert space.

<a id="oa-flow.nc.5"></a><a id="nc-5"></a>

## NC-5. Faithful-state specialization used later

If \(\varphi=\omega_\Omega\) is a faithful normal positive functional and \(\Omega=\Lambda(1)\), then

<a id="equation-nc17"></a>

\[
 P=\overline{\Delta^{1/4}M_+\Omega}
  =\overline{\{xj(x)\Omega:x\in M\}}.
 \tag{NC17}
\]
The first equality is [NC-2](OA-FLOW-NC.md#oa-flow.nc.2)/3. Here \(J\Omega=\Omega\) and \(\Delta\Omega=\Omega\), directly from the unital finite-star graph and its adjoint graph. For entire \(x\), ([NC15](OA-FLOW-NC.md#equation-nc15)) with \(a=1\) shows
\[
 xj(x)\Omega=\Delta^{1/4}yy^*\Omega,\qquad y=\sigma_{i/4}(x).
\]
Conversely, for entire \(y\), take \(x=\sigma_{-i/4}(y)\). To obtain every positive bounded \(a\), approximate \(a^{1/2}\) strongly with uniformly bounded entire Gaussian elements \(y_n\). Then \(y_ny_n^*\to a\) strongly, so their vectors converge; both vectors are \(S\)-fixed, making their quarter-power images converge by the estimate in [NC-4](OA-FLOW-NC.md#oa-flow.nc.4). The two closures in ([NC17](OA-FLOW-NC.md#equation-nc17)) are therefore equal. This specialization does not replace the arbitrary-weight argument in [NC-1](OA-FLOW-NC.md#oa-flow.nc.1)–4.
