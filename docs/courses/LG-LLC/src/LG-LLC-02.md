# Irreducible representations of general linear groups over a local field

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Parabolic induction supplies representations, but usually supplies too many at once: an induced representation can have several irreducible constituents. Segments organize this ambiguity. A segment groups consecutive twists of one supercuspidal representation into an essentially square-integrable representation; a multisegment specifies how such groups are assembled.

We assume the classification and Kirillov models of irreducible representations of the two-dimensional general linear group from *The Kirillov model and the classification of irreducible representations*. The precise rank-one input is recalled below. The general Bernstein–Zelevinsky theorems are stated. We prove their rank-two dictionary, compute the Jacquet modules that make cuspidal support intrinsic in that case, and prove square-integrability of the rank-two Steinberg representation by an explicit coefficient calculation. Basic references are [Getz–Hahn 2022], [Jacquet–Langlands 1970] and [Wedhorn 2000].

## 1. Induction and its normalizations

Let \(F\) be a nonarchimedean local field, \(\mathcal O\) its ring of integers, \(\varpi\) a uniformizer and \(q\) the residue cardinality. Put \(G_n=\mathrm{GL}_n(F)\) and \(\nu(g)=|\det g|_F\). All representations are complex, smooth and admissible; “irreducible” always includes nonzero.

For a standard parabolic \(P=MU\), with \(M\simeq G_{n_1}\times\cdots\times G_{n_r}\), write

\[
\pi_1\times\cdots\times\pi_r
=\operatorname{Ind}_{P}^{G_n}
 (\delta_P^{1/2}\,\pi_1\boxtimes\cdots\boxtimes\pi_r).
\tag{1.1}
\]

Induction is realized by functions with left covariance and right translation. Thus for the upper triangular Borel \(B=TN\) in \(G_2\),

\[
 f\left(\begin{pmatrix}a&x\\0&d\end{pmatrix}g\right)
 =|a/d|^{1/2}\chi_1(a)\chi_2(d)f(g)
\tag{1.2}
\]

in \(I(\chi_1,\chi_2)=\chi_1\times\chi_2\). This convention fixes which constituent is a subrepresentation and which is a quotient at a reducibility point.

The **normalized Jacquet module** is

\[
r_N(V)=\delta_B^{-1/2}\otimes
 V/\langle n v-v:n\in N,\ v\in V\rangle.
\tag{1.3}
\]

For general \(G_n\), a representation is supercuspidal if it is not a subquotient of induction from a proper parabolic. The equivalent vanishing of all proper Jacquet modules is a theorem. Every irreducible representation has a unique unordered multiset of supercuspidal representations whose induction contains it as a subquotient. This multiset is its **cuspidal support**. These general facts are imported from [Zelevinsky 1980, §1.10] for nonarchimedean \(F\), and from [Getz–Hahn 2022, Theorems 8.3.3–8.3.6] in their stated domains; Theorem 8.3.6 there assumes characteristic zero. Our rank-two uniqueness proof appears in Section 4.

## 2. Segments and the two classifications

Fix an irreducible supercuspidal \(\rho\) of \(G_d\). A segment on its integer twist line is

\[
\Delta=[\rho\nu^a,\rho\nu^{a+1},\ldots,\rho\nu^b],
\qquad a,b\in\mathbb Z,\quad a\le b.
\tag{2.1}
\]

An arbitrary starting representation absorbs a nonintegral twist. The degree of this segment is \(d(b-a+1)\). The interval notation records the actual representations, so translating the base \(\rho\) and the endpoints together does not change the segment.

Two segments are **linked** when their union is a segment and neither contains the other. For segments \([a,b]\) and \([c,d]\) on the same line with \(a\le c\), this means precisely

\[
a<c\le b+1\le d.
\tag{2.2}
\]

Indeed, absence of a gap says \(c\le b+1\); absence of containment says \(a<c\) and \(b<d\). Segments on different integer twist lines are never linked. Equal segments, and a segment contained in another, are never linked. Adjacent disjoint segments can be linked.

