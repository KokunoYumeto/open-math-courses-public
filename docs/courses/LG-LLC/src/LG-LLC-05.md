# Monodromy blocks and the passage from supercuspidals to all parameters

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Weil representation records the semisimple part of a local parameter. A nilpotent operator records the extra information that appears, for example, at multiplicative reduction. The important structural fact is that this operator organizes irreducible Weil representations into finite chains. Those chains are the parameter-side counterparts of segments in the representation theory of general linear groups.

We assume the definitions of Weil representations and local factors, and the Langlands classification by segments from *Irreducible representations of general linear groups over a local field*. The classification of Weil–Deligne objects is proved here by graded linear algebra. The reduction theorem for the full correspondence is then stated separately from this algebraic bijection. Basic references are [Blasius 2006], [Getz–Hahn 2022] and [Wedhorn 2000].

## 1. Two versions of the special block

Let \(F\) be a nonarchimedean local field, with \(\lVert\Phi\rVert=q^{-1}\) for geometric Frobenius. A Frobenius-semisimple Weil–Deligne representation is a pair \((r,N)\) on a finite-dimensional complex vector space, with \(r\) smooth on inertia, \(r(\Phi)\) semisimple, \(N\) nilpotent, and

\[
r(w)Nr(w)^{-1}=\lVert w\rVert N.
\tag{1.1}
\]

Define the **uncentered block** \(\operatorname{Sp}(k)\) on \(e_0,\ldots,e_{k-1}\) by

\[
r(w)e_j=\lVert w\rVert^j e_j,
\quad Ne_j=e_{j+1}\ (j<k-1),\quad Ne_{k-1}=0.
\]

Its **centered block** is

\[
S_k=\lVert\cdot\rVert^{-(k-1)/2}\operatorname{Sp}(k).
\tag{1.2}
\]

The Weil exponents of \(S_k\) run from \(-(k-1)/2\) to \((k-1)/2\). Its determinant is one, and \(\ker N\) has exponent \((k-1)/2\). We write \(S_k\), rather than leaving the centering implicit, when identifying a unitary Steinberg representation. Both conventions will be used, but never interchangeably.

## 2. Why Frobenius semisimplicity gives enough semisimplicity

**Lemma 2.1 (Weil-group prerequisite).** If \(r\) is smooth on inertia and \(r(\Phi)\) is semisimple, then \(r\) is a semisimple Weil representation.

This is Representations of Weil groups, Theorem 3.1, with the same geometric Frobenius convention. Smoothness gives finite inertia image in finite dimension, exactly the hypothesis of that theorem. We use this semisimplicity to form isotypic components; the graded monodromy classification is proved in the next section.

If \(\rho\) is irreducible of dimension \(d\), then \(\rho\) and \(\rho\lVert\cdot\rVert^a\) are nonisomorphic for a nonzero integer \(a\): equality of determinants at \(\Phi\) would require \(q^{-ad}=1\). Thus the integer norm twists of \(\rho\) form an infinite chain of distinct labels.

Equation (1.1) says that \(N\) maps the \(\rho\lVert\cdot\rVert^a\)-isotypic component into the \(\rho\lVert\cdot\rVert^{a+1}\)-isotypic component. Different integer-twist orbits therefore do not interact.

## 3. A graded Jordan basis

**Lemma 3.1.** Let \(M=\bigoplus_{a\in\mathbb Z}M_a\) have finite support, and let \(T:M_a\to M_{a+1}\) be nilpotent. There is a basis consisting of homogeneous chains

\[
x,Tx,\ldots,T^{k-1}x,
\qquad T^kx=0.
\tag{3.1}
\]

The multiset of starting degrees and chain lengths is uniquely determined.

**Proof.** Put \(F_j=\ker T\cap\operatorname{im}T^j\). This is a descending graded filtration of \(\ker T\). Choose a homogeneous basis of \(\ker T\) compatible with every \(F_j\). For a basis vector \(y_i\), let \(h_i\) be the largest \(j\) with \(y_i\in F_j\). Choose a homogeneous lift \(x_i\) with \(T^{h_i}x_i=y_i\); it exists in degree \(\deg y_i-h_i\). These are the chains of length \(h_i+1\).

They are linearly independent. In a relation among their vectors, give \(T^a x_i\) its remaining length \(h_i-a\). Apply \(T^b\), where \(b\) is the largest remaining length occurring. All shorter terms vanish, and the surviving terms are distinct basis vectors \(y_i\). Their coefficients are zero. Repeating proves that every coefficient in the relation was zero.

