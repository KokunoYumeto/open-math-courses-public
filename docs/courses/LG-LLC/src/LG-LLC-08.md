# Dihedral supercuspidals, rectifiers and rank-two characterization

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A character of a quadratic extension produces a two-dimensional Weil representation by induction. The Weil representation also produces a supercuspidal representation of the general linear group. Their epsilon factors have the same induction constant. This gives a concrete part of the correspondence, and character twists identify its representations uniquely. A second construction, using a finite-field cuspidal representation, labels the same objects with a different character; its unramified quadratic rectifier must be included.

We assume the quadratic-induction results of *Two-dimensional Weil representations: induction and projective symmetry*, the non-supercuspidal dictionary, the proved rank-two converse theorem, and the Weil-representation construction from *Supercuspidal representations of the two-dimensional general linear group*. The automorphic construction and its functional equation are stated inputs. We prove the induced parameter's epsilon formula, the determinant match, the independence of the inducing description and a precise characterization theorem. Basic references are [Jacquet–Langlands 1970], [Deligne 1973] and [Adrian–Roe 2013].

## 1. The construction and its character label

Let \(F\) be a nonarchimedean local field, and let \(E/F\) be a separable quadratic extension. Use geometric reciprocity on both fields. Let \(\eta_{E/F}\) be the quadratic character of \(F^\times\), and write \(\theta^\sigma(x)=\theta(\sigma x)\) for a smooth character \(\theta:E^\times\to\mathbb C^\times\).

**Theorem 1.1 (Weil construction, stated).** The Weil representation for the norm quadratic space \(E\), together with \(\theta\), gives a smooth irreducible representation \(\Pi_E(\theta)\) of \(\mathrm{GL}_2(F)\). If \(\theta\ne\theta^\sigma\), it is supercuspidal. It has
\[
\begin{aligned}
\omega_{\Pi_E(\theta)}&=\theta|_{F^\times}\eta_{E/F},\\
\Pi_E(\theta^\sigma)&\simeq\Pi_E(\theta),\\
\Pi_E(\theta)^\vee&\simeq\Pi_E(\theta^{-1}),\\
\Pi_E(\theta)\otimes(\xi\circ\det)
 &\simeq\Pi_E(\theta(\xi\circ N_{E/F})).
\end{aligned}
\tag{1.1}
\]
For \(\psi_E=\psi_F\circ\operatorname{Tr}_{E/F}\), its standard factors satisfy
\[
L_F(s,\Pi_E(\theta))=L_E(s,\theta),\qquad
\epsilon_F(s,\Pi_E(\theta),\psi_F)
=\lambda(E/F,\psi_F)\epsilon_E(s,\theta,\psi_E).
\tag{1.2}
\]
Use the same self-dual additive measures in the two factor theories.

The exact construction and irreducibility locators are [Jacquet–Langlands 1970, §1 and Theorem 4.6]; (1.1) and (1.2) are Theorem 4.7. The induced representation of their index-two norm subgroup is included in \(\Pi_E(\theta)\); it is a representation of the full general linear group. This label belongs to the Weil construction and should be distinguished from the finite-field label in Section 5.

The condition in their Theorem 4.6 that \(\theta\) not factor through the norm is equivalent to \(\theta\ne\theta^\sigma\). Indeed a norm character is invariant. Conversely, an invariant character is trivial on every \(\sigma u/u\); Hilbert 90 identifies these elements with the norm-one subgroup. It therefore descends to \(N(E^\times)\), an open subgroup of index two in \(F^\times\). It extends to a smooth character of \(F^\times\): choose a representative of the other coset and a square root of the prescribed value on its square. This proves the equivalence using the class-field norm theorem and Hilbert 90. An invariant character gives a principal series \(I(\xi,\xi\eta_{E/F})\), as stated in Theorem 4.6(iv), rather than a supercuspidal.

## 2. Induction in dimension zero and the lambda factor

