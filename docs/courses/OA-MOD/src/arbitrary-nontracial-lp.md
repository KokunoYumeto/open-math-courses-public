# Nontracial \(L^p\) spaces for arbitrary von Neumann algebras

*Independently written by OpenAI Codex (AI), October 2026, at requested Ultra effort. New prose: CC0-1.0.*

For an arbitrary von Neumann algebra \(N\), including one with no faithful normal state, we construct two-sided Banach \(N\)-modules \(L^p(N)\), \(1\leq p\leq\infty\). Their positive \(L^1\) elements are precisely normal positive functionals. A change of the auxiliary faithful semifinite weight gives a coherent isometry. This supplies the general-algebra construction left outside the factor and separable-predual scope of homogeneous core operators.

The proof uses the general regular-core construction in OE02–03, the traced density theorem PT08, cocycle reconstruction CX10, and lifting through an already existing operator-valued weight OM01. The last input remains conditional on the three explicitly stated contracts in OR03–04: the scalar mixed-graph criterion, finite mixed-ideal transfer, and analytic-generator comparison. OE02–03 also retain their stated harmonic-analysis and positive-integration inputs. The arguments below prove the construction from these named inputs. They do not prove those inputs or their prerequisites.

For comparison, Fumio Hiai's freely available *Concise lectures on selected topics of von Neumann algebras*, section 11.1, Lemmas 11.1–11.4 and Theorem 11.5, give the core-density approach. Complete PDF pages 101–106 were actually inspected. The missing theorem locator printed in the converse argument on page 104 is replaced here by the precise course provider CX10. This is independently written exposition; no human source text or source file is redistributed.

## The general core and its normalized trace

If \(N=0\), all spaces and maps below are zero. Otherwise choose a faithful normal semifinite weight \(\varphi_0\) by WH13. A state is not required. Write

\[
 \begin{aligned}
 P&=N\rtimes_{\sigma^{\varphi_0}}\mathbb R,\\
 \theta_s(x)&=x\quad(x\in N),&
 \theta_s(\lambda_t)&=e^{-ist}\lambda_t,\\
 E(a)&=\int_{\mathbb R}\theta_s(a)\,ds
       \quad(a\in P_+).
 \end{aligned}
 \tag{LP.1}
\]

The integral takes values in the full extended positive cone of \(N\).

Here is why the generality of this input matters. In the regular representation on \(L^2(\mathbb R,H_{\varphi_0})\), let

\[
 \begin{aligned}
 (\pi(x)\xi)(r)&=\sigma_{-r}^{\varphi_0}(x)\xi(r),\\
 (\lambda_t\xi)(r)&=\xi(r-t),&
 (D_s\xi)(r)&=e^{-isr}\xi(r).
 \end{aligned}
\]

There is no restriction on the Hilbert cardinality. The multiplication-field gauge \(V\xi(r)=\Delta_{\varphi_0}^{ir}\xi(r)\) turns the represented \(N\) into constant operators. An operator fixed by conjugation with every \(D_s\) is a multiplication field; commutation with the gauged translation action makes this field constant. Commutation with the conjugated constant commutant operators then puts that constant in \(N\). The equality at \(r=0\) uses continuity of each fixed conjugated commutant operator, not evaluation of a general measurable field. This is the fixed-algebra proof in OE02, and gives \(P^\theta=N\).

OE03 proves that \(E\) is normal, faithful and semifinite, using positive Tonelli, vector Plancherel and
\(E(\lambda(f)^*\lambda(f))=2\pi\|f\|_2^2\,1\), with finite-weight cutdowns. Put \(\Phi_0=\varphi_0\circ E\). The forward theorem for the already existing \(E\) gives \(\sigma_t^{\Phi_0}|_N=\sigma_t^{\varphi_0}\). Covariance of \(E\) and invariance of \(\varphi_0\) make \(\Phi_0\) invariant under \(\operatorname{Ad}\lambda_t\). Thus \(\lambda_t\) lies in its centralizer. Since \(N\) and these unitaries generate \(P\),

