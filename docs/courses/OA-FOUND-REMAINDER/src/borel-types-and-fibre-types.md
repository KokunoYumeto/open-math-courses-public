# Borel types and fibre types

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

An algebra is finite precisely when it has a faithful normal tracial state, provided it acts on a separable Hilbert space. Its failure to be finite also has a witness: a proper isometry. Encoding both witnesses makes finiteness a Borel condition. A finite projection with full central carrier witnesses semifiniteness; a nonzero finite projection only witnesses the presence of a semifinite part. These distinctions matter when algebras have several central summands.

The same witnesses can be selected measurably in a field of factors. Traces then integrate, and isometries assemble into decomposable operators. We obtain the type of a direct integral from the types of its factors, including the converses.

We use [Borel supports and isomorphism classes](../reader/borel-supports-and-isomorphism-classes.html), Sections 1–3 and Theorem 5.1, for dense choices, Borel membership, supports, carriers and fixed unitary classes. [Projections and types](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html), Lemmas 6.3 and 7.4 and Theorem 10.3, supplies centrally orthogonal sums, full-carrier good projections and the homogeneous type-I decomposition. [Abelian operator algebras](../../foundations-of-von-neumann-algebras/abelian-operator-algebras.html), Theorems 8.2 and 8.4, classifies countably generated diffuse abelian algebras. The normal centre-valued trace is Theorem 5.2 of [Traces, Part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html). Positive normal functionals extend normally and positively to the ambient operator algebra by Theorem 10.1 of [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html).

The descriptive-set-theoretic inputs are the analytic-image, separation, measurability and selection theorems in [Polish spaces and standard Borel spaces](../../foundations-of-von-neumann-algebras/polish-spaces-and-standard-borel-spaces.html), Corollary 2.5, Theorem 4.3, Theorem 6.2 and Theorem 7.7. Their complete arguments include the recursive prefix choice and analytic measurability needed for completed-measure selection. Normal functionals on varying fibres are integrated by [Normal functionals across fibres](../reader/normal-functionals-across-fibres.html), Theorem 4.1. Measurable operator fields, countable generators and the centre of a factor integral come from [Direct integrals of von Neumann algebras](../reader/supplements/direct-integrals-of-von-neumann-algebras-commutants-and-centres-takesa.html), Theorem 4.3 and Lemma 5.1.

Related freely readable treatments are Effros’s paper on fixed-space Borel coding, Lurie’s lectures on separable fields and the commutant/centre dictionary, and Vaes and Wouters’s paper on Borel and measured fields. The selections used here are made for a specified measure, with a standard base, separable fibres and countable data; their Borel versions are defined on a common conull set. No everywhere-Borel witness choice or determinacy assumption is needed. Takesaki’s book supplies further context for type decomposition.

Throughout Sections 1–3, \(H\) is a fixed infinite-dimensional separable Hilbert space, \(\mathcal V(H)\) is the Effros standard Borel space of unital von Neumann subalgebras of \(B(H)\), and \(a_n(M)\) are Borel contractions strongly-star dense in \(M_1\). Write \(\mathcal P(H)\) for the projections and \(\mathcal T(H)_+\) for the positive trace-class operators. All operator balls carry their common weak/strong/strong-star Borel structure.

## 1. Coding finite corners

For \(D\in\mathcal T(H)_+\), put
\[
\varphi_D(x)=\operatorname{Tr}(Dx),\qquad
s_M(D)=s(\varphi_D|_M)=e_M(s(D)).
\tag{1.1}
\]
Both the last projection and its dependence on \((M,D)\) are Borel by the support lesson.

Let \(\mathcal W\) consist of triples \((M,p,D)\) satisfying
\[
\begin{gathered}
p\in M,\quad p\ne0,\quad D\geq0,\quad \operatorname{Tr}D=1,\quad s_M(D)=p,\\
\operatorname{Tr}\!\left(D\,p a_n(M)p a_m(M)p\right)
=
\operatorname{Tr}\!\left(D\,p a_m(M)p a_n(M)p\right)
\quad(n,m\geq1).
\end{gathered}
\tag{1.2}
\]
This is a Borel subset of
\(\mathcal V(H)\times\mathcal P(H)\times\mathcal T(H)_+\).

