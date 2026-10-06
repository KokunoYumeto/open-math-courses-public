# Two-dimensional Weil representations: induction and projective symmetry

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An irreducible two-dimensional parameter sometimes comes from a character of a quadratic extension. This makes a nonabelian parameter accessible through local class field theory. The question is whether every parameter has this form. We prove that the answer is yes when the residue characteristic is odd. In residue characteristic two, two further kinds of projective symmetry can occur.

We assume the Weil group and the ramification filtration of a nonarchimedean local field, finite-dimensional complex representation theory, and local reciprocity. Basic references are [Deligne 1973], [Getz–Hahn 2022] and [Weil 1974]. The proofs below isolate the group-theoretic reasons for the distinction between odd and even residue characteristic.

Throughout, \(F\) has residue field of cardinality \(q\) and characteristic \(p\). The Weil group fits into

\[
1\longrightarrow I_F\longrightarrow W_F\overset{v_W}{\longrightarrow}\mathbb Z\longrightarrow0.
\]

We choose geometric Frobenius \(\Phi\) with \(v_W(\Phi)=1\). A smooth complex Weil representation has finite image on inertia. Local reciprocity \(\operatorname{Art}_F:F^\times\to W_F^{\mathrm{ab}}\) sends a uniformizer to geometric Frobenius. We identify a character of \(F^\times\) with the corresponding character of \(W_F\) using this map. There is no monodromy operator in this lesson.

## 1. Removing the infinite scalar part

The image of a Weil representation need not be finite. For example, an unramified character can take any nonzero complex value on \(\Phi\). In dimension two, irreducibility makes this infinite part particularly simple.

**Proposition 1.1 (finite-image reduction).** An irreducible smooth finite-dimensional complex representation \(r\) of \(W_F\) becomes finite-image after an unramified twist. Its projective image is finite.

The finite-twist assertion and extension of the resulting finite representation to \(G_F\) are Representations of Weil groups, Theorem 2.2. Scalar twists have the same projective image, so that image is finite. We may consequently apply finite local Galois theory to the finite twist. This reduction is valid for every nonarchimedean local field; no restriction to characteristic zero is introduced.

## 2. What induction from a quadratic extension gives

Let \(E/F\) be quadratic, \(H=W_E\), and choose \(t\in W_F\setminus H\). For a character \(\theta:H\to\mathbb C^\times\), write

\[
\theta^t(h)=\theta(tht^{-1}).
\]

Since \(t^2\in H\), conjugating twice acts trivially on characters. The conjugate character is independent of the representative of the nontrivial coset.

**Theorem 2.1.** The representation \(\operatorname{Ind}_{W_E}^{W_F}\theta\) is irreducible exactly when \(\theta\ne\theta^t\). In that case

\[
\operatorname{Ind}\theta\simeq\operatorname{Ind}\theta^t,
\qquad
\det(\operatorname{Ind}\theta)=\eta_{E/F}\,\theta|_{F^\times},
\tag{2.1}
\]

where the restriction in the second formula uses the inclusion \(F^\times\subset E^\times\), and \(\eta_{E/F}\) is the quadratic reciprocity character.

**Proof.** A basis indexed by the two cosets makes every \(h\in H\) act diagonally, with characters \(\theta\) and \(\theta^t\). The element \(t\) exchanges the two coordinate lines. If the characters are distinct, every \(H\)-stable line is a coordinate line, and neither is \(W_F\)-stable. The representation is irreducible. If they coincide, \(H\) acts by scalars; \(t\) is diagonalizable because its square is a nonzero scalar. Its two eigenlines are invariant. This proves both implications. Exchanging the coset labels proves the first isomorphism in (2.1).

For the determinant, let \(\operatorname{Ver}:W_F^{\mathrm{ab}}\to W_E^{\mathrm{ab}}\) denote transfer. On \(h\in H\), transfer is represented by \(h(tht^{-1})\), and on \(t\) it is represented by \(t^2\). Thus the determinant is \(\theta\circ\operatorname{Ver}\) on \(H\), while on \(t\) it is \(-\theta(t^2)\). The sign is precisely the character of \(W_F/H\). Compatibility of reciprocity with transfer identifies \(\theta\circ\operatorname{Ver}\) with \(\theta|_{F^\times}\). This gives (2.1) on both cosets. \(\square\)

The determinant includes the quadratic character even when \(\theta\) is unramified. Omitting it changes the central character in the local correspondence.

**Proposition 2.2.** Every irreducible two-dimensional representation preserving an unordered pair of distinct lines is induced from a character of a subgroup \(W_E\) for a quadratic extension \(E/F\).

