# Beyond general linear groups: parameters and packets

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

For \(\mathrm{GL}_n\), a parameter identifies one irreducible representation. Passing to \(\mathrm{SL}_2\) already changes this: restricting one representation of \(\mathrm{GL}_2(F)\) can produce two or four inequivalent irreducibles. They share a projective parameter. We explain the general packet formulation, prove the restriction and counting arguments, and calculate both sizes explicitly.

Here \(F\) is a finite extension of \(\mathbb Q_p\). This keeps the restriction statements within the hypotheses of the cited local theorem, including when \(p=2\). The earlier positive-characteristic existence theorem for \(\mathrm{GL}_n\) remains a separate result.

## 1. Dual groups and full local parameters

Let \(G\) be a connected reductive group over \(F\). A based root datum consists of the character and cocharacter lattices, the roots and coroots, and a choice of simple roots:
\[
\bigl(X^*(T),\Phi,X_*(T),\Phi^\vee,\Delta\bigr).
\]
Exchanging the two lattices and the roots with the coroots defines the complex dual group \(\widehat G\). The Galois action on the based datum acts through pinned automorphisms of \(\widehat G\). Its restriction to \(W_F\) gives
\[
{}^LG=\widehat G\rtimes W_F.
\tag{1.1}
\]
The action has finite image. For split \(G\), (1.1) is a direct product. Inner forms have the same based dual datum and the same \(L\)-group; their relevant parameters and packet enhancements carry the additional information.

Some split examples make the exchange visible.

| \(G\) | \(\widehat G\) |
| --- | --- |
| \(\mathbb G_m\) | \(\mathbb C^\times\) |
| \(\mathrm{GL}_n\) | \(\mathrm{GL}_n(\mathbb C)\) |
| \(\mathrm{SL}_n\) | \(\mathrm{PGL}_n(\mathbb C)\) |
| \(\mathrm{PGL}_n\) | \(\mathrm{SL}_n(\mathbb C)\) |
| \(\mathrm{Sp}_{2n}\) | \(\mathrm{SO}_{2n+1}(\mathbb C)\) |
| \(\mathrm{SO}_{2n+1}\) | \(\mathrm{Sp}_{2n}(\mathbb C)\) |

The simply connected and adjoint forms exchange because the root and weight lattices exchange. For example, \(\mathrm{SL}_2\) has roots \(\pm2\) in its character lattice \(\mathbb Z\) and coroots \(\pm1\) in its cocharacter lattice. The exchanged datum is that of \(\mathrm{PGL}_2\).

An \(L\)-parameter is a \(\widehat G\)-conjugacy class of homomorphisms
\[
\phi:W_F\times\mathrm{SL}_2(\mathbb C)\longrightarrow{}^LG
\tag{1.2}
\]
Its projection to \(W_F\) sends \((w,h)\) to \(w\). Write
\[
\phi(w,1)=(c(w),w),\qquad
c(wu)=c(w)\,a(w)(c(u)),
\tag{1.2a}
\]
where \(a(w)\) is the pinned action. Choose a finite Galois quotient \(\Gamma\) through which that action factors. The quotient homomorphism
\(\widehat G\rtimes W_F\to\widehat G\rtimes\Gamma\) sends \((g,w)\) to \((g,\bar w)\).
Admissibility requires a continuous Weil restriction whose images in this finite-action target are semisimple, a finite image of \(c|_{I_F}\), and an algebraic restriction to \(\mathrm{SL}_2(\mathbb C)\). Equivalently, the inertia image in \(\widehat G\rtimes\Gamma\) is finite: it is contained in \(c(I_F)\times\Gamma\), and its first coordinates recover \(c(I_F)\), proving both implications.

The full inertia image in (1.1) is infinite, since its projection is the identity on \(I_F\). Inertia is itself infinite: its tame quotients have every order prime to \(p\), obtained by adjoining corresponding roots of a uniformizer over the maximal unramified extension. Thus the finite condition concerns the dual coordinate, rather than the entire Weil-form target. For split \(G\), the parameter \(\phi(w,h)=(1,w)\) satisfies it. We impose the usual relevance condition for the chosen form of \(G\): parabolic \(L\)-subgroups containing the image must correspond to \(F\)-parabolic subgroups of that form.

