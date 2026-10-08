# Odd-primary one-group cohomology from primitive tests and the bar construction

<a id="DG-CHAR-13F-one-group.proof"></a>

Let \(p\) be an odd prime and \(k=\mathbb F_p\). This proof computes the full cohomology of the one-group objects \(K(k,n)\), for every \(n\geq1\), not only the degrees needed for seven-dimensional bordism. It combines an injectivity argument with a dimension bound. No transgression formula, unproved collapse assertion, or explicit Adem relation is used.

The operations and their faithful triangular test are those of [Odd-primary operation coordinates](odd-primary-operation-coordinates.md). The ordinary reduced powers, Cartan formula, instability and suspension were constructed in [*Odd-prime reduced powers and the Wu classes*, Sections G–I](odd-prime-reduced-powers-and-wu-classes.md#g-normalized-chains-and-a-cyclic-resolution). The coefficient Bockstein and the cyclic-group calculation are in Section 1 of the coordinate proof.

## 1. Statement and indexing

Write an admissible word as

\[
 I=\beta^{\epsilon _0}P^{s_1}\beta^{\epsilon _1}\cdots
                     P^{s_L}\beta^{\epsilon _L},
 \qquad s_i\geq p s_{i+1}+\epsilon_i,\qquad s_{L+1}=0.
 \tag{1}
\]

Here \(\epsilon_i\in\{0,1\}\); trailing zero pairs are discarded. The empty word and \(\beta\) are included. Put

\[
 \begin{split}
 r_i&=s_i-p s_{i+1}-\epsilon_i,\\
 D(I)&=2(p-1)\sum_i s_i+\sum_{i\geq0}\epsilon_i,\\
 e(I)&=2\sum_{i\geq1}r_i+\sum_{i\geq0}\epsilon_i.
 \end{split}
 \tag{2}
\]

Thus \(e(1)=0\), \(e(\beta)=1\), and \(e(I)\equiv D(I)\pmod2\). If \(I=\beta^{\epsilon_0}P^{s_1}J\), with \(J\) starting at \(\epsilon_1\), direct subtraction gives

\[
 e(I)=2s_1+\epsilon_0-D(J),\qquad
 e(I)-e(J)=2r_1+\epsilon_0\geq0.
 \tag{3}
\]

For \(n\geq1\), define

\[
 {\cal G}_n=\{I:e(I)<n\}
       \ \cup\ \{I:e(I)=n,\ \epsilon_0=1\}.
 \tag{4}
\]

Let \(F_n\) be the free graded-commutative \(k\)-algebra on symbols \(u_I\), \(I\in{\cal G}_n\), of degree \(n+D(I)\). In odd characteristic this means a polynomial generator in each even degree and an exterior generator in each odd degree. Give every generator the primitive coproduct.

**Theorem.** If \(\iota_n\) is the fundamental class of \(K(k,n)\), the homomorphism

\[
 F_n\longrightarrow H^*(K(k,n);k),\qquad u_I\longmapsto I\iota_n
 \tag{5}
\]

is an isomorphism of graded Hopf algebras. The coproduct on the target is induced by addition on \(K(k,n)\), not by its diagonal map.

Each degree of \(F_n\) is finite dimensional: the operation labels have positive weights as in (10) of the coordinate proof, and every generator has degree at least \(n\). All tensor products and duals below are degreewise over \(k\).

## 2. A cochain-representing simplicial model

Use normalized simplicial cochains, and define the simplicial abelian group

\[
 G_n(m)=Z^n(\Delta[m];k).
 \tag{6}
\]

Faces and degeneracies pull back cocycles. All its levels are finite sets. Its universal cocycle evaluates an \(n\)-simplex \(c\in G_n(n)\) on the identity \(n\)-simplex.

A simplicial map \(X\to G_n\) is precisely a normalized \(n\)-cocycle on \(X\): the image of a simplex \(x:\Delta[m]\to X\) is the pullback of that cocycle. This proves both directions and their inverse relationship, including compatibility with degenerate simplices.

Homotopy classes give \(H^n(X;k)\). For the forward implication, the prism chain operator on \(X\times\Delta[1]\) shows that the two restrictions of a cocycle differ by a coboundary. Conversely suppose \(c_1-c_0=\delta b\). Let \(t\) be the degree-zero cochain on \(\Delta[1]\) taking values zero and one at its endpoints. The cocycle

\[
 \operatorname{pr}_X^*c_0+
       \delta\big(\operatorname{pr}_{\Delta[1]}^*t\smile
                         \operatorname{pr}_X^*b\big)
 \tag{7}
\]

on \(X\times\Delta[1]\) restricts to \(c_0,c_1\), so supplies the required homotopy. The cup product in (7) is the normalized Alexander–Whitney product; its degree and endpoint restrictions are explicit. The same construction works pointedly with reduced cochains. Thus \(G_n\) is the simplicial cochain model of \(K(k,n)\) used here. The fundamental class is nonzero: pull it back along the map representing the nonzero normalized class of the simplicial \(n\)-sphere.

For later use compute the normalized complex of \(G_n\) **as an abelian group**, not of the free vector space on its underlying set. Use

\[
 N_m^+A=\bigcap_{i=1}^m\ker d_i,\qquad \partial=d_0.
 \tag{8}
\]

For \(m<n\), (6) is zero; for \(m=n\), its normalized group is \(k\). If \(m>n\), a cochain in the intersection (8) vanishes on every \(n\)-face missing a vertex \(i\geq1\). When \(m>n+1\) that is every \(n\)-face. When \(m=n+1\), the sole possible exception is the face \([1,\ldots,n+1]\); the cocycle equation on \([0,\ldots,n+1]\) forces its coefficient to vanish too. Consequently

\[
 N^+G_n=k[n].
 \tag{9}
\]

This is also compatible with the normalized-quotient convention: the natural projection is
\((1-s_0d_1)(1-s_1d_2)\cdots(1-s_{m-1}d_m)\), with the rightmost factor first. Its difference from the identity is degenerate; it kills degeneracies and projects onto (8).

## 3. The two different chain calculations for a bar object

For \(r\geq1\), put

\[
 B_{a,b}=G_r(b)^a.
 \tag{10}
\]

In the horizontal variable this is the nerve of the additive group \(G_r(b)\). Its faces remove the first or last entry, or replace two adjacent entries by their sum; degeneracies insert zero. The vertical maps apply those of \(G_r\) componentwise. Every map is a group homomorphism, and the two directions commute.

We use two chain constructions on (10). They must not be conflated:

| Input to normalization | What it computes |
|---|---|
| The bisimplicial abelian group \(B\) itself | A comparison of the simplicial models \(\operatorname{diag}B\) and \(G_{r+1}\) |
| The bisimplicial vector space \(k[B]\), free on the underlying sets | Ordinary cohomology, and its bar-filtration upper bound |

For the first calculation, horizontal normalization of the nerve of any abelian group \(A\) is \(A\) in degree one and zero elsewhere. Indeed its degree-zero group is zero; in degree one all positive faces vanish. In degree \(a\geq2\), the last face forces entries \(1,\ldots,a-1\) to vanish and face \(a-1\) then forces the remaining entry to vanish. Thus double normalization of \(B\) is \(k\) in bidegree \((1,r)\) only, by (9).

The normalized diagonal/total comparison therefore gives

\[
 N^+\operatorname{diag}B
 \ \underset{\operatorname{Sh}^N}{\stackrel{\operatorname{AW}^N}{\rightleftarrows}}\
 \operatorname{Tot}N_h^+N_v^+B=k[r+1].
 \tag{11}
\]

These are chain-homotopy inverse maps, not an asserted identity of the two complexes. The total differential is \(\partial_h+(-1)^a\partial_v\). The shuffle sums over lattice paths with sign given by their inversion count. The Alexander–Whitney component restricts to the horizontal front \(a\)-face and the vertical back \(b\)-face, **then applies both Moore projections**. Without these projections it need not land in the Moore normal summands.

The exact existing native programme proofs used for (11) are:

- AI Integrated Stacks, revision `565b10e987aba5969b21145a0833f42d69f96790`, [simplicial.tex, theorem-dold-kan](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/simplicial.tex#L4125): normalization is an equivalence between simplicial objects of an abelian category and nonnegative chain complexes; its inverse is given by the finite sum over ordinal surjections.
- In that same exact file, [theorem-illusie-I-eilenberg-zilber](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/simplicial.tex#L5091), [theorem-illusie-I-iterated-dold-kan](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/simplicial.tex#L5196), and [lemma-illusie-I-normalized-eilenberg-zilber](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/simplicial.tex#L5266). These supply the signed maps, the finite free-model homotopy recursion, the two normalization conventions, and the projected normalized comparison.

Here is an explicit justification that the chain homotopies in (11) give simplicial homotopies. It avoids treating a homotopy assertion as a bare equality. Suppose \(f,g:N^+A\to N^+C\) and \(h\) satisfy \(\partial h+h\partial=g-f\). On \(N^+A\otimes N k[\Delta[1]]\) define

\[
 x\otimes v_0\longmapsto f(x),\quad
 x\otimes v_1\longmapsto g(x),\quad
 x\otimes[01]\longmapsto(-1)^{|x|}h(x).
 \tag{12}
\]

Because \(\partial[01]=v_1-v_0\), the chain-map identity on the third term is exactly \(\partial h+h\partial=g-f\). Compose (12) with the normalized Alexander–Whitney map on \(N^+(A\otimes k[\Delta[1]])\), and use fullness of normalization. This gives a simplicial linear map \(A\otimes k[\Delta[1]]\to C\) with endpoints \(f,g\). Its restriction along \((a,\sigma)\mapsto a\otimes[\sigma]\) is an ordinary simplicial homotopy on underlying sets.

Apply this to (11) and (9). The result is a pointed simplicial homotopy equivalence

\[
 \operatorname{diag}B\simeq G_{r+1}.
 \tag{13}
\]

The maps in (13) are additive, so also preserve the addition-induced cohomology coproduct.

For the second calculation, apply chains to \(k[B]\) and dualize. The same diagonal/total comparison applies to this **different** bisimplicial vector space. Normalize vertically but initially leave the horizontal direction unnormalized; quotienting its acyclic degenerate complex later does not change the total cohomology. The total cochain complex computes \(H^*(G_{r+1};k)\) by (13). Filter by horizontal degree. Before horizontal normalization its first page is

\[
 E_1^{a,b}=H^b(G_r^a;k).
 \tag{14}
\]

The field Künneth isomorphism identifies this with the internal-degree-\(b\) part of \(H^*(G_r;k)^{\otimes a}\). One can verify Künneth directly here: the shuffle comparison reduces chains of the product to a tensor product; splitting each vector-space chain complex into its homology and contractible pairs computes the tensor homology. All degreewise dualizations and finite products are legitimate; (6) has finite levels.

Horizontal normalization removes the unit factors. Interior faces in the nerve induce the reduced coproduct on one factor, while the first and last faces supply the terms cancelled by the units. Thus the horizontal complex on the next page is the cobar complex of the connected graded coalgebra \(H^*(G_r;k)\). In the unsuspended word convention its differential inserts the reduced coproduct in position \(i\) with sign \((-1)^i\); the total-cochain convention adds the common sign \((-1)^b\) in internal degree \(b\). Multiplying an entire differential by that fixed sign does not change its homology. Koszul signs in coproducts of products are retained. We get

\[
 E_2^{a,b}=\operatorname{Cotor}_{H^*(G_r;k)}^{a,b}(k,k).
 \tag{15}
\]

Only a dimension inequality is required. This is a first-quadrant filtered complex with a finite filtration in each total degree. Taking successive cycle quotients and boundaries on each page cannot increase dimension. The final page is the associated graded of its cohomology: for a fixed total degree the finite filtration stabilizes after finitely many possible differentials. Therefore

\[
 \dim H^q(G_{r+1};k)
 \leq\sum_{a+b=q}\dim\operatorname{Cotor}_{H^*(G_r;k)}^{a,b}(k,k).
 \tag{16}
\]

No collapse has been assumed to obtain (16).

## 4. Independence in a fixed input degree

The triangular test in the coordinate proof has input \(v_J\) of degree exactly \(e(J)\). Fix an operation degree \(D\) and retain only labels with \(e(J)\leq n\). For each retained column suspend that input \(n-e(J)\) times. Reduced cohomological suspension is an isomorphism on that class and its test output.

For operations of degree \(D\), the chosen graded suspension convention gives

\[
 I(\sigma^t v_J)=(-1)^{Dt}\sigma^t(Iv_J).
 \tag{17}
\]

The sign is common to every row in this fixed-degree column. Hence the resulting test matrix is the corresponding triangular square submatrix with each column multiplied by a unit. It is invertible. Represent each suspended input by its map to \(G_n\) using Section 2. A relation among the classes \(I\iota_n\) would pull back to zero in every test and is therefore zero coefficientwise. In degree zero, the empty word is tested by the nonzero fundamental class itself.

Consequently, for every \(D\), the classes

\[
 \{I\iota_n:D(I)=D,\ e(I)\leq n\}
 \tag{18}
\]

are linearly independent. This is stronger than independence only in the eventual stable range, and uses the full triangular proof rather than a finite numerical matrix.

## 5. Free-algebra injection, including all powers

If \(I=\beta^{\epsilon_0}P^{s_1}J\) and \(e(I)>n\), (3) and instability imply \(I\iota_n=0\). For \(\epsilon_0=0\), the reduced-power index exceeds half the input degree. For \(\epsilon_0=1\), either that also occurs, or the inner power is the top power of an even class, after which \(\beta(y^p)=0\) by the derivation rule.

If \(e(I)=n\) and \(\epsilon_0=0\), the inner input has even degree \(2s_1\) and

\[
 I\iota_n=(J\iota_n)^p.
 \tag{19}
\]

Its tail is admissible and \(e(J)\leq n\), by (3). Removing this initial top-power step strictly decreases the operation degree. Repetition terminates at a unique label in \({\cal G}_n\) with even total class degree.

Conversely, for any admissible label \(J\) with \(e(J)\leq n\) and \(q=n+D(J)>0\) even, prepend \(P^{q/2}\). If \(J\) has first power \(s_1\), the new admissibility inequality is

\[
 q/2-p s_1-\epsilon_0(J)=(n-e(J))/2\geq0.
 \tag{20}
\]

For \(J=1,\beta\) the same formula holds with the missing power zero. This produces exactly the label in (19). We have proved a bijection:

\[
 \{\text{\(p^a\)-th powers of even generators of }F_n,\ a\geq0\}
 \ \longleftrightarrow\
 \{J:e(J)\leq n,\ n+D(J)\text{ even}\}.
 \tag{21}
\]

Odd generators already have \(e(J)<n\): equality is excluded by \(e(J)\equiv D(J)\pmod2\).

Every generator image in (5) is primitive. The fundamental class is primitive under addition, as can be checked on cocycles in (6), and each operation is additive and natural. Thus (5) is a Hopf-algebra map.

The primitives of a free graded-commutative Hopf algebra with primitive generators are exactly the linear span of its odd generators and the \(p^a\)-th powers of its even generators. Here is a direct proof. A monomial involving at least two different variables has a coproduct term separating the full power of one variable from all the others, with coefficient \(1\) or \(-1\). No different monomial can cancel that specified term, because its two factors determine the original exponents and odd-variable set. For a monomial in one even variable, all interior binomial coefficients vanish in \(k\) exactly when its exponent is a power of \(p\), by the base-\(p\) calculation in Section 2 of the coordinate proof. A single odd variable contributes only its first power. This proves the assertion, degree by degree.

By (18) and (21), the map (5) is injective on primitives. It is therefore injective on the whole algebra. Indeed, if its homogeneous kernel were nonzero, choose a nonzero element of least positive degree. Its reduced coproduct has factors of strictly smaller positive degree. The map is injective on those degrees, so their tensor map is injective; since the element is in the kernel, its reduced coproduct must be zero. It would be a nonzero primitive in the kernel, a contradiction. This proves

\[
 F_n\hookrightarrow H^*(G_n;k)
 \tag{22}
\]

without presuming the cohomology calculation or the absence of multiplicative relations.

## 6. The bar upper bound for a primitive free coalgebra

We calculate only the bigraded dimensions in (15). For a locally finite coalgebra \(C\), its cobar cochains identify degreewise with the cochains of the free bar resolution over its graded dual \(C^\#\). Thus they compute \(\operatorname{Ext}_{C^\#}(k,k)\). The duality is degreewise, not the unrestricted dual of an infinite direct sum. The free bar resolution is exact: its augmented complex has the contracting homotopy inserting a leading unit. Any other free resolution computes the same groups, since augmentation-preserving maps lift a free basis successively, and their differences lift similarly to a chain homotopy. We can therefore use the following explicit resolutions.

**An odd primitive generator.** For \(C=\Lambda(z)\), \(|z|=v\) odd, its dual algebra is again exterior, on \(t\) of internal degree \(v\). The free resolution has one generator in homological degree \(a\) and internal degree \(av\), with differential multiplication by \(t\). It is exact because \(\ker(t)=kt=\operatorname{im}(t)\). Applying \(\operatorname{Hom}(-,k)\) makes every differential zero. The total-degree generating series is

\[
 \frac1{1-T^{v+1}}.
 \tag{23}
\]

**An even primitive generator.** For \(C=k[x]\), \(|x|=v\) even, decompose its coalgebra using base-\(p\) digits. For each \(j\geq0\), let \(C_j\) have basis

\[
 c_{a,j}=\frac{x^{a p^j}}{a!},\qquad 0\leq a<p.
\]

Then \(\Delta c_{a,j}=\sum_{b+c=a}c_{b,j}\otimes c_{c,j}\). Multiplication gives a coalgebra isomorphism \(\bigotimes_{j\geq0}C_j\to k[x]\). It is bijective on the monomial bases by unique base-\(p\) expansion. Its compatibility with coproduct follows from
\((X+Y)^m=\prod_j(X^{p^j}+Y^{p^j})^{m_j}\); the factorials cancel the digit binomial coefficients.

The graded dual of \(C_j\) is \(k[t]/(t^p)\), with \(|t|=w=v p^j\). Its free resolution alternates multiplication by \(t\) and \(t^{p-1}\). Exactness follows from

\[
 \ker(t)=(t^{p-1}),\qquad \ker(t^{p-1})=(t).
\]

The generator in homological degree \(2a\) has internal degree \(apw\), and that in degree \(2a+1\) has internal degree \(apw+w\). Hom into \(k\) again has zero differential. Therefore this digit factor contributes

\[
 \frac{1+T^{w+1}}{1-T^{pw+2}}.
 \tag{24}
\]

Tensor the resolutions for all variables and all digit factors. For each finite collection, exactness over the field follows by splitting augmented complexes into their degree-zero homology and contractible pairs; tensoring a contracting homotopy with the other complexes, with the tensor differential signs, contracts every summand containing such a pair. In each internal degree only finitely many positive-degree factors occur. Thus the same argument applies to the full locally finite tensor product.

If \(S\) is the set of odd generators of \(F_r\), and \(T_r\) is the set of **all \(p\)-power iterates of its even generators**, including the zeroth iterate, (23)–(24) give

\[
 \operatorname{Hilb}\operatorname{Cotor}_{F_r}(k,k)
 =
 \prod_{z\in S}\frac1{1-T^{|z|+1}}
 \prod_{x\in T_r}\frac{1+T^{|x|+1}}{1-T^{p|x|+2}}.
 \tag{25}
\]

Formula (25) is a dimension calculation. It makes no unnecessary claim identifying the full ring structure of this Cotor group.

## 7. Complete label matching and induction

By (21), labels for \(T_r\) are precisely admissible \(J\) with \(e(J)\leq r\) and \(r+D(J)\) even. Labels for \(S\) satisfy \(e(J)<r\) and \(r+D(J)\) odd.

We match every factor of (25) with exactly one generator of \(F_{r+1}\).

1. For \(J\in S\), keep the same word. Its new degree is \((r+D(J))+1\), even. These are exactly the even generators of \(F_{r+1}\) with \(e(J)<r+1\): parity forces \(e(J)\leq r-1\).
2. For \(J\in T_r\), again keep the same word. Its new degree is \((r+D(J))+1\), odd. These are exactly all the odd generators of \(F_{r+1}\), since their excess is at most \(r\).
3. For \(J\in T_r\), put \(q=r+D(J)\) and form
   \[
    \mu(J)=\beta P^{q/2}J.
    \tag{26}
   \]
   The new word is admissible by (20), now with \(n=r\). Its excess is
   \(2(q/2)+1-D(J)=r+1\), its leading Bockstein is one, and its total class degree is
   \[
    (r+1)+D(\mu(J))=p q+2.
    \tag{27}
   \]
   Conversely any even generator at excess \(r+1\) has this form uniquely: remove its leading \(\beta P^s\); equation (3) gives \(r+D(J)=2s\), and its admissibility gives \(e(J)\leq r\). The possibility \(s=0\) cannot occur because the tail's total class degree would be zero whereas \(r\geq1\).

The three lists are disjoint and exhaustive, so

\[
 \operatorname{Hilb}\operatorname{Cotor}_{F_r}(k,k)
       =\operatorname{Hilb}F_{r+1}.
 \tag{28}
\]

For \(r=1\), \(G_1\) is the nerve of the additive cyclic group \(k\): a one-cocycle on a simplex is determined by its values on consecutive edges, and the nerve's composition is their addition. The existing cyclic computation gives

\[
 H^*(G_1;k)=\Lambda(\iota_1)\otimes k[\beta\iota_1]=F_1.
\]

Indeed \({\cal G}_1=\{1,\beta\}\) directly from (2)–(4). Assume now that (5) is a Hopf isomorphism for \(r\). Apply (16), (25), and (28), and combine them with the injection (22) for \(r+1\). In every degree the injection's source has dimension both at most and at least the dimension of its target. It is an isomorphism. This proves the theorem by induction for all \(n\) and every odd prime.

The argument also proves that no differential can reduce the dimensions used in (16), but this is a consequence, not an assumption on which the induction rests.

## 8. Stable spanning and the spectrum interface

For a fixed nonnegative \(d\), take \(n>d\). Every positive-degree generator in \(F_n\) has degree at least \(n\), so degree \(n+d<2n\) contains no product of two such generators. Every admissible word of degree \(d\) has \(e(I)\leq D(I)=d<n\), by the positive weights in the coordinate proof. Hence

\[
 H^{n+d}(G_n;k)=\bigoplus_{D(I)=d}k(I\iota_n).
 \tag{29}
\]

To specify compatibility, let \(f:\Sigma G_n\to G_{n+1}\) represent \(\sigma\iota_n\), using Section 2. Define cohomology suspension by \(\sigma^{-1}f^*\). Formula (17) gives
\[
 \sigma^{-1}f^*(I\iota_{n+1})=(-1)^d I\iota_n.
 \tag{30}
\]
A stable degree-\(d\) operation has precisely the same graded sign in its compatibility equation. Thus its coefficients in the basis (29) agree from one \(n>d\) to the next. Pullback by the classifying map of any cocycle proves that the operation equals that fixed linear combination on every sufficiently high input degree. Suspension and its reduced cohomology isomorphism extend equality to all input degrees. This establishes spanning for stable natural cohomology operations on the simplicial/cochain models used above. Negative degrees eventually have zero representing cohomology because \(G_n\) has no positive cohomology below \(n\).

## 9. Spectrum maps, including the inverse-limit term

We now identify (29) with the full spectrum mapping group, rather than presuming that compatible evaluations detect every spectrum map.

We fix the suspension normalization before making that comparison. If \(\sigma_q\) is the cochain suspension used in (17), put \(\widehat\sigma_q=(-1)^q\sigma_q\) on degree-\(q\) classes. Then for every degree-\(D\) word,
\[
 I\widehat\sigma_q=(-1)^{q+D}\sigma_{q+D}I
                     =\widehat\sigma_{q+D}I.
 \tag{30a}
\]
Thus the same operations commute with this normalized suspension. Use structure maps \(\Sigma G_n\to G_{n+1}\) representing \(\widehat\sigma_n\iota_n\). This changes neither the ordinary cohomology groups nor the operations or their products; it fixes their identification with the representing spectrum. Compared with structure maps representing \(\sigma_n\iota_n\), the level rescaling \((-1)^{n(n-1)/2}\) gives an isomorphism of the two prespectrum models. Use the shifted \(\Omega\)-spectrum with level \(G_{n+d}\) to represent \(\Sigma^dHk\), retaining that level's normalized structure map. This convention applies to all shifts and their compositions.

First the \(G_n\) form an Eilenberg–Mac Lane \(\Omega\)-spectrum. Here is a concrete model check. Take the nonnegative chain complex with \(k\) in degrees \(n+1,n\) and identity differential, and map it onto \(k[n+1]\). Its kernel is \(k[n]\). Apply the inverse of normalization. Exactness gives a termwise surjective map of simplicial abelian groups with kernel \(G_n\), and its source is contractible: the identity chain contraction becomes an additive simplicial homotopy by (12).

For clarity, a simplicial abelian group is Kan. Given a horn with missing face \(j\), start with zero. Correct the supplied faces \(i<j\) in ascending order by adding \(s_i(a_i-d_ix)\). Then correct the supplied faces \(i>j\) in descending order by adding \(s_{i-1}(a_i-d_ix)\). The simplicial identities and the horn compatibility equations show that each correction fixes its required face and preserves those already fixed. A termwise surjection of simplicial abelian groups is a Kan fibration: lift the requested target simplex first, then solve the resulting horn in its kernel by that same algorithm. Consequently the preceding contractible-source map is a fibration. Its fibre \(G_n\) is equivalent to \(\Omega G_{n+1}\). The contraction supplies the comparison additively: on the normalized complex its connecting map sends the lifted basis vector to its differential, which is the basis vector with coefficient one. Normalize its adjoint as in (30a). Applying pointed mapping spaces into this fibration verifies the equivalence for every simplicial source, not merely on a list of homotopy groups.

Use sequential pointed simplicial spectra with cofibrant structure maps and \(\Omega\)-spectrum targets to compute maps. A levelwise cofibrant replacement of a prespectrum can be made successively: replace the map from the suspension of the preceding replaced level to the next level by its mapping cylinder. The new structure map is a cofibration and each projection to the old level is a pointed homotopy equivalence. Into a levelwise Kan \(\Omega\)-spectrum, the space of such strict compatible maps from this replacement computes the derived mapping space.

The finite-stage calculation explains exactly which limit this entails. For an \(\Omega\)-spectrum \(F\), let \(M_N\) be the space of compatible maps on levels through \(N\). Restriction \(M_{N+1}\to M_N\) is a fibration, since extending the last map is restriction along a cofibration of sources into the Kan target \(F_{N+1}\). Inductively evaluation on the top level is a homotopy equivalence

\[
 M_N\simeq\operatorname{Map}_*(E_N,F_N).
 \tag{31}
\]

Indeed, the next partial mapping space is the pullback of
\(\operatorname{Map}_*(E_{N+1},F_{N+1})\to
\operatorname{Map}_*(\Sigma E_N,F_{N+1})\)
along \(M_N\). The displayed map is a fibration. By the induction hypothesis and \(F_N\simeq\Omega F_{N+1}\), the other arrow in this pullback is a homotopy equivalence, so evaluation on level \(N+1\) is one too. This also identifies its restriction map with precomposition by the source structure map followed by the target loop equivalence. Thus the infinite mapping space is the homotopy inverse limit of the level mapping spaces. Passing back through the levelwise replacement gives the same tower up to homotopy equivalence. A finite initial segment can be discarded; its lower values and compatibility paths are determined by the tail with contractible choices.

Apply this to \(E=Hk\), \(F=\Sigma^dHk\), and \(n\) large enough that \(n,n+d\geq1\). Put
\[
 Z_n=\operatorname{Map}_*(G_n,G_{n+d}).
\]
Representability and suspension give
\[
 \pi_iZ_n=\widetilde H^{\,n+d-i}(G_n;k)\qquad(i\geq0).
 \tag{32}
\]
For \(i=0\), this is the group of components. For \(i>0\), use pointed maps from \(S^i\wedge G_n\) and the iterated cochain suspension for the identification in (32). The mapping spaces are simplicial abelian groups, and their bonding maps can be taken additive using the additive loop equivalences above. On a basis word of operation degree \(d-i\), the transition has sign
\[
 (-1)^{\,n+(d-i)+i+(n+d)}=1.
 \tag{32a}
\]
The four exponents come respectively from the source structure normalization, (17), moving the structure-suspension coordinate past the \(i\) sphere coordinates, and the inverse target structure normalization. Thus the eventual basis transitions in (32) are the identity, with no suppressed suspension sign.

We spell out the possible inverse-limit correction. For a tower of these group-valued spaces, the path model of its homotopy inverse limit is the homotopy fibre of
\[
 1-\mathrm{shift}:\prod_n Z_n\longrightarrow\prod_n Z_n.
\]
Its long exact homotopy sequence, and the fact that homotopy groups commute with these products, yield the short exact sequence
\[
 0\longrightarrow
 \operatorname{coker}\left(
 \prod_n\pi_1Z_n\xrightarrow{\,1-\mathrm{shift}\,}\prod_n\pi_1Z_n\right)
 \longrightarrow[Hk,\Sigma^dHk]
 \longrightarrow
 \ker\left(
 \prod_n\pi_0Z_n\xrightarrow{\,1-\mathrm{shift}\,}\prod_n\pi_0Z_n\right)
 \longrightarrow0.
 \tag{33}
\]
The first term is often denoted \(\lim^1\); naming it does not make it disappear.

In this case it does disappear. By (29) and (32a), the bonding maps of \(\pi_1Z_n\), which have operation degree \(d-1\), are eventually the identity on the indicated bases, or both sides are zero when \(d-1<0\). The same is true for \(\pi_0Z_n\) in degree \(d\).

Here is the explicit surjectivity check for the product map in the first term. Given \(b_n\), choose \(a_N=0\) after the bonding maps \(r_n\) become surjective. Recursively choose \(a_{n+1}\) with \(r_n(a_{n+1})=a_n-b_n\) for \(n\geq N\); then define the finitely many earlier values backwards by \(a_n=b_n+r_n(a_{n+1})\). This solves \(a_n-r_n(a_{n+1})=b_n\) for every \(n\). Thus its cokernel is zero. The kernel for \(\pi_0\) is the eventually stable vector space displayed in (29). In particular, there is no nonzero spectrum map in (33) invisible to all its level evaluations.

Every admissible operation supplies those compatible evaluations, with the homotopies required by the mapping-space model because equal cohomology classes give homotopic representing maps. Surjectivity and injectivity in (33) show that it determines a unique spectrum-map class. Composition agrees with composition of natural operations, since their evaluations agree and the detection just proved is injective. We have therefore established, for every \(d\),
\[
 [Hk,\Sigma^dHk]=
 \begin{cases}
 \displaystyle\bigoplus_{D(I)=d} k I,&d\geq0,\\
 0,&d<0.
 \end{cases}
 \tag{34}
\]
This is the full stable spanning assertion **SB**, including its spectrum interpretation and degreewise finiteness.

Combining (34) with the faithful dual-coordinate injection and coproduct calculation in Sections 2–5 of the coordinate proof proves operation input **O**: the full dual stable-operation Hopf algebra is
\[
 k[\xi_1,\xi_2,\ldots]\otimes\Lambda(\tau_0,\tau_1,\ldots),
 \quad |\xi_j|=2(p^j-1),\quad|\tau_j|=2p^j-1,
\]
with precisely the coproduct and root action computed there. No independent claim about a hidden family of spectrum operations remains.

This bar-construction proof of **SB** and **O** does not require an additional filtered higher-operation hypothesis.

## 10. Mathematical sources

The one-group theorem is classical; see J. Peter May, [*A general algebraic approach to Steenrod operations*](https://www.math.uchicago.edu/~may/BOOKS/Algebraic.pdf), Section 10. Here its proof uses primitive tests, the bar upper bound and explicit resolutions. Section 3 links the exact AI Integrated Stacks proofs of the normalized simplicial comparison.