\[
 \sigma_t^{\Phi_0}=\operatorname{Ad}\lambda_t.
\]

Let \(d>0\) be the injective affiliated operator with \(d^{it}=\lambda_t\). The inverse centralizer perturbation in PT05 gives

\[
 \begin{aligned}
 \tau&=(\Phi_0)_{d^{-1}},\\
 (D\Phi_0:D\tau)_t&=d^{it}=\lambda_t,\\
 \sigma_t^\tau&=\mathrm{id},\\
 \theta_s(d)&=e^{-s}d,\\
 \tau\circ\theta_s&=e^{-s}\tau .
 \end{aligned}
 \tag{LP.2}
\]

In particular \(\tau\) is a faithful normal semifinite trace. The last normalization follows either from OE03 or directly from cocycle naturality: \(\Phi_0\circ\theta_s=\Phi_0\), and its cocycle relative to \(\tau\circ\theta_s\) is \(\theta_{-s}(\lambda_t)=e^{ist}\lambda_t\). This is exactly the cocycle relative to \(e^{-s}\tau\). Fixed-reference injectivity identifies the two weights, including infinite values.

The useful bounded normalizer

\[
 a_0=d^{-1}1_{(1,\infty)}(d),\qquad E(a_0)=1
 \tag{LP.3}
\]

comes from spectral calculus: for each \(\ell>0\), the orbit integral is
\(\int_{s<\log\ell}e^s\ell^{-1}\,ds=1\). The operator \(d\) itself need not be \(\tau\)-measurable. Its imaginary powers are nevertheless bounded unitaries. We will use precisely that distinction.

## Every grade-one positive density descends to a weight

PT08 says that every normal semifinite weight \(\Psi\) on \(P\) has a unique positive affiliated density \(h\), with its actual support, such that \(\Psi=\tau_h\). This assertion includes nonfaithful weights and nonmeasurable densities. All evaluations are normal positive form pairings; a formal product of unbounded operators is not their definition. Trace scaling gives

\[
 \tau_h\circ\theta_s=e^{-s}\tau_{\theta_{-s}(h)}.
 \tag{LP.4}
\]

For instance this follows first with bounded spectral regularizations from
\(\tau(\theta_s(b))=e^{-s}\tau(b)\), then on every positive element by normal form evaluation. Density uniqueness proves

\[
 \Psi\circ\theta_s=\Psi
 \quad\Longleftrightarrow\quad
 \theta_s(h)=e^{-s}h .
 \tag{LP.5}
\]

We now prove that such invariant weights are exactly the dual weights \(\varphi\circ E\). First suppose \(\Psi\) is faithful. Both \(\Psi\) and \(\Phi_0\) are invariant, so naturality PT02 fixes the normalized cocycle
\(u_t=(D\Psi:D\Phi_0)_t\) under \(\theta\). Therefore \(u_t\in N\). Its cocycle law on \(P\), restricted using \(\sigma^{\Phi_0}|_N=\sigma^{\varphi_0}\), is a \(\sigma^{\varphi_0}\)-cocycle on \(N\). CX10 supplies a unique faithful normal semifinite \(\varphi\) with
\((D\varphi:D\varphi_0)_t=u_t\). The lifting theorem OM01 gives

\[
 (D(\varphi\circ E):D\Phi_0)_t
       =(D\varphi:D\varphi_0)_t=u_t.
 \tag{LP.6}
\]

Fixed-reference injectivity on \(P\) gives \(\Psi=\varphi\circ E\). Conversely every such dual weight is invariant, because \(E\theta_s=E\). Injectivity on faithful weights follows from the same lifting identity and fixed-reference injectivity on \(N\).