Let \(Q(\Delta)\) denote the unique irreducible quotient of the increasing induction in (2.1), and let \(Z(\Delta)\) denote its unique irreducible subrepresentation. The following are theorem inputs, not conclusions of an elementary induction argument.

**Theorem 2.1 (segment and Langlands classification, stated).** The representations \(Q(\Delta)\) are exactly the essentially square-integrable irreducible representations of general linear groups. Write
\(Q(\Delta)=\delta_\Delta\nu^{e_\Delta}\), where \(\delta_\Delta\) is square-integrable with unitary central character and \(e_\Delta\in\mathbb R\). For a multisegment \(\mathfrak m=\{\Delta_1,\ldots,\Delta_t\}\), order the segments so that \(e_{\Delta_1}\ge\cdots\ge e_{\Delta_t}\). Then

\[
Q(\Delta_1)\times\cdots\times Q(\Delta_t)
\longtwoheadrightarrow L(\mathfrak m)
\tag{2.3}
\]

has a unique irreducible quotient. The map \(\mathfrak m\mapsto L(\mathfrak m)\) is a bijection onto all irreducible admissible representations, in each total degree. Choices among equal exponents do not change the quotient. The cuspidal support is the multiset of all entries of the segments, with their multiplicities.

The sources are [Getz–Hahn 2022, Theorems 8.4.1–8.4.3] and the multisegment classification in [Wedhorn 2000, (2.2.9) and (2.3.9)]. Its increasing single-segment quotient convention agrees with ours.

**Theorem 2.2 (Zelevinsky classification, stated).** Say that \([a,b]\) precedes \([c,d]\) if \(a<c\le b+1\le d\). Order a multisegment so that no earlier segment precedes a later one. The induction of the corresponding \(Z(\Delta_i)\) has a unique irreducible subrepresentation, denoted \(Z(\mathfrak m)\). This is independent of the allowed ordering, and \(\mathfrak m\mapsto Z(\mathfrak m)\) is another bijection onto irreducible representations. See [Zelevinsky 1980, §§4 and 6].

The two labels differ. Already for a single length-two segment, \(Q(\Delta)\) is a Steinberg twist whereas \(Z(\Delta)\) is a determinant character. The involution relating the two multisegment classifications must therefore be applied before identifying their labels.

**Theorem 2.3 (irreducibility, genericity and temperedness, stated).** The induction
\(Q(\Delta_1)\times\cdots\times Q(\Delta_t)\) is irreducible if and only if no two segments are linked. An irreducible representation is generic if and only if its Langlands multisegment is unlinked. It is tempered if and only if all its segment representations are square-integrable with unitary central character. These are [Getz–Hahn 2022, Theorems 8.4.4–8.4.5], with the equivalent multisegment description in [Wedhorn 2000, (2.2.9)(4), (2.3.7) and (2.4.4)].

Here generic means admitting a nonzero Whittaker functional for a nondegenerate character of the upper unipotent group. Square-integrable means that matrix coefficients are square-integrable modulo the center, whose character is unitary; “essentially” permits twisting by a real power of \(\nu\).

## 3. The complete rank-two dictionary

We use the following rank-one classification input: \(I(\chi_1,\chi_2)\) is irreducible unless \(\chi_1\chi_2^{-1}=\nu^{\pm1}\); away from those ratios, interchanging the characters gives an isomorphic representation. At either exceptional ratio there are exactly two constituents, a determinant character and its Steinberg twist, in the subquotient positions stated below. Every irreducible representation of \(G_2\) is a supercuspidal, one of these irreducible principal series, a Steinberg twist, or a determinant character. This is the prerequisite classification; its reducibility and subquotient assertions are [Jacquet–Langlands 1970, Theorem 3.3].

The Steinberg representation has the boundary realization

\[
\mathrm{St}_2=C^\infty(\mathbb P^1(F))/\mathbb C.
\tag{3.1}
\]