Here is the needed evaluation fact. If \(D_j\to D\) in trace norm, \(x_j\to x\) strongly, and \(\|x_j\|\leq C\), then
\[
\operatorname{Tr}(D_jx_j)\longrightarrow\operatorname{Tr}(Dx).
\tag{1.3}
\]
The contribution from \(D_j-D\) is bounded by \(C\|D_j-D\|_1\). Approximate \(D\) in trace norm by finite-rank operators; their traces against \(x_j\) are finite sums of strongly continuous vector coefficients, while the approximation error is uniformly bounded by \(2C\) times the trace-norm error. This proves (1.3). Products of bounded strong-star convergent operators converge strongly-star, so every equation in (1.2) is Borel. Membership and the support condition are already Borel.

**Lemma 1.1.** A nonzero projection \(p\in M\) is finite if and only if some \(D\) makes \((M,p,D)\in\mathcal W\).

**Proof.** Suppose first that (1.2) holds. The functional \(\varphi_D|_M\) is supported on \(p\), so it equals \(x\mapsto\varphi_D(pxp)\). One can see this directly from the Cauchy–Schwarz inequality for a positive functional: its value on \(1-p\) is zero, which annihilates each term with a factor \(1-p\).

The contractions \(p a_n(M)p\) are strongly-star dense in \((pMp)_1\). Indeed, a contraction in \(pMp\) is also a contraction in \(M\), and compressing strong-star approximants preserves convergence. Apply (1.3) to bounded approximating sequences in each variable of the trace equations. The restriction
\[
\tau=\varphi_D|_{pMp}
\]
is a normal tracial state on \(pMp\), and it is faithful because its support is \(p\). If \(v^*v=p\) and \(vv^*\leq p\) for \(v\in pMp\), then
\[
\tau(p-vv^*)=\tau(v^*v)-\tau(vv^*)=0.
\]
Faithfulness gives \(vv^*=p\), so \(p\) is finite.

Conversely, suppose \(p\) is finite. The finite algebra \(pMp\), acting on the separable space \(pH\), has a faithful normal tracial state. To specify the cited trace contract, take its normal faithful centre-valued trace \(T\), choose a faithful normal state \(\omega\) on its centre, and set \(\tau=\omega T\). Such an \(\omega\) exists by restricting a strictly positive trace-class density on \(pH\). Normality, faithfulness and the trace identity follow from the corresponding properties of \(T\).

Extend \(\tau\) to \(M\) by \(x\mapsto\tau(pxp)\). This is positive and normal, has value one at \(1\), and has support exactly \(p\). The positive normal extension theorem supplies a positive trace-class \(D\) on \(H\) representing it. Thus \(\operatorname{Tr}D=1\), its restricted support is \(p\), and all equations in (1.2) hold. \(\square\)

The trace-class operator \(D\) need not have ambient support \(p\). It is the support of its *restriction* to \(M\) that appears in (1.2).

**Proposition 1.2.** The relation
\[
\mathcal F=\{(M,p):p\in M,\ p\text{ is finite}\}
\tag{1.4}
\]
is Borel.

**Proof.** Work in the Borel space of pairs with \(p\in M\). By Lemma 1.1, the nonzero finite pairs form the projection of the Borel set \(\mathcal W\), hence are analytic. Add the Borel zero-projection pairs.

Its complement has the following analytic witness:
\[
v\in M_1,\qquad v^*v=p,\qquad vv^*\leq p,\qquad vv^*\ne p.
\tag{1.5}
\]
These are Borel conditions on \((M,p,v)\). They express precisely that \(p\) is equivalent to a proper subprojection of itself. The first two support equations also give \(v=pvp\), so (1.5) describes an isometry in the corner and introduces no larger ambient equivalence. Both the relation and its complement are analytic. The separation theorem makes the relation Borel. \(\square\)

Taking \(p=1\) proves that the finite-algebra locus \(\mathcal V_{\mathrm f}\) is Borel. The proof gives more than a test for whole algebras: it tests any chosen corner jointly with its ambient algebra.

## 2. Semifiniteness and the type-I locus

A finite projection need not have full central carrier. Recall the following projection characterization:
\[
\begin{aligned}
M\text{ is semifinite}
&\iff \text{some finite }p\in M\text{ has }c_M(p)=1,\\
M\text{ is not of pure type III}
&\iff \text{some nonzero finite }p\in M.
\end{aligned}
\tag{2.1}
\]
The second line is the definition of type III. For the first, the existence direction is Lemma 7.4(2) of the types lesson. Its maximal centrally orthogonal family of finite projections has finite sum and central carrier one. Conversely, a full-carrier finite \(p\) prevents a nonzero type-III central summand: every nonzero central \(z\) has \(zp\ne0\), and \(zp\) is finite. The type decomposition therefore has no type-III part.