Write
\[
S_\phi=Z_{\widehat G}(\operatorname{im}\phi),\qquad
\mathcal S_\phi=\pi_0\bigl(S_\phi/Z(\widehat G)^{W_F}\bigr).
\tag{1.3}
\]
The fixed center is contained in \(S_\phi\), and \(\mathcal S_\phi\) is a finite group. A parameter is tempered if the \(\widehat G\)-coordinates of \(\phi(w,1)\), for \(w\in W_F\), have compact closure. Boundedness is a condition on this Weil restriction. A nontrivial algebraic \(\mathrm{SL}_2(\mathbb C)\)-factor is not bounded and is nevertheless allowed in a tempered parameter.

A tempered parameter is discrete when its image is in no proper relevant Levi \(L\)-subgroup; equivalently its centralizer modulo the fixed center is finite. This is the parameter condition corresponding to square integrability modulo the center.

For \(\mathrm{GL}_n\), the full parameter (1.2) and a Frobenius-semisimple Weil–Deligne pair are equivalent. The conversion retains the convention
\[
r(w)=\phi\left(w,
\begin{pmatrix}\|w\|^{1/2}&0\\0&\|w\|^{-1/2}\end{pmatrix}\right),
\qquad
N=d\phi\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad
r(w)Nr(w)^{-1}=\|w\|N.
\tag{1.4}
\]
In (1.4) we use the \(\mathrm{GL}_n(\mathbb C)\)-coordinate of \(\phi\). Here \(\operatorname{Art}_F(\varpi)=\Phi_F\) and \(\|\Phi_F\|=q^{-1}\). For a centered block \(S_k\), the Weil restriction of (1.2) is scalar on the \(k\)-dimensional algebraic factor, whereas the \(r\) in (1.4) has the centered norm weights. This distinction makes Steinberg tempered.

The ordinary reductive-group \(L\)-group should also be distinguished from that of a nonlinear covering group. [Gan–Gao–Weissman, §§1–3] develops central extensions, their universal extensions and their local structure. A covering group has extra extension data; the root-datum construction (1.1) alone does not supply its complete Langlands theory.

## 2. The packet conjecture

**Conjectural framework (stated).** The irreducible admissible representations of \(G(F)\) are partitioned into finite packets
\[
\operatorname{Irr}G(F)=\coprod_{\phi\in\Phi(G)}\Pi_\phi(G),
\tag{2.1}
\]
indexed by relevant parameters. Tempered representations correspond to bounded Weil parameters. In the tempered part, square-integrable representations modulo the center correspond to discrete parameters. Induction from a Levi is compatible with the inclusion of its \(L\)-group. The nontempered correspondence is formulated through the Langlands quotient classification.

For a quasi-split group, fixing a Whittaker datum is part of the internal normalization of a tempered packet. The expected internal parametrization uses
\[
\operatorname{Irr}(\mathcal S_\phi),
\tag{2.2}
\]
with the generic member corresponding to the trivial representation. “Irreducible representations” in (2.2) is essential: a general component group need not be abelian, so one cannot replace them all by one-dimensional characters. For inner forms, one uses a suitable central extension or enhanced component group, with central character prescribed by the inner-twist data. Pure and rigid inner twists organize this refinement; (2.2) without that data is not a statement covering all inner forms.

The tempered formulation and Whittaker normalization are [Getz–Hahn, §12.5, Conjectures 12.5.1, 12.5.3 and 12.5.4]; the quotient extension is explained in [Arthur, *Introduction to the trace formula*, §28, equation (28.9)]. These are conjectural assertions for a general group.

A partition alone would be too weak. Endoscopic character identities characterize how packet members combine. In the quasi-split tempered formulation, the stable packet distribution is weighted by the dimensions of the representations in (2.2); more generally, evaluation at an element of \(\mathcal S_\phi\) gives the coefficients of an endoscopic transfer. For abelian component groups these dimensions are all one. Changing the Whittaker datum can change the labels.

Why are general-linear packets singletons? Write a full parameter as
\[
V=\bigoplus_i U_i\otimes M_i,
\tag{2.3}
\]
where the \(U_i\) are pairwise inequivalent irreducible representations of \(W_F\times\mathrm{SL}_2(\mathbb C)\), and \(M_i\) are their multiplicity spaces. Complete reducibility follows from finite inertia, Frobenius semisimplicity and the algebraic \(\mathrm{SL}_2\)-representation, as in the earlier parameter classification. Schur's lemma says that a commuting endomorphism is identity on each \(U_i\) and arbitrary on \(M_i\). Its invertible elements therefore form
\[
S_\phi\simeq\prod_i\mathrm{GL}(M_i).
\tag{2.4}
\]
Each factor is connected. The quotient by the scalar center is connected too, so \(\mathcal S_\phi=1\). Repeated summands require the general linear factors in (2.4), rather than just scalar tori. The trivial component group agrees with the singleton bijection proved earlier.

