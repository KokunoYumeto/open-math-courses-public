# Weil divisors and the class group

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A Cartier divisor has a local equation. A Weil divisor instead assigns an integer multiplicity to each codimension-one subvariety. Normality lets us measure those multiplicities with discrete valuations and recover regular functions from the absence of poles. The two descriptions agree on locally factorial schemes, but a normal singularity can have a Weil divisor with no local equation. The quadric cone will provide an explicit example and a class group of order two.

Our main convention is that \(X\) is a locally Noetherian integral normal scheme. A Weil divisor has **locally finite** support; it is a finite sum when \(X\) is Noetherian. We use Effective Cartier divisors and invertible sheaves, especially its full Cartier-class comparison. The necessary algebra is already written in Discrete valuation rings, normal rings and Serre's criterion, Theorems 1.2 and 3.3, and Regular local rings, Lemma 4.1 and Theorem 5.3. These give DVRs, the codimension-one intersection theorem, the height-one-prime characterization of UFDs, and factoriality of regular local rings. The normality convention and its locality are proved in the prerequisite Properties of schemes, Section 4.

## 1. Codimension-one valuations

A **prime divisor** is an integral closed subscheme \(P\subset X\) whose generic point \(\xi_P\) has \(\dim\mathcal O_{X,\xi_P}=1\). Its reduced closed structure is understood. Normality and the DVR theorem make \(\mathcal O_{X,\xi_P}\) a discrete valuation ring with fraction field \(K(X)\). Write its normalized valuation as \(v_P\), so a uniformizer has value one.

A **Weil divisor** is a formal sum

\[
D=\sum_P n_P[P],\qquad n_P\in\mathbb Z,
\tag{1.1}
\]

in which the family of closed subsets with nonzero coefficient is locally finite: each point has a neighborhood meeting only finitely many of them. Such sums form \(\operatorname{Div}(X)\). This is [Stacks, Tag 0BE2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-definition-Weil-divisor). A locally finite family meets a quasi-compact open in only finitely many members, by taking a finite subcover of the neighborhoods in its definition. Thus every divisor on a Noetherian scheme is a finite sum.

**Theorem 1.1.** For every \(f\in K(X)^*\),

\[
\operatorname{div}_X(f)=\sum_P v_P(f)[P]
\tag{1.2}
\]

is a Weil divisor, and \(\operatorname{div}_X(fg)=\operatorname{div}_X(f)+\operatorname{div}_X(g)\).

**Proof.** Around any point choose a nonempty affine open \(\operatorname{Spec}A\); it is a Noetherian normal domain. Write \(f=a/b\) with \(a,b\in A\setminus\{0\}\). A height-one prime at which the valuation is nonzero must contain \(a\) or \(b\), since otherwise both are units in its local ring. Any height-one prime containing \(a\) is minimal over \((a)\): a minimal prime over that ideal contained in it is nonzero, so cannot be strictly smaller inside a height-one prime of a domain. There are only finitely many minimal primes over each ideal in a Noetherian ring. The same holds for \(b\). This proves local finiteness, including finiteness of the divisors meeting this affine open, since taking closure and intersecting an open preserves their generic points. Additivity follows from addition of DVR valuations. \(\square\)

The local-finiteness assertion is [Stacks, Tag 02RL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-divisor-locally-finite). On a DVR, \(v(a)\) for nonzero \(a\in R\) also equals \(\ell_R(R/aR)\): if \(a=u\pi^m\), the filtration by powers of \(\pi\) has \(m\) residue-field factors. Hence the valuation formula agrees here with the more general length definition of [Stacks, Tag 02RJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-definition-order-vanishing).

The divisors (1.2) are **principal**, and the **class group** is

\[
\operatorname{Cl}(X)=\operatorname{Div}(X)/\operatorname{div}_X(K(X)^*).
\]

The following detection rule will be used repeatedly. For every Noetherian normal domain \(A\),

\[
A=\bigcap_{\operatorname{ht}\mathfrak p=1}A_{\mathfrak p}
\quad\text{inside }\operatorname{Frac}(A).
\tag{1.3}
\]