**Proof.** The action on the two lines is transitive, since a fixed line would contradict irreducibility. Its kernel \(H\) has index two. The permutation character is smooth, and an index-two subgroup of a Weil group is the Weil group of the quadratic extension defined by that character. The action of \(H\) on one line is a character \(\theta\). The two lines, exchanged by the other coset, give exactly the matrices of \(\operatorname{Ind}_H^{W_F}\theta\). \(\square\)

We call these representations **dihedral**. We include the Klein four projective image in this term: the dihedral group of order four is the Klein four-group.

## 3. Why odd residue characteristic forces induction

We need a small fact about finite \(p\)-groups. Its proof also explains why the argument fails at \(p=2\).

**Lemma 3.1.** The dimension of an irreducible complex representation of a finite \(p\)-group is a power of \(p\).

**Proof.** Induct on the group order. A nontrivial finite \(p\)-group has a normal subgroup \(H\) of index \(p\). To see this, use its nontrivial center: if the group is abelian it has a quotient of order \(p\); otherwise apply induction to its quotient by the center and pull back a subgroup of index \(p\).

Let \(V\) be irreducible and choose an irreducible constituent \(U\) of \(V|_H\). Semisimplicity holds by averaging. Conjugation permutes the isotypic components of \(V|_H\) transitively, for their orbit sums are invariant in \(V\). There are either \(p\) distinct conjugates of \(U\) or just one.

In the first case, \(\operatorname{Ind}_H^G U\) is irreducible. Indeed, its restriction is the sum of \(p\) distinct irreducibles, and a nonzero invariant subspace must contain an entire constituent and then all its translates. Frobenius reciprocity gives a nonzero map from this induced representation to \(V\), hence an isomorphism. Thus \(\dim V=p\dim U\).

In the second case \(U\) extends to \(G\). If \(gH\) generates \(G/H\), choose an intertwiner \(A\) implementing conjugation by \(g\) on \(U\). The operator \(A^pU(g^p)^{-1}\) is scalar. Multiplying \(A\) by a suitable scalar makes it equal to one; the relation \(g^p\in H\) then defines the extension. The multiplicity space \(\operatorname{Hom}_H(U,V)\), after this extension is removed, is an irreducible representation of the cyclic quotient \(G/H\). It has dimension one. Hence \(\dim V=\dim U\). Both cases finish the induction. \(\square\)

**Theorem 3.2.** If \(p\ne2\), every irreducible smooth two-dimensional complex representation of \(W_F\) is dihedral.

**Proof.** Let \(P_F\) be wild inertia. Its image is a finite \(p\)-group. By Lemma 3.1 every constituent of the two-dimensional restriction to \(P_F\) has dimension one. There are two possibilities.

If the two characters of \(P_F\) are distinct, their eigenspaces are two distinct lines. Since \(P_F\) is normal in \(W_F\), the Weil group permutes these lines. Proposition 2.2 applies.

If the characters coincide, wild inertia acts by scalars. The projective image of inertia therefore factors through tame inertia, which is procyclic. Let \(C\) be this finite cyclic projective image. If \(C=1\), the full representation is generated by scalar inertia and one Frobenius matrix; that matrix has an eigenline, contradicting irreducibility. Thus \(C\ne1\).

A nontrivial finite-order projective transformation of the complex projective line has exactly two fixed points. For a cyclic group \(C\), these are the common fixed points of any generator. Inertia is normal in the Weil group, so its projective normalizer preserves this unordered pair of points. The corresponding pair of lines in \(\mathbb C^2\) is preserved by \(W_F\). Proposition 2.2 again applies. \(\square\)

The scalar-wild-inertia case does not require extending a wild character to all of \(W_F\). Passing to projective inertia avoids that additional problem. At \(p=2\), wild inertia can itself have an irreducible constituent of dimension two; this is the place where the proof stops working.

## 4. The possible projective groups

**Lemma 4.1.** Every finite Galois group of a nonarchimedean local field is solvable.

**Proof.** For a finite Galois extension \(L/F\), its wild inertia is a finite \(p\)-group. Every finite \(p\)-group is solvable, by the same induction through its nontrivial center used above. The quotient of inertia by wild inertia is cyclic: it embeds, through the action on a uniformizer, in the multiplicative group of the residue field of \(L\). The quotient by inertia is the cyclic Galois group of finite residue fields. A group with a solvable normal subgroup and solvable quotient is solvable, because its derived series first enters the normal subgroup and then terminates. Apply this twice. \(\square\)

For completeness we record the geometric group classification needed here, including why the nonsolvable possibility is excluded.