Indeed, (1.2) for \((\chi_1,\chi_2)=(\nu^{-1/2},\nu^{1/2})\) has trivial left \(B\)-covariance. Its functions are locally constant functions on \(B\backslash G_2\simeq\mathbb P^1(F)\); its constant functions form the trivial subrepresentation. Twisting gives the exact sequences

\[
0\longrightarrow\chi\circ\det
\longrightarrow I(\chi\nu^{-1/2},\chi\nu^{1/2})
\longrightarrow\mathrm{St}_2\otimes(\chi\circ\det)
\longrightarrow0,
\tag{3.2}
\]

\[
0\longrightarrow\mathrm{St}_2\otimes(\chi\circ\det)
\longrightarrow I(\chi\nu^{1/2},\chi\nu^{-1/2})
\longrightarrow\chi\circ\det\longrightarrow0.
\tag{3.3}
\]

The second follows also by contragredience of the first, using normalized induction duality [Getz–Hahn 2022, Proposition 8.2.3] and the rank-one constituent identification.

**Proposition 3.1.** The segment classification in total degree two is exactly the rank-one classification just recalled. Singleton segments are linked exactly at its two reducibility ratios.

**Proof.** A degree-two multisegment has only three possible forms. It can be one singleton whose supercuspidal entry has degree two; its Langlands quotient is that entry itself. It can be one length-two segment of characters, necessarily
\([\chi\nu^{-1/2},\chi\nu^{1/2}]\); (3.2) identifies its \(Q\) with \(\mathrm{St}_2\otimes\chi\) and its \(Z\) with \(\chi\circ\det\). Finally, it can have two character singletons. If they are unlinked, their induction is irreducible by the rank-one input and gives the principal series. If linked, they are the two characters in (3.2). Ordering their real exponents decreasingly gives (3.3), so their Langlands quotient is \(\chi\circ\det\).

To verify the linking assertion without invoking the general criterion, two distinct singleton characters have a segment as their union exactly when one is the other times \(\nu\). Thus they are linked exactly when \(\chi_1\chi_2^{-1}=\nu\) or \(\nu^{-1}\). Equal characters fail the noncontainment condition and give an irreducible principal series. These possibilities exhaust both classifications, with the same isomorphisms and exceptional constituents. ∎

For clarity, the two exceptional Langlands labels are

| Representation | Langlands multisegment |
| --- | --- |
| \(\mathrm{St}_2\otimes\chi\) | \(\{[\chi\nu^{-1/2},\chi\nu^{1/2}]\}\) |
| \(\chi\circ\det\) | \(\{[\chi\nu^{-1/2}],[\chi\nu^{1/2}]\}\) |

The central character in both rows is \(\chi^2\). Their cuspidal supports agree; their grouping into segments does not.

## 4. The two Bruhat cells and cuspidal support

**Lemma 4.1 (rank-one geometric lemma).** The normalized Jacquet module of \(I(\chi_1,\chi_2)\) has a two-step filtration whose quotients are

\[
\chi_2\boxtimes\chi_1,\qquad
\chi_1\boxtimes\chi_2.
\tag{4.1}
\]

This asserts a filtration, not necessarily a direct sum.

**Proof.** First, coinvariants under \(N\simeq(F,+)\) are exact on smooth representations. Write \(F=\bigcup_{r\ge0}\varpi^{-r}\mathcal O\). Coinvariants are the directed limit of coinvariants for these compact groups. Each compact coinvariant functor is averaging onto invariants and is exact over \(\mathbb C\); directed limits of vector spaces are exact. The normalization twist preserves exactness.

Evaluation at the closed Bruhat cell gives a surjection \(f\mapsto f(1)\). Its kernel consists of functions supported away from that point of \(B\backslash G_2\). On the open cell, use
\(w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\) and coordinate \(w n(x)\). The kernel is then \(C_c^\infty(F)\), and right \(n(u)\) acts by \(\phi(x)\mapsto\phi(x+u)\).