## 3. Restriction to \(\mathrm{SL}_2\): the precise input

Put \(G_2=\mathrm{GL}_2(F)\), \(H=\mathrm{SL}_2(F)\), and let \(Z\) be the center of \(G_2\).

**Theorem 3.1 (restriction theorem, stated).** For an irreducible admissible representation \(\pi\) of \(G_2\), its restriction to \(H\) is a finite direct sum of pairwise inequivalent irreducible admissible representations. Every irreducible admissible representation of \(H\) occurs in such a restriction. The sets of constituents are the \(L\)-packets of \(H\).

The finite decomposition and lifting are [Labesse–Langlands, §2, Lemmas 2.4–2.5], and multiplicity one is [Lemma 2.6]. The definition and partition into local \(L\)-indistinguishability classes follow Lemma 2.8. With the \(\mathrm{GL}_2\) correspondence, the packet's parameter is the projectivization
\[
\overline\phi:W_F\times\mathrm{SL}_2(\mathbb C)
\xrightarrow{\operatorname{rec}\pi}\mathrm{GL}_2(\mathbb C)
\longrightarrow\mathrm{PGL}_2(\mathbb C).
\tag{3.1}
\]
A determinant twist does not change (3.1) or the restriction to \(H\).

We use the finite decomposition as input and prove the Clifford and counting assertions ourselves.

**Proposition 3.2 (transitivity and stabilizer).** The constituents of \(\pi|_H\) form one \(G_2\)-orbit. If \(\tau\) is a constituent and \(S\) its stabilizer in \(G_2\), their number is exactly
\[
k=[G_2:S].
\tag{3.2}
\]
The subgroup \(S\) contains \(ZH\) and is open.

**Proof.** Normality of \(H\) makes \(\pi(g)V_\tau\) an \(H\)-subrepresentation with conjugate action, for every \(g\in G_2\). The direct sum of constituent spaces in any orbit is \(G_2\)-stable. It is nonzero, so irreducibility of \(\pi\) says it is the whole space. Thus there is only one orbit. The map \(gS\mapsto g\cdot\tau\) is well-defined, surjective and injective by the definition of stabilizer, proving (3.2).

Elements of \(H\) preserve every constituent space, and the center acts by the central character of \(\pi\); hence \(ZH\subset S\). To prove openness, take a nonzero vector \(v\in V_\tau\). Smoothness gives a compact open subgroup \(K_v\) fixing \(v\). For \(g\in K_v\), the spaces \(V_\tau\) and \(\pi(g)V_\tau\) intersect in \(v\). In a multiplicity-free direct sum of inequivalent irreducibles this forces equality. Thus \(K_v\subset S\). The index in (3.2) is finite, and in particular the constituent number divides that index, with equality. ∎

## 4. Counting by self-twists, with proof

Define the finite self-twist group
\[
X(\pi)=\{\chi:F^\times\longrightarrow\mathbb C^\times
\text{ smooth character}:\pi\otimes(\chi\circ\det)\simeq\pi\}.
\tag{4.1}
\]

**Proposition 4.1.** Assuming Theorem 3.1,
\[
k=|X(\pi)|.
\tag{4.2}
\]
More precisely, \(X(\pi)\) is the character group of \(G_2/S\).

**Proof.** Since \(H\subset S\) and \(G_2/H\simeq F^\times\) by determinant, \(S\) is the preimage of a subgroup of this abelian group. It is therefore normal. The finite quotient \(A=G_2/S\) acts freely and transitively on the \(k\) constituent spaces. Label them \(V_a\) for \(a\in A\), with \(V_1=V_\tau\).

For a character \(\chi\) of \(A\), define \(T_\chi\) to be multiplication by \(\chi(a)\) on \(V_a\). Every multiplier is nonzero, so \(T_\chi\) is invertible. If \(g\) has image \(b\in A\), then \(\pi(g)V_a=V_{ba}\), and hence
\[
T_\chi\pi(g)=\chi(b)\pi(g)T_\chi.
\tag{4.3}
\]
This is an intertwiner from \(\pi\) to its twist. Since \(S\) is open, the inflated character is smooth and belongs to (4.1).