They span, because

\[
\begin{aligned}
\sum_i(h_i+1)&=\sum_{j\ge0}\dim F_j\\
&=\sum_{j\ge0}(\dim\operatorname{im}T^j-\dim\operatorname{im}T^{j+1})
=\dim M.
\end{aligned}
\]

For uniqueness, let \(R_{a,b}\) be the rank of \(T^{b-a}:M_a\to M_b\), for \(a\le b\). A chain contributes one to \(R_{a,b}\) exactly when its interval contains \([a,b]\). Therefore the number of chains with interval exactly \([a,b]\) is

\[
R_{a,b}-R_{a-1,b}-R_{a,b+1}+R_{a-1,b+1}.
\tag{3.2}
\]

These intrinsic ranks determine every multiplicity. \(\square\)

**Theorem 3.2.** Every Frobenius-semisimple Weil–Deligne representation is a direct sum of blocks

\[
\rho\otimes\operatorname{Sp}(k),
\]

where \(\rho\) is an irreducible Weil representation. Each block is indecomposable. The multiset of pairs \((\rho,k)\) is unique. Equivalently one may use centered blocks \(\tau\otimes S_k\), with \(\tau=\rho\lVert\cdot\rVert^{(k-1)/2}\).

**Proof.** Lemma 2.1 decomposes the underlying Weil representation into irreducibles. Choose one representative \(\rho_0\) on each integer-twist orbit and write its part as

\[
\bigoplus_a(\rho_0\lVert\cdot\rVert^a)\otimes M_a.
\]

By (1.1) and Schur's lemma, \(N\) is identity on the irreducible factor, tensored with a linear map \(T_a:M_a\to M_{a+1}\), after fixing the obvious twist identifications. Lemma 3.1 decomposes the multiplicity spaces into interval chains. A chain starting at \(a\) of length \(k\) is exactly \((\rho_0\lVert\cdot\rVert^a)\otimes\operatorname{Sp}(k)\).

A single chain is indecomposable: its graded endomorphisms commuting with the consecutive identity maps have one common scalar, so it has no nontrivial idempotent. Formula (3.2) proves uniqueness within each twist orbit, and different orbits do not interact. Finally (1.2) gives the centered version. \(\square\)

Frobenius-semisimple does not mean semisimple as a Weil–Deligne representation. For example \(S_2\) is indecomposable, with a nonzero monodromy operator. It is not an irreducible Weil representation.

## 4. Segments have the same labels as monodromy chains

Suppose, in every rank, a twist-compatible bijection \(c\) has been given from supercuspidal representations to irreducible Weil representations. Write \(\nu=\lvert\det\rvert_F\). For a segment

\[
\Delta=[\sigma,\sigma\nu,\ldots,\sigma\nu^{k-1}],
\]

let \(Q(\Delta)\) be its essentially square-integrable representation. The block assigned to it is

\[
c(\sigma)\otimes\operatorname{Sp}(k)
=c(\sigma\nu^{(k-1)/2})\otimes S_k.
\tag{4.1}
\]

For a Langlands quotient belonging to the multisegment \(\{\Delta_1,\ldots,\Delta_t\}\), take the direct sum of the blocks (4.1).

**Proposition 4.1.** Under the stated supercuspidal bijection and the Langlands classification, this construction is a bijection between irreducible representations of all general linear groups and Frobenius-semisimple Weil–Deligne representations, preserving dimensions.

**Proof.** Langlands classification parametrizes the irreducibles by multisets of segments. Theorem 3.2 parametrizes Weil–Deligne objects by multisets of irreducible starting representations and positive chain lengths. The bijection \(c\), including its compatibility with \(\nu\) and \(\lVert\cdot\rVert\), identifies a segment of length \(k\) with a unique block. If \(\sigma\) has rank \(d\), the segment representation and its parameter both have dimension or rank \(dk\). Reversing Theorem 3.2 and applying \(c^{-1}\) to each starting label gives the inverse. \(\square\)

This is an algebraic parametrization. Preservation of Rankin–Selberg factors requires a further theorem. The reduction theorem says that a family \(c\) preserving factors of supercuspidal pairs, character twists, determinants and duals extends by (4.1) to the local Langlands correspondence. Its proof uses the Langlands classification and multiplicativity of local gamma factors; it is not being inferred from the counting of labels in Proposition 4.1. The precise extension formula appears in [Wedhorn 2000, (4.2.2)].

In rank two this parametrization is particularly concrete. There are exactly three parameter types:

