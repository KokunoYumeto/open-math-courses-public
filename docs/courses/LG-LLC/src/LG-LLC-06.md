# The rank-two correspondence: principal series, Steinberg twists and characters

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

At a reducibility point of a principal series, its two constituents have the same two character labels. Their parameters nevertheless differ: the Steinberg constituent has a nonzero monodromy operator, while the determinant character has none. This difference changes both the local Euler factor and the conductor. We calculate those changes, including ramified twists and the tensor product of two Steinberg parameters.

We assume normalized induction and the rank-two representation classification, Tate's local functional equation, the Schwartz and Whittaker models, and the generic newvector theorem. Their precise uses are identified below. The correspondence statement from *The statement of the local Langlands correspondence* fixes the normalization, but its existence theorem is not used to deduce the factor calculations in this lesson. Basic references are [Jacquet–Langlands 1970], [Deligne 1973] and [Getz–Hahn 2022].

## 1. The candidate dictionary

Let \(F\) be any nonarchimedean local field, with residue cardinality \(q\), and put \(\nu=|\cdot|_F\). Reciprocity sends a uniformizer to geometric Frobenius \(\Phi\), with \(\lVert\Phi\rVert=q^{-1}\). A hat denotes the corresponding Weil character. Write \(I(\mu_1,\mu_2)\) for normalized induction to \(G_2=\mathrm{GL}_2(F)\), and write \(\mathrm{St}\chi\) for \(\mathrm{St}_2\otimes(\chi\circ\det)\).

The non-supercuspidal irreducibles are precisely
\[
I(\mu_1,\mu_2)\quad(\mu_1/\mu_2\ne\nu^{\pm1}),
\qquad \mathrm{St}\chi,
\qquad \chi\circ\det.
\tag{1.1}
\]
This classification is the prerequisite recalled in *Irreducible representations of general linear groups over a local field*, Section 3; its source is [Jacquet–Langlands 1970, Theorem 3.3]. Principal-series labels are unordered. Define
\[
\begin{aligned}
R(I(\mu_1,\mu_2))&=(\widehat\mu_1\oplus\widehat\mu_2,0),\\
R(\mathrm{St}\chi)&=\widehat\chi\otimes S_2,\\
R(\chi\circ\det)&=(\widehat{\chi\nu^{-1/2}}
                         \oplus\widehat{\chi\nu^{1/2}},0).
\end{aligned}
\tag{1.2}
\]
Here \(S_2\) has basis \(e_-,e_+\), Weil weights \(\lVert\cdot\rVert^{-1/2},\lVert\cdot\rVert^{1/2}\), and \(Ne_-=e_+\), \(Ne_+=0\). Its monodromy kernel is the positive-half line.

**Proposition 1.1.** The map (1.2) is a bijection onto the rank-two Frobenius-semisimple parameters whose underlying Weil action is reducible.

**Proof.** Such a parameter has either zero monodromy and two character summands, or the form \(\lambda S_2\), by the rank-two classification in the correspondence-statement lesson, Lemma 3.1. A sum of two characters whose ratio is not \(\lVert\cdot\rVert^{\pm1}\) gives the first line of (1.2). When their ratio is \(\lVert\cdot\rVert\), the unique midpoint \(\widehat\chi\) gives the third line. Nonzero monodromy gives the second line, with \(\widehat\chi\) recovered from the kernel character by removing \(\lVert\cdot\rVert^{1/2}\). These three cases are disjoint. Reciprocity and the uniqueness of the labels in (1.1) prove both surjectivity and injectivity. ∎

## 2. Twists, determinants and duals

**Proposition 2.1.** The candidate commutes with character twists and duality, and its determinant is the character corresponding to the central character.

**Proof.** Twisting normalized induction multiplies both inducing characters by the twisting character. Twisting \(\mathrm{St}\chi\) or \(\chi\circ\det\) multiplies \(\chi\) by that character. Each line of (1.2) therefore commutes with twists.

The central character of the principal series is \(\mu_1\mu_2\): a scalar matrix has modular character one. The central characters of the other two representations are \(\chi^2\). The determinant of \(S_2\) is one, so (1.2) gives exactly these three determinant characters.