Conversely, a self-twist has an invertible intertwiner \(T\) satisfying (4.3). It commutes with \(H\). Schur's lemma and multiplicity one force
\[
T|_{V_a}=t_a\,\operatorname{id},\qquad t_a\ne0.
\]
For \(s\in S\), restrict (4.3) to \(V_1\): both sides have the same nonzero scalar \(t_1\), so \(\chi(\det s)=1\). Thus \(\chi\) factors through \(A\). All self-twists are precisely its characters. A finite abelian group has as many complex characters as elements: decompose it into cyclic groups, each with its full set of roots-of-unity characters, and take products. Therefore \(|X(\pi)|=|A|=k\). ∎

Every \(\chi\in X(\pi)\) satisfies
\[
\chi^2=1.
\tag{4.4}
\]
Indeed, the scalar matrix \(zI\) acts on the twist by \(\omega_\pi(z)\chi(z^2)\). Equality of central characters and cancellation of \(\omega_\pi(z)\ne0\) give \(\chi(z)^2=1\) for every \(z\in F^\times\).

The earlier rank-two classification and parameter twist compatibility now give \(k\in\{1,2,4\}\). A determinant character has only the trivial self-twist, since determinant is surjective. A special representation \(\mathrm{St}_2\otimes\mu\) also has only the trivial one: its full parameter is \(\widehat\mu\otimes\operatorname{Std}_{\mathrm{SL}_2}\), whose commuting algebra on the algebraic \(\mathrm{SL}_2\)-factor is scalar. The principal-series case is calculated next. For supercuspidals, the dimension-four endomorphism argument in Section 6 proves the remaining bound.

## 5. A two-element packet and the dihedral self-twist

Let \(\eta\ne1\) be a quadratic character and let
\[
\pi=I(\mu,\mu\eta)
\]
be normalized induction for \(\mathrm{GL}_2(F)\). The ratio \(\eta\) is different from \(\nu^{\pm1}\), so this representation is irreducible. Twisting replaces its unordered inducing pair by \(\{\mu\chi,\mu\eta\chi\}\). Equality with the original unordered pair gives either \(\chi=1\) or \(\chi=\eta\), and both work. Hence
\[
X(\pi)=\{1,\eta\},\qquad |\Pi_{\overline\phi}(\mathrm{SL}_2)|=2.
\tag{5.1}
\]
On the diagonal \(\operatorname{diag}(a,a^{-1})\), the inducing character restricts to \(\eta(a)\). Every element of \(G_2\) lies in \(B_{G_2}H\), since the determinant map on \(B_{G_2}\) is surjective, and \(B_{G_2}\cap H=B_H\). Restricting the induction functions therefore identifies the two induced spaces. The modulus factors for the two Borels agree there. Thus the restriction is the normalized principal series
\[
\operatorname{Ind}_{B_H}^{H}\eta=\tau_+\oplus\tau_-.
\tag{5.2}
\]
There is a concrete description of its summands. Choose the nontrivial self-twist intertwiner \(T\) from Proposition 4.1. It acts by \(1\) on \(V_1\) and \(-1\) on the other constituent. Then \(T^2=1\), both eigenspaces are nonzero, and
\[
\tau_\pm=\ker(T\mp1).
\tag{5.3}
\]
They are irreducible and inequivalent by Theorem 3.1. The labels can be reversed; a Whittaker normalization fixes which member is generic. Equations (5.1)–(5.3) fully specify the decomposition without assuming that the two representations are isomorphic.

Now let \(E/F\) be quadratic, let \(\theta\ne\theta^\sigma\), and put \(r=\operatorname{Ind}_{W_E}^{W_F}\widehat\theta\). Write \(\eta_{E/F}\) for the quadratic character trivial on \(W_E\).

**Proposition 5.1 (dihedral self-twist).**
\[
r\otimes\eta_{E/F}\simeq r,\qquad
\pi(\theta)\otimes(\eta_{E/F}\circ\det)\simeq\pi(\theta).
\tag{5.4}
\]
Consequently its \(\mathrm{SL}_2\)-packet has at least two members.

