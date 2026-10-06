# The real Connes spectrum: orbit supports, corners and cocycles

*Independent proof development, GPT-6.1 Sol (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

Let \(M\ne0\) be a von Neumann factor and let \(\alpha:\mathbb R\to\operatorname{Aut}(M)\) be a group of normal \(*\)-automorphisms, continuous on every normal scalar coefficient. No separability, finite state, modular realization, norm continuity of the action or countable-decomposability is assumed in this chapter. Write \(M^\alpha\) for its fixed algebra. A fixed projection is a projection \(p\in M^\alpha\). Its nonzero corner has the restricted action \(\alpha^p\).

The earlier complete inputs are the smooth real Fourier filters and scalar local division [RF-1–3](OA-FLOW-RF.md#oa-flow.rf.1); the actual normal filters, hull/support equality, local detection, invariant bimodules and full product-support rule [AL-1–4](OA-FLOW-AL.md#oa-flow.al.1); arbitrary projection joins, bounded supports and central supports PC-1 and PC-2; the full Hilbert/spectral calculus [SF-0](OA-FLOW-SF.md#oa-flow.sf.sf0); and bounded strong-to-ultraweak convergence [SF-2](OA-FLOW-SF.md#oa-flow.sf.sf2). Scalar compact-interval arguments use CF-1. All further arguments are written below.

The freely readable source development is [Alain Connes, *Une classification des facteurs de type III* (1973), Definition 2.2.1, Theorem 2.2.4, Lemma 2.2.6 and Lemmas 2.3.2–2.3.4, printed pp.174–178](https://numdam.org/article/ASENS_1973_4_6_2_133_0.pdf#page=43). The source's orbit-support sandwich mechanism is reconstructed here with the actual real-line local proofs. No general locally compact abelian theorem, external spectral-synthesis theorem or cited result replaces any step.

<a id="oa-flow.cs.0"></a>
## CS-0. Exact spectra and the intersection being proved invariant

Use \(\widehat f(r)=\int f(t)e^{itr}\,dt\) and the weak-star normal filters \(T_f x=\int f(t)\alpha_t(x)dt\), constructed in [AL-1](OA-FLOW-AL.md#oa-flow.al.1). The spectra are exactly the [AL-2](OA-FLOW-AL.md#oa-flow.al.2) annihilator hulls, and not a different support convention:

<a id="equation-cs1"></a>

\[
 \operatorname{Sp}_\alpha(x)
 =\bigcap_{T_fx=0}\{r:\widehat f(r)=0\},\qquad
 \operatorname{Sp}(\alpha)
 =\bigcap_{T_f=0}\{r:\widehat f(r)=0\}.
 \tag{CS1}
\]
For a closed set \(E\), \(M(\alpha,E)\) consists of elements whose first spectrum is contained in \(E\). [AL-2](OA-FLOW-AL.md#oa-flow.al.2)–4 prove that these spaces are ultraweakly closed, that a nonzero element has nonempty spectrum, and that

<a id="equation-cs2"></a>

\[
 \operatorname{Sp}(\alpha)=\overline{\bigcup_x\operatorname{Sp}_\alpha(x)},\qquad
 M(\alpha,E)M(\alpha,F)\subseteq M(\alpha,\overline{E+F}).
 \tag{CS2}
\]
Adjoint reflects the spectrum; time translation preserves it. Every real \(r\) in an action spectrum and every open interval \(O\ni r\) admit a nonzero element with compact spectrum in \(O\). This follows by applying a compact smooth filter nonzero at \(r\), as proved in [AL-3](OA-FLOW-AL.md#oa-flow.al.3). Filtering an element of a fixed bimodule \(eMf\) stays in that bimodule. Its spectrum is the ambient element spectrum, and the corner spectrum has this same local detection property.

Define

<a id="equation-cs3"></a>

\[
 \Gamma(\alpha)=
 \bigcap_{0\ne p\in\operatorname{Proj}(M^\alpha)}
       \operatorname{Sp}(\alpha^p).
 \tag{CS3}
\]
All spectra in this intersection are closed. They contain zero: the corner unit \(p\) is fixed and \(T_f p=\widehat f(0)p\), so every annihilator of the entire corner action vanishes at zero. They are symmetric, by the adjoint and union identities in ([CS2](OA-FLOW-CS.md#equation-cs2)). Thus \(\Gamma(\alpha)\) is closed, symmetric and contains zero, before any subgroup assertion is proved.

<a id="oa-flow.cs.1"></a>
## CS-1. The support-join sandwich lemma

Suppose \(0\ne y\in eMf\), where \(e,f\) are fixed projections, and \(\operatorname{Sp}_\alpha(y)\) is contained in a compact interval \(I\). Define its two orbit supports

<a id="equation-cs4"></a>

\[
 a=\bigvee_{t\in\mathbb R}s(\alpha_t(y)\alpha_t(y)^*),\qquad
 b=\bigvee_{t\in\mathbb R}s(\alpha_t(y)^*\alpha_t(y)).
 \tag{CS4}
\]
PC-1 constructs each support and every join as the projection onto the indicated closed range or closed span. Both joins are nonzero; \(a\le e\) and \(b\le f\). Normal automorphisms preserve order, joins and supports: they preserve least upper bounds by applying their inverse, and preserve the range support as the least projection \(q\) with \(qx=x\), or \(xq=x\) for the initial support. Consequently \(\alpha_s\) permutes each joined family, so \(a,b\) are fixed. Moreover \(a\alpha_t(y)=\alpha_t(y)=\alpha_t(y)b\) for every \(t\).

If \(0\ne z\in aMa\), some \(t\) satisfies \(\alpha_t(y)^*z\ne0\). Otherwise every vector in \(zH\) is killed by every \(\alpha_t(y)^*\), and is perpendicular to their joined ranges, namely \(aH\). This gives \(az=0\), contradicting \(az=z\ne0\). Put \(w=\alpha_t(y)^*z\). Its corner relations are \(bw=w=wa\). If \(w\alpha_u(y)=0\) for all \(u\), \(w\) vanishes on the closed span of the ranges \(\alpha_u(y)H\), which is \(aH\). Since \(w=wa\), that would give \(w=0\). Thus some \(u\) gives

<a id="equation-cs5"></a>

\[
 0\ne v=\alpha_t(y)^*z\alpha_u(y)\in bMb.
 \tag{CS5}
\]
If \(\operatorname{Sp}_\alpha(z)\subseteq J\) for a compact interval \(J\), the complete product, adjoint and time-translation rules give

<a id="equation-cs6"></a>

\[
 \operatorname{Sp}_\alpha(v)\subseteq -I+J+I=J+(I-I).
 \tag{CS6}
\]
The equality is of scalar sets; each is compact, so the product-support closure creates no additional points. Repeating the argument with \(y^*\) exchanges \(a,b\), with the same difference interval \(I-I\). No polar partial isometry of \(y\) is assumed fixed, and no spectral assertion about such a polar partial isometry is used.

Let \(\delta\ge0\) be the length of \(I\), so \(I-I=[-\delta,\delta]\). Localize any \(r\in\operatorname{Sp}(\alpha^a)\) to a nonzero \(z\in aMa\) with spectrum in \([r-\eta,r+\eta]\), for arbitrary \(\eta>0\). The nonzero \(v\) above has a spectral point in \(\operatorname{Sp}(\alpha^b)\cap[r-\eta-\delta,r+\eta+\delta]\), by ([CS2](OA-FLOW-CS.md#equation-cs2)) and ([CS6](OA-FLOW-CS.md#equation-cs6)). Let \(\eta\downarrow0\); compactness of the bounded scalar interval and closedness of the target spectrum give

<a id="equation-cs7"></a>

\[
 \operatorname{Sp}(\alpha^a)\subseteq
      \operatorname{Sp}(\alpha^b)+[-\delta,\delta],\qquad
 \operatorname{Sp}(\alpha^b)\subseteq
      \operatorname{Sp}(\alpha^a)+[-\delta,\delta].
 \tag{CS7}
\]
This is the precise transfer estimate. The center of \(I\) cancels; the error is its length. It is not an assertion that the two uncompressed corner spectra are equal.

<a id="oa-flow.cs.2"></a>
## CS-2. Arbitrarily narrow transfers between any two fixed corners

Let \(e,f\) be any two nonzero fixed projections of the factor and let \(\delta>0\). PC-2 proves \(eMf\ne\{0\}\): otherwise their central supports would be orthogonal, whereas each nonzero projection of a factor has central support \(1\). Choose \(0\ne y_0\in eMf\).

Its element spectrum is nonempty. Choose a point in that spectrum and an open interval around it of length less than \(\delta\). [AL-3](OA-FLOW-AL.md#oa-flow.al.3) supplies a compact smooth filter supported there whose value at that point is nonzero; its filtered element \(y\) is nonzero and remains in \(eMf\). Its compact spectrum is contained in a closed interval \(I\) of length at most \(\delta\). [CS-1](OA-FLOW-CS.md#oa-flow.cs.1) therefore produces nonzero fixed \(a\le e\), \(b\le f\) with both transfer inclusions ([CS7](OA-FLOW-CS.md#equation-cs7)), now with error at most \(\delta\). This uses only local smooth detection, not synthesis or an eigenvector assumption.

<a id="oa-flow.cs.3"></a>
## CS-3. Corner invariance and the directed spectral neighborhoods

For every nonzero fixed \(e\),

<a id="equation-cs8"></a>

\[
 \Gamma(\alpha^e)=\Gamma(\alpha).
 \tag{CS8}
\]
Indeed the fixed projections of \(eMe\) are exactly the ambient fixed projections \(a\le e\), with identical restricted spectra. Thus the full intersection ([CS3](OA-FLOW-CS.md#equation-cs3)) is contained in the corner intersection.

Conversely let \(r\in\Gamma(\alpha^e)\). For any nonzero fixed \(f\) and any \(\delta>0\), [CS-2](OA-FLOW-CS.md#oa-flow.cs.2) gives \(a\le e\), \(b\le f\) satisfying ([CS7](OA-FLOW-CS.md#equation-cs7)). Since \(r\in\operatorname{Sp}(\alpha^a)\), its distance from \(\operatorname{Sp}(\alpha^b)\), and hence from \(\operatorname{Sp}(\alpha^f)\), is at most \(\delta\). The latter spectrum is closed. Letting \(\delta\downarrow0\) gives \(r\in\operatorname{Sp}(\alpha^f)\). Since \(f\) was arbitrary, \(r\in\Gamma(\alpha)\), as required.

The closed thickenings

<a id="equation-cs9"></a>

\[
 \mathcal F_\alpha=
 \{\operatorname{Sp}(\alpha^e)+[-\varepsilon,\varepsilon]:
        0\ne e\in\operatorname{Proj}(M^\alpha),\ \varepsilon>0\}
 \tag{CS9}
\]
have intersection \(\Gamma(\alpha)\) and form a downward-directed family. To check the latter, start with two such sets using \(e,f,\varepsilon_1,\varepsilon_2\). Choose positive \(\delta,\rho\) with \(\rho\le\varepsilon_1\) and \(\delta+\rho\le\varepsilon_2\). [CS-2](OA-FLOW-CS.md#oa-flow.cs.2) gives \(a\le e\), \(b\le f\) and \(\operatorname{Sp}(\alpha^a)\subseteq\operatorname{Sp}(\alpha^b)+[-\delta,\delta]\). Restriction gives \(\operatorname{Sp}(\alpha^a)\subseteq\operatorname{Sp}(\alpha^e)\) and \(\operatorname{Sp}(\alpha^b)\subseteq\operatorname{Sp}(\alpha^f)\). Hence \(\operatorname{Sp}(\alpha^a)+[-\rho,\rho]\) is contained in both original thickenings. Their intersection is ([CS3](OA-FLOW-CS.md#equation-cs3)), since a point in all positive thickenings of a closed spectrum belongs to that spectrum.

<a id="oa-flow.cs.4"></a>
## CS-4. Spectral translation and the subgroup law

We first prove

<a id="equation-cs10"></a>

\[
 \Gamma(\alpha)+\operatorname{Sp}(\alpha)
       =\operatorname{Sp}(\alpha).
 \tag{CS10}
\]
Let \(r\in\operatorname{Sp}(\alpha)\), \(s\in\Gamma(\alpha)\), and \(\eta>0\). Choose \(0\ne x\) with compact spectrum in \([r-\eta,r+\eta]\). Put \(p=\bigvee_t s(\alpha_t(x)^*\alpha_t(x))\), a nonzero fixed projection by [CS-1](OA-FLOW-CS.md#oa-flow.cs.1)'s support argument. Since \(s\in\operatorname{Sp}(\alpha^p)\), choose \(0\ne z\in pMp\) with spectrum in \([s-\eta,s+\eta]\). Some \(t\) has \(\alpha_t(x)z\ne0\): if all products vanished, \(zH\) would be in the common kernel, the complement of \(pH\), contradicting \(pz=z\). Its spectrum is nonempty and lies in \([r+s-2\eta,r+s+2\eta]\). Thus \(r+s\) belongs to the closed \(\operatorname{Sp}(\alpha)\), by letting \(\eta\downarrow0\). This proves one inclusion of ([CS10](OA-FLOW-CS.md#equation-cs10)); its other inclusion follows from \(0\in\Gamma(\alpha)\).

The same translation proof works for each corner action, with its own intersection definition; it did not use the factor bridge. If \(r,s\in\Gamma(\alpha)\), [CS-3](OA-FLOW-CS.md#oa-flow.cs.3) gives \(s\in\Gamma(\alpha^p)\) for every nonzero fixed \(p\), while \(r\in\operatorname{Sp}(\alpha^p)\). Applying that translation statement inside the corner puts \(r+s\) in every \(\operatorname{Sp}(\alpha^p)\). Hence \(r+s\in\Gamma(\alpha)\). [CS-0](OA-FLOW-CS.md#oa-flow.cs.0) already proved symmetry, closedness and zero membership. Therefore \(\Gamma(\alpha)\) is a closed additive subgroup of \(\mathbb R\). In particular translation by each of its elements preserves every invariant-corner spectrum, as well as the full action spectrum.

<a id="oa-flow.cs.5"></a>
## CS-5. The balanced matrix action proves exterior-cocycle invariance

Let \(u_t\in\mathcal U(M)\) be strongly continuous and satisfy

<a id="equation-cs11"></a>

\[
 u_{t+s}=u_t\alpha_t(u_s),\qquad
 \beta_t(x)=u_t\alpha_t(x)u_t^*.
 \tag{CS11}
\]
The identity gives \(u_0=1\); multiplication and the group law show that \(\beta\) is a group of normal automorphisms. It has continuous normal coefficients: [AL-1](OA-FLOW-AL.md#oa-flow.al.1) gives strong-star continuity of each \(\alpha\) orbit and of bounded products. A strongly continuous unitary family is strongly-star continuous, since
\(\|(u_t^*-u_s^*)\xi\|=\|(1-u_tu_s^*)\xi\|\to0\).
Bounded strong-star multiplication and SF-2 therefore give the claimed scalar continuity.

On \(N=M\overline\otimes M_2\), represented concretely on \(H\oplus H\), put

<a id="equation-cs12"></a>

\[
 v_t=\begin{pmatrix}1&0\\0&u_t\end{pmatrix},\qquad
 W_t(X)=v_t(\alpha_t\otimes\operatorname{id})(X)v_t^*.
 \tag{CS12}
\]
Here \(N\) is simply the weakly closed algebra of two-by-two matrices with entries in \(M\). Normality and scalar continuity hold entry by entry, using the four bounded coordinate maps. The cocycle law in ([CS11](OA-FLOW-CS.md#equation-cs11)) gives
\(v_{t+s}=v_t(\alpha_t\otimes\operatorname{id})(v_s)\), so \(W_{t+s}=W_tW_s\). Each map is a normal automorphism, and its inverse is \(W_{-t}\).

The algebra \(N\) is a factor. Indeed an element of its center commutes with the four scalar matrix units, hence is a diagonal matrix with the same entry \(a\) twice. Commutation with every diagonal copy of \(M\) gives \(a\in Z(M)=\mathbb C1\). Thus its center is scalar, with no classification or tensor-product theorem imported.

The projections \(p_1=1\otimes e_{11}\), \(p_2=1\otimes e_{22}\) are nonzero and fixed by \(W\). Their corner actions, under the actual coordinate isomorphisms, are \(\alpha\) and \(\beta\). Such an isomorphism preserves the weak-star integral and every annihilator hull: testing its normal coefficients gives \(\theta(T_fx)=T_f\theta(x)\), and injectivity preserves which filters are zero. Applying [CS-3](OA-FLOW-CS.md#oa-flow.cs.3) twice therefore gives

<a id="equation-cs13"></a>

\[
 \Gamma(\alpha)=\Gamma(W^{p_1})=\Gamma(W)
        =\Gamma(W^{p_2})=\Gamma(\beta).
 \tag{CS13}
\]
This proves invariance for an actual strongly continuous unitary cocycle. It neither constructs a cocycle from an arbitrary modular-looking action nor uses an arbitrary-cocycle-realization theorem.

<a id="oa-flow.cs.6"></a>
## CS-6. An exact finite matrix check

Take \(M=M_3(\mathbb C)\), \(h=\operatorname{diag}(0,2,5)\) and \(\alpha_t(x)=e^{ith}xe^{-ith}\). Then \(\alpha_t(e_{ij})=e^{it(h_i-h_j)}e_{ij}\), so the scalar Fourier integral and finite matrix expansion give

<a id="equation-cs14"></a>

\[
 \operatorname{Sp}_\alpha(e_{ij})=\{h_i-h_j\},\quad
 \operatorname{Sp}(\alpha)=\{0,\pm2,\pm3,\pm5\},\quad
 \Gamma(\alpha)=\{0\}.
 \tag{CS14}
\]
For the first identity, a filter vanishes exactly when its transform vanishes at that point; smooth bumps exclude every different point. For the full action identity, the filter acts diagonally on the nine matrix units, so its annihilator hull is exactly the finite set displayed. Each rank-one diagonal corner has identity action and spectrum \(\{0\}\), proving the last identity with [CS-0](OA-FLOW-CS.md#oa-flow.cs.0). Corner spectra themselves need not coincide: the corner on coordinates one and two has spectrum \(\{0,\pm2\}\), whereas the third-coordinate corner has only \(\{0\}\). [CS-3](OA-FLOW-CS.md#oa-flow.cs.3) preserves their Connes-spectrum intersections, not these individual spectra.

For \(y=e_{13}\), [CS-1](OA-FLOW-CS.md#oa-flow.cs.1) has \(I=\{-5\}\), \(a=e_{11}\), \(b=e_{33}\), and zero transfer error. The sandwich \(y^*e_{11}y=e_{33}\) explicitly cancels the two frequencies \(+5\) and \(-5\). With \(u_t=e^{-ith}\), ([CS11](OA-FLOW-CS.md#equation-cs11)) gives the identity action \(\beta\); its Connes spectrum is still \(\{0\}\). This example verifies the sign and the distinction between action spectrum and Connes spectrum. It is not a type III model or a proof of the general theorem.

**Exercise.** In ([CS7](OA-FLOW-CS.md#equation-cs7)), why is the error the length of \(I\), rather than its distance from zero? **Solution.** The two copies of \(y\) in ([CS5](OA-FLOW-CS.md#equation-cs5)) contribute \(-I\) and \(I\); their sum is \(I-I=[-\delta,\delta]\). Translating \(I\) by any scalar leaves that difference unchanged. The support-join argument supplies the nonzero sandwich independently of the central frequency.

This chapter proves the real-action corner, subgroup, translation and exterior-cocycle statements at arbitrary-factor scope. The comparison with the modular \(S\)-invariant requires the separate full n.s.f. GNS spectral proof and exact corner transport; no such identity is assumed above.
