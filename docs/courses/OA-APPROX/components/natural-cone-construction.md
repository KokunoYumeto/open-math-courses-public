# Constructing the natural cone from bounded multiplication

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original text: public domain (CC0).*

The methods used here are credited to H. Araki, U. Haagerup, M. Rieffel and A. Van Daele, and F. Hiai. Free primary accounts are [Araki's 1974 paper](https://msp.org/pjm/1974/50-2/pjm-v50-n2-p02-p.pdf), [Haagerup's 1975 paper](https://journals.msp.org/mscand/article/view/2067), [Rieffel–Van Daele's 1977 paper](https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf), and Hiai's [author arXiv version, 2004.02383v1](https://arxiv.org/pdf/2004.02383v1). Hiai's Lemma 3.3 and Theorem 3.2 give a useful cyclic version of the endpoint and middle-cone arguments. We work with the entire spaces of bounded multiplication vectors, so that the endpoint proof also applies to an infinite weight and an arbitrary Hilbert-space cardinality.

<a id="nc00"></a>
## NC00. The existing operator construction and its precise interface

Inner products are linear in the second variable. A first-variable-linear source pairing is translated by \(\langle u,v\rangle=(v\mid u)\). The conjugate-linear adjoint convention is
\[
 \langle Su,v\rangle=\langle S^*v,u\rangle.
 \tag{1}
\]
All operator equalities below include their actual domains. In particular, a displayed product of unbounded operators is not an equality of formal expressions alone.

The preceding proofs used here are the following. Their complete arguments are retained in the weight foundations, with the original component terms and inner-product conventions preserved.

* NC01 and NC01b construct the chosen diagonal weight and its original GNS graph on an arbitrary algebra. For an arbitrary preselected faithful normal semifinite weight, WR1–7 construct and recover its full GNS finite ideal; MW1–4 prove covariance and the opposite-weight formulas.
* BG1–6 prove both commutant inclusions, modular normalization, fullification and the original closed involution and adjoint, including their whole graph cores. BW1–5 prove the two whole multiplier ideals, their adjoint intersections, mixed multiplication and real modular covariance. Thus these inputs apply before a cone or a cyclic state vector has been constructed.
* SF0, SB0–6 and SF1–4 construct the bounded and unbounded spectral calculus, actual inverse and power domains, and pairing identities. FF4–5 construct the representing operator of a closed positive form and prove its commutant covariance. NC02 below gives the operator-domain criterion needed for the extension argument.
* CF1–10 supply scalar completeness, choice, compactness, Hahn–Banach, continuous C*-calculus and arbitrary-cardinality Hilbert projection and representation. CP01–06 construct the concrete predual and its norm-closed vector-series realization. SC00–10 construct scalar measure and integration. FF1–3 supply Gaussian Fourier integration and vectorwise integrals; the rectangle proof in SF4 supplies the elementary analytic uniqueness used below.
* NC00c proves the common analytic multiplication algebra from these real modular and scalar inputs. It includes the complex-power domains, product law and uniformly bounded multiplier approximation. NC01a treats merely bounded multiplication vectors by the full operator ideals.

Here is the combined concrete interface, which fixes the objects used in the rest of this proof. For a faithful n.s.f. weight \(\varphi\) on \(N\), its GNS representation identifies \(N\) faithfully and normally with \(M\subset B(H)\), and
\[
 \mathcal A=\Lambda(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*),
 \qquad S=\overline{\Lambda(a)\mapsto\Lambda(a^*)},
 \qquad F=S^*,
 \qquad \Delta=S^*S.
 \tag{2}
\]
The full left and right multiplication spaces are \(B_l,B_r\), with multipliers \(L_\xi\in M\), \(R_\eta\in M'\). Their exact defining mixed identity and covariance are
\[
 L_\xi\eta=R_\eta\xi,
 \quad L_{x\xi}=xL_\xi,
 \quad R_{y\eta}=yR_\eta
 \quad(\xi\in B_l,\eta\in B_r,x\in M,y\in M').
 \tag{3}
\]
The multipliers are injective assignments. Their ranges are left ideals, and
\[
 \mathcal A=B_l\cap D(S),\quad
 \mathcal D=B_r\cap D(F),\quad
 L(\mathcal A)=L(B_l)\cap L(B_l)^*,\quad
 R(\mathcal D)=R(B_r)\cap R(B_r)^*.
 \tag{4}
\]
In particular, a self-adjoint left multiplier puts its vector in \(\mathcal A\), with \(S\xi=\xi\); the corresponding assertion holds on the right. Products satisfy \(\xi\zeta=L_\xi\zeta\), \(\eta\theta=R_\theta\eta\), and the involutions on the two algebras are \(S,F\). Both algebras are dense, and are the graph cores of their involutions.

The modular output is
\[
 S=J\Delta^{1/2},\qquad F=J\Delta^{-1/2},\qquad
 J^2=1,\quad JMJ=M',\quad J\Delta^zJ=\Delta^{-\overline z}.
 \tag{5}
\]
Here \(\Delta\) is injective; its spectrum may accumulate at zero or infinity. The domain of a real power is
\[
 D(\Delta^\alpha)
 =\{u:\int_{(0,\infty)}t^{2\alpha}\,d\langle u,E_\Delta(t)u\rangle<\infty\}.
 \tag{6}
\]
The modular group \(U_t=\Delta^{it}\) implements automorphisms \(\sigma_t\) of \(M\). The common analytic algebra \(\mathcal A_0\) is invariant under every complex power, and for \(\xi,\zeta\in\mathcal A_0\),
\[
 \Delta^z(\xi\zeta)=(\Delta^z\xi)(\Delta^z\zeta),
 \quad J\mathcal A=\mathcal D,\quad
 R_{J\xi}=JL_\xi J.
 \tag{7}
\]
The algebra \(\mathcal A_0\) is dense in the stated involution graphs; the Gaussian approximants to \(\xi\in\mathcal A\) converge to \(\xi\) and \(S\xi\), with uniformly bounded left multipliers converging strongly. The additional approximation proved in NC01a is: every \(\eta\in B_r\) has a net \(\eta_i\in\mathcal D\) with
\[
 \eta_i\to\eta,\qquad R_{\eta_i}\to R_\eta\text{ strongly},
 \qquad\|R_{\eta_i}\|\le\|R_\eta\|.
 \tag{8}
\]
The analogous approximation holds on the left. The algebraic product reversal by \(J\), and \(FJ=JS\), have the graph domains supplied by (5)–(7).

No cone theorem is an input to this interface. In particular, endpoint duality and the middle cone's self-duality are proved below.

<a id="nc00a"></a>
## NC00a. The bounded-multiplication contracts from the original modular graphs

We record the proof of (3)–(4), to make their bounded tests and adjoint tests explicit. The real-square subspace in RS4 is
\[
 K=\overline{\operatorname{span}_{\mathbb R}\{a^\sharp a:a\in\mathcal A\}},
\]
and BG6 proves \(D(S)=K+iK\), \(S(k+i\ell)=k-i\ell\). Approximating \(k\) and \(\ell\) by real square spans proves that \(\mathcal A^2\) is a graph core for this **original** \(S\). The same conclusion holds for the right algebra and \(F\), by BG5–6, including its exact adjoint graph.

For a right-bounded vector \(\eta\), the operator determined by \(R_\eta a=L_a\eta\) commutes with all \(L_b\), by associativity on \(\mathcal A\), and hence belongs to \(M'\). The assignments are linear and injective, because \(L_a\eta=0\) for all \(a\) implies \(\eta=0\) by nondegeneracy. For \(y\in M'\), the defining tests immediately give \(R_{y\eta}=yR_\eta\). Thus their range \(\mathfrak n_r\) is a left ideal.

If \(\eta\in B_r\cap D(F)\), then for \(a,b\in\mathcal A\),
\[
\begin{aligned}
 \langle L_aF\eta,b\rangle
 &=\langle F\eta,a^\sharp b\rangle
  =\langle b^\sharp a,\eta\rangle\\
 &=\langle a,L_b\eta\rangle
  =\langle R_\eta^*a,b\rangle.
\end{aligned}
\]
Density shows that \(F\eta\in B_r\) and \(R_{F\eta}=R_\eta^*\). Conversely, if \(R_\eta^*=R_\theta\) for another \(\theta\in B_r\), the same chain of pairings, read backwards, proves
\[
 \langle S(a^\sharp b),\eta\rangle
 =\langle\theta,a^\sharp b\rangle.
\]
Extend this over the proved product graph core. It is exactly the adjoint-domain test (1), so \(\eta\in D(F)\) and \(F\eta=\theta\). Consequently the right algebra defined by the two bounded multiplier tests in BG2 and BG6 is precisely \(\mathcal D=B_r\cap D(F)\), and
\[
 R(\mathcal D)=\mathfrak n_r\cap\mathfrak n_r^*.
\]
The right algebra is full, dense and nondegenerate by BG1–6. Apply the proved argument to its opposite left Hilbert algebra. Its closed involution is \(F\), its adjoint is \(S\), and its generated algebra is \(M'\). This gives all the left assertions of (3)–(4), including covariance, injectivity, the ideal intersection, and equality with the full left completion. In particular, the definition of \(B_l\) is exactly boundedness of \(\eta\mapsto R_\eta\xi\) on \(\mathcal D\), with multiplier \(L_\xi\).

The mixed identity initially holds for \(\eta\in\mathcal D\) by that definition. Its extension to every \(\eta\in B_r\) is proved after the approximating net in NC01a. This derivation of the full bounded tests uses the complete modular graph construction, and supplies the exact product-core density used later in NC03.

<a id="nc00c"></a>
## NC00c. Gaussian vectors, complex powers and analytic multiplication

The real modular identities in BG6 and BW4 suffice to construct the analytic algebra used in (7). Put
\[
 g_n(t)=\sqrt{n/\pi}\,e^{-nt^2},\qquad
 \xi_n(z)=\int_{\mathbb R}g_n(t-z)U_t\xi\,dt
 \quad(\xi\in\mathcal A,\ z\in\mathbb C).
 \tag{7a}
\]
These are vectorwise integrals. On each compact set of complex parameters, the Gaussian and each of its derivatives have an integrable common majorant. Difference quotients therefore give an entire vector function and entire strong-operator functions
\[
 X_n(z)=\int g_n(t-z)U_tL_\xi U_{-t}\,dt,
 \qquad S\xi_n(z)=\int\overline{g_n(t-z)}U_tS\xi\,dt.
 \tag{7b}
\]
The second equality follows by taking finite real-parameter Riemann sums in the closed graph of the conjugate-linear \(S\). Their graph-norm tails converge by the same Gaussian majorant. In the first equality, test the integral against each \(\eta\in\mathcal D\) using mixed multiplication and BW4. It gives \(R_\eta\xi_n(z)=X_n(z)\eta\). Hence \(\xi_n(z)\in B_l\cap D(S)=\mathcal A\), with \(L_{\xi_n(z)}=X_n(z)\). There is no assertion that an arbitrary operator integral belongs to the weight's finite ideal without this vector test.

Let \(A=\log\Delta\), with its spectral domain, and let \(e_k=1_{[-k,k]}(A)\). The proved scalar Gaussian transform gives
\[
 e_k\xi_n(z)=e^{izA}e^{-A^2/(4n)}e_k\xi.
 \tag{7c}
\]
For every real \(\alpha\), the scalar function \(e^{\alpha s-s^2/(4n)}\) is bounded on the whole real line. Thus the spectral-domain criterion and (7c), followed by \(e_k\uparrow1\), give
\[
 \xi_n(z)\in\bigcap_{w\in\mathbb C}D(\Delta^w),
 \qquad \Delta^w\xi_n(z)=\xi_n(z-iw).
 \tag{7d}
\]
The sign comes from \(U_t=e^{itA}\): \(e^{izA}=\Delta^{iz}\). This computation includes all inverse domains.

The word “common” also requires right boundedness. For \(\xi\in\mathcal A\), put \(\chi=\Delta^{1/2}\xi=JS\xi\in\mathcal D\), by BG6. Its right Gaussian integral is a vector of \(\mathcal D\) by the right version of (7b). On every spectral band, (7c) gives
\[
 \xi_n(z)=\chi_n(z+i/2).
 \tag{7g}
\]
Both sides are actual Hilbert vectors, so the band identity passes to their full limits. Consequently every \(\xi_n(z)\) is in \(\mathcal A\cap\mathcal D\), with both bounded multipliers. The right argument uses \(F\chi\), which exists since \(\chi\in\mathcal D\), and hence proves its full right involution domain too. Likewise, anti-linearity and \(J\Delta^{1/2}J=\Delta^{-1/2}\) give
\[
 J\xi_n(z)=(S\xi)_n(\bar z-i/2).
 \tag{7h}
\]
To check (7h), write \(J\xi_n(z)\) as the right Gaussian of \(J\xi\) at \(\bar z\), and use \(\Delta^{-1/2}J\xi=S\xi\) on finite spectral bands. Thus conjugation preserves the left generating family as well. On the common intersection the two products agree, since \(L_\xi\zeta=R_\zeta\xi\), so finite products remain in both algebras. No boundedness of an unsmeared complex modular orbit is inferred.

For real \(r\), changing the integration variable gives
\(U_r\xi_n(z)=\xi_n(z+r)\) and
\(L_{\xi_n(z+r)}=U_rL_{\xi_n(z)}U_{-r}\).
The vector and multiplier functions for a product are
\[
 F(r)=\xi_n(z+r)\zeta_m(v+r),\qquad
 L_{F(r)}=L_{\xi_n(z+r)}L_{\zeta_m(v+r)}.
\]
They extend entirely in \(r\), by the locally bounded entire operator and vector functions in (7b). Each value is an algebra vector. The involution is the reversed product of the two involutions, so its graph function has the required conjugated parameter and locally bounded norm as well. On the real axis \(F(r)=U_rF(0)\), because BG6 gives algebra covariance. For each \(k\), the entire functions \(e_kF(z)\) and \(e^{izA}e_kF(0)\) agree on the real axis; scalar pairing and the power-series uniqueness proof make them equal everywhere. Since \(F(z)\) is an actual Hilbert vector, the spectral-domain criterion now gives \(F(0)\in D(\Delta^w)\) and \(\Delta^wF(0)=F(-iw)\). This proves the complex-power product law, including its domains, rather than analytically continuing a formal unbounded product.

Take the algebra generated by all the vectors \(\xi_n(z)\), and close this generating family under the involution and complex translates just described. The finite sums and products form \(\mathcal A_0\). The same entire-function argument for every finite product proves
\[
 \Delta^w\mathcal A_0=\mathcal A_0,
 \qquad \Delta^w(\xi\zeta)=(\Delta^w\xi)(\Delta^w\zeta).
 \tag{7e}
\]
For the involution of a Gaussian generator, conjugation of the kernel in (7b) gives the Gaussian of \(S\xi\) at \(\bar z\); its complex translates are still generators. Thus the indicated closure under involution creates no extra spectral-domain assumption.

Finally \(\xi_n(0)\to\xi\) and \(S\xi_n(0)\to S\xi\), because the positive mass-one Gaussian kernels form an approximate identity and \(U_t\) is strongly continuous. Also
\[
 \|L_{\xi_n(0)}\|\le\|L_\xi\|,
 \qquad L_{\xi_n(0)}\to L_\xi\text{ strongly}.
 \tag{7f}
\]
For the last assertion test each Hilbert vector in the strongly continuous orbit \(U_tL_\xi U_{-t}\), split the integral into a small interval and its Gaussian tail, and use the uniform operator bound. The identical argument for adjoints gives strong* convergence. Applying the whole argument to the opposite right algebra replaces \(\Delta\) by \(\Delta^{-1}\) and gives the right analytic graph and multiplier approximation. These are the full analytic and approximation inputs used in NC03–NC06.

<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="240" viewBox="0 0 1050 240">
<rect width="1050" height="240" fill="#f8fbff"/>
<g font-family="Arial, sans-serif" fill="#17344c">
<text x="24" y="36" font-size="24" font-weight="bold">A Gaussian controls every spectral power</text>
<text x="24" y="73" font-size="19">s = log λ ∈ ℝ; Uₜ has multiplier exp(its)</text>
<text x="24" y="109" font-size="19">ξₙ(z): exp(izs − s²/(4n))     →     Δʷξₙ(z) = ξₙ(z − iw)</text>
<text x="24" y="146" font-size="19">On each band |s| ≤ k: analytic multiplication is a bounded identity.</text>
<text x="24" y="180" font-size="19">All bands together: an actual vector value proves the full power domain.</text>
<text x="24" y="215" font-size="16">Proof: NC00c (7a)–(7f). No spectral bound on Δ and no cyclic vector are assumed.</text>
</g>
</svg>

The diagram displays the exact scalar multipliers and domain mechanism; it is a schematic of spectral calculus, not a plotted spectral distribution. Its editable source is the inline SVG. The scalar Gaussian and spectral arguments are the earlier CF/SC/SF/FF proofs; the bounded modular method is credited to Rieffel–Van Daele.

<a id="nc01"></a>
## NC01. Choosing a weight at arbitrary cardinality

Every von Neumann algebra has a faithful normal semifinite weight. Here is the construction used to choose the weight in (2). Start with a faithful normal concrete presentation. Nonzero positive elements are detected by positive normal vector functionals. The support lemma CG01 constructs the support of a normal positive functional, its faithful restriction, and its compression formula, independently of any natural cone.

Choose a maximal family of normal states \((\omega_i)_{i\in I}\) whose nonzero supports \(p_i\) are mutually orthogonal. The union of a chain remains such a family. Its support join is one: otherwise a vector state on \((1-\bigvee_i p_i)H\) provides another nonzero disjoint support. Define
\[
 \varphi(a)=\sup_{E\subset I\text{ finite}}\sum_{i\in E}\omega_i(a),
 \qquad a\in N_+.
 \tag{9}
\]
Finite nonnegative subsums prove additivity and positive homogeneity. For \(a_j\uparrow a\), normality follows by interchanging the two suprema over \(j\) and finite \(E\). If \(\varphi(a)=0\), every \(\omega_i(a)=0\), so \(a^{1/2}p_i=0\). The finite sums of the \(p_i\) converge strongly to one, and therefore \(a=0\). Thus the weight is faithful.

For \(p_E=\sum_{i\in E}p_i\), supportedness gives \(\varphi(p_E)=|E|\). For every \(a\in N_+\),
\[
 \varphi(p_Eap_E)\le\|a\|\varphi(p_E)<\infty,
 \qquad p_Eap_E\longrightarrow a\text{ strongly}.
\]
These uniformly bounded finite positive elements converge ultraweakly as well, by H03's series-vector tail estimate. Each finite positive element \(c\) lies in the finite span \(\mathfrak m_\varphi\), because \(c=c^{1/2}c^{1/2}\) and \(\varphi((c^{1/2})^*c^{1/2})=\varphi(c)<\infty\). Every element of \(N\) is a complex linear combination of positive elements. Consequently \(\mathfrak m_\varphi\) is ultraweakly dense in \(N\), which is semifiniteness. This also gives the strong density of the finite ideal, since \(xp_E\) has finite square weight for every \(x\in N\). No countability of \(I\) is asserted. The zero algebra uses the zero weight and the empty family.

The following direct construction supplies the GNS representation and full left Hilbert algebra for this weight. It retains the original algebra through a faithful normal representation.

<a id="nc01a"></a>
## NC01a. Approximating the entire bounded-vector space by finite-star vectors

Let \(\mathfrak n\) be either full multiplication left ideal, in its respective von Neumann algebra \(B\), and let \(\mathcal C=\mathfrak n\cap\mathfrak n^*\). This is a nondegenerate *-algebra by the operator construction. For a finite subset \(E\subset\mathcal C\) and \(\varepsilon>0\), put
\[
 h_E=\sum_{x\in E}x^*x,\qquad
 e_{E,\varepsilon}=h_E(h_E+\varepsilon)^{-1}.
\]
The positive contraction \(e_{E,\varepsilon}\) belongs to \(\mathfrak n\) by the left-ideal property and bounded calculus, and to \(\mathfrak n^*\) by self-adjointness. Thus it belongs to \(\mathcal C\). These contractions converge strongly to one along finite-set enlargement and \(\varepsilon\downarrow0\). Here is a direct bound, avoiding a countability assumption or an assertion of monotonicity for squares. If \(x\in E\), then \(x^*x\le h_E\), and
\[
 \|x(1-e_{E,\varepsilon})\|^2
 \le\|(1-e_{E,\varepsilon})h_E(1-e_{E,\varepsilon})\|
 \le\varepsilon/4.
\]
The last inequality is the scalar bound \(\varepsilon^2t/(t+\varepsilon)^2\le\varepsilon/4\). Taking adjoints shows convergence of \(e_{E,\varepsilon}\) to one on the range of every \(x^*\). Their linear span is dense because \(\mathcal C\) is self-adjoint and nondegenerate. The uniform contraction bound extends convergence to all of \(H\).

Use this net for \(\mathfrak n_r=R(B_r)\). For \(\eta\in B_r\), set \(\eta_i=e_i\eta\). Covariance gives \(R_{\eta_i}=e_iR_\eta\in\mathfrak n_r\). Its adjoint \(R_\eta^*e_i\) also lies in \(\mathfrak n_r\), since \(e_i\in\mathfrak n_r\) and this is a left ideal. The ideal intersection (4) therefore puts \(\eta_i\) in \(\mathcal D\). Strong convergence and the contraction bound give every assertion in (8). The identical proof on \(\mathfrak n_l=L(B_l)\) gives the left approximation.

For \(\xi\in B_l\), the defining equality \(L_\xi\eta_i=R_{\eta_i}\xi\) now tends to \(L_\xi\eta=R_\eta\xi\); both operator limits are justified on these fixed vectors. This proves the entire mixed identity in (3). All these proofs apply to nets at arbitrary cardinality and supply no extraneous involution-domain claim for their original merely bounded vectors.

<a id="nc01b"></a>
## NC01b. Normal GNS models and the original full diagonal-weight algebra

We use the complete CF1–10 Hilbert and bounded-calculus arguments and the CP01–06 concrete predual. In the following calculations the inner product is translated to the second-variable convention. CP06 identifies a concrete von Neumann algebra \(N\) isometrically with \((N_*)^*\). Its quotient predual is a norm-closed subspace of \(N^*\): Hahn–Banach gives the quotient norm as the supremum of its pairings with the unit ball of its dual. The normal coefficients therefore remain normal under functional-norm limits.

**Normal positive functionals.** For \(\omega\in N_*^+\), positivity and the scalar quadratic-polynomial test give
\[
 |\omega(b^*c)|^2\le\omega(b^*b)\omega(c^*c).
\]
Indeed \(\omega((b+zc)^*(b+zc))=A+2\operatorname{Re}(z d)+|z|^2C\ge0\), with \(A=\omega(b^*b)\), \(C=\omega(c^*c)\), and \(d=\omega(b^*c)\). For \(C>0\), choose \(z=-\overline d/C\); for \(C=0\), arbitrary phases and magnitudes of \(z\) force \(d=0\). This proves both cases.
Quotient \(N\) by the null space of this form and complete, using
\(\langle[b],[c]\rangle=\omega(b^*c)\). The null space is a left ideal: bounded order and the positive square root give
\[
 \omega(c^*a^*ac)\le\|a\|^2\omega(c^*c).
\]
Thus \(\pi_\omega(a)[c]=[ac]\) defines a contractive unital *-representation on \(H_\omega\), with cyclic vector \(\Omega_\omega=[1]\) representing \(\omega\). Multiplication, adjoints and the identity follow on quotient vectors by taking the displayed pairings, and extend by density.

This representation is normal. Indeed every predual functional is a series
\(f(a)=\sum_j\langle u_j,av_j\rangle\) with \(\sum_j\|u_j\|\|v_j\|<\infty\), by CP03–06. Fixed multiplication gives
\[
 f(b^*ac)=\sum_j\langle bu_j,acv_j\rangle,
 \qquad \sum_j\|bu_j\|\|cv_j\|
 \le\|b\|\|c\|\sum_j\|u_j\|\|v_j\|.
\]
In particular the coefficients on quotient vectors, \(\omega(b^*ac)\), belong to \(N_*\). For arbitrary vectors, approximate both by quotient vectors. Contractivity gives the functional-norm estimate
\[
 \|\langle\xi,\pi_\omega(\,\cdot\,)\eta\rangle
       -\langle\xi_0,\pi_\omega(\,\cdot\,)\eta_0\rangle\|
 \le\|\xi-\xi_0\|\|\eta\|+\|\xi_0\|\|\eta-\eta_0\|.
\]
The norm-closedness just proved puts each limiting coefficient in \(N_*\). An ultraweak functional on the target is itself a norm-summable series of coefficients. Its pullback is a norm-convergent series in \(N_*\), so \(\pi_\omega\) is ultraweak continuous. The zero functional gives the zero space.

**Arbitrary sums.** For any set-indexed family of such representations, take their Hilbert direct sum \(H=\bigoplus_i H_i\), with the componentwise action \(\pi(a)\). Each vector has countable support: for every positive integer \(n\), only finitely many component norms can exceed \(1/n\). Finite-support vectors are dense, and completeness follows by the coordinate argument in CF8. The coefficient series obeys
\[
 \langle\xi,\pi(a)\eta\rangle
 =\sum_i\langle\xi_i,\pi_i(a)\eta_i\rangle,
 \qquad\sum_i\|\xi_i\|\|\eta_i\|\le\|\xi\|\|\eta\|.
\]
Its finite sums belong to \(N_*\) and its tails converge in functional norm. The same target-predual series argument proves that the direct sum is normal, without a cardinality restriction.

Apply this construction to the supported functionals \(\omega_i\) from NC01. In fact the following proof allows any nonzero finite normal positive \(\omega_i\) with orthogonal supports \(p_i\) joining to one; it therefore also covers a faithful finite functional as a one-block family. Define
\[
 \mathfrak n_\varphi=\{x:\sum_i\omega_i(x^*x)<\infty\},
 \qquad \Lambda(x)=([x]_i)_i\in\bigoplus_i H_i.
\]
Its squared norm is \(\varphi(x^*x)\). The same left-ideal estimate defines the contractive action \(\pi(a)\Lambda(x)=\Lambda(ax)\).

This GNS space is the entire direct sum. For any finite tuple of quotient vectors \(([x_i]_i)_{i\in E}\), use \(x=\sum_{i\in E}x_ip_i\). Supportedness means \([yp_i]_i=[y]_i\) and \([yp_i]_j=0\) for \(j\ne i\), by the support compression and Cauchy–Schwarz. Hence \(\Lambda(x)\) is exactly the chosen finite tuple and \(x\in\mathfrak n_\varphi\). Such tuples are dense. The normal direct sum above is therefore the original weight's GNS representation.

Let \(R_i\) be the coordinate projection and let \(\eta_i=\Lambda(p_i)\). They satisfy
\[
 R_i\Lambda(x)=\Lambda(xp_i)=\pi(x)\eta_i,
 \qquad R_i\in\pi(N)',\qquad \sum_iR_i=1\text{ strongly}.
 \tag{9a}
\]
Here \(xp_i\in\mathfrak n_\varphi\), since its square weight is \(\omega_i(x^*x)\). The represented vector functional of \(\eta_i\) is \(\omega_i\). If \(\pi(a)=0\), (9a) gives \(\Lambda(ap_i)=0\); faithfulness of \(\varphi\) gives \(ap_i=0\) for every \(i\), hence \(a=0\). The representation is isometric. To see the norm assertion from the stated bounded calculus, if \(\|\pi(a)\|<\|a\|\), choose a continuous function on the spectrum of \(a^*a\) that vanishes on \([0,\|\pi(a)\|^2]\) but is nonzero at \(\|a\|^2\). Its nonzero calculus value is killed by \(\pi\), contradicting faithfulness.

**The image is a von Neumann algebra.** We give the compactness step explicitly. For a Banach space \(X\), place its dual unit ball in the product of closed scalar discs \(\prod_{x\in X}\{z:|z|\le\|x\|\}\), by evaluation. This product is compact. One direct proof uses choice to extend a filter with the finite-intersection property to an ultrafilter. On each scalar disc, repeated finite subdivision into closed squares chooses a nested square sequence of diameters tending to zero whose intersections with the disc belong to the ultrafilter. Scalar completeness gives a limit point in the disc; every neighbourhood belongs to that coordinate ultrafilter. The coordinate limits therefore give a product limit, because a basic neighbourhood tests only finitely many coordinates. If a family of product-closed sets with the finite-intersection property had empty intersection, its extending ultrafilter would give a limit lying in each of them, a contradiction. This proves compactness. The evaluation families satisfying additivity and complex homogeneity form a closed subset of the product, and the coordinate bound makes them precisely the dual unit ball. Its product topology is the weak* topology. This is Banach–Alaoglu with its scalar and choice inputs displayed.

Since \(N=(N_*)^*\), its unit ball is compact ultraweakly. Put \(B=\pi(N)\), a unital norm-closed C*-algebra by isometry. The complete self-adjoint contraction-density proof [ODF03–05](operator-density-foundations.md#odf03) supplies, for each self-adjoint contraction \(T\in B''\), a net of self-adjoint contractions \(\pi(a_\lambda)\) converging strongly to \(T\), with \(\|a_\lambda\|\le1\). Here the represented algebra has an identity, so the orbit closure in ODF03 contains each test tuple directly by using that identity. Compactness supplies a convergent subnet by the complete net construction in [COMPACT](../src/hypertraces-finite-injectivity.md#compactness). Explicitly, the closures of the tails have a common cluster point; index the subnet by triples consisting of a neighbourhood, an original tail index and a chosen later index hitting that neighbourhood. Shrink the neighbourhood and advance both indices in the order. A hit beyond both previously chosen indices gives a common successor, so this is directed, and projection onto the chosen index is order preserving and eventually beyond each original index. It gives the convergent subnet. Write its ultraweak limit as \(a\in N\). Normality makes \(\pi(a_\lambda)\) converge ultraweakly to \(\pi(a)\), while its bounded strong convergence has limit \(T\), by CP03–06's series-tail test. Coefficients separate operators, so \(T=\pi(a)\). Scaling and taking the real and imaginary self-adjoint parts of an arbitrary \(T\in B''\) prove \(B''=B\). We now write \(M=\pi(N)\).

The inverse identification is normal as well. On each closed norm ball, \(\pi\) is a continuous bijection from a compact ultraweak space to a Hausdorff ultraweak space, so its inverse is continuous there: a compact subset of a Hausdorff space is closed, by separating one exterior point from its points and taking a finite subcover. Let \(f\in N_*\), and put \(g=f\circ\pi^{-1}\in M^*\). Its restriction to the unit ball is ultraweak continuous. For \(\varepsilon>0\), continuity at zero gives finitely many \(h_1,\ldots,h_n\in M_*\) such that \(|g(x)|<\varepsilon\) whenever \(\|x\|\le1\) and all the \(h_j(x)\) are sufficiently small. In particular \(g\) has norm at most \(\varepsilon\) on the common kernel \(V=\bigcap_j\ker h_j\). Hahn–Banach CF3 extends this restriction to \(G\in M^*\) with \(\|G\|\le\varepsilon\). The functional \(g-G\) vanishes on \(V\), so it factors through the finite-dimensional map \(x\mapsto(h_1(x),\ldots,h_n(x))\). Extending a linear functional on its image to \(\mathbb C^n\) proves \(g-G\in\operatorname{span}\{h_j\}\subset M_*\). Since \(\varepsilon\) is arbitrary and \(M_*\) is norm closed, \(g\in M_*\). Thus \(\pi^{-1}\) pulls every normal functional back to a normal functional. Normal positive functionals can consequently be transported in both directions without a normality-converse theorem.

**The initial left Hilbert algebra and its closed graph.** Let
\(\mathcal A=\Lambda(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*)\), with product \(\Lambda(x)\Lambda(y)=\Lambda(xy)\) and involution \(\Lambda(x)^\sharp=\Lambda(x^*)\). The left-ideal estimate gives bounded left multiplication, and the original sum pairings give
\(\langle\Lambda(x)\Lambda(y),\Lambda(z)\rangle=\langle\Lambda(y),\Lambda(x^*)\Lambda(z)\rangle\). All these series are absolutely convergent by Cauchy–Schwarz. The finite-star set is a *-algebra: left multiplication preserves \(\mathfrak n_\varphi\), and applying the same fact to adjoints proves stability under products.

For \(a,b\in\mathfrak n_\varphi\), the inequalities
\((a^*b)^*(a^*b)\le\|a\|^2b^*b\) and \((a^*b)(a^*b)^*\le\|b\|^2a^*a\) put \(a^*b\) in the finite-star set. Thus \(p_Ex\) belongs to that set for \(x\in\mathfrak n_\varphi\), and
\(\Lambda(p_Ex)=\pi(p_E)\Lambda(x)\to\Lambda(x)\), since normality and \(p_E\uparrow1\) give \(\pi(p_E)\uparrow1\). This proves density of \(\mathcal A\). When \(x\) is finite-star, these vectors are products \(\Lambda(p_E)\Lambda(x)\), so the product span is dense as well. Finally \(p_Ex p_F\) is finite-star for every bounded \(x\in N\), by the two square bounds with right supports \(p_F\) and \(p_E\). Their represented operators converge strongly to \(\pi(x)\). Consequently the left algebra generates exactly \(M\).

The original involution is closable. First the subspace
\(K=\overline{\operatorname{span}\{b'\eta_i:b'\in M',i\in I\}}\) is all of \(H\). It reduces \(M'\); its projection belongs to \((M')'=M\), hence equals \(\pi(p)\) for a projection \(p\in N\). Since \(\pi(p)\eta_i=\eta_i\), we have \(\omega_i(1-p)=0\), so each support \(p_i\le p\). Their join is one, whence \(K=H\). For every finite-star \(x\), every \(b'\in M'\), and all \(i,j\), (9a), commutation and adjoints give the exact second-variable-linear identity
\[
 \langle R_i b'\eta_j,\Lambda(x^*)\rangle
 =\langle\Lambda(x),R_jb'^*\eta_i\rangle.
 \tag{9b}
\]
If \(\Lambda(x_n)\to0\) and \(\Lambda(x_n^*)\to\zeta\), (9b) makes \(\zeta\) orthogonal to \(R_iK\) for every \(i\). These spaces together span \(H\), so \(\zeta=0\). This proves closability of precisely the initial involution. Let its closure be \(S\). We have now supplied the left Hilbert algebra to which the complete BG1–6 construction applies.

**The bounded part of the original closed graph.** If \(x\in\mathfrak n_\varphi\), \(\Lambda(x)\in D(S)\), and \(S\Lambda(x)=\eta\), take finite-star \(x_n\) converging in this original graph. Identity (9b) passes to the limit. The same bounded adjoint computation with \(x\) on the right gives
\[
 \langle R_i b'\eta_j,\eta\rangle
 =\langle R_i b'\eta_j,\pi(x^*)\eta_i\rangle.
\]
The projected commutant-orbit spans are dense in \(R_iH\), so \(R_i\eta=\pi(x^*)\eta_i\). Summing squares yields
\(\varphi(xx^*)=\sum_i\|\pi(x^*)\eta_i\|^2=\|\eta\|^2<\infty\), and then (9a) gives \(\eta=\Lambda(x^*)\). Conversely finite-star vectors belong to the initial graph. Thus its closure has added no extra bounded finite-star vectors.

**Fullness.** For \(\xi\in B_l\), its multiplier belongs to \(M\), so \(L_\xi=\pi(x)\) for a unique \(x\in N\). The vectors \(\eta_i\) are right-bounded with \(R_{\eta_i}=R_i\), by testing \(L_a\eta_i=R_i a\) on \(\mathcal A\). Their self-adjoint multipliers and NC00a put them in \(\mathcal D\). The defining mixed test gives
\[
 R_i\xi=L_\xi\eta_i=\pi(x)\eta_i,
 \qquad \varphi(x^*x)=\sum_i\|R_i\xi\|^2=\|\xi\|^2.
\]
Thus \(x\in\mathfrak n_\varphi\), and (9a) gives \(\xi=\Lambda(x)\). Conversely, for \(x\in\mathfrak n_\varphi\), the finite-star vectors \(\Lambda(p_Ex)\to\Lambda(x)\) have multipliers \(\pi(p_Ex)\to\pi(x)\) strongly with bound \(\|x\|\). For every \(\eta\in\mathcal D\), pass to the limit in
\(R_\eta\Lambda(p_Ex)=\pi(p_Ex)\eta\). This proves \(\Lambda(x)\in B_l\) and \(L_{\Lambda(x)}=\pi(x)\). Therefore \(B_l=\Lambda(\mathfrak n_\varphi)\). Combining this with the preceding original-graph domain check gives
\[
 B_l\cap D(S)=\Lambda(\mathfrak n_\varphi\cap\mathfrak n_\varphi^*)=\mathcal A.
\]
To check fullness as an algebra, let \(\mathcal A''\) be the double completion from BG6. Every \(\xi\in\mathcal A''\) satisfies the bounded left-multiplier tests in BG6, so \(\xi\in B_l\). BG6 prove that its closed involution has the same original graph \(S\), so \(\xi\in D(S)\). Therefore \(\mathcal A''\subset B_l\cap D(S)=\mathcal A\); the reverse inclusion is also proved in BG6. Hence \(\mathcal A''=\mathcal A\). This is the full original left Hilbert algebra required in (2)–(4). The proof uses no normality converse for a general weight, no opposite-weight reconstruction, and no separability hypothesis.

<a id="nc02"></a>
## NC02. A positive symmetric operator has a covariant positive extension

Let \(T_0\) be a densely defined positive symmetric linear operator, with domain \(D\). Complete \(D\) for
\[
 \|v\|_V^2=\|v\|^2+\langle v,T_0v\rangle.
 \tag{10}
\]
The inclusion into \(H\) extends to a contraction \(\iota:V\to H\). This map is injective. Indeed, if \(v_n\) tends to \(v\in V\) and to zero in \(H\), then for every \(w\in D\),
\[
 \langle w,v_n\rangle_V
   =\langle (1+T_0)w,v_n\rangle_H\longrightarrow0.
\]
Consequently \(v\) is orthogonal in \(V\) to its dense subspace \(D\), and \(v=0\). Identify \(V\) with \(\iota V\subset H\). The continuous extension of the second term in (10) is a densely defined closed positive form \(q\), since its form norm is exactly the complete \(V\)-norm.

FF4 constructs its positive self-adjoint representing operator \(h\). Its operator-domain criterion says that \(v\in D(h)\) precisely when the form \(q(w,v)\) is \(\langle w,f\rangle\) for some \(f\in H\), for every \(w\in V\), and then \(hv=f\). Here is that criterion directly from FF4. Let \(j:V\to H\) be inclusion and \(B=jj^*\), so \(h=B^{-1}-1\) and \(D(h)=\operatorname{Ran}B\). If \(q(w,v)=\langle w,f\rangle_H\) for every \(w\in V\), then
\(\langle w,v\rangle_V=\langle jw,v+f\rangle_H\).
Hilbert representation gives \(v=j^*(v+f)\) as a vector of \(V\), hence its Hilbert image is \(B(v+f)\). Thus \(v\in D(h)\) and \(hv=f\). Conversely, if \(v=B u\), the identity \(j^*u\) for its graph vector gives \(q(w,v)=\langle w,u-v\rangle_H\). This proves both directions, with the exact operator domain.

For \(v\in D\), symmetry and form-norm approximation give \(q(w,v)=\langle w,T_0v\rangle\), so \(h\) extends \(T_0\).

If every unitary in a von Neumann algebra \(B\) preserves \(D\) and commutes with \(T_0\) there, it preserves (10), hence \(V\) and \(q\). FF5's uniqueness and commutant transport prove \(uhu^*=h\), including domains, for every such unitary. The spectral calculus then places every bounded transform of \(h\) in \(B'\). Thus \(h\) is affiliated with \(B'\). This proves the extension and its covariance, including the form-closure step used in Hiai's endpoint argument.

<a id="nc03"></a>
## NC03. Endpoint duality using all right-bounded vectors

Define the two closed square sets
\[
 C_l=\overline{\{\xi S\xi:\xi\in\mathcal A\}},
 \qquad C_r=\overline{\{\eta F\eta:\eta\in\mathcal D\}}.
 \tag{11}
\]
For any subset \(C\subset H\), its dual is
\[
 C^\vee=\{v:\langle u,v\rangle\in[0,\infty)\text{ for every }u\in C\}.
 \tag{12}
\]
We claim
\[
 \boxed{C_l=C_r^\vee,\qquad C_r=C_l^\vee.}
 \tag{13}
\]
First, commuting multipliers and the adjoint identities in (3)–(4) give
\[
 \langle\xi S\xi,\eta F\eta\rangle
 =\langle L_\xi L_\xi^*\eta,\eta\rangle
 =\|L_\xi^*\eta\|^2\ge0.
 \tag{14}
\]
The pair is real, so its order is unchanged by conjugation. This proves one inclusion in each equality.

Now let \(v\in C_r^\vee\). Define on the **whole** dense right-bounded space
\[
 T_v\eta=R_\eta v,
 \qquad \eta\in B_r.
 \tag{15}
\]
For \(\eta\in\mathcal D\),
\[
 \langle\eta,T_v\eta\rangle
 =\langle R_\eta^*\eta,v\rangle
 =\langle\eta F\eta,v\rangle\ge0.
\]
For general \(\eta\in B_r\), use (8). Both \(\eta_i\to\eta\) and \(R_{\eta_i}v\to R_\eta v\), so the same nonnegative diagonal inequality passes to \(\eta\). Polarization makes \(T_v\) symmetric and positive on its full domain. In particular it is closable: if \(\eta_n\to0\) and \(T_v\eta_n\to w\), testing symmetry against every \(\theta\in B_r\) gives \(\langle\theta,w\rangle=0\), and density gives \(w=0\).

The full-domain choice in (15) also proves covariance directly. Every \(y\in M'\) preserves \(B_r\), and (3) gives
\[
 T_v(y\eta)=R_{y\eta}v=yR_\eta v=yT_v\eta.
 \tag{16}
\]
NC02 therefore supplies a positive self-adjoint extension \(h\) affiliated with \(M\). It was not necessary first to put \(v\) in an involution domain.

Use the bounded resolvents
\[
 b_n=(1+h/n)^{-1}\in M,
 \qquad v_n=b_nv.
 \tag{17}
\]
For \(\eta\in B_r\), affiliation gives commutation with \(R_\eta\), and the fact that \(h\) extends (15) gives
\[
 R_\eta v_n=b_nR_\eta v=b_nh\eta.
 \tag{18}
\]
The operator \(b_nh\) is bounded and positive. Equations (3)–(4), or the defining bounded-multiplier test, show that \(v_n\in B_l\) and \(L_{v_n}=b_nh\ge0\). Also \(b_n\to1\) strongly, so \(v_n\to v\).

Every left-bounded vector \(w\) with \(a=L_w\ge0\) is a norm limit of left squares. Here is a proof entirely within bounded multiplication. For \(\varepsilon>0\), put
\[
 \xi_\varepsilon=(a+\varepsilon)^{-1/2}w,
 \qquad c_\varepsilon=L_{\xi_\varepsilon}=a(a+\varepsilon)^{-1/2},
 \qquad f_\varepsilon(a)=a(a+\varepsilon)^{-1}.
 \tag{19}
\]
Covariance puts \(\xi_\varepsilon\) in \(B_l\). Its positive self-adjoint multiplier and (4) put it in \(\mathcal A\), with \(S\xi_\varepsilon=\xi_\varepsilon\). Therefore
\[
 \xi_\varepsilon S\xi_\varepsilon
 =c_\varepsilon\xi_\varepsilon
 =f_\varepsilon(a)w\longrightarrow w.
 \tag{20}
\]
Indeed \(f_\varepsilon(a)\) tends strongly to the range support \(p\) of \(a\), and injectivity of multiplication gives \((1-p)w=0\) from \(L_{(1-p)w}=(1-p)a=0\). Thus (20) has the stated vector limit.

Apply this to every \(v_n\), then use closedness of the square set: \(v\in C_l\). This proves \(C_r^\vee\subset C_l\). Run the same proof on the opposite right Hilbert algebra to obtain \(C_l^\vee\subset C_r\). This proves (13), without a cyclic vector or a prior convexity assumption on the square sets. Dual sets are closed convex cones, so both endpoint sets are now closed convex cones.

Each left square is fixed by \(S\); closedness gives
\[
 C_l\subset D(S),\quad Su=u\ (u\in C_l).
 \tag{21}
\]
The right assertion is \(Fv=v\) on \(C_r\). Product reversal by \(J\), including \(FJ=JS\), gives
\[
 JC_l=C_r,
 \qquad \Delta^{1/2}C_l=C_r.
 \tag{22}
\]
The square spans are dense: complex polarization spans the product algebra by squares, and the product graph-core theorem gives density in \(H\). Thus neither cone has a nonzero vector together with its negative. This also records the endpoint graph domains needed for taking the quarter powers.

<a id="nc04"></a>
## NC04. Defining the middle cone and identifying both power descriptions

For \(\xi\in B_l\), define the always meaningful vector
\[
 Q(\xi)=L_\xi J\xi.
\]
Set
\[
 P=\overline{\{Q(\xi):\xi\in\mathcal A_0\}}.
 \tag{23}
\]
On the analytic multiplication algebra, (5) and (7) give
\[
 \Delta^{1/4}(\xi S\xi)
 = (\Delta^{1/4}\xi)J(\Delta^{1/4}\xi)
 =Q(\Delta^{1/4}\xi).
 \tag{24}
\]
Every expression in this equality belongs to its stated domain; \(\Delta^{1/4}\) maps \(\mathcal A_0\) onto itself.

Analytic left squares are dense in \(C_l\). For the approximants from NC00, the estimate
\[
 \|L_{\xi_r}S\xi_r-L_\xi S\xi\|
 \le\|L_{\xi_r}\|\,\|S\xi_r-S\xi\|
   +\|(L_{\xi_r}-L_\xi)S\xi\|
\]
gives this assertion first for each square, then for the whole closure. If \(u_n,u\in C_l\), (21) gives \(\Delta^{1/2}(u_n-u)=J(u_n-u)\), and the spectral pairing inequality gives
\[
 \|\Delta^{1/4}(u_n-u)\|^2
 \le\|u_n-u\|\,\|\Delta^{1/2}(u_n-u)\|
 =\|u_n-u\|^2.
 \tag{25}
\]
Therefore (24) extends to the closure description
\[
 P=\overline{\Delta^{1/4}C_l}
   =\overline{\Delta^{-1/4}C_r}.
 \tag{26}
\]
For the second equality use (22) and the spectral domain identity on \(C_l\). Both images in (26) are convex cones because the respective powers are linear on their entire cone domains. Their closures are convex too.

Equation (7) gives \(JQ(\xi)=Q(\xi)\), so \(J\) fixes \(P\) pointwise. Covariance and commutation of \(J\) with the real group give
\[
 U_tQ(\xi)=Q(U_t\xi),\qquad U_tP=P.
 \tag{27}
\]
No cone order theorem is being used to assert this group invariance.

<a id="nc05"></a>
## NC05. Self-duality by a positive Gaussian smoothing

For \(u\in C_l\), \(v\in C_r\), the spectral pairing identity and (13) give
\[
 \langle\Delta^{1/4}u,\Delta^{-1/4}v\rangle
 =\langle u,v\rangle\ge0.
 \tag{28}
\]
One obtains the identity first on bounded spectral bands and then by convergence in the two quarter-power domains. The two descriptions in (26) imply \(P\subset P^\vee\).

Suppose \(w\in P^\vee\). Define
\[
 w_n=G_nw,
 \qquad G_n=\sqrt{n/\pi}\int_{\mathbb R}e^{-nt^2}U_t\,dt
       =\exp\!\left(-\frac{(\log\Delta)^2}{4n}\right).
 \tag{29}
\]
The integral is a Hilbert-vector integral, obtained by truncation and scalar pairing; its absolute norm bound is one. The Gaussian Fourier formula in MA03/16 proves the spectral equality. The scalar multiplier converges to one and is bounded by one, so \(w_n\to w\). For every real \(\alpha\),
\[
 \sup_{s\in\mathbb R}\exp\left(\alpha s-\frac{s^2}{4n}\right)<\infty,
\]
which, together with (6), proves \(w_n\in D(\Delta^\alpha)\). Thus every power used next has an actual vector value.

The kernel in (29) is nonnegative. Equation (27) implies that \(G_n\) preserves \(P\); self-adjointness of \(G_n\) implies that it preserves \(P^\vee\). For \(u\in C_l\),
\[
 \langle u,\Delta^{1/4}w_n\rangle
 =\langle\Delta^{1/4}u,w_n\rangle\ge0.
\]
Endpoint duality gives \(\Delta^{1/4}w_n\in C_r\). Its inverse quarter power is defined, and equals \(w_n\); (26) therefore puts \(w_n\in P\). Closedness and its vector limit give \(w\in P\). We have proved
\[
 \boxed{P=P^\vee.}
 \tag{30}
\]

<a id="nc06"></a>
## NC06. Preservation by every bounded algebra element

The generating set in (23) can be enlarged to **all left-bounded vectors**:
\[
 P=\overline{\{Q(\xi):\xi\in B_l\}}.
 \tag{31}
\]
First use Gaussian approximation for \(\xi\in\mathcal A\). Its vector convergence and strong multiplier convergence with a uniform bound give \(Q(\xi_r)\to Q(\xi)\). Next approximate \(\xi\in B_l\) by the left version of (8); the same estimate gives \(Q(\xi_i)\to Q(\xi)\). Both limits lie in \(P\). The reverse containment follows from \(\mathcal A_0\subset B_l\).

For \(a\in M\), \(\xi\in B_l\), covariance says that \(a\xi\) is still in \(B_l\). Since \(JaJ\in M'\),
\[
 Q(a\xi)=aL_\xi J(a\xi)
        =aL_\xi(JaJ)J\xi
        =aJaJ\,Q(\xi).
 \tag{32}
\]
Equations (31)–(32) and boundedness give
\[
 \boxed{aJaJ(P)\subset P\quad(a\in M).}
 \tag{33}
\]
This proof uses the genuine left ideal \(B_l\); it does not put \(a\xi\) in the finite-star algebra, which need not be a left ideal.

<a id="nc07"></a>
## NC07. Central conjugation with its domain proof

Let \(z\in Z(M)\). The finite-star ideal is preserved by \(z\), since it is a left ideal in each of its two factors and \(z\) commutes with them. On its GNS core,
\[
 S(z\Lambda(a))=\Lambda((za)^*)=z^*S\Lambda(a).
 \tag{34}
\]
Closed graph approximation extends this to \(zD(S)\subset D(S)\), with \(Sz=z^*S\) there. For a central unitary \(u\), apply it also to \(u^*\) to obtain equality \(uD(S)=D(S)\). Thus \(u\) preserves the closed form \(\|S\xi\|^2\) on \(D(S)\). The form representation and transport give \(u\Delta u^*=\Delta\), including domains, so \(u\) commutes with \(\Delta^{1/2}\). In the polar factorization,
\[
 Ju\Delta^{1/2}=Su=u^*S=u^*J\Delta^{1/2}.
\]
The range of \(\Delta^{1/2}\) is dense, so \(Ju=u^*J\), and hence \(JuJ=u^*\). Every central element is a complex linear combination of central unitaries: for a self-adjoint central contraction \(c\), the two elements \(c\pm i(1-c^2)^{1/2}\) are central unitaries; split a general central element into real and imaginary parts and scale. Conjugating the coefficients gives
\[
 \boxed{JzJ=z^*\quad(z\in Z(M)).}
 \tag{35}
\]
Together, (5), (30), pointwise fixedness by \(J\), and (33) construct the standard form for the chosen arbitrary-weight GNS representation.

<a id="nc08"></a>
## NC08. The universal cyclic core and natural cone

Let \(A\subset B(K)\) be any von Neumann algebra and let \(\gamma\) be cyclic and separating. This includes any support-corner algebra used in CG09. The finite vector weight \(\omega_\gamma\) is faithful and normal. Its GNS map \(a\mapsto a\gamma\) identifies its GNS representation with the given one. The finite-star Hilbert algebra is therefore \(\mathcal A=A\gamma\), with algebra unit \(\gamma\), and
\[
 S=\overline{a\gamma\mapsto a^*\gamma}.
 \tag{36}
\]
Apply the operator construction NC00, so (5) holds for this same original graph.

A direct pairing on \(A\gamma\) gives, for \(b'\in A'\),
\[
 \langle S(a\gamma),b'\gamma\rangle
 =\langle\gamma,ab'\gamma\rangle
 =\langle b'^*\gamma,a\gamma\rangle.
\]
Thus \(b'\gamma\in D(S^*)\) and \(S^*(b'\gamma)=b'^*\gamma\). Taking \(a=b'=1\) gives \(S\gamma=S^*\gamma=\gamma\), hence \(\Delta\gamma=\gamma\) and \(J\gamma=\gamma\). From (5),
\[
 F=S^*=JSJ
 \tag{37}
\]
with equality of domains, since \(J\Delta^{1/2}J=\Delta^{-1/2}\). The original graph core \(A\gamma\) is sent by \(J\) to \(A'\gamma\), by \(JAJ=A'\) and \(J\gamma=\gamma\). Therefore (37) proves
\[
 \boxed{F=\overline{b'\gamma\mapsto b'^*\gamma},
 \quad A'\gamma\text{ is an actual graph core of }F.}
 \tag{38}
\]
In particular the modular graph-core assertion is proved for the given cyclic representation, rather than inferred from the axioms of a self-dual cone.

Here every left-bounded vector is \(a\gamma\), \(a\in A\): its multiplier applied to the right unit \(\gamma\) equals that vector by (3). Conversely each \(a\gamma\) is left bounded with multiplier \(a\). Thus (31) becomes
\[
 P_\gamma=\overline{\{aJaJ\gamma:a\in A\}}.
 \tag{39}
\]
The endpoint square set is \(C_l=\overline{A_+\gamma}\), since a left square is \(aa^*\gamma\) and every positive element has a bounded square root. The corresponding right statement is \(C_r=\overline{A'_+\gamma}\). Equation (26) consequently gives
\[
 \boxed{P_\gamma
   =\overline{\{\Delta^{1/4}a\gamma:a\in A_+\}}
   =\overline{\{\Delta^{-1/4}b'\gamma:b'\in A'_+\}}.}
 \tag{40}
\]
Every \(a\gamma\) lies in \(D(\Delta^{1/2})\), and
\[
 \Delta^{1/2}a\gamma=Ja^*\gamma.
 \tag{41}
\]
The natural cone (39) is self-dual by NC05, and has all the preservation and central identities proved above. Real modular covariance, the actual spectral powers/logarithm domains, the Gaussian entire-vector cores, (38), and (40)–(41) are precisely the cyclic outputs used in CG09 and in the cyclic realization proof. No faithful state on the original arbitrary algebra has been assumed.

## An exact finite-weight model

<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="410" viewBox="0 0 1120 410" role="img" aria-labelledby="title desc">
<title id="title">Quarter powers turn the two endpoint vectors into the same positive matrix</title>
<desc id="desc">In the Hilbert Schmidt model with density d equal to diagonal one and four, the positive algebra element a has entries two one one two. Its left GNS vector has entries two two one four and its right endpoint vector has entries two one two four. Applying Delta to the quarter power on the left or negative quarter power on the right gives the positive matrix with entries two square root two square root two four.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#3f5362"/></marker><style>text{font-family:Arial,sans-serif;fill:#182a38}.title{font-size:27px;font-weight:700}.body{font-size:21px}.small{font-size:18px}.matrix{font-size:29px}.label{font-size:23px;font-weight:600}</style></defs>
<rect width="1120" height="410" fill="white"/>
<text x="35" y="43" class="title">Quarter powers meet at the positive matrix</text>
<text x="35" y="76" class="body">M = M₂(C), H = Hilbert–Schmidt matrices, d = diag(1, 4), Δ(X) = dXd⁻¹, J(X) = X*</text>
<g transform="translate(40 108)"><rect width="270" height="180" rx="12" fill="#eaf0f8"/><text x="22" y="32" class="label">u ∈ Cₗ</text><text x="22" y="65" class="body">u = a d¹ᐟ²</text><path d="M85 84H73V157H85M190 84H202V157H190" fill="none" stroke="#182a38" stroke-width="2"/><text x="97" y="112" class="matrix">2</text><text x="159" y="112" class="matrix">2</text><text x="97" y="147" class="matrix">1</text><text x="159" y="147" class="matrix">4</text></g>
<g transform="translate(425 108)"><rect width="270" height="180" rx="12" fill="#e5f4eb"/><text x="22" y="32" class="label">w ∈ P</text><text x="22" y="65" class="body">w = d¹ᐟ⁴ a d¹ᐟ⁴</text><path d="M76 84H64V157H76M198 84H210V157H198" fill="none" stroke="#182a38" stroke-width="2"/><text x="91" y="112" class="matrix">2</text><text x="154" y="112" class="matrix">√2</text><text x="81" y="147" class="matrix">√2</text><text x="162" y="147" class="matrix">4</text></g>
<g transform="translate(810 108)"><rect width="270" height="180" rx="12" fill="#f0eaf5"/><text x="22" y="32" class="label">v ∈ Cᵣ</text><text x="22" y="65" class="body">v = d¹ᐟ² a</text><path d="M85 84H73V157H85M190 84H202V157H190" fill="none" stroke="#182a38" stroke-width="2"/><text x="97" y="112" class="matrix">2</text><text x="159" y="112" class="matrix">1</text><text x="97" y="147" class="matrix">2</text><text x="159" y="147" class="matrix">4</text></g>
<path d="M323 210H412" fill="none" stroke="#3f5362" stroke-width="3" marker-end="url(#arrow)"/>
<path d="M797 210H708" fill="none" stroke="#3f5362" stroke-width="3" marker-end="url(#arrow)"/>
<text x="340" y="189" class="label">Δ¹ᐟ⁴</text><text x="722" y="189" class="label">Δ⁻¹ᐟ⁴</text>
<text x="35" y="326" class="body">a = [2, 1; 1, 2] ≥ 0.  The middle matrix has trace 6 and determinant 6, so it is positive.</text>
<text x="35" y="357" class="body">In this finite model: Cᵣ = Cₗ∨ and P = {positive Hilbert–Schmidt matrices} = P∨.</text>
<text x="35" y="388" class="small">Exact three-vector example of NC03–NC05. General domains and closures are proved there; the full space has eight real dimensions.</text>
</svg>


The diagram uses the second-variable-linear Hilbert–Schmidt pairing
\(\langle X,Y\rangle=\operatorname{Tr}(X^*Y)\), the weight
\(\varphi(a)=\operatorname{Tr}(da)\) with \(d=\operatorname{diag}(1,4)\), and
\(\Lambda(a)=ad^{1/2}\). The vector multiplication is
\(X\mathbin{\star}Y=Xd^{-1/2}Y\). Thus the left endpoint contains
\(u=ad^{1/2}\), the right contains \(v=d^{1/2}a\), and both quarter-power paths give
\(w=d^{1/4}ad^{1/4}\). For the displayed positive \(a\), these are exactly the three matrices in the figure.
The finite model has \(P\) equal to all positive Hilbert–Schmidt matrices. This illustrates the domains and identities of NC03–NC05; their arbitrary-weight proof remains in the text. Hiai's Example 3.6(2), printed page22, supplies the related tracial Hilbert–Schmidt standard model. The density matrix and the diagram's coordinates are explicit substitutions into (5), (24) and (26).