**Lemma 4.2.** A finite subgroup of \(\operatorname{PGL}_2(\mathbb C)\) is cyclic, dihedral, tetrahedral \(A_4\), octahedral \(S_4\), or icosahedral \(A_5\).

**Proof.** Lift the group to its finite inverse image in \(\operatorname{SL}_2(\mathbb C)\), and average a positive Hermitian form. Conjugation then places it in \(\operatorname{SU}(2)\), whose projective action is the rotation action on the sphere. A point stabilizer is cyclic, consisting of rotations about its axis.

Write \(g\) for the group order and \(m_1,\ldots,m_r\ge2\) for the stabilizer orders of the exceptional point orbits. Count pairs consisting of a nonidentity rotation and one of its two fixed points. An exceptional orbit contributes \((g/m_i)(m_i-1)\). Consequently

\[
\sum_{i=1}^r(1-m_i^{-1})=2-2/g.
\tag{4.1}
\]

The quotient of the sphere is an orientable compact surface. Triangulate it with the exceptional images as vertices and lift the triangulation. The Euler formula is

\[
2=g\left(2-2h-\sum_i(1-m_i^{-1})\right),
\]

where \(h\) is its genus. Equation (4.1) gives \(h=0\). Small loops around the exceptional images generate the group, have orders \(m_i\), and their product is one. More precisely, the sphere minus the exceptional images has fundamental group generated by these loops with this one product relation; filling their lifted punctures adds the relations that the \(m_i\)-th powers are one. Its resulting covering is the simply connected sphere. Thus these relations present the rotation group itself.

Equation (4.1) gives \(r\le3\). The two-orbit case forces \(m_1=m_2=g\), and gives a cyclic group. In the three-orbit case, order the \(m_i\). The strict inequality \(m_1^{-1}+m_2^{-1}+m_3^{-1}>1\) gives exactly

\[
(2,2,m),\quad(2,3,3),\quad(2,3,4),\quad(2,3,5).
\]

Their orders from (4.1) are \(2m,12,24,60\). The first presentation reduces to two involutions whose product has order \(m\), the dihedral group. For the other three, the triangle presentations have surjections onto the following permutation groups. Take generators of orders two and three with products of the third indicated order:

\[
\begin{array}{c|c|c|c}
(m_1,m_2,m_3)&x&y&\langle x,y\rangle\\\hline
(2,3,3)&(12)(34)&(123)&A_4\\
(2,3,4)&(12)&(234)&S_4\\
(2,3,5)&(12)(34)&(135)&A_5.
\end{array}
\]

In the first row the generators give the three double transpositions and a three-cycle. In the second, conjugating the transposition by the three-cycle gives transpositions connecting all four letters. In the third the product is a five-cycle; the generated subgroup has order divisible by \(2,3,5\), hence order \(30\) or \(60\) in \(A_5\). Order \(30\) would give a quotient of \(A_5\) of order two. Such a quotient is impossible because \(A_5\) is generated by three-cycles, which all map trivially to a group of order two. Hence the subgroup has order \(60\). The orders agree with those already computed, so the surjections are isomorphisms. \(\square\)

**Theorem 4.3.** The projective image of an irreducible smooth two-dimensional Weil representation is dihedral, \(A_4\), or \(S_4\). In the odd-residue-characteristic case it is dihedral.

**Proof.** Proposition 1.1 and Lemma 4.1 make the projective image finite and solvable. Lemma 4.2 lists the possibilities. A cyclic projective image makes all representing matrices scalar multiples of powers of one diagonalizable matrix, so the representation is reducible. The \((2,3,5)\) triangle presentation has trivial abelianization: in an abelian quotient, \(2x=3y=5z=0\) and \(x+y+z=0\), which force each generator to vanish by coprimality. Its nontrivial group is therefore perfect and cannot be solvable. This excludes \(A_5\). Finally use Theorem 3.2. \(\square\)

An irreducible representation is called **primitive** if it is not induced from a quadratic extension. In dimension two these are precisely the tetrahedral and octahedral cases. Indeed, a dihedral projective group preserves the pair of endpoints of its rotation axis, so Proposition 2.2 applies. Conversely, the matrices of an induced representation preserve two lines, and their projective image is dihedral. Existence of primitive dyadic representations is a further arithmetic theorem of Weil; it is stated here, not constructed.

## 5. Two explicit families

Let \(E/F\) be unramified quadratic. Choose a character \(\bar\theta\) of \(\mathbb F_{q^2}^{\times}\) with \(\bar\theta\ne\bar\theta^q\). Inflate it to \(\mathcal O_E^\times\), make it trivial on \(1+\mathfrak p_E\), and prescribe any nonzero value on a uniformizer. The resulting \(\theta\) gives an irreducible induced parameter. Its projective rotation subgroup has order