Supports do not disappear in this argument. For a normal semifinite \(\varphi\) on \(N\), of support \(e\), its dual weight has support exactly \(e\). It vanishes on \(1-e\) by bimodularity. If \(r\in P\) is a projection on which it vanishes, faithfulness of \(\varphi\) on \(eNe\) gives
\(eE(r)e=E(ere)=0\). Faithfulness of \(E\) then gives \(ere=0\), hence \(re=0\) and \(r\leq1-e\). Thus its maximal zero projection is \(1-e\). To see semifiniteness when \(e<1\), choose a faithful normal semifinite weight on \((1-e)N(1-e)\), extend both corner weights, and add them. Their sum is faithful and semifinite. Its dual is semifinite; \(e\) lies in its centralizer, by the diagonal corner construction and modular restriction. Compression to \(e\) is therefore semifinite as well.

For an invariant nonfaithful \(\Psi\), its support \(e=s(\Psi)\) is fixed by \(\theta\), so belongs to \(N\). Add the dual of a faithful semifinite weight on \((1-e)N(1-e)\). The diagonal sum \(\widetilde\Psi\) is faithful semifinite and invariant. The faithful case gives \(\widetilde\Psi=\widetilde\varphi\circ E\). Its support projection \(e\) is in its centralizer; modular restriction puts \(e\) in the centralizer of \(\widetilde\varphi\). Compress and use bimodularity:

\[
 \Psi(a)=\widetilde\Psi(eae)
        =\widetilde\varphi(eE(a)e)
        =\varphi(E(a)).
\]

Here \(\varphi\) is the compression, extended by zero. Its support is \(e\). For injectivity, the support argument makes equal dual weights have equal supports; add the same complementary faithful weight and apply faithful injectivity. The zero weight is included. We have proved the support-preserving bijection

\[
 \begin{aligned}
 \varphi&\longmapsto h_\varphi,\\
 \varphi\circ E&=\tau_{h_\varphi},&
 \theta_s(h_\varphi)&=e^{-s}h_\varphi,&
 s(h_\varphi)&=s(\varphi).
 \end{aligned}
 \tag{LP.7}
\]

## Finite functionals, localizers and the canonical integral

Let \(h=h_\varphi\). Its bounded supported localizer
\(a_h=h^{-1}1_{(1,\infty)}(h)\) satisfies \(E(a_h)=s(h)\), by the scalar integral used in LP01. Positive form evaluation gives
\(\tau_h(a_h)=\tau(1_{(1,\infty)}(h))\). It follows that, with infinite values allowed,

\[
 \begin{gathered}
 \tau(1_{(\ell,\infty)}(h_\varphi))
       =\ell^{-1}\varphi(1),\\
 \ell>0,\\
 h_\varphi\text{ is }\tau\text{-measurable}\\
 \Longleftrightarrow\quad \varphi(1)<\infty.
 \end{gathered}
 \tag{LP.8}
\]

Indeed trace scaling and \(\theta_s(h)=e^{-s}h\) give the displayed tail for every threshold. Finite mass makes these tails tend to zero. Infinite mass makes every positive tail infinite, which excludes measurability. This also handles \(h=0\).

For every bounded positive normalizer \(a\) with \(E(a)=1\), bimodularity gives the inverse formula

\[
 \varphi(x)=
 \tau\!\left(a^{1/2}x^{1/2}h_\varphi x^{1/2}a^{1/2}\right)
       \quad(x\in N_+).
 \tag{LP.9}
\]

The right side denotes the normal trace pairing of the corresponding positive closed form; it equals \(\tau_{h_\varphi}(x^{1/2}a x^{1/2})\). It includes infinity. LP03 takes \(a=a_0\) when needed.

For \(\omega\in N_*^+\), set \(D\omega=h_\omega\). The positive measurable sum \(h_\omega+h_\eta\) has grade one. LP09 and linearity of positive trace pairings identify its inverse functional with \(\omega+\eta\). Thus \(D\) is additive and positively homogeneous. Every predual functional is a finite complex linear combination of positive normal functionals: CP04–06 represent it by a coefficient series with \(\sum_j\|\xi_j\|\|\eta_j\|<\infty\). Rescale each nonzero pair to have equal vector norms. Vector polarization expresses each coefficient as four positive vector functionals, and each of the four resulting series has summable squared vector norms, hence defines a bounded normal positive functional. Extend \(D\) by these combinations. Independence follows by taking the real and imaginary parts of a zero relation, moving positive summands to opposite sides, and using positive additivity. This proves complex linearity without presuming a Jordan theorem.

