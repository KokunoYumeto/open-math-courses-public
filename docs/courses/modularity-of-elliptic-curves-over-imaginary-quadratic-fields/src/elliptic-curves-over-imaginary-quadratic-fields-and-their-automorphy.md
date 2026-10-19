# Elliptic curves over imaginary quadratic fields and their automorphy

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An elliptic curve \(E\) over \(\mathbb Q\) is modular: there is a weight-two newform whose Hecke eigenvalue at each prime \(\ell\) of good reduction is \(\ell+1-\#E(\mathbb F_\ell)\). Wiles and Taylor–Wiles proved this for semistable curves in 1995, and Breuil, Conrad, Diamond and Taylor extended it to all curves in 2001. Over an imaginary quadratic field \(K\) the corresponding objects are automorphic representations of \(\mathrm{GL}_2(\mathbb A_K)\) that occur in the cohomology of arithmetic groups such as \(\mathrm{SL}_2(\mathcal O_K)\) acting on hyperbolic three-space. This course proves that every elliptic curve over every imaginary quadratic field is modular in this sense, with the expected local behaviour at every place.

The proof was found by OpenAI in 2026 [OpenAI-030]. It uses a lifting theorem and a modularity criterion of Caraiani and Newton [CN], taken here without proof, together with a new geometric construction: a cyclic cover of a twist of the given curve whose cohomology contains a chain of congruences. The chain leads from an auxiliary elliptic curve, which the criterion of Caraiani and Newton shows to be modular, to the given curve.

This lesson fixes the conventions, states the theorem, states the results taken from the literature, and describes the route of the proof.

**Prerequisites.** [*Modularity lifting: the Taylor–Wiles method in outline*](course:LG-GLOB/LG-GLOB-11), for the idea of lifting automorphy from a residual representation. From *Galois representations*: [*The ℓ-adic Tate module of an elliptic curve*](course:LG-GAL/the-adic-tate-module-of-an-elliptic-curve); [*Weil–Deligne representations and Grothendieck’s monodromy theorem*](course:LG-GAL/weil-deligne-representations-and-monodromy), Theorem 2.2; [*Frobenius elements and determination by traces*](course:LG-GAL/frobenius-elements-and-determination-by-traces), Theorems 3.1 and 4.2; [*Residual representations and Serre's modularity theorem*](course:LG-GAL/residual-representations-and-serre-modularity), Lemma 1.2 and Proposition 3.1; [*p-adic Hodge theory and the Fontaine–Mazur conjecture*](course:LG-GAL/p-adic-hodge-theory-and-the-fontaine-mazur-conjecture). From *The local Langlands correspondence*: [*The rank-two correspondence: principal series, Steinberg twists and characters*](course:LG-LLC/LG-LLC-06). From *Automorphic forms and representations of GL₂*: [*Real and complex representations: weights, gamma factors and classical forms*](course:automorphic-forms-and-representations-of-gl2/real-and-complex-representations-weights-gamma-factors-and-classical-forms), Section 8.

## 1. Galois representations

Throughout, \(L\) is a number field with algebraic closure \(\overline L\) and absolute Galois group \(G_L=\operatorname{Gal}(\overline L/L)\). For each finite place \(v\) we fix an embedding \(\overline L\hookrightarrow\overline{L_v}\); it identifies \(G_{L_v}\) with a decomposition group in \(G_L\). Frobenius elements \(\operatorname{Frob}_v\) are geometric. For a prime \(\ell\), the \(\ell\)-adic cyclotomic character is \(\epsilon_\ell\colon G_L\to\mathbb Z_\ell^\times\). In this course \(\epsilon_\ell\) has Hodge–Tate weight \(-1\).

**Cohomology through Tate modules.** For an abelian variety \(A/L\) of dimension \(g\), the Tate module \(T_\ell A=\varprojlim_kA[\ell^k](\overline L)\) is free of rank \(2g\) over \(\mathbb Z_\ell\), with a continuous action of \(G_L\). Put
\[
\begin{gathered}
H^1(A,\mathbb Z_\ell)=\operatorname{Hom}_{\mathbb Z_\ell}(T_\ell A,\mathbb Z_\ell),\\
H^1(A)=H^1(A,\mathbb Z_\ell)\otimes_{\mathbb Z_\ell}\overline{\mathbb Q}_\ell ,
\end{gathered}
\]
with \(G_L\) acting by \((\sigma x)(t)=x(\sigma^{-1}t)\). For a smooth projective geometrically connected curve \(C/L\) with Jacobian \(J\) we put \(H^1(C)=H^1(J)\). An endomorphism \(\alpha\) of \(A\) defined over \(L\) acts on \(T_\ell A\) by \(\alpha_*\) and on \(H^1(A)\) by \(\alpha^*x=x\circ\alpha_*\); these actions commute with \(G_L\). For an elliptic curve the Weil pairing identifies \(\wedge^2T_\ell E\) with \(\mathbb Z_\ell(1)\), so
\[
\det H^1(E)=\epsilon_\ell^{-1}.
\]
By the Hodge–Tate decomposition of \(V_\ell E\), the representation \(H^1(E)\) has labelled Hodge–Tate weights \(\{0,1\}\) at every place above \(\ell\) and every embedding.

**Residual representations.** Let \(r\colon G_L\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)\) be continuous. Its image lies in \(\mathrm{GL}_n\) of a finite extension of \(\mathbb Q_\ell\), and by compactness \(r\) preserves a lattice over the ring of integers of that extension. We write \(\bar r\colon G_L\to\mathrm{GL}_n(\overline{\mathbb F}_\ell)\) for the semisimplification of the reduction of such a lattice. It does not depend on the lattice: its characteristic polynomials are the reductions of those of \(r\), and these determine a semisimple representation by the characteristic-polynomial form of the Brauer–Nesbitt theorem (Lemma 1.2 of [*Residual representations and Serre's modularity theorem*](course:LG-GAL/residual-representations-and-serre-modularity)).

**Lemma 1.1.** If \(\bar r\) is absolutely irreducible, then \(r\) is absolutely irreducible.

**Proof.** Suppose \(r\otimes\overline{\mathbb Q}_\ell\) has a proper nonzero invariant subspace \(W\). Choose an invariant lattice \(\Lambda\) over the ring of integers \(\mathcal O\) of a finite extension containing the field of definition of \(W\). Then \(\Lambda\cap W\) is an invariant saturated sublattice of rank \(\dim W\), and its reduction is a proper nonzero invariant subspace of \(\Lambda/\mathfrak m\Lambda\). Hence \(\Lambda/\mathfrak m\Lambda\) has at least two Jordan–Hölder constituents, and so does \(\bar r\). \(\square\)

Lemma 1.1 is used repeatedly in Lesson 8: an \(\ell\)-adic representation with absolutely irreducible residual representation is semisimple, and two such representations with the same characteristic polynomials of Frobenius on a density-one set of places are isomorphic (Theorem 4.2 of [*Frobenius elements and determination by traces*](course:LG-GAL/frobenius-elements-and-determination-by-traces)).

**Local conditions at \(\ell\).** For a place \(v\mid\ell\), a representation of \(G_{L_v}\) on a finite-dimensional \(\overline{\mathbb Q}_\ell\)-vector space is *potentially semistable* or *potentially crystalline* if it becomes semistable or crystalline on \(G_{L'}\) for a finite extension \(L'/L_v\); its labelled Hodge–Tate weights are defined through \(\mathbb C_\ell\)-periods as in [*p-adic Hodge theory and the Fontaine–Mazur conjecture*](course:LG-GAL/p-adic-hodge-theory-and-the-fontaine-mazur-conjecture). A two-dimensional representation of \(G_{L_v}\) is *potentially ordinary of weight zero* if, after restriction to some finite extension, it has an invariant line on which the group acts by an unramified character, and the quotient is \(\epsilon_\ell^{-1}\) times an unramified character. For \(H^1\) of an elliptic curve with good ordinary reduction this is the dual of the connected–étale sequence of its \(\ell\)-divisible group.

**Definition 1.2 (decomposed genericity, [CN, Definition 2.1.27]).** A continuous \(\bar r\colon G_L\to\mathrm{GL}_2(\overline{\mathbb F}_\ell)\) is *decomposed generic* if there is a rational prime \(q\ne\ell\) that splits completely in \(L\) such that for every place \(v\mid q\) of \(L\) the representation \(\bar r\) is unramified at \(v\) and the eigenvalues \(\alpha_v,\beta_v\) of \(\bar r(\operatorname{Frob}_v)\) satisfy \(\alpha_v/\beta_v\ne q\) and \(\beta_v/\alpha_v\ne q\) in \(\overline{\mathbb F}_\ell\).

**Lemma 1.3.** If \(q\equiv1\pmod\ell\), the eigenvalue condition at \(v\) says exactly that \(\alpha_v\ne\beta_v\).

**Proof.** The image of \(q\) in \(\overline{\mathbb F}_\ell\) is \(1\), and \(\alpha_v/\beta_v\ne1\) is equivalent to \(\beta_v/\alpha_v\ne1\) and to \(\alpha_v\ne\beta_v\). \(\square\)

In Lesson 7 every decomposed-generic prime is chosen with \(q\equiv1\pmod\ell\), so only distinct Frobenius eigenvalues at all places above \(q\) have to be arranged.

## 2. Automorphic representations and their Galois representations

A *CM field* is a totally imaginary quadratic extension of a totally real field. Imaginary quadratic fields are CM, and so is every abelian extension of \(\mathbb Q\) that is not totally real (Exercise 6.1).

Let \(L\) be a CM field and \(\pi\) a cuspidal automorphic representation of \(\mathrm{GL}_2(\mathbb A_L)\). Every archimedean place \(v\) of \(L\) is complex, with \(L_v\cong\mathbb C\). We say that \(\pi\) is *regular algebraic of weight zero* if at each archimedean place \(\pi_v\) has the infinitesimal character of the trivial representation of \(\mathrm{GL}_2(\mathbb C)\), regarded as a real Lie group. A representation of \(\mathrm{PGL}_2(\mathbb A_L)\) is one of \(\mathrm{GL}_2(\mathbb A_L)\) with trivial central character.

**Lemma 2.1.** If \(\pi\) is regular algebraic of weight zero and \(v\) is archimedean, then \(\pi_v\) is the irreducible principal series whose Langlands parameter \(W_{\mathbb C}=\mathbb C^\times\to\mathrm{GL}_2(\mathbb C)\) is
\[
z\longmapsto\begin{pmatrix}z/|z|&0\\0&\bar z/|z|\end{pmatrix}.
\tag{2.1}
\]

**Proof.** Local components of cuspidal representations of \(\mathrm{GL}_2\) are generic, that is, they have Whittaker models: the global Whittaker function of a cusp form factors through local Whittaker models, as in the proof of [JL, Theorem 11.1]. By the classification of irreducible admissible representations of \(\mathrm{GL}_2(\mathbb C)\) and of their Whittaker models in Section 8 of [*Real and complex representations*](course:automorphic-forms-and-representations-of-gl2/real-and-complex-representations-weights-gamma-factors-and-classical-forms), the representations with the infinitesimal character of the trivial representation are the trivial representation and the principal series induced from the characters \(z\mapsto z/|z|\) and \(z\mapsto\bar z/|z|\). Write a character of \(\mathbb C^\times\) as \(z\mapsto z^a\bar z^b\) with \(a-b\in\mathbb Z\). The first character has \((a,b)=(\frac12,-\frac12)\) and the second \((-\frac12,\frac12)\), which is the infinitesimal character \(\rho\) of the trivial representation (Exercise 6.4). Only the principal series is generic. \(\square\)

**Tate normalization.** For a finite place \(v\) let \(\operatorname{rec}_{L_v}\) be the local Langlands correspondence for \(\mathrm{GL}_2(L_v)\), normalized so that uniformizers correspond to geometric Frobenius elements. We put
\[
\begin{aligned}
&\operatorname{rec}^T_{L_v}(\pi_v)\\
&\quad=\operatorname{rec}_{L_v}\bigl(\pi_v\otimes|\det|_v^{-1/2}\bigr).\quad(2.2)
\end{aligned}
\]
At a complex place the same twist turns (2.1) into \(z\mapsto\operatorname{diag}(\bar z^{-1},z^{-1})\), the parameter of Hodge types \((1,0)\) and \((0,1)\).

**Theorem 2.2 (named result N2: Galois representations of weight-zero cuspidal representations).** Let \(L\) be a CM field, \(\pi\) a cuspidal automorphic representation of \(\mathrm{GL}_2(\mathbb A_L)\) that is regular algebraic of weight zero, \(\ell\) a prime and \(\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C\) an isomorphism. There is a continuous semisimple representation
\[
r_\iota(\pi)\colon G_L\longrightarrow\mathrm{GL}_2(\overline{\mathbb Q}_\ell),
\]
unique up to isomorphism, such that for every finite place \(v\nmid\ell\) of \(L\)
\[
\begin{aligned}
&\mathrm{WD}\bigl(r_\iota(\pi)|_{G_{L_v}}\bigr)^{\mathrm{ss}}\\
&\quad\cong\iota^{-1}\operatorname{rec}^T_{L_v}(\pi_v)^{\mathrm{ss}} .\quad(2.3)
\end{aligned}
\]
Moreover \(r_\iota(\pi)\) is unramified at every \(v\nmid\ell\) at which \(\pi_v\) is unramified, and there the characteristic polynomial of \(r_\iota(\pi)(\operatorname{Frob}_v)\) is \(\iota^{-1}\) of that of \(\operatorname{rec}^T_{L_v}(\pi_v)(\operatorname{Frob}_v)\).

Existence with (2.3) at the places where \(\pi_v\) and \(L_v\) are unramified is due to Harris, Lan, Taylor and Thorne [HLTT, Theorem 1 of the introduction, proved as Corollary 7.14] and to Scholze [Sch, Corollary V.4.2], and (2.3) at all \(v\nmid\ell\) is Varma's Theorem 1\(^{\mathrm{ss}}\) [Var]. Unramifiedness at a place where \(\pi_v\) is unramified but \(L_v\) is ramified follows from Varma's Theorem 1, which bounds the monodromy of \(r_\iota(\pi)|_{G_{L_v}}\) by that of \(\operatorname{rec}^T_{L_v}(\pi_v)\); the semisimplified statement (2.3) alone would allow a nilpotent monodromy operator. Uniqueness follows from the Chebotarev density theorem and the Brauer–Nesbitt theorem, since \(r_\iota(\pi)\) is semisimple. The course uses Theorem 2.2 without proof.

**Definition 2.3.** A continuous \(r\colon G_L\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)\) is *realized* by \(\pi\) (with respect to \(\iota\)) if \(r\cong r_\iota(\pi)\).

At a place \(v\mid\ell\) Caraiani and Newton use a Hecke-theoretic condition called *\(\iota\)-ordinarity of weight zero* [CN, Theorem 5.2]: at sufficiently deep level at \(v\), suitably normalized \(U_v\)-operators have an eigenvector with \(\iota\)-adic unit eigenvalues. The course uses this notion only through the statements of Section 4, so its precise definition plays no further role.

## 3. The theorem

**Theorem 3.1 (modularity over imaginary quadratic fields).** Let \(K\) be an imaginary quadratic field and \(E/K\) an elliptic curve. There is an isobaric automorphic representation \(\pi_E\) of \(\mathrm{GL}_2(\mathbb A_K)\) with trivial central character and weight zero such that, for every prime \(\ell\) and every isomorphism \(\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C\),
\[
r_\iota(\pi_E)\cong H^1(E),
\]
and at every finite place \(v\nmid\ell\)
\[
\iota\,\mathrm{WD}\bigl(H^1(E)|_{G_{K_v}}\bigr)^{\mathrm{F\text{-}ss}}\cong\operatorname{rec}^T_{K_v}(\pi_{E,v}),
\]
where F-ss denotes Frobenius semisimplification. The parameter of \(\pi_E\) at the complex place is (2.1), and
\[
L(E/K,s)=L(\pi_E,s-\tfrac12).
\]
If \(E\) has no complex multiplication, \(\pi_E\) is cuspidal. If \(E\) has complex multiplication by an imaginary quadratic field \(M\), then \(\pi_E\) is the automorphic induction of a Hecke character of \(KM\) when \(M\ne K\), and an isobaric sum of two Hecke characters of \(K\) when \(M=K\).

For an isobaric sum \(\chi_1\boxplus\chi_2\) of Hecke characters, \(r_\iota\) denotes the sum of the Galois characters of \(\chi_1\) and \(\chi_2\), Tate-normalized in the same way. The \(L\)-function identity is a restatement of the local statements. At a finite place where \(E\) has good reduction, the Euler factor of \(E\) is \(\det\bigl(1-\operatorname{Frob}_vNv^{-s}\mid H^1(E)\bigr)^{-1}\), and that of \(\pi_{E,v}\otimes|\det|_v^{-1/2}\) at \(s\) is that of \(\pi_{E,v}\) at \(s-\frac12\) (Exercise 6.3); bad places and the archimedean place are treated in the same way with the full parameters. For non-CM \(E\), the theory of \(L\)-functions of cuspidal representations of \(\mathrm{GL}_2\) [JL] therefore shows that \(L(E/K,s)\) extends to an entire function with a functional equation relating \(s\) and \(2-s\).

## 4. Results used without proof

The decisive inputs are three results of Caraiani and Newton. The course uses them in the following specialized forms; the numbering is that of the third arXiv version of [CN].

**Theorem 4.1 (named result N1a: lifting theorem, [CN, Theorem 5.2]).** Let \(L\) be a CM field and \(\ell\) an odd prime with \(\ell\ne5\). Let \(r\colon G_L\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)\) be continuous, unramified outside finitely many places, with \(\det r=\epsilon_\ell^{-1}\). Suppose that \(r|_{G_{L_v}}\) is potentially semistable with labelled Hodge–Tate weights \(\{0,1\}\) for every \(v\mid\ell\), that \(\bar r\) is decomposed generic, and that \(\bar r|_{G_{L(\zeta_\ell)}}\) is absolutely irreducible. Suppose that a cuspidal representation \(\pi\) of \(\mathrm{PGL}_2(\mathbb A_L)\), regular algebraic of weight zero, satisfies \(\overline{r_\iota(\pi)}\cong\bar r\) for some \(\iota\), and that at each \(v\mid\ell\) one of the following holds:

1. \(r|_{G_{L_v}}\) and \(r_\iota(\pi)|_{G_{L_v}}\) are both potentially crystalline, one is potentially ordinary of weight zero if and only if the other is, and \(\operatorname{rec}_{L_v}(\pi_v)\) has zero monodromy;
2. neither \(r|_{G_{L_v}}\) nor \(r_\iota(\pi)|_{G_{L_v}}\) is potentially crystalline, and \(\pi\) is \(\iota\)-ordinary of weight zero at \(v\).

Then \(r\cong r_\iota(\Pi)\) for a cuspidal representation \(\Pi\) of \(\mathrm{PGL}_2(\mathbb A_L)\) that is regular algebraic of weight zero.

In [CN] the theorem is stated for every odd \(\ell\); for \(\ell=5\) it carries one further condition on the projective image of \(\bar r\), which the course never needs. Its local hypotheses are slightly weaker than (1) and (2). The determinant condition \(\epsilon_\ell^{-1}\) allows \(\ell=3\) with residual image \(\mathrm{SL}_2(\mathbb F_3)\) [CN, Remark 5.2.2].

**Theorem 4.2 (named result N1b: elliptic starting point, [CN, Theorem 6.1]).** Let \(L\) be a CM field with \(\zeta_5\notin L\) and \(A/L\) an elliptic curve without complex multiplication. If the mod-\(5\) representation of \(A\) is decomposed generic and absolutely irreducible on \(G_{L(\zeta_5)}\), then \(H^1(A)\) is realized by a cuspidal representation of \(\mathrm{PGL}_2(\mathbb A_L)\) that is regular algebraic of weight zero.

[CN] state this with the Tate module in place of \(H^1\); the two are dual, and duality preserves absolute irreducibility and decomposed genericity of two-dimensional residual representations, since it replaces the eigenvalues of each \(\bar r(\operatorname{Frob}_v)\) by their inverses.

**Theorem 4.3 (named result N1c: modular elliptic curves, [CN, Lemma 6.1.3]).** Let \(L\) be a CM field and \(D/L\) an elliptic curve without complex multiplication. If a cuspidal regular algebraic representation \(\pi\) of \(\mathrm{GL}_2(\mathbb A_L)\) realizes \(H^1(D)\) for one prime \(\ell\) and one \(\iota\), then \(\pi\) has weight zero and trivial central character, realizes \(H^1(D)\) for every prime and every \(\iota\), and
\[
\begin{aligned}
&\iota\,\mathrm{WD}\bigl(H^1(D)|_{G_{L_v}}\bigr)^{\mathrm{F\text{-}ss}}\\
&\quad\cong\operatorname{rec}^T_{L_v}(\pi_v)\qquad(v\nmid\ell).
\end{aligned}
\]
If \(D\) has potentially multiplicative reduction at \(v\mid\ell\), then \(\pi\) is \(\iota\)-ordinary of weight zero at \(v\). Moreover, the proof of [CN, Lemma 6.1.3(4)] shows: if \(\pi\) is cuspidal, regular algebraic of weight zero with trivial central character, and \(\pi_v\) is a twist of the Steinberg representation by a character of order at most two, then \(\pi\) is \(\iota\)-ordinary of weight zero at \(v\).

The remaining results taken from the literature are listed here with the lesson where each is used; they are stated in full there.

| Named result | Content | Used in |
|---|---|---|
| N2 | Theorem 2.2 | Lesson 8 |
| N3 | cyclic base change for \(\mathrm{GL}_2\), strong multiplicity one, quadratic automorphic induction | Lesson 8 |
| N4 | Serre's open image theorem | Lessons 5 and 7 |
| N5 | Hilbert's irreducibility theorem in the counting form of Cohen and Serre | Lesson 7 |
| N6 | Raynaud's theorem on the Picard functor of a regular model | Lesson 3 |
| N7 | comparison theorems of \(p\)-adic Hodge theory for abelian varieties | Lessons 5 and 6 |
| N8 | Grothendieck's theory of semistable abelian varieties and Raynaud's uniformization | Lesson 6 |
| N9 | the main theorem of complex multiplication | Lesson 8 |
| N10 | Weil pairings, characteristic polynomials and good reduction of abelian varieties; Weil's theorem over finite fields; Jacobians of families of curves | Lessons 5, 6 and 7 |

## 5. The route of the proof

The CM case is a consequence of the theory of complex multiplication and is treated in Lesson 8. Let \(E/K\) have no complex multiplication. By Serre's open image theorem there is a prime \(p>100\) such that the image of \(G_K\) on \(E[p]\) contains \(\mathrm{SL}_2(\mathbb F_p)\). Put
\[
n=3p,\qquad F=K(\mu_n).
\]
The field \(F\) is CM, abelian over \(\mathbb Q\), and does not contain \(\zeta_5\) (Exercise 6.1).

Write \(E\colon y^2=h(x)\). For a parameter \(t\) with \(h(t)\ne0\) let \(B_t\colon h(t)y^2=h(x)\) be the quadratic twist of \(E\) by \(h(t)\); it carries the point \(R_t=(t,1)\). Lesson 2 constructs a smooth projective curve \(C_n(t)\) of genus \(n\) with a cyclic cover \(C_n(t)\to B_t\) of degree \(n\), branched over the two points \(\pm[n]R_t\), together with an involution inverting the deck transformations. For each character \(\theta\colon\mu_n\to\overline{\mathbb Q}^\times\), the \(\theta\)-eigenspace of the deck group in \(H^1(C_n(t))\) is a two-dimensional representation \(V_\theta\) of \(G_F\) with determinant \(\epsilon_\ell^{-1}\) and Hodge–Tate weights \(\{0,1\}\) (Lesson 5). Choose characters \(\eta\) of order \(3\) and \(\psi\) of order \(p\) and put \(\chi=\eta\psi\). Then \(V_1=H^1(B_t)\), and \(V_\eta=H^1(A_t)\) for an elliptic curve \(A_t\) over \(F\). Because the first homology of \(C_n(t)\) is a free module over the integral group ring of \(\mu_n\) (Lesson 4), characters that agree modulo \(\ell\) give the same residual representation, and Lesson 5 obtains
\[
\begin{aligned}
H^1(A_t)&=V_\eta\ \overset{p}{\equiv}\ V_\chi\ \overset{3}{\equiv}\ V_\psi\\
&\overset{p}{\equiv}\ V_1=H^1(B_t),\quad(5.1)
\end{aligned}
\]
where \(\overset{\ell}{\equiv}\) means equal residual representations at \(\ell\). The order-\(p\) part of a character becomes trivial modulo \(p\), and the order-\(3\) part modulo \(3\).

Lessons 6 and 7 choose one parameter \(t\in K\) for which every step can be applied: the local reduction type of the Jacobian of \(C_n(t)\) at the places above \(3p\) is that of \(E^n\), uniformly in \(\theta\) (Lesson 6), and the residual representations needed below are absolutely irreducible over the relevant cyclotomic fields and decomposed generic, while \(A_t\) has no complex multiplication (Lesson 7). Lesson 8 then argues as follows.

- \(A_t\) is modular over \(F\) by Theorem 4.2, applied at the prime \(5\).
- Theorem 4.1 moves automorphy along (5.1): from \(V_\eta\) to \(V_\chi\) at \(p\), from \(V_\chi\) to \(V_\psi\) at \(3\), and from \(V_\psi\) to \(V_1\) at \(p\). Before each step, automorphy is transported to the coefficient prime of that step, and the local conditions at that prime are verified on the automorphic side.
- \(F/K\) is abelian, and cyclic base change carries the automorphy of \(B_t\) down a tower of cyclic extensions of prime degree from \(F\) to \(K\).
- \(B_t\) is the quadratic twist of \(E\) by \(h(t)\), so twisting by the corresponding quadratic Hecke character gives \(\pi_E\); Theorem 4.3 gives the local statements.

The lessons follow this order: the curves (Lesson 2), their degenerations (Lesson 3), integral homology and monodromy (Lesson 4), the rank-two systems and the congruences (Lesson 5), local reduction types (Lesson 6), residual properties and the choice of \(t\) (Lesson 7), and the propagation of automorphy (Lesson 8).

## 6. Exercises

**6.1.** Let \(K\) be imaginary quadratic, \(p>5\) a prime and \(F=K(\mu_{3p})\). Show that \(F/\mathbb Q\) is abelian, that every field \(L\) with \(K\subseteq L\subseteq F\) is a CM field, and that \(\zeta_5\notin F\).

**6.2.** Let \(r\colon G_L\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)\) be continuous with \(\bar r\) absolutely irreducible, and let \(r'\) be semisimple with the same characteristic polynomials of \(\operatorname{Frob}_v\) for all \(v\) outside a finite set. Show that \(r\cong r'\).

**6.3.** Let \(v\) be a finite place of \(L\) with residue field of order \(Nv\), and let \(\sigma=\operatorname{rec}_{L_v}(\pi_v)\) be unramified with \(\sigma(\operatorname{Frob}_v)\) of eigenvalues \(\alpha,\beta\). Show that \(L(\pi_v\otimes|\det|_v^{-1/2},s)=L(\pi_v,s-\frac12)\), and that if \(\operatorname{rec}^T_{L_v}(\pi_v)\) is the parameter of \(H^1(E)\) for an elliptic curve \(E\) with good reduction at \(v\), then \(L(\pi_v,s-\frac12)\)\(=(1-a_vNv^{-s}+Nv^{1-2s})^{-1}\) with \(a_v=Nv+1-\#\widetilde E(k_v)\).

**6.4.** The trivial representation of \(\mathrm{GL}_2(\mathbb C)\) has infinitesimal character given, for the holomorphic and the antiholomorphic factor of the complexified Lie algebra, by \(\rho=(\frac12,-\frac12)\) up to the Weyl group. Show that the principal series induced from \(z\mapsto z^{a_1}\bar z^{b_1}\) and \(z\mapsto z^{a_2}\bar z^{b_2}\) has the infinitesimal character \((a_1,a_2)\) and \((b_1,b_2)\), and deduce that the characters \(z/|z|\) and \(\bar z/|z|\) of Lemma 2.1 give the infinitesimal character of the trivial representation.

## 7. Solutions

**6.1.** \(K/\mathbb Q\) and \(\mathbb Q(\mu_{3p})/\mathbb Q\) are abelian, and so is their compositum \(F\). An abelian extension \(L/\mathbb Q\) inside \(\mathbb C\) is stable under complex conjugation \(c\), and \(c|_L\) is a central element of \(\operatorname{Gal}(L/\mathbb Q)\) of order at most two; it is independent of the complex embedding because every embedding differs from a fixed one by an element of the abelian Galois group, which commutes with \(c\). If \(L\supseteq K\), then \(c|_L\ne1\), the fixed field \(L^+\) of \(c|_L\) has index two, and every embedding of \(L^+\) is real because \(c\) fixes it. So \(L\) is a totally imaginary quadratic extension of the totally real field \(L^+\). For \(\zeta_5\): the extension \(\mathbb Q(\mu_{3p})/\mathbb Q\) is unramified at \(5\) because \(5\nmid3p\), so the ramification index of \(5\) in \(F\) is at most \([K:\mathbb Q]=2\). In \(\mathbb Q(\zeta_5)\) the prime \(5\) is totally ramified of index \(4\), and ramification indices are multiplicative in towers, so a field containing \(\zeta_5\) has ramification index at \(5\) divisible by \(4\).

**6.2.** By Lemma 1.1, \(r\) is absolutely irreducible, hence semisimple. By the Chebotarev density theorem the Frobenius elements outside a finite set are dense in \(G_L\), so \(r\) and \(r'\) have the same characteristic polynomial at every element of \(G_L\) by continuity. Two semisimple representations over a field of characteristic zero with the same characteristic polynomials are isomorphic (Theorem 4.2 of [*Frobenius elements and determination by traces*](course:LG-GAL/frobenius-elements-and-determination-by-traces)).

**6.3.** For an unramified parameter, \(L(\pi_v,s)\)\(=\bigl((1-\alpha Nv^{-s})(1-\beta Nv^{-s})\bigr)^{-1}\). Twisting by \(|\det|_v^{-1/2}\) multiplies the image of a uniformizer by \(|\varpi_v|_v^{-1/2}=Nv^{1/2}\), and a uniformizer corresponds to geometric Frobenius, so the eigenvalues become \(\alpha Nv^{1/2}\) and \(\beta Nv^{1/2}\). Hence \(L(\pi_v\otimes|\det|_v^{-1/2},s)\)\(=\prod(1-\alpha Nv^{1/2-s})^{-1}\)\(=L(\pi_v,s-\frac12)\). If these eigenvalues are those of geometric Frobenius on \(H^1(E)\), their sum is the trace \(a_v=Nv+1-\#\widetilde E(k_v)\) and their product is \(\det=Nv\), because \(\epsilon_\ell^{-1}(\operatorname{Frob}_v)=Nv\) for geometric Frobenius. So the factor is \((1-a_vNv^{-s}+Nv^{1-2s})^{-1}\).

**6.4.** For a character \(z\mapsto z^a\bar z^b\) of \(\mathbb C^\times\), the derivative along the holomorphic coordinate is \(a\) and along the antiholomorphic one is \(b\). The principal series induced from two such characters has, by the Harish-Chandra isomorphism, the infinitesimal character given by the pair \((a_1,a_2)\) for the holomorphic factor and \((b_1,b_2)\) for the antiholomorphic factor, where the normalized induction already contains the shift by \(\rho\). For \(z/|z|=z^{1/2}\bar z^{-1/2}\) and \(\bar z/|z|=z^{-1/2}\bar z^{1/2}\) these pairs are \((\frac12,-\frac12)\) and \((-\frac12,\frac12)\), both Weyl conjugate to \(\rho=(\frac12,-\frac12)\).

## Sources

- [OpenAI-030] OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI Math Release preprint, 4 October 2026, Section 1 (the theorem, the history and the plan), Section 2 (conventions) and Section 6 (the automorphy inputs). https://github.com/openai/math/tree/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026
- [CN] A. Caraiani and J. Newton, *On the modularity of elliptic curves over imaginary quadratic fields*, arXiv:2301.10509v3, Definition 2.1.27, Theorem 5.2 with Remark 5.2.2, Theorem 6.1 and Lemma 6.1.3. https://arxiv.org/abs/2301.10509v3
- [HLTT] M. Harris, K.-W. Lan, R. Taylor and J. Thorne, *On the rigid cohomology of certain Shimura varieties*, Theorem 1 of the introduction, proved as Corollary 7.14. https://arxiv.org/abs/1411.6717
- [Sch] P. Scholze, *On torsion in the cohomology of locally symmetric varieties*, Ann. of Math. 182 (2015), Corollary V.4.2. https://arxiv.org/abs/1306.2070
- [Var] I. Varma, *Local-global compatibility for regular algebraic cuspidal automorphic representations when ℓ ≠ p*, Theorem 1\(^{\mathrm{ss}}\). https://arxiv.org/abs/1411.2520
- [JL] H. Jacquet and R. P. Langlands, *Automorphic forms on GL(2)*, Lecture Notes in Math. 114 (1970), Theorem 11.1 (analytic continuation and functional equation of the \(L\)-function of a cuspidal representation) and its proof. https://publications.ias.edu/sites/default/files/automorphic-forms-on-gl2_rpl.pdf
- [ACC] P. B. Allen, F. Calegari, A. Caraiani, T. Gee, D. Helm, B. V. Le Hung, J. Newton, P. Scholze, R. Taylor and J. A. Thorne, *Potential automorphy over CM fields*, for potential modularity of elliptic curves over CM fields. https://arxiv.org/abs/1812.09999
- [AKT] P. B. Allen, C. Khare and J. A. Thorne, *Modularity of GL₂(F_p)-representations over CM fields*, for modularity of a positive proportion of elliptic curves over CM fields. https://arxiv.org/abs/1910.12986