For principal series, the usual invariant pairing of normalized induction with its inverse-character induction gives
\(I(\mu_1,\mu_2)^\vee\simeq I(\mu_1^{-1},\mu_2^{-1})\); this normalized-duality fact is part of the induction prerequisite [Getz–Hahn 2022, §8.2]. Also \(\mathrm{St}_2^\vee\simeq\mathrm{St}_2\). One can see the latter from the same pairing at the reducibility point: the dual of the infinite-dimensional constituent is the infinite-dimensional constituent with the inverse cuspidal support \(\{\nu^{-1/2},\nu^{1/2}\}\), whose only such constituent is Steinberg. Thus \((\mathrm{St}\chi)^\vee=\mathrm{St}\chi^{-1}\), while a determinant character is inverted.

On \(S_2\), the alternating form with \(B(e_-,e_+)=1\) is Weil-invariant and satisfies \(B(Nx,y)+B(x,Ny)=0\). It identifies \(S_2\) with its dual, whose monodromy is \(-{}^tN\). Direct sums dualize by inverting their characters. Applying these identities to (1.2) proves the dual assertion. ∎

## 3. Standard factors from two Tate integrals

Initially let \(\psi\) have conductor zero and use self-dual additive measure, with \(\operatorname{vol}(\mathcal O)=1\) and multiplicative measure giving \(\mathcal O^\times\) volume one. Put \(X=q^{-s}\). For a smooth character \(\tau\), write
\[
\epsilon(s,\tau,\psi)=w(\tau,\psi)
                         q^{-a(\tau)(s-1/2)}.
\tag{3.1}
\]
For unramified \(\tau\), this epsilon factor is one and
\(L(s,\tau)=(1-\tau(\varpi)X)^{-1}\). For ramified \(\tau\), its \(L\)-factor is one. These are Tate's character-factor inputs.

We use only the following part of the **Schwartz-model prerequisite**. The Whittaker functions of an irreducible principal series are the images of \(\Phi\in\mathcal S(F^2)\), and their standard zeta integrals are
\[
J_{\mu_1,\mu_2}(s,\Phi)=
\int_{F^\times}\int_{F^\times}
 \Phi(x,y)\mu_1(x)\mu_2(y)|xy|^s\,d^\times x\,d^\times y.
\tag{3.2}
\]
The Weyl operator in that realization is the Fourier operator; after the dual characters are inserted, its functional equation is obtained by applying Tate's functional equation in each variable. For the untwisted special constituent, the image is obtained from the subspace
\[
\int_F\Phi(x,0)\,dx=0.
\tag{3.3}
\]
Determinant twists insert the twisting character in both variables of (3.2). These realization statements are [Jacquet–Langlands 1970, Proposition 3.2 and the realization assertion of Proposition 3.6]. The displayed zeta identity and Fourier action are also the identities used in the proof of Proposition 3.5. We now compute their factor consequences.

**Lemma 3.1 (principal series).** If the principal series is irreducible, then
\[
\begin{aligned}
L(s,I(\mu_1,\mu_2))&=L(s,\mu_1)L(s,\mu_2),\\
\epsilon(s,I(\mu_1,\mu_2),\psi)
 &=\epsilon(s,\mu_1,\psi)\epsilon(s,\mu_2,\psi).
\end{aligned}
\tag{3.4}
\]

**Proof.** Every locally constant compactly supported function on \(F^2\) is a finite sum of functions \(f_1(x)f_2(y)\): enclose its support in a compact rectangle and partition that rectangle into sufficiently small additive cosets on which it is constant. On such a tensor, (3.2) is the product of the two Tate integrals.

Each Tate integral belongs to \(L(s,\mu_i)\mathbb C[X,X^{-1}]\), and some \(f_i\) realizes \(L(s,\mu_i)\). For an unramified character take \(f_i=1_{\mathcal O}\). For a ramified character take \(f_i=\mu_i^{-1}1_{\mathcal O^\times}\), which gives the constant integral one. Thus the integral ideal in (3.2) is exactly the product ideal, proving its normalized \(L\)-generator in (3.4).