**Theorem 2.1.** The semifinite locus and the complement of the pure type-III locus are analytic subsets of \(\mathcal V(H)\).

**Proof.** By Proposition 1.2 and the Borel carrier map, the relations
\[
(M,p)\in\mathcal F,\ c_M(p)=1
\quad\text{and}\quad
(M,p)\in\mathcal F,\ p\ne0
\tag{2.2}
\]
are Borel. Their projections are exactly the two sets in (2.1). Projections of Borel relations between standard Borel spaces are analytic. \(\square\)

This asserts analyticity of the *complement* of pure type III. It does not promote either that complement or the semifinite locus to Borel by this argument.

For type I we use a different construction. Fix \(K=\ell^2(\mathbb N)\) and set
\[
\Theta(M)=(M\bar\otimes B(K))\otimes1_K
\quad\text{on }H\otimes K\otimes K.
\tag{2.3}
\]
The map \(\Theta\) is Borel. To verify this using countable generators, take all
\[
a_n(M)\otimes E_{ij}\otimes1,\qquad n,i,j\geq1.
\]
Their generated von Neumann algebra is exactly (2.3): finite matrix corners and the strong-star density of the \(a_n(M)\) recover all elementary tensors, and the spatial tensor product is generated by those tensors. Each displayed field is Borel, and Borel generation is an Effros theorem.