This is the full algebraic Hartogs theorem in the prerequisite lesson, Theorem 3.3. Consequently a fraction is regular if all those valuations are nonnegative, and is a unit if they are all zero, by applying (1.3) to it and its inverse. If there are no height-one primes, the intersection is the whole fraction field and \(A\) is a field. In scheme form, \(\operatorname{div}_X(f)=0\) implies \(f\in\Gamma(X,\mathcal O_X^*)\).

## 2. The divisor of a line-bundle section

Let \(\mathcal L\) be invertible and choose a nonzero meromorphic section \(s\), equivalently a nonzero generic frame. In a local regular frame \(e\) near \(\xi_P\), write \(s=f e\) and set

\[
v_P(s)=v_P(f).
\]

Changing \(e\) multiplies \(f\) by a regular unit, so the integer is independent of the frame. The same affine argument as in Theorem 1.1 proves local finiteness of

\[
\operatorname{div}_{\mathcal L}(s)=\sum_P v_P(s)[P].
\]

Changing the meromorphic section to \(hs\) adds \(\operatorname{div}(h)\). Thus the class depends only on \(\mathcal L\), defining

\[
c_1:\operatorname{Pic}(X)\longrightarrow\operatorname{Cl}(X).
\tag{2.1}
\]

In tensor-product frames, valuations of section coefficients add. This proves that \(c_1\) is a homomorphism, as in [Stacks, Tag 02SL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-c1-additive).

**Theorem 2.1 (Cartier–Weil comparison).** The map (2.1) is injective. It is surjective, hence an isomorphism, if and only if every local ring of \(X\) is a UFD. In particular it is an isomorphism for a regular integral locally Noetherian scheme.

**Proof of injectivity.** If \(c_1(\mathcal L)=0\), choose \(s\) with \(\operatorname{div}_{\mathcal L}(s)=\operatorname{div}(h)\). The meromorphic section \(t=h^{-1}s\) then has zero divisor. On a trivializing affine open \(\operatorname{Spec}A\), its coefficient has valuation zero at every height-one prime. By (1.3) that coefficient and its inverse belong to \(A\). Thus \(t\) is a regular nowhere-vanishing frame locally, and its local frames agree because it was one meromorphic section. It trivializes \(\mathcal L\) globally. This proves [Stacks, Tag 0BE8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-normal-c1-injective).

**Proof when the local rings are UFDs.** Let \(D\) be any Weil divisor. Near a point \(x\), only finitely many components of its support meet. A prime divisor through \(x\) gives a height-one prime of \(\mathcal O_{X,x}\), hence a principal prime in that UFD. Its ideal is coherent near \(x\), and this stalk generator spreads to a generator on a smaller neighborhood: the finite kernel and cokernel of the generator map vanish at \(x\) and vanish after shrinking. A divisor not containing \(x\) can be removed by shrinking. Thus the finitely many local components have regular prime equations \(f_i\), and their product \(\prod_i f_i^{n_i}\) is an invertible meromorphic local equation for \(D\), including negative exponents.

On overlaps, the ratios of two such equations have valuation zero at every prime divisor. Apply (1.3) on trivializing affine neighborhoods to see that these ratios are units. The local equations therefore define a Cartier divisor. Its line bundle, with the canonical meromorphic section one in the fractional realization, has Weil divisor \(D\). This proves surjectivity even for locally finite sums on a non-quasi-compact scheme.

**Proof of the converse.** Suppose \(c_1\) is surjective and take \(A=\mathcal O_{X,x}\). Each height-one prime \(\mathfrak p\subset A\) comes from a prime divisor \(P\) on \(X\), by taking the closure of the corresponding codimension-one point. Surjectivity gives a line bundle and meromorphic section whose divisor can be made exactly \([P]\) by multiplying by a rational function. Trivialize that bundle at \(x\). Its coefficient \(f\in\operatorname{Frac}(A)^*\) has valuation one at \(\mathfrak p\) and zero at every other height-one prime of \(A\). Formula (1.3) puts \(f\) in \(A\), and it belongs to \(\mathfrak p\). For any \(a\in\mathfrak p\), the quotient \(a/f\) has nonnegative valuation at every height-one prime, so also belongs to \(A\). Hence \(\mathfrak p=fA\). Every height-one prime is principal, and Lemma 4.1 of the regular-local prerequisite makes the Noetherian domain \(A\) a UFD.