\[
m=\operatorname{ord}(\bar\theta/\bar\theta^q),
\]

and the full projective image has order \(2m\). Both inertia characters are nontrivial: a trivial character is conjugation-invariant. Thus the Artin conductor is two, since the representation has no inertia invariants and wild inertia is trivial. This uses the Artin conductor formula, with zero Swan term.

For a concrete parameter over \(\mathbb Q_3\), let \(\bar\theta\) have order eight on \(\mathbb F_9^\times\). The conjugate is \(\bar\theta^3\), their quotient has order four, and the projective image is dihedral of order eight. The inertia determinant is \(\bar\theta^4\), a quadratic character. Its Frobenius determinant is \(-\theta(3)\), because Frobenius exchanges the two lines. These computations are compatible with (2.1).

There is also a particularly useful Klein four example. Put

\[
L=\mathbb Q_3(i,\alpha),\qquad i^2=-1,\quad\alpha^4=3.
\]

The extension \(\mathbb Q_3(i)/\mathbb Q_3\) is unramified quadratic because \(X^2+1\) is irreducible modulo three. The polynomial \(X^4-3\) is Eisenstein over this extension, so \([L:\mathbb Q_3]=8\). It contains every root \(\alpha,i\alpha,-\alpha,-i\alpha\), hence is Galois. Define

\[
a(\alpha)=i\alpha,\quad a(i)=i,
\qquad
b(\alpha)=\alpha,\quad b(i)=-i.
\]

Then \(a^4=b^2=1\) and \(bab=a^{-1}\). These eight automorphisms give the dihedral group of order eight. Its faithful two-dimensional representation is

\[
r(a)=\begin{pmatrix}i&0\\0&-i\end{pmatrix},
\qquad
r(b)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{5.1}
\]

The center \(\langle a^2\rangle\) acts by \(-1\), so the projective image is the Klein four-group. Its three subgroups of index two lift to

\[
\langle a\rangle,
\quad\langle a^2,b\rangle,
\quad\langle a^2,ab\rangle.
\]

Each is abelian, each has two distinct eigencharacters in (5.1), and the other coset exchanges their eigenlines. The same parameter is induced from all three quadratic extensions

\[
\mathbb Q_3(i),\quad\mathbb Q_3(\sqrt3),\quad\mathbb Q_3(\sqrt{-3}).
\]

For the first subgroup the inducing character sends \(a\) to \(i\). For the second it sends \(a^2\) to \(-1\) and \(b\) to \(1\). For the third it sends \(a^2\) to \(-1\) and \(ab\) to \(1\). These formulas specify the characters on the indicated finite Galois quotients, hence the Weil characters completely.

**Example 5.2.** A Klein four projective parameter exists over every field with odd residue cardinality \(q\), including \(q\equiv1\pmod4\). In the unramified quadratic extension, take a residue character \(\bar\theta\) of order \(2(q-1)\), and set its uniformizer value to one. This order divides \(q^2-1\), since \(q+1\) is even. The character \(\bar\theta/\bar\theta^q=\bar\theta^{1-q}\) has order two and is nontrivial. The induced representation is therefore irreducible and has projective image of order four by Exercise 6.2. For \(q=5\), a character of order eight on \(\mathbb F_{25}^\times\) gives this example. Its finite linear lift need not be the order-eight dihedral group used over \(\mathbb Q_3\); the projective parameter is what matters.

## 6. Exercises with solutions

**Exercise 6.1 (easy).** For unramified quadratic \(E/F\) and an unramified character \(\theta\) with \(\theta(\varpi_E)=c\), compute \(\det\operatorname{Ind}\theta\). Is the induced representation irreducible?

**Solution.** Inertia acts trivially. A geometric Frobenius matrix has the form \(\left(\begin{smallmatrix}0&c\\1&0\end{smallmatrix}\right)\), up to the coset basis convention. Its determinant is \(-c\). Thus the determinant is the unramified character with uniformizer value \(-c\), exactly \(\eta_{E/F}\theta|_{F^\times}\). Since conjugation fixes an unramified character, \(\theta=\theta^t\); the induction is the sum of the two unramified characters whose uniformizer values are the square roots \(\pm\sqrt c\).

**Exercise 6.2 (medium).** Suppose \(\theta\ne\theta^t\). If \(m\) is the order of \(\theta/\theta^t\), prove that the induced representation has projective image of order \(2m\).