Apply the Tate functional equation in the two variables, first on a tensor and then on their finite sums. The Fourier/Weyl identification in the prerequisite gives the gamma factor
\[
\gamma(s,I(\mu_1,\mu_2),\psi)
 =\gamma(s,\mu_1,\psi)\gamma(s,\mu_2,\psi).
\tag{3.5}
\]
The dual principal series has the inverse characters. Substituting its already computed \(L\)-factor and the definition \(\gamma=\epsilon L^\vee(1-s)/L(s)\) into (3.5) cancels the four Tate \(L\)-factors and leaves the asserted product of epsilon factors. ∎

**Lemma 3.2 (special representations).** Put \(\beta=\tau(\varpi)\) when \(\tau\) is unramified. Then
\[
\begin{array}{c|c|c}
&L(s,\mathrm{St}\tau)&\epsilon(s,\mathrm{St}\tau,\psi)\\\hline
\tau\text{ unramified}&(1-\beta q^{-1/2}X)^{-1}&-\beta q^{1/2}X\\
\tau\text{ ramified}&1&\epsilon(s,\tau,\psi)^2.
\end{array}
\tag{3.6}
\]

**Proof.** In the special model (3.2) has characters \(\tau\nu^{1/2}\), \(\tau\nu^{-1/2}\), with condition (3.3). If \(\tau\) is ramified, all double Tate integrals are Laurent polynomials. Choose both functions supported on units and equal there to \(\tau^{-1}\). Their tensor satisfies (3.3), because its second factor vanishes at zero, and its double integral is one. Hence the special integral ideal has generator one.

Suppose \(\tau\) is unramified. Before the condition (3.3), the possible denominator is
\[
(1-\beta q^{-1/2}X)(1-\beta q^{1/2}X).
\tag{3.7}
\]
At \(X=\beta^{-1}q^{-1/2}\), the possible pole comes from the tail \(y\to0\). Its residue is a fixed nonzero constant times the first-variable integral of \(\Phi(x,0)\), evaluated at that value of \(X\). On the shell \(v(x)=r\), the first-variable weight there is
\(\beta^r q^{-r/2}X^r=q^{-r}\). Multiplicative measure multiplied by \(|x|\) is a fixed multiple of additive measure, so this residue vanishes by (3.3). This shell argument is rigorous by first partitioning \(\Phi\) into rectangles; the tails in each variable are geometric series, and the two roots in (3.7) are distinct. Thus every special integral belongs to
\((1-\beta q^{-1/2}X)^{-1}\mathbb C[X,X^{-1}]\).

For equality, take \(\Phi=1_{\mathcal O}\otimes1_{\mathcal O^\times}\). It satisfies (3.3), and its integral is exactly \((1-\beta q^{-1/2}X)^{-1}\). This proves the \(L\)-factor in (3.6).

The two-variable Fourier equation remains valid on the special subrepresentation, so its gamma factor is
\(\gamma(s,\tau\nu^{1/2})\gamma(s,\tau\nu^{-1/2})\). In the ramified case every relevant \(L\)-factor is one, giving
\[
\epsilon(s,\mathrm{St}\tau)
=\epsilon(s+1/2,\tau)\epsilon(s-1/2,\tau)
=\epsilon(s,\tau)^2.
\]
The last equality follows directly from the monomial (3.1). In the unramified case, divide the product gamma factor by the dual special \(L\)-factor and multiply by its standard \(L\)-factor. The result is
\[
\frac{1-\beta q^{1/2-s}}{1-\beta^{-1}q^{s-1/2}}
=-\beta q^{1/2-s}.
\]
This proves the sign and the exponent in (3.6). ∎

For \(\chi\circ\det\), the standard factors are defined through its Langlands quotient by the two character blocks \(\chi\nu^{-1/2},\chi\nu^{1/2}\) [Getz–Hahn 2022, §11.8]. Consequently
\[
\begin{aligned}
L(s,\chi\circ\det)&=L(s,\chi\nu^{-1/2})L(s,\chi\nu^{1/2}),\\
\epsilon(s,\chi\circ\det)&=\epsilon(s,\chi)^2.
\end{aligned}
\tag{3.8}
\]
The two norm shifts in the epsilon product cancel, also when \(\chi\) is ramified. No Whittaker integral for a one-dimensional representation is asserted.