Finally, regular local rings are UFDs by the complete Auslander–Buchsbaum factoriality proof in that same lesson, Theorem 5.3. This proves the regular case. \(\square\)

The equivalence is [Stacks, Tag 0BE9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-local-rings-UFD-c1-bijective). More directly, a Cartier divisor maps to the Weil divisor given by valuations of its local equations. This map is injective: zero valuations make every local equation a unit by (1.3). Combined with the Cartier-class theorem of the preceding divisor lesson, it identifies the image of \(c_1\) with Weil classes that have Cartier representatives.

## 3. Restricting to an open subscheme

Let \(Z\subset X\) be closed and \(U=X\setminus Z\). Denote by \(\operatorname{Div}_Z(X)\) the group of locally finite Weil divisors supported in \(Z\).

**Theorem 3.1 (excision).** Restriction gives an exact sequence

\[
\operatorname{Div}_Z(X)\longrightarrow
\operatorname{Cl}(X)\longrightarrow\operatorname{Cl}(U)
\longrightarrow0.
\tag{3.1}
\]

When \(X\) is Noetherian, its leftmost group is
\(\bigoplus_{P\subset Z}\mathbb Z[P]\). Removing a closed subset containing no codimension-one points does not change the class group.

**Proof.** Assume \(U\ne\varnothing\). A prime divisor of \(U\) has a unique closure that is a prime divisor of \(X\), since its generic local ring is unchanged. A locally finite sum on \(U\) extends by these closures to a locally finite sum on \(X\). Indeed, for any affine Noetherian open \(V\subset X\), the open \(V\cap U\) is a Noetherian topological space and is quasi-compact. Only finitely many support components meet it. A closure meets \(V\) exactly when its dense part in \(U\) meets \(V\), so only these finitely many closures meet \(V\). This proves that restriction on divisor groups is surjective; its kernel is \(\operatorname{Div}_Z(X)\).

The function fields of \(X\) and \(U\) identify, and valuations at retained prime divisors are unchanged. Principal divisors restrict to the corresponding principal divisors on \(U\). If a class restricts to zero, choose \(f\in K(X)^*\) whose divisor on \(U\) equals the restriction of a representative \(D\). Then \(D-\operatorname{div}_X(f)\) is supported in \(Z\). Conversely every such divisor restricts to zero. This proves exactness. For \(U\) empty, the right group is zero and the left group is all of \(\operatorname{Div}(X)\), giving the assertion directly. If \(Z\) contains no prime divisors, the left group is zero and the map is an isomorphism. \(\square\)

Global finite sums are essential in the direct-sum form of this result. For a counterexample without quasi-compactness, glue countably many affine lines \(X_i=\operatorname{Spec}k[t]\) along their common \(D(t)\). The resulting scheme is integral, normal and locally Noetherian. Let \(o_i\) be its separate origins. Their family is locally finite, because each chart meets just its own origin. The open \(U=D(t)\) has complement \(Z=\{o_i\}\). The divisor

\[
D=\sum_{i\text{ odd}}[o_i]
\]

is locally finite and restricts to zero. It is not, modulo principal divisors, a finite sum of origins: every rational function has the same \(t\)-valuation at every \(o_i\), whereas subtracting a finite sum from \(D\) leaves alternating coefficients outside a finite set. Thus a direct sum in (3.1) would miss part of the kernel in this example. The locally finite version retains the full locally Noetherian generality.

## 4. Affine and projective space

**Proposition 4.1.** For \(n\ge0\), \(\operatorname{Cl}(\mathbb A^n_k)=0\). For \(n\ge1\),

