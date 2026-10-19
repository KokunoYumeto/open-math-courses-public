# Periodic corner spectra from factor contact

*Original exposition and diagram by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New text and diagram: CC0-1.0. Human sources retain their own terms.*

Let \(M\ne0\) be a concrete von Neumann algebra, and let \(\alpha:\mathbb R\to\operatorname{Aut}(M)\) be a point-ultraweakly continuous group of normal automorphisms with a period \(P>0\). Set \(\omega=2\pi/P\) and \(N=M^\alpha\). Inner products follow the second-variable-linear convention of this course. The concrete predual and its dual are proved in [H03](../src/infinite-tensor-products.md#10-hilbert-and-operator-foundations-for-the-finite-leg-vector-slice). Positive roots, supports, arbitrary projection joins and the expression of an operator as a linear combination of unitaries are proved in [Sections 8.1–8.5 of the periodic CAR lesson](../src/constant-car-states-and-the-periodic-core.md#8-projection-comparison-and-the-finite-factor-alternative). Scalar Lebesgue integration and the elementary exponential integral are used below.

The classical definitions are Connes's action spectrum and fixed-corner intersection. We prove their periodic specialization directly. The proof does not require a spectrum theorem for arbitrary locally compact groups, a spectral-synthesis theorem, or a general dual-center kernel theorem.

<a id="pp00"></a>
## PP00. The exact theorem

Define the integer eigenspaces by
\[
 M_k=\{x\in M:\alpha_t(x)=e^{ik\omega t}x\text{ for every }t\in\mathbb R\}.
 \tag{PP1}
\]
If \(N\) is a factor, every nonzero projection \(e\in N\) has
\[
 \operatorname{Sp}(\alpha^e)=\operatorname{Sp}(\alpha)
       =\{k\omega:M_k\ne0\},
 \qquad \Gamma(\alpha)=\operatorname{Sp}(\alpha).
 \tag{PP2}
\]
Here \(\alpha^e\) is the restriction to \(eMe\), and \(\Gamma\) is the intersection over **all** nonzero fixed projections, as defined in PP01. No finiteness, trace, separability or factoriality of the ambient \(M\) is needed for (PP2); the fixed algebra is the factor hypothesis. If every integer eigenspace is nonzero, then \(\Gamma(\alpha)=\omega\mathbb Z\). PP02–PP04 prove these assertions.

<a id="pp01"></a>
## PP01. The normal-coefficient integral and its hull

For \(f\in L^1(\mathbb R)\), put
\[
 \widehat f(s)=\int_{\mathbb R} f(t)e^{ist}\,dt,
 \qquad T_f(x)=\int_{\mathbb R} f(t)\alpha_t(x)\,dt.
 \tag{PP3}
\]
The second integral is defined against every \(\psi\in M_*\). The scalar coefficient is continuous, bounded by \(\|\psi\|\|x\|\), and therefore integrable after multiplication by \(f\). Its integral defines a bounded linear functional of \(\psi\), of norm at most \(\|f\|_1\|x\|\). The identity \((M_*)^*=M\) gives a unique operator \(T_f(x)\) in \(M\), with that norm bound. This also proves linearity in both \(f\) and \(x\); no operator-norm continuity of \(t\mapsto\alpha_t(x)\) is assumed.

Use the positive-frequency convention in (PP3) to define
\[
 \operatorname{Sp}(\alpha)
    =\bigcap_{T_f=0}\{s\in\mathbb R:\widehat f(s)=0\},
 \qquad
 \Gamma(\alpha)=
    \bigcap_{0\ne e\in\operatorname{Proj}(N)}
                    \operatorname{Sp}(\alpha^e).
 \tag{PP4}
\]
The first intersection runs over all complex \(L^1\) kernels for which the entire operator map \(T_f\) is zero. Each fixed corner is nonzero and has the same period; its coefficient integral is the ambient integral restricted to that corner. Indeed \(\alpha_t(exe)=e\alpha_t(x)e\), and normal compression commutes with the defining scalar-coefficient integral. Thus the same definition applies to every corner.

For an eigenoperator \(x\in M_k\), substitution gives exactly
\[
 T_f(x)=\widehat f(k\omega)x.
 \tag{PP5}
\]
Consequently, a nonzero eigenoperator makes its frequency belong to the hull in (PP4).

<a id="pp02"></a>
## PP02. A single interval filter excludes the nonperiodic frequencies

Set
\[
 g(t)=P^{-1}1_{[0,P]}(t),\qquad
 f(t)=g(t)-g(t-P).
 \tag{PP6}
\]
Endpoints have Lebesgue measure zero. The change of variable \(t=u+P\) and periodicity give \(T_{g(\cdot-P)}(x)=T_g(x)\) for every \(x\); hence \(T_f=0\). The scalar exponential integral gives
\[
 \widehat f(s)=(1-e^{iPs})A_P(s),\qquad
 A_P(s)=
 \begin{cases}(e^{iPs}-1)/(iPs),&s\ne0,\\1,&s=0.
 \end{cases}
 \tag{PP7}
\]
If \(s\notin\omega\mathbb Z\), then \(s\ne0\), \(e^{iPs}\ne1\), and both factors in (PP7) are nonzero. This annihilating kernel excludes every such \(s\) from the action spectrum.

For an integer \(k\), use
\[
 h_k(t)=P^{-1}1_{[0,P]}(t)e^{-ik\omega t},\qquad Q_k=T_{h_k}.
 \tag{PP8}
\]
Commuting a normal automorphism with the coefficient integral and changing variables in one period prove
\[
 \alpha_u(Q_kx)=e^{ik\omega u}Q_kx.
 \tag{PP9}
\]
To justify the interval change, the scalar integrand \(e^{-ik\omega t}\psi(\alpha_t(x))\) is continuous and periodic. Integrals over two intervals of length \(P\) agree: subtract integer periods, split at the remaining endpoint, and translate the split part by \(P\). Therefore \(Q_kM\subseteq M_k\). Conversely \(Q_kx=x\) for \(x\in M_k\), by the integral of the constant scalar one. If \(M_k=0\), then \(T_{h_k}=Q_k=0\), while \(\widehat h_k(k\omega)=1\); this excludes that lattice point. If \(M_k\ne0\), (PP5) includes it. We have proved
\[
 \operatorname{Sp}(\alpha)=\{k\omega:M_k\ne0\}
 \tag{PP10}
\]
without a Fourier completeness or spectral-localization assumption. The same proof, with identity \(e\), applies to every nonzero fixed corner.

<a id="pp03"></a>
## PP03. Contact in the fixed factor

The fixed algebra \(N\) is a von Neumann algebra: it is the intersection of the ultraweakly closed kernels of \(x\mapsto\alpha_t(x)-x\), and it is closed under products and adjoints. The support and join constructions cited above therefore apply inside \(N\).

For a projection \(p\in N\), form
\[
 z_N(p)=\bigvee_{u\in\mathcal U(N)}upu^*.
 \tag{PP11}
\]
Conjugation by any unitary permutes the family, so it fixes the join. Every element of \(N\) is a linear combination of its unitaries: for a self-adjoint contraction \(a\), the positive root \(c=(1-a^2)^{1/2}\) commutes with \(a\), \(a+ic\) is unitary, and \(a=((a+ic)+(a-ic))/2\). Scale and split real and imaginary parts for the general element. Thus the join in (PP11) is central. It majorizes \(p\), and every central projection majorizing \(p\) majorizes all its conjugates and their join. In a factor it is one whenever \(p\ne0\).

If two nonzero projections \(p,q\in N\) had \(pNq=0\), then for all unitaries \(u,v\in N\),
\[
 (upu^*)(vqv^*)=u\,p(u^*v)q\,v^*=0.
 \tag{PP12}
\]
The ranges of every conjugate of \(p\) and every conjugate of \(q\) would be orthogonal. Their closed spans, which are the ranges of the two joins (PP11), would also be orthogonal. Both joins are one, a contradiction. Hence
\[
 p,q\in\operatorname{Proj}(N)\setminus\{0\}
       \quad\Longrightarrow\quad pNq\ne0.
 \tag{PP13}
\]
This proof uses no projection-dimension or trace comparison theorem.

<a id="pp04"></a>
## PP04. An actual eigenoperator in every fixed corner

Take \(0\ne x\in M_k\) and \(0\ne e\in\operatorname{Proj}(N)\). Its left and right supports belong to \(N\). For example, \(\alpha_t(x)=e^{ik\omega t}x\) has the same left support as \(x\), while an automorphism carries its least left-support projection to that of its image. This proves fixedness; the right support is identical in this respect.

Put \(l=s_l(x)\ne0\). By (PP13), choose \(a\in N\) with \(eal\ne0\). Then
\[
 y=eax\ne0,
 \qquad y\in M_k.
 \tag{PP14}
\]
If \(eax=0\), the bounded operator \(ea\) vanishes on \(\operatorname{ran}x\), hence on its closure \(lH\), contradicting \(eal\ne0\). This proves the nonzero assertion, rather than presuming that compression preserves a nonzero operator.

Now \(r=s_r(y)\ne0\) is in \(N\). Again (PP13) supplies \(b\in N\) with \(rbe\ne0\). Since \(\ker y=(1-r)H\),
\[
 z=ybe=eaxbe\ne0,
 \qquad z\in eMe\cap M_k.
 \tag{PP15}
\]
Indeed \(ybe=0\) would put the range of \(be\) in \(\ker y\), and would force \(rbe=0\). Fixedness of \(e,a,b\) gives the same eigenphase for \(z\). Thus every active integer degree survives in every nonzero fixed corner. An eigenoperator of the corner is already an eigenoperator of the ambient algebra, so there are no additional degrees. Formula (PP10) in the ambient algebra and in each corner now proves all of (PP2).

### The two nonzero contacts

The diagram shows the exact support witnesses in (PP14)–(PP15). The boxes denote algebra elements and support tests; their widths do not indicate ranks, dimensions or trace. All arrows keep the frequency \(k\omega\). No inverse of \(x\) or \(y\) is asserted.

<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="420" viewBox="0 0 1100 420" role="img" aria-labelledby="pp-contact-title pp-contact-desc">
<title id="pp-contact-title">Every active degree survives every fixed corner</title>
<desc id="pp-contact-desc">For nonzero e in the fixed factor N and nonzero x of degree k, contact e N l(x) supplies a with e a l(x) nonzero. Density of the range of x gives y=e a x nonzero. Contact r(y) N e supplies b with r(y) b e nonzero. The kernel identity for y gives z=e a x b e nonzero in e M e with the same degree k.</desc>
<defs><marker id="pp-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#38536f"/></marker></defs>
<rect width="1100" height="420" rx="18" fill="#f7f9fc"/>
<g font-family="Arial, sans-serif" fill="#152b44">
<text x="30" y="40" font-size="25" font-weight="bold">PP04 · Fixed-factor contact preserves every integer degree</text>
<text x="30" y="79" font-size="21">0 ≠ e ∈ Proj(N),   0 ≠ x ∈ Mₖ,   N = Mᵅ is a factor</text>
<rect x="30" y="111" width="302" height="142" rx="12" fill="#fff5e7" stroke="#d9b984"/>
<text x="50" y="146" font-size="21" font-weight="bold">First contact: e N l(x) ≠ 0</text>
<text x="50" y="184" font-size="21">choose a ∈ N: e a l(x) ≠ 0</text>
<text x="50" y="221" font-size="21">ran(x) is dense in l(x)H</text>
<line x1="343" y1="181" x2="386" y2="181" stroke="#38536f" stroke-width="3" marker-end="url(#pp-arrow)"/>
<rect x="400" y="111" width="290" height="142" rx="12" fill="#eaf4fb" stroke="#99bdd8"/>
<text x="420" y="146" font-size="23" font-weight="bold">y = e a x ≠ 0</text>
<text x="420" y="184" font-size="21">y has degree k</text>
<text x="420" y="221" font-size="21">0 ≠ r(y) ∈ Proj(N)</text>
<line x1="702" y1="181" x2="744" y2="181" stroke="#38536f" stroke-width="3" marker-end="url(#pp-arrow)"/>
<rect x="759" y="111" width="311" height="142" rx="12" fill="#edf5ed" stroke="#a4c5a4"/>
<text x="779" y="146" font-size="21" font-weight="bold">Second contact: r(y) N e ≠ 0</text>
<text x="779" y="184" font-size="21">choose b ∈ N: r(y) b e ≠ 0</text>
<text x="779" y="221" font-size="21">ker(y) = (1 − r(y))H</text>
<path d="M 915 266 L 915 291 L 549 291 L 549 313" fill="none" stroke="#38536f" stroke-width="3" marker-end="url(#pp-arrow)"/>
<rect x="30" y="324" width="1040" height="65" rx="12" fill="white" stroke="#bbcbdc"/>
<text x="52" y="365" font-size="25" font-weight="bold">z = e a x b e ≠ 0,   z ∈ eMe,   αₜ(z) = exp(i k ω t) z</text>
</g></svg>

The classical fixed-corner conclusion is Connes, [Proposition 2.2.2(c), with its full proof on printed pp.174–175](https://numdam.org/article/ASENS_1973_4_6_2_133_0.pdf#page=43). PP02 supplies the particular interval-filter spectrum calculation, and PP03–PP04 give each nonzero support witness explicitly.

<a id="pp05"></a>
## PP05. The CAR lattice and the exact modular intersection input

For the faithful constant CAR product with \(0<p<1\), \(p\ne1/2\), put
\[
 \lambda=\frac{\min(p,1-p)}{\max(p,1-p)},\qquad
 \omega=|\log\lambda|,\qquad P=2\pi/\omega.
 \tag{PP16}
\]
The periodic lesson constructs a nonzero eigenoperator of every integer degree in [equation (6)](../src/constant-car-states-and-the-periodic-core.md#1-the-constant-faithful-product-state), proves that the fixed algebra is a factor in [Theorem 3.2 and Section 10](../src/constant-car-states-and-the-periodic-core.md#10-complete-local-expectations-and-the-constant-state-centralizer), and gives the entire core center action in [Theorems 4.2–5.1 and equations (24)–(27)](../src/constant-car-states-and-the-periodic-core.md#4-crossing-by-the-period-circle). Therefore (PP2) gives, at exactly that CAR scope,
\[
 \Gamma(\sigma^\phi)=\omega\mathbb Z
     =\ker(\theta|_{Z(C)}).
 \tag{PP17}
\]
The last equality also follows directly from the central generator \(z\mapsto e^{-iaP}z\). This is a comparison for the explicitly constructed periodic core, not a general dual-center theorem.

For the subtype inference use the separate modular intersection identity
\[
 S(M)\cap(0,\infty)=\exp\Gamma(\sigma^\phi),\qquad
 S(M)=\bigcap_{\psi\ \mathrm{faithful\ normal\ semifinite}}
                                      \operatorname{Sp}(\Delta_\psi).
 \tag{PP18}
\]
The complete local proof is [MG-0–4, in particular MG14](../../OA-FLOW/OA-FLOW-MG.html#oa-flow.mg.4), for a type III factor with separable predual. It includes the all-weight comparison and corner transport; (PP17) alone does not prove (PP18). The comparison must retain all faithful normal semifinite weights, rather than replacing their intersection by one product-state spectrum.

The countable faithful CAR product has separable predual at this application. Its Hilbert space is the completion of the increasing finite tensor spaces, each finite-dimensional. Rational complex finite-coordinate combinations give a countable dense set. Finite sums of vector functionals from those vectors are norm dense in the concrete predual: truncate the summable coefficient series of H03 and approximate each of its finitely many vectors, using \(\|\psi_{u,v}-\psi_{u',v'}\|\le\|u-u'\|\|v\|+\|u'\|\|v-v'\|\). The resulting rational finite sums form a countable norm-dense set. Thus this countability hypothesis of MG14 follows from the actual countable product, rather than from a factor name alone.

Under this input, (PP17) gives \(S(M)\cap(0,\infty)=\lambda^{\mathbb Z}\). Each modular operator is positive self-adjoint, so the intersection is a closed subset of \([0,\infty)\). Because \(\lambda^n\to0\), its closedness also puts zero in the intersection. Hence
\[
 S(M)=\{0\}\cup\lambda^{\mathbb Z},\qquad
 M\text{ has type }\mathrm{III}_\lambda.
 \tag{PP19}
\]
The subtype terminology is defined by this spectral intersection in Connes's [introduction to Part IV, printed p.213](https://numdam.org/article/ASENS_1973_4_6_2_133_0.pdf#page=82). Thus the exact center period \(L=\omega\) gives \(\lambda=e^{-L}\) for this factor. No existence, uniqueness or classification of other factors is concluded.

<a id="pp06"></a>
## PP06. A finite matrix diagnosis

The fixed-factor hypothesis cannot be dropped. On \(M_2(\mathbb C)\), let \(\alpha_t=\operatorname{Ad}\operatorname{diag}(e^{i\omega t},1)\), with \(\omega>0\). Its four matrix units have frequencies \(0,0,\omega,-\omega\), so (PP10) gives
\[
 \operatorname{Sp}(\alpha)=\{0,\omega,-\omega\}.
 \tag{PP20}
\]
The fixed algebra is the diagonal algebra. Its nonzero fixed projection \(e_{11}\) has scalar corner \(\mathbb C e_{11}\), on which the action is the identity, with spectrum \(\{0\}\). Every nonzero fixed corner contains its fixed identity and therefore contains frequency zero. The intersection is exactly \(\Gamma(\alpha)=\{0\}\). The projection supports of the off-diagonal eigenoperators are fixed, but diagonal-factor contact (PP13) fails: \(e_{11}Ne_{22}=0\).

**Exercise.** In PP04, why can one not start with \(exe\ne0\)? **Solution.** Nonzero compression is not guaranteed: the matrix example has \(x=e_{12}\ne0\), \(e=e_{11}\), and \(exe=0\). The two fixed-factor contacts construct \(a,b\) with the actual nonzero element \(eaxbe\). The density and kernel arguments in (PP14)–(PP15) prove both nonzero steps. In the matrix example the fixed algebra is not a factor, so the required second contact is unavailable. This is precisely the missing hypothesis, not a failure of the corner-spectrum definition.

The freely accessible primary definitions and antecedent are Connes, [*Une classification des facteurs de type III* (1973), Definition 2.1.2, Definition 2.2.1 and Proposition 2.2.2](https://numdam.org/article/ASENS_1973_4_6_2_133_0.pdf), printed pp.170 and 174–175. The modular intersection theorem on printed pp.190–192 is a distinct prerequisite. Original source text and images are not redistributed here.