**Proof.** In the two-coset induction basis, \(W_E\) acts diagonally through \(\widehat\theta\) and \(\widehat\theta^\sigma\); every element outside \(W_E\) exchanges the two lines. The matrix \(D=\operatorname{diag}(1,-1)\) commutes with the diagonal matrices and changes the sign of each exchanging matrix under conjugation. Therefore
\[
Dr(w)D^{-1}=\eta_{E/F}(w)r(w)
\]
for every \(w\), providing the intertwiner. Alternatively induction commutes with tensoring and \(\eta_{E/F}|_{W_E}=1\). The parameter has \(N=0\). Twist compatibility and injectivity of LLC prove the second identity in (5.4), whether \(\theta\) denotes the parameter character directly or an automorphic admissible-pair character with its rectifier. The nontrivial quadratic character lies in \(X(\pi(\theta))\); (4.2) proves the packet bound. ∎

## 6. Four members exactly for projective Klein-four image

**Proposition 6.1.** A rank-two packet has four members precisely when its full projective parameter has image
\[
V_4\simeq(\mathbb Z/2\mathbb Z)^2.
\tag{6.1}
\]
Such a parameter has trivial algebraic \(\mathrm{SL}_2\)-factor and an irreducible two-dimensional Weil lift.

**Proof.** First let \(r\) be irreducible. A self-twist \(\chi\) has an invertible matrix \(T_\chi\) with
\[
T_\chi r(w)T_\chi^{-1}=\chi(w)r(w).
\tag{6.2}
\]
The determinant implies \(\chi^2=1\). Schur's lemma says the intertwiner line for each \(\chi\) has dimension one. Distinct characters give independent eigenvectors for conjugation on \(\operatorname{End}(\mathbb C^2)\). One can verify independence by applying conjugation by a Weil element that distinguishes two characters to a shortest hypothetical linear relation and subtracting a scalar multiple of that relation. Its shorter nonzero relation is impossible. Thus there are at most four self-twists. They form a finite group of exponent two, so their number is \(1,2\), or \(4\).

If there are four, choose independent nontrivial characters with intertwiners \(A,B\). Each matrix has scalar square, since twisting twice is trivial. Its trace is zero: some Weil element conjugates it to its negative. Rescale so \(A^2=B^2=1\). The products \(AB\) and \(BA\) intertwine the same twist, so \(AB=cBA\); determinants give \(c^2=1\). If \(c=1\), diagonalizing the nonscalar involution \(A\) makes \(B\) diagonal too, and \(1,A,B,AB\) span at most a two-dimensional space. They instead lie in four independent character lines. Hence \(c=-1\). In a suitable basis,
\[
A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
B=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{6.3}
\]
Their common centralizer in \(\mathrm{PGL}_2(\mathbb C)\) is exactly the four classes of \(1,A,B,AB\): projective commutation with \(A\) forces a matrix to be diagonal or off-diagonal, and commutation with \(B\) leaves two classes of each kind. Equation (6.2) makes the projective image of \(r\) lie in this group. A proper subgroup is trivial or cyclic of order two. Its lifts would be scalar multiples of powers of one diagonalizable matrix, preserving its eigenlines; this contradicts irreducibility. Thus the projective image is all \(V_4\).

Conversely, suppose the projective image is \(V_4\). Its common projective centralizer is the same \(V_4\). Each of the four centralizing classes has a lift \(T\), and
\[
Tr(w)T^{-1}=\chi_T(w)r(w)
\]
defines a character: multiplication of two Weil elements proves multiplicativity, continuity follows from the representation, and determinants give \(\chi_T^2=1\). Two classes yielding the same character differ by a scalar, by Schur's lemma. Thus they give four distinct self-twists. Equation (4.2) gives four constituents.

The other rank-two types cannot give four: determinant and special representations have only one self-twist; an irreducible principal series has at most the two choices obtained by permuting its inducing pair. Conversely a finite full projective image cannot contain a nontrivial algebraic image of the connected group \(\mathrm{SL}_2(\mathbb C)\). A reducible semisimple Weil lift has projective image in a torus, whose finite subgroups are cyclic, so it cannot give \(V_4\). This completes both directions for all types. ∎

For odd residue characteristic, these parameters exist for every residue cardinality \(q\). Let \(E/F\) be unramified quadratic and choose a tame character of \(E^\times\) whose residue character has order \(2(q-1)\), possible since this divides \(q^2-1\). On inertia, \(\theta^\sigma=\theta^q\), so \(\theta/\theta^\sigma=\theta^{1-q}\) is nontrivial quadratic. The character is regular. The induced representation's projective inertia has order two. A Frobenius exchanges its two lines and has scalar square, so its projective class has order two and lies outside projective inertia. They commute projectively, giving \(V_4\). This argument also works when \(q\equiv1\pmod4\).