\[
\operatorname{Cl}(\mathbb P^n_k)=\mathbb Z[H],
\qquad \operatorname{Pic}(\mathbb P^n_k)=\mathbb Z[\mathcal O(1)],
\tag{4.1}
\]

where \(H\) is a hyperplane.

**Proof.** A polynomial ring over a field is a UFD; the complete Gauss-content and factorization proof is Integral extensions, Proposition 2.3. Every height-one prime is generated by a prime element \(p\), and \(\operatorname{div}(p)\) is that prime divisor with multiplicity one. All finite sums of prime divisors are therefore principal, proving the affine assertion, including the field case \(n=0\).

Remove a hyperplane from \(\mathbb P^n\); its complement is \(\mathbb A^n\). Excision shows that \([H]\) generates the class group. If \(m[H]=\operatorname{div}(f)\), restriction to the affine complement has zero divisor. The zero-divisor detection rule makes \(f\) a unit in \(k[t_1,\ldots,t_n]\), hence a nonzero constant. Its divisor on projective space is zero, so \(m=0\). This proves that the generator has infinite order. Projective space is regular, so Theorem 2.1 identifies Pic with Cl. The section defining \(H\) identifies its bundle with \(\mathcal O(1)\), as proved in the Cartier lesson. \(\square\)

The following statement allows a UFD base that is not Noetherian.

**Theorem 4.2.** If \(R\) is a UFD and \(n\ge1\), then

\[
\mathbb Z\xrightarrow{\ \sim\ }\operatorname{Pic}(\mathbb P^n_R),
\qquad d\longmapsto\mathcal O(d).
\tag{4.2}
\]

**Proof.** First prove \(\operatorname{Pic}(\operatorname{Spec}S)=0\) for any UFD \(S\). An invertible module embeds in its generic one-dimensional vector space as a finitely generated fractional ideal. Clear denominators, obtaining an ideal \(I\subset S\), and divide its finite generators by their gcd. It remains to show that a locally principal ideal \(J\) whose generators have gcd one is all of \(S\).

At a maximal ideal \(\mathfrak m\), write its local generator as \(a/b\), with \(b\notin\mathfrak m\). If it is a nonunit in \(S_{\mathfrak m}\), some prime irreducible \(\pi\) dividing \(a\) lies in \(\mathfrak m\). Every generator \(j\) of \(J\) has \(j/(a/b)\in S_{\mathfrak m}\). Clear its denominator outside \(\mathfrak m\): \(c b j=a r\) for \(c\notin\mathfrak m\). Primality of \(\pi\), and \(\pi\nmid cb\), force \(\pi\mid j\). This contradicts gcd one. Thus \(J_{\mathfrak m}=S_{\mathfrak m}\) for every maximal ideal. A proper ideal would lie in one of them, so \(J=S\). The original invertible ideal is principal, proving the affine Picard assertion.

Each standard chart \(U_i\) of \(\mathbb P^n_R\) has a polynomial UFD as coordinate ring, by Tag 0BC1. A line bundle therefore has a frame \(e_i\) on each chart. For \(i>0\), set \(t_i=X_i/X_0\). The coordinate ring of \(U_0\cap U_i\) is \(R[t_1,\ldots,t_n,t_i^{-1}]\), whose units are exactly \(c t_i^m\), \(c\in R^*\). To see this, units of a polynomial ring over a domain have degree zero, and lowest and highest Laurent exponents of a product add; an invertible Laurent polynomial must consequently have a single term with unit coefficient.

Rescale the frames by constants to write \(e_i=t_i^{m_i}e_0\). For \(n\ge2\), compare \(i,j>0\) on the triple overlap. In coordinates of \(U_i\), put \(s_0=X_0/X_i\) and \(s_j=X_j/X_i\). The ratio is

\[
e_j/e_i=s_j^{m_j}s_0^{m_i-m_j}.
\]