Integration \(\phi\mapsto\int_F\phi(x)\,dx\) identifies its coinvariants with \(\mathbb C\). To check injectivity of this identification, refine a compactly supported locally constant function into finitely many cosets of a common compact open additive subgroup. Translation identifies the characteristic functions of all these cosets in coinvariants. A function with integral zero is consequently a sum of their differences, and is zero in coinvariants.

For \(t=\operatorname{diag}(a,d)\), the open-cell action is

\[
\phi(x)\longmapsto
|d/a|^{1/2}\chi_1(d)\chi_2(a)\phi(xd/a).
\]

The integral picks up \(|a/d|\); after multiplication by \(\delta_B(t)^{-1/2}=|a/d|^{-1/2}\), its character is \(\chi_2(a)\chi_1(d)\). Evaluation at the closed cell has unnormalized character \(|a/d|^{1/2}\chi_1(a)\chi_2(d)\), so its normalized character is \(\chi_1(a)\chi_2(d)\). Exactness now gives (4.1). ∎

For a determinant character, \(N\) acts trivially, whence

\[
r_N(\chi\circ\det)
=\chi\nu^{-1/2}\boxtimes\chi\nu^{1/2}.
\tag{4.2}
\]

Apply Lemma 4.1 and exactness to (3.2). Subtracting the character in (4.2) from the two filtration characters leaves

\[
r_N(\mathrm{St}_2\otimes\chi)
=\chi\nu^{1/2}\boxtimes\chi\nu^{-1/2}.
\tag{4.3}
\]

**Theorem 4.2.** Cuspidal support for \(G_2\) is well defined up to order. It is read from the computed Jacquet modules as follows:

\[
\begin{array}{c|c}
\pi&\operatorname{supp}_{\mathrm{cusp}}(\pi)\\\hline
I(\chi_1,\chi_2)\text{ irreducible}&\{\chi_1,\chi_2\}\\
\mathrm{St}_2\otimes\chi&\{\chi\nu^{-1/2},\chi\nu^{1/2}\}\\
\chi\circ\det&\{\chi\nu^{-1/2},\chi\nu^{1/2}\}\\
\rho\text{ supercuspidal}&\{\rho\}.
\end{array}
\tag{4.4}
\]

**Proof.** For every non-supercuspidal irreducible, (4.1)–(4.3) give a nonzero finite-length \(T\)-module. Forgetting the order in either character of its semisimplification gives the multiset in (4.4). Suppose the same representation occurs in another induction \(I(\eta_1,\eta_2)\). By the rank-one classification that induction is either irreducible, or has precisely the two constituents in (3.2)–(3.3). The computations for each constituent show that every one of its Jacquet characters has unordered pair \(\{\eta_1,\eta_2\}\). Hence this pair equals the pair intrinsic to \(r_N(\pi)\).

A supercuspidal cannot occur in a proper induction by definition, and induction from \(G_2\) itself has only that irreducible as its constituent. Conversely all three non-supercuspidal types occur in their displayed character inductions. This proves both existence and uniqueness in rank two without using the general cuspidal-support uniqueness theorem. ∎

## 5. Why the rank-two Steinberg coefficients are square-integrable

Here the Steinberg representation has trivial central character, so work in \(\overline G=\mathrm{PGL}_2(F)\). Let \(I\) be the image of the Iwahori subgroup consisting of integral invertible matrices that are upper triangular modulo \(\varpi\), and give it volume one.

The lattice tree makes the relevant double cosets explicit. Vertices are homothety classes of rank-two \(\mathcal O\)-lattices; two vertices are adjacent when representatives \(L,L'\) satisfy \(\varpi L\subset L'\subset L\) with quotient dimension one. Each vertex has \(q+1\) neighbors. The group \(I\) fixes the two endpoints of the edge
\([\mathcal O^2],[\mathcal O e_1+\varpi\mathcal O e_2]\). Set