The narrower condition \(q\equiv-1\pmod4\) concerns a particular tame quotient with inertia of order four and a Frobenius that inverts it, yielding a dihedral group of order eight. That condition is not a condition on the existence of projective Klein-four parameters.

## 7. The four-element packet over \(\mathbb Q_3\)

Let \(\alpha^4=3\) and \(K=\mathbb Q_3(i,\alpha)\). The field \(\mathbb Q_3(i)\) is unramified quadratic because \(x^2+1\) is irreducible modulo three. The polynomial \(x^4-3\) is Eisenstein over it, so \([K:\mathbb Q_3]=8\). It contains all four roots and is Galois. Its automorphisms
\[
R(\alpha)=i\alpha,\quad R(i)=i;\qquad
S(\alpha)=\alpha,\quad S(i)=-i
\]
satisfy
\[
R^4=S^2=1,\qquad SRS^{-1}=R^{-1}.
\]
They generate the dihedral group of order eight. Its irreducible representation
\[
r(R)=\begin{pmatrix}i&0\\0&-i\end{pmatrix},
\qquad
r(S)=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\tag{7.1}
\]
is irreducible because \(R\) has two eigenlines and \(S\) exchanges them. Projectively, \(R\) and \(S\) are commuting independent involutions. Thus the image is \(V_4\), and the associated supercuspidal restricts to four inequivalent representations of \(\mathrm{SL}_2(\mathbb Q_3)\).

The self-twists are
\[
1,\quad\eta_{\mathbb Q_3(i)/\mathbb Q_3},\quad
\eta_{\mathbb Q_3(\sqrt3)/\mathbb Q_3},\quad
\eta_{\mathbb Q_3(\sqrt{-3})/\mathbb Q_3}.
\tag{7.2}
\]
To check the fields directly, \(S\) negates \(i\) and \(R\) fixes it; \(R\) negates \(\alpha^2=\sqrt3\) and \(S\) fixes it; both negate \(i\alpha^2=\sqrt{-3}\). These are the three nontrivial characters of the quotient by the commutator \(\langle R^2\rangle\). Matrices in the four classes of (6.3) realize their self-intertwiners.

In this example \(S_{\overline\phi}=V_4\) in \(\mathrm{PGL}_2\), whose center is trivial; hence \(\mathcal S_{\overline\phi}=V_4\). Its four one-dimensional characters account for the four split-group packet members. A Whittaker datum chooses the trivial label. An unramified scalar change in a two-dimensional lift, including a rectifier needed for an admissible-pair convention, does not change this projective packet.

## 8. Endoscopy and known classification results

For general groups, geometrically conjugate regular semisimple elements can split into several \(G(F)\)-conjugacy classes. A stable orbital integral sums the orbital integrals over that stable class. An endoscopic transfer uses specified transfer factors to form a weighted sum. Spectral transfer relates that geometric identity to a combination of characters within a packet. This is why the packet structure is part of the correspondence.

For unramified endoscopic data \(H_{\mathrm{end}}\) of \(G\), with compatible hyperspecial subgroups and normalized transfer factors, the ordinary fundamental lemma asserts
\[
SO_{\gamma_{\mathrm{end}}}(1_{K_{\mathrm{end}}})
=\sum_{\gamma\leftrightarrow\gamma_{\mathrm{end}}}
\Delta(\gamma_{\mathrm{end}},\gamma)\,O_\gamma(1_K).
\tag{8.1}
\]
Here \(\gamma_{\mathrm{end}}\) is strongly \(G\)-regular, the sum is over the matching ordinary conjugacy classes, and measures on corresponding centralizers are compatible. [Hales, §§6 and 8] gives the full normalization, including the importance of the base point.

**Fundamental-lemma theorem (stated).** Ngô proves the Lie-algebra identity and the nonstandard identity in [Ngô 2010, Introduction, Theorems 1–2; Theorems 1.11.1 and 1.12.7]. In those exact statements the residue characteristic is greater than twice the relevant Coxeter number; the nonstandard statement also retains the paired root data and the good-characteristic hypotheses specified in §1.12. The proof is geometric in equal characteristic; the mixed-characteristic and group versions use Waldspurger's reductions, described in that Introduction and in [Hales, §7]. The argument globalizes affine Springer fibers into the Hitchin fibration and compares their cohomology through the support theorem. This is an input to endoscopic classification, not a proof of every variant of a fundamental lemma.

