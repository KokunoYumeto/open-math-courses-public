# Harris–Taylor: geometry, numerical counting and existence

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The cohomology of a tower can attach a Weil representation to a supercuspidal representation without yet proving a correspondence. Three questions remain: is that Weil representation irreducible, do its local factors agree with the automorphic ones, and does every supercuspidal occur in the part of the construction where these assertions have been established? Harris and Taylor connect the tower to global Shimura varieties. Automorphic induction supplies parameters in the image; Henniart's numerical theorem then supplies the exhaustion.

This lesson states those substantial inputs and proves the two counting deductions that finish the argument. The theorems of Harris and Taylor are stated as in [Carayol 2000] and [Wedhorn 2000]; [Scholze 2013] gives another proof of the local correspondence.

## 1. The existence theorem and its normalization

Let \(F/\mathbb Q_p\) be finite. Reciprocity \(\operatorname{Art}_F\) sends a uniformizer to geometric Frobenius \(\Phi\), and \(\|\Phi\|=q^{-1}\). A Frobenius-semisimple Weil–Deligne parameter \((r,N)\) satisfies
\[
r(w)Nr(w)^{-1}=\|w\|N.
\tag{1.1}
\]
Write \(\mathcal A_n(F)\) for irreducible admissible representations of \(\mathrm{GL}_n(F)\), \(\mathcal C_n(F)\) for its supercuspidal subset, \(\mathcal W_n(F)\) for irreducible \(n\)-dimensional complex Weil representations with open inertia kernel, and \(\mathcal D_n(F)\) for all \(n\)-dimensional parameters in (1.1).

**Theorem 1.1 (Harris–Taylor, stated).** For every finite extension \(F/\mathbb Q_p\) there are bijections, simultaneously in all ranks,
\[
\operatorname{rec}_F:\mathcal A_n(F)\longrightarrow\mathcal D_n(F).
\tag{1.2}
\]
They satisfy the following five properties.