The module orientation deserves a check. For \(x\in N\), the dual of \(y\mapsto\omega(x^*yx)\) is \(b\mapsto(\omega\circ E)(x^*bx)\). Relative to the trace its density is \(x h_\omega x^*\), by positive form pairing and traciality. Uniqueness therefore gives this congruence identity. Polarization gives, for \(b,c\in N\),

\[
 D\!\left[y\mapsto\omega(b^*yc)\right]=c h_\omega b^*.
 \tag{LP.10}
\]

The polarized functionals are finite; all measurable sums and products use their closed extensions.

Conversely, if \(T\) is measurable and \(\theta_s(T)=e^{-s}T\), uniqueness of polar decomposition makes its polar partial isometry \(u\) fixed by \(\theta\), so \(u\in N\). Its modulus has grade one and, by LP07–08, is \(h_\omega\) for a unique \(\omega\in N_*^+\). Formula LP10 makes \(T=u h_\omega\) the density of \(y\mapsto\omega(yu)\). This proves that \(D\) is onto the entire grade-one space. Positive injectivity follows from LP07. A general element of the kernel has real and imaginary parts represented by differences of positive densities; equality of those densities and LP07 make both functional differences zero. Thus \(D\) is injective.

Define \(\int T=D^{-1}(T)(1)\). Then

\[
 \begin{aligned}
 \int T&=\tau(a^{1/2}Ta^{1/2}),&
 \int u h_\omega&=\omega(u),\\
 F_T(x)&=\int xT,&
 \|F_T\|&=\int |T|=\omega(1).
 \end{aligned}
 \tag{LP.11}
\]

To justify the first expression, decompose \(D^{-1}(T)\) into four finite positive functionals. Each localized density has finite trace by LP09, so their linear combination is trace integrable. This also proves independence of \(a\). The last equality is the normal-functional polar decomposition NF02, with \(u^*u=s(\omega)\). Consequently the grade-one space is isometric to the Banach predual \(N_*\). The ordinary core trace of \(T\) is not the integral in LP11.

## Change of reference preserves the actual trace and densities

Let \(\varphi,\psi\) be faithful normal semifinite weights on \(N\), and let \(P_\varphi,P_\psi\) be their regular cores in one faithful standard representation. Put \(u_t=(D\psi:D\varphi)_t\). The multiplication unitary

\[
 (W\xi)(r)=u_{-r}^*\xi(r)
\]

implements the normal isomorphism \(I_{\psi,\varphi}:P_\psi\to P_\varphi\) with

\[
 \begin{aligned}
 I_{\psi,\varphi}(x)&=x,\\
 I_{\psi,\varphi}(\lambda_t^\psi)
       &=u_t\lambda_t^\varphi,\\
 I_{\psi,\varphi}(\theta_s^\psi A)
       &=\theta_s^\varphi(I_{\psi,\varphi} A).
 \end{aligned}
 \tag{LP.12}
\]

Indeed \(\sigma_{-r}^\psi(x)=u_{-r}\sigma_{-r}^\varphi(x)u_{-r}^*\), proving the first identity. For translations,
\(u_{-r}^*u_{t-r}=\sigma_{-r}^\varphi(u_t)\) by the cocycle law, proving the second. The field \(W\) commutes with every scalar phase \(D_s\), proving the last. The inverse field gives onto, not only a homomorphism on algebraic generators. Positive orbit integrals intertwine as well.

Write \(\Psi_\psi=\psi\circ E_\psi\) and \(\Phi_\varphi=\varphi\circ E_\varphi\). On \(P_\varphi\), OM01 and the ordered chain rule give