## 4. Matching every pair with a character

**Theorem 4.1.** For every non-supercuspidal \(\pi\) in (1.1) and every character \(\xi\) of \(F^\times\), the analytic \(L\)- and epsilon factors of \(\pi\times\xi\) equal the parameter factors of \(R(\pi)\otimes\widehat\xi\).

**Proof.** The rank-two character-pair integral is the standard integral of \(\pi\otimes(\xi\circ\det)\), including its epsilon factor; this was proved in the local-factor lesson, Proposition 3.1. The nongeneric extension has the same twist identity by its defining character-block product. Thus insert \(\xi\) in all character labels in (3.4), (3.6) and (3.8).

On a direct sum of Weil characters, both factors are products of Tate factors by their definitions and one-dimensional reciprocity compatibility. This proves the principal-series and determinant-character cases.

Put \(\tau=\chi\xi\) for the special case. Its parameter has Weil characters \(\widehat{\tau\nu^{-1/2}},\widehat{\tau\nu^{1/2}}\), and its kernel is the second line. If \(\tau\) is unramified, Frobenius on that kernel has value \(\beta q^{-1/2}\), giving the \(L\)-factor in (3.6). The underlying Weil epsilon product is one. The monodromy correction, on the quotient by the kernel, is
\[
\det(-q^{-s}\Phi\mid V^{I_F}/(\ker N)^{I_F})
=-\beta q^{1/2-s}.
\tag{4.1}
\]
If \(\tau\) is ramified, the inertia-invariant space is zero, so the \(L\)-factor and correction are both one. The two underlying character epsilon factors multiply to \(\epsilon(s,\tau)^2\). This is exactly the ramified line of (3.6).

Finally, every additive character is \(\psi_a(x)=\psi(ax)\) for some \(a\ne0\). The analytic character-pair change is
\(\omega_\pi(a)\xi(a)^2|a|^{2(s-1/2)}\); the parameter change is its determinant at \(a\) times the same norm power. Proposition 2.1 identifies these determinants. Thus the match for conductor-zero \(\psi\) proves it for every \(\psi\). ∎

## 5. All non-supercuspidal rank-two pairs

The only pair that cannot be reduced immediately to character pairs is a pair of special representations. We compute it rather than inferring it from the existence of the correspondence.

**Lemma 5.1.** There is an isomorphism of Weil–Deligne objects
\[
S_2\otimes S_2\simeq S_3\oplus1.
\tag{5.1}
\]

**Proof.** Write \(e_{ab}=e_a\otimes e_b\). The three vectors
\[
e_{--},\quad e_{+-}+e_{-+},\quad2e_{++}
\]
form a monodromy chain with weights \(-1,0,1\). The remaining vector \(e_{+-}-e_{-+}\) has weight zero and monodromy zero. These four vectors form a basis over \(\mathbb C\), and the two indicated spaces are stable. ∎