The parameter is
\[
\rho_E(\theta)=\operatorname{Ind}_{W_E}^{W_F}\widehat\theta,
\qquad N=0.
\tag{2.1}
\]
The induction constant is defined by
\[
\lambda(E/F,\psi_F)=
\frac{\epsilon_F(s,\operatorname{Ind}_{W_E}^{W_F}1,\psi_F)}
     {\epsilon_E(s,1,\psi_E)}.
\tag{2.2}
\]
This ratio is independent of \(s\). Here is the normalization check. Define \(n_F(\psi_F)\) by saying that \(\varpi_F^{-n_F}\mathcal O_F\) is the largest fractional ideal on which \(\psi_F\) is trivial. If the different has exponent \(d=d(E/F)\), trace duality gives
\[
n_E(\psi_E)=e(E/F)n_F(\psi_F)+d.
\tag{2.3}
\]
The conductor–discriminant identity gives
\(a_F(\operatorname{Ind}1)=f(E/F)d\). These ramification identities are prerequisites [Deligne 1973, §§2 and 5; Conrad, Remark 4.26 and §5]. The epsilon exponent in the numerator is
\(f d+2n_F\), while that in the denominator, expressed with \(q_F\), is \(f n_E=f d+fe n_F=f d+2n_F\). They cancel. Thus (2.2) is the usual constant measured at \(s=1/2\) as well.

**Theorem 2.1.** For every smooth character of \(E^\times\),
\[
\epsilon_F(s,\rho_E(\theta),\psi_F)
=\lambda(E/F,\psi_F)\epsilon_E(s,\theta,\psi_E).
\tag{2.4}
\]

**Proof.** The defining induction property of Weil epsilon factors applies to virtual representations of dimension zero [Deligne 1973, Theorem 4.1(3) and equations (5.6.1)–(5.6.2)]. Apply it to \([\widehat\theta]-[1]\) over \(E\). Multiplicativity on virtual classes gives
\[
\frac{\epsilon_F(s,\operatorname{Ind}\widehat\theta,\psi_F)}
     {\epsilon_F(s,\operatorname{Ind}1,\psi_F)}
=\frac{\epsilon_E(s,\theta,\psi_E)}
      {\epsilon_E(s,1,\psi_E)}.
\]
Dimension zero cancels the possible change of additive Haar measures. Norm twisting to introduce \(s\) commutes with induction because the Weil norm on \(W_F\) restricts to that on \(W_E\). Multiply by the numerator's denominator and use (2.2). This proves (2.4) with the chosen measures, rather than dropping the induction constant. ∎

**Proposition 2.2.** If \(E/F\) is unramified quadratic, then
\[
\lambda(E/F,\psi_F)=(-1)^{n_F(\psi_F)}.
\tag{2.5}
\]
In particular it is one for conductor-zero \(\psi_F\).

**Proof.** In this case \(\operatorname{Ind}1=1\oplus\eta_{E/F}\), with \(\eta_{E/F}\) unramified and \(\eta_{E/F}(\varpi_F)=-1\). For an unramified character \(\alpha\), the Tate change-of-additive-character formula gives
\[
\epsilon_F(s,\alpha,\psi_F)
=\alpha(\varpi_F)^{n_F}q_F^{-n_F(s-1/2)}.
\]
A unit used to scale a conductor-zero additive character contributes nothing to an unramified \(\alpha\). Multiply this formula for \(1\) and \(\eta_{E/F}\). Its value is \((-1)^{n_F}q_F^{-2n_F(s-1/2)}\). The different exponent is zero, so \(n_E=n_F\) and \(q_E=q_F^2\). The denominator of (2.2) is \(q_F^{-2n_F(s-1/2)}\). Division proves (2.5). ∎

## 3. Matching the dihedral part

**Theorem 3.1.** For \(\theta\ne\theta^\sigma\), the representation \(\Pi_E(\theta)\) and parameter \(\rho_E(\theta)\) have the same central/determinant character and the same \(L\)- and epsilon factors after every character twist. They have equal conductors.

**Proof.** Quadratic induction is irreducible by the theorem proved in the Weil-representation lesson. Its determinant, computed there by transfer, is
\[
\det\rho_E(\theta)=
\widehat{\theta|_{F^\times}\eta_{E/F}}.
\tag{3.1}
\]
Comparison with the scalar action in (1.1) gives the central-character match, including its quadratic sign.