\[
 \begin{aligned}
 (D(\psi\circ E_\varphi):D\tau_\varphi)_t
  &=(D(\psi\circ E_\varphi):D\Phi_\varphi)_t
       (D\Phi_\varphi:D\tau_\varphi)_t\\
  &=u_t\lambda_t^\varphi.
 \end{aligned}
 \tag{LP.13}
\]

Let \(\tau'=\tau_\psi\circ I_{\psi,\varphi}^{-1}\). Transport of the defining numerator cocycle gives \((D(\psi\circ E_\varphi):D\tau')_t=I_{\psi,\varphi}(\lambda_t^\psi)=u_t\lambda_t^\varphi\). Reversing this identity and LP13 gives equal cocycles for \(\tau'\) and \(\tau_\varphi\) relative to the same reference \(\psi\circ E_\varphi\). Fixed-reference injectivity proves

\[
 \tau_\psi=\tau_\varphi\circ I_{\psi,\varphi},\qquad
 I_{\psi,\varphi}(h_\omega^\psi)=h_\omega^\varphi .
 \tag{LP.14}
\]

The second identity follows from PT08 uniqueness and orbit-weight transport. Trace preservation extends \(I\) to affiliated operators and to the measure algebra, by transporting spectral projections and bounded-domain cuts. Thus it preserves every homogeneous space and its spectral size.

For three references, the cocycle chain rule is
\((D\chi:D\varphi)_t=(D\chi:D\psi)_t(D\psi:D\varphi)_t\).
Apply LP12 to the generators: the two successive core maps equal \(I_{\chi,\varphi}\). They therefore agree on the whole core and on measurable limits. The resulting \(L^p\) identifications are coherent, with identity for an unchanged reference.

## Spectral size and sharp complementary multiplication

Let \(\mathcal H_a=\{T:\ T\text{ is }\tau\text{-measurable},\
\theta_s(T)=e^{-as}T\}\), for real \(a>0\). The measure algebra makes it a complex vector space. If \(T=u|T|\), then \(u\in N\) and \(|T|^{1/a}\) is a measurable positive grade-one density. Define

\[
 \begin{aligned}
 g_a(T)&=\left(\int |T|^{1/a}\right)^a,\\
 d_T(\ell)&=g_a(T)^{1/a}\ell^{-1/a},\\
 \mu_t(T)&=g_a(T)t^{-a}\quad(t>0).
 \end{aligned}
 \tag{LP.15}
\]

Here \(\mu_t(T)=\inf_{\tau(1-e)\leq t}\|Te\|\), with bounded-domain projections \(e\). LP08 gives \(d_T\); the spectral-cut characterization gives \(\mu_t\). Projection comparison, using the polar equivalence of discarded supports, proves that no bounded-domain cut can discard less trace than the corresponding high spectral projection. In each fixed positive grade, convergence in measure is therefore exactly convergence of the gauge of the difference.

For arbitrary measurable \(A,B\), projection cuts give

\[
 \begin{aligned}
 \mu_{s+t}(A+B)&\leq\mu_s(A)+\mu_t(B),\\
 \mu_{s+t}(AB)&\leq\mu_s(A)\mu_t(B),\\
 \mu_t(CAD)&\leq\|C\|\,\mu_t(A)\,\|D\|
                    \quad(C,D\in P).
 \end{aligned}
 \tag{LP.16}
\]

For the sum, intersect cuts. For the product, let \(e,f\) cut \(A,B\), and let \(r\) be the right support of \((1-e)B\). Its polar range lies in \(1-e\), so \(\tau(r)\leq\tau(1-e)\). On \(q=f\wedge(1-r)\), \(Bq=eBq\), giving the product norm bound and a discarded trace at most \(s+t\). Arbitrarily small slack proves the infimum assertion for the closed product. For right bounded multiplication use the same support argument; left bounded multiplication is immediate. None of these cuts is asserted to remain homogeneous.

For \(0<a<1\), LP15–16 first give the rough bound

\[
 \|AB\|_1\leq B(a)g_a(A)g_{1-a}(B),\qquad
 B(a)=a^{-a}(1-a)^{-(1-a)}\leq2 .
 \tag{LP.17}
\]

We remove the constant without an endpoint-continuity assumption. Take positive grade-one densities \(h,k\), initially of integral one. Supported powers define
\(F(z)=h^z k^{1-z}\), \(0<\Re z<1\). It has grade one. For a positive measurable \(c\), the difference quotients of \(c^z\) converge in measure to \(c^z\log c\) on \(\Re z>0\), taking the latter to be zero on the kernel. On \(0\leq\ell\leq R\), the scalar difference quotients converge uniformly on a small closed disk of positive real exponents: \(\ell^\epsilon|\log\ell|^2\) is bounded near zero. The omitted high spectral projection has arbitrarily small trace. This proves differentiability in measure. The continuous measure-algebra product gives

\[
 F'(z)=h^z\log h\,k^{1-z}-h^z k^{1-z}\log k .
\]

Both terms are measurable spectral products; the bare logarithms are not assumed measurable. The difference quotients have grade one, and dual-action continuity in measure preserves this grade in the limit. LP11 and LP15 turn the convergence into predual norm convergence. Thus \(F\) is norm holomorphic.

LP17 bounds \(F(u+it)\) by \(B(u)\); the supported imaginary powers are contractions and cancel their imaginary grades in the product. On the closed inner strip \(\delta\leq\Re z\leq1-\delta\), both boundary norms are at most \(B(\delta)\), and the function is bounded and norm continuous. The three-lines argument CI02 gives the same bound at every interior point. Let \(\delta\downarrow0\), so \(B(\delta)\to1\). Rescaling the positive inputs gives

\[
 \|h^a k^{1-a}\|_1
       \leq(\int h)^a(\int k)^{1-a}.
 \tag{LP.18}
\]

Zero inputs are handled directly. Now write \(A=u h^a\) by left polar decomposition and \(B=k^{1-a}v\) by right polar decomposition. Both partial isometries lie in \(N\). Formula LP16 for bounded multiplication, at grade one, gives the sharp bound

\[
 \|AB\|_1\leq g_a(A)g_{1-a}(B).
 \tag{LP.19}
\]

## The two-sided Banach modules

For \(1\leq p<\infty\) put

\[
 \begin{gathered}
 L^p(N)=\mathcal H_{1/p},\\
 \|T\|_p=\left(\int |T|^p\right)^{1/p},\\
 L^\infty(N)=N .
 \end{gathered}
 \tag{LP.20}
\]

For \(p=1\), LP11 already proves completeness and the norm. If \(1<p<\infty\), set \(a=1/p\). For nonzero \(S=u h^a\), the measurable operator \(T_0=h^{1-a}u^*\) has complementary grade and satisfies \(ST_0=u h u^*\). The supports \(u^*u=s(h)\) make the spectral tails of \(u h u^*\) and \(h\) equivalent. LP08 therefore gives
\(\int ST_0=\int h\) and \(g_{1-a}(T_0)=(\int h)^{1-a}\). Normalize \(T_0\), and use LP19 in the opposite direction, to obtain

\[
 g_a(S)=\sup_{g_{1-a}(T)\leq1}
               \left|\int ST\right|.
 \tag{LP.21}
\]

The grade-one integral is linear. Applying this supremum to \(S_1+S_2\) proves the triangle inequality; scaling and separation follow from LP15. Onto Banach duality is not presumed in this argument.

For completeness, a norm-Cauchy net \(S_i\) is measure Cauchy by LP15. The complete measure algebra, MT05–09, supplies a measurable limit \(S\). Trace scaling makes \(\theta_s\) continuous in measure: a discarded trace is multiplied by \(e^{-s}\), while the bounded cut norm is unchanged by the automorphism. Thus \(S\) retains grade \(a\). Fix \(i\), and apply the sum estimate to
\(S_i-S=(S_i-S_j)+(S_j-S)\). For \(s,t>0\), let \(j\) tend to the measure limit to get

\[
 g_a(S_i-S)(s+t)^{-a}
       \leq s^{-a}\liminf_j g_a(S_i-S_j).
\]

Let \(t\downarrow0\). The Cauchy condition gives \(g_a(S_i-S)\to0\). This proves completeness of the actual homogeneous space; no replacement completion or countable exhaustion of \(N\) was introduced.

For \(x,y\in N\), closed measurable multiplication preserves the grade, and LP16 gives

\[
 \|xTy\|_p\leq\|x\|\,\|T\|_p\,\|y\|.
 \tag{LP.22}
\]

Associativity, distributivity and the adjoint in the measure algebra make these genuine two-sided Banach \(N\)-modules. The unit acts as the identity; \(\|T^*\|_p=\|T\|_p\) follows from polar equivalence of spectral projections. At \(p=\infty\) these are the usual operator norm and multiplication on \(N\). LP14 gives isometries of these modules for every change of reference.

The measurable grade-zero space really is \(N\). If a grade-zero \(T\) has a finite-trace high spectral projection \(q\), then \(\theta_s(q)=q\), whereas trace scaling gives \(\tau(q)=e^{-s}\tau(q)\). Hence \(q=0\). Measurability supplies such a high cut, so \(T\) is bounded and fixed. This proves the endpoint assertion rather than postulating it.

## Imaginary grades without a faithful state

The faithful semifinite reference density \(d=h_{\varphi_0}\) has full support. For \(b\in\mathbb R\), \(d^{ib}\) is a bounded unitary in \(P\), even when \(d\) is not measurable. If
\(\theta_s(T)=e^{-(a+ib)s}T\), then

\[
 \begin{aligned}
 T&\longmapsto T d^{-ib}\in\mathcal H_a,\\
 |T d^{-ib}|&=d^{ib}|T|d^{-ib}.
 \end{aligned}
 \tag{LP.23}
\]

Inner trace invariance preserves every spectral-tail trace. Right multiplication by \(d^{ib}\) is the inverse, so this is an isometry for the gauge LP15. In particular imaginary grade has the operator-norm space \(N\) as its coordinate; positive real grades \(0<a\leq1\) have the Banach spaces just constructed.

Neither this coordinate map nor LP20 needs a faithful normal state. A state-dependent compatible interpolation couple is an additional construction with different hypotheses; the open identification recorded in HL-DEP-GRADED-STRIP is not used here. The Banach range of the grade parameter is \(0<a\leq1\). For \(a>1\), two orthogonal grade-one densities of integral one give \(g_a(h_1^a+h_2^a)=2^a>2\), so this formula is generally only a quasi-norm. This does not contradict LP20, which uses \(a=1/p\) for \(p\geq1\).

## Two solved models that test the generality

**Uncountably many atoms.** Let \(I\) be uncountable and \(N=\ell^\infty(I)\). The counting trace \(\nu(x)=\sum_{i\in I}x_i\) on positive elements means the supremum of finite subsums. It is faithful, normal and semifinite: finite-coordinate truncations form an increasing net with bounded finite trace. There is no faithful normal state. A normal positive functional has coefficients \(w_i\geq0\) of finite sum; for each integer \(n\), only finitely many exceed \(1/n\). Its nonzero support is therefore countable, and cannot be all of \(I\).

The modular action of \(\nu\) is trivial. The regular core and its trace have the concrete model

\[
 \begin{aligned}
 P&=\ell^\infty(I)\,\bar\otimes\,L^\infty(\mathbb R),\\
 \theta_s(f)_i(r)&=f_i(r+s),&
 \tau(f)&=\sum_{i\in I}\int_{\mathbb R}f_i(r)e^r\,dr,\\
 d_i(r)&=e^{-r}.
 \end{aligned}
 \tag{LP.24}
\]

The normalization is checked by LP03: \(a_0(r)=e^r1_{r<0}\) has orbit integral one, and \(\tau_{d}(x^{1/2}a_0x^{1/2})=\sum_i x_i\). The trace scales by \(e^{-s}\).

For \(p<\infty\), every grade \(1/p\) measurable element is, coordinate by coordinate,

\[
 \begin{gathered}
 T_i(r)=a_i e^{-r/p},\\
 \begin{aligned}
 \tau(1_{(\ell,\infty)}(|T|))
       &=\\
 &\ell^{-p}\sum_i |a_i|^p,
 \end{aligned}\\
 \|T\|_p=\left(\sum_i|a_i|^p\right)^{1/p}.
 \end{gathered}
 \tag{LP.25}
\]

To prove the classification, \(e^{r/p}T_i(r)\) is translation invariant as a measurable function on the single scalar coordinate, hence constant almost everywhere. This can be seen by bounded truncation and convolution with an approximate identity: each bounded translation-invariant truncation has constant convolutions and is constant almost everywhere. There is no need for one exceptional null set shared by uncountably many coordinates. Spectral integration gives the displayed tail, finite exactly when \((a_i)\in\ell^p(I)\); infinite sum gives an infinite tail at every threshold and excludes measurability. Finite \(p\)-summability also forces countable support. At \(p=\infty\), the bounded fixed functions are precisely \(\ell^\infty(I)\).

The operator \(d\) has infinite high-tail trace at every threshold, so is not \(\tau\)-measurable. Nevertheless \(d^{ib}_i(r)=e^{-ibr}\) is bounded and unitary. This verifies the exact hypothesis used by LP23 and disproves a faithful-state reduction in this example.

**Matrices and noncommuting reference weights.** Take \(N=M_n(\mathbb C)\) and first use the ordinary trace. Then
\(P=M_n\bar\otimes L^\infty(\mathbb R)\), with \(\tau=\operatorname{Tr}\otimes e^rdr\). For \(A\in M_n\), the element \(T_A(r)=A e^{-r/p}\) has

\[
 \tau(1_{(\ell,\infty)}(|T_A|))
       =\ell^{-p}\operatorname{Tr}|A|^p,\qquad
 \|T_A\|_p=(\operatorname{Tr}|A|^p)^{1/p}.
 \tag{LP.26}
\]

Diagonalize \(|A|\) and integrate each scalar tail, including zero eigenvalues. Thus LP20 recovers the Schatten norm, LP11 recovers \(F_{T_A}(x)=\operatorname{Tr}(xA)\), and LP22 gives both matrix module actions.

If instead \(\varphi(x)=\operatorname{Tr}(Bx)\) and \(\psi(x)=\operatorname{Tr}(Cx)\), with \(B,C>0\) not required to commute, then \(u_t=C^{it}B^{-it}\). In the common regular realization LP12 uses
\(W(r)=B^{-ir}C^{ir}\). The equality
\(u_{-r}^*u_{t-r}=\sigma_{-r}^{\varphi}(u_t)\) verifies the order of the generator map. For a third positive matrix \(D\),
\((D^{it}C^{-it})(C^{it}B^{-it})=D^{it}B^{-it}\), precisely the coherence order in LP04. No cancellation across nonadjacent factors, scalar phase choice or unbounded inverse is being assumed.

## References

- Fumio Hiai, *Concise lectures on selected topics of von Neumann algebras*, section 11.1, Lemmas 11.1–11.4 and Theorem 11.5; actual reading: complete PDF pages 101–106. [Author's freely available text](https://arxiv.org/abs/2004.02383).
- Alain Connes, “Une classification des facteurs de type III,” *Annales scientifiques de l'École Normale Supérieure* 6 (1973), 133–252. [Open article](https://numdam.org/articles/10.24033/asens.1247/). Historical cocycle antecedent; no new whole-source reading claim.