\[
s_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
s_1=\begin{pmatrix}0&\varpi^{-1}\\\varpi&0\end{pmatrix},\quad
\omega=\begin{pmatrix}0&1\\\varpi&0\end{pmatrix}.
\tag{5.1}
\]

Modulo the center, \(s_0,s_1\) are involutions, their alternating products are distinct, and \(\omega^2=1\). The latter exchanges the edge endpoints and conjugates \(s_0\) to \(s_1\). Thus the extended affine Weyl group is
\(\widetilde W=\langle s_0,s_1\rangle\rtimes\langle\omega\rangle\), with \(\ell(\omega)=0\).

The double cosets of \(I\) are \(IwI\), for \(w\in\widetilde W\), and

\[
\operatorname{vol}(IwI)=q^{\ell(w)}.
\tag{5.2}
\]

One elementary verification uses the unique path between two tree edges. Its successive wall types alternate, giving a reduced word in \(s_0,s_1\); possible endpoint exchange records \(\omega\). At each new step there are exactly \(q\) choices after excluding the edge just traversed. The edge stabilizer acts transitively on those choices: reducing the upper, respectively lower, unipotent matrix entries modulo \(\varpi\) gives the translations on the \(q\) choices. Inductively its stabilizers give transitivity on paths of the fixed wall sequence. This proves both the double-coset description and the \(q^{\ell(w)}\) count of right \(I\)-cosets. It also proves the convolution rule \(T_uT_v=T_{uv}\) when lengths add, for \(T_w=1_{IwI}\).

**Proposition 5.1.** Every matrix coefficient of \(\mathrm{St}_2\) is in \(L^2(\overline G)\).

**Proof.** In the boundary model (3.1), \(I\) has two orbits on \(\mathbb P^1(F)\), so \(\dim\mathrm{St}_2^I=1\). Each of the two maximal vertex stabilizers \(K_0,K_1\) is transitive on that boundary, so \(\mathrm{St}_2^{K_i}=0\). These assertions pass from boundary functions to their quotient because invariants for compact groups are exact by averaging.

Choose an \(I\)-fixed vector \(v\) and an \(I\)-fixed smooth dual vector \(v^\vee\) with \(\langle v,v^\vee\rangle=1\). Such a dual vector exists by averaging any functional nonzero on \(v\); admissibility identifies the dual of the invariant line with the invariant line of the smooth dual. The normalized averages over \(K_i\) act as zero. Since \(K_i=I\sqcup Is_iI\),

\[
T_{s_i}v=-v\quad(i=0,1).
\]

The element \(\omega\) acts on the invariant line by a scalar \(\zeta\) with \(\zeta^2=1\). For \(w\) of length \(r\), convolution of a reduced word therefore acts on this line by a scalar of absolute value one. The coefficient
\(c(g)=\langle\mathrm{St}_2(g)v,v^\vee\rangle\) is constant on \(IwI\), while integrating it over that coset gives the same scalar. Equation (5.2) yields

\[
|c(g)|=q^{-\ell(w)}\quad(g\in IwI).
\tag{5.3}
\]

There are two elements of length zero and four of each positive length in \(\widetilde W\). Consequently

\[
\int_{\overline G}|c(g)|^2\,dg
=2+4\sum_{r\ge1}q^{-r}
=2+\frac4{q-1}<\infty.
\tag{5.4}
\]

Both the Steinberg representation and its smooth dual are irreducible. They are generated by their nonzero invariant vectors. Every matrix coefficient is therefore a finite linear combination of left and right translates of \(c\). Haar measure on \(\overline G\) is invariant under both translations, so all those coefficients are square-integrable. ∎

A unitary character twist does not change coefficient absolute values. Thus \(\mathrm{St}_2\otimes\chi\) is square-integrable when \(\chi\) is unitary, and essentially square-integrable for any character \(\chi\). The determinant-character constituent in (3.2) has coefficient of constant absolute value when unitary, and cannot be square-integrable on the noncompact group \(\overline G\).