The supercuspidal twisted Kirillov model consists of compactly supported functions on \(F^\times\), so its twisted standard \(L\)-factor is one, as proved in the correspondence-statement lesson, Proposition 4.2. An irreducible two-dimensional Weil representation, including every character twist of (2.1), has zero inertia invariants: a nonzero invariant space would be the full irreducible space and would force the representation to factor through the cyclic Weil quotient. Its \(L\)-factor is consequently one as well.

Projection onto the two coset summands proves the induction projection formula
\[
\rho_E(\theta)\otimes\widehat\xi
\simeq\rho_E(\theta(\xi\circ N_{E/F})).
\tag{3.2}
\]
The reciprocity norm identity is used to identify the restricted character. Its extra factor is invariant under \(\sigma\), so the inducing character remains regular. The automorphic twist identity in (1.1), the automorphic formula (1.2), and our induced epsilon formula (2.4) now give equal epsilon factors for every \(\xi\) and every \(\psi_F\).

For conductors, use conductor-zero \(\psi_F\). The \(E\)-epsilon exponent, expressed with \(q_F\), is
\(f(a_E(\theta)+d)\), by (2.3). The constant \(\lambda\) contributes no exponent. Equality of factors proves
\[
a_\epsilon(\Pi_E(\theta))
=a_F(\rho_E(\theta))
=f(E/F)\bigl(a_E(\theta)+d(E/F)\bigr).
\tag{3.3}
\]
The right-hand side is also the Artin induction formula for a character. Since the representation is generic, its epsilon conductor is its newvector conductor by the generic newvector prerequisite. ∎

**Corollary 3.2 (independence of an inducing description).** If two regular quadratic inducing pairs have isomorphic induced Weil representations, their Weil-constructed representations are isomorphic. This holds also in residue characteristic two.

**Proof.** Their determinant characters agree by (3.1). Theorem 3.1 identifies their twisted epsilon factors with those of the same twisted parameter. Their twisted \(L\)-factors and dual \(L\)-factors are all one, so their twisted gamma factors agree. The rank-two local converse theorem applies to these two supercuspidals and gives an isomorphism. No uniqueness of the quadratic inducing field is assumed. ∎

Thus a parameter induced from three quadratic extensions supplies a single representation. The Klein-four examples of the Weil-representation lesson illustrate exactly this issue.

## 4. Existence and a precise characterization

**Theorem 4.1 (Kutzko, stated).** For a p-adic field \(F\), the rank-two local Langlands correspondence exists, including the primitive parameters in residue characteristic two. It is a bijection to Frobenius-semisimple rank-two Weil–Deligne parameters with the five properties stated in the correspondence-statement lesson.

The original theorem is [Kutzko 1980], announced there with an outline of the proof. Its place in the history and its extension to the modern factor-normalized formulation are recalled in [Carayol 2000, Introduction and §2] and [Getz–Hahn 2022, §12.4]; a complete proof of existence in every rank is [Scholze 2013, Theorem 1.2]. Positive-characteristic existence is supplied by the theorem of Laumon–Rapoport–Stuhler stated later. The calculations of Sections 1–3 hold for every nonarchimedean local field; the historical p-adic attribution here does not restrict those calculations.

**Proposition 4.2.** Every factor-preserving correspondence sends \(\Pi_E(\theta)\) to \(\rho_E(\theta)\).

