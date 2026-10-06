# The statement of the local Langlands correspondence

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Local class field theory turns a character of a local field into a one-dimensional Weil representation. The local Langlands correspondence extends this dictionary to irreducible representations of every general linear group. Its normalization is fixed by factors of pairs, not just by a match of dimensions or central characters. In rank two those requirements already force the principal series, Steinberg twists and determinant characters, and the converse theorem proves uniqueness on the remaining representations.

We assume local reciprocity, the representation classification by segments, the local factors and rank-two converse theorem from *Local factors of pairs and the rank-two converse theorem*, and the elementary definitions of Weil–Deligne representations. The general existence and uniqueness theorems are stated. Basic references are [Wedhorn 2000], [Getz–Hahn 2022], [Deligne 1973] and [Cogdell–Shahidi–Tsai 2017].

## 1. The two sides, with one fixed normalization

Let \(F\) be a nonarchimedean local field, \(q\) its residue cardinality and \(W_F\) its Weil group. Local reciprocity is normalized by
\[
\operatorname{Art}_F(\varpi)=\Phi_{\mathrm{geom}},
\qquad \lVert\Phi_{\mathrm{geom}}\rVert=q^{-1}.
\tag{1.1}
\]
For a character \(\chi:F^\times\to\mathbb C^\times\), write
\(\widehat\chi=\chi\circ\operatorname{Art}_F^{-1}\) on the Weil abelianization. In particular \(\widehat{|\,\cdot\,|}=\lVert\cdot\rVert\).

Let \(\operatorname{Irr}(G_n)\) be the isomorphism classes of irreducible smooth admissible representations of \(G_n=\mathrm{GL}_n(F)\). Let \(\operatorname{WD}_n(F)\) be the isomorphism classes of \(n\)-dimensional Frobenius-semisimple Weil–Deligne objects \((r,N)\): the inertia action has finite image, \(r(\Phi_{\mathrm{geom}})\) is semisimple, \(N\) is nilpotent, and
\[
r(w)Nr(w)^{-1}=\lVert w\rVert N.
\tag{1.2}
\]
The Weil action is then semisimple; a proof is given in *Monodromy blocks and the passage from supercuspidals to all parameters*.

Tensor products and duals have monodromy
\[
N_{V\otimes V'}=N_V\otimes1+1\otimes N_{V'},\qquad
N_{V^\vee}=-{}^tN_V.
\tag{1.3}
\]
The determinant parameter has Weil character \(\det r\) and zero monodromy, since the induced operator on the top exterior power is \(\operatorname{tr}N=0\).

The parameter factor is
\[
L(s,r,N)=\det(1-q^{-s}r(\Phi_{\mathrm{geom}})
 \mid(\ker N)^{I_F})^{-1}.
\tag{1.4}
\]
We use the usual Artin–Deligne epsilon factor and self-dual additive measure. At additive-character conductor zero its exponent in \(q^{-(s-1/2)}\) is
\[
a(r,N)=a(r)+\dim V^{I_F}-\dim(\ker N)^{I_F}.
\tag{1.5}
\]
These factor definitions and their one-dimensional compatibility with Tate's factors are prerequisites; see [Deligne 1973, §3.2.2] and [Wedhorn 2000, §3.2].

## 2. The correspondence as a family of bijections

A **local Langlands correspondence** for \(F\) is a family
\[
\operatorname{rec}_{F,n}:\operatorname{Irr}(G_n)
\overset{\sim}{\longrightarrow}\operatorname{WD}_n(F),
\qquad n\ge1,
\tag{2.1}
\]
with the following five properties. They refer to the same family in every rank.

