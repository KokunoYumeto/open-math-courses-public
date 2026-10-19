# Dual fixed points, core commutants and central cocycles

This companion supplies the three core arguments used in Section 7 of *Centrally trivial automorphisms and core normalizers*. It proves the dual fixed-point theorem, the core relative-commutant theorem, and realization of each specified strongly continuous central cocycle. The last section states exactly how they give the normalizer description in **every faithful normal state chart**.

*Selected from independently written programme proofs in Codex (OpenAI), September 2026; proof selection, source reconciliation and integration by GPT-6 Astra (OpenAI), Ultra, October 2026. No human review is claimed. Original programme expression is dedicated under CC0 1.0. The mathematical antecedents and the remaining general foundations are identified below; citations do not incorporate the cited books' text or figures.*

The results are conditional on the explicit general inputs in Section 0. Their proofs are included here, so the reader does not need an inaccessible working-copy path for any of these three arguments.

## 0. General inputs and proof boundaries

**F1 — Regular crossed products and normal core charts.** For a point-ultraweakly continuous action of a locally compact abelian group, the regular coefficient and translation operators generate the crossed product. Faithful normal regular models are normally isomorphic by their specified generator maps. A standard-form representation supplies a strongly continuous unitary implementation of the action. For every n.s.f. weight on a von Neumann algebra, its modular crossed product is a core chart; chart isomorphisms are normal, preserve the specified embedded algebra and intertwine the dual flow. These assertions, and the cocycle identities that construct the chart maps, remain general standard-form and core-construction inputs. The proofs below do not derive them from bounded or tracial representation theory.

**F2 — Modular theory.** The faithful-state Tomita theorem, the bounded KMS strip theorem, the identified modular conjugation of the dual weight, the inner-change derivative formula and the modular restriction to a finite centralizer corner are the precise inputs stated in (R3)–(R6) and (R22) below. In particular, (R22) includes the identification with the actual dual-weight modular conjugation, not just a formal antiunitary calculation. These are general modular inputs with unresolved transitive proof obligations in this selected edition.

**F3 — Scalar harmonic analysis and spectral calculus.** Haar integration, Pontryagin duality, scalar Plancherel, Fourier inversion, the translation/character Weyl commutant, the scalar multiplication maximal abelian algebra, and the elementary distribution facts stated before (R8) are used at their stated scopes. The spectral part includes Stone's theorem, affiliation and Borel calculus for self-adjoint operators, finite scalar spectral measures, scalar Tonelli and dominated convergence. Scalar Fourier uniqueness on \(L^1(\mathbb R)\) is included as a short argument in Section 3. None of these statements is inferred merely from the existence of a trace.

**F4 — Bounded operator, predual and weight foundations.** Polar decomposition, projection joins, bounded strong limits, normal positive-functional separation, Banach–Alaoglu and normal slices are used. The concrete predual, decomposition into four positive normal functionals, fixed multiplication, and bounded faithful-state topology have their supplied proofs in [Bounded-topology foundations](bounded-topology-foundations.md) and [Bounded topology and tracial representations](../src/bounded-topology-and-tracial-representations.md), Section 3A. General positive-functional normality, polar decomposition and projection joins are supplied by [Tracial-normality foundations](tracial-normality-foundations.md). Its WG002–WG003 define semifiniteness by ultraweak density of the finite domain algebra and prove that this algebra is the linear span of finite-weight positive elements; the argument following (R27) verifies that definition directly. Product normal-functional density and normal slices are in [Normal tensor tests and tracial GNS identifications](normal-tensor-and-tracial-product-foundations.md), TF1. The general tensor commutant theorem used in Section 2 is an additional input; TF1 alone is not asserted to prove it.

The proof selection below retains the original formula labels A, R and C, making the used arguments identifiable independently of file names. Section 1 contains the full fixed-point argument (A11)–(A14) of programme provider 22. Section 2 contains the full faithful-state proof (R1)–(R24) of provider 23 and also its arbitrary-algebra corner extension (R25)–(R30). Section 3 contains provider 26's complete spectral realization and normalizer argument through (C27). General dual-action averaging, noncentral stability and topological quotient theorems are separate obligations, not consequences certified by this selection.

## 1. Recovering the coefficient algebra from dual fixed points

Let \(G\) be a locally compact Hausdorff abelian group with Haar measure, and let \(\alpha:G\to\operatorname{Aut}(M)\) be point-ultraweakly continuous, where \(M\ne0\). No separability or countability assumption is imposed. In the standard-form regular model on \(L^2(G,H)\), write

\[
\begin{gathered}
N=M\rtimes_\alpha G,\qquad P=\pi_\alpha(M),\\
[\pi_\alpha(a)\xi](r)=\alpha_{-r}(a)\xi(r),\\
[\lambda_s\xi](r)=\xi(r-s),\\
[Q_\chi\xi](r)=\overline{\chi(r)}\xi(r).
\end{gathered}
\tag{A9}
\]

The standard-form implementers satisfy \(U_s aU_s^*=\alpha_s(a)\) and \(U_{s+t}=U_sU_t\). The character multipliers are strongly continuous: compact-open convergence is uniform on a compactly supported continuous vector function's support; density and their common unitary norm extend convergence to every vector. Conjugation by \(Q_\chi\) and its inverse preserve the regular generators and give the normal dual action

\[
\begin{gathered}
\theta_\chi(\pi_\alpha(a))=\pi_\alpha(a),\\
\theta_\chi(\lambda_s)=\overline{\chi(s)}\lambda_s.
\end{gathered}
\tag{A3}
\]

The Weyl and bounded-tensor inputs F3–F4 give

\[
\begin{gathered}
\{L_s,Q_\chi:s\in G,\chi\in\widehat G\}''=B(L^2(G)),\\
(1_H\otimes B(L^2(G)))'=B(H)\otimes1,\\
[L_s\xi](r)=\xi(r-s).
\end{gathered}
\tag{A5}
\]

**Theorem.** \(N^\theta=\pi_\alpha(M)\).

**Proof.** Coefficients are fixed by (A3). For the reverse inclusion define on \(\mathcal H\)

\[
\begin{gathered}
{}[V_s\xi](r)=U_s\xi(r+s),\\
[W\xi](r)=U_r\xi(r).
\end{gathered}
\tag{A11}
\]

For \(W\), both this formula and the formula with \(U_r^*\) preserve continuity and compact support of vector functions. Pointwise norm equality gives two inverse isometries on a dense class, hence inverse unitaries on \(\mathcal H\). No countable basis is chosen.

Every constant \(b'\in M'\) commutes with the regular generators. Also \(V_s\) commutes with both families: for coefficients use \(U_s\alpha_{-(r+s)}(a)=\alpha_{-r}(a)U_s\); for translations use commutativity of \(G\). Thus all elements of \(N\) commute with these operators.

Take \(x\in N^\theta\). It commutes with every \(Q_\chi\). The unitary \(W\) commutes with \(Q_\chi\) and satisfies

\[
\begin{gathered}
WV_sW^*=1_H\otimes R_s,\\
R_s\xi(r)=\xi(r+s),
\end{gathered}
\tag{A12}
\]

because \(U_rU_sU_{r+s}^*=1\). Hence \(WxW^*\) commutes with \(Q_\chi\) and \(R_s=L_{-s}\). Equation (A5) gives \(WxW^*=a\otimes1\) for some \(a\in B(H)\).