- an irreducible two-dimensional Weil representation with \(N=0\);
- a sum of two characters with \(N=0\);
- a character times \(S_2\), with \(N\ne0\).

The last type corresponds to \(\operatorname{St}_2\otimes\chi\). A character sum corresponds to an irreducible principal series unless the inducing-character ratio is \(\lvert\cdot\rvert^{\pm1}\). At those ratios its Langlands quotient is a character of the determinant. The special constituent at the same reducibility point has the third, nonzero-monodromy parameter. This proves the rank-two non-supercuspidal counting check without conflating the two constituents.

## 5. Factors see the end of the chain

For \(V=(r,N)\), let \(V_N^I=(\ker N)^{I_F}\). Define

\[
L(s,V)=\det(1-q^{-s}r(\Phi)\mid V_N^I)^{-1}.
\tag{5.1}
\]

**Proposition 5.1.** For irreducible \(\rho\),

\[
L(s,\rho\otimes\operatorname{Sp}(k))
=L(s,\rho\lVert\cdot\rVert^{k-1}).
\tag{5.2}
\]

If \(\rho\) is ramified the factor is one. If \(\rho=\chi\) is unramified and \(\alpha=\chi(\varpi)\), then

\[
L(s,\chi S_k)=(1-\alpha q^{-s-(k-1)/2})^{-1}.
\tag{5.3}
\]

**Proof.** The kernel of monodromy in the uncentered block is its last copy of \(\rho\), on which Weil action is \(\rho\lVert\cdot\rVert^{k-1}\). This proves (5.2) directly from (5.1). The space \(\rho^{I_F}\) is Weil-stable. Irreducibility makes it either zero or the whole space. In the latter case \(\rho\) factors through the infinite cyclic quotient, whose irreducible finite-dimensional complex representations are one-dimensional. Thus a ramified irreducible has no invariants, and an unramified irreducible is a character. Centering gives (5.3). \(\square\)

The Weil–Deligne conductor is

\[
a(r,N)=a(r)+\dim V^{I_F}-\dim(\ker N)^{I_F}.
\tag{5.4}
\]

Hence \(a(\chi S_k)=k-1\) if \(\chi\) is unramified, and \(a(\chi S_k)=k\,a(\chi)\) if it is ramified. In the latter case every Weil summand has conductor \(a(\chi)\), and neither space of invariants in the correction term is nonzero.

For an unramified additive character and self-dual measure, the monodromy correction to the epsilon factor is

\[
\det(-q^{-s}r(\Phi)\mid V^{I_F}/(\ker N)^{I_F}).
\]

The underlying unramified Weil summands have epsilon factor one. Multiplying the eigenvalues on the first \(k-1\) terms of the centered chain gives

\[
\epsilon(s,\chi S_k,\psi)=(-\alpha)^{k-1}q^{(k-1)(1/2-s)}.
\tag{5.5}
\]

For \(k=2\), these formulas give \(L(s)= (1-\alpha q^{-s-1/2})^{-1}\), conductor one, and epsilon factor \(-\alpha q^{1/2-s}\). They fix exactly which line is the kernel of \(N\).

## 6. Three-dimensional examples

The centered segment \([\nu^{-1},1,\nu]\) gives \(\operatorname{St}_3\) and parameter \(S_3\). It has

\[
L(s,\operatorname{St}_3)=(1-q^{-s-1})^{-1},\quad a(S_3)=2,
\quad\epsilon(s,S_3,\psi)=q^{1-2s}.
\]

The Langlands quotient of \(\nu\times1\times\nu^{-1}\), treating the three singleton segments as separate segments, is the trivial representation of \(\operatorname{GL}_3(F)\). Its parameter is \(\lVert\cdot\rVert\oplus1\oplus\lVert\cdot\rVert^{-1}\), with zero monodromy. Its factor is

\[
\prod_{j=-1}^{1}(1-q^{-s-j})^{-1},
\]

and its conductor is zero. The two parameters have the same semisimplified Weil constituents but different \(N\); their \(L\)-factors distinguish them.

Finally choose an unramified character \(\chi\) whose value \(\beta\) on a uniformizer is a nontrivial root of unity. The induction \(\operatorname{St}_2\times\chi\) is irreducible by the nonlinking criterion: its singleton segment is not adjacent to the two-term segment of \(\operatorname{St}_2\). Its parameter is \(S_2\oplus\chi\), so

\[
L(s)=(1-q^{-s-1/2})^{-1}(1-\beta q^{-s})^{-1},
\quad a=1,\quad\epsilon(s,\psi)=-q^{1/2-s}.
\]