**Theorem 5.2 (the special pair).** Let \(\eta=\chi\chi'\). For conductor-zero \(\psi\),
\[
\begin{array}{c|c|c}
&L(s,\mathrm{St}\chi\times\mathrm{St}\chi')&
\epsilon(s,\mathrm{St}\chi\times\mathrm{St}\chi',\psi)\\\hline
\eta\text{ unramified}&
\bigl((1-\beta X)(1-\beta q^{-1}X)\bigr)^{-1}&\beta^2qX^2\\
\eta\text{ ramified}&1&\epsilon(s,\eta,\psi)^4,
\end{array}
\tag{5.2}
\]
where \(\beta=\eta(\varpi)\). These factors equal those of the tensor product of the parameters in (1.2).

**Proof.** First assume \(\chi,\chi'\) unitary, so both special representations are tempered. The stated analytic gamma multiplicativity theorem gives
\[
\gamma(s,\mathrm{St}\chi\times\mathrm{St}\chi')
=\gamma(s-1,\eta)\gamma(s,\eta)^2\gamma(s+1,\eta).
\tag{5.3}
\]
For special pairs it is [Jacquet–Piatetski-Shapiro–Shalika 1983, Theorems 3.1 and 8.2, equation (14) in §8.2]. This is an analytic theorem about generic induction, available independently of LLC.

Tempered convergence says both \(L(s)\) and the dual \(L(s)\) are holomorphic for \(\operatorname{Re}(s)>0\) [Getz–Hahn 2022, Proposition 11.5.1]. If \(P(X)=L(s)^{-1}\), every root of \(P(q^{-s})\) therefore has \(\operatorname{Re}(s)\le0\). In that half-plane, the dual inverse factor at \(1-s\) is nonzero. The epsilon factor is a nonzero Laurent monomial. Hence the zeros of gamma in this half-plane, including multiplicities, are precisely the roots of \(P\), and determine \(P\) by its constant coefficient one.

For unramified \(\eta\), put \(Y=q^{s-1}\). Substitution of Tate's factors in (5.3) and cancellation gives
\[
\gamma(s)=\beta^2qX^2
\frac{(1-\beta X)(1-\beta q^{-1}X)}
     {(1-\beta^{-1}Y)(1-\beta^{-1}q^{-1}Y)}.
\tag{5.4}
\]
Since \(|\beta|=1\), the numerator roots have real parts zero and minus one, and the denominator roots have real parts one and two. The preceding zero criterion proves the first \(L\)-factor in (5.2). Dividing (5.4) by its \(L\)-ratio gives its epsilon factor \(\beta^2qX^2\).

For ramified \(\eta\), all four Tate \(L\)-factors are one. The four shifts \(-1,0,0,1\) in the epsilon monomials sum to zero, so (5.3) is the nonzero monomial \(\epsilon(s,\eta)^4\). It has no roots on \(\mathbb C^\times\). The zero criterion forces \(P=1\), proving the second line of (5.2) and its epsilon factor.

A smooth character can be written \(\chi=\chi_u\nu^t\) with \(\chi_u\) unitary and \(t\) real: its unit restriction has finite image, and one chooses \(t\) to remove the modulus of its uniformizer value. The pair integrals show that norm twisting the two factors shifts \(s\) by \(t+t'\). The functional equation gives the same shift for gamma and epsilon. Thus the unitary calculation proves (5.2) for arbitrary characters as well.

On the parameter side, Lemma 5.1 gives \(\widehat\eta S_3\oplus\widehat\eta\). For unramified \(\eta\), the kernel Frobenius values are \(\beta q^{-1}\) and \(\beta\). The monodromy quotient in the three-dimensional block has values \(\beta q\) and \(\beta\), so its correction is \(\beta^2qX^2\). All underlying unramified character epsilon factors are one. For ramified \(\eta\), all inertia invariants vanish; the underlying four character epsilon factors, with weights \(-1,0,0,1\), give \(\epsilon(s,\eta)^4\). These calculations match the two analytic cases. The change-of-additive-character formula has determinant \(\widehat\eta^4\) and dimension four on both sides, proving the match for every \(\psi\). ∎

**Corollary 5.3.** All pairs of non-supercuspidal rank-two irreducibles have matching \(L\)- and epsilon factors under (1.2).

**Proof.** A principal series or determinant character is the Langlands quotient with its two one-character blocks. The stated Langlands-quotient product theorem [Getz–Hahn 2022, §11.8] reduces its pair factors against any of the three types to the products of the corresponding character pairs. On the parameter side the same reduction is the distributivity of tensor product over direct sum and multiplicativity of the factors. Theorem 4.1 supplies every character pair. If both representations are special, use Theorem 5.2. These alternatives exhaust (1.1). ∎

For example, two unramified principal series with Frobenius values \(\alpha_1,\alpha_2\) and \(\beta_1,\beta_2\) have \(L\)-factor \(\prod_{i,j}(1-\alpha_i\beta_jX)^{-1}\) and epsilon factor one for conductor-zero \(\psi\). The spherical integral giving this factor was computed in the local-factor lesson, Theorem 2.2. In contrast, the untwisted Steinberg pair has conductor two, not four: its tensor monodromy kernel has dimension two.

## 6. Conductors, and the generic hypothesis

Write \(a_\epsilon(\pi)\) for the exponent of \(q^{-(s-1/2)}\) in the standard epsilon factor for conductor-zero \(\psi\). The Artin–Deligne definition is
\[
a(r,N)=a(r)+\dim V^{I_F}-\dim(\ker N)^{I_F}.
\tag{6.1}
\]

**Theorem 6.1.** The epsilon conductor is preserved on every representation in (1.1), with values
\[
\begin{aligned}
a_\epsilon(I(\mu_1,\mu_2))&=a(\mu_1)+a(\mu_2),\\
a_\epsilon(\mathrm{St}\chi)&=
 \begin{cases}1,&a(\chi)=0,\\2a(\chi),&a(\chi)>0,\end{cases}\\
a_\epsilon(\chi\circ\det)&=2a(\chi).
\end{aligned}
\tag{6.2}
\]
For the first two, which are generic, it is also the Casselman newvector conductor. A ramified determinant character has no nonzero Casselman newvector at any level.

**Proof.** The analytic exponents follow from (3.4), (3.6) and (3.8). On a sum of characters the Artin conductor is their conductor sum, and zero monodromy adds nothing. Norm twists are unramified and do not affect character conductors. On \(\widehat\chi S_2\), the underlying Artin conductor is \(2a(\chi)\). If \(\chi\) is unramified, the two-dimensional inertia-invariant space and one-dimensional kernel contribute one more in (6.1). If it is ramified, both invariant spaces are zero and the correction is zero. This proves (6.2) directly on the parameter side.

The generic newvector theorem states that the epsilon conductor is the least \(r\ge0\) for which \(V^{K_1(\mathfrak p^r)}\ne0\), and that this space is one-dimensional at the least level [Getz–Hahn 2022, Theorem 11.5.6]. Here
\[
K_1(\mathfrak p^r)=
\{g\in\mathrm{GL}_2(\mathcal O):g_{21}\in\mathfrak p^r,
                         \ g_{22}\equiv1\pmod{\mathfrak p^r}\}.
\tag{6.3}
\]
At \(r=0\) this means the full maximal compact subgroup. Apply the theorem to the two infinite-dimensional types in (1.1).

For the determinant character, \(\operatorname{diag}(u,1)\) belongs to (6.3) for every \(u\in\mathcal O^\times\) and every \(r\). If \(\chi\) is ramified, choose \(u\) with \(\chi(u)\ne1\). That element acts by a nontrivial scalar on the entire one-dimensional space, so no vector is fixed at any level. Thus the generic newvector theorem cannot be applied to this representation. Its well-defined epsilon conductor still equals its Artin–Deligne conductor \(2a(\chi)\). If \(\chi\) is unramified it is already maximal-compact invariant, with level zero. ∎

This example separates two notions that agree on generic representations. Replacing the epsilon conductor of a ramified determinant character by a nonexistent newvector level would give a false statement of conductor preservation.

**Proposition 6.2 (forced normalization).** Any family satisfying properties 1–5 of the correspondence agrees with (1.2) on all non-supercuspidals.

**Proof.** Its rank-one parameters are fixed by reciprocity. Pair-factor preservation against all characters gives the twisted standard \(L\)-profiles computed in Section 3. These recover the two Weil characters for principal series and determinant characters, and the single monodromy-kernel character for a special representation. The rank-two profile lemma in the correspondence-statement lesson, Lemma 3.2, then forces respectively zero monodromy or the centered special block with the indicated midpoint. Thus the candidate values are forced, including their norm twists. ∎

## 7. A weight-two form of level eleven

Consider the normalized newform
\[
f(z)=\eta(z)^2\eta(11z)^2
=q_z\prod_{m\ge1}(1-q_z^m)^2(1-q_z^{11m})^2,
\qquad q_z=e^{2\pi iz}.
\tag{7.1}
\]
The fact that it is the weight-two newform of level eleven with trivial character is an input from classical modular-form theory; the precise form, its eta expression and its associated elliptic-curve class are recorded in [LMFDB, newform orbit 11.2.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/). The associated class contains the curve \(y^2+y=x^3-x^2-10x-20\). Local–global compatibility is stated later in *Local–global compatibility for modular forms and elliptic curves*. The finite product in (7.1), truncated at degree eleven, computes
\[
a_2=-2,\quad a_3=-1,\quad a_5=1,\quad a_7=-2,\quad a_{11}=1.
\]

Use the unitary automorphic normalization. At \(p\ne11\), the two Satake values are the roots of
\[
T^2-\frac{a_p}{\sqrt p}T+1=0.
\tag{7.2}
\]
Thus the parameter has zero monodromy, trivial inertia and those two geometric-Frobenius values. For example, at \(p=2\) they are \((-1+i)/\sqrt2\) and \((-1-i)/\sqrt2\). Their sum is \(-\sqrt2\) and their product is one, giving
\(L(s)=(1+\sqrt2\,2^{-s}+2^{-2s})^{-1}\). At \(p=3\) the values are \((-1\pm i\sqrt{11})/(2\sqrt3)\); at \(5\) they are \((1\pm i\sqrt{19})/(2\sqrt5)\); at \(7\) they are \((-1\pm i\sqrt6)/\sqrt7\). These follow directly from (7.2).

At eleven the weight-two newform's local factor is \((1-a_{11}11^{-s-1/2})^{-1}\) in unitary normalization, of inverse-polynomial degree one. A supercuspidal has factor one by Proposition 4.2 of *The statement of the local Langlands correspondence*. The central character is trivial. Thus a principal series would have labels \(\mu,\mu^{-1}\), both ramified or both unramified, giving degree zero or two. A determinant character likewise has degree zero or two by (3.5). The classification therefore leaves a Steinberg twist \(\mathrm{St}_\chi\); degree one forces \(\chi\) unramified by (3.6). That formula makes \(\chi(11)=a_{11}=1\), so \(\chi=1\) and this local representation is \(\mathrm{St}_2\). Its parameter is \(S_2\), with conductor one and epsilon factor \(-11^{1/2-s}\).

The split multiplicative sign can also be checked directly on the curve. Its discriminant is \(-11^5\) and \(c_4=496\), so the reduction at eleven is multiplicative. Its singular point modulo eleven is \((5,5)\). In coordinates \(X=x-5,Y=y-5\), the quadratic tangent cone is \(Y^2-3X^2=(Y-5X)(Y+5X)\) over \(\mathbb F_{11}\). Both tangent directions are rational, so the reduction is split, explaining the sign \(a_{11}=1\). The unitary local Euler variable includes the half shift; omitting it would place the kernel on the wrong Weil line.

## 8. Exercises and complete solutions

**Exercise 8.1 (easy).** Compute the determinant of the parameter of \(\mathrm{St}\chi\).

**Solution.** Its two Weil characters are \(\widehat\chi\lVert\cdot\rVert^{-1/2}\) and \(\widehat\chi\lVert\cdot\rVert^{1/2}\), whose product is \(\widehat{\chi^2}\). Monodromy on the determinant is trace \(N=0\). The central character of the representation is \(\chi^2\), so these agree by reciprocity.

**Exercise 8.2 (medium).** Verify the epsilon-factor match for a ramified Steinberg twist, retaining its root number.

**Solution.** If \(a(\chi)=m>0\), write \(\epsilon(s,\chi)=w_\chi q^{-m(s-1/2)}\). The analytic two-variable functional equation gives the product at shifts \(\pm1/2\), hence
\(\epsilon(s,\mathrm{St}\chi)=w_\chi^2 q^{-2m(s-1/2)}\). On the parameter side inertia acts by the ramified scalar \(\widehat\chi\), so neither the full space nor its monodromy kernel has invariants. The correction is one, and the underlying Weil epsilon product is the same two shifted character factors. Their product has exactly the displayed root number \(w_\chi^2\), not just the same conductor exponent.

**Exercise 8.3 (medium).** Compute the parameter conductor of a Steinberg twist from the ramification definition, and explain why the nongeneric analogue of a newvector assertion fails.

**Solution.** At each ramification group the two Weil summands are the same scalar character, because norm twists restrict trivially to inertia. Their invariant codimensions are therefore twice those of the character; summing the Artin-conductor terms gives \(a(r)=2a(\chi)\). For an unramified character, (6.1) adds \(2-1=1\); for a ramified character it adds \(0-0=0\). This gives one or \(2a(\chi)\), respectively. A ramified \(\chi\circ\det\), by contrast, has parameter conductor \(2a(\chi)\) and no monodromy, but \(\operatorname{diag}(u,1)\in K_1(\mathfrak p^r)\) acts nontrivially for some unit \(u\), at every \(r\). Its Casselman level is consequently nonexistent.

**Exercise 8.4 (hard).** Verify every factor of the untwisted Steinberg pair directly, including its conductor and monodromy decomposition.

**Solution.** The four basis vectors in Lemma 5.1 split the tensor into a length-three chain and a weight-zero singleton. Its monodromy kernel has Frobenius values \(q^{-1}\) and one, giving
\(L(s)=((1-q^{-s})(1-q^{-s-1}))^{-1}\). The quotient by that kernel has values \(q\) and one, giving epsilon correction \(q^{1-2s}\). The underlying Weil action is unramified, so its epsilon product is one and its Artin conductor is zero; formula (6.1) gives \(4-2=2\). Analytically, (5.3) is the product of the Tate gamma factors at \(s-1,s,s,s+1\). Its simplified expression (5.4), with \(\beta=1\), has zeros exactly at the two displayed Euler roots in the nonpositive half-plane. Tempered convergence forces the same \(L\)-factor, and then gamma's defining ratio forces \(\epsilon=q^{1-2s}\). This verifies both analytic factors independently of an appeal to LLC. The complete Iwahori integral computing a Laurent multiple of this \(L\)-factor is in the local-factor lesson, equation (5.5).

## What this lesson does not prove

The rank-two representation classification and the normalized-induction duality statement are prerequisites [Jacquet–Langlands 1970, Theorem 3.3; Getz–Hahn 2022, §8.2]. The Schwartz realization, its Fourier/Weyl action and its special-subspace description used in Section 3 are [Jacquet–Langlands 1970, Proposition 3.2, the zeta identities in the proof of Proposition 3.5, and the realization assertion of Proposition 3.6]. Tate's character functional equation and reciprocity compatibility are inputs, as are the Artin–Deligne factor definitions. Sections 3–4 compute the resulting rank-two factors and prove their match.

The analytic special-pair gamma multiplicativity theorem in (5.3) is stated with its exact locator there. Tempered convergence is [Getz–Hahn 2022, Proposition 11.5.1]. The general Langlands-quotient factor product rule, including ramified principal-series pairs, is [Getz–Hahn 2022, §11.8]. Theorem 5.2 proves the complete special-pair factor match from those analytic inputs and explicit linear algebra. The generic newvector theorem is [Getz–Hahn 2022, Theorem 11.5.6], or the prerequisite *Local newforms and the conductor*. We apply its generic hypothesis explicitly. The classical modular-form identity and its automorphic local-component interpretation in Section 7 are prerequisites; local–global compatibility is stated in the later modular-form lesson. No general existence theorem for LLC is proved or used in the factor matching here.

## References

- [Jacquet–Langlands 1970] Hervé Jacquet and Robert P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, Springer, 1970, §§2–3, especially Theorem 2.18 and Propositions 3.2, 3.5–3.6, Corollary 3.7.
- [Deligne 1973] Pierre Deligne, “[Formes modulaires et représentations de GL(2)](https://publications.ias.edu/sites/default/files/Number21.pdf),” in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349, Springer, 1973, 55–105, §§3.2.2–3.2.6. The unitary normalization is §3.2.3; its newvector property concerns infinite-dimensional representations.
- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§8.2, 11.5, 11.8 and 12.4. Published as Graduate Texts in Mathematics 300, Springer, 2024; numbering here refers to the draft.
- [Jacquet–Piatetski-Shapiro–Shalika 1983] Hervé Jacquet, Ilya I. Piatetski-Shapiro and Joseph A. Shalika, “[Rankin–Selberg convolutions](https://www.math.columbia.edu/~hj/Rankin%20Selberg%20convolutions.pdf),” *American Journal of Mathematics* 105 (1983), 367–464, Theorems 3.1 and 8.2 and equation (14) of §8.2.
- [LMFDB] The L-functions and Modular Forms Database, [newform orbit 11.2.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/), Properties, Related objects, q-expansion and Expression as an eta quotient. The coefficients used here were also computed directly from the product and checked by finite-field point counts.