We still have to prove \(a\in M\). For fixed \(b'\in M'\), commutation of \(x\) with \(b'\otimes1\) says that \(a\otimes1\) commutes with the multiplication operator \(W(b'\otimes1)W^*\), whose value is \(U_r b'U_r^*\). For fixed \(\xi,\eta\in H\), the scalar function

\[
k(r)=\langle[a,U_r b'U_r^*]\xi,\eta\rangle
\tag{A13}
\]

is continuous and bounded. Testing the zero operator between \(h\otimes\xi\) and \(g\otimes\eta\) gives \(\int h(r)\overline{g(r)}k(r)\,dr=0\) for every \(h,g\in C_c(G)\). Every compactly supported continuous test function occurs as \(h\overline g\), by choosing a cutoff \(g=1\) on the support of \(h\). Therefore \(k=0\) everywhere: a nonzero value, rotated by a scalar phase, has positive real part in a neighborhood, and a nonnegative nonzero cutoff there would give a positive integral.

In particular \(k(0)=0\) for every fixed \(b',\xi,\eta\), so \([a,b']=0\) for every \(b'\in M'\). Thus \(a\in M''=M\) and

\[
x=W^*(a\otimes1)W=\pi_\alpha(a).
\tag{A14}
\]

The proof tests one continuous scalar function at a time; it does not intersect uncountably many conull sets. Normal regular-model comparison gives the assertion in every permitted model. \(\square\)

## 2. The core relative commutant

Let \(M\) be a nonzero von Neumann algebra, let \(\varphi\) be an n.s.f. weight, and write

\[
\begin{gathered}
C_\varphi=M\rtimes_{\sigma^\varphi}\mathbb R,\\
[\pi_\varphi(x)\xi](s)=\sigma^\varphi_{-s}(x)\xi(s),\\
[\lambda_t\xi](s)=\xi(s-t).
\end{gathered}
\tag{R1}
\]

Lebesgue measure is fixed on \(\mathbb R\). The regular-model comparison (F1) places \(C_\varphi\) inside \(M\bar\otimes B(L^2(\mathbb R))\), using a faithful normal unital representation of \(M\). The chart transports in core-chart input F1 identify the coefficient embeddings and permit a change of n.s.f. weight. The claim to be proved is

\[
\pi_\varphi(M)'\cap C_\varphi=Z(C_\varphi). \tag{R2}
\]

No factor, faithful-state, separable-predual or countable-decomposition hypothesis occurs in (R2). The zero algebra satisfies the corresponding equality directly. Central-cocycle realization is a separate assertion, proved in Section 3 and not used in this relative-commutant proof.

### General modular facts used below

The following general modular facts are prerequisites; none asserts (R2).

For a faithful normal state \(\omega\) on \(P\), its standard GNS data are \(H_\omega,\xi_\omega,J_\omega,\Delta_\omega\), with

\[
J_\omega P J_\omega=P',\qquad
\Delta_\omega^{it}x\Delta_\omega^{-it}=\sigma_t^\omega(x).
\tag{R3}
\]

The state is invariant under its modular group. For \(x,y\in P\), there is a bounded function \(G_{x,y}\), continuous on \(-1\leq\operatorname{Im}z\leq0\) and holomorphic in its interior, satisfying

\[
\begin{gathered}
G_{x,y}(s)=\omega(\sigma^\omega_{-s}(x)y),\\
G_{x,y}(s-i)=\omega(y\sigma^\omega_{-s}(x)),\\
|G_{x,y}(z)|\leq\|x\|\|y\|.
\end{gathered}
\tag{R4}
\]

Linearity and uniqueness of the strip function imply norm-continuous dependence on \(y\), uniformly on the strip. Equation (R4) is the finite-state KMS theorem. No analytic continuation of an arbitrary element \(y\) is asserted.

For an n.s.f. weight \(\Phi\), general Tomita correspondence gives \(J_\Phi N J_\Phi=N'\) in its standard GNS representation. Input F2 identifies the dual weight's conjugation with the explicit coefficient-space conjugation. We use that identification, including its closed-operator content, rather than assuming that a formal antiunitary must be the weight's modular conjugation.

Two further general weight results will be used for corners. With \(\operatorname{Ad}(u)(x)=uxu^*\), the inner derivative formula is

\[
[D(\varphi\circ\operatorname{Ad}(u)):D\varphi]_t
=u^*\sigma_t^\varphi(u).
\tag{R5}
\]

Equal weights have derivative \(1\). If \(p\in M_\varphi\) is a projection with \(0<\varphi(p)<\infty\), then \(\varphi_p=\varphi|_{pMp}/\varphi(p)\) is a faithful normal state and

\[
\sigma_t^{\varphi_p}(x)=\sigma_t^\varphi(x)\quad(x\in pMp). \tag{R6}
\]

Here \(M_\varphi\) denotes the fixed algebra of \(\sigma^\varphi\). We use the semifiniteness convention from F4: the finite domain algebra is ultraweakly dense. None of these general results asserts the crossed-product relative-commutant theorem.

### Scalar distributions and bounded tensor slices

Use the unitary Fourier transform

\[
(\mathcal Ff)(q)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-isq}f(s)\,ds.
\tag{R7}
\]

The required scalar foundations are Plancherel, Fourier inversion on the Schwartz space \(\mathcal S\), integration by parts for compactly supported smooth functions, and the following distribution facts. Partial Fourier transformation preserves tempered distributions; a distribution on \(\mathbb R\) supported at \(0\) is a finite linear combination of derivatives of the Dirac mass; consequently a bounded continuous function whose Fourier transform is supported at \(0\) is constant. Finite sums of products of one-variable test functions are dense in the test-function space on a product, with its usual fixed-compact-support topology. These scalar distribution facts are harmonic-analysis prerequisites.

We also use the von Neumann tensor commutant theorem, normal slice maps, and the identification of the scalar multiplication algebra on \(L^2(\mathbb R)\) with its own commutant. These are bounded tensor and scalar spectral foundations. They do not identify arbitrary operator-valued measurable fields. In particular, the continuous \(P\)-valued functions needed below will be constructed from normal slices.

### A scalar identity forces zero frequency

**Lemma.** Suppose \(H:\mathbb R^2\to\mathbb C\) is bounded and continuous and, for every \(f,g\in C_c^\infty(\mathbb R)\),

\[
\begin{aligned}
&\iiint e^{is(p-q)}f(p)\overline{g(q)}H(q,s)\,dp\,dq\,ds\\
&=\iiint e^{i(s-i)(p-q)}f(p)\overline{g(q)}\\
&\qquad H(p,s)\,dp\,dq\,ds.
\end{aligned}
\tag{R8}
\]

On the left integrate \(p\) first, and on the right integrate \(q\) first; their Fourier decay makes the remaining integrals absolutely convergent. Then \(H(q,s)=H(q,0)\) for all \(q,s\).

**Proof.** The two sides extend to distributions in a compactly supported smooth test function \(\Phi(p,q)\). On the left, integration by parts in \(p\) gives arbitrarily rapid decay in \(s\); on the right use \(q\), including the smooth factor \(e^{p-q}\). Thus equality on product tests implies equality on all \(\Phi\).

Define a tempered distribution \(K\) by

\[
\begin{gathered}
K(h)=\iiint e^{isr}h(r,q)H(q,s)\,dr\,dq\,ds\\
(h\in\mathcal S(\mathbb R^2)),
\end{gathered}
\tag{R9}
\]

where the \(r\) integral is performed first. The partial Fourier transform of a Schwartz function is integrable in \((q,s)\), so boundedness of \(H\) makes (R9) continuous in the Schwartz topology.

Put \(p=q+r\) in the equality for \(\Phi\), and then replace \(q+r\) by \(q\) on its right side. As \(\Phi\) varies, \(h(r,q)=\Phi(q+r,q)\) ranges through all compactly supported smooth functions. We obtain

\[
\begin{gathered}
K(h)=K(Th),\\
(Th)(r,q)=e^r h(r,q-r),\\
(T^{-1}h)(r,q)=e^{-r}h(r,q+r).
\end{gathered}
\tag{R10}
\]

Take a test function \(h\) whose support avoids \(r=0\). A smooth partition splits it into two tests supported respectively in \(r\leq-\varepsilon\) and \(r\geq\varepsilon\), for some \(\varepsilon>0\). For the negative part,

\[
\begin{gathered}
T^nh(r,q)=e^{nr}h(r,q-nr)\longrightarrow0\\
\text{in }\mathcal S(\mathbb R^2).
\end{gathered}
\tag{R11}
\]

Indeed its \(r\)-support stays in a fixed compact set; its \(q\)-support grows at most linearly in \(n\); every fixed derivative and polynomial weight introduces at most a polynomial factor in \(n\), dominated by \(e^{-n\varepsilon}\). Iterating (R10) gives \(K(h)=K(T^nh)\), hence \(K(h)=0\). For the positive part use \(T^{-n}h=e^{-nr}h(r,q+nr)\) and the same estimate. Therefore

\[
\operatorname{supp}K\subset\{0\}\times\mathbb R. \tag{R12}
\]

For \(\eta\in C_c^\infty(\mathbb R)\), set \(h_\eta(s)=\int\eta(q)H(q,s)\,dq\). This is bounded and continuous, and (R12) says that its Fourier transform is supported at \(0\). The one-variable distribution theorem makes \(h_\eta\) a polynomial, and boundedness makes that polynomial constant. Thus

\[
\int\eta(q)\bigl(H(q,s)-H(q,0)\bigr)\,dq=0.
\]

Since \(\eta\) is arbitrary and the integrand is continuous in \(q\), it vanishes everywhere. This proves the lemma. \(\square\)

No finite iterate in (R11) is asserted to vanish globally. Its translated support can move arbitrarily far in \(q\); decay in the Schwartz topology is the reason the distributional limit works.

### A commuting multiplier lies in the centralizer

Let \(\omega\) be a faithful normal state on \(P\), put \(\sigma=\sigma^\omega\), and use its standard representation. Set \(\Pi(x)=(1\otimes\mathcal F)\pi_\omega(x)(1\otimes\mathcal F)^*\). A bounded norm-continuous function \(a:\mathbb R\to P\) defines the bounded multiplication operator \(M_a\) on \(L^2(\mathbb R,H_\omega)\).

**Lemma.** If \(M_a\Pi(x)=\Pi(x)M_a\) for every \(x\in P\), then \(a(q)\in P_\omega\) for every \(q\).

**Proof.** Fix \(x\in P\), and use inner products linear in the first variable. Applying the two Fourier transforms to \(\xi_\omega f\) gives

\[
\begin{aligned}
&\langle\Pi(x)(\xi_\omega f),M_{a^*}(\xi_\omega g)\rangle\\
&={1\over2\pi}\iiint e^{is(p-q)}f(p)\overline{g(q)}\\
&\qquad\omega(a(q)\sigma_{-s}(x))\,dp\,dq\,ds.
\end{aligned}
\tag{R13}
\]

Here the \(p\) integral is taken first. It is a Schwartz Fourier transform, so the remaining integral is bounded by an integrable function. Formula (R13) follows first as an \(H_\omega\)-valued Fourier integral with an \(L^1\) input, and then by the scalar inner product. Its constant is the product of the two factors \((2\pi)^{-1/2}\).

Since \(M_a\) commutes with \(\Pi(x)\), the same inner product equals \(\langle\Pi(x)M_a(\xi_\omega f),\xi_\omega g\rangle\). Fourier transformation, now paired with the Schwartz transform of \(g\), expresses it as

\[
\begin{aligned}
&{1\over2\pi}\iiint e^{is(p-q)}f(p)\overline{g(q)}\\
&\qquad\omega(\sigma_{-s}(x)a(p))\,dq\,dp\,ds.
\end{aligned}
\tag{R14}
\]

This time perform the \(q\) integral first. Although \(a(p)f(p)\) need not have a rapidly decaying Fourier transform, the transform of \(g\) does; this establishes the stated convergence and avoids an unsupported interchange of three absolute integrals.

For fixed \(p\), apply (R4) to \(x,a(p)\). Write its strip function as \(G(z,p)\), and put

\[
b(z)=\int_{\mathbb R}e^{-izq}\overline{g(q)}\,dq.
\]

Uniformly for \(-1\leq\operatorname{Im}z\leq0\), \(b(z)\) decays faster than any power of \(|\operatorname{Re}z|\), by integration by parts. On the compact support of \(f\), the factor \(e^{izp}\) is uniformly bounded on this strip. The bounded holomorphic function \(e^{izp}b(z)G(z,p)\) can therefore be integrated around rectangles in the strip: the vertical sides tend to zero, and dominated convergence permits approaching its boundary lines. We get

\[
\begin{aligned}
&\int_{\mathbb R}e^{isp}b(s)G(s,p)\,ds\\
&=\int_{\mathbb R}e^{i(s-i)p}b(s-i)G(s-i,p)\,ds.
\end{aligned}
\tag{R15}
\]

All bounds are uniform in \(p\in\operatorname{supp}f\), so (R15) may be multiplied by \(f(p)\) and integrated. Equating (R13) and (R14), and using the lower KMS boundary in (R15), yields (R8) with

\[
H(q,s)=\omega(a(q)\sigma_{-s}(x)). \tag{R16}
\]

This \(H\) is bounded and jointly continuous: norm continuity of \(a\) handles its first variable and the modular action's point-ultraweak continuity handles its second, uniformly after a small norm perturbation of \(a\).

The preceding lemma gives

\[
\begin{aligned}
\omega(a(q)\sigma_{-s}(x))&=\omega(a(q)x)\\
&=\omega(\sigma_s(a(q))x).
\end{aligned}
\tag{R17}
\]

The last equality uses invariance of \(\omega\). For fixed \(q,s\), this holds for every \(x\in P\). Take \(x=(\sigma_s(a(q))-a(q))^*\); faithfulness implies \(\sigma_s(a(q))=a(q)\). Thus \(a(q)\in P_\omega\). \(\square\)

### Continuous multipliers obtained by slicing

**Lemma.** In the state regular model, with \(C=P\rtimes_{\sigma^\omega}\mathbb R\),

\[
C'\cap(P\bar\otimes B(L^2(\mathbb R)))\subset C. \tag{R18}
\]

**Proof.** If \(X\) belongs to the left side, it commutes with every \(1\otimes\lambda_t\). Fourier transformation puts it in \(P\bar\otimes L^\infty(\mathbb R)\); denote this transformed operator by \(S\). It commutes with every \(\Pi(x)\).

Multiplication by scalar characters in the original variable commutes with \(\pi_\omega(P)\) and normalizes the translation group. Its conjugation therefore preserves the original relative commutant. In the Fourier variable this is the translation action \(\beta_r\) on the scalar multiplication factor; choose the sign so that \((\beta_rb)(q)=b(q-r)\).

For \(k\in C_c^\infty(\mathbb R)\), define the normal average \(S_k=\int k(r)\beta_r(S)\,dr\). It is the multiplication operator of the bounded norm-continuous function

\[
\begin{gathered}
a_k(q)=(\operatorname{id}\otimes\ell_{k,q})(S),\\
\ell_{k,q}(b)=\int_{\mathbb R}k(q-v)b(v)\,dv.
\end{gathered}
\tag{R19}
\]

Indeed \(\|\ell_{k,q}\|\leq\|k\|_1\) and

\[
\begin{aligned}
&\|a_k(q)-a_k(q')\|\\
&\leq\|S\|\,\|k(q-\cdot)-k(q'-\cdot)\|_1.
\end{aligned}
\tag{R20}
\]

Translation continuity in \(L^1\) proves norm continuity. To verify the multiplier identity, check it first on elementary tensors. For general \(S\), test on elementary vector sections and use normal slice maps and scalar Fubini. Both resulting functionals of \(S\) are normal: the scalar kernels are \(L^1\), with norm bounded by \(\|k\|_1\) times the norms of the tested vectors. Ultraweak density of elementary tensors proves the identity. This construction does not choose a measurable \(P\)-valued representative for \(S\).

Each \(S_k\) still commutes with \(\Pi(P)\), so the KMS multiplier lemma places every \(a_k(q)\) in \(P_\omega\). Its multiplication operator consequently belongs to \(P_\omega\bar\otimes L^\infty(\mathbb R)\). For completeness, uniformly approximate \(a_k\) by finite step functions on each compact interval, using norm continuity, then let those intervals increase to \(\mathbb R\). The bounded multipliers converge strongly on \(L^2\) vectors and all approximants belong to that tensor algebra.

Transform back. The algebra \(P_\omega\bar\otimes\{\lambda_t:t\in\mathbb R\}''\) lies in \(C\), because \(\pi_\omega(y)=y\otimes1\) for \(y\in P_\omega\). Thus every average \(X_k\) lies in \(C\). Choose nonnegative \(k_n\) of integral \(1\) supported in \([-1/n,1/n]\). The scalar character unitaries are strongly continuous, so \(X_{k_n}\to X\) ultraweakly. Since \(C\) is ultraweakly closed, \(X\in C\), proving (R18). \(\square\)

It follows in fact that the left side of (R18) is \(Z(C)\): one inclusion has just been proved, and \(Z(C)\subset C\subset P\bar\otimes B(L^2(\mathbb R))\).

### Modular conjugation reverses the orientation

**Theorem.** If \(P\) has a faithful normal state \(\omega\), then

\[
\pi_\omega(P)'\cap C_\omega=Z(C_\omega). \tag{R21}
\]

**Proof.** For the action \(\sigma^\omega\), the standard implementers are \(U_s=\Delta_\omega^{is}\). The conjugation formula in dual modular-conjugation input F2 and its weight identification in the same input F2 give

\[
\begin{gathered}
{}[\mathcal J\xi](s)=\Delta_\omega^{-is}J_\omega\xi(-s),\\
\mathcal J C_\omega\mathcal J=C_\omega'.
\end{gathered}
\tag{R22}
\]

The modular unitaries commute with \(J_\omega\) as operators, taking its antilinearity into account. Directly on vector sections,

\[
\begin{aligned}
&[\mathcal J\pi_\omega(x)\mathcal J\xi](s)\\
&=\Delta_\omega^{-is}J_\omega\sigma_s^\omega(x)
  \Delta_\omega^{is}J_\omega\xi(s)\\
&=\Delta_\omega^{-is}\bigl(J_\omega\sigma_s^\omega(x)J_\omega\bigr)
  \Delta_\omega^{is}\xi(s)\\
&=J_\omega xJ_\omega\xi(s).
\end{aligned}
\tag{R23}
\]

Thus \(\mathcal J\pi_\omega(P)\mathcal J=P'\otimes1\). The tensor commutant theorem and (R22) show

\[
\begin{aligned}
&\mathcal J(\pi_\omega(P)'\cap C_\omega)\mathcal J\\
&= (P\bar\otimes B(L^2(\mathbb R)))\cap C_\omega'\\
&= Z(C_\omega).
\end{aligned}
\tag{R24}
\]

The second equality is (R18). Conjugation by \(\mathcal J\) carries \(Z(C_\omega)\) onto \(Z(C_\omega')=Z(C_\omega)\), since it carries \(C_\omega\) onto its commutant. Apply it once more to (R24) to obtain (R21). \(\square\)

The orientation in (R24) matters. The ambient tensor relative commutant in (R18) is not the target in (R21); the identified modular conjugation is the bridge between them.

### Enough finite fixed projections for a weight

**Lemma.** Every nonzero von Neumann algebra \(M\) admits an n.s.f. weight \(\psi\) and an orthogonal family \((p_i)_{i\in I}\) such that

\[
\sum_{i\in I}p_i=1,\qquad p_i\in M_\psi,\qquad\psi(p_i)=1,
\tag{R25}
\]

and each \(p_iMp_i\) has a faithful normal state. The sum is the strong supremum of finite partial sums; \(I\) need not be countable.

**Proof.** Every nonzero corner contains a nonzero normal positive functional. Its support \(p\) is a nonzero projection, and its normalized restriction to \(pMp\) is a faithful normal state. Take a maximal orthogonal family of such support projections, using Zorn's lemma. If its strong sum were smaller than \(1\), the residual corner would supply another support, contradicting maximality.

Choose faithful normal states \(\omega_i\) on the corners and put, for \(x\geq0\),

\[
\psi(x)=\sum_{i\in I}\omega_i(p_i x p_i). \tag{R26}
\]

An arbitrary nonnegative sum means the supremum of its finite partial sums. Normality follows by interchanging two suprema over increasing positive nets and finite subsets. If \(\psi(x)=0\), faithfulness of all \(\omega_i\) implies \(p_i x p_i=0\), hence \(x^{1/2}p_i=0\) for every \(i\); their strong sum is \(1\), so \(x=0\).

For finite \(F\subset I\), let \(p_F=\sum_{i\in F}p_i\). Then \(\psi(p_F)=|F|\), and for \(a\in M\),

\[
\psi((ap_F)^*(ap_F))\leq\|a\|^2|F|. \tag{R27}
\]

Thus \(Mp_F\subset\mathfrak n_\psi\), and \(ap_F\to a\) strongly. To verify semifiniteness with the stated domain-algebra convention directly, every positive \(b\in p_FMp_F\) has \(\psi(b)\leq\|b\|\,|F|<\infty\). Decomposing a corner element into its positive and negative real and imaginary parts gives \(p_FMp_F\subset\mathfrak m_\psi\). The bounded net \(p_Fap_F\) converges strongly to \(a\), hence ultraweakly. Therefore \(\mathfrak m_\psi\) is ultraweakly dense, proving semifiniteness.

Fix \(i\) and put \(u=1-2p_i\). Each compression in (R26) is unchanged by \(\operatorname{Ad}(u)\), so \(\psi\circ\operatorname{Ad}(u)=\psi\). By (R5), \(u^*\sigma_t^\psi(u)=1\), whence \(\sigma_t^\psi(p_i)=p_i\). The corner restriction of \(\psi\) is exactly \(\omega_i\), and (R6) identifies its modular group. \(\square\)

**Corner identification.** If \(p\in M_\psi\) and \(0<\psi(p)<\infty\), then

\[
\pi_\psi(p)C_\psi\pi_\psi(p)
\cong(pMp)\rtimes_{\sigma^{\psi_p}}\mathbb R
\tag{R28}
\]

by the coefficient embedding \(x\mapsto\pi_\psi(x)\) and translations \(t\mapsto\pi_\psi(p)\lambda_t\), with unit \(\pi_\psi(p)\).

To prove this, \(\pi_\psi(p)=p\otimes1\) and it commutes with every \(\lambda_t\). The ultraweakly dense algebraic span of \(\pi_\psi(a)\lambda_t\) compresses to the span of \(\pi_\psi(pap)\lambda_t\). On \(L^2(\mathbb R,pH_\psi)\) these are exactly the regular generators of the corner action in (R6), with a faithful normal unital coefficient representation of \(pMp\). The regular-model comparison (F1) gives the normal model identification, and the compressed dense span proves surjectivity onto the full corner. No assertion that \(\pi_\psi(p)\) is central in \(C_\psi\) is needed.

### The relative commutant for every algebra

**Theorem.** For every von Neumann algebra \(M\), every n.s.f. weight \(\varphi\), and its modular crossed product,

\[
\pi_\varphi(M)'\cap C_\varphi=Z(C_\varphi). \tag{R29}
\]

Consequently the canonical core satisfies \(M'\cap C(M)=Z(C(M))\), in particular for every factor, with no countability assumption.

**Proof.** First use the diagonal weight \(\psi\) from (R25). If \(X\in\pi_\psi(M)'\cap C_\psi\), it commutes with every \(\pi_\psi(p_i)\). Its compression

\[
X_i=\pi_\psi(p_i)X\pi_\psi(p_i)
\]

commutes with the corner coefficient algebra \(\pi_\psi(p_iMp_i)\). By (R28) and the faithful-state theorem, \(X_i\) is central in the core corner. In particular it commutes with \(\pi_\psi(p_i)\lambda_t\). Because \(X\) and \(\lambda_t\) both commute with \(\pi_\psi(p_i)\), this says

\[
[X,\lambda_t]\pi_\psi(p_i)=0\quad(i\in I,\ t\in\mathbb R). \tag{R30}
\]

Finite sums of these projections increase strongly to \(1\), so (R30) gives \([X,\lambda_t]=0\). The element \(X\) already commutes with \(\pi_\psi(M)\); these elements and the translations generate \(C_\psi\), hence \(X\in Z(C_\psi)\). The reverse inclusion is immediate.

For the original weight \(\varphi\), the normal chart isomorphism from core-chart input F1 sends \(\pi_\psi(x)\) to \(\pi_\varphi(x)\), and therefore transports both the relative commutant and the center. This proves (R29) in every chart and in the canonical glued core. \(\square\)

This proves the relative-commutant statement used in the normalizer application in Section 4, subject to the general foundations stated above. Central-cocycle realization is supplied in Section 3; additional topological characteristic-square conclusions remain separate.

## 3. Realizing each specified central cocycle

Let \(M\ne0\) be a von Neumann algebra and let \(C=C(M)\) be the core constructed in core-chart input F1, with its embedded copy of \(M\) and dual action \(\theta\). A central unitary cocycle means a strongly continuous map

\[
\begin{gathered}
c:\mathbb R\longrightarrow\mathcal U(Z(C)),\\
c(s+t)=c(s)\theta_s(c(t)).
\end{gathered}
\tag{C1}
\]

The equation gives \(c(0)=1\). Strong and strong-star continuity agree for unitary-valued maps. We will prove

\[
\begin{gathered}
\text{there is }v\in\mathcal U(C)\text{ such that }\\
\theta_t(v)=v c(t),\qquad c(t)=v^*\theta_t(v)\\
(t\in\mathbb R).
\end{gathered}
\tag{C2}
\]

The unitary is allowed to lie in the full core. Requiring it to be central would be a different assertion and can fail. The factor case of (C2) is the realization needed in the normalizer application in Section 4.

### The translating spectral coordinate

Choose any n.s.f. weight \(\varphi\) on \(M\) and use its chart \(C_\varphi=M\rtimes_{\sigma^\varphi}\mathbb R\). Stone’s theorem, applied to the core translation group as detailed below, gives a positive nonsingular affiliated operator \(h\) with

\[
h^{it}=\lambda_\varphi(t),\qquad \theta_s(h)=e^{-s}h.
\tag{C3}
\]

Put \(P=\log h\). By spectral calculus,

\[
P=P^*,\qquad \theta_s(P)=P-s1.
\tag{C4}
\]

These are identities of affiliated operators through their spectral projections. The logarithm has full spectral meaning because \(h\) has zero kernel; it need not be bounded. No dominant weight or extra weight-cocycle reconstruction theorem is used here.

Only the core's translation generators and Stone's theorem are needed for this translating coordinate. Let \(P\) be the self-adjoint generator of the strongly continuous group \(t\mapsto\lambda_\varphi(t)\). Its spectral projections belong to the core, and \(h=e^P\) is positive, nonsingular and affiliated, with \(h^{it}=\lambda_\varphi(t)\). For a fixed \(s\), the dual-action formula gives
\[
\begin{gathered}
\theta_s(e^{itP})=e^{-ist}e^{itP}=e^{it(P-s1)}.
\end{gathered}
\]
Stone uniqueness and normal spectral transport yield (C4), and exponentiation yields (C3). Thus realization does not need an additional trace-density identification of \(h\). The general modular and chart inputs constructing the core remain F1–F2.

### Spectral and von Neumann algebra prerequisites

We use the following general spectral, integration, and von Neumann algebra results.

We use the bounded spectral calculus for a self-adjoint operator, its finite scalar spectral measures under normal positive functionals, scalar Tonelli on Lebesgue measure times a finite measure, and dominated convergence. We also use compact ultraweak integrals of bounded strongly continuous operator functions, normality of multiplication by fixed bounded operators, polar decomposition, projection joins and bounded strong limits. We also use the duality \(A=(A_*)^*\) and weak-star compactness of its unit ball (Banach–Alaoglu), and the decomposition of every normal functional as a complex linear combination of four positive normal functionals. These are the exact spectral, integration and von Neumann-algebra foundations used below.

The scalar Fourier prerequisite is uniqueness on \(L^1(\mathbb R)\): if \(g\in L^1\) and \(\int e^{-irs}g(s)\,ds=0\) for every \(r\), then \(g=0\) almost everywhere. The following paragraph supplies it from scalar Plancherel and elementary integration. Fourier transforms of \(L^1\) functions are continuous by dominated convergence. No vector-valued disintegration theorem is used.

For the final application to normalizers, Sections 1 and 2 give

\[
C^\theta=M,\qquad M'\cap C=Z(C).
\tag{C5}
\]

The realization proof itself will not use (C5). Joint strong evaluation of the action on bounded sets is given by the standard-form implementation in F1 and bounded strong multiplication. Normal chart maps from F1 transport all the conclusions to the abstract core.

**Scalar Fourier uniqueness.** Suppose \(g\in L^1(\mathbb R)\) and its Fourier transform vanishes. Let \(\eta_\varepsilon(s)=(\sqrt\pi\varepsilon)^{-1}e^{-s^2/\varepsilon^2}\). The convolution \(g*\eta_\varepsilon\) belongs to \(L^1\cap L^2\): Fubini gives its \(L^1\) bound, and weighted Cauchy–Schwarz followed by Fubini gives \(\|g*\eta_\varepsilon\|_2\le\|g\|_1\|\eta_\varepsilon\|_2\). Its Fourier transform is zero by Fubini and the convolution identity. Scalar Plancherel makes \(g*\eta_\varepsilon=0\). Finally,
\[
\begin{aligned}
\|g*\eta_\varepsilon-g\|_1
&\le\int_{\mathbb R}\eta_\varepsilon(s)
\|g(\cdot-s)-g\|_1\,ds\\
&\longrightarrow0.
\end{aligned}
\]
For this limit, translations are continuous in \(L^1\), first for compactly supported continuous functions and then by density; the Gaussian mass outside any fixed neighborhood of zero tends to zero, and the integrand norm is at most \(2\|g\|_1\). Hence \(g=0\). This proves the exact scalar uniqueness used below from the declared Plancherel and integration inputs.

### Reduce to a commutative algebra

Let \(A\subset C\) be the von Neumann algebra generated by \(Z(C)\) and the spectral projections of \(P\). It is abelian: the spectral projections commute with one another, and the center commutes with all of them. It is invariant under \(\theta\) by (C4) and invariance of \(Z(C)\). Every \(c(t)\) belongs to \(A\).

We prove a more general intermediate statement. Suppose \(A\) is any abelian von Neumann algebra, \(\theta\) is a point-ultraweakly continuous real action, \(P\) is affiliated with \(A\) and satisfies (C4), and \(c:\mathbb R\to\mathcal U(A)\) is a strongly continuous cocycle. Then (C2) has a solution in \(\mathcal U(A)\). This statement requires no trace on \(A\).

The linear maps

\[
\beta_t(a)=c(t)^*\theta_t(a)\qquad(a\in A)
\tag{C6}
\]

form a group of normal linear isometries. Indeed commutativity and (C1) give \(\beta_s\beta_t=\beta_{s+t}\), and the inverse is \(\beta_{-t}\). They need not be algebra automorphisms or preserve the identity. A fixed vector \(a\) for these maps satisfies \(\theta_t(a)=c(t)a\).

### A spectral majorant with total value one

Use the strictly positive continuous function

\[
k(x)=\frac1{\pi(1+x^2)},\qquad \int_{\mathbb R}k(x)\,dx=1.
\tag{C7}
\]

It is uniformly continuous and vanishes at infinity. Its strict positivity implies that \(k(P)\) has support \(1\), even when it has no bounded inverse. For every \(s\),

\[
\theta_s(k(P))=k(P-s).
\tag{C8}
\]

For a normal positive functional \(\omega\) on \(A\), its scalar spectral measure \(\nu_\omega(B)=\omega(1_B(P))\) is finite, with mass \(\omega(1)\). Scalar Tonelli gives

\[
\begin{aligned}
&\int_{\mathbb R}\omega(k(P-s))\,ds\\
&=\int_{\mathbb R}\int_{\mathbb R}k(x-s)\,ds\,d\nu_\omega(x)\\
&=\omega(1).
\end{aligned}
\tag{C9}
\]

In particular the compact positive integrals obey

\[
\begin{gathered}
0\le\int_{-n}^{n}k(P-s)\,ds\le1,\\
\int_{-n}^{n}k(P-s)\,ds\uparrow1.
\end{gathered}
\tag{C10}
\]

For the last assertion, their bounded scalar spectral functions increase pointwise to one. Monotone spectral convergence gives the strong supremum, or equivalently (C9) gives it against every normal positive functional. The sequence here exhausts the specified real parameter, not the Hilbert space or a noncountable family of normal functionals.

### Bounded twisted averages

For each frequency \(r\in\mathbb R\) set

\[
\begin{gathered}
b_r=k(P)e^{irP},\\
z_r(s)=\beta_s(b_r)\\
=c(s)^*k(P-s)e^{ir(P-s)}.
\end{gathered}
\tag{C11}
\]

This is a bounded strongly continuous \(A\)-valued function of \(s\). In addition to continuity of \(c\), use norm continuity of \(s\mapsto k(P-s)\) and \(e^{ir(P-s)}=e^{-irs}e^{irP}\). Its modulus is

\[
|z_r(s)|=k(P-s).
\tag{C12}
\]

The compact integrals \(a_{r,n}=\int_{-n}^{n}z_r(s)\,ds\) exist as ultraweak integrals. They satisfy

\[
|a_{r,n}|\le\int_{-n}^{n}k(P-s)\,ds\le1.
\tag{C13}
\]

Here is a direct justification of the first inequality. For every unitary \(w\in A\), commutativity and (C12) give \(\operatorname{Re}(w^*z_r(s))\le k(P-s)\). Integrate that inequality. The polar part of \(a_{r,n}\) extends to a unitary of \(A\) by adding the complementary support projection; choosing this \(w\) gives \(\operatorname{Re}(w^*a_{r,n})=|a_{r,n}|\).

For positive normal \(\omega\), positivity on the abelian algebra gives \(|\omega(z_r(s))|\le\omega(|z_r(s)|)\). This follows, for example, by Cauchy–Schwarz for the positive functional weighted by \(|z_r(s)|\), with the unitary extension of its polar part. Equations (C9) and (C12) imply scalar absolute integrability. Every normal functional is a complex linear combination of four positive normal functionals, so this holds for all of \(A_*\).

The integrals \(a_{r,n}\) therefore converge at every normal functional. Their uniform norm bound in (C13) and weak-star compactness of the unit ball show that the limit is an element \(a_r\in A\), with \(\|a_r\|\le1\). Thus

\[
a_r=\int_{\mathbb R}\beta_s(b_r)\,ds
\tag{C14}
\]

is an actual bounded ultraweak integral. Its notation does not assert operator-norm Bochner integrability.

Each \(\beta_t\) is normal and bounded linear. Passing it through the scalar-tested integral and translating the real parameter gives

\[
\begin{gathered}
\beta_t(a_r)=\int_{\mathbb R}\beta_{t+s}(b_r)\,ds=a_r,\\
\theta_t(a_r)=c(t)a_r.
\end{gathered}
\tag{C15}
\]

All translated scalar integrals are absolutely convergent by the preceding bounds and normality of the functionals composed with \(\beta_t\).

### Partial implementers and invariant supports

Write the polar decomposition \(a_r=u_r|a_r|\), with support projection \(p_r=s(|a_r|)\). Because \(A\) is abelian,

\[
u_r^*u_r=u_ru_r^*=p_r.
\tag{C16}
\]

Equation (C15) gives \(\theta_t(|a_r|)=|a_r|\) and hence \(\theta_t(p_r)=p_r\). Uniqueness of the polar decomposition gives

\[
\theta_t(u_r)=c(t)u_r.
\tag{C17}
\]

Indeed the right side has the same initial and final support \(p_r\) and, multiplied by \(|a_r|\), is \(\theta_t(a_r)\). If \(a_r=0\), these assertions simply use \(u_r=p_r=0\).

### Rational Fourier probes cover the identity

**Lemma.** \(\bigvee_{r\in\mathbb Q}p_r=1\).

**Proof.** Set \(q=1-\bigvee_{r\in\mathbb Q}p_r\). It is a \(\theta\)-invariant projection in \(A\). For rational \(r\), \(q a_r=0\). Pull the fixed factor \(e^{irP}\) out of (C14), using (C11), to get

\[
\int_{\mathbb R}e^{-irs}q c(s)^*k(P-s)\,ds=0
\quad(r\in\mathbb Q).
\tag{C18}
\]

For any positive normal functional \(\omega\) on \(A\), the function

\[
g_\omega(s)=\omega(q c(s)^*k(P-s))
\tag{C19}
\]

is continuous. It is in \(L^1\), because its absolute value is at most \(\omega(q k(P-s))\), whose integral is \(\omega(q)\) by (C9) applied to the positive normal functional \(a\mapsto\omega(qa)\). Equation (C18) says its Fourier transform vanishes on \(\mathbb Q\). Continuity of that transform makes it zero on all of \(\mathbb R\). Fourier uniqueness gives \(g_\omega=0\) almost everywhere, and scalar continuity makes it zero everywhere.

At \(s=0\) this says \(\omega(qk(P))=0\), since \(c(0)=1\). It holds for all positive normal functionals, so \(qk(P)=0\). The operator \(k(P)\) has support \(1\). Its spectral projections \(1_{[1/n,\infty)}(k(P))\) increase to \(1\), and \(qk(P)=0\) forces their products with \(q\) to vanish. Therefore \(q=0\). \(\square\)

Rational parameters suffice because an individual scalar Fourier transform is continuous. The projections \(p_r\) are not assumed finite or sigma finite; this countable family does not restrict the dimension or predual of \(A\).

### Assemble the unitary

Enumerate \(\mathbb Q\) as \((r_n)_{n\ge1}\) and define

\[
\begin{gathered}
e_1=p_{r_1},\\
e_n=p_{r_n}\prod_{j<n}(1-p_{r_j})\quad(n\ge2).
\end{gathered}
\tag{C20}
\]

The projections commute, are invariant under \(\theta\), and are pairwise orthogonal. Their finite sums equal \(\bigvee_{j\le n}p_{r_j}\), so they increase strongly to \(1\). Set

\[
v_N=\sum_{n=1}^N e_nu_{r_n}.
\tag{C21}
\]

The summands have initial and final support \(e_n\). Orthogonality gives
\(v_N^*v_N=v_Nv_N^*=\sum_{n\le N}e_n\) and \(\|v_N\|\le1\). On any faithful normal representation and any vector \(\xi\),

\[
\begin{gathered}
\|(v_L-v_N)\xi\|^2
=\sum_{N<n\le L}\|e_n\xi\|^2\\
\longrightarrow0\qquad(L\ge N\longrightarrow\infty).
\end{gathered}
\tag{C22}
\]

The same estimate holds for the adjoints. Thus \(v_N\to v\) and \(v_N^*\to v^*\) strongly, for an element \(v\in A\). Products of uniformly bounded strongly convergent operators converge strongly, giving \(v^*v=vv^*=1\).

Equations (C17) and invariance of \(e_n\) give \(\theta_t(v_N)=c(t)v_N\). A normal automorphism preserves bounded strong-star convergence. Taking the limit gives

\[
\theta_t(v)=c(t)v=v c(t)\qquad(t\in\mathbb R).
\tag{C23}
\]

This proves (C2) in the abstract abelian setting. The strong-limit argument is vectorwise and works on Hilbert spaces of arbitrary dimension. It is not an assertion that every strong operator topology here is first countable.

### Realize the cocycle in the core

**Theorem.** For every von Neumann algebra \(M\) and every strongly continuous central cocycle (C1) of its core's dual flow, a unitary \(v\in C(M)\) satisfies (C2). In any chosen weight chart it may be chosen in the abelian algebra generated by \(Z(C)\) and the spectral projections of \(\log h_\varphi\).

**Proof.** Stone’s theorem and the dual-action generator formula give (C4), and the abelian reduction above supplies the invariant abelian algebra containing the entire cocycle. Equations (C7)–(C23) prove realization there. A normal chart isomorphism transports the cocycle, spectral data, resulting unitary and identity, so the conclusion holds in the chart-independent core. If \(M=0\), all algebras are zero and the assertion has its usual zero-algebra interpretation. \(\square\)

In particular this supplies the realization required for factors in the normalizer application in Section 4, under the stated foundations. The argument does not assume the stronger theorem that all, possibly noncentral, unitary cocycles of every trace-scaling action are coboundaries. Commutativity of the intermediate algebra is used in (C6), (C12)–(C13), the invariant polar supports and their assembly.

The chosen unitary commutes with every \(h_\varphi^{it}=\lambda_\varphi(t)\). This extra property is a consequence of where it was constructed, not an additional hypothesis on the cocycle.

### Realization and the normalizing inclusions

Suppose \(v\) satisfies (C2), and take \(x\in M=C^\theta\). Centrality of \(c(t)\) gives

\[
\begin{gathered}
\theta_t(vxv^*)=v c(t)x c(t)^*v^*=vxv^*,\\
\theta_t(v^*xv)=c(t)^*v^*xv c(t)=v^*xv.
\end{gathered}
\tag{C24}
\]

Both elements belong to \(M\) by the full fixed-point theorem (C5). Hence \(vMv^*\subset M\) and \(v^*Mv\subset M\); conjugating the second inclusion gives the reverse of the first. Thus \(vMv^*=M\).

If \(v,w\) realize the same \(c\), then

\[
\theta_t(wv^*)=w c(t)c(t)^*v^*=wv^*.
\tag{C25}
\]

Therefore \(wv^*\in\mathcal U(M)\) and \(w=a v\) for \(a\in\mathcal U(M)\). Conversely, every \(av\) with \(a\in\mathcal U(M)\) realizes \(c\). The set of all realizing unitaries is exactly \(\mathcal U(M)v\). This is an existence and fiber statement; it asserts no continuous choice of \(v\) as \(c\) varies.

### The characteristic-square discrepancy map

Let \(E=\{u\in\mathcal U(C):uMu^*=M\}\) and give it the strong unitary topology. For \(u\in E\) define

\[
\delta(u)(t)=u^*\theta_t(u).
\tag{C26}
\]

This lies in \(\mathcal U(Z(C))\). Indeed, for \(x\in M\), both \(x\) and \(uxu^*\) are fixed. The identity
\(\theta_t(u)x\theta_t(u)^*=uxu^*\) says \(u^*\theta_t(u)\) commutes with \(x\). The relative-commutant theorem (C5) places it in \(Z(C)\).

The action law gives the cocycle equation, and strong continuity gives the required continuous curve. Centrality then implies

\[
\begin{gathered}
\delta(uv)(t)=\delta(u)(t)\delta(v)(t),\\
\ker\delta=\mathcal U(M).
\end{gathered}
\tag{C27}
\]

For the product, expand \(v^*u^*\theta_t(u)\theta_t(v)\) and commute the central discrepancy past \(v\). For the kernel, (C26) is identically one exactly when \(u\) is fixed, so use (C5). The realization and normalizer results make \(\delta\) onto every strongly continuous central cocycle. Thus the middle-row surjectivity used in Section 4 is now an actual conditional theorem.

The map \(\delta\) is continuous into the cocycle space with the topology of uniform convergence on compact time sets for the strong unitary topology. The map \((t,u)\mapsto u^*\theta_t(u)\) is jointly continuous by standard-form implementation in F1 and the strong topological-group operations on unitaries. For a compact time set, a finite cover by neighborhoods witnessing that joint continuity gives a single neighborhood of \(u\) controlling the discrepancy uniformly in time. This proves the claimed function-space continuity without metrizability or separability assumptions. Quotient-topology comparisons and Polish conclusions require separate topological hypotheses and proofs.

For nonfactor \(M\), the fixed central unitaries are \(\mathcal U(Z(M))\), by (C5) and centrality. They reduce to \(\mathbb T\) for a factor. The present extension to arbitrary \(M\) does not change that distinction in the characteristic-square application.

## 4. The description in every faithful normal state chart

Fix **any** faithful normal state \(\varphi\) on \(M\), and use the specified embedding of \(M\) in \(C_\varphi\). Let

\[
E_\varphi
=\{V\in\mathcal U(C_\varphi):VMV^*=M\}.
\]

Sections 1–3 prove that

\[
\begin{gathered}
\delta_\varphi:E_\varphi\longrightarrow
Z^1(\mathbb R,\mathcal U(Z(C_\varphi))),\\
\delta_\varphi(V)(s)=V^*\theta_s(V)
\end{gathered}
\tag{B1}
\]

is onto and has kernel \(\mathcal U(M)\). Here \(Z^1\) consists of the specified strongly continuous cocycles with the equation (C1), not just their cohomology classes.

For such a cocycle \(c\), choose the realizer \(V_c^\varphi\) constructed in Section 3. It lies in the abelian algebra generated by \(Z(C_\varphi)\) and the spectral projections of \(P_\varphi\); hence it commutes with every \(\lambda_\varphi(t)=e^{itP_\varphi}\). Both inclusions in (C24) show that

\[
\alpha_c^\varphi
=\operatorname{Ad}(V_c^\varphi)|_M
\in\operatorname{Aut}(M).
\tag{B2}
\]

Normality follows from normality of inner conjugation and of the specified coefficient inclusion; the inverse is the restriction of conjugation by \((V_c^\varphi)^*\).

If \(V\in E_\varphi\), put \(c=\delta_\varphi(V)\). Equation (C25) gives

\[
\begin{gathered}
u=V(V_c^\varphi)^*\in\mathcal U(M),\\
V=uV_c^\varphi,\\
\operatorname{Ad}(V)|_M
=\operatorname{Ad}(u)\circ\alpha_c^\varphi.
\end{gathered}
\tag{B3}
\]

Conversely every product \(uV_c^\varphi\) is a core normalizer. A different realizer of the same specified cocycle is exactly a left multiple by a unitary of \(M\), so this change is absorbed into \(u\). No continuous selection of realizers is asserted.

To compare states, let \(J_{\psi,\varphi}:C_\varphi\to C_\psi\) be the normal chart isomorphism in F1. It is the identity on the specified copy of \(M\) and intertwines the dual actions. Therefore it maps centers to centers, normalizers to normalizers, and

\[
\begin{aligned}
&J_{\psi,\varphi}(V^*\theta_s(V))\\
&=J_{\psi,\varphi}(V)^*
  \theta_s(J_{\psi,\varphi}(V)).
\end{aligned}
\tag{B4}
\]

The transported realizer need not be the spectral choice made in the new chart; (C25) supplies the exact left unitary relating them. Thus the existence statement (B3) holds in every faithful normal state chart. It is not limited to one dominant weight, a tracial state or a specially normalized state. For a separable-predual factor a faithful normal state exists by the supplied bounded-topology foundation. Combining (B3) with the consumer's independently proved equality of centrally trivial automorphisms and core-normalizer restrictions gives precisely its every-faithful-state formulation; the present companion does not itself prove that type \({\rm III}_0\) classification theorem.

## 5. Source roles, provenance and remaining work

The mathematical fixed-point antecedent is Takesaki, *Theory of Operator Algebras II*, X.2.3(i), printed pp. 259–261. Section 1 retains the earlier programme's spatial proof: two explicitly checked families lie in the regular commutant, the Weyl relation removes the group coordinate, and a continuous scalar test returns the coefficient to \(M\). It does not require the whole crossed-product commutant theorem used in the book's route.

The Fourier–KMS method behind Section 2 is Takesaki II, XII.1.7–1.9, printed pp. 370–375. The normalization in (R13)–(R14) is computed from the specified unitary Fourier transform. The distribution argument uses exponential decay in Schwartz seminorms on the two half-lines; moving support alone does not make a finite iterate vanish. The identified dual-weight conjugation proves the needed orientation change, and the explicit corner argument retains arbitrary-algebra scope. The core relative-commutant and normalizer targets are XII.6.13–6.15, printed pp. 449–452.

Section 3 retains the programme's direct spectral-averaging proof of central cocycle realization. Takesaki II, XII.1.11 and XII.6.15, provide the broader classical stability and normalizer context. The proof here uses commutativity, an integrable scalar spectral majorant, rational Fourier probes, invariant polar supports and their strong sum. Its conclusion concerns each specified central cocycle; the full noncentral stability theorem remains separate. The translating coordinate follows directly from the crossed-product unitary group and Stone's theorem, as explained in Section 3.

The every-faithful-state target used by the consumer is Takesaki, *Theory of Operator Algebras III*, XVIII.2.8(ii), printed p. 326. The Takesaki volumes cited are *Theory of Operator Algebras II* and *III* (Springer, 2003). Their mathematical ideas are credited here; no source-book prose, figures or exercise sequence is reproduced. Publisher records: [Takesaki II](https://doi.org/10.1007/978-3-662-10451-4), [Takesaki III](https://doi.org/10.1007/978-3-662-10453-8).

The selected programme proofs were written in Codex (OpenAI), September 2026, and carried a CC0 notice for their original expression. Their headers do not identify an exact model, so none is invented here. This companion retains those mathematical arguments and their formula labels, with explicit learner-facing inputs, one scalar Fourier-uniqueness proof, a direct Stone-coordinate explanation and the chart comparison (B1)–(B4). The selection does not replace the broader original provider lessons or claim completion of their unselected topics or exercises. The consumer's eight solutions remain in that lesson.

Remaining general proof obligations are F1–F3 and the explicitly named tensor-commutant portion of F4. In particular, standard form, KMS, the actual dual-weight modular conjugation, core-chart functoriality, unbounded spectral calculus and the stated scalar distribution foundations remain distinct from the supplied bounded/tracial arguments. General operator-valued averaging, noncentral real-action stability, measurable normal forms, continuous selections and topological characteristic-square conclusions are not certified by this companion.
