# Compact coefficient integration for normal covariant representations

*Original exposition: CC0-1.0 to the extent of rights held.*

Let \(G\) be any locally compact Hausdorff group with left Haar measure satisfying \(\mu(Es)=\Delta(s)\mu(E)\). Thus \(\int f(ts)dt=\Delta(s)^{-1}\int f\) and \(\int f(t^{-1})dt=\int f(t)\Delta(t)^{-1}dt\). Scalar products are linear in the first variable. Let \(\alpha\) be a point-ultraweakly continuous action on a von Neumann algebra \(M\).

[AT](OA-FLOW-AT.md#oa-flow.at.1), [NR3](OA-FLOW-NR.md#oa-flow.nr.3), [CP4/6](OA-FLOW-CP.md#oa-flow.cp.4), [HR](OA-FLOW-HR.md#hr-03), and [L24](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) supply the normality, continuity and compact-carrier integration used below. Initially use the faithful regular pair
\[
 (\pi(a)\xi)(t)=\alpha_{t^{-1}}(a)\xi(t),\qquad
 (\lambda_s\xi)(t)=\xi(s^{-1}t).
\]
No implementing group on the original coefficient Hilbert space is needed.

The mathematics of compact coefficient integration is treated in Haagerup, [Lemmas 2.3–2.4, printed pp.102–103](https://www.mscand.dk/article/download/11768/9784/30722#page=4). Below we prove the coefficient laws, their represented versions, normality and the precise nonfaithful regular case from the earlier programme inputs.

<a id="ccm-4"></a>

## CCM4. Compact coefficient integrals and their exact algebra

Let \(\mathcal C\) be the bounded, compactly supported strong* continuous maps \(x:G\to M\). Define the normal weak integral

<a id="equation-ccm14"></a>

\[
 L_x=\int_G\lambda_s\pi(x(s))\,ds.                    \tag{CCM14}
\]
On a compactly supported continuous vector field, the operator-valued integrand acts continuously in Hilbert norm and has compact support. Its integral is a genuine Bochner vector integral; its norm is bounded by \(\mu(\operatorname{supp}x)\sup\|x(s)\|\). Duality and vector tests give the same bounded operator as (CCM14). Thus no global measurability or countable basis is used. The change of variable \(s=tu\), justified by left invariance, gives

<a id="equation-ccm15"></a>

\[
 (L_x\xi)(t)=\int_G\alpha_u(x(tu))\xi(u^{-1})\,du.
                                                               \tag{CCM15}
\]
Joint strong* continuity on bounded sets proves continuity of this compactly supported vector field. In particular all calculations can first be made on the dense compact tensor core.

Fubini for compact continuous vector integrands, the covariance relation, and the two Haar changes above give

<a id="equation-ccm16"></a>

\[
 \begin{split}
 L_xL_y&=L_{x\star y},\qquad
 (x\star y)(t)=\int_G\alpha_u(x(tu))y(u^{-1})\,du,\\
 L_x^*&=L_{x^\#},\qquad
 x^\#(t)=\Delta(t)^{-1}\alpha_{t^{-1}}(x(t^{-1})^*).
 \end{split}                                                    \tag{CCM16}
\]
For the product, directly expand \(\lambda_s\pi(x(s))\lambda_v\pi(y(v))=\lambda_{sv}\pi(\alpha_{v^{-1}}(x(s))y(v))\), then put \(s=tu,v=u^{-1}\). For the adjoint expand \(\pi(x(s)^*)\lambda_{s^{-1}}=\lambda_{s^{-1}}\pi(\alpha_s(x(s)^*))\) and use inversion. These formulas show \(\mathcal C\) is an algebra closed under \(\#\); the product has support in \(\operatorname{supp}x\operatorname{supp}y\). Continuity of it and its adjoint follows by integrating the joint strong* continuous bounded integrand on a fixed compact set in a neighborhood of each \(t\). The required uniform convergence on each tested vector follows from a finite compact cover, so this passage also works for nets.

<a id="ccm-general-covariant-integration"></a>

### The integral in every normal unital covariant pair

The boundedness condition in the definition of \(\mathcal C\) is automatic. Choose a faithful normal concrete representation \(\iota:M\to B(H_c)\). For each \(\zeta\in H_c\), the pullback \(\omega_\zeta(a)=\langle\iota(a)\zeta,\zeta\rangle\) is a positive normal functional, and its intrinsic seminorm satisfies \(p_{\omega_\zeta}(b)^2=\omega_\zeta(b^*b)=\|\iota(b)\zeta\|^2\). Intrinsic strong* continuity of \(x\) therefore makes \(s\mapsto\iota(x(s))\zeta\) norm continuous before any common operator norm bound has been obtained. For compact \(K\subseteq G\), its image is compact and hence bounded. Apply [the uniform boundedness theorem, with its Baire proof](../../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-04) once, to the family \(\{\iota(x(s)):s\in K\}\) of bounded operators on the Banach space \(H_c\). It yields \(\sup_K\|\iota(x(s))\|<\infty\). The faithful isometry proved in [ST2](OA-FLOW-ST12.md#oa-flow.st.2) identifies this with \(\sup_K\|x(s)\|\); ST2's bounded strong* comparison is now available. The operator norm is lower semicontinuous in the concrete strong topology, since it is the supremum of the continuous functions \(\|\iota(x(s))\zeta\|\) for unit vectors \(\zeta\); hence it is Borel measurable. For compactly supported \(x\), \(\int\|x(s)\|\,ds\) is finite.

Let \(\rho:M\to B(H_\rho)\) be a normal unital *-homomorphism, and let \(V:G\to\mathcal U(H_\rho)\) be strongly continuous with \(V_s\rho(a)V_s^*=\rho(\alpha_s(a))\). Faithfulness of \(\rho\) is not required. For \(\zeta\in H_\rho\), the positive normal functional \(a\mapsto\langle\rho(a)\zeta,\zeta\rangle\) gives

\[
 \|\rho(b)\zeta\|^2=\langle\rho(b^*b)\zeta,\zeta\rangle.
\]

Thus \(\rho\) carries bounded intrinsic strong* convergence to strong* convergence on \(H_\rho\). Each field \(s\mapsto V_s\rho(x(s))\zeta\) is norm continuous with compact support. The continuous-vector integration proved in [L24](OA-FLOW-L24.md#oa-flow.grp.vectorintegration) therefore defines a bounded operator

\[
 \Phi_{\rho,V}(x)\zeta=\int_G V_s\rho(x(s))\zeta\,ds,
 \qquad \|\Phi_{\rho,V}(x)\|\le\int_G\|x(s)\|\,ds.
\]

First identify its generated von Neumann algebra. Write \(A=\{\rho(M),V(G)\}''\). If \(T\in A'\), it commutes with every integrand and hence with its vector integral. Thus \(\Phi_{\rho,V}(x)\in A\). Conversely, [H0's compact cutoffs](OA-FLOW-TOPOLOGY.md#l138-h0) give nonnegative \(f_W\in C_c(G)\), supported in the identity neighborhood \(W\), with \(\int f_W=1\). Indeed choose a nonzero nonnegative cutoff inside \(W\); its integral is positive because Haar measure has full support, and normalize it. Direct the neighborhoods by reverse inclusion. Strong continuity gives

\[
 A_W:=\Phi_{\rho,V}(f_W1)=\int f_W(s)V_s\,ds\longrightarrow I,
 \qquad \|A_W\|\le1.
\]

For fixed \(t\), the coefficient \(s\mapsto f_W(t^{-1}s)1\) has integral \(V_tA_W\to V_t\). Also \(\Phi_{\rho,V}(f_W a)=A_W\rho(a)\to\rho(a)\). A bounded operator commuting with all coefficient integrals consequently commutes with all \(V_t\) and \(\rho(a)\). Taking commutants proves

\[
 \{\Phi_{\rho,V}(x):x\in\mathcal C\}''=\{\rho(M),V(G)\}''.
\]

Unitality is used in \(\rho(1)=I\). Without it the conclusion on the whole Hilbert space fails: take \(M=\mathbb C\), \(\rho=0\) on \(\mathbb C^2\), and the representation of \(\mathbb Z/2\mathbb Z\) generated by \(\operatorname{diag}(1,-1)\). All integrals are zero, whose double commutant is \(\mathbb CI\), while the algebra generated by \(V\) is the diagonal algebra. Restriction to the invariant corner \(\rho(1)H_\rho\) gives the unital version.

<a id="ccm-general-coefficient-laws"></a>

### The Haar factors and the coefficient identities

All integrals in the following calculations have compact carriers. Products and action maps are jointly strong* continuous on the common norm bounds by [AT4](OA-FLOW-AT.md#oa-flow.at.4). [CP6](OA-FLOW-CP.md#oa-flow.cp.6) realizes the coefficient integrals in \(M=(M_*)^*\), and the vector tests and [HR5's Radon-product Fubini theorem](OA-FLOW-HR.md#hr-05) permit the indicated iterated integrals. No assertion about an unrestricted product Borel sigma algebra is needed.

Covariance gives

\[
 V_s\rho(x(s))V_v\rho(y(v))
   =V_{sv}\rho\bigl(\alpha_{v^{-1}}(x(s))y(v)\bigr).
\]

Set \(t=sv\) in the inner integral: the right-translation Jacobian is \(ds=\Delta(v)^{-1}dt\). Next put \(u=v^{-1}\): inversion gives \(dv=\Delta(u)^{-1}du\), while the preceding factor becomes \(\Delta(u)\). They cancel, leaving precisely the convolution in (CCM16). For the adjoint,

\[
 \rho(x(s)^*)V_{s^{-1}}
    =V_{s^{-1}}\rho\bigl(\alpha_s(x(s)^*)\bigr).
\]

Now \(t=s^{-1}\) contributes \(ds=\Delta(t)^{-1}dt\), with no second factor to cancel. Consequently

\[
 \Phi_{\rho,V}(x)\Phi_{\rho,V}(y)=\Phi_{\rho,V}(x\star y),
 \qquad \Phi_{\rho,V}(x)^*=\Phi_{\rho,V}(x^\#).
\]

For completeness these operations form a \*-algebra on the coefficients themselves, independently of any injectivity of \(\Phi_{\rho,V}\). The support of \(x\star y\) lies in \(\operatorname{supp}x\operatorname{supp}y\). For \(t\) in a compact neighborhood the variable \(u\) lies in the fixed compact set \((\operatorname{supp}y)^{-1}\). Joint strong\* continuity of the bounded integrand, followed by a finite cover of that compact carrier for each tested vector, gives continuity of the integral and its adjoint. The same argument and continuity of \(\Delta\) prove \(x^\#\in\mathcal C\).

Expanding both convolutions and then substituting \(r=vu\), a left translation with no Haar factor, gives

\[
 \begin{aligned}
 ((x\star y)\star z)(t)
 &=\int_v\int_u\alpha_{vu}(x(tvu))\alpha_v(y(u^{-1}))z(v^{-1})\,du\,dv\\
 &=\int_v\int_r\alpha_r(x(tr))\alpha_v(y(r^{-1}v))z(v^{-1})\,dr\,dv\\
 &=(x\star(y\star z))(t).
 \end{aligned}
\]

The double involution is pointwise:

\[
 (x^\#)^\#(t)
 =\Delta(t)^{-1}\Delta(t^{-1})^{-1}
   \alpha_{t^{-1}}(\alpha_t(x(t)))=x(t).
\]

For reversal of order, expand the right-hand side and use \(\Delta(tv)=\Delta(t)\Delta(v)\):

\[
 (y^\#\star x^\#)(t)
 =\Delta(t)^{-1}\int_v
   \alpha_{t^{-1}}(y(v^{-1}t^{-1})^*)\alpha_v(x(v)^*)\,dv.
\]

The other side expands as

\[
 (x\star y)^\#(t)
 =\Delta(t)^{-1}\int_u
   \alpha_{t^{-1}}(y(u^{-1})^*)
   \alpha_{t^{-1}u}(x(t^{-1}u)^*)\,du.
\]

Set \(u=tv\). Left invariance gives the same expression, so \((x\star y)^\#=y^\#\star x^\#\). Associativity, anti-involution and linearity are therefore coefficient identities even for a nonfaithful pair.

The two module operations are \((a\cdot x)(t)=\alpha_{t^{-1}}(a)x(t)\) and \((x\cdot a)(t)=x(t)a\). The same bounded-product and action continuity shows that both fields belong to \(\mathcal C\), with support contained in \(\operatorname{supp}x\). Their five compatibility laws are

\[
 \begin{aligned}
 (a\cdot x)\star y&=a\cdot(x\star y),&
 (x\cdot a)\star y&=x\star(a\cdot y),\\
 (x\star y)\cdot a&=x\star(y\cdot a),&
 (a\cdot x)^\#&=x^\#\cdot a^*,\\
 (x\cdot a)^\#&=a^*\cdot x^\#.
 \end{aligned}
\]

For the first law, \(\alpha_u(\alpha_{(tu)^{-1}}(a))=\alpha_{t^{-1}}(a)\), which factors out of the integral. For the middle balance law, \(\alpha_u(x(tu)a)=\alpha_u(x(tu))\alpha_u(a)\), and \((a\cdot y)(u^{-1})=\alpha_u(a)y(u^{-1})\). The third law factors the constant right multiplier out. For the fourth, the adjoint reverses \(\alpha_t(a)x(t^{-1})\), and \(\alpha_{t^{-1}}\alpha_t(a^*)=a^*\); for the fifth, it reverses \(x(t^{-1})a\), leaving \(\alpha_{t^{-1}}(a^*)\) on the left. These are direct pointwise and integral calculations. Covariance separately gives the represented module identities

\[
 \Phi_{\rho,V}(a\cdot x)=\rho(a)\Phi_{\rho,V}(x),
 \qquad \Phi_{\rho,V}(x\cdot a)=\Phi_{\rho,V}(x)\rho(a).
\]

<a id="ccm-normal-regular-kernel"></a>

### The regular kernel for a possibly nonfaithful normal representation

Let \(\rho:M\to B(H_\rho)\) now be any normal unital representation. No implementing unitary representation on \(H_\rho\) is required. Define on \(L^2(G,H_\rho)\)

\[
 (\pi_\rho(a)\xi)(t)=\rho(\alpha_{t^{-1}}(a))\xi(t),
 \qquad (\lambda_s\xi)(t)=\xi(s^{-1}t).
\]

The multiplication field is strongly continuous and bounded by \(\|a\|\). Applying it to compact scalar tensors and using the bound extends it to \(L^2(G,H_\rho)\), as in [NR3](OA-FLOW-NR.md#oa-flow.nr.3); pointwise products and adjoints on that dense core prove it is a unital *-representation. To prove full ultraweak continuity, take compact scalar tensors \(h\eta,k\zeta\). Their vector coefficient pulls back to the functional

\[
 a\longmapsto\int_G h(t)\overline{k(t)}
       (\omega_{\eta,\zeta}\circ\rho\circ\alpha_{t^{-1}})(a)\,dt.
\]

The functional \(\omega_{\eta,\zeta}\circ\rho\) belongs to \(M_*\) by normality of \(\rho\). [AT3](OA-FLOW-AT.md#oa-flow.at.3) makes its predual orbit norm continuous; L24's Banach-valued compact integral therefore lies in \(M_*\), and evaluation at \(a\) gives the displayed coefficient. Compact tensors approximate arbitrary pairs of Hilbert vectors, and the bound \(\|\omega_{v,w}-\omega_{v',w'}\|\le\|v-v'\|\|w\|+\|v'\|\|w-w'\|\), together with [CP6's norm closure](OA-FLOW-CP.md#oa-flow.cp.6), puts every pulled-back vector coefficient in \(M_*\). Finally [CP4](OA-FLOW-CP.md#oa-flow.cp.4) expresses every ultraweak functional on the target as a square-summable vector series; its pullback series converges in \(M_*\) by the Cauchy--Schwarz tail estimate. This proves normality for the full ultraweak topology, without using faithfulness or a sequential substitute for normality.

Translation is unitary by left invariance and strongly continuous on the dense compact continuous vector fields by [L24](OA-FLOW-L24.md#oa-flow.grp.translations), then on their Hilbert completion. Direct substitution proves \(\lambda_s\pi_\rho(a)\lambda_s^*=\pi_\rho(\alpha_s(a))\). No invariance of \(\ker\rho\) is needed for these definitions.

For \(\xi\in C_c(G,H_\rho)\), left invariance in the change \(s=tu\) yields

\[
 (\Phi_{\pi_\rho,\lambda}(x)\xi)(t)
   =\int_G\rho(\alpha_u(x(tu)))\xi(u^{-1})\,du.
\]

This integral exists for every \(t\). The integration variable is in the fixed compact set \((\operatorname{supp}\xi)^{-1}\); AT4 and normality of \(\rho\) give joint continuity of its vector integrand on the common compact norm bounds. A finite compact cover gives continuity in \(t\), and its support lies in \(\operatorname{supp}x\operatorname{supp}\xi\). Thus it is a compact continuous vector field. To identify it with the Hilbert-space integral, test against compact continuous tensor vectors and use compact-carrier Fubini; the dense tensor core separates vectors in \(L^2\). The operator bound above then extends this equality from that core to the bounded operator on all of \(L^2\); the pointwise kernel assertion is for the displayed continuous core.

This construction asserts no faithful crossed-product identification for an arbitrary \(\rho\). Nor does nonfaithfulness of \(\rho\) force nonfaithfulness of \(\pi_\rho\): for \(M=\mathbb C^2\), the swapping action of \(\mathbb Z/2\mathbb Z\), and \(\rho(a,b)=a\), the regular representation of \(M\) is \(\operatorname{diag}(a,b)\), which is faithful. The faithful regular identification in NR3–4 retains its stated faithfulness hypothesis.
