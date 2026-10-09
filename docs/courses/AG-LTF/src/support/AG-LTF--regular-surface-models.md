# Regular surface models and exceptional-curve contraction

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. Public domain (CC0 1.0).*

This reading, including its proofs, is released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). It supplies the surface input to [Stable pointed family extension, S.3](AG-LTF--stable-pointed-family-extension.md#S3). Comparison references credit the human-authored Stacks Project; the proofs here are independently written.

<a id="exact-admitted-source-and-terms"></a>

## 1. Scope and main components

A surface here is an integral Noetherian scheme of dimension two. The resolution argument concerns excellent surfaces in equal characteristic, allowing imperfect residue fields. Normalization is finite, the regular locus open, and normal local rings have normal completions. A modification is a proper birational map with integral source. A normalized point blowup is a closed-point blowup followed by normalization.

The retained ordinary foundations are: Cohen structure and finite regular subrings of complete local domains; Serre's criterion, regular local factoriality and excellence; proper coherent finiteness, Stein factorization, flat base change, formal functions and cohomological dimension bounded by fibre dimension; curve Riemann–Roch and duality; Grothendieck duality and local/Matlis duality. We also use the modification theorems that an admissible blowup dominates a proper modification, and a generically finite proper map has finite strict transform after blowing up its base, the latter in [Stacks, 0B49](https://stacks.math.columbia.edu/tag/0B49). Surface resolution and contraction are proved below.

<a id="main-component"></a>

**Lemma 1.1 (the common-field component).** Given modifications \(Y\to T\) and \(T'\to T\) of excellent surfaces, choose a dense open \(V\) where both maps are identities. Normalize its reduced closure in \(Y\times_TT'\), obtaining \(W\). Both projections are proper birational maps of integral normal surfaces, independently of \(V\).

**Proof.** The selected generic point has residue field \(K(T)\). Its reduced closure is integral. A smaller dense open selects the same point and the same closure. Each product projection is proper, as is its restriction to this closed subscheme. Finite normalization preserves properness. The resulting maps induce identities on the common field, proving birationality and dimension two. ∎

We call this the **normalized main component**. The schematic closure of the integral open graph already gives the indicated reduced structure.

**Example 1.2.** The self-product of the blowup \(B\to\mathbf A^2_k\) of the origin contains the entire exceptional fibre \(\mathbf P^1_k\times_k\mathbf P^1_k\). The common open graph closes instead to the diagonal \(B\), meeting that fibre only in its diagonal \(\mathbf P^1_k\). Thus an unrestricted product has an additional vertical component.

<a id="field-degree-main-component"></a>

**Lemma 1.3 (completed field degrees).** For finite inclusions \(A_0\subset B\subset A\) of excellent normal domains, write their fields \(K_0\subset L\subset K\). Let \(Y\to\operatorname{Spec}B\) be regular and birational. Normalize the closure of \(\operatorname{Spec}K\) in \(Y\times_B\operatorname{Spec}A\), obtaining \(X\). Then \(X\to\operatorname{Spec}A\) is proper birational and \(X\to Y\) finite dominant of degree \(d=[K:L]\). Above a closed point \(y\) of local dimension two, the completed local factors of \(X\) are finite normal domains over \(\widehat{\mathcal O}_{Y,y}\), with positive degrees summing to \(d\).

**Proof.** The product, its selected closed component and its normalization are finite over \(Y\). Their generic field is \(K\). The other projection is proper by base change, and an isomorphism at the generic point of \(\operatorname{Spec}A\).

Put \(D=\mathcal O_{Y,y}\), \(C=(\pi_*\mathcal O_X)_y\). Each maximal localization of this finite semilocal algebra is normal of dimension two, by integrality and the dimension formula, and Cohen–Macaulay by \(S_2\). Parameters of \(D\) remain parameters in these rings, because the fibre is finite, and form a regular sequence on \(C\). Hence \(C\) is free over regular \(D\): its positive Koszul Tor groups with the residue field vanish, so a minimal free resolution has no positive term. Its rank is \(d\). Completion decomposes \(C\otimes_D\widehat D\) as the product of the completed local factors. Each is normal by excellence, hence a domain, and is a direct summand of a free module over local \(\widehat D\), hence free of positive rank. These ranks are their fraction-field degrees and sum to \(d\). ∎

This corrects the intermediate-field pullback in [Stacks, 0BGN](https://stacks.math.columbia.edu/tag/0BGN).

## 2. Domination by point blowups

<a id="domination"></a>

**Theorem 2.1.** Every modification of excellent normal surfaces is dominated by finitely many normalized point blowups. If its target is regular, all these blowups are ordinary blowups of regular surfaces. Compare [Stacks, 0BBT](https://stacks.math.columbia.edu/tag/0BBT).

**Proof.** Normalize the source \(Y\) of \(Y\to T\). A proper birational map onto normal \(T\) is an isomorphism in codimension at most one and wherever its fibres are finite: locally a finite algebra in the common field equals the normal target algebra. Its exceptional locus lies over finitely many closed points; count its contracted irreducible curves.

Blow up such a point \(t\), normalize, and take \(Y'\) to be the normalized main component of the pullback (Lemma 1.1). A curve contracted by \(Y'\to T'\) maps onto a contracted curve in \(Y\): if its image in \(Y\) were a point, its image in the product would also be a point, contradicting finiteness of normalization. The map \(Y'\to Y\) is an isomorphism at curve generic points, so this correspondence is injective.

Fix a contracted curve \(C\) over \(t\), and its generic DVR \(V_C\). Choose \(u\in V_C\) with residue transcendental over \(\kappa(t)\), and write \(u=a/b\) with \(a,b\in\mathcal O_{T,t}\). Both are in its maximal ideal: a unit \(b\) would give residue in \(\kappa(t)\), and a unit \(a\) gives the same contradiction using \(u^{-1}\). Thus \(N=\min(v_C(a),v_C(b))>0\). If \(C\) remains contracted to a closed point \(t'\) after a blowup, divide \(a,b\) by the local exceptional generator \(e\). Its valuation is positive. The same quotient \(u=a'/b'\) still has transcendental residue over \(\kappa(t')\), which is finite over \(\kappa(t)\). Both \(a',b'\) remain in the maximal ideal, but their minimum valuation is \(N-v_C(e)<N\). Finitely many steps remove this curve; the injective correspondence then strictly reduces the total curve count. Induction terminates at an isomorphism to the current target, which maps to \(Y\).

At a regular point, its parameters \(x,y\) give exceptional fibre \(\operatorname{Proj}(\kappa[x,y])=\mathbf P^1_\kappa\), with conormal \(\mathcal O(1)\). At each closed exceptional point, the exceptional equation together with a lifted parameter of \(\mathbf P^1\) generates the maximal ideal. The blowup is regular there and unchanged elsewhere. Normalization is unnecessary. ∎

Every product in this proof is replaced by its normalized main component; that is the surface to which the valuation decrease applies.

## 3. Local vanishing and boundedness

Here \(A\) is an excellent normal local domain of dimension two, with closed point \(s\), punctured spectrum \(U\), and normal modification \(f:X\to\operatorname{Spec}A\). Its structure-sheaf pushforward is \(A\), its fibres have dimension at most one, and \(H^i(X,F)=0\) for coherent \(F\) and \(i>1\). Its \(H^1(\mathcal O_X)\) has finite length.

<a id="local-vanishing"></a>

**Lemma 3.1.** A nonempty effective Cartier divisor \(Z\) supported on the closed fibre has positive conormal degree on some reduced irreducible fibre component.

**Proof.** For every component \(C_i\), choose a closed point \(p_i\) off the other components and a local function \(g_i\) vanishing there but nonzero on \(C_i\). Write \(g_i=a_i/b_i\) with \(a_i,b_i\in A\), and set \(h=\prod a_i\). Let \(e_i=v_{C_i}(h)>0\), \(z_i=v_{C_i}(Z)\), and maximize the positive ratio \(z_i/e_i\). Replace \(h\) by \(h^{z_i}\) and \(Z\) by \(e_iZ\). Height-one valuations then show \(h\in\Gamma(X,\mathcal O_X(-Z))\), with nonzero restriction on \(C_i\). At \(p_i\), the restriction retains a factor \(g_i\): dividing the remaining factor by a local equation of \(Z\) is regular, by normality and the fact that no other component of \(Z\) passes through \(p_i\). A nonzero section with a zero has positive degree on the proper integral curve. Undo the multiplier of \(Z\). ∎

**Lemma 3.2.** The restriction \(H^1(X,\mathcal O_X)\to H^1(f^{-1}U,\mathcal O_X)\) is injective.

**Proof.** A kernel class is an extension \(0\to\mathcal O_X\to V\to\mathcal O_X\to0\) split over \(f^{-1}U\). The quotient defines a section \(\sigma\) in \(\mathbf P(V)\) with trivial conormal. Its splitting gives a disjoint second section on that open. Normalize the latter's closure. If it misses \(\sigma\), it is proper and lies in the affine complement of \(\sigma\); its map to normal \(X\) is finite birational, hence an isomorphism, giving a global splitting. If it meets \(\sigma\), the pullback intersection is a nonempty effective Cartier divisor supported on the closed fibre, with trivial conormal. Lemma 3.1 excludes this. ∎

**Lemma 3.3 (surface dualizing vanishing).** For dualizing modules normalized by \(\omega_X[2]=f^!(\omega_A[2])\), one has \(R^1f_*\omega_X=0\).

**Proof.** First \(\operatorname{Hom}_{D(A)}(\kappa(s)[-1],Rf_*\mathcal O_X)=0\). Adjunction identifies it with \(\operatorname{Ext}^1_X(\mathcal O_{X_s},\mathcal O_X)\): the degree-zero term in \(Lf^*\kappa(s)[-1]\) is torsion, and negative-degree terms require negative Ext. Represent a class by \(0\to\mathcal O_X\to F\to\mathcal O_{X_s}\to0\). Pullback by \(\mathcal O_X\to\mathcal O_{X_s}\) splits by Lemma 3.2. Thus \(1\) lifts to a global \(v\in F\). Multiplication by the fibre ideal induces \(\mathfrak m_s\to A\), which is multiplication by a scalar in \(A\): it is a scalar in the common field, integral at every height-one DVR because \(\mathfrak m_s\) is the unit ideal there. Subtract that scalar from \(v\); the resulting lift is annihilated by the fibre ideal and splits the extension.

If \(R^1f_*\omega_X\ne0\), its finite length gives a nonzero quotient to \(\kappa(s)\), hence a nonzero map \(Rf_*(\omega_X[2])\to\kappa(s)[1]\). Duality converts this to a nonzero map \(\kappa(s)[-1]\to Rf_*\mathcal O_X\), since normalized duality sends \(\kappa(s)\) to itself and is an involution. This contradicts the first calculation. ∎

This proves the surface Grauert–Riemenschneider vanishing used here in positive as well as zero characteristic.

<a id="torsion-bound"></a>

**Lemma 3.4.** Fixed nonzero \(a\in A\) gives a uniform bound on the lengths of \(H^1(X,\mathcal O_X)[a]\). Compare [Stacks, 0AXJ](https://stacks.math.columbia.edu/tag/0AXJ).

**Proof.** First choose a reduced principal divisor containing the height-one primes dividing \(a\). Start with \(c\) in those primes, a parameter \(g\) independent of it, and \(N\) with \(\mathfrak m^N\subset\mathfrak m(c,g)\). Perturbations in this power preserve \(\operatorname{length}A/(c,g)\); the one-dimensional parameter-length bound bounds their number of minimal primes. Maximize that number among perturbations also in the prescribed primes, and write the divisor as \(\sum e_jP_j\). Prime avoidance gives \(u_j\) of valuation one at \(P_j\) and zero at the others. Multiply the \(u_j^2\) for \(e_j=1\) and \(u_j\) for \(e_j>1\), and a factor in \(\mathfrak m^N\) outside every \(P_j\). Adding this perturbation makes every old coefficient one, and maximality forbids new primes. The principal quotient is reduced, since a principal quotient of a normal surface has no embedded associated primes. The resulting \(c\) satisfies \(a\mid c^r\) for some \(r\), by valuations. For any module \(M\), multiplication by \(c^{j-1}\) embeds \(M[c^j]/M[c^{j-1}]\) into \(M[c]\). A bound for reduced \(c\)-torsion therefore bounds \(a\)-torsion.

Assume \(A/(a)\) reduced. Let \(Z=V(a)\subset X\), and \(Z_0\) the closure of its part over \(U\). This is a reduced proper birational curve over \(\operatorname{Spec}A/(a)\), has finite fibres and is finite. Its functions lie between \(A/(a)\) and the finite normalization \(D\). Restriction \(\Gamma(Z,\mathcal O_Z)\to\Gamma(Z_0,\mathcal O_{Z_0})\) is injective: a kernel section's boundary in \(H^1(X,\mathcal O_X)\) vanishes over \(U\), so Lemma 3.2 makes the section come from \(A\); its zero on \(Z_0\) then makes it zero on \(Z\). The multiplication sequence identifies \(H^1(X,\mathcal O_X)[a]\) with \(\Gamma(Z,\mathcal O_Z)/(A/(a))\), a submodule of fixed finite-length \(D/(A/(a))\). ∎

**Lemma 3.5 (rationality).** Call \(A\) rational if all normal modifications have \(H^1(\mathcal O)=0\). Boundedness of these lengths gives a normalized point sequence with every local surface ring rational.

**Proof.** Leray for \(X'\xrightarrow gX\to\operatorname{Spec}A\) gives
\[
0\to H^1(X,\mathcal O_X)\to H^1(X',\mathcal O_{X'})
\to H^0(X,R^1g_*\mathcal O_{X'})\to0.
\]
The final sheaf is supported on finitely many closed points. Choose a modification maximizing the bounded length. Every further modification has zero \(R^1g_*\mathcal O\). A local modification at a closed point spreads to a neighbourhood and glues to the identity elsewhere; its first cohomology is the relevant stalk. Thus its local surface rings are rational. Rationality persists for birational local extensions essentially of finite type: realize them on normal projective modifications by closing affine presentations in projective space, and apply the same sequence to further local modifications. Theorem 2.1 gives the required point sequence.

Regular local surface rings are rational. Theorem 2.1 dominates any modification by ordinary regular point blowups. Their two affine charts give cohomological dimension one. Filtration by the exceptional divisor has quotients \(\mathcal O_{\mathbf P^1}(j)\), with zero \(H^1\) for \(j\ge-1\). Serre vanishing for large \(\mathcal O(-nE)\) and descent along this filtration give \(H^1(\mathcal O)=0\). Leray proves it for a sequence, and the displayed injection proves it for the original modification. ∎

**Lemma 3.6 (separable boundedness).** Finite separable extensions \(A\subset B\) of excellent normal local surface rings preserve boundedness. Compare [Stacks, 0AXL](https://stacks.math.columbia.edu/tag/0AXL).

**Proof.** Choose a field basis \(b_1,\ldots,b_n\in B\), and \(d=\det(\operatorname{Tr}(b_ib_j))\ne0\). The strict-transform finiteness theorem and normalization dominate any modification of \(B\) by \(Y\) finite over a normal modification \(X\) of \(A\). Domination increases \(H^1\). Normality extends trace, giving an injection
\[
\pi_*\mathcal O_Y\to\mathcal O_X^n,\quad h\mapsto(\operatorname{Tr}(b_ih))_i.
\]
Its cokernel is killed by \(d\), using the reverse map \((s_i)\mapsto\sum b_is_i\) and the adjugate of the trace matrix. Thus the kernel of \(H^1(Y,\mathcal O_Y)\to H^1(X,\mathcal O_X)^n\) is killed by \(d\) and bounded by Lemma 3.4. The image is bounded by the hypothesis on \(A\). Dividing \(A\)-length by the finite residue degree bounds \(B\)-length as well. ∎

<a id="inseparable-boundedness"></a>

**Lemma 3.7 (inseparable degree \(p\)).** For \(A=k[[x,y]]\) in characteristic \(p>0\), its normalization \(B\) in a purely inseparable degree-\(p\) extension has bounded first-cohomology lengths of normal modifications. Compare [Stacks, 0B4U](https://stacks.math.columbia.edu/tag/0B4U).

**Proof.** Write \(L=K(g)\), \(g^p=f\in A\), clearing denominators by a \(p\)-th power. Choose \(k^p\subset k'\subset k\) of degree \([k:k']=p^e<\infty\), so \(df\ne0\) over \(A_0=k'[[x^p,y^p]]\). If \(f\) has an exponent not divisible by \(p\), use \(k'=k\). Otherwise choose a coefficient outside \(k^p\), a member of a \(p\)-basis detecting it, and let \(k'\) be generated by \(k^p\) and all the other basis members. Then \([k:k']=p\) and its coefficient derivation detects \(df\). Thus \(\Omega_{A/A_0}\) is free of rank \(r=e+2\). Choose \(\eta\in\Omega^{r-1}_{A/A_0}\) with \(\theta=\eta\wedge df\ne0\), and set \(\omega_A=\Omega^r_{A/A_0}\).

For \(S=R[z]/(z^p-h)\), differential trace kills pulled-back forms and sends \(\alpha\wedge z^i dz\) to zero for \(i<p-1\), and to \(\alpha\wedge dh\) for \(i=p-1\). The relation \(dh=0\) on \(S\) makes it well defined. It is generator-independent: for \(z=P(w)=\sum\lambda_jw^j,\ w^p=b\), one has \(h=\sum\lambda_j^pb^j\). For \(i<p-1\), the derivative identity \(P^iP'=(P^{i+1})'/(i+1)\) makes all coefficients of \(w^{mp-1}\) zero. For \(i=p-1\), lift the universal calculation to integers and use \(P^{p-1}P'=(P^p)'/p\). Reduction gives coefficient \(\sum j\lambda_j^pb^{j-1}\), exactly the coefficient in \(dh=(\sum j\lambda_j^pb^{j-1})db\). Wedge multiplication proves the assertion in every degree.

For a finite normal degree-\(p\) purely inseparable morphism this trace extends integrally at height-one DVRs, hence into the target's reflexive hull. A finite normal degree-\(p\) DVR extension has ramification index \(p\) or residue degree \(p\), since their product is its free-module rank. In the first case a source uniformizer has \(p\)-th power a target uniformizer. In the second take a lift of a residue generator. Reduction modulo the target uniformizer and Nakayama give \(S=R[z]/(z^p-h)\) in both cases, where the preceding formula is integral.

Finite duality gives \(c:\Omega^r_{B/A_0}\to\omega_B=\operatorname{Hom}_A(B,\omega_A)\). The forms \(\eta\wedge g^{p-1-i}dg\) give functionals \(\varphi_i\) with \(\varphi_i(g^j)=\delta_{ij}\theta\). Thus \(c\) is generically onto and its coherent cokernel is killed by fixed nonzero \(d\in B\).

Dominate a modification \(Y\) of \(B\) by one finite over a modification \(X\) of \(A\), then dominate \(X\) by regular point blowups (Theorem 2.1). Put \(D_X=(\Omega^r_{X/A_0})^{**}\). Its generic identification extends to \(D_X\to\omega_X\). For a point blowup the chart identity \(y=xt,\ dy=t\,dx+x\,dt\) shows that its determinant module is either \(b^*D_X\) or \(b^*D_X(E)\). Their pushforward is \(D_X\) and higher pushforward zero, by the two-chart exceptional filtration of Lemma 3.5. Duality adjunction extends the map at each step. Composing differential trace with it gives \(c_Y:\Omega^r_{Y/A_0}\to\omega_Y\) extending \(c\). Global canonical-module trace therefore realizes \(c\) inside its range.

Lemma 3.3 and duality give
\[
0\to\Gamma(Y,\omega_Y)\to\omega_B\to
\operatorname{Ext}^2_B(H^1(Y,\mathcal O_Y),\omega_B)\to0.
\]
The last term, the Matlis dual of \(H^1(Y,\mathcal O_Y)\), is killed by \(d\). The original module is therefore killed by \(d\), and its whole length is bounded by Lemma 3.4. Domination gives the bound for the initial modification. ∎

## 4. Rational singularities and the Gorenstein step

<a id="rational-to-gorenstein"></a>

**Lemma 4.1.** For rational \(A\), its ordinary point blowup is normal with rational local surface rings. If \(A\) has a dualizing module, finitely many point blowups give invertible dualizing module. Compare [Stacks, 0BBV](https://stacks.math.columbia.edu/tag/0BBV).

**Proof.** Normalize its point blowup first, and put \(I=\mathfrak m\mathcal O_X=\mathcal O_X(-E)\). Globally generated coherent sheaves have zero \(H^1\), as quotients of copies of \(\mathcal O_X\) with \(H^2=0\). Thus \(H^1(I^n)=0\), and \(\Gamma(I)=\mathfrak m\), a proper ideal of \(A\) containing \(\mathfrak m\). For generators \(x_i\) of \(I\), the kernel \(F\) of \(\mathcal O_X^q\to I\) is locally free, and \(F\otimes I\) is generated by the relations \(x_ie_j-x_je_i\), checked where some \(x_i\) generates \(I\). Tensoring by \(I^{n-1}\) and taking cohomology gives \(\Gamma(I^n)=\mathfrak m^n\) by induction. On the unnormalized blowup, sections of \(\mathcal O(n)\) include \(\mathfrak m^n\); on its normalization they equal that module. A nonzero quotient of the normalization algebra by the original structure sheaf would have a nonzero section after a large ample twist. These equalities exclude it. Rationality of its local rings follows from Lemma 3.5.

The Cartier exceptional curve is Cohen–Macaulay. Its ideal sequences give
\[
H^1(E,\mathcal O_E(n))=0,\qquad
H^0(E,\mathcal O_E(n))=\mathfrak m^n/\mathfrak m^{n+1}\quad(n\ge0).
\]
Its very ample \(H=\mathcal O_E(1)\) has degree \(\dim_\kappa\mathfrak m/\mathfrak m^2-1\), at least two when \(A\) is singular.

For a proper Cohen–Macaulay curve \(D\) with constants \(k\) and very ample \(H\) of degree at least two, \(\omega_D\otimes H\) is globally generated. After algebraic closure, a hyperplane through a specified point avoiding the component generic points gives \(0\to\omega_D\to\omega_D\otimes H\to Q\to0\), with finite-support \(Q\) of length at least two. Let \(F\) be generated by \(\omega_D\) and the global sections. It has nonzero image in \(Q\), since \(h^1(\omega_D)=1\). If \(H^1(F)\ne0\), duality gives a retraction to \(\omega_D\) whose composite on \(\omega_D\) is a nonzero scalar. The complementary finite-support summand cannot embed in the Cohen–Macaulay \(\omega_D\otimes H\). Thus \(H^1(F)=0\). A nonzero quotient \((\omega_D\otimes H)/F\) would give a global section outside \(F\), contradicting its definition. Nakayama gives generation at the specified point; field descent finishes.

Lemma 3.3 and duality give \(\Gamma(X,\omega_X)=\omega_A\). Adjunction gives \(\omega_X|_E=\omega_E(1)\). In
\[
0\to\omega_X(n+1)\to\omega_X(n)\to\omega_E(n+1)\to0,
\]
the final \(H^1\) is zero for \(n\ge0\), by duality and \(H^0(E,H^{-(n+1)})=0\). Serre vanishing at large \(n\) therefore gives \(H^1(\omega_X(n))=0\) for all \(n\ge0\). Restriction and the curve generation show that \(f^*\omega_A\to\omega_X\) is onto near \(E\), and elsewhere an isomorphism.

Make the strict transform of \(\omega_A\) invertible by its Fitting-ideal blowup, and dominate by Theorem 2.1. Every point blowup is already normal. Every ancestor of a final singular point is singular, since regular point blowups preserve regularity. The surjectivity just proved persists along these ancestors. It factors through the invertible torsion-free quotient given by the Fitting blowup; a surjection from a line bundle onto torsion-free rank-one \(\omega_X\) is an isomorphism. At regular points \(\omega_X\) is already invertible. ∎


## 5. Double points and termination

<a id="double-point-resolution"></a>

**Theorem 5.1.** An excellent rational Gorenstein local surface ring in equal characteristic is resolved by finitely many blowups of singular closed points. Intermediate surfaces are normal with rational Gorenstein singularities. Compare [Stacks, 0BGE](https://stacks.math.columbia.edu/tag/0BGE).

**Proof.** Lemma 4.1 makes the point blowup normal and rational. Its dualizing module is generated by the pullback of free rank-one \(\omega_A\), so is free. Excellence preserves normal completions. For the exceptional curve \(E\), adjunction gives \(\omega_E=\mathcal O_E(-1)\). Since \(H^1(\mathcal O_E)=0\) and \(H^0(\mathcal O_E)=\kappa\), Riemann–Roch gives degree two for \(\mathcal O_E(1)\), and \(h^0(\mathcal O_E(n))=2n+1\). Therefore
\[
\operatorname{gr}_{\mathfrak m}A=\kappa[T_1,T_2,T_3]/(q)
\]
for one nonzero quadratic form: the degree-two kernel is one-dimensional and this quotient has the required dimension in every degree. In a Cohen presentation the completion is thus a hypersurface with initial form \(q\). We compute there; completion preserves exceptional fibres and completed local rings after point blowups.

We need a fact valid over imperfect fields. If a nonzero polynomial \(Q\) of degree at most two belongs to \(J^2\subset\kappa[u,v]\), where \(J\) has colength greater than one, then \(Q\) is a scalar square of an affine linear polynomial. A nonzero partial derivative is linear and in \(J\); change coordinates to make it \(u\). Then \(J=(u,F(v))\), with \(\deg F>1\), or \(J=(u)\). Reduction first modulo \(u\), then modulo \(u^2\), makes \(Q\) a scalar multiple of \(u^2\). If both derivatives vanish, the remaining case is characteristic two with \(Q=a+du^2+v^2\). If \(a,d\) are squares, we are done. Otherwise a coefficient derivation gives \(u^2+\alpha\in J\), hence also \(v^2+\beta\in J\). Their ideal \(J_0\) has colength four and free conormal on those generators; \(J=J_0\) contradicts \(Q\in J^2\). If \(J/J_0\) contains a nonzero affine linear expression the first argument applies. Otherwise it has dimension at most one in the basis \(1,u,v,uv\), and the only remaining colength is three. After algebraic closure and translation a colength-three ideal containing \((u^2,v^2)\) must be \((u,v)^2\); its square contains no nonzero quadratic. This contradiction proves the fact.

Assume first \(q\) is not a scalar square. At a singular point on the blowup, its affine conic equation belongs to the square of the point ideal; otherwise it gives a linear relation between the three proposed parameters. The quadratic fact forces the point to be rational. Center it at \([1:0:0]\). Then \(q=q(T_2,T_3)\) is a nonsquare binary quadratic, whose conic has that vertex as its unique singular point. On the chart \(x_2=x_1u,\ x_3=x_1v\), the new quadratic restricts at \(T_1=0\) to the same binary quadratic. Every continuing singular point is consequently unique, rational, nonsquare, and lies in the \(x_1\)-chart. The same \(x_1\) defines all successive exceptional divisors.

Here is the termination argument. An infinite sequence with identical residue field and fixed \(t\) generating the pulled-back maximal ideal at every step defines a nonsingular formal arc. In its successive local rings \(A_n\), put \(J_n=\ker(A\to A_n/\mathfrak m_n^{n+1})\). Divide a maximal-ideal generator by \(t\) at the next step, and subtract its residue multiple of \(t\); the adjusted generator belongs to \(\mathfrak m_{n+1}^2\). Also \(t^j\notin\mathfrak m_n^{j+1}\), since the next step would otherwise make \(t^j\) divisible by \(t^{j+1}\). Induction gives \(\operatorname{length}A/J_n=n+1\) and \(J_n/J_{n+1}\) generated by \(t^{n+1}\). Successive subtraction in its graded ring \(\kappa[t]\) shows the inverse limit is complete with maximal ideal \((t)\). It is a complete DVR \(R\); the chart formulas extend \(A_n\to R\), and \(\widehat A\to R\) is onto.

This arc on normal \(\widehat A\) becomes regular after finitely many blowups. Let \(P=\ker(\widehat A\to R)\), write \(P=(z_2,\ldots,z_r)\) minimally, and take \(z_2\) generating its generic DVR ideal. The module \(P/(P^2+(z_2))\) is \(t\)-torsion. Thus \(t^{a_i}z_i-b_iz_2\in P^2\) for each \(i>2\). Modulo \(P\), \(b_i\) is zero or a unit times \(t^{c_i}\); absorb its remainder into the quadratic right side. On the arc chart \(z_j=tw_j\), divide by \(t^2\). Both positive exponents decrease by one. When one reaches zero, a unit-coefficient linear relation removes a generator, by Nakayama. Induction on the generator number, and these decreasing exponents between removals, reaches a maximal ideal generated by \(t,z_2\), hence a regular surface. An infinite nonsquare branch is impossible.

For \(q=T_3^2\), write its cubic correction \(H\). On the \(x_1\)-chart,
\[
v^2=x_1H(1,u,v)+x_1^2(\text{higher terms}).
\]
The exceptional divisor is a double line. Normality at its generic point forces \(h(T_1,T_2)=H(T_1,T_2,0)\ne0\), since otherwise the equation lies in \((x_1,v)^2\) at a height-one point. Singular points occur at its finitely many zeros on \(\mathbf P^1\). A simple zero gives a nonsquare next tangent form, with cross term between \(x_1\) and a parameter of that zero. Any continuing square point is a multiple zero of this cubic. There is at most one; it is rational since twice its residue degree cannot exceed three.

We separate double from triple zeros; this also spells out a higher-order case needed for the chart argument. If the restricted cubic has a double and a distinct simple zero, choose parameters so its binary part is \(a x_1x_2^2\), \(a\) a unit. There may also be cubic terms divisible by \(x_3\). On the \(x_2\)-chart the equation has the form
\[
v^2+x_2(a u+v P(u,v))+x_2^2(\text{higher terms})=0.
\]
At an exceptional point \(u\ne0\) its \(x_2\)-linear coefficient is a unit. At \(u=0\) the quadratic has nonzero cross term \(a x_2u\), so any singularity is nonsquare. The \(x_3\)-chart has no exceptional point. Thus a continuing square point lies in the \(x_1\)-chart. Its new tangent square may involve \(x_1\); the square hypothesis permits a change \(v\mapsto v+\lambda x_1\) making it the third coordinate, including in characteristic two. Its restricted cubic then has form \(x_1Q(x_1,x_2)\), with unit coefficient of \(x_2^2\). The direction \(x_1=0\) is simple, so the next continuing square point again lies in the \(x_1\)-chart. The rational multiple-zero direction can be recentered by translating \(x_2\) by a residue multiple of \(x_1\). This preserves \(x_1\) as exceptional parameter. Repeating gives the fixed-parameter arc, so the branch terminates.

If the binary cubic has a triple zero, choose it as \(x_2^3\) and its direction as \([1:0]\). On the \(x_1\)-chart the cubic contribution becomes \(x_1u^3\), of order four in the new parameters. If this point remains square, change its third coordinate by a multiple of \(x_1\) to remove the new tangent square. All other terms not involving that third coordinate are divisible by \(x_1^2\), because the original binary cubic was \(x_2^3\). Thus the new binary cubic is
\[
x_1^2(d u+e x_1).
\]
It is nonzero by normality of its next point blowup. If \(d\ne0\), its only multiple zero is \(x_1=0\); if \(d=0\), that direction is its triple zero. Blow up this direction on the \(u\)-chart, writing \(x_1=u s\) and the third coordinate \(u t\). The retained term \(x_1u^3\) contributes \(u^2s\), while \(d x_1^2u\) contributes \(d u s^2\). These are the entire new binary cubic:
\[
u s(u+d s).
\]
Indeed all remaining binary terms before this blowup are divisible by \(x_1^2\) and have order at least four; after substitution and division by \(u^2\) they have order at least four. Terms involving the third coordinate do not change the binary cubic or introduce a square-root translation here, since their transformed order is at least three and the new quadratic is \(t^2\). The coefficient of \(u^2s\) is a unit, so this cubic has at least two distinct zero directions. If any square point continues, it now belongs to the double-plus-simple case already treated. Consequently the triple-zero case takes at most two preliminary blowups before entering that case or becoming nonsquare.

Each square step has finitely many other branches, all nonsquare. The finite square branch produces finitely many of them, each terminating by the first case. This resolves the singularity. ∎

## 6. Completion and global resolution

<a id="complete-local-resolution"></a>

**Theorem 6.1.** A complete normal local surface domain in equal characteristic has a regular modification, including one made by normalized point blowups.

**Proof.** Choose a finite complete regular subring \(A_0\subset A\), and induct on \(n=[K:K_0]\). Degree one gives \(A=A_0\) by normality of \(A_0\). For \(K_0\subsetneq L\subsetneq K\), let \(B\) be the finite normalization in \(L\). It is complete local: a finite algebra over a complete local ring decomposes into local factors, and this domain has only one. Induction resolves \(B\) by regular \(Y\). Lemma 1.3 gives a normal modification \(X\) of \(A\), finite over \(Y\) of degree \(d=[K:L]<n\). Its singular set is finite and closed. The completed local factors there have degree at most \(d\) over complete regular surface rings, by Lemma 1.3, so induction resolves them.

Two facts permit descent. First, a regular resolution \(V\to T\) gives a normalized point resolution without assuming that fact: Theorem 2.1 gives a normalized point sequence \(T'\to T\) mapping to \(V\). Its local surface rings are birational extensions of regular local rings on \(V\), hence rational by Lemma 3.5. Lemma 4.1 and Theorem 5.1 resolve their finitely many singular points by further point blowups.

Second, point sequences over the completion of an excellent local ring descend. Closed fibres agree, so each center is an actual closed point of the algebraic surface. Blowup commutes with flat completion. Finite normalization commutes with this regular base change: the base-changed normal source is normal, finite and birational, hence is the normalization of the base-changed blowup. Repeat for each center; regularity descends faithfully flat. To assemble local point sequences globally, blow up their actual closed fibre points one at a time and normalize. Each operation is the identity off its chosen point. This resolves \(X\), hence \(A\).

If there is no proper intermediate field, \(K/K_0\) is separable or purely inseparable of degree \(p\): use its maximal separable subextension, and the degree-\(p\) first subextension in a nontrivial purely inseparable extension. Lemma 3.6 or 3.7 bounds cohomology, starting with rational regular \(A_0\). Lemma 3.5 reduces to rational local rings, Lemma 4.1 makes them Gorenstein, and Theorem 5.1 resolves them. Their finite local point sequences glue as above. The resolution-to-point-sequence argument proves the second assertion. ∎

<a id="excellent-surface-resolution"></a>

**Corollary 6.2.** Normalization and finitely many normalized point blowups resolve an excellent equal-characteristic surface. Their composite is projective and unchanged in codimension at most one of the normalization.

**Proof.** Normalization is finite. Its singular locus is closed with no point of codimension at most one, hence consists of finitely many closed points. Their completions are normal. Apply Theorem 6.1, descend and assemble their point sequences as in its proof. Blowups are projective and normalizations finite, so the composite is projective. Centers are closed surface points and leave codimension at most one unchanged. ∎

This is the needed excellent equal-characteristic implication of [Stacks, 0BGP](https://stacks.math.columbia.edu/tag/0BGP), with corrected main components and completed-degree bounds. Arbitrary nonexcellent rings are outside the assertion.


## 7. Exceptional curves and projective contraction

An exceptional curve of the first kind is a Cartier divisor \(E\simeq\mathbf P^1_k\) on a surface regular near \(E\), with normal bundle \(\mathcal O_{\mathbf P^1}(-1)\). Its constant field is \(k=H^0(E,\mathcal O_E)\).

<a id="exceptional-thickenings"></a>

**Lemma 7.1.** For \(E_n=nE\), the ring \(\Lambda=\varprojlim H^0(E_n,\mathcal O_{E_n})\) is complete regular local of dimension two. Its maximal ideal \(\mathfrak n\) satisfies \(\Lambda/\mathfrak n^n=H^0(E_n,\mathcal O_{E_n})\).

**Proof.** The successive ideal quotients are \(\mathcal O_E(j)\), with zero \(H^1\) for \(j\ge0\). Restriction on sections is therefore onto and the associated graded ring is
\[
\bigoplus_{j\ge0}H^0(\mathbf P^1_k,\mathcal O(j))=k[X,Y].
\]
Lift its degree-one basis to \(x,y\in\Lambda\). From any element in filtration degree \(j\), subtract its degree-\(j\) polynomial in \(x,y\), then repeat in higher degrees. Completeness expresses it as a convergent sum of multiples of degree-\(j\) monomials. Thus the filtration ideal is \((x,y)^j\), proving the quotients. The ring is local with residue \(k\) and Noetherian since its associated graded is Noetherian. The Hilbert function \(j+1\) gives dimension two; its two-generated maximal ideal proves regularity. ∎

<a id="projective-contraction"></a>

**Theorem 7.2.** On a regular surface \(X\) projective over affine Noetherian \(S\), an exceptional curve of the first kind has a contraction \(b:X\to X'\), with \(X'\) regular and projective over \(S\). The map is the blowup of a regular closed point. Compare [Stacks, 0C2L](https://stacks.math.columbia.edu/tag/0C2L) and [0C2M](https://stacks.math.columbia.edu/tag/0C2M).

**Proof.** Choose an ample power \(L\) with \(H^1(X,L)=0\) and sections \(t_0,\ldots,t_r\) embedding \(X\to\mathbf P^r_S\). Put \(d=\deg_kL|_E>0\) and \(M=L(dE)\). Its restriction to \(E\) is trivial. For \(1\le j\le d+1\), in
\[
0\to L((j-1)E)\to L(jE)\to\mathcal O_E(d-j)\to0
\]
the last \(H^1\) vanishes. Hence \(H^1(X,L((d-1)E))=0\), and \(1\) on \(E\) lifts to \(s\in H^0(X,M)\). The images of the \(t_i\), together with \(s\), generate \(M\) and define \(\varphi:X\to\mathbf P^{r+1}_S\). On \(E\) the first \(r+1\) coordinates vanish; off \(E\), projecting onto them recovers the original embedding, so \(\varphi\) is quasi-finite there. It is proper: its closed graph is followed by a projection obtained by base change from proper \(X\to S\).

Take its Stein factorization \(X\xrightarrow bX'\to\mathbf P^{r+1}_S\). The second map is finite, so \(X'\) is projective with ample pullback of \(\mathcal O(1)\). The first has geometrically connected fibres and \(b_*\mathcal O_X=\mathcal O_{X'}\). Its only positive-dimensional fibre is \(E\). No other point can join this fibre: the first coordinates distinguish the complement, and the remaining fibres are finite. Proper quasi-finiteness and the pushforward equality consequently make \(b\) an isomorphism off \(p=b(E)\).

Formal functions identifies \(\widehat{\mathcal O}_{X',p}\) with the inverse limit of sections on thickenings of the fibre. Its ideal and \(I_E\) have the same radical: \(\mathfrak m_p\mathcal O_X\subset I_E\), and \(I_E^c\subset\mathfrak m_p\mathcal O_X\) for some \(c\). Their powers are cofinal, so the inverse limit is \(\Lambda\) of Lemma 7.1. Thus \(p\) is regular of dimension two, since completion preserves dimension and embedding dimension; elsewhere \(X'\) is regular.

The map \(\mathfrak m_p/\mathfrak m_p^2\to H^0(E,I_E/I_E^2)\) is the complete degree-one space from Lemma 7.1. These sections generate \(\mathcal O_E(1)\); Nakayama gives \(\mathfrak m_p\mathcal O_X=I_E\) near \(E\), so the scheme fibre is exactly \(E\). This invertible ideal factors \(b\) through \(B=\operatorname{Bl}_pX'\). On the exceptional divisors the induced map pulls back \(\mathcal O(1)\) to \(\mathcal O_E(1)\), so it is nonconstant and finite. Thus \(X\to B\) is proper birational and quasi-finite, hence finite. The regularity calculation of Theorem 2.1 makes \(B\) normal, and finite birationality then makes \(X\to B\) an isomorphism. ∎

Here the restriction degree \(d\) is independent of the embedding dimension \(r\); the target is \(\mathbf P^{r+1}\). This resolves the comparison source's ambiguous use of one symbol for both numbers.

## 8. The trait model used for stable families

<a id="trait-model"></a>

**Theorem 8.1.** Over an excellent equal-characteristic DVR \(R\) with fraction field \(K\), a smooth proper geometrically connected curve \(C/K\) has a regular projective flat model. Finitely many projective contractions give such a model without exceptional curves of the first kind. Every operation preserves the marked generic curve and function field.

**Proof.** The generic curve is projective. Embed it in \(\mathbf P^m_K\), and take its schematic closure \(Y\subset\mathbf P^m_R\). This is integral, with no \(R\)-torsion, hence flat over the DVR. Its finite normalization is projective and unchanged on the smooth normal generic curve. Its singular set is finite and its singular completed local rings normal. Corollary 6.2 resolves it by projective normalized point blowups. Centers lie above special-fibre points; the generic curve has only points of codimension at most one and is unchanged. The resulting integral regular projective surface is flat by absence of \(R\)-torsion.

An exceptional curve \(E\simeq\mathbf P^1_k\) is vertical. Its map to affine \(\operatorname{Spec}R\) factors through its constants \(\operatorname{Spec}k\), and properness makes its one-point image closed. Theorem 7.2 contracts it to a regular projective surface with the same generic fibre, again flat by the torsion argument. This removes exactly one special-fibre component: every other component meets the isomorphism open and retains its distinct birational image. The finite component count decreases. Iteration terminates at the minimal regular projective model required by the stable-family proof; uniqueness is not needed here. ∎

This construction applies after the separately specified finite separable torsion-visibility extension and the complete excellent trait in S.3. Resolution and contraction introduce no further field extension. S.7 determines the alteration's final separable field independently.

## 9. Dependency closure and references

The surface input proceeds through the normalized main components (Lemmas 1.1 and 1.3), domination (Theorem 2.1), local vanishing and boundedness (Lemmas 3.1–3.7), the rational-to-Gorenstein step (Lemma 4.1), double points and arc termination (Theorem 5.1), completion and global sequences (Theorem 6.1 and Corollary 6.2), and projective contraction (Lemma 7.1 and Theorem 7.2). Theorem 8.1 applies exactly this chain to the trait.

For comparison the human Stacks Project locators are [0BBT](https://stacks.math.columbia.edu/tag/0BBT), [0AXJ](https://stacks.math.columbia.edu/tag/0AXJ), [0AXL](https://stacks.math.columbia.edu/tag/0AXL), [0B4U](https://stacks.math.columbia.edu/tag/0B4U), [0BBV](https://stacks.math.columbia.edu/tag/0BBV), [0BGE](https://stacks.math.columbia.edu/tag/0BGE), [0BGN](https://stacks.math.columbia.edu/tag/0BGN), [0BGP](https://stacks.math.columbia.edu/tag/0BGP), [0C2L](https://stacks.math.columbia.edu/tag/0C2L) and [0C2M](https://stacks.math.columbia.edu/tag/0C2M). The proofs above do not require bundled chapters, patches or corrected TeX.