## 6. A three-dimensional example

Consider \(\nu^{-1}\times1\times\nu\). Its support has each of the three consecutive characters once. There are exactly four multisegments with this support:

\[
\begin{aligned}
\mathfrak m_0&=\{[-1],[0],[1]\},&
\mathfrak m_1&=\{[-1,0],[1]\},\\
\mathfrak m_2&=\{[-1],[0,1]\},&
\mathfrak m_3&=\{[-1,1]\}.
\end{aligned}
\tag{6.1}
\]

Here \([a,b]\) abbreviates \([\nu^a,\ldots,\nu^b]\). No overlapping intervals are possible, because an overlap would repeat a support character. Each multisegment is therefore obtained by choosing where to cut the two edges of the interval \([-1,1]\).

The consecutive-induction theorem [Zelevinsky 1980, §2, Theorem 2.2] says that the constituents of a consecutive supercuspidal induction are indexed by the orientations of these edges. Corollary 2.3 there gives length two when joining two consecutive pieces. In the present case it gives the following four distinct constituents, each with multiplicity one:

\[
\begin{array}{c|c}
\mathfrak m&L(\mathfrak m)\\\hline
\mathfrak m_0&\mathbf1_{G_3}\\
\mathfrak m_1&\text{unique quotient of }\nu\times
 (\mathrm{St}_2\otimes\nu^{-1/2})\\
\mathfrak m_2&\text{unique quotient of }
 (\mathrm{St}_2\otimes\nu^{1/2})\times\nu^{-1}\\
\mathfrak m_3&\mathrm{St}_3.
\end{array}
\tag{6.2}
\]

For a direct multiplicity check, first split \(\nu^{-1}\times1\) using (3.2), then induce each constituent with \(\nu\). Each resulting induction has length two by Lemma IV.2. There are four possible irreducible labels by (6.1), and the graph description asserts that all four occur. Total length four forces multiplicity one. The trivial representation is the Langlands quotient of \(\nu\times1\times\nu^{-1}\): this decreasing induction has covariance \(\delta_B\), and is dual to the increasing induction with trivial covariance and its constant subrepresentation. The other rows follow from the segment centers \(-1/2,1/2\), and zero. Only the final row is generic, since every other multisegment has a linked pair. Only that row is tempered.

## 7. Exercises and complete solutions

**Exercise 7.1 (easy).** List all linked pairs of singleton segments of total degree two. Decide what happens for \(\{[\chi],[\chi]\}\) and for \(\{[\chi],[\chi\nu^2]\}\).

**Solution.** Both entries must be characters. The complete list is \(\{[\chi],[\chi\nu]\}\), with the unordered pair understood; writing \(\chi\nu^{-1}\) as the first entry gives the same list. Equal singleton segments contain each other, so are not linked. The twists separated by two have a gap, so their union is not a segment. Both of the latter pairs give irreducible principal series by the rank-one criterion.

**Exercise 7.2 (medium).** Show directly that \(Q([\nu^{-1/2},\nu^{1/2}])\) is square-integrable. Identify a coefficient and its squared integral when \(I\) has volume one.

**Solution.** Sequence (3.2) identifies the quotient with \(\mathrm{St}_2\). The invariant-line coefficient normalized to value one at the identity satisfies \(|c|=q^{-r}\) on a double coset of length \(r\), by the two Hecke eigenvalues \(-1\). The coset volume is \(q^r\), so its contribution to the squared integral is \(q^{-r}\). Counting lengths gives \(2+4/(q-1)\). Irreducibility makes all coefficients finite sums of translates of this one, completing the required square-integrability proof. This uses the computation of Section 5, rather than the square-integrability assertion of the general classification.

**Exercise 7.3 (medium).** Determine the multisegments and multiplicities of the constituents of \(\nu^{-1}\times1\times\nu\), and determine which constituents are generic or tempered.