It must be a unit on \(U_i\cap U_j\), where \(s_j\) is inverted but \(s_0\) is an ordinary polynomial variable. The unit description forces \(m_i=m_j\). Thus all exponents equal \(d\), and the transition functions are those of \(\mathcal O(d)\). For \(n=1\), there is just one exponent, giving the same conclusion directly. Finally chart frames can only be changed by constants from \(R^*\); they cannot remove a nonzero exponent on \(U_0\cap U_1\). Hence \(\mathcal O(d)\) is trivial only for \(d=0\), proving injectivity. \(\square\)

This is the positive-dimensional assertion of [Stacks, Tag 0BXJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-Pic-projective-space-UFD). For \(n=0\), the scheme is \(\operatorname{Spec}R\) and its Picard group is zero, by the first part of the proof.

## 5. The quadric cone

Put \(A=k[x,y,z]/(xy-z^2)\), \(S=\operatorname{Spec}A\), and \(L=V(x,z)\). This is a normal two-dimensional domain in every characteristic, as proved in the normal-rings prerequisite, Solution 6.4. Its proof embeds it as \(k[s^2,t^2,st]\subset k[s,t]\), verifies the hypersurface depth condition, and checks regularity away from the vertex; it does not use division by two.

The prime ideal \(\mathfrak p=(x,z)\) has height one: its quotient is \(k[y]\), and the finite-type domain height formula gives codimension one. In \(A_{\mathfrak p}\), the element \(y\) is a unit and \(x=z^2/y\). Hence the maximal ideal is generated by \(z\), a uniformizer of this DVR, and

\[
\operatorname{div}_S(x)=2[L].
\tag{5.1}
\]

There are no other components, since \(A/(x)=k[y,z]/(z^2)\) has underlying reduced line \(L\). The nonreduced scheme cut out by \(x\) explains the multiplicity two.

The complement \(D(x)\) has ring \(A_x=k[x,x^{-1},z]\), a UFD. Excision shows that \([L]\) generates \(\operatorname{Cl}(S)\). To determine all relations, suppose \(m[L]=\operatorname{div}(f)\). On \(D(x)\), the divisor of \(f\) is zero, so \(f\) is a unit of \(A_x\). Its units are exactly \(c x^r\), with \(c\in k^*\) and \(r\in\mathbb Z\). Thus (5.1) gives \(m=2r\). Conversely every even multiple is principal. Therefore

\[
\operatorname{Cl}(S)\cong\mathbb Z/2,
\qquad [L]\longleftrightarrow1.
\tag{5.2}
\]

The ruling is not Cartier at the vertex. Its ideal \(I=(x,z)\), localized at \(\mathfrak m=(x,y,z)\), has two independent classes in \(I_{\mathfrak m}/\mathfrak m I_{\mathfrak m}\), by the degree-one computation in the Cartier lesson. To connect this scheme-ideal obstruction with the Weil divisor, suppose \([L]\) had a local Cartier equation \(h\). At the vertex its valuation is one at \(\mathfrak p\) and zero at every other height-one prime. Hartogs puts \(h\) in the local ring, and for every element of \(\mathfrak p\) puts its quotient by \(h\) in that ring. Thus \(\mathfrak p\) would equal \((h)\), contradicting the two-generator calculation. Twice \([L]\), however, is the principal Cartier divisor of \(x\).

There is a useful consequence: \(\operatorname{Pic}(S)=0\). Its injection into the two-element class group cannot have the nonzero class in its image, since that would make \([L]\) Cartier after subtracting a principal divisor. The punctured cone is regular, because the two opens \(D(x),D(y)\) cover it and are regular polynomial localizations. Excision preserves its class group, while Theorem 2.1 makes its Picard group \(\mathbb Z/2\). Removing a codimension-two point preserves Cl but can change Pic.

## 6. Exercises and solutions

**Exercise 6.1 (easy).** Compute \(\operatorname{Cl}(\mathbb A^2_k\setminus\{0\})\) and its Picard group.

**Solution.** The omitted closed point has codimension two, so Theorem 3.1 identifies the class group with that of the affine plane, which is zero by Proposition 4.1. The punctured plane is regular, so Theorem 2.1 identifies its Picard group with its class group. Both are zero. This makes no claim that the punctured plane is affine.