**Lemma 2.2.** \(M\) is type I if and only if \(\Theta(M)\) is type I. When this holds,
\[
\Theta(M)\cong Z(M)\bar\otimes B(K).
\tag{2.4}
\]
Moreover \(\Theta(M)'\) is sigma-finite and properly infinite.

**Proof.** Apply the existing homogeneous type-I decomposition to \(M\). Since \(H\) is separable, all its nonzero multiplicities are finite or countably infinite. Tensoring each homogeneous part with \(B(K)\) replaces its matrix factor by \(B(K)\). Their countable central sum is \(Z(M)\bar\otimes B(K)\). This proves the forward implication and (2.4).

For the reverse implication, compress by
\[
q=1_H\otimes E_{11}\otimes1_K\in\Theta(M).
\]
The algebra \(q\Theta(M)q\) is normally isomorphic to \(M\). A corner of a type-I algebra is type I: every nonzero projection in the corner majorizes an abelian projection in the large algebra, by Lemma 7.4(1), and that projection remains abelian in the corner. In particular this holds below every nonzero central projection of the corner. Thus \(M\) is type I.

The tensor commutation theorem gives
\[
\Theta(M)'=M'\otimes1_K\bar\otimes B(K).
\tag{2.5}
\]
The last factor contains two isometries with orthogonal ranges summing to \(1\), for instance those sending the standard basis to its even and odd positions. Their tensor lifts show proper infiniteness. A von Neumann algebra on a separable Hilbert space is sigma-finite: a family of nonzero orthogonal projections gives an orthonormal family by choosing a unit vector in each range. \(\square\)

**Theorem 2.3.** The type-I locus \(\mathcal V_{\mathrm I}\) is Borel.

**Proof.** An abelian von Neumann algebra on a separable Hilbert space has at most countably many minimal projections. Their sum \(z_{\mathrm a}\) is its atomic part, isomorphic to \(\ell^\infty(J)\) for a finite or countably infinite set \(J\): multiplication by each minimal projection produces a scalar, and bounded scalar families recover all elements on their sum. The complementary part has no minimal projections. If nonzero, it is isomorphic to \(L^\infty[0,1]\) by the complete diffuse-classification theorem cited above.

Consequently there are only countably many abstract possibilities for such an abelian algebra:
\[
A_{d,\epsilon}=\ell^\infty(d)\oplus
\begin{cases}
0,&\epsilon=0,\\
L^\infty[0,1],&\epsilon=1,
\end{cases}
\quad
d\in\{0,1,2,\ldots,\aleph_0\},\quad \epsilon\in\{0,1\},
\tag{2.6}
\]
with the zero algebra omitted. The weights of atoms do not alter their algebra, and all nonzero diffuse parts have the same normal algebraic model.

By Lemma 2.2, every \(\Theta(M)\) for type-I \(M\) is isomorphic to one of the countably many \(A_{d,\epsilon}\bar\otimes B(K)\). Choose for each of these a faithful normal representation on the fixed space \(H\otimes K\otimes K\) whose commutant is properly infinite; a separable faithful representation followed by infinite identity amplification does this.

The faithful-normal-representation comparison theorem, Theorem 4.1 of [Multiplicity](../reader/supplements/normal-representation-comparison.html), makes any two such representations of the same abstract algebra unitarily equivalent. Its hypotheses hold by (2.5) and separability. Therefore the type-I values of \(\Theta\) belong to a countable union \(\mathcal C\) of fixed unitary classes. Each class is Borel by Theorem 5.1 of the support lesson. Conversely every member of \(\mathcal C\) is type I. Lemma 2.2 now gives
\[
\mathcal V_{\mathrm I}=\Theta^{-1}(\mathcal C),
\]
which is Borel. \(\square\)

The extra identity factor in (2.3) ensures that the represented stabilized algebras have properly infinite commutants. Abstract centre classification alone would not determine an arbitrary representation's unitary class.

**Corollary 2.4.** Among factors on \(H\), the type-I and type-II\(_1\) loci are Borel, and the type-II\(_\infty\) locus is analytic.

**Proof.** The factor locus is Borel: the Borel centre map has value \(\mathbb C1\) exactly there. Intersect it with \(\mathcal V_{\mathrm I}\) for type I. A finite factor outside type I is type II\(_1\), so its locus is
\[
\mathcal V_{\mathrm{factor}}\cap\mathcal V_{\mathrm f}
\setminus\mathcal V_{\mathrm I}.
\]
A semifinite factor that is neither finite nor type I is type II\(_\infty\). Intersect the analytic semifinite locus with the Borel complement of those two loci and with the factor locus. Analytic sets remain analytic under intersection with Borel sets. \(\square\)

## 3. Measurable witnesses on a base

Let \((X,\mu)\) be a standard sigma-finite measure space, and let \(M(x)\) be a measurable field of nonzero von Neumann algebras on separable Hilbert spaces \(H(x)\). We work in the completion of \(\mu\). The usual measurable orthonormal bases partition the base by the dimension of \(H(x)\) and identify the field with a fixed Hilbert space on each part. The proofs above work on every fixed dimension; in finite dimension all algebras are finite and type I. Countably many dimension parts therefore cause no measurability difficulty.

We first replace \(\mu\) by an equivalent probability measure when the represented base is nonempty. The direct-integral base-change unitary preserves all intrinsic algebraic properties. In particular the image measure of the algebra-field map is finite, so the completed-measure selection theorem applies. The empty represented base has zero integral and requires no selections.

Here and below a measure-measurable operator field can be replaced by a Borel field outside a null set. In a standard Borel target, choose a compatible Polish realization and approximate the map by countably valued maps of shrinking error. Replace their measurable level sets by Borel sets modulo null sets, take their pointwise limit where it exists, and use a fixed value elsewhere. The countably many replacements have one common null set. This also applies to trace-class fields.

If \(R\) is one of the Borel witness relations above, apply the measurable-section theorem to its projection. A universally measurable choice of a witness on the projection, composed with \(x\mapsto M(x)\), is measurable for the completed image measure. After the preceding replacement it gives a legitimate measurable field. The assertion is about a specified measure; it does not require a Borel selector for every arbitrary Borel relation.

We shall use the following choices:

- For a nonzero finite \(p(x)\), choose \(D(x)\) in (1.2).
- For a nonfinite \(p(x)\), choose a contraction \(v(x)\) satisfying (1.5).
- For a semifinite factor, choose a nonzero finite \(p(x)\) and a trace witness \(D(x)\).
- For a type-I factor, choose a nonzero abelian \(p(x)\).

The first two relations are Borel even when the prescribed projection varies. The third comes from \(\mathcal W\) with full carrier; its projection is the analytic semifinite locus. For the fourth, the following countable equations give a Borel relation:
\[
p\in M,\quad p\ne0,\quad
[p a_n(M)p,\ p a_m(M)p]=0\quad(n,m\geq1).
\tag{3.1}
\]
Strong-star density proves that these equations say exactly that \(pMp\) is abelian. Its projection is the type-I factor locus: a factor has a nonzero abelian projection precisely when it is type I.

The probability-measure reduction also makes a field of norm-one normal functionals integrable without any extra bound.

**Lemma 3.1.** For a measurable projection \(P=\int^\oplus p(x)\,d\mu(x)\in M=\int^\oplus M(x)\,d\mu(x)\),
\[
P\text{ is finite in }M
\quad\Longleftrightarrow\quad
p(x)\text{ is finite in }M(x)\text{ almost everywhere}.
\tag{3.2}
\]
The fibres here need not be factors.

**Proof.** Suppose the fibre projections are finite. On the set where \(p(x)\ne0\), choose \(D(x)\) by (1.2), and put the functional equal to zero on the remaining set. The fields
\[
\tau_x(a)=\operatorname{Tr}(D(x)a)
\]
are measurable, normal, supported on \(p(x)\), and tracial and faithful on \(p(x)M(x)p(x)\). Their norms are one where nonzero. Their measurability follows from (1.3) and trace-norm measurability of \(D(x)\).

By the varying-predual theorem,
\[
\tau(a)=\int_X\tau_x(a(x))\,d\mu(x)
\tag{3.3}
\]
is normal. It is a trace on \(PMP\). It is faithful there: a nonzero positive \(a\in PMP\) has \(a(x)\ne0\) on a set of positive measure, and on that set \(\tau_x(a(x))>0\). The integral in (3.3) is then positive. A finite faithful normal trace makes \(P\) finite, by the isometry calculation in Lemma 1.1. If \(P=0\), the conclusion is immediate.

Conversely, the set
\[
E=\{x:p(x)\text{ is nonfinite}\}
\]
is measurable by Proposition 1.2. If \(\mu(E)>0\), select \(v(x)\) satisfying (1.5) on \(E\) and put it equal to zero outside \(E\). It integrates to a contraction \(V\in M\) with
\[
V^*V=P_E,\qquad VV^*\leq P_E,\qquad
P_E=\int_E^\oplus p(x)\,d\mu(x).
\]
The defect \(P_E-VV^*\) is nonzero, because its fibre is nonzero at almost every point of \(E\). More explicitly, a countable fundamental vector family detects a nonzero matrix coefficient on a positive-measure subset; hence the decomposable field is not the zero operator. Thus \(P_E\) is infinite. Since \(P_E\leq P\), \(P\) cannot be finite. \(\square\)

The normality in (3.3) uses the previously proved varying-predual theorem. A pointwise monotone-convergence assertion for an arbitrary uncountable global net would not replace that argument.

## 4. Types of a factor integral

Now assume that almost every \(M(x)\) is a factor. Discard any null exceptions and zero fibres. The centre theorem gives
\[
Z(M)=L^\infty(X,\mu)\,1,
\tag{4.1}
\]
so central cuts are precisely restrictions to measurable subsets, modulo null sets.

The fibre sets for type I and finiteness are Borel preimages. The semifinite and non-type-III sets are analytic preimages and hence measurable for the completed measure. Their complements are measurable too. Among factors, type II is semifinite and outside type I, and proper infiniteness is the complement of finiteness. Thus all the fibre sets used below are measurable. We can cut the integral over them.

**Theorem 4.1.** A direct integral of factors over a standard sigma-finite measure space has each of the following properties if and only if almost every fibre has that property:
\[
\text{finite},\quad \text{semifinite},\quad \text{properly infinite},
\quad \text{type I},\quad \text{type II},\quad \text{type III}.
\tag{4.2}
\]

**Proof.**

*Finiteness.* Apply Lemma 3.1 with \(P=1\).

*Proper infiniteness.* For a factor, nonfiniteness is equivalent to proper infiniteness, by the finite/properly infinite central decomposition. Suppose almost all fibres are nonfinite. On every measurable \(E\) of positive measure, select a proper isometry in \(M(x)\) with initial projection \(1\), for \(x\in E\). Its decomposable integral is a proper isometry in \(M_E\): the defect is nonzero by the same countable-vector argument as in Lemma 3.1. Thus no nonzero central projection of \(M\) is finite. The projection-type decomposition says that \(1\) is properly infinite.

Conversely, if the finite-fibre set \(E\) had positive measure, Lemma 3.1 would make the nonzero central projection \(1_E\) finite. This is impossible in a properly infinite algebra. So almost all fibres are properly infinite.

*Semifiniteness.* Suppose the fibres are semifinite. Select nonzero finite projections \(p(x)\) and their trace witnesses as in Section 3. Lemma 3.1 makes their integral \(P\) finite. Every nonzero projection in a factor has central carrier \(1\), and (4.1) shows that \(P\) has global central carrier \(1\): a central field \(1_E\) annihilating \(P\) would force \(p(x)=0\) almost everywhere on \(E\). By (2.1), \(M\) is semifinite.

Conversely, a semifinite \(M\) has a finite projection \(P\) with full carrier, by the good-projection lemma. Lemma 3.1 makes \(p(x)\) finite almost everywhere, and (4.1) and full carrier make it nonzero almost everywhere. A factor with a nonzero finite projection is semifinite. This proves the converse.

*Type I.* Suppose the fibres are type I. Select nonzero abelian \(p(x)\) by (3.1). The integral \(P\) is abelian, since any two elements of \(PMP\) commute in every retained fibre, hence commute globally. It has central carrier \(1\) by (4.1). Below every nonzero central projection \(z\) lies the nonzero abelian projection \(zP\), so \(M\) is type I.

Conversely, a type-I \(M\) has a full-carrier abelian \(P\) by Lemma 7.4(1). Full carrier gives \(p(x)\ne0\) almost everywhere. Choose countably many global measurable contractions \(a_n(x)\) strongly-star dense in \(M(x)_1\) at every retained point. Their compressed global operators commute, because \(PMP\) is abelian. Remove the common null set for their countably many commutator equations. At every remaining point the equations (3.1) hold; density makes \(p(x)M(x)p(x)\) abelian. The factor \(M(x)\) is therefore type I.

*Type III.* If every fibre is type III and \(P\in M\) is finite, Lemma 3.1 makes \(p(x)\) finite almost everywhere. Type-III fibres force \(p(x)=0\), so \(P=0\). Thus \(M\) is type III. Conversely, if the non-type-III fibre set \(E\) had positive measure, its factor fibres would be semifinite. The semifinite direction already proved would produce a nonzero finite projection in \(M_E\subseteq M\). This contradicts type III.

*Type II.* If the fibres are type II, their integral is semifinite by the established case. It has no nonzero abelian projection: the countable-commutator argument in the type-I converse makes the fibres of any abelian projection abelian, and type-II factors force them to be zero. A semifinite algebra with no nonzero abelian projection is type II, by the type decomposition.

Conversely, a type-II integral is semifinite, so almost all fibres are semifinite. The type-I fibre set cannot have positive measure: its nonzero central integral would be type I by the established case and hence would contain a nonzero abelian projection in \(M\). Removing that set leaves only type-II factors. This completes all six equivalences. \(\square\)

**Example 4.2.** Let \(R\) be a finite factor and let
\[
M=R\oplus B(\ell^2).
\]
This is a factor integral over two positive-measure atoms. It is semifinite and nonfinite. It is not properly infinite, since \(1_R\oplus0\) is a nonzero finite central projection. A nonfinite fibre somewhere therefore does not suffice for proper infiniteness of the whole integral; Theorem 4.1 requires the fibre property almost everywhere.

### The individual central type pieces

**Corollary 4.3.** In the standard factor integral of this section, let \(X_{I_n}\), \(X_{I_\infty}\), \(X_{II_1}\), \(X_{II_\infty}\) and \(X_{III}\) be the sets where the fibre has the indicated type, with \(n\geq1\) finite and \(I_\infty=I_{\aleph_0}\). These sets are measurable for the completed measure. Under (4.1), their characteristic functions are exactly the intrinsic central type projections of \(M\). They form a countable partition modulo one null set.

**Proof.** *Finite matrix size.* Fix \(n\). A nonzero factor \(N\) has type \(I_n\) exactly when it has contractions \(e_{ij}\in N\), \(1\leq i,j\leq n\), satisfying
\[
e_{ij}^*=e_{ji},\qquad
e_{ij}e_{kl}=\delta_{jk}e_{il},\qquad
\sum_{i=1}^n e_{ii}=1,
\tag{4.3}
\]
and
\[
[e_{11}a_r(N)e_{11},e_{11}a_s(N)e_{11}]=0
\quad(r,s\geq1).
\tag{4.4}
\]
The full matrix identities force \(e_{11}\ne0\). Strong-star density and bounded multiplication extend (4.4) to all of \(e_{11}Ne_{11}\). The matrix splitting of Proposition 8.4 in the projection lesson identifies \(N\) with \(M_n(e_{11}Ne_{11})\); its centre is the diagonal copy of the centre of the corner, by Lemma 8.2(4). Since \(N\) is a factor and the corner is commutative, the corner is scalar. Thus \(N\cong M_n(\mathbb C)\). Conversely, the usual matrix units in \(M_n(\mathbb C)\) satisfy these conditions in every faithful normal representation.

Membership of each \(e_{ij}\) and the countably many equations (4.3)–(4.4) are Borel conditions on fixed operator balls. Projecting this Borel witness relation gives an analytic \(I_n\)-factor locus. Its inverse image in the base is measurable for the completion by the analytic-image and measurability proofs cited above. Section 3's completed-measure selection, followed by its conull Borel repair, supplies measurable matrix units on \(X_{I_n}\). Their bounded integrals satisfy (4.3). Their first diagonal corner is abelian because it is abelian in almost every fibre. All diagonal projections are equivalent; their central carriers are equal and their sum is the identity of the cut, so each has full central carrier. This makes \(M_{X_{I_n}}\) homogeneous of type \(I_n\).

Conversely, suppose a central cut \(M_E\) has type \(I_n\). Its homogeneous decomposition supplies \(n\) abelian full-carrier projections with sum \(1_E\); Lemma 9.3 and Proposition 8.4 of the projection lesson supply full matrix units. Write these finitely many operators as measurable fields. The matrix identities hold outside one null set. Compress the countable global dense fields used in the type-I converse of Theorem 4.1 by the first diagonal projection. Their commutators vanish globally, hence outside a further common null set. Equations (4.3)–(4.4) then show that \(M(x)\) has type \(I_n\) almost everywhere on \(E\). Thus \(1_{X_{I_n}}\) is the largest \(n\)-homogeneous central projection: every such central cut lies below it modulo null sets.

*The remaining types.* A type-I factor on a separable Hilbert space is either \(I_n\) for a finite \(n\), or \(I_{\aleph_0}\), by Theorem 10.3 and Corollary 10.4 of the projection lesson. Hence
\[
X_{I_\infty}=X_I\setminus\bigcup_{n\geq1}X_{I_n}.
\tag{4.5}
\]
This is measurable. Its integral is type I and properly infinite by Theorem 4.1. On the separable direct-integral Hilbert space, the homogeneous type-I decomposition has only finite or countably infinite multiplicities. Proper infiniteness excludes every nonzero finite homogeneous central cut. Thus this integral is homogeneous \(I_{\aleph_0}\). Conversely, a homogeneous \(I_{\aleph_0}\) central cut is type I and properly infinite, so Theorem 4.1 puts almost all its fibres in \(X_{I_\infty}\).

For factors, type \(II_1\) means type II and finite, and type \(II_\infty\) means type II and properly infinite. Their measurable fibre sets are therefore the corresponding intersections of the sets already constructed in Theorem 4.1. Apply both relevant equivalences of that theorem to each central cut to obtain the largest central projection of each type. Its type-III equivalence gives the same assertion for \(X_{III}\). The factor type decomposition makes these sets disjoint and exhaustive. There are countably many type pieces and equations, so all exceptional sets used in this proof may be united into one null set. The uniqueness of the intrinsic type decomposition then identifies the characteristic functions with its central projections. \(\square\)

The corollary applies to a given standard factor disintegration. Existence of that disintegration is a separate assertion proved in the central-decomposition unit. No assertion about arbitrary nonseparable factor fields is added here.

## 5. Graded exercises with solutions

**Exercise 5.1 — introductory: one corner, three conclusions.** In \(M=B(\ell^2(\mathbb N))\), let \(p\) be the projection onto the first coordinate. Verify the finite-corner trace witness, compute its central carrier, and determine which of finiteness, semifiniteness and pure type III hold for \(M\). Explain why replacing full carrier by nonzero in the first line of (2.1) loses information when central summands are allowed.

**Solution.** Take \(D=p\), whose trace is one. Since the ambient algebra is all of \(B(\ell^2)\), \(s_M(D)=p\). The corner is \(\mathbb Cp\), so the trace equations hold. The rank-one projection is finite. The centre of \(M\) is \(\mathbb C1\), hence \(c_M(p)=1\). Thus \(M\) is semifinite.

The unilateral shift \(S\) satisfies \(S^*S=1\) and \(SS^*=1-p\); it proves that \(M\) is not finite. The nonzero finite \(p\) excludes pure type III. Thus full carrier and a finite corner give semifiniteness, while they do not assert that the whole identity is finite.

For the last distinction, take a direct sum \(N_{\mathrm f}\oplus N_{\mathrm{III}}\), with a nonzero finite algebra and a nonzero type-III algebra. The projection \(1_{N_{\mathrm f}}\oplus0\) is nonzero and finite, so the algebra is not of pure type III. Every finite projection vanishes on \(N_{\mathrm{III}}\), since its central cut there would otherwise be a nonzero finite projection. No finite projection has full central carrier, so the algebra is not semifinite.

**Exercise 5.2 — intermediate: why both stabilization factors occur.** Let \(M=M_2(\mathbb C)\oplus M_3(\mathbb C)\) and \(N=M_4(\mathbb C)\oplus M_7(\mathbb C)\), in their standard faithful finite-dimensional representations. Compute the abstract algebras after tensoring with \(B(\ell^2)\). Show that their further infinite identity amplifications are unitarily equivalent on a fixed separable infinite-dimensional Hilbert space. Contrast this with identity amplification alone.

**Solution.** Regrouping tensor factors gives
\[
M\bar\otimes B(\ell^2)\cong B(\ell^2)\oplus B(\ell^2)
\cong N\bar\otimes B(\ell^2),
\]
because \(\mathbb C^r\otimes\ell^2\) has countably infinite dimension for each positive finite \(r\). After identity amplification the two faithful normal representations have properly infinite sigma-finite commutants, one \(B(\ell^2)\) commutant on each central summand. Their unitary equivalence follows from the representation comparison theorem; it can also be obtained by separately identifying the countably infinite defining Hilbert spaces on the two summands and the multiplicity spaces.

In contrast, \(M\otimes1_{\ell^2}\) is still abstractly \(M_2\oplus M_3\), and \(N\otimes1_{\ell^2}\) is still \(M_4\oplus M_7\). They are not isomorphic: an isomorphism must permute their two minimal central summands, but the corresponding simple matrix algebras have dimensions \(4,9\) versus \(16,49\) as complex vector spaces. Thus identity amplification alone does not erase the finite matrix sizes. The first stabilization factor erases those sizes; the second supplies the commutant hypothesis needed for unitary comparison.

**Exercise 5.3 — advanced: unbounded matrix sizes in a finite field.** Partition \((0,1]\) into \(I_n=(2^{-n-1},2^{-n}]\), \(n\geq0\), with Lebesgue measure. On \(I_n\), let \(M(x)=M_{n+1}(\mathbb C)\) in its defining representation. Construct a faithful normal tracial state on the integral and determine its type. Then replace the fibres on \(I_0\) by \(B(\ell^2)\). Determine finiteness, semifiniteness and proper infiniteness of the modified integral, and exhibit a finite projection of full central carrier.

**Solution.** On \(I_n\) put
\[
\tau_x(a)=\frac{1}{n+1}\operatorname{Tr}_{n+1}(a).
\]
This is a measurable norm-one field of faithful normal tracial states. Therefore
\[
\tau(a)=\sum_{n=0}^{\infty}
\int_{I_n}\frac{\operatorname{Tr}_{n+1}(a(x))}{n+1}\,dx
\]
is a normal state and trace by the varying-predual theorem. For positive nonzero \(a\), some set of positive measure has \(a(x)\ne0\), where \(\tau_x(a(x))>0\); hence \(\tau\) is faithful. The integral is finite and type I. The matrix dimensions need not have a uniform bound.

In the modified integral all fibres are still type I and semifinite. Its central cut over \(I_0\) is properly infinite, witnessed by the constant unilateral-shift field, so the whole algebra is nonfinite. Its complementary central cut, over \((0,1/2]\), is nonzero and finite, so the whole algebra is not properly infinite.

Choose \(p(x)\) rank one on \(I_0\) and equal to the identity on every other \(I_n\). Each \(p(x)\) is nonzero and finite, so Lemma 3.1 makes \(P=\int^\oplus p(x)\,dx\) finite. Since the fibres are factors and the projection is nonzero everywhere, (4.1) gives \(c_M(P)=1\). This explicitly witnesses global semifiniteness.

## References

- [Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer, New York, 1979.
- [Effros] Edward G. Effros, [The Borel space of von Neumann algebras on a separable Hilbert space](https://msp.org/pjm/1965/15-4/pjm-v15-n4-p07-s.pdf), *Pacific Journal of Mathematics* 15(4) (1965), 1153–1164.
- [Lurie 18–20] Jacob Lurie, *Math 261y: von Neumann Algebras*, [Lecture 18](https://www.math.ias.edu/~lurie/261ynotes/lecture18.pdf), [Lecture 19](https://www.math.ias.edu/~lurie/261ynotes/lecture19.pdf) (17 October 2011), and [Lecture 20](https://www.math.ias.edu/~lurie/261ynotes/lecture20.pdf) (19 October 2011).
- [Vaes–Wouters] Stefaan Vaes and Lise Wouters, [Borel fields and measured fields of Polish spaces, Banach spaces, von Neumann algebras and C*-algebras](https://arxiv.org/html/2405.16603v2), arXiv:2405.16603v2 (3 April 2025). Their Proposition 3.2 obtains dense sections on a conull Borel set from a countable Borel basis; Proposition 2.5 has the additional hypothesis of analytic determinacy.