**Solution.** There are two potential cuts, between \(-1,0\) and between \(0,1\). The four cut patterns give exactly (6.1). The consecutive-induction theorem and its two-piece length calculation give the four rows of (6.2), once each. The first row has linked singleton pairs; the second links \([-1,0]\) with \([1]\); the third links \([-1]\) with \([0,1]\). They are nongeneric. The full segment in the fourth row is unlinked and centered, hence \(\mathrm{St}_3\) is generic and tempered. The mixed rows have nonzero segment centers, and the singleton row has centers \(-1,0,1\), so none of those is tempered.

**Exercise 7.4 (hard).** Prove uniqueness of cuspidal support for \(G_2\) from its geometric lemma. Explain why knowing only the central character would be insufficient.

**Solution.** The open-cell coinvariant is integration on \(C_c^\infty(F)\), with normalized diagonal character \(\chi_2\boxtimes\chi_1\); the closed-cell coinvariant is evaluation, with character \(\chi_1\boxtimes\chi_2\). Exactness of Jacquet modules, proved by compact averaging in Lemma 4.1, gives these two characters for a principal series. At the reducibility point the determinant character contributes (4.2), leaving (4.3) for Steinberg. Thus every non-supercuspidal irreducible has a nonzero Jacquet character whose unordered pair is precisely its support. Any other character induction containing it has, by the rank-one constituent calculation, the same unordered pair. A supercuspidal has itself as its only possible support because it cannot occur in a proper induction. This is Theorem 4.2 with every geometric-lemma step specified.

The central character records only the product of the support characters. For example, \(I(\nu^t,\nu^{-t})\) has trivial central character for every \(t\); choosing \(t=0\) and \(t=1\) gives two irreducible principal series with different supports. Their Jacquet modules distinguish them. ∎

## What this lesson does not prove

The general subquotient and cuspidal-support theorems, and the supercuspidality criterion through Jacquet modules, are [Getz–Hahn 2022, Theorems 8.3.3–8.3.6]. The general segment, Langlands, Zelevinsky, irreducibility, genericity and temperedness theorems are stated in Section 2 with their exact locators. The consecutive-induction graph classification and its two-piece length calculation used in the rank-three example are [Zelevinsky 1980, §2, Theorem 2.2 and Corollary 2.3]. These general results are not proved here.

The rank-one irreducibility and classification theorem is the assigned prerequisite, recalled at the beginning of Section 3; its principal-series assertions are [Jacquet–Langlands 1970, Theorem 3.3], and the exhaustion is the Kirillov-model classification in §§2–3. Normalized induction duality is [Getz–Hahn 2022, Proposition 8.2.3]. We used these inputs to prove agreement with the segment description. The rank-one geometric lemma, the resulting intrinsic support calculation and the rank-two Steinberg coefficient summation were proved here.

## References

- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, *An Introduction to Automorphic Representations, with a View toward Trace Formulae*, draft of 22 April 2022, §§8.2–8.4. The published book is Graduate Texts in Mathematics 300, Springer, 2024. An [author version](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf) is available; the locators here use the draft numbering.
- [Wedhorn 2000] Torsten Wedhorn, [*The local Langlands correspondence for GL(n) over p-adic fields*](https://arxiv.org/abs/math/0011210v2), lectures at the School on Automorphic Forms on GL(n), ICTP Trieste, 2000, §§2.2–2.4.
- [Jacquet–Langlands 1970] Hervé Jacquet and Robert P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, Springer, 1970, §§2–3, especially Theorem 3.3. The IAS distributes a re-typeset edition retaining the theorem numbers.
- [Zelevinsky 1980] Andrei V. Zelevinsky, “Induced representations of reductive p-adic groups. II. On irreducible representations of GL(n),” *Annales scientifiques de l’École normale supérieure* 13 (1980), 165–210, §1.10, §2, Theorem 6.1 and §9. The [journal archive](https://www.numdam.org/item/ASENS_1980_4_13_2_165_0/) provides the article. Its general classification proofs are not reproduced here.