The qualification on \(\chi\) ensures irreducibility; for an adjacent singleton one must specify the appropriate Langlands quotient instead.

## 7. Exercises with solutions

**Exercise 7.1 (easy).** Write the centered parameter of \(\operatorname{St}_n\) and compute its determinant.

**Solution.** It is \(S_n=\lVert\cdot\rVert^{-(n-1)/2}\operatorname{Sp}(n)\). Its exponents are \(j-(n-1)/2\) for \(0\le j<n\); their sum is zero. The determinant is therefore the trivial character, agreeing with the central character of the untwisted unitary Steinberg representation.

**Exercise 7.2 (medium).** Compute \(L(s,\operatorname{St}_3\otimes\chi)\) for an unramified character \(\chi\), and then for a ramified character.

**Solution.** The parameter is \(\chi S_3\). In the unramified case its monodromy kernel has Frobenius eigenvalue \(\chi(\varpi)q^{-1}\), giving \((1-\chi(\varpi)q^{-s-1})^{-1}\). In the ramified case no vector in the kernel is inertia-fixed, giving one. Formula (5.4) gives conductor two in the first case and \(3a(\chi)\) in the second.

**Exercise 7.3 (medium).** Suppose normalized induction from characters \(\chi_1,\ldots,\chi_n\) is irreducible. Determine its parameter. Explain why the conclusion about \(N\) is different for a Steinberg constituent of a reducible induction.

**Solution.** The Langlands label consists of the singleton segments \([\chi_i]\). Each singleton gives its character parameter with zero monodromy, so their direct sum is the parameter and \(N=0\). A Steinberg constituent has a different multisegment label: consecutive characters form one segment. The same characters are then connected by the nonzero operator of \(S_n\). Being a subquotient of a character induction does not force zero monodromy.

**Exercise 7.4 (hard).** Prove that the segment-to-block construction is injective even when the same Weil irreducible occurs in several overlapping segments.

**Solution.** Separate the integer-twist orbits. On one orbit choose \(\rho_0\); the multiplicity spaces \(M_a\) and the ranks \(R_{a,b}\) of their consecutive monodromy maps are intrinsic to the parameter. Formula (3.2) recovers how many segments start at \(a\) and end at \(b\), including repetitions and overlapping intervals. Thus it recovers the entire multisegment on that orbit. Repeat for every orbit and apply \(c^{-1}\) to the irreducible starting labels. The recovered multiset determines the Langlands quotient uniquely. Surjectivity is the homogeneous-chain decomposition, so this also supplies a complete inverse to Proposition 4.1.

## What this lesson does not prove

Weil semisimplicity is the prerequisite Representations of Weil groups, Theorem 3.1, with its finite-inertia hypothesis checked in Section 2.

The Langlands and Bernstein–Zelevinsky classifications on the representation side are the inputs in Section 4; see [Getz–Hahn 2022, §§8.4 and 10.5] and [Wedhorn 2000, (2.2.9)]. The existence of the supercuspidal bijection preserving factors is the substantive local Langlands theorem, discussed in *The theorem of Harris and Taylor and its strategy* and *Other existence proofs and further properties*. The reduction theorem using multiplicativity of gamma factors is stated in Section 4; see [Wedhorn 2000, (4.2.2)] and [Getz–Hahn 2022, §§11.8 and 12.4]. The definition and normalization of Artin conductors and Weil epsilon factors are taken from [Deligne 1973, §§4–5 and 8]. All chain decomposition, uniqueness, dimension-two counting and block factor calculations in this lesson are proved explicitly.

## References

- [Blasius 2006] D. Blasius, [*Hilbert modular forms and the Ramanujan conjecture*](https://arxiv.org/abs/math/0511007), in *Noncommutative Geometry and Number Theory*, Vieweg, 2006, §§1.6–1.7.
- [Getz–Hahn 2022] J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§8.4, 10.5, 11.8 and 12.4.
- [Wedhorn 2000] T. Wedhorn, [*The local Langlands correspondence for GL(n) over p-adic fields*](https://arxiv.org/abs/math/0011210v2), lectures at the School on Automorphic Forms on GL(n), ICTP Trieste, 2000, §§2.2 and 4.2.
- [Deligne 1973] P. Deligne, [*Les constantes des équations fonctionnelles des fonctions L*](https://publications.ias.edu/sites/default/files/Number20.pdf), in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349, Springer, 1973, 501–597, §§4–5 and 8.