1. In rank one, \(\operatorname{rec}_F(\chi)=\widehat\chi=\chi\circ\operatorname{Art}_F^{-1}\).
2. For any ranks \(n,m\), any \(\pi,\pi'\) of those ranks, and any nontrivial additive character \(\psi\),
\[
\begin{aligned}
L(s,\pi\times\pi')&=L(s,\operatorname{rec}_F(\pi)\otimes\operatorname{rec}_F(\pi')),\\
\varepsilon(s,\pi\times\pi',\psi)&=
\varepsilon(s,\operatorname{rec}_F(\pi)\otimes\operatorname{rec}_F(\pi'),\psi).
\end{aligned}
\tag{1.3}
\]
3. Twisting by \(\chi\circ\det\) tensors the parameter by \(\widehat\chi\).
4. If \(\omega_\pi\) is the central character, then \(\det\operatorname{rec}_F(\pi)=\widehat{\omega_\pi}\).
5. Taking the contragredient takes the dual parameter.

The map restricts to a bijection \(\mathcal C_n(F)\to\mathcal W_n(F)\), with \(N=0\). This is the main theorem of Harris and Taylor; see [Carayol 2000, §§2.1–2.4] and [Wedhorn 2000, (1.2.2) and (4.2.2)], and [Scholze 2013, Theorem 1.2] for another proof. The factor convention and the reduction from supercuspidals are those established in the correspondence-statement and monodromy-block lessons. This theorem concerns all representations in (1.2), including nongeneric Langlands quotients.

For the construction, choose \(\ell\ne p\) and a coefficient identification \(\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C\) taking the chosen square root of the norm to its positive real value. Set \(\nu=|\det|_F\). The earlier Jacquet–Langlands lesson specified the virtual vanishing-cycle representation \(\Psi(\rho)\) for a division-algebra representation \(\rho\). The construction theorem of Harris and Taylor [Carayol 2000, §5.6, Théorème 2; Wedhorn 2000, (4.4.1)] produces a true \(n\)-dimensional Weil representation \(r_\ell(\pi)\) satisfying
\[
[\Psi(\operatorname{JL}^{-1}(\pi)^\vee)]
=[\pi\otimes r_\ell(\pi)]
\tag{1.4}
\]
for supercuspidal \(\pi\). The definition of the factor-normalized assignment is
\[
\operatorname{rec}_{F,\ell}(\pi)
=r_\ell\bigl(\pi^\vee\otimes\nu^{(1-n)/2}\bigr).
\tag{1.5}
\]
Formula (1.4) is a virtual identity. It does not assert, on its own, concentration in a single cohomological degree. At this stage (1.5) takes values in semisimple Weil representations; its irreducibility and bijectivity are conclusions of the subsequent argument.

## 2. The global statement that identifies local information

The companion compatibility result has hypotheses which matter.

**Theorem 2.1 (Harris–Taylor, stated).** Let \(L\) be a CM field, with complex conjugation \(c\), and let \(\Pi\) be a cuspidal automorphic representation of \(\mathrm{GL}_n(\mathbb A_L)\). Assume
\[
\Pi^\vee\simeq\Pi^c,
\tag{2.1}
\]
that \(\Pi_\infty\) has the infinitesimal character of an algebraic representation of \(\operatorname{Res}_{L/\mathbb Q}\mathrm{GL}_n\), and that \(\Pi_x\) is square-integrable at some finite place \(x\). There are a nonzero integer \(a(\Pi)\) and a continuous \(\ell\)-adic Galois representation \(R_\ell(\Pi)\) such that for every finite \(y\nmid\ell\),
\[
[R_\ell(\Pi)|_{W_{L_y}}]
=a(\Pi)[r_\ell(\Pi_y)].
\tag{2.2}
\]
The brackets denote semisimple classes. This is the global compatibility theorem of Harris and Taylor as recalled in [Taylor–Yoshida 2007, Introduction]; [Carayol 2000, §7, Théorème 3] states its form for the cohomology of the Shimura varieties. Here \(r_\ell\) on general representations is extended from their supercuspidal support with norm shifts; see [Carayol 2000, §7.3].

In particular (2.2) supplies bad-place Weil information as well as good-place information. It does **not** identify the monodromy operators on the two sides. [Taylor–Yoshida 2007, Introduction] states this limitation explicitly. The full Weil–Deligne compatibility for modular forms stated in the preceding lesson has its own Carayol authority; it must not be attributed to (2.2).

The point of globalizing a prescribed local supercuspidal is that good-place information, global Galois representations and global functional equations become available. The local component can be prescribed up to an unramified twist. Harris and Taylor proved this globalization, and [Scholze 2013, Theorem 10.7] states it as follows. Every finite extension \(F/\mathbb Q_p\) is the completion \(L_w\) of a suitable CM field \(L\) at a finite place \(w\) [Scholze 2013, §8 and Remark 10.4]. For every essentially square-integrable representation \(\pi\) of \(\mathrm{GL}_n(F)\), in particular for every supercuspidal one, there is a cuspidal automorphic representation \(\Pi\) of \(\mathrm{GL}_n(\mathbb A_L)\) with \(\Pi^\vee\simeq\Pi^c\), with \(\Pi_\infty\) having the infinitesimal character of an algebraic representation of \(\operatorname{Res}_{L/\mathbb Q}\mathrm{GL}_n\), and with \(\Pi_x\) supercuspidal at a finite place \(x\ne w\), such that \(\Pi_w\) is an unramified twist of \(\pi\). Such a \(\Pi\) satisfies the hypotheses of Theorem 2.1. Theorem 2.1 then returns the resulting comparison to the prescribed place, and the local twist formulas remove the auxiliary twist.

## 3. How the Shimura variety and the tower meet

Here is the architecture, with the geometry treated as stated input. Write \(L=L^+E\), where \(L^+\) is totally real and \(E\) is imaginary quadratic with \(p=uu^c\) split in \(E\). Choose a central division algebra \(B/L\) with an involution inducing \(c\) on its center and satisfying the splitting and parity conditions in [Carayol 2000, §§6.1–6.2]. For the associated unitary similitude group \(G\), let \(\mu:G(\mathbb R)\to\mathbb R^\times\) be the common similitude multiplier. Its kernel is
\[
\ker\mu=U(n-1,1)\times U(n)^{[L^+:\mathbb Q]-1}.
\tag{3.1}
\]
The derived real subgroup is instead
\[
G^{\mathrm{der}}(\mathbb R)
=SU(n-1,1)\times SU(n)^{[L^+:\mathbb Q]-1}.
\tag{3.1a}
\]
Here is the algebraic distinction. In every unitary factor, \(\operatorname{diag}(z,1,\ldots,1)\) with \(|z|=1\) realizes determinant \(z\). Thus (3.1) retains the determinant circles. Complexifying the common-multiplier equations gives \(G_{\mathbb C}\simeq\mathbb G_m\times\prod_{j=1}^{[L^+:\mathbb Q]}\mathrm{GL}_n\): the conjugate matrix in each pair is determined by the multiplier and the inverse transpose. Every commutator has determinant one, while elementary transvections, which generate \(\mathrm{SL}_n(\mathbb C)\), are commutators with diagonal matrices having unequal diagonal entries. Hence the derived complex subgroup is \(\prod_j\mathrm{SL}_n\). Its real determinant-one equations give (3.1a); for \(n=1\) these factors are trivial.

Only the signature-\((n-1,1)\) factor contributes a symmetric domain of positive dimension when \(n>1\). Passing from \(U(n-1,1)\) to \(SU(n-1,1)\) preserves that domain, since the determinant map on the maximal compact subgroup \(U(n-1)\times U(1)\) is onto \(U(1)\). The real dimension is \(n^2-((n-1)^2+1)=2(n-1)\), so the complex dimension remains \(n-1\). The resulting simple Shimura varieties have this dimension. Their moduli describe abelian varieties with polarization, a \(B\)-action and level structure. With sufficiently small level they are smooth and proper over the reflex field.

At a chosen split finite place \(w\), where \(B_w\simeq M_n(L_w)\), the local group contains \(\mathrm{GL}_n(L_w)\). The corresponding factor of the universal \(p\)-divisible group is, after applying a matrix idempotent, a one-dimensional Barsotti–Tate \(\mathcal O_{L_w}\)-module of height \(n\). Barsotti–Tate here means a compatible system of finite flat \(p\)-power torsion group schemes.

On the special fiber, stratify by the height \(h\) of its maximal étale quotient:
\[
0\le h\le n-1,\qquad
\text{connected height}=n-h,\qquad
\dim X^{(h)}=h.
\tag{3.2}
\]
The closure of a stratum contains the strata of smaller height. The basic stratum \(h=0\) has the full connected height \(n\). Its deformation theory is the height-\(n\) Lubin–Tate theory used in (1.4).

Two kinds of Igusa varieties separate two pieces of information. The first trivializes the finite-level étale quotient. The second trivializes connected torsion with a local lifting condition to higher levels. That condition is necessary: an automorphism of a truncated group scheme need not lift to the entire formal module. In the inverse limit, the second covering has group \(\mathcal O_{D_{n-h}}^\times\), where \(D_{n-h}\) has invariant \(1/(n-h)\). After this covering the local vanishing-cycle factor becomes the constant factor supplied by the corresponding Lubin–Tate deformation space.

Thus a stratum calculation separates an Igusa cohomology factor from a local vanishing-cycle factor. Restoring all linear-group translates involves induction from the parabolic with Levi
\[
\mathrm{GL}_{n-h}(L_w)\times\mathrm{GL}_h(L_w).
\tag{3.3}
\]
For a supercuspidal contribution the proper-parabolic Jacquet modules vanish. This is why the basic stratum isolates the desired height-\(n\) factor. The precise identity, including multiplicities, shifts and Jacquet functors, is [Carayol 2000, §7.3, Théorème 4], with the outline of its proof in [Carayol 2000, §8]; the preceding description is its architecture, not a replacement formula.

The Igusa factor is evaluated by counting fixed points of Hecke correspondences composed with sufficiently large powers of Frobenius. The Lefschetz trace formula turns these fixed points into traces; the classification of the abelian varieties and their extra structures turns the sums into orbital integrals. A trace-formula comparison then identifies them with the automorphic traces occurring in the generic-fiber cohomology. This comparison yields (1.4) and Theorem 2.1. The Frobenius power is part of the fixed-point argument's hypothesis, not an arbitrary Hecke operator.

Another global bridge is base change from the unitary similitude group to the general linear group over the CM field. Harris and Taylor use the stable base change theorem of Clozel and Labesse, which [Harris 2005, (1.2.6)] states for the groups \(G\) above. A cuspidal automorphic representation \(\pi\) of \(G\) that is cohomological for one of the algebraic representations \(\xi\) considered there has a base change \((\Pi,\psi)\), where \(\Pi\) is an automorphic representation of \(\mathrm{GL}_n(\mathbb A_L)\) and \(\psi\) is a Hecke character of \(E\), with local matching at all unramified places and at all places split in \(E\), in particular at almost all inert places. Conversely, let \(\Pi\) be cuspidal with \(\Pi^\vee\simeq\Pi^c\), with \(\Pi_\infty\) the cohomological representation attached to \(\xi\), and with \(\Pi_v\) in the discrete series at every place \(v\) over which \(B\) ramifies, and let \(\psi\) satisfy the central-character conditions of [Harris 2005, (1.2.6)]. Then \((\Pi,\psi)\) is the base change of an automorphic representation \(\pi\) of \(G\), and \(\pi_f\) occurs in the cohomology of the Shimura variety of \(G\) with coefficients in the local system attached to \(\xi\); in particular this cohomology is nonzero. The trace identity behind the theorem is [Clozel–Labesse 1999, Théorème A.3.1]; the remark following that theorem corrects the constant in the earlier form of the identity and notes the gap in its earlier proof. One should use this precise statement rather than assume that restriction along the auxiliary torus covering preserves automorphy of every summand.

The representation-theoretic bookkeeping consists of normalized induction and normalized Jacquet modules, with their exactness and adjunction [Bernstein–Zelevinsky 1977, §§1.8–1.9 and 2.3], the Grothendieck groups of representations of finite length with the maps these functors induce on them [Zelevinsky 1980, §1.7], and the Grothendieck group of \(G(\mathbb A_f)\times W_{L_w}\)-modules that are admissible for \(G(\mathbb A_f)\) and continuous for the Weil group, with the Weil action recorded up to semisimplification [Harris 2005, §4.2]. The alternating sums in this argument belong to those groups. Replacing them by individual cohomology groups would change the theorem.

## 4. What finite counting proves

For a fixed smooth central character \(\omega:F^\times\to\mathbb C^\times\) and integer \(c\ge0\), define
\[
\begin{aligned}
\mathcal C_n(\omega,\le c)&=
\{\pi\in\mathcal C_n(F):\omega_\pi=\omega,\ a(\pi)\le c\},\\
\mathcal W_n(\omega,\le c)&=
\{r\in\mathcal W_n(F):\det r=\widehat\omega,\ a(r)\le c\}.
\end{aligned}
\tag{4.1}
\]
The conductor exponents use a conductor-zero additive character. Fixing \(\omega\) removes the continuous unramified twisting freedom.

These are finite sets. The relevant finiteness inputs are [Henniart 1988, Proposition 2.3 and §§2.5–2.6]. On the automorphic side there is also a useful explanation using the previous lesson. The division-algebra conductor formula in [Henniart, §2.5] bounds the required unit level, and Jacquet–Langlands preserves conductors. At a bounded level and fixed central character, a representation of \(D^\times\) factors through a finite-dimensional algebra: take the finite quotient by that level and central powers of a uniformizer, imposing the prescribed scalar action of those powers. The algebra has a finite basis of coset representatives and hence finitely many simple modules.

**Proposition 4.1 (finite-fiber counting).** Suppose a map \(f:\mathcal C_n(F)\to\mathcal W_n(F)\) preserves central characters as determinants and conductors. Suppose that its restriction to \(\mathcal C_n(\omega,\le c)\) is injective and that
\[
\#\mathcal C_n(\omega,\le c)=\#\mathcal W_n(\omega,\le c)<\infty.
\tag{4.2}
\]
Then its restriction is onto \(\mathcal W_n(\omega,\le c)\). If these hypotheses hold for every \(\omega,c\), then \(f\) is a bijection.

**Proof.** Preservation puts the restriction's image inside the target in (4.1). Injectivity makes its image have cardinality \(\#\mathcal C_n(\omega,\le c)\). By (4.2), the complement in the finite target has cardinality zero, so the image is the whole target.

For a general \(r\), let \(\omega=\det r\circ\operatorname{Art}_F\) and \(c=a(r)\). The preceding conclusion supplies its preimage. If \(f(\pi)=f(\pi')\), preservation gives the same central character and conductor to both; put them in the same bounded fiber and apply its injectivity. Thus \(f\) is both onto and one-to-one. ∎

The equality (4.2) is an explicit hypothesis of this elementary deduction. Henniart's original numerical theorem has a different formulation; it is not a statement that an arbitrary preliminary bijection preserves every prescribed central character.

**Theorem 4.2 (Henniart's numerical theorem, stated in the direction needed).** For a nonarchimedean local field \(F\), an injection
\[
b:\mathcal W_n(F)\longrightarrow\mathcal C_n(F)
\tag{4.3}
\]
which preserves conductors and commutes with all unramified twists is a bijection. Such injections exist. This is [Henniart 1988, Theorem 1.2]. The finite numerical counts underlying it are modulo unramified twisting; Theorem 1.3 and §2 specify them. The central-character equality is stronger data subsequently obtained from the actual correspondence.

A count on infinite sets would prove nothing here: an injection of a proper infinite subset can be onto another set of the same cardinality. Theorem 4.2 contains the conductor filtration and unramified twisting requirements which make the numerical argument effective.

## 5. Exhaustion of the base-change subset

Let \(\mathcal C'_n(F)\subset\mathcal C_n(F)\) consist of the supercuspidals which become unramified after a finite succession of cyclic local base changes. Subsequent base changes need not stay supercuspidal; the final unramified representation is a spherical representation of the same general linear group over the last field.

The following is the substantive construction input, not an elementary consequence of ramification theory:
\[
\operatorname{rec}'_F:\mathcal C'_n(F)\xrightarrow{\sim}\mathcal W_n(F),
\tag{5.1}
\]
with the desired local factors, determinants, duals and twists. The subset is stable under unramified twists, and (5.1) preserves conductors and commutes with them. [Carayol 2000, §2.3] states this strategy. Its realization uses non-Galois automorphic induction, Brauer induction and factor comparison; see [Carayol 2000, §§3.5 and 7.3].

Non-Galois induction matters because not every irreducible Weil representation is induced from a character of a single subfield. Brauer's theorem supplies an integral virtual combination of induced characters. The global construction realizes those combinations on the automorphic side. The factor comparison then shows that the relevant virtual combination is a single supercuspidal, rather than leaving an arbitrary virtual difference. In the construction of Harris and Taylor this follows from the factor comparison; a closely related argument with the same positivity conclusion, for Henniart's construction, is in [Carayol 2000, §§4.5–4.6]. We state it, including the positivity conclusion, as part of the construction input.

**Proposition 5.1 (exhaustion).** Given (5.1) with conductor and unramified-twist compatibility, Theorem 4.2 implies
\[
\mathcal C'_n(F)=\mathcal C_n(F).
\tag{5.2}
\]
Consequently the cohomological map is a bijection onto irreducible Weil parameters on all supercuspidals.

**Proof.** Invert (5.1), and compose its inverse with the inclusion of the subset:
\[
\mathcal W_n(F)\xrightarrow{(\operatorname{rec}'_F)^{-1}}
\mathcal C'_n(F)\hookrightarrow\mathcal C_n(F).
\tag{5.3}
\]
This is an injection. Its conductor equality follows from that of (5.1). For an unramified \(\chi\), if \(\operatorname{rec}'_F(\pi)=r\), its twist property gives \(\operatorname{rec}'_F(\pi\otimes\chi\circ\det)=r\otimes\widehat\chi\). Stability of the subset and uniqueness of the inverse prove the twist property for (5.3). Theorem 4.2 makes (5.3) onto. Its image is exactly \(\mathcal C'_n(F)\), so (5.2) follows. The cohomological map agrees with (5.1) there by the construction input, hence now agrees on the whole domain. ∎

There is a parallel deduction using the finite-fiber hypothesis (4.2), if that stronger counting input is given. The inverse of (5.1) maps \(\mathcal W_n(\omega,\le c)\) injectively into \(\mathcal C'_n(F)\cap\mathcal C_n(\omega,\le c)\). Equal finite cardinalities with \(\mathcal C_n(\omega,\le c)\) force that intersection to be the entire fiber. Every supercuspidal lies in some fiber, giving (5.2). This proves the requested finite-count version without substituting it for the actual statement of Henniart's theorem.

After exhaustion, the monodromy-block lesson extends the supercuspidal bijections to all of (1.2): a centered segment of length \(k\) corresponds to \(r\otimes S_k\), and a Langlands quotient corresponds to the direct sum of its segment parameters. The five properties persist after this extension [Carayol 2000, §2.4; Wedhorn 2000, (4.2.2)].

## 6. Height two and independence of the auxiliary prime

For \(n=2\), a supercuspidal \(\pi\) has a two-dimensional irreducible parameter \(r\), and its division-algebra type \(\rho=\operatorname{JL}^{-1}(\pi)\) satisfies, in the course's normalization,
\[
[\Psi(\rho)]=[\pi^\vee\otimes r\otimes\|\cdot\|^{-1/2}].
\tag{6.1}
\]
For a dihedral example \(r=\operatorname{Ind}_{W_E}^{W_F}\theta\), restricting the Weil factor to \(W_E\) gives
\[
(\theta\oplus\theta^\sigma)\otimes\|\cdot\|^{-1/2}|_{W_E}.
\tag{6.2}
\]
Thus extracting the local Weil factor and tensoring back by \(\|\cdot\|^{1/2}\) recovers precisely \(r\), not a parameter shifted by a half norm. The same argument retains an irreducible primitive parameter when there is no inducing quadratic character. Compatibility with Kutzko's correspondence follows from the uniqueness theorem: both rank-two correspondences satisfy the factor characterization. This is a compatibility statement, not a new construction of the primitive representations.

Deligne's 1973 letter, part B, supplies the height-two origin of this approach: vanishing cycles at supersingular points have the commuting Weil, linear-group and quaternionic actions. Harris and Taylor place the same local mechanism inside higher-dimensional unitary Shimura varieties.

For two auxiliary primes or coefficient identifications, transport both constructions to complex coefficients using the prescribed positive square root of the norm. The factor comparison of [Carayol 2000, §7.3] supplies identical pair factors for both systems; rank one has the same reciprocity normalization. Henniart's uniqueness theorem, as stated in the correspondence-statement lesson, therefore identifies the two systems. The segment extension identifies their monodromy blocks as well. This is the uniqueness of [Carayol 2000, §2.3.1] applied to the two systems. Uniqueness is applied after the required factors have been established; it cannot turn a preliminary semisimple map lacking them into a correspondence.

## 7. Exercises and complete solutions

**Exercise 7.1 (easy).** Prove the finite-set counting deduction with fixed central character and conductor bound.

**Solution.** Let the two fibers be \(S,T\). Preservation defines \(f:S\to T\), and injectivity gives \(\#f(S)=\#S\). Since \(\#S=\#T<\infty\), one has \(\#(T\setminus f(S))=0\), so \(f(S)=T\). Applying this at \(\omega=\det r\circ\operatorname{Art}_F\), \(c=a(r)\), supplies a preimage of every parameter. Two preimages of the same parameter lie in that same fiber and are equal. The equality of finite cardinalities is needed; equality of cardinalities of unrestricted infinite sets would not suffice.

**Exercise 7.2 (medium).** Explain the supercuspidal domain of the construction and its extension to arbitrary irreducibles.

**Solution.** The construction theorem (1.4) extracts \(r_\ell(\pi)\) when \(\pi\) is supercuspidal. The vanishing of proper-parabolic Jacquet modules isolates its basic-stratum contribution. The theorem neither supplies \(N\) for every nonsupercuspidal nor classifies their parameters directly. After the supercuspidal bijection is established, the representation classification writes an arbitrary irreducible as the Langlands quotient of ordered essentially square-integrable segment representations. Replace a segment of length \(k\) built on \(\sigma\) by \(\operatorname{rec}_F(\sigma)\otimes S_k\), keeping its central norm shift, and take the direct sum. The uniqueness of the segment data and the graded Jordan-block classification make this a bijection. In particular a Steinberg segment acquires nonzero \(N\); a determinant character acquires the appropriate sum of one-dimensional blocks, with \(N=0\). The previous reduction lesson proves the block classification and explains the factor compatibility inputs.

**Exercise 7.3 (medium).** Identify the local and global roles in properties (1)–(5).

**Solution.** Property (1) comes from local Lubin–Tate/class-field theory at height one. Properties (3), (4) and (5) first appear for the cohomological Weil assignment through globalizing the local representation, comparing global twists, determinants and duals at good places, and using density to identify the global Galois representations; Theorem 2.1 then returns the comparison to the bad place; see [Carayol 2000, §7.2], with the dual and norm conversion in (1.5). Property (2) on supercuspidals uses global compatibility and automorphic induction to compare factors for induced characters, then Brauer induction and local factor properties to extract genuine supercuspidals; see [Carayol 2000, §7.3]. Local numerical counting supplies exhaustion. Finally the local classification, monodromy blocks, dual formulas and multiplicativity extend the properties to arbitrary irreducibles [Carayol 2000, §2.4]. Thus the proof uses local and global steps together; assigning every property exclusively to one side would misdescribe it.

**Exercise 7.4 (hard).** Why does Henniart's uniqueness imply independence of \(\ell\), and what normalization must be held fixed?

**Solution.** Choose \(\ell,\ell'\ne p\) and coefficient identifications with complex numbers which send the selected half norm to the positive real half norm. Construct the supercuspidal maps and complete the exhaustion for both. Their rank-one maps are \(\chi\circ\operatorname{Art}_F^{-1}\). By the factor comparison of [Carayol 2000, §7.3] they preserve the same complex \(L\)- and epsilon factors of every pair, for the same additive character and reciprocity convention. Extend each system by the same segment classification. Both now meet the full uniqueness characterization, so their values agree on every irreducible representation. In particular the induced nilpotent block structures agree, not just the underlying Weil semisimplifications. One cannot compare the raw \(r_\ell(\pi)\) directly to rec: its contragredient and half norm in (1.5) must first be applied. Changing the chosen image of a half norm without transporting the convention changes that formula.

## What this lesson does not prove

The existence and factor theorem, geometric construction, virtual cohomology and global compatibility are stated in [Carayol 2000, §§2, 5 and 7], [Wedhorn 2000, (1.2.2) and (4.4.1)] and [Taylor–Yoshida 2007, Introduction]; [Scholze 2013, Theorem 1.2] gives another proof of the existence and factor theorem. The unitary moduli and stratum identities are outlined in [Carayol 2000, §§6–8]. We stated this geometry rather than prove its deformation theory, point counts or trace formula. Its admissible Grothendieck-group formalism is in [Bernstein–Zelevinsky 1977, §§1–2], [Zelevinsky 1980, §1] and [Harris 2005, §4.2]. The cohomological unitary base change is the theorem of Clozel and Labesse stated in [Harris 2005, (1.2.6)], with its trace identity in [Clozel–Labesse 1999, Théorème A.3.1]; the globalization used above is due to Harris and Taylor and is stated in [Scholze 2013, Theorem 10.7].

The numerical theorem and bounded-count finiteness are [Henniart 1988, Theorems 1.2–1.3, Proposition 2.3 and §§2.5–2.8]. We proved Proposition 4.1 conditional on the explicit finite-fiber equality. We did not attribute preservation of arbitrary prescribed central characters to the preliminary numerical bijections.

The bijection on the base-change subset, with factor, twist and conductor compatibility, is the Harris–Taylor construction input outlined in [Carayol 2000, §§2.3, 3.5 and 7.3]. Its non-Galois automorphic induction and Brauer-to-genuine-representation step are stated. Given those inputs, Proposition 5.1 proves the exhaustion. We do not infer it merely from the solvability of local Galois groups.

The classification, block extension and Henniart uniqueness are earlier course inputs. Their application gives the extension and auxiliary-prime independence explained here. The height-two geometric origin is [Deligne 1973, letter, part B, pp. 3–4]. The compatibility example uses the exact virtual formula already established in the Jacquet–Langlands lesson.

## References

- [Harris 2005] Michael Harris, [“The local Langlands correspondence: notes of (half) a course at the IHP Spring 2000”](https://www.numdam.org/item/AST_2005__298__17_0/), in *Formes automorphes (I)*, *Astérisque* 298 (2005), 17–145, §4.2 and (1.2.6).
- [Clozel–Labesse 1999] Laurent Clozel and Jean-Pierre Labesse, [“Changement de base pour les représentations cohomologiques de certains groupes unitaires”](https://www.numdam.org/item/AST_1999__257__119_0/), Appendix A to Jean-Pierre Labesse, *Cohomologie, stabilisation et changement de base*, *Astérisque* 257 (1999), 119–133, Théorème A.3.1.
- [Bernstein–Zelevinsky 1977] I. N. Bernstein and A. V. Zelevinsky, [“Induced representations of reductive p-adic groups. I”](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BZ-induced-1.pdf), *Annales scientifiques de l'École Normale Supérieure* 10 (1977), 441–472, §§1–2.
- [Zelevinsky 1980] A. V. Zelevinsky, [“Induced representations of reductive p-adic groups. II. On irreducible representations of GL(n)”](https://www.numdam.org/item/ASENS_1980_4_13_2_165_0/), *Annales scientifiques de l'École Normale Supérieure* 13 (1980), 165–210, §1.
- [Henniart 1988] Guy Henniart, [“La conjecture de Langlands locale numérique pour GL(n)”](https://www.numdam.org/item/ASENS_1988_4_21_4_497_0/), *Annales scientifiques de l'École Normale Supérieure* 21 (1988), 497–544, Theorems 1.2–1.3 and §2.
- [Deligne 1973] Pierre Deligne, [letter to I. Piatetski-Shapiro](https://publications.ias.edu/sites/default/files/deligne73.pdf), 25 March 1973, part B, the local construction at supersingular points.
- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §12.4, especially Theorem 12.4.1.
- [Carayol 2000] Henri Carayol, [“Preuve de la conjecture de Langlands locale pour GL_n : travaux de Harris–Taylor et Henniart”](https://www.numdam.org/item/SB_1998-1999__41__191_0/), Séminaire Bourbaki, exposé 857 (1998–1999), *Astérisque* 266 (2000), 191–243, §§2–8.
- [Wedhorn 2000] Torsten Wedhorn, [*The local Langlands correspondence for GL(n) over p-adic fields*](https://arxiv.org/abs/math/0011210v2), lectures at the School on Automorphic Forms on GL(n), ICTP Trieste, 2000, (1.2.2), (4.2.2) and (4.4.1).
- [Taylor–Yoshida 2007] Richard Taylor and Teruyoshi Yoshida, [“Compatibility of local and global Langlands correspondences”](https://math.stanford.edu/~rltaylor/monod2.pdf), *Journal of the American Mathematical Society* 20 (2007), 467–493, Introduction.
- [Scholze 2013] Peter Scholze, [*The Local Langlands Correspondence for GL_n over p-adic fields*](https://arxiv.org/abs/1010.1540v1), *Inventiones mathematicae* 192 (2013), 663–715, Theorem 1.2, §8, Remark 10.4 and Theorem 10.7.