**Exercise 6.2 (easy).** Prove that removing a closed subset of codimension at least two from an integral normal locally Noetherian scheme preserves its class group. Explain why locally finite support introduces no boundary exception here.

**Solution.** No prime divisor is contained in the removed subset. Restriction thus retains every codimension-one generic point and its DVR. Closures give a bijection between the prime divisors of the two schemes. Locally finite sums extend by the affine-Noetherian argument in Theorem 3.1, so restriction is an isomorphism on divisor groups. The common function field and identical DVR valuations identify their principal-divisor subgroups. Passing to quotients gives the desired isomorphism. The local-finiteness argument is necessary if neither scheme is quasi-compact.

**Exercise 6.3 (medium).** Compute \(\operatorname{Cl}(\mathbb P^n_k)\) for \(n\ge1\) by deleting a hyperplane. Explain why a surjective map from \(\mathbb Z\) alone does not finish the computation.

**Solution.** The complement is affine space with zero class group, so excision gives a surjection \(\mathbb Z[H]\to\operatorname{Cl}(\mathbb P^n_k)\). It could a priori have a nonzero kernel. If \(mH\) is principal, its rational equation has no zeros or poles on affine space; there it is a unit of the polynomial ring, hence a nonzero constant. This same element of the function field is constant on projective space and has zero divisor. Thus \(m=0\), eliminating every possible relation. The hyperplane class is consequently an infinite cyclic generator.

**Exercise 6.4 (medium).** Compute the class group of the cone \(xy=z^2\), including in characteristic two, and identify all relations on its ruling class.

**Solution.** Normality in all characteristics is supplied by the precise prerequisite proof identified in Section 5. Invert \(x\); the resulting Laurent polynomial ring is a UFD, so excision makes the ruling class a generator. At its generic point \(y\) is invertible, \(z\) is a uniformizer and \(x=z^2/y\), giving \(2[L]=\operatorname{div}(x)\). Any relation \(m[L]=\operatorname{div}(f)\) makes \(f\) a unit after inverting \(x\). The units there are \(c x^r\), whose divisors are exactly \(2r[L]\). Therefore the relation subgroup is \(2\mathbb Z\), and the group is \(\mathbb Z/2\). A bound on the order alone would not prove that the generator is nonzero; the unit calculation supplies that missing step.

**Exercise 6.5 (medium).** Show that the ruling is not Cartier at the cone vertex although twice it is principal. Compare the scheme cut out by \(x\) with the reduced ruling.

**Solution.** In the local ring at the vertex the ruling ideal has two independent degree-one generators \(x,z\); products with the maximal ideal have degree at least two. It cannot be a principal ideal or an invertible ideal. If its Weil divisor had a Cartier equation, the valuation-one and Hartogs argument in Section 5 would make that ideal principal, so the Weil divisor is not Cartier either. In contrast \(x\) is nonzero in the domain and defines an effective Cartier divisor. Its quotient ring is \(k[y,z]/(z^2)\), a doubled structure on the ruling. Its cycle is \(2[L]\), and its associated line bundle is trivial because the divisor is principal. Equality of supports therefore does not identify the reduced ruling with that effective Cartier divisor.

## References and proof dependencies

The order map, Cartier–Weil comparison, locally finite excision theorem and all assigned class-group computations are proved above. The positive-dimensional Picard computation over an arbitrary UFD is also proved, with no Noetherian assumption on the base. The prerequisite proofs of DVR characterization, algebraic Hartogs, regular-local factoriality and cone normality are written and linked at their exact lesson locators. Polynomial factoriality uses the complete prerequisite programme proof linked in Section 4.

The Stacks project authors, *The Stacks project*, are cited in the AI Integrated Stacks Project edition at commit `565b10e987aba5969b21145a0833f42d69f96790`. Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), draft of 27 July 2024, §§15.4–15.5, provides the geometric comparison and examples. Timothy J. Ford, [*Commutative Algebra*](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf), version of 23 September 2026, Chapter 11, Section 3.3, provides the affine class-group and localization viewpoint.