**Classical-group classification (stated in its cited framework).** Over a characteristic-zero nonarchimedean local field, [Arthur 2012, Theorem 7.1(b)] partitions the tempered representations of quasi-split symplectic and special orthogonal groups into finite packets with their component-group labels. For even special orthogonal groups the theorem is formulated using the indicated outer-automorphism orbits. The precise trace-formula hypothesis is retained in [Getz–Hahn, Theorem 12.5.5 and §13.8]: stabilization of the twisted trace formula. Their Theorem 12.5.6 states the parallel quasi-split unitary result, citing [Mok 2015, Theorem 2.5.1], under that same framework.

Arthur's theorem also constructs packets for parameters with an additional algebraic factor,
\[
\psi:W_F\times\mathrm{SL}_2(\mathbb C)_{\mathrm{WD}}
\times\mathrm{SL}_2(\mathbb C)_{\mathrm{Arthur}}\longrightarrow{}^LG.
\tag{8.2}
\]
The second named factor in (8.2) organizes potentially nontempered automorphic contributions. Such Arthur packets are not the disjoint Langlands partition (2.1); their internal maps can have different fibers. [Arthur 2012, Theorem 7.1(a) and the remarks following it] explicitly makes this distinction. The global multiplicity formula is [Arthur 2012, Theorem 7.2], explained in [Getz–Hahn, §13.8].

Inner forms of general linear groups were treated by the Jacquet–Langlands lesson. For other inner forms, relevance and the enhanced internal labels must be supplied, rather than transferring the split packet cardinality unchanged. [Arthur, *Introduction to the trace formula*, §§27–30] explains the stable and spectral mechanisms and the dependence on ordinary, weighted and twisted inputs. Its 2005 statements are read with their stated hypotheses. The preceding lesson's Fargues–Scholze construction supplies general semisimple parameters and a spectral action; it does not by itself replace the full conjectural packet structure.

## 9. Exercises and complete solutions

**Exercise 9.1 (easy).** Prove that \(\pi\otimes(\chi\circ\det)\simeq\pi\) forces \(\chi^2=1\).

**Solution.** Evaluate the equality of central characters at \(zI\). Its determinant is \(z^2\), so \(\omega_\pi(z)\chi(z)^2=\omega_\pi(z)\). Since a character never vanishes, cancellation gives \(\chi(z)^2=1\) for every \(z\). The assertion holds for all the representation types, including characters of determinant.

**Exercise 9.2 (medium).** Decompose \(I(\mu,\mu\eta)|_H\) for a nontrivial quadratic \(\eta\).

**Solution.** The ratio of its inducing characters is \(\eta\), which is different from \(\nu^{\pm1}\); the general-linear principal series is irreducible. Restricting its inducing data to \(\operatorname{diag}(a,a^{-1})\) gives \(\eta(a)\), with the same normalized modulus. Its self-twists must permute \(\{\mu,\mu\eta\}\), giving exactly \(1,\eta\). Proposition 4.1 therefore gives precisely two irreducible constituents. On their spaces choose the self-twist operator with eigenvalues \(1,-1\). Its eigenspaces give
\[
\operatorname{Ind}_{B_H}^{H}\eta=\ker(T-1)\oplus\ker(T+1).
\]
They are both nonzero, irreducible and inequivalent by the restriction theorem. A change of the sign of \(T\) swaps the labels, and a fixed Whittaker normalization selects the generic label.

**Exercise 9.3 (medium).** Show that a dihedral supercuspidal has the self-twist \(\eta_{E/F}\).

**Solution.** For \(r=\operatorname{Ind}_{W_E}^{W_F}\widehat\theta\), the restriction of \(\eta_{E/F}\) to \(W_E\) is trivial. The induction tensor identity therefore gives \(r\otimes\eta_{E/F}\simeq r\). Explicitly, the operator \(\operatorname{diag}(1,-1)\) commutes with the two diagonal character actions and negates the exchanging matrices. Both parameters have \(N=0\). LLC twist compatibility and bijectivity give the self-twist of the corresponding \(\pi\). Proposition 4.1 shows that its packet has at least two members.

**Exercise 9.4 (hard).** Characterize four-element packets and relate the result to the two-dimensional Weil classification.