**Proof.** Take the preimage \(\pi'\) of \(\rho_E(\theta)\). The rank-two classification in the correspondence-statement lesson makes \(\pi'\) supercuspidal. Its central character and every twisted factor agree with those of \(\Pi_E(\theta)\) by Theorem 3.1 and factor preservation. Their gamma factors agree, and the local converse theorem identifies \(\pi'\) with \(\Pi_E(\theta)\). ∎

In odd residue characteristic, every irreducible two-dimensional Weil representation is dihedral by the proved classification. Consequently this identifies the entire supercuspidal part there. In residue characteristic two, the primitive tetrahedral and octahedral parameters require the additional constructions in the existence theorem. The elementary dihedral calculation is retained with its actual scope.

The next theorem records exactly what character epsilon factors determine.

**Theorem 4.3 (characterization with the non-supercuspidal dictionary fixed).** Let \(R_1,R_2\) be bijections from rank-two irreducible representations to rank-two parameters. Suppose they agree with the dictionary of the non-supercuspidal lesson, have determinant equal to the central character, and satisfy
\[
\epsilon(s,\pi\otimes(\xi\circ\det),\psi)
=\epsilon(s,R_i(\pi)\otimes\widehat\xi,\psi)
\quad(i=1,2)
\tag{4.1}
\]
for every character \(\xi\). Rank-one parameters are fixed by reciprocity. Then \(R_1=R_2\).

**Proof.** Their common non-supercuspidal dictionary fills precisely all reducible-Weil parameters. Bijectivity therefore makes both maps carry supercuspidals onto irreducible Weil parameters with zero monodromy.

For a supercuspidal \(\pi\), put \(\rho=R_1(\pi)\) and \(\pi'=R_2^{-1}(\rho)\). The determinant assumption gives \(\omega_\pi=\omega_{\pi'}\), and (4.1) gives equal twisted epsilon factors. Every twisted standard and dual \(L\)-factor of these supercuspidals is one. Thus their gamma factors are their epsilon factors and agree for all twists. The rank-two local converse theorem gives \(\pi\simeq\pi'\), whence \(R_2(\pi)=R_1(\pi)\). The maps already agree on the other representations. ∎

The fixed-dictionary hypothesis is necessary. Take an unramified character \(\alpha\) with \(\alpha(\varpi)=\zeta_3\), a primitive cube root of unity. The two distinct irreducible principal series
\[
I(1,1),\qquad I(\alpha,\alpha^{-1})
\tag{4.2}
\]
have central character one and equal epsilon factors after every character twist. For an unramified twist, both epsilon factors are one for conductor-zero \(\psi\). For a ramified twist \(\xi\) of conductor \(m\), the unramified-twist rule for Tate's epsilon factor multiplies its value by \(\alpha(\varpi)^m\); the inverse-character factor multiplies by the inverse value. These cancel, and both pair epsilon factors are \(\epsilon(s,\xi)^2\). Changing \(\psi\) multiplies both by the same determinant and norm factor. But their standard \(L\)-factors are
\[
(1-X)^{-2},\qquad (1+X+X^2)^{-1},
\tag{4.3}
\]
which differ. One could interchange just these two parameters in a bijection and retain the determinant and all character-twisted epsilon identities. Therefore those identities alone do not characterize an unrestricted rank-two dictionary.

There is also a bounded-data version on supercuspidals. If their conductors are at most \(c'\), agreement of twisted epsilon factors for characters of conductor at most \(2c'+4\) suffices. Their twisted \(L\)-factors are one, so these are exactly the bounded gamma equalities in Exercise 7.4 of the local-factor lesson. Its proof uses [Deligne–Henniart 1981, Theorem 4.6 and Lemma 4.7] to extend the equality to all higher-conductor twists, and then the proved converse theorem. This supplies the explicit role of stability and preserves its strict ramification-break condition.

## 5. Depth zero and the rectifier

Let \(E/F\) be unramified quadratic. A regular character \(\bar\Theta:k_E^\times\to\mathbb C^\times\) gives a finite-field cuspidal representation of \(\mathrm{GL}_2(k_F)\) [Deligne–Lusztig 1976, Proposition 7.4 and Theorem 8.3]. Its dimension formula is the absolute value of the Euler characteristic in their Theorem 7.1: the prime-to-\(p\) part of \(|\mathrm{GL}_2(k_F)|\), divided by \(|k_E^\times|\), is \((q_F-1)^2(q_F+1)/(q_F^2-1)=q_F-1\). Inflating it to \(\mathrm{GL}_2(\mathcal O_F)\), extending over the center by a chosen lift \(\Theta:E^\times\to\mathbb C^\times\), and compactly inducing gives a depth-zero supercuspidal, denoted \(\pi_{\mathrm{tame}}(\Theta)\). This construction and its irreducibility are the depth-zero prerequisite [Murnaghan 2009, §8, Proposition 1]. The central character of this labeling is \(\Theta|_{F^\times}\).

**Theorem 5.1 (depth-zero rectifier, stated).** In this labeling the parameter is
\[
\operatorname{rec}(\pi_{\mathrm{tame}}(\Theta))
=\operatorname{Ind}_{W_E}^{W_F}\widehat{\Theta\delta_E},
\tag{5.1}
\]
where \(\delta_E\) is the unramified quadratic character of \(E^\times\), so \(\delta_E(\varpi_E)=-1\). For p-adic fields this is the depth-zero case of the rectifier theorem of Bushnell and Henniart; see [Adrian–Roe 2013, Theorem 3.3, Proposition 3.4 and Theorem 9.5]. The explicit example below is over \(\mathbb Q_3\), within that scope. The finite-field construction and the comparison theorem are not proved here.

The correction already makes the determinant work. Restriction of \(\delta_E\) to \(F^\times\) is \(\eta_{E/F}\): both are unramified and take \(\varpi_F\) to minus one. Hence
\[
\det\operatorname{Ind}\widehat{\Theta\delta_E}
=\widehat{\Theta|_{F^\times}\delta_E|_{F^\times}\eta_{E/F}}
=\widehat{\Theta|_{F^\times}}.
\]
Inducing \(\Theta\) without its rectifier would insert an extra quadratic central character. Since the rectifier has order two, (5.1) also identifies \(\pi_{\mathrm{tame}}(\Theta)\) with \(\Pi_E(\Theta\delta_E)\) in the Weil-construction labeling.

**Example 5.2 (a complete depth-zero example over \(\mathbb Q_3\)).** Let \(E=\mathbb Q_3(i)\), with \(i^2=-1\), the unramified quadratic extension. In \(k_E=\mathbb F_9\), the element \(g=1+i\) has order eight: \(g^2=-i\) and \(g^4=-1\). Put \(\zeta=e^{\pi i/4}\), and choose
\[
\bar\Theta(g)=\zeta,\qquad \Theta(3)=1,
\qquad \Theta|_{1+3\mathcal O_E}=1.
\]
Frobenius changes the residue character to its cube, which is different. Thus the finite-field representation is cuspidal, of dimension two. Its inflation and central extension give the indicated compact induction. The corrected character \(\theta=\Theta\delta_E\) has \(\theta(3)=-1\), residue character \(\bar\Theta\), and conductor one.

The parameter has \(N=0\), conductor two by (3.3), and projective image of order eight: \(\theta/\theta^\sigma\) has residue order four. Its Frobenius matrix on the coset basis can be taken as
\[
\rho(\Phi_F)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad \rho(\Phi_F)^2=-1.
\tag{5.2}
\]
Its determinant at a uniformizer is one. On units the central character is \(\Theta|_{\mathbb Z_3^\times}\); in particular \(\Theta(-1)=\zeta^4=-1\). Its standard \(L\)-factor is one.

Fix the conductor-zero character \(\psi_F\) whose value on \(u/3\), for an integral \(u\), is \(e^{2\pi i\bar u/3}\), and use the positive-sign Fourier transform. Then \(\psi_E(u/3)=\omega^{\operatorname{Tr}_{\mathbb F_9/\mathbb F_3}(\bar u)}\), where \(\omega=e^{2\pi i/3}\). The character Gauss sum is
\[
G=\sum_{j=0}^7\zeta^{-j}\omega^{\operatorname{Tr}(g^j)}.
\tag{5.3}
\]
For \(j=0,\ldots,7\), the trace sequence is \(2,2,0,2,1,1,0,1\). The \(j=2,6\) terms cancel, and the others give
\[
\begin{aligned}
G&=\omega^2(1-i\sqrt2)+\omega(-1+i\sqrt2)\\
 &= (\omega^2-\omega)(1-i\sqrt2)
 =-\sqrt6-i\sqrt3.
\end{aligned}
\tag{5.4}
\]
For clarity, Tate's ramified formula here follows by taking the test function \(\theta^{-1}1_{\mathcal O_E^\times}\). Its zeta integral is one. Its Fourier transform is supported on the valuation-minus-one shell, with value \(9^{-1}\theta(v)G\) at \(v/3\). The dual zeta integral is consequently \(\theta(3)G9^{-s}=-G9^{-s}\). All character \(L\)-factors are one, so this is its epsilon factor. Proposition 2.2 gives \(\lambda=1\), and therefore
\[
\epsilon_F(s,\pi_{\mathrm{tame}}(\Theta),\psi_F)
=(\sqrt6+i\sqrt3)3^{-2s}.
\tag{5.5}
\]
The value at \(s=1/2\) is \((\sqrt6+i\sqrt3)/3\), of absolute value one. Its conductor exponent is two, agreeing with the induced parameter and the generic newvector conductor. The negative uniformizer value in the rectifier accounts for the sign in this calculation.

## 6. Exercises and complete solutions

**Exercise 6.1 (easy).** Compute the lambda factor for an unramified quadratic extension, allowing arbitrary additive-character conductor.

**Solution.** Decompose \(\operatorname{Ind}1=1\oplus\eta\). The two unramified Tate epsilon factors multiply to \((-1)^{n_F}q_F^{-2n_F(s-1/2)}\). The trace character has \(n_E=n_F\), and its trivial-character factor is \(q_E^{-n_F(s-1/2)}=q_F^{-2n_F(s-1/2)}\). Their ratio is \((-1)^{n_F}\). It is one when \(n_F=0\), and minus one when \(n_F\) is odd.

**Exercise 6.2 (medium).** Derive induced epsilon factors from induction in dimension zero.

**Solution.** The virtual class \(\widehat\theta-1\) has dimension zero. Its epsilon factor is the quotient of those of its two terms, and induction preserves that quotient with the trace additive character. Solving the quotient identity for \(\epsilon_F(\operatorname{Ind}\widehat\theta)\) introduces exactly the ratio \(\epsilon_F(\operatorname{Ind}1)/\epsilon_E(1)\), namely \(\lambda\). The norm restriction gives the same identity for every \(s\). Measures cancel in the virtual quotient, while (2.2) fixes them in the two positive-dimensional factors.

**Exercise 6.3 (medium).** Verify conductor preservation for an unramified quadratic regular character of conductor \(m\), and for a ramified quadratic character of conductor \(m\).

**Solution.** Formula (3.3) is \(f(m+d)\). In the unramified quadratic case \(f=2,d=0\), so the value is \(2m\). In the ramified quadratic case \(f=1\), so it is \(m+d\), with the actual different exponent retained. For a tamely ramified quadratic extension \(d=1\), giving \(m+1\); for a dyadic extension \(d\) need not be one. The analytic factor (1.2), with \(n_F=0,n_E=d\), has the same exponent. The constant \(\lambda\) has none. The representation is generic, so the newvector conductor is this epsilon exponent.

**Exercise 6.4 (hard).** Prove rank-two characterization by twisted epsilon factors with the non-supercuspidal dictionary fixed. Explain its bounded-conductor version and why removing the fixed-dictionary hypothesis fails.

**Solution.** A fixed non-supercuspidal dictionary exhausts reducible-Weil parameters. For two candidate bijections and a common irreducible parameter, their two preimages are therefore supercuspidal. Their central characters agree by the determinant condition. Twisted standard and dual factors are one on both preimages, so equal twisted epsilon factors are equal gamma factors. The proved local converse theorem identifies the preimages, giving equality of the bijections. For conductor bound \(c'\), the same argument begins with twists of conductor at most \(2c'+4\). The explicit stability argument of the local-factor lesson's Exercise 7.4 supplies equality for all higher twists and then applies the converse theorem. Finally, the two principal series (4.2) have equal central and all twisted epsilon factors but unequal \(L\)-factors (4.3). Interchanging their parameters supplies the required counterexample to an unrestricted assertion.

## What this lesson does not prove

The Weil representation, the construction and its irreducibility, and the automorphic functional equation (1.2) are [Jacquet–Langlands 1970, §1 and Theorems 4.6–4.7], or the supercuspidal-construction prerequisite. The virtual epsilon-factor induction axiom is [Deligne 1973, Theorem 4.1(3), equations (5.6.1)–(5.6.2)]; its application to a character and the normalization of lambda were proved here. The ramification norm, different and conductor–discriminant identities are prerequisites. Their precise exponents were retained in (2.3) and (3.3).

Kutzko's rank-two existence theorem is stated in Section 4 [Kutzko 1980]; its proof using local representation theory is not supplied. Positive-characteristic existence is the stated later theorem of Laumon–Rapoport–Stuhler. The rank-two converse theorem is proved earlier in this course. The explicit stability input is [Deligne–Henniart 1981, Theorem 4.6 and Lemma 4.7], used through the earlier bounded-twist exercise. The characterization and the counterexample to an unrestricted epsilon-only claim were proved here.

The finite-field cuspidal representation and its compact-induction construction are prerequisites from the supercuspidal-construction lesson. Exact external locators are [Deligne–Lusztig 1976, Theorem 7.1, Proposition 7.4 and Theorem 8.3] and [Murnaghan 2009, §8, Proposition 1]. The rectifier is a stated comparison theorem of Bushnell and Henniart [Adrian–Roe 2013, Theorem 3.3, Proposition 3.4 and Theorem 9.5]. Its p-adic depth-zero application, central-character check and the complete \(\mathbb Q_3\) epsilon calculation were carried out explicitly. No assertion that the two constructions use identical character labels is made.

## References

- [Jacquet–Langlands 1970] Hervé Jacquet and Robert P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, Springer, 1970, §1 and Theorems 4.6–4.7.
- [Deligne 1973] Pierre Deligne, “[Les constantes des équations fonctionnelles des fonctions L](https://publications.ias.edu/sites/default/files/Number20.pdf),” in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349, Springer, 1973, 501–597, Theorem 4.1 and §5, especially equations (5.5.1)–(5.6.2).
- [Deligne–Henniart 1981] Pierre Deligne and Guy Henniart, “[Sur la variation, par torsion, des constantes locales d'équations fonctionnelles de fonctions L](https://publications.ias.edu/sites/default/files/Number43.pdf),” *Inventiones mathematicae* 64 (1981), 89–118, Theorem 4.6 and Lemma 4.7.
- [Kutzko 1980] Philip Kutzko, “[The Langlands conjecture for GL_2 of a local field](https://www.ams.org/journals/bull/1980-02-03/S0273-0979-1980-14765-5/S0273-0979-1980-14765-5.pdf),” *Bulletin of the American Mathematical Society (New Series)* 2 (1980), 455–458.
- [Adrian–Roe 2013] Moshe Adrian and David Roe, [*Rectifiers and the local Langlands correspondence: the unramified case*](https://arxiv.org/abs/1307.0469), §§3 and 9, Theorem 3.3, Proposition 3.4 and Theorem 9.5. The cited version uses geometric Frobenius and gives the depth-zero rectifier value \((-1)^{n-1}\).
- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§11.5 and 12.4.
- [Carayol 2000] Henri Carayol, “[Preuve de la conjecture de Langlands locale pour GL_n : travaux de Harris–Taylor et Henniart](https://www.numdam.org/item/SB_1998-1999__41__191_0/),” Séminaire Bourbaki, exposé 857 (1998–1999), *Astérisque* 266 (2000), 191–243.
- [Scholze 2013] Peter Scholze, [*The Local Langlands Correspondence for GL_n over p-adic fields*](https://arxiv.org/abs/1010.1540v1), *Inventiones mathematicae* 192 (2013), 663–715, Theorem 1.2.
- [Conrad] Keith Conrad, [*The different ideal*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf), expository notes, Remark 4.26 and §5.
- [Deligne–Lusztig 1976] Pierre Deligne and George Lusztig, “[Representations of reductive groups over finite fields](https://publications.ias.edu/sites/default/files/Number27.pdf),” *Annals of Mathematics* 103 (1976), 103–161.
- [Murnaghan 2009] Fiona Murnaghan, [*Representations of Reductive p-adic Groups*](https://www.math.toronto.edu/murnaghan/courses/mat1197/notes.pdf), notes under revision March 2009, §8, Proposition 1, page 66: compact induction from an inflated finite-field cuspidal representation extended over the center.