**Solution.** On \(W_E\), divide the diagonal matrices by their first entry. Their image is the cyclic group formed by \(\theta^t/\theta\), of order \(m\). The other coset acts by an antidiagonal matrix, whose square is scalar and which inverts this diagonal group. It is outside the diagonal group, so the union has exactly \(2m\) elements. Irreducibility gives \(m\ge2\). Proposition 1.1 shows that \(m\) is finite even when \(\theta\) itself has infinite image.

**Exercise 6.3 (medium).** Show that \(G_F\) is prosolvable. Explain why this does not mean it is abelian.

**Solution.** Every finite continuous quotient of \(G_F\) is the Galois group of a finite Galois extension, and Lemma 4.1 makes it solvable. The profinite group is the inverse limit of these finite quotients, which is the definition of prosolvable. The order-eight dihedral extension in Section 5 is a nonabelian quotient. Thus prosolvability permits noncommuting elements and does not imply a fixed bound on the derived length of all finite quotients.

**Exercise 6.4 (hard).** Prove that an irreducible two-dimensional Weil representation is induced from three different quadratic extensions exactly when its projective image is the Klein four-group. Apply the result to (5.1).

**Solution.** Write \(X(r)=\{\eta:r\otimes\eta\simeq r\}\). Every self-twist satisfies \(\eta^2=1\), by determinants. If \(\eta\ne1\), choose an intertwiner \(A\) with \(Ar(w)A^{-1}=\eta(w)r(w)\). Schur's lemma gives \(A^2\) scalar, and \(A\) is nonscalar; after rescaling it has eigenvalues \(1,-1\). Its two eigenlines are preserved by \(\ker\eta\) and exchanged by the other coset. Thus \(r\) is induced from the quadratic field belonging to \(\eta\). Conversely the sign matrix on the two inducing lines supplies this intertwiner. Quadratic inducing fields therefore correspond exactly to the nontrivial elements of \(X(r)\).

The conjugation representation on \(\operatorname{End}(\mathbb C^2)\) contains each self-twist character once: an intertwiner spans its character eigenspace by Schur's lemma. Hence \(|X(r)|\le4\). If there are three inducing fields, there are four self-twists, and these four one-dimensional eigenspaces fill the endomorphism algebra. Projective conjugation consequently acts through their quadratic values and has abelian exponent-two image. Its action is faithful on the projective image: a matrix commuting with every endomorphism is scalar. A finite abelian projective subgroup supporting an irreducible two-dimensional lift is the Klein four-group, by Lemma 4.2 and the exclusion of the cyclic case.

Conversely, for Klein four projective image, lifts of two distinct nontrivial elements can be taken as the diagonal and antidiagonal matrices in (5.1). Conjugation on the identity and the three traceless matrices gives the four characters of the Klein four-group. They are exactly the four self-twists, so there are three quadratic inducing fields. Section 5 supplies them and their inducing characters explicitly. \(\square\)

## What this lesson does not prove

The unramified finite-image reduction and extension to the absolute Galois group are the prerequisite Representations of Weil groups, Theorem 2.2, used in Section 1.

Local reciprocity, including its transfer compatibility, is used in Theorem 2.1; a precise reference is [Fesenko–Vostokov 2002, Chapter IV, §§2–4, especially (3.6)]. The structure of wild and tame inertia used in Theorem 3.2 and Lemma 4.1 is the local ramification theorem [Fesenko–Vostokov 2002, Chapter II, (4.4)]. The Artin conductor formula in Section 5 is the definition in [Deligne 1973, §4]. Existence and the arithmetic classification of primitive dyadic parameters are not proved here; the original reference is [Weil 1974]. None of the induction, determinant, odd-characteristic, projective-group or self-twist arguments above depends on that existence theorem.

## References

- [Deligne 1973] P. Deligne, [*Les constantes des équations fonctionnelles des fonctions L*](https://publications.ias.edu/sites/default/files/Number20.pdf), in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349, Springer, 1973, 501–597, §§2 and 4.
- [Getz–Hahn 2022] J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§12.1–12.2; published as Graduate Texts in Mathematics 300, Springer, 2024.
- [Fesenko–Vostokov 2002] I. B. Fesenko and S. V. Vostokov, [*Local Fields and Their Extensions*](https://ivanfesenko.org/wp-content/uploads/2021/10/vol.pdf), second edition, Translations of Mathematical Monographs 121, American Mathematical Society, 2002, Chapters II and IV.
- [Weil 1974] A. Weil, [*Exercices dyadiques*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0027/LOG_0007.pdf), Inventiones Mathematicae 27 (1974), 1–22.