1. For \(n=1\), \(\operatorname{rec}_{F,1}(\chi)=\widehat\chi\).
2. For every pair \(\pi,\pi'\), their Rankin–Selberg \(L\)- and epsilon factors equal those of the tensor product of their parameters, with the same \(\psi\):
   \[
   L(s,\pi\times\pi')=L(s,\operatorname{rec}(\pi)\otimes\operatorname{rec}(\pi')),
   \quad
   \epsilon(s,\pi\times\pi',\psi)=
   \epsilon(s,\operatorname{rec}(\pi)\otimes\operatorname{rec}(\pi'),\psi).
   \tag{2.2}
   \]
3. Character twists satisfy
   \(\operatorname{rec}(\pi\otimes(\chi\circ\det))=
   \operatorname{rec}(\pi)\otimes\widehat\chi\).
4. If \(\omega_\pi\) is the central character, then
   \(\det\operatorname{rec}(\pi)=\widehat{\omega_\pi}\).
5. Duality satisfies \(\operatorname{rec}(\pi^\vee)=\operatorname{rec}(\pi)^\vee\).

The tensor relation for \(L\)-factors alone does not replace the epsilon-factor relation: the latter retains ramification information and the conductor. Conversely a match of central characters does not identify a representation; many principal series have the same product of inducing characters.

**Theorem 2.1 (Henniart uniqueness, stated).** There is at most one family (2.1) satisfying these properties.

**Theorem 2.2 (existence, stated).** Such a family exists for every finite extension of \(\mathbb Q_p\), by Harris–Taylor and independently Henniart. It exists for local fields of positive characteristic by Laumon–Rapoport–Stuhler. Together with the archimedean correspondence this gives the general linear correspondence over every local field.

The normalization and the first two theorems are [Wedhorn 2000, (1.2.2)]; uniqueness is proved in [Henniart 1993] and existence in [Scholze 2013, Theorem 1.2]. The general-local-field statement is [Getz–Hahn 2022, Theorem 12.4.1]. Their proofs and strategies are subjects of later lessons; no construction of the general correspondence is asserted here.

The structural extension by segments gives, in every rank,
\[
\begin{array}{c|c}
\text{representation}&\text{parameter}\\\hline
\text{supercuspidal}&\text{irreducible Weil representation, }N=0\\
\text{essentially square-integrable}&\text{indecomposable Weil--Deligne object}.
\end{array}
\tag{2.3}
\]
These general correspondences follow from the stated supercuspidal reduction and segment extension [Wedhorn 2000, (4.2.2)]. We prove the rank-two assertions below. “Indecomposable” on the Weil–Deligne side is important: a Steinberg parameter has reducible underlying Weil action.

One consequence needs no classification.

**Proposition 2.3.** Every family satisfying the five properties preserves epsilon-factor conductors in every rank.

**Proof.** Pair \(\pi\) with the trivial character, whose parameter is the trivial Weil character by property 1. Property 2 identifies the standard epsilon factor with that of \(\operatorname{rec}(\pi)\). For a conductor-zero additive character, their exponents in \(q^{-(s-1/2)}\) are respectively \(a(\pi)\) and (1.5). Equality as functions of \(s\) forces equality of these exponents. ∎

For generic \(\pi\), the newvector theorem makes this also an equality with its Casselman newvector conductor. For nongeneric representations the epsilon-factor conductor remains defined; the generic newvector theorem is not being extended to them.

## 3. A rank-two parameter is detected by twisted \(L\)-factors

Define the centered special block \(S_2\) by
\[
r(w)=
\begin{pmatrix}
\lVert w\rVert^{-1/2}&0\\0&\lVert w\rVert^{1/2}
\end{pmatrix},
\qquad Ne_-=e_+,\quad Ne_+=0.
\tag{3.1}
\]
In the uncentered notation \(\operatorname{Sp}(2)\) with Weil characters \(1,\lVert\cdot\rVert\), this is
\(S_2=\operatorname{Sp}(2)\otimes\lVert\cdot\rVert^{-1/2}\).

**Lemma 3.1.** A two-dimensional Frobenius-semisimple parameter has exactly one of these forms:
\[
(\rho,0)\ \text{with \(\rho\) irreducible};\qquad
(\lambda_1\oplus\lambda_2,0);\qquad
\lambda\otimes S_2.
\tag{3.2}
\]
Here \(\lambda_i,\lambda\) are Weil characters, and the last case has nonzero monodromy.

**Proof.** If the Weil action is irreducible, \(\ker N\) is a nonzero Weil-stable subspace, so equals the entire space and \(N=0\). Otherwise the semisimple Weil action is a sum of characters. If \(N\ne0\), its image and kernel are the same line. Relation (1.2) says that the character on this line is \(\lVert\cdot\rVert\) times the character on the quotient. Writing their midpoint as \(\lambda\) gives (3.1); rescaling a basis makes the nonzero coefficient of \(N\) equal to one. If \(N=0\), no further constraint is present. These cases are disjoint. ∎

**Lemma 3.2 (twisted factor profile).** The family \(L(s,\sigma\otimes\widehat\xi)\), for all characters \(\xi\) of \(F^\times\), determines which case of (3.2) occurs. It determines \(\sigma\) completely in the last two cases.

**Proof.** In the direct-sum case, \(\ker N\) has the two characters \(\lambda_1,\lambda_2\). In the special case it has the single character \(\lambda\lVert\cdot\rVert^{1/2}\). Restrict these characters, through reciprocity, to \(\mathcal O^\times\). For each unit character \(\eta\), extend \(\eta^{-1}\) to \(\xi_\eta\) by setting \(\xi_\eta(\varpi)=1\). The polynomial
\[
P_\eta(X)=L(s,\sigma\otimes\widehat{\xi_\eta})^{-1}
\tag{3.3}
\]
has roots determined by the Frobenius values of exactly the kernel characters whose unit restriction is \(\eta\). Thus its degree counts those characters, with multiplicity, and its factors recover their uniformizer values. Together the unit restriction and that value recover each character. Only finitely many of these polynomials are nonconstant.

The sum of their degrees is two for the direct-sum case and one for the special case. In the latter, knowing the kernel character recovers \(\lambda\) by removing \(\lVert\cdot\rVert^{1/2}\).

For an irreducible two-dimensional \(\rho\), every character twist has zero inertia invariants. Otherwise that invariant space, stable under the Weil group because inertia is normal, would be the whole irreducible twist. The representation would factor through \(W_F/I_F\simeq\mathbb Z\), whose irreducible complex representations have dimension one. This is impossible. Its entire factor profile is therefore one, and the degree sum is zero. This distinguishes all three cases. ∎

## 4. The values forced on non-supercuspidals

We use the rank-two analytic formulas from the local-factor prerequisite:
\[
\begin{aligned}
L(s,I(\mu_1,\mu_2)\times\xi)
 &=L(s,\mu_1\xi)L(s,\mu_2\xi)
 &&\text{if the principal series is irreducible},\\
L(s,(\mathrm{St}_2\otimes\chi)\times\xi)
 &=L(s,\chi\xi|\cdot|^{1/2}),\\
L(s,(\chi\circ\det)\times\xi)
 &=L(s,\chi\xi|\cdot|^{-1/2})
   L(s,\chi\xi|\cdot|^{1/2}).
\end{aligned}
\tag{4.1}
\]
For the first two lines the analytic inputs are [Jacquet–Langlands 1970, §3, the principal and special representation factor calculations following Theorem 3.3]. The last line is the Langlands-quotient extension [Getz–Hahn 2022, §11.8]. These formulas include ramified characters: a ramified Tate character has \(L\)-factor one.

**Theorem 4.1.** Every family with properties 1–5 has the following values:
\[
\begin{aligned}
\operatorname{rec}(I(\mu_1,\mu_2))
 &=\widehat{\mu_1}\oplus\widehat{\mu_2}
 &&(\mu_1/\mu_2\ne|\cdot|^{\pm1}),\\
\operatorname{rec}(\mathrm{St}_2\otimes\chi)
 &=\widehat\chi\otimes S_2,\\
\operatorname{rec}(\chi\circ\det)
 &=\widehat{\chi|\cdot|^{-1/2}}\oplus
   \widehat{\chi|\cdot|^{1/2}}.
\end{aligned}
\tag{4.2}
\]

**Proof.** Property 2 against every rank-one representation, together with property 1, makes the parameter's twisted factor profile exactly (4.1). The first and third profiles have total degree two in the procedure of Lemma 3.2, even if the two characters have different inertia restrictions or their poles coincide. That lemma forces zero monodromy and recovers the two displayed characters with their multiplicities. The special profile has degree one, with kernel character \(\widehat\chi\lVert\cdot\rVert^{1/2}\); it forces the nonzero-monodromy case and its midpoint \(\widehat\chi\). This proves all three values. ∎

The two representations at a reducibility point have the same underlying semisimple Weil action. One has monodromy zero, and the other has monodromy of rank one. Their different twisted \(L\)-profiles detect precisely that distinction.

**Proposition 4.2.** For a supercuspidal \(\pi\) of \(G_2\), every \(L(s,\pi\times\xi)\) equals one. Every correspondence with properties 1–5 consequently sends \(\pi\) to an irreducible Weil representation with \(N=0\); conversely every such parameter has a supercuspidal preimage.

**Proof.** The supercuspidal Kirillov-model prerequisite identifies \(V_\pi\) with \(C_c^\infty(F^\times)\) [Jacquet–Langlands 1970, §2]. A character twist has the same compact-support space. Each of its Mellin zeta integrals is a Laurent polynomial in \(q^{-s}\); the function \(1_{\mathcal O^\times}\), adjusted by the unit character if needed, gives the constant integral one. Their ideal is therefore the full Laurent polynomial ring, whose normalized \(L\)-generator is one. By Proposition 3.1 of the local-factor lesson, these are the pair factors.

Property 2 transfers this profile to the parameter. Lemma 3.2 forces its first case, which has irreducible Weil action and zero monodromy. Conversely, the three non-supercuspidal types have the two other parameter types by Theorem 4.1. A bijective correspondence cannot send any of them to an irreducible Weil parameter, so its preimage must be supercuspidal. ∎

Together with the representation classification, (4.2) and Proposition 4.2 also prove (2.3) in rank two: the essentially square-integrable representations are the supercuspidals and Steinberg twists, and their parameters are exactly the indecomposable ones.

## 5. Two normalization checks

For rank one, the dictionary is \(\chi\mapsto\widehat\chi\). Products and inverses commute with reciprocity, proving the twist, determinant and dual identities directly. The pair \(\chi,\chi'\) has Tate factor for \(\chi\chi'\), agreeing with the Weil factor of \(\widehat\chi\,\widehat{\chi'}\) by the class-field-theoretic factor compatibility prerequisite. This checks all five properties in dimension one.

For \(\mathrm{St}_2\), the kernel of the parameter's monodromy is its \(+\tfrac12\) line. Hence
\[
L(s,S_2)=(1-q^{-s-1/2})^{-1}.
\tag{5.1}
\]
For conductor-zero \(\psi\), the Weil epsilon factor of the two unramified characters is one. Its monodromy correction is
\[
\det(-q^{-s}\Phi\mid V^{I_F}/(\ker N)^{I_F})
=-q^{1/2-s}.
\tag{5.2}
\]
On the representation side, use the normalized Iwahori Whittaker function in the local-factor lesson:
\[
W(a_r)=q^{-r}\ (r\ge0),\quad W(a_r)=0\ (r<0),\quad
W(a_rw)=-q^{-r-1}\ (r\ge-1).
\]
Its ordinary zeta integral is (5.1). The dual integral at \(1-s\), with trivial central character, is
\[
\sum_{r\ge-1}(-q^{-r-1})q^{-r(1/2-s)}
=-q^{1/2-s}(1-q^{s-3/2})^{-1}.
\tag{5.3}
\]
Dividing by \(L(1-s,\mathrm{St}_2)\) in the functional equation gives exactly (5.2). The conductor is one. Reversing which character carries \(\ker N\) would change (5.1) and fail this check.

## 6. Exercises and complete solutions

**Exercise 6.1 (easy).** Check the determinant property for the irreducible principal series \(I(\mu_1,\mu_2)\).

**Solution.** A scalar \(z1_2\) acts on normalized induction by \(\mu_1(z)\mu_2(z)\), since its modular character is one. Thus \(\omega_\pi=\mu_1\mu_2\). The determinant of \(\widehat{\mu_1}\oplus\widehat{\mu_2}\) is \(\widehat{\mu_1}\widehat{\mu_2}=\widehat{\mu_1\mu_2}\), as required.

**Exercise 6.2 (medium).** Prove that a supercuspidal rank-two representation has \(L(s,\pi\times\xi)=1\) for every character, and explain what this says about inertia invariants of its parameter.

**Solution.** Its twisted Kirillov space is compactly supported on \(F^\times\), so all Mellin integrals are Laurent polynomials; a unit-supported function supplies one. This proves that the ideal generator is one. Property 2 gives \(L(s,\sigma\otimes\widehat\xi)=1\) for all \(\xi\). Lemma 3.2 rules out both reducible parameter types and gives \(\sigma=(\rho,0)\) irreducible. For such a parameter, a nonzero inertia-invariant space in any twist would be Weil-stable and therefore the whole representation, contradicting irreducibility in dimension two of a representation factoring through the cyclic quotient. Thus every twist has zero inertia invariants, not just zero invariants in its monodromy kernel.

**Exercise 6.3 (medium).** Verify the epsilon-factor match for \(\mathrm{St}_2\), including the sign, with conductor-zero \(\psi\).

**Solution.** On the parameter side the quotient of inertia invariants by the monodromy kernel is the \(-\tfrac12\) line, with geometric Frobenius value \(q^{1/2}\). Its correction is \(-q^{-s}q^{1/2}\), while its unramified Weil epsilon factor is one. On the representation side (5.3), divided by the dual \(L\)-factor, gives the same \(-q^{1/2-s}\). In particular the root number at \(s=1/2\) is \(-1\), and the epsilon exponent is one.

**Exercise 6.4 (hard).** Prove uniqueness of the rank-two correspondence without invoking the general Henniart uniqueness theorem.

**Solution.** Let \(\operatorname{rec}_1,\operatorname{rec}_2\) be two families with the five properties. They agree in rank one by local reciprocity and on rank-two non-supercuspidals by Theorem 4.1. For a supercuspidal \(\pi\), put \(\sigma=\operatorname{rec}_1(\pi)\), and let \(\pi'=\operatorname{rec}_2^{-1}(\sigma)\). Proposition 4.2 makes \(\sigma\) irreducible with \(N=0\), and makes \(\pi'\) supercuspidal. Property 4 and injectivity of rank-one reciprocity give \(\omega_\pi=\omega_{\pi'}\).

For every character \(\xi\), property 2 identifies the \(L\)- and epsilon factors of \(\pi\times\xi\) and \(\pi'\times\xi\) with the same tensor parameter \(\sigma\otimes\widehat\xi\). Property 5 makes their dual factors match \(\sigma^\vee\otimes\widehat{\xi}^{-1}\) as well. The definition of gamma therefore gives equal twisted gamma factors. Both representations are infinite-dimensional, so the rank-two local converse theorem proves \(\pi\simeq\pi'\). It follows that \(\operatorname{rec}_2(\pi)=\sigma=\operatorname{rec}_1(\pi)\). This covers every irreducible rank-two representation. ∎

## What this lesson does not prove

The general uniqueness and existence theorems are stated in Section 2, with [Wedhorn 2000, (1.2.2)], [Henniart 1993], [Scholze 2013, Theorem 1.2] and [Getz–Hahn 2022, Theorem 12.4.1] as locators. The general supercuspidal reduction and extension through segments are [Wedhorn 2000, (4.2.2)]. Their rank-two consequences were proved here.

Local reciprocity, Tate-factor compatibility, Artin–Deligne local factor definitions, and the Kirillov-model classification are prerequisites. The analytic formulas used in (4.1) are the principal/special calculations in [Jacquet–Langlands 1970, §3, following Theorem 3.3], and the extension in [Getz–Hahn 2022, §11.8]. The functional equation used for the explicit Steinberg check is [Jacquet–Langlands 1970, Theorem 2.18]. The profile argument, the forced values, conductor equality, the supercuspidal implication and rank-two uniqueness were proved in this lesson.

The normalization here is the unitary correspondence of [Deligne 1973, §3.2.3]. The alternative correspondences in §§3.2.5–3.2.6 insert different absolute-value twists. Importing their formulas without those twists would change both the central character and the arguments of the \(L\)-factors.

## References

- [Wedhorn 2000] Torsten Wedhorn, [*The local Langlands correspondence for GL(n) over p-adic fields*](https://arxiv.org/abs/math/0011210v2), lectures at the School on Automorphic Forms on GL(n), ICTP Trieste, 2000, §§1.2, 3.2 and 4.2.
- [Henniart 1993] Guy Henniart, “[Caractérisation de la correspondance de Langlands locale par les facteurs \(\epsilon\) de paires](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0113/LOG_0039.pdf),” *Inventiones mathematicae* 113 (1993), 339–350.
- [Scholze 2013] Peter Scholze, [*The Local Langlands Correspondence for GL_n over p-adic fields*](https://arxiv.org/abs/1010.1540v1), *Inventiones mathematicae* 192 (2013), 663–715, Theorem 1.2.
- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, *An Introduction to Automorphic Representations, with a View toward Trace Formulae*, draft of 22 April 2022, §§11.8 and 12.4–12.5. Published as Graduate Texts in Mathematics 300, Springer, 2024; the [author version](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf) uses the cited numbering.
- [Deligne 1973] Pierre Deligne, “[Formes modulaires et représentations de GL(2)](https://publications.ias.edu/sites/default/files/Number21.pdf),” in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349, Springer, 1973, 55–105, §§3.2.2–3.2.6.
- [Jacquet–Langlands 1970] Hervé Jacquet and Robert P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, Springer, 1970, §§2–3.
- [Cogdell–Shahidi–Tsai 2017] James W. Cogdell, Freydoon Shahidi and Tung-Lun Tsai, “Local Langlands correspondence for GL_n and the exterior and symmetric square \(\epsilon\)-factors,” *Duke Mathematical Journal* 166 (2017), 2053–2132, §1; [arXiv:1412.1448](https://arxiv.org/abs/1412.1448). This records the factor-compatible framework and further operations.