**Solution.** For an irreducible Weil lift, self-twist operators occupy distinct character eigenspaces of the four-dimensional endomorphism space, so there are at most four; determinants make their group of exponent two. Four give two nonscalar involutions \(A,B\). Their character lines force \(AB=-BA\), so they have the Pauli forms (6.3). Projective commutation traps the projective Weil image in their common centralizer \(V_4\). Irreducibility excludes its proper cyclic subgroups. Conversely the four centralizing projective classes for a \(V_4\) image yield four distinct quadratic self-twists by (6.2), and Proposition 4.1 yields four constituents. The principal, special and determinant types give at most two and cannot have full projective image \(V_4\).

Such an irreducible lift is dihedral for each of its three quadratic self-twist fields: the index-two kernel of a nontrivial twist preserves the two eigenlines of its intertwiner, and an element outside exchanges them, expressing the lift as induction of one line. This is the index-two argument from the two-dimensional Weil lesson. Primitive projective \(A_4\) or \(S_4\) parameters consequently do not give four-element packets. Over \(\mathbb Q_3\), (7.1) realizes \(V_4\) and its three quadratic fields are exactly (7.2).

## What this lesson does not prove

The general packet conjecture, enhanced inner-form refinements and endoscopic character identities are stated; see [Getz–Hahn, §12.5] and [Arthur, *Introduction to the trace formula*, §§27–30]. The full ordinary reductive-group \(L\)-group construction is used as standard root-datum theory; [Hales, §§2–3] gives its unramified instances. [Gan–Gao–Weissman, §§1–3] is the separate central-extension background.

Finite semisimple restriction, lifting and multiplicity one are [Labesse–Langlands, §2, Lemmas 2.4–2.6]. Their packet partition is stated after Lemma 2.8. We proved transitivity, openness, the exact stabilizer index, self-twist counting and the dihedral twist, as well as the complete two- and four-member calculations. Schur's lemma and the earlier \(\mathrm{GL}_2\) classification and LLC are the prerequisites to those proofs.

The fundamental lemma and its geometric proof are stated with locators [Ngô 2010, Theorems 1.11.1 and 1.12.7; Introduction, Theorems 1–2]; its group normalization and reduction are [Hales, §§6–8]. Arthur's local and global classifications are [Arthur 2012, Theorems 7.1–7.2] in the framework specified in Section 8. The unitary statement is [Mok 2015, Theorem 2.5.1], also stated in [Getz–Hahn, Theorem 12.5.6]. No proof of these deep classification or transfer theorems is claimed here.

## References

- [Labesse–Langlands 1979] Jean-Pierre Labesse and Robert P. Langlands, [*L-indistinguishability for SL(2)*](https://publications.ias.edu/sites/default/files/ll-ps.pdf), *Canadian Journal of Mathematics* 31 (1979), 726–785; §2 locators refer to the IAS re-typeset edition, pp.9–13.
- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§12.5 and 13.8.
- [Gan–Gao–Weissman 2018] Wee Teck Gan, Fan Gao and Martin H. Weissman, [*L-groups and the Langlands program for covering groups: a historical introduction*](https://arxiv.org/abs/1705.07559), *Astérisque* 398 (2018), §§1–3.
- [Clay 4] James Arthur, *An introduction to the trace formula*, §§27–30; Thomas C. Hales, *A statement of the fundamental lemma*, §§1–9; both in [*Harmonic Analysis, the Trace Formula, and Shimura Varieties*](https://www.claymath.org/wp-content/uploads/2022/03/cmip04c.pdf), Clay Mathematics Proceedings 4 (2005).
- [Arthur 2012] James Arthur, [*Classifying automorphic representations*](https://www.math.toronto.edu/arthur/pdf/Classifying_automorphic_representations.pdf), in *Current Developments in Mathematics 2012*, International Press, 2013, Preface and §7, Theorems 7.1–7.2.
- [Ngô 2010] Bao Châu Ngô, [*Le lemme fondamental pour les algèbres de Lie*](https://www.numdam.org/item/PMIHES_2010__111__1_0/), *Publications Mathématiques de l'IHÉS* 111 (2010), 1–169, Introduction and §§1.11–1.12.
- [Mok 2015] Chung Pang Mok, [*Endoscopic Classification of Representations of Quasi-Split Unitary Groups*](https://arxiv.org/abs/1206.0882v5), *Memoirs of the AMS* 235 (2015), Theorem 2.5.1.
