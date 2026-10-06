# Expectations, traces and ideals in crossed products

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A representation of a crossed product can forget group directions while faithfully representing every coefficient. The reduced construction prevents this in two useful ways. Its matrix entries recover an element from its coefficients; for a topologically free action on a space, functions with sufficiently small support also test whether a representation is faithful. These two observations lead to the expectation and simplicity theorems.

We use the regular model proved in [Reduced crossed products and Fell's absorption principle](KT-CP-02.md). The expectation and trace sections use counting measure. The final structural theorem uses left and right Haar measure on a second countable locally compact group, with a separable coefficient algebra. A discrete group \(\Gamma\) may be uncountable, and a coefficient C*-algebra \(A\) may be nonunital. Compactness is assumed only in the statements about probability measures and tracial states on \(C(X)\).

The principal sources for comparison are [Archbold–Spielberg 1994], [Exel 2017, Chapter 29], and the transformation-group examples in [Blackadar 2006]. Our proof starts with the entries of the regular operator, then uses them in a norm test for representations. We finish with the full quasi-orbit classification for an amenable group acting freely on the primitive ideal space, including the measure and representation arguments needed for noncommutative coefficients.

## Reading an element through its matrix entries

Let \(\alpha:\Gamma\to\operatorname{Aut}(A)\) be an action. Write \(B=A\rtimes_{\alpha,r}\Gamma\). A dense *-subalgebra consists of finite sums

\[
p=\sum_{g\in F}a_g u_g,\qquad
(a u_g)(b u_h)=a\alpha_g(b)u_{gh},\qquad
(a u_g)^*=\alpha_{g^{-1}}(a^*)u_{g^{-1}}.
\tag{1}
\]

When \(A\) is nonunital, \(u_g\) is a multiplier of \(B\); each \(a u_g\) is still an element of \(B\). In particular, expressions such as \(xu_g^*\) remain in \(B\). The copy of \(A\) is isometric.

Choose a faithful nondegenerate representation \(\rho:A\to B(H)\), and realize \(B\) faithfully on \(\ell^2(\Gamma,H)\). For \(t\in\Gamma\), let \(V_t:H\to\ell^2(\Gamma,H)\) insert a vector in coordinate \(t\). The regular formulas give

\[
V_t^*pV_r=\rho\!\left(\alpha_{t^{-1}}(a_{tr^{-1}})\right).
\tag{2}
\]

Indeed, \(u_g\) takes the \(r\) coordinate to the \(gr\) coordinate, so it contributes to row \(t\) precisely when \(g=tr^{-1}\). This order matters when the group is nonabelian.

**Theorem 3.1 (expectation and coefficients).** The coefficient rule

\[
E(p)=a_e
\tag{3}
\]

extends to a completely positive contractive map \(E:B\to A\). It fixes \(A\), is \(A\)-bimodular, and is faithful: \(E(x^*x)=0\) implies \(x=0\). Thus it is a faithful conditional expectation. For each \(g\), define

\[
a_g(x)=E(xu_g^*).
\tag{4}
\]

Every \(x\in B\) is uniquely determined by the family \((a_g(x))_{g\in\Gamma}\).

**Proof.** Equation (2), with \(t=r=e\), identifies \(\rho(E(p))\) with \(V_e^*pV_e\). Compression is contractive. If polynomials converge in \(B\), their compressed operators converge in norm, and their values belong to the closed algebra \(\rho(A)\). Isometry of \(\rho\) therefore defines a unique bounded extension \(E\) with

\[
\rho(E(x))=V_e^*xV_e.
\tag{5}
\]

Matrix amplification of compression is positive at every level. Since a faithful C*-representation reflects positivity, (5) proves complete positivity of \(E\). Polynomial multiplication gives \(E(axb)=aE(x)b\); continuity extends this identity to arbitrary \(x\). The same computation gives \(E(a)=a\). Its norm is one if \(A\ne0\); if \(A=0\), both algebras and this map are zero.

All matrix entries extend continuously from polynomials. Thus

\[
V_t^*xV_r
=\rho\!\left(\alpha_{t^{-1}}(a_{tr^{-1}}(x))\right).
\tag{6}
\]

In particular,

\[
V_t^*x^*xV_t=\rho\!\left(\alpha_{t^{-1}}(E(x^*x))\right).
\tag{7}
\]

If \(E(x^*x)=0\), then \(\|xV_t v\|^2=0\) for every \(t\) and \(v\in H\). Finite-coordinate vectors are dense in \(\ell^2(\Gamma,H)\), even when \(\Gamma\) is uncountable. Hence \(x=0\). Applying this to \(x=b^{1/2}\) also shows that a positive element \(b\) with \(E(b)=0\) vanishes.

Finally, if every coefficient in (4) is zero, (6) makes every matrix entry zero. Pairing \(x\) with finite-coordinate vectors, followed by density, gives \(x=0\). Subtract two elements to obtain the uniqueness assertion. \(\square\)

For a polynomial, the positivity formula takes a particularly useful form:

\[
E(p^*p)=\sum_g\alpha_{g^{-1}}(a_g^*a_g).
\tag{8}
\]

It resembles a sum of squared coefficients, but the action transports each square back to the identity coordinate.

In the Hilbert \(A\)-module model, if \(A\) is unital and \(\delta_e\) denotes the vector equal to \(1_A\) at \(e\), then

\[
E(x^*x)=\langle x\delta_e,x\delta_e\rangle_A.
\tag{9}
\]

For nonunital \(A\), there is no such vector with entry \(1_A\). One can instead test vectors supported at \(e\) with entries from \(A\), or use (5)–(7); these formulas require no unit.

**Coefficients are not a summation theorem.** Equation (4) does not assert norm convergence of \(\sum_g a_g(x)u_g\), in any particular order. Already for \(\Gamma=\mathbb Z\), ordinary symmetric Fourier partial sums of a continuous function need not converge uniformly. The injectivity assertion comes from matrix entries, not from assuming convergence of the formal Fourier series.

For the full crossed product \(B_u=A\rtimes_\alpha\Gamma\), let \(q:B_u\to B\) be the canonical quotient and put \(E_u=E q\). This is a completely positive conditional expectation. It is faithful exactly when \(q\) is injective: a nonzero element of \(\ker q\) disproves faithfulness, and the converse follows from Theorem 3.1. Consequently the same coefficient uniqueness argument cannot be applied to an arbitrary full crossed product without an additional hypothesis.

## Turning invariant coefficient traces into traces

A tracial state \(\tau\) on \(A\) is **invariant** if \(\tau\alpha_g=\tau\) for every \(g\). A state has norm one; this definition also makes sense for a nonunital algebra.

**Proposition 3.2 (the diagonal trace).** If \(\tau\) is an invariant tracial state on \(A\), then \(\tau E\) is a tracial state on \(B\). It is faithful if \(\tau\) is faithful. Likewise \(\tau E_u\) is a tracial state on the full crossed product.

**Proof.** Complete positivity and contractivity of \(E\) make \(\tau E\) positive with norm at most one. Its restriction to the isometric copy of \(A\) is \(\tau\), so its norm is at least one.

It remains to check the trace identity. Two elementary terms in (1) have zero identity coefficient in either product unless \(h=g^{-1}\). In that case,

\[
\begin{aligned}
\tau(E((a u_g)(b u_{g^{-1}})))
&=\tau(a\alpha_g(b))\\
&=\tau(\alpha_{g^{-1}}(a)b)\\
&=\tau(b\alpha_{g^{-1}}(a))\\
&=\tau(E((b u_{g^{-1}})(a u_g))).
\end{aligned}
\tag{10}
\]

Linearity proves the identity for polynomials. Norm approximation and boundedness of the state prove it for all pairs in \(B\). If \(\tau E(x^*x)=0\), faithfulness of \(\tau\) gives \(E(x^*x)=0\), and Theorem 3.1 gives \(x=0\). Composing the reduced trace with \(q\) proves the full assertion. \(\square\)

This is often called the dual trace; for \(\mathbb Z\), its coefficient formula appears at the start of [Blackadar 1998]. Invariance is a real requirement. For example, on \(A=\mathbb C^2\) with the flip action of \(\mathbb Z/2\), evaluation on the first summand is a trace on \(A\). Its composition with \(E\) is not a trace on the crossed product: for the projection \(p=(1,0)\),

\[
(\tau E)(u p u^*)=0,\qquad (\tau E)(p)=1.
\]

A trace on the crossed product must give equal values to these unitarily conjugate projections.

## When every trace is diagonal

Let \(X\) be a nonempty compact Hausdorff space. A left action of \(\Gamma\) on \(X\) induces \(\alpha_g(f)(x)=f(g^{-1}x)\). An action is **free** if \(gx=x\) forces \(g=e\). It is **topologically free** if, for each \(g\ne e\), its fixed-point set has empty interior. The latter allows fixed points.

The trace statement has a useful stronger form than the \(\mathbb Z\) case.

**Theorem 3.3 (traces of a free action).** For a free action of any discrete \(\Gamma\) on compact \(X\), restriction to \(C(X)\) is an affine bijection from tracial states of \(C(X)\rtimes_r\Gamma\) onto invariant probability measures on \(X\). Its inverse is

\[
\mu\longmapsto T_\mu,\qquad
T_\mu(x)=\int_X E(x)\,d\mu.
\tag{11}
\]

The same statement holds for the full crossed product, using \(E_u\). In particular, all its tracial states factor through the reduced quotient.

**Proof.** A tracial state \(T\) restricts to a state on \(C(X)\). By the Riesz representation theorem, this state is integration against a unique regular Borel probability measure \(\mu\). Unitary covariance and the trace identity give

\[
T(\alpha_g(f))=T(u_g f u_g^*)=T(f),
\]

so \(\mu\) is invariant.

Fix \(g\ne e\). Every point has a neighborhood \(U\) with \(U\cap gU=\varnothing\): separate the point and its \(g\)-translate and then shrink. Compactness gives a finite cover by such neighborhoods. Choose a continuous partition of unity \((k_i)\) subordinate to this cover, and set \(h_i=k_i^{1/2}\). We may arrange that each support lies in its covering neighborhood, and \(\sum_i h_i^2=1\). For any \(f\in C(X)\),

\[
h_i(fu_g)h_i=f h_i\alpha_g(h_i)u_g=0.
\tag{12}
\]

Using the trace identity rather than any approximation of \(T\), we obtain

\[
T(fu_g)=\sum_i T((fu_g)h_i^2)
=\sum_i T(h_i(fu_g)h_i)=0.
\tag{13}
\]

Thus \(T\) agrees with (11) on polynomials and hence everywhere. Conversely, an invariant probability measure defines an invariant coefficient trace, so Proposition 3.2 proves that (11) is a tracial state. Restriction recovers the measure. Both maps are affine. The proof of (12)–(13) uses only covariance and finite sums, so it also works in the full algebra. \(\square\)

In particular, a free uniquely ergodic homeomorphism gives a unique tracial state on both \(C(X)\rtimes\mathbb Z\) and \(C(X)\rtimes_r\mathbb Z\). Unique ergodicity means existence and uniqueness of an invariant probability measure; it does not merely mean that every orbit is dense.

Topological freeness alone is insufficient for this trace classification. A reflection of the circle by \(\mathbb Z/2\) has fixed points but their set has empty interior. At a fixed point, evaluation of coefficients together with either one-dimensional representation of \(\mathbb Z/2\) gives a tracial state on the full crossed product. Both states have the same restriction to \(C(X)\), but give opposite values to the group generator. For a finite group the full and reduced algebras coincide, as proved in the next lesson; the distinction therefore persists for the reduced algebra as well.

## A norm test using a small support

The ideal theorem needs only topological freeness. The essential step is a compression that deletes finitely many group directions while retaining most of a positive identity coefficient.

**Lemma 3.4 (finite compression).** Suppose the action on compact \(X\) is topologically free. For every positive \(b\in C(X)\rtimes_r\Gamma\) and \(\varepsilon>0\), there is \(h\in C(X)\), with \(0\le h\le1\), such that

\[
\|hbh-hE(b)h\|<2\varepsilon,\qquad
\|hE(b)h\|>\|E(b)\|-\varepsilon.
\tag{14}
\]

If \(E(b)=0\), replace the strict second inequality by its automatic nonnegative version.

**Proof.** Choose a polynomial \(p=\sum_{g\in F}a_g u_g\) with \(\|b-p\|<\varepsilon\). If \(E(b)\ne0\), the open set

\[
W=\{x:E(b)(x)>\|E(b)\|-\varepsilon\}
\]

is nonempty (if the threshold is negative, the whole space works). Each \(\operatorname{Fix}(g)\), \(g\ne e\), is closed because \(X\) is Hausdorff. Its complement is open and dense. A finite intersection of open dense sets is dense: intersect a nonempty open set with them successively. We can therefore choose

\[
x_0\in W\setminus\bigcup_{g\in F\setminus\{e\}}\operatorname{Fix}(g).
\]

Separate \(x_0\) and \(gx_0\) for each of the finitely many \(g\)'s. A common smaller open neighborhood \(U\) of \(x_0\) has \(U\cap gU=\varnothing\) for all of them. Normality of compact Hausdorff \(X\) supplies a continuous \(h\), supported in \(U\), with \(0\le h\le1\) and \(h(x_0)=1\). Equation (12) gives

\[
hph=hE(p)h.
\tag{15}
\]

The two errors between (15) and the first expression in (14) are bounded by \(\|b-p\|\) and \(\|E(b-p)\|\). Contractivity of \(E\) proves the first inequality. Evaluating \(hE(b)h\) at \(x_0\) proves the second.

If \(E(b)=0\), Theorem 3.1 already gives \(b=0\); take \(h=0\). \(\square\)

Only a finite set of group elements is avoided. We have not assumed that points with trivial stabilizer form a dense set for an arbitrary uncountable group.

**Theorem 3.5 (intersection and uniqueness).** For a topologically free action on compact Hausdorff \(X\), every nonzero closed two-sided ideal of \(C(X)\rtimes_r\Gamma\) intersects \(C(X)\) nontrivially. Equivalently, a C*-homomorphism out of this crossed product is injective whenever its restriction to \(C(X)\) is injective.

**Proof.** Let \(J\) have zero intersection with \(C(X)\), and let \(Q:B\to B/J\) be the quotient. Its restriction to \(C(X)\) is injective and hence isometric. For a positive \(b\in J\), Lemma 3.4 gives

\[
\begin{aligned}
\|E(b)\|-\varepsilon
&<\|hE(b)h\|\\
&=\|Q(hE(b)h)\|\\
&=\|Q(hE(b)h-hbh)\|<2\varepsilon.
\end{aligned}
\tag{16}
\]

Here \(hbh\in J\). Letting \(\varepsilon\) tend to zero gives \(E(b)=0\), hence \(b=0\). Every \(y\in J\) has \(y^*y\in J\), so \(J=0\). Apply this to a homomorphism's kernel to get the equivalent formulation. \(\square\)

The same proof gives the result for \(C_0(X)\) when \(X\) is locally compact Hausdorff: use a compactly supported bump function in \(U\), and choose a point where the nonzero positive \(E(b)\) is close to its supremum. This avoids any unit or compactness argument in (14)–(16).

For a full crossed product, the corresponding conclusion is that an ideal disjoint from the coefficient algebra is contained in the kernel of the reduced quotient. This follows by replacing \(E\) by \(E_u\) in (14)–(16) and then using faithfulness of \(E\) on \(q(b)\). This is the commutative case of [Archbold–Spielberg 1994, Theorem 1].

## Minimality removes the remaining ideals

An action on a nonempty space is **minimal** if every orbit is dense. For a group of homeomorphisms, this is equivalent to saying that the only invariant open sets are \(\varnothing\) and \(X\). Indeed, an orbit closure is closed and invariant. Conversely, a nonempty closed invariant set contains an orbit and therefore contains its closure; if every orbit is dense, that set is all of \(X\). Take complements to obtain the assertion about open sets.

**Corollary 3.6 (simplicity).** If the action on a nonempty locally compact Hausdorff space \(X\) is minimal and topologically free, then \(C_0(X)\rtimes_r\Gamma\) is simple.

**Proof.** Let \(J\ne0\) be an ideal. Theorem 3.5 and its locally compact version give \(J\cap C_0(X)\ne0\). This intersection is a closed ideal of \(C_0(X)\), so it is \(C_0(U)\) for a nonempty open set \(U\subseteq X\). It is invariant: conjugation by the canonical multiplier \(u_g\) preserves \(J\) and \(C_0(X)\). Minimality gives \(U=X\).

Thus \(C_0(X)\subseteq J\). If \((e_i)\) is an approximate identity of \(C_0(X)\), then \(e_i(a u_g)\to a u_g\) in norm for every elementary term. Finite sums are dense, so \(J\) contains the entire crossed product. \(\square\)

For compact \(X\), the last step can instead use \(1\in J\). The locally compact proof explains why the argument works without a unit.

This is a simplicity theorem for the reduced algebra, without an amenability or exactness assumption. It does not identify every ideal with an invariant open set for every topologically free action. Such a stronger assertion needs control of quotient actions and, in appropriate formulations, exactness.

## Three dynamics to keep in view

**Irrational rotation.** Let \(R_\theta(z)=e^{2\pi i\theta}z\), with irrational \(\theta\), and take \(\alpha(f)=f\circ R_\theta^{-1}\). Every nonzero power is fixed-point free. Every orbit is dense: the closure of the subgroup generated by \(e^{2\pi i\theta}\) is a closed infinite subgroup of the circle; a proper closed subgroup of the circle is finite. Corollary 3.6 gives simplicity of the reduced rotation algebra.

There is exactly one invariant probability measure. If \(\mu\) is invariant, then for \(n\ne0\),

\[
\int_{\mathbb T}z^n\,d\mu
=e^{-2\pi i n\theta}\int_{\mathbb T}z^n\,d\mu,
\]

so the integral is zero. The constant coefficient is one. Trigonometric polynomials are dense in \(C(\mathbb T)\), so these values characterize normalized Haar measure. Theorem 3.3 gives a unique trace, with

\[
T(z^m u^n)=
\begin{cases}1,&m=n=0,\\0,&\text{otherwise}.\end{cases}
\tag{17}
\]

Our covariance convention is \(u z u^*=e^{-2\pi i\theta}z\), equivalently \(z u=e^{2\pi i\theta}u z\). Reversing the implementing generator changes the displayed sign, not the preceding arguments.

**A Cantor odometer.** Fix an integer \(d\ge2\). Put \(X=\varprojlim\mathbb Z/d^k\mathbb Z\), and let \(T(x)=x+1\). This is a compact metrizable totally disconnected space with no isolated points, hence a Cantor space. Cylinder neighborhoods specify finitely many residues. An orbit visits every such cylinder, because addition by one is transitive modulo \(d^k\). The action is minimal.

If \(T^n x=x\), then every \(d^k\) divides \(n\), so \(n=0\). The action is free. An invariant measure must assign mass \(d^{-k}\) to each cylinder at level \(k\), because those cylinders are cyclically permuted. These values define the inverse-limit probability measure and determine it uniquely: cylinder functions are uniformly dense. The resulting reduced crossed product is simple with a unique trace. This is a standard Bunce–Deddens dynamical model; the relationship with the torsion-rotation model is described in [Blackadar 2006]. No classification by supernatural numbers is needed for our conclusions.

For any minimal homeomorphism of an infinite Cantor space, the action of \(\mathbb Z\) is free: a periodic point would have a finite closed orbit, and minimality would force the whole space to be that finite set. Thus the simplicity conclusion holds generally; unique trace requires the additional unique ergodicity hypothesis.

**Rational rotation.** If \(\theta=p/q\), in lowest terms, every orbit is finite. On the circle these orbits are proper closed invariant subsets. Restriction to one orbit \(O\) gives a surjective reduced crossed-product map

\[
C(\mathbb T)\rtimes_r\mathbb Z
\longrightarrow C(O)\rtimes_r\mathbb Z
\tag{18}
\]

by the quotient functoriality of the preceding lesson. Its kernel contains a nonzero continuous function vanishing on \(O\), and its range is nonzero. Hence the source is not simple. This proof does not infer nonsimplicity merely from failure of the sufficient hypothesis.

Another obstruction appears in the generators: \(u^q\) commutes with both coefficients and \(u\). It is a nonscalar central unitary, since its \(q\)-coefficient is \(1\) while a scalar has zero coefficient there. A simple unital C*-algebra has scalar center. The quotient argument above proves the obstruction directly and also covers \(q=1\).

## Quasi-orbits for a free action on the primitive ideal space

The compression argument above concerns functions on a space and a discrete group. We now prove the broader ideal theorem for a separable C*-algebra and a second countable locally compact group. The action is assumed free on its **primitive ideal space**, not merely on a chosen commutative subalgebra. This section supplies the general result attributed to Green and to Gootman–Rosenberg. We use the ideal-centre and local-normalization methods explained in Dana Williams, *Crossed Products of C*-Algebras*, author draft, §8.2 and Chapter 9, Step V, specializing the stabilizers to the trivial group. The argument below includes the needed support lemmas.

Let \(A\) be separable, let \(G\) be second countable and locally compact, and let \(\alpha\) be a strongly continuous action. An ideal is closed and two-sided. A **primitive ideal** is the kernel of an irreducible representation. Write \(X=\operatorname{Prim}(A)\), with the hull–kernel topology: its open sets are
\[
 U_J=\{P\in X:J\not\subseteq P\},\qquad J\triangleleft A.
 \tag{3Q.1}
\]
The action is \(sP=\alpha_s(P)\). For \(P\in X\), its **orbit core** is
\[
 I_P=\bigcap_{s\in G}sP.
 \tag{3Q.2}
\]
Its hull is exactly \(\overline{GP}\): closed hulls are intersections of the primitive ideals they contain, since irreducible representations separate every C*-quotient. A **quasi-orbit** identifies \(P,Q\) when these closures agree, equivalently when \(I_P=I_Q\). Give the set of quasi-orbits the quotient topology from \(X\).

**Theorem 3.7 (free primitive-space ideal theorem).** Suppose \(G\) is amenable and \(sP=P\) implies \(s=e\) for every \(P\in X\). Then contraction and extension are inverse order isomorphisms
\[
 \{G\text{-invariant ideals of }A\}
 \longleftrightarrow
 \{\text{ideals of }A\rtimes_\alpha G\},
 \quad I\longmapsto I\rtimes_\alpha G.
 \tag{3Q.3}
\]
The full and reduced crossed products agree. The assignment
\[
 [P]\longmapsto I_P\rtimes_\alpha G
 \tag{3Q.4}
\]
is a homeomorphism from the quasi-orbit space onto \(\operatorname{Prim}(A\rtimes_\alpha G)\). For a nondiscrete group the coefficients belong to the multiplier algebra, so contraction means
\[
 I(J)=\{a\in A:i_A(a)(A\rtimes G)\subseteq J\}.
 \tag{3Q.5}
\]
For a discrete group this is the usual intersection with \(A\). In particular this statement does not require \(A\) to be commutative or type I, or the original primitive space to be Hausdorff.

We first establish the primitive-space tools, then compare two representations, and finally deduce the ideal theorem.

### Primitive ideals, prime ideals and dense orbits

An algebra is **prime** if it is nonzero and two nonzero ideals have nonzero product. It is **\(G\)-prime** if it is nonzero and this holds for nonzero invariant ideals. A nonzero quotient has these properties when its proper kernel is called prime or \(G\)-prime, respectively. The theorem is immediate for \(A=0\); henceforth take \(A\ne0\).

**Lemma 3.8.** In a separable \(G\)-prime C*-algebra there is \(P\in\operatorname{Prim}(A)\) with \(I_P=0\). For the trivial group this says that every separable prime C*-algebra has a faithful irreducible representation.

**Proof.** Choose a countable norm-dense set of positive elements \(b_j\). The nonzero ideals generated by \((b_j-t)_+\), for positive rational \(t\), form a countable list \(J_n\) such that every nonzero ideal contains one of them. Indeed, approximate a nonzero positive element \(b\in J\) by \(b_j\), with \(\|b-b_j\|<t<\|b_j\|\). In \(A/J\), the image of \(b_j\) has norm less than \(t\), so \((b_j-t)_+\in J\), and it is nonzero. The same approximation with \(t\to0\) shows that every ideal is generated by the members of this list that it contains.

We construct nonzero hereditary subalgebras \(B_n\), positive contractions \(a_n\) of norm one, and group elements \(s_n\), so that
\[
 a_n\in B_{n-1}\cap\alpha_{s_n}(J_n),\qquad
 a_m b=b\quad(b\in B_n, m\le n).
 \tag{3Q.6}
\]
Start with \(B_0=A\). If \(B\ne0\) is hereditary, let \(K\) be the ideal it generates. The invariant ideals generated by all translates of \(K\) and \(J_n\) have nonzero product. Some product \(K\alpha_s(J_n)\) is consequently nonzero, after translating back. Then \(B\cap\alpha_s(J_n)\ne0\). To verify this last step, if \(b\in B_+\), \(x\in A\) and \(j\in\alpha_s(J_n)\) satisfy \(bxj\ne0\), the element \(bxjj^*x^*b\) is nonzero, positive and belongs to that intersection. If all such products vanished, \(K\alpha_s(J_n)\) would vanish.

Choose a nonzero positive element \(c\) in that intersection and rescale it to norm one. Functional calculus gives a positive contraction \(a_n=f(c)\), with \(f=1\) on \([3/4,1]\) and \(f=0\) on \([0,1/2]\). Let \(B_n\) be the nonzero hereditary subalgebra generated by \(g(c)\), where \(g\ge0\) vanishes outside \((3/4,1]\) and \(g(1)>0\). Then \(a_n\) acts as the identity on \(B_n\), and the earlier identities are retained.

In the state space of the unitization, the sets \(F_n=\{\varphi:\varphi(a_n)=1\}\) are nonempty compact faces. They are nested: if a state is one on \(a_{n+1}\), its cyclic vector is fixed by \(a_{n+1}\); the relation \(a_na_{n+1}=a_{n+1}\) makes it fixed by \(a_n\) too. Their intersection is a nonempty compact face. It has an extreme point without any selection assumption: successively maximize evaluations at a countable dense set of self-adjoint elements, retaining nested nonempty compact faces. The intersection of these faces contains exactly one functional, since those elements distinguish states. That functional is extreme in the original state space, hence pure. Its restriction to \(A\) is nonzero, and its GNS representation is irreducible. If its kernel \(P\) had a nonzero orbit core, that ideal would contain some \(J_n\), and therefore \(\alpha_{s_n}(J_n)\subseteq P\), contradicting \(\varphi(a_n)=1\). Thus \(I_P=0\). \(\square\)

The foundational facts about states and GNS representations used here are proved in the existing programme chapter [Representations and positive functionals](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html#OA-FND-GN-10), Theorem 8.3, Proposition 8.4 and Theorem 8.5. These are written prerequisite proofs. The hereditary construction above proves the additional separable prime and orbit-core assertions.

### A measurable primitive space with a continuous action

We shall use a finer topology on \(X\) during the measure argument. Its Borel sets are the same as those of the hull–kernel topology. The latter still governs the final homeomorphism.

**Lemma 3.9.** There is a Polish topology on \(X\) for which the action of \(G\) is jointly continuous and which has the hull–kernel Borel sets.

**Proof.** Choose a countable dense rational complex *-subalgebra \(D\subset A\). Every ideal \(J\) determines the C*-seminorm \(p_J(a)=\|a+J\|\). Conversely, a C*-seminorm bounded by the norm of \(A\) extends from \(D\) to \(A\), and equals its quotient norm: the induced injective homomorphism from the C*-quotient into the seminorm completion is isometric. The set of these seminorms is a closed subset of the compact metrizable product \(\prod_{a\in D}[0,\|a\|]\). The closed conditions are the triangle and product inequalities, rational homogeneity, the adjoint identity and the C*-identity. Thus the space of all ideals, with these norm coordinates, is compact metrizable.

A nonzero quotient is prime precisely when
\[
 p(a)p(b)=\sup_{c\in D_1}p(acb)\qquad(a,b\in D),
 \tag{3Q.7}
\]
where \(D_1\) is a countable dense set in the unit ball. For a prime quotient, Lemma 3.8 supplies a faithful irreducible representation. The double commutant and Kaplansky density theorems make its unit ball strongly dense in that of \(B(H)\). A norm-one rank-one operator can send a vector almost attaining \(\|b\|\) to a vector almost attaining \(\|a\|\), proving the reverse inequality in (3Q.7); the forward inequality is submultiplicativity. Quotient contractions can be lifted with norm at most \(1+\varepsilon\), then scaled and approximated in \(D_1\), so the supremum has the asserted domain. Conversely, if two nonzero quotient ideals have zero product, take nonzero elements from them. The right side is zero and the left side is positive. Approximation by \(D\) preserves the identity, so (3Q.7) cannot hold for all its pairs.

For each \(a,b\) and positive integer \(m\), the condition that some \(c\in D_1\) satisfies \(p(acb)>p(a)p(b)-1/m\) is open. Excluding the zero quotient is also an open condition. Hence the prime ideals, which are the primitive ideals by Lemma 3.8, form a \(G_\delta\) subset of a compact metric space. Such a subset admits a complete compatible metric: if it is \(\bigcap_n O_n\), add to a bounded ambient metric the terms \(2^{-n}\min\{1,|1/d(x,O_n^c)-1/d(y,O_n^c)|\}\), omitting terms with empty complement. A Cauchy sequence has an ambient limit and bounded reciprocal distances, so that limit belongs to every \(O_n\). This gives the Polish topology.

The action is continuous in these coordinates, since \(p_{sJ}(a)=p_J(\alpha_{s^{-1}}a)\), and the action on each fixed \(a\) is norm continuous. The coordinate functions are Borel for the hull–kernel topology: \(p_P(a)>t\) is \(U_{\langle(a^*a-t^2)_+\rangle}\). Conversely the countable ideals \(J_n\) in Lemma 3.8 generate every ideal, so their sets \(U_{J_n}\) generate all hull–kernel opens and are open in the norm-coordinate topology. The Borel structures therefore coincide. \(\square\)

For the norm-controlled density used in (3Q.7), the exact written provider is [Kaplansky's density theorem and its consequences](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences.html#OA-FND-KD-07), Theorem 7.1(1), with the double commutant theorem stated and proved in its preceding prerequisite. No transitivity theorem is being assumed beyond this density result.

### Decomposing the ideal centre

Let \((\pi,U)\) be a nondegenerate covariant representation on a separable Hilbert space \(H\). For an ideal \(J\), let \(e_J\) be the projection onto \(\overline{\pi(J)H}\). This projection commutes with \(\pi(A)\), because \(J\) is an ideal, and with its commutant, because that commutant preserves \(\pi(J)H\). Thus \(e_J\) is central in \(\pi(A)''\). The **ideal centre** is the abelian von Neumann algebra
\[
 \mathcal D=\{e_{J_n}:n\ge1\}'',
 \qquad U_s e_JU_s^*=e_{\alpha_s(J)}.
 \tag{3Q.8}
\]
Every \(J\) is generated by the \(J_n\)'s it contains, so \(e_J\) is their supremum. Equation (3Q.8) therefore says that \(U\) normalizes \(\mathcal D\).

Here is a direct construction of the decomposition we need. The commutative separable unital algebra \(C^*(1,e_{J_n})\) has a compact metrizable character space \(\Omega\). Decompose \(H\) into countably many orthogonal cyclic subspaces for this algebra, with scalar spectral measures \(\mu_j\). Take a finite positive combination \(\mu\) dominating all these measures. Radon–Nikodym densities \(\rho_j=d\mu_j/d\mu\) identify the \(j\)-th cyclic subspace with \(L^2(\{\rho_j>0\},\mu)\), by \(f\mapsto\sqrt{\rho_j}f\). Consequently
\[
 H=\int_\Omega^\oplus H_x\,d\mu(x),
 \quad H_x=\ell^2\{j:\rho_j(x)>0\},
 \quad\mathcal D=L^\infty(\Omega,\mu).
 \tag{3Q.9}
\]
The measure can be normalized to a probability. Multipliers by indicators are obtained by bounded measurable approximation to continuous functions, and simple functions are dense in \(L^2\), proving the last equality.

Every operator commuting with these multipliers is decomposable. One may see this explicitly by using the measurable coordinate vectors of \(H_x\): matrix coefficients of an operator applied to indicator times a coordinate vector are Radon–Nikodym densities; commutation with indicators makes them agree on restrictions. The operator bound holds on every finite rational coordinate vector outside one countable union of null sets, and hence on each fibre by density. This constructs a measurable field of bounded operators of the same norm bound. Applying it to the countable algebra \(D\), discard one null set for all its algebraic identities and then extend by continuity. We obtain representations \(\pi_x:A\to B(H_x)\) and \(\pi=\int^\oplus\pi_x\).

An increasing sequential approximate identity of \(A\) converges strongly to one on almost every fibre: its fibre limits are projections, and the global strong limit is one, as is checked on the countable coordinate vectors. The same argument for each \(J_n\) shows that
\[
 \overline{\pi_x(J_n)H_x}=
 \begin{cases}H_x,&e_{J_n}(x)=1,\\0,&e_{J_n}(x)=0.
 \end{cases}
 \tag{3Q.10}
\]
There is one conull set on which these statements hold for all \(n\). Since every ideal is generated by members of this list, its fibre representation is either zero or nondegenerate. Thus \(\pi_x\) is **homogeneous**: every nonzero reducing subspace has the same kernel. Its kernel \(P_x\) is prime, since two ideals represented nondegenerately cannot have zero product; Lemma 3.8 makes it primitive.

The map \(x\mapsto P_x\) is Borel for the topology of Lemma 3.9: \(\|a+P_x\|=\|\pi_x(a)\|\) is measurable by taking a supremum over finite rational coordinate vectors. It is injective, because the bits \(e_{J_n}(x)\) distinguish characters of \(C^*(1,e_{J_n})\), and (3Q.10) recovers those bits from \(P_x\). More explicitly, the inverse is the Borel bit code \(P\mapsto(1_{U_{J_n}}(P))_n\); the character space is a closed subset of the space of bit sequences. We may therefore push \(\mu\) forward to \(X\), and write
\[
 \begin{aligned}
 H&=\int_X^\oplus H_P\,d\mu(P),\qquad
 \pi=\int_X^\oplus\pi_P\,d\mu(P),\\
 \ker\pi_P&=P\quad\text{almost everywhere}.
 \end{aligned}
 \tag{3Q.11}
\]
All multipliers in \(\mathcal D\) are measurable scalar functions of \(P\), since their sigma-algebra is generated by these bits. Covariance on the support projections, followed by bounded measurable approximation, gives
\[
 U_sM_hU_s^*=M_{h\circ s^{-1}}.
 \tag{3Q.12}
\]
It also proves that \(\mu\) is quasi-invariant: a multiplier is zero precisely when its support has measure zero, and unitary conjugation preserves that property. We will use (3Q.12) directly; no choice of pointwise fibre unitaries is necessary.

The scalar measure providers are the written programme chapters [Haar measure on locally compact groups](https://kokunoyumeto.github.io/open-math-courses-public/courses/harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups.html#OA-FND-HM-01), Theorem 2.2, for a positive functional on the compact character space, and [Measure and Hilbert space tools for Haar integration](https://kokunoyumeto.github.io/open-math-courses-public/courses/harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools.html#4-densities-and-bounded-functionals), Theorem 4.1, for finite dominated scalar measures. Both full proofs apply at exactly these conditions. The additional content of (3Q.8)–(3Q.12), including homogeneity and the primitive kernels, has been proved above rather than assumed as an ideal-centre decomposition theorem.

### A Schur estimate for measurable coefficients

Put \(R=\pi\rtimes U\). For a bounded Borel function \(b:G\times X\to A\), supported in a compact subset of the group variable, let \(T_b(s)\) have fibre \(\pi_P(b(s,P))\), and set
\[
 R'(b)=\int_GT_b(s)U_s\,ds.
 \tag{3Q.13}
\]
This is a strong operator integral: bounded Borel matrix coefficients on the separable Hilbert space give strong measurability, and the compact group support gives integrability. For ordinary \(f\in C_c(G,A)\), it is \(R(f)\).

Write \(a(s,P)=\|b(s,P)+P\|\). Covariance on \(\pi(A)\) and on scalar multipliers gives
\[
 \|R'(b)\|^2\le
 \left(\mathop{\mathrm{ess\,sup}}_P\int_Ga(s,P)\,ds\right)
 \left(\mathop{\mathrm{ess\,sup}}_P\int_Ga(s,sP)\,ds\right).
 \tag{3Q.14}
\]
To prove it, the fibre operator \(T_b(s)\) is bounded in absolute value by the scalar multiplier \(M_{a(s,\cdot)}\). Therefore
\[
 |\langle T_b(s)U_sh,k\rangle|
 \le\|M_{\sqrt{a(s,\cdot)}}U_sh\|
       \|M_{\sqrt{a(s,\cdot)}}k\|.
\]
Apply Cauchy–Schwarz in \(s\). The second squared integral is bounded by the first factor in (3Q.14) times \(\|k\|^2\). Conjugate the multiplier by \(U_s\), using (3Q.12), to bound the other integral by the second factor times \(\|h\|^2\). This proves the estimate without any fibre-unitary or Radon–Nikodym cocycle choices.

For these measurable coefficients the product and adjoint formulas are
\[
 \begin{aligned}
 (b*c)(t,P)&=\int_Gb(s,P)\alpha_s(c(s^{-1}t,s^{-1}P))\,ds,\\
 b^*(s,P)&=\Delta(s)^{-1}\alpha_s(b(s^{-1},s^{-1}P)^*).
 \end{aligned}
 \tag{3Q.15}
\]
They follow first for functions with finitely many Borel pieces in \(P\) and elementary continuous coefficients in \(s\), from (3Q.12) and covariance. Bounded pointwise approximation, strong dominated convergence and Fubini extend them to bounded Borel coefficients of compact group support. Haar inversion shows that the second factor in (3Q.14) is the first factor for \(b^*\). We may also use the norm of \(b(s,P)\) in \(A\), a larger bound, in both factors.

### Local orbit normalization

We use right Haar measure \(d_Rt\), the image of left Haar measure under inversion. Because the action on \(X\) is free, the map \(t\mapsto tP\) is injective. Right Haar measure gives orbit measures
\[
 \beta_P(B)=\int_G1_B(tP)\,d_Rt,
 \qquad \beta_{sP}=\beta_P.
 \tag{3Q.16}
\]
These measures need not be finite. We only integrate over fixed compact sets in the construction below.

**A support fact.** Let \(L\subset X\) be compact for the Polish topology, and let \(K\) be a compact symmetric identity neighbourhood. For almost every \(P\in L\), every relative neighbourhood \(L\cap V\) of \(P\) satisfies
\[
 \int_K1_{L\cap V}(tP)\,d_Rt>0.
 \tag{3Q.17}
\]
It suffices to check a countable base of \(V\)'s. For one such \(V\), let \(E\) be the Borel set of points of \(L\cap V\) where the integral vanishes. Fix \(Q\in X\), and put \(T=\{t:tQ\in L\cap V\}\). If \(tQ\in E\), the right Haar measure of \(T\cap Kt\) is zero, by right invariance. Since \(Kt\) is a neighbourhood of \(t\), this point lies outside the support of right Haar measure restricted to \(T\). A countable base of \(G\) shows that such points form a Haar-null subset of \(T\): their zero-measure neighbourhoods have a countable subcover. Thus \(\beta_Q(E)=0\) for every \(Q\). Integrating over \(\mu\) and using Tonelli gives \(\int_G\mu(t^{-1}E)\,d_Rt=0\). Quasi-invariance would make every integrand positive if \(\mu(E)>0\), a contradiction. Hence \(\mu(E)=0\), proving (3Q.17).

Fix a compact symmetric identity neighbourhood \(K\). Choose a symmetric open identity neighbourhood \(N\) with \(N^2\subset K\). Freeness and compactness of \(K\setminus N\) give, for every \(P_0\), an open neighbourhood \(V\) such that
\[
 P,Q\in V,\quad Q=tP,\quad t\in K
       \quad\Longrightarrow\quad t\in N.
 \tag{3Q.18}
\]
Otherwise choose \(P_j,Q_j\to P_0\) and \(t_j\in K\setminus N\) with \(Q_j=t_jP_j\); a convergent subsequence of \(t_j\) would give a nonidentity stabilizer of \(P_0\). The relation \(Q=tP\), \(t\in K\), restricted to \(V\), is consequently transitive: two such elements lie in \(N\), and their product lies in \(K\). It is reflexive and symmetric as well.

Cover \(L\) by finitely many such \(V_i\), and choose a nonnegative continuous partition \(\psi_i\) of one on \(L\), with \(\psi_i(P)>0\) only in \(V_i\). Extend each function by zero off \(L\). Set
\[
 \phi_i(P)=\int_K\psi_i(tP)\,d_Rt,
 \qquad
 e_i(P)=\begin{cases}
       \psi_i(P)/\sqrt{\phi_i(P)},&\phi_i(P)>0,\\
       0,&\phi_i(P)=0.
       \end{cases}
 \tag{3Q.19}
\]
These are Borel functions. Whenever \(P,Q\in V_i\) are \(K\)-related, \(\phi_i(P)=\phi_i(Q)\). To check this, write \(Q=rP\). If \(u\in K\) and \(\psi_i(uQ)>0\), then \(u,r\in N\), so \(ur\in K\). Conversely, if \(t\in K\) and \(\psi_i(tP)>0\), then \(tr^{-1}\in K\). Right translation therefore matches the two integration domains without changing Haar measure or the value of \(\psi_i\).

On the conull subset \(L'\) furnished by (3Q.17), \(\psi_i(P)>0\) implies \(\phi_i(P)>0\). The preceding constancy now gives
\[
 \begin{aligned}
 \sum_i e_i(P)\int_K e_i(tP)\,d_Rt&=1
       &&(P\in L'),\\
 \sum_i e_i(P)\int_K e_i(tP)\,d_Rt&\le1
       &&(P\in X).
 \end{aligned}
 \tag{3Q.20}
\]
Indeed each nonzero summand equals \(\psi_i(P)\); the others are zero. The same upper bound holds if every \(e_i\) is replaced by \(\min\{e_i,m\}\). This observation handles any unbounded normalizing functions.

### Free action gives the regular kernel comparison

For \(f\in C_c(G,A)\), take \(K\) containing its support and inverse support. With the preceding normalizers put
\[
 Qf(s,P)=\sum_i e_i(P)f(s)e_i(s^{-1}P),
 \qquad C_f=\max\{\|f\|_\infty,\|f^*\|_\infty\}.
 \tag{3Q.21}
\]
Haar inversion and (3Q.20) bound the row integral of its coefficient norms by \(\|f\|_\infty\). Its adjoint is \(Q(f^*)\), so the other integral is bounded by \(\|f^*\|_\infty\). The Schur estimate yields a bound \(C_f\), independent of \(L\), its cover and the truncation level. For the truncated normalizers it gives the genuine finite compression
\[
 R'(Q_mf)=\sum_i M_{e_i\wedge m}R(f)M_{e_i\wedge m},
 \qquad \|R'(Q_mf)\|\le C_f.
 \tag{3Q.22}
\]
As \(m\to\infty\), the scalar weights increase. Their product with \(\|U_sh(P)\|\|k(P)\|\), interpreted through (3Q.14), is integrable by the same Cauchy–Schwarz bound. Equivalently one can apply the two multiplier bounds used to prove (3Q.14). Thus the matrix coefficients converge, defining a bounded weak limit \(R'(Qf)\). The convolution formulas continue to hold after multiplication by an ordinary \(R(g)\): the coefficient \(Qf*g\) is uniformly bounded, because (3Q.20) bounds its integral weights, and its truncated coefficients converge pointwise. Strong dominated convergence on the compact group support gives the required product limit.

We claim that finite compressions of \(R(f)\), with suitable choices of \(L,V_i\) and large \(m\), converge weakly to \(\pi(f(e))\). Here is the approximation argument. For \(g\in C_c(G,A)\), substitute \(t=s^{-1}\) in the convolution integral to get
\[
 (Qf*g)(s,P)=\sum_i e_i(P)
   \int_K e_i(tP)\,f(t^{-1})\alpha_{t^{-1}}(g(ts))\,d_Rt.
 \tag{3Q.23}
\]
Continuity on compact supports makes
\(f(t^{-1})\alpha_{t^{-1}}(g(ts))\) uniformly close to \(f(e)g(s)\), for all \(s\), when \(t\) lies in a sufficiently small identity neighbourhood \(N\). Choose this \(N\) also with \(N^2\subset K\), and then choose the cover using (3Q.18). A nonzero integrand in (3Q.23), with \(e_i(P)>0\), has both \(P,tP\in V_i\), hence \(t\in N\). Equation (3Q.20) shows that the coefficient differs from \(f(e)g(s)\) by at most the chosen uniform error for \(P\in L'\).

The measure \(\mu\) is tight. For completeness, in a complete separable metric space cover by balls of radius \(2^{-n}\), and retain finitely many whose union has measure greater than \(1-\delta2^{-n}\). Intersect the corresponding finite unions of closed balls over \(n\). Its closure is complete and totally bounded, hence compact, and its measure is at least \(1-\delta\). This proves the needed compact approximation. We may therefore choose \(L\) so that \(\|1_{X\setminus L}k\|\) is as small as desired for any finite list of test vectors \(k\), using absolute continuity of their squared norms.

On \(L'\), the uniform coefficient error, integrated over the fixed compact support in \(s\), bounds
\(\langle R'(Qf*g)h-\pi(f(e))R(g)h,1_{L'}k\rangle\)
by that error times its Haar volume and \(\|h\|\|k\|\). On the complement, the operator bounds \(C_f\|g\|_1\) and \(\|f(e)\|\|g\|_1\) multiply \(\|h\|\|1_{X\setminus L}k\|\). Both errors can be made arbitrarily small. Truncation then makes the same true of (3Q.22). Finite sums of \(R(g)h\) are dense, since \(R\) is nondegenerate; the uniform bound extends the approximation to arbitrary finite lists of vectors. We have proved the claimed weak approximation, with no compactness or Hausdorff assumption on the original hull–kernel space.

Let \(\operatorname{Reg}\pi\) be the regular representation from Lesson 2. We prove
\[
 \ker R\subseteq\ker\operatorname{Reg}\pi.
 \tag{3Q.24}
\]
In its Hilbert-module model, the dense vectors \(g\otimes h\) have coefficient formula
\[
 \langle\operatorname{Reg}\pi(F)(g_1\otimes h),g_2\otimes k\rangle
 =\langle\pi((g_2^* * F * g_1)(e))h,k\rangle.
 \tag{3Q.25}
\]
Here \(F,g_1,g_2\in C_c(G,A)\). Apply the weak approximation to \(f=g_2^* * F * g_1\). Each approximating coefficient is
\[
 \sum_i\langle R(F)R(g_1)M_{e_i\wedge m}h,
                       R(g_2)M_{e_i\wedge m}k\rangle.
 \tag{3Q.26}
\]
Choose \(K\) also to contain the supports of \(g_j^* * g_j\) and their inverses. The sum of the squared norms of the first vector family is at most \(C_{g_1^* * g_1}\|h\|^2\), by (3Q.22) applied to that function; likewise for the second family. These constants depend only on \(g_1,g_2\).

If \(R(a)=0\), approximate \(a\in A\rtimes G\) by \(F\in C_c(G,A)\). Cauchy–Schwarz in (3Q.26) bounds its absolute value by
\(\|F-a\|\sqrt{C_{g_1^* * g_1}C_{g_2^* * g_2}}\|h\|\|k\|\).
Take the weak limit, then let \(F\to a\). Regular representations are contractive for the full norm, so (3Q.25) vanishes with \(F\) replaced by \(a\). Density of the module vectors proves (3Q.24). This is the local-normalization part of the primitive-space theorem; it used freeness, not amenability.

### From the kernel comparison to all ideals

We now use amenability. Write \(B=A\rtimes G\). The full ideal exact sequence from Lesson 1 and the full-to-reduced norm equality proved in [Amenability of groups and crossed products](KT-CP-04.md), section *Compression proves the norm equality*, give
\[
 \ker\operatorname{Reg}\pi=I\rtimes G,
 \qquad I=\ker\pi,
 \qquad \ker\operatorname{Reg}\pi\subseteq\ker R.
 \tag{3Q.27}
\]
Indeed \(I\) is invariant by covariance; \(\pi\) is faithful on \(A/I\), so its regular representation is faithful on the reduced crossed product of that quotient. Amenability makes this quotient's full norm its reduced norm. The covariant pair \((\pi,U)\) factors through it, which proves the second inclusion. Combined with (3Q.24), this proves
\[
 \ker(\pi\rtimes U)=(\ker\pi)\rtimes G
 \tag{3Q.28}
\]
for every covariant pair on a separable Hilbert space.

The algebra \(B\) is separable: second countability of \(G\), compactly supported scalar approximation and a countable dense set in \(A\) give an \(L^1\)-dense countable set in \(C_c(G,A)\), hence a full-norm dense set. Every quotient \(B/J\) consequently has a faithful nondegenerate representation on a separable Hilbert space, by taking a countable sum of state representations detecting a dense set of positive elements. Apply (3Q.28) to that representation composed with the quotient map. Its coefficient kernel is exactly \(I(J)\) in (3Q.5), since a multiplier vanishes in a faithful quotient representation precisely when its products with \(B/J\) vanish. We obtain \(J=I(J)\rtimes G\).

Conversely, the canonical coefficient representation of \(A/I\) in the multiplier algebra of \((A/I)\rtimes G\) is faithful, as is seen in its regular model. The full exact sequence therefore gives \(I(I\rtimes G)=I\). Both maps preserve inclusion. This proves the order isomorphism (3Q.3). No list of primitive representations or factor decompositions has been assumed to get it.

### Which extended ideals are primitive?

For closed ideals, the closed linear span of their product is their intersection: an approximate identity of one ideal approximates every element of the intersection. Hence primality can be expressed using the order and binary meets of the ideal lattice. The order isomorphism (3Q.3) shows that \(I\rtimes G\) is prime exactly when \(I\) is \(G\)-prime. Since \(B\) is separable, Lemma 3.8 with the trivial group says that a prime quotient of \(B\) has a faithful irreducible representation. Thus its prime ideals are primitive.

Every orbit core \(I_P\) is \(G\)-prime. If invariant ideals \(J_1,J_2\) are not contained in \(I_P\), neither is contained in \(P\): for an invariant \(J\), containment in \(P\) is equivalent to containment in every translate of \(P\). Primality of \(P\) implies \(J_1J_2\not\subseteq P\), hence \(J_1J_2\not\subseteq I_P\). It follows that \(I_P\rtimes G\) is primitive.

Conversely, let \(K\) be a primitive ideal of \(B\), and contract it to \(I\). The quotient \(A/I\) is \(G\)-prime. Apply the group version of Lemma 3.8 in that quotient to find a primitive ideal with zero orbit core. Lifting its irreducible representation to \(A\) gives \(P\in X\) with \(I_P=I\). Then \(K=I_P\rtimes G\). Equality of two such ideals is equivalent, by contraction, to equality of their orbit cores. This proves the bijection in (3Q.4).

Finally the bijection respects precisely the quotient topology. For an invariant ideal \(J\), the inverse image in \(X\) of the primitive-space open set determined by \(J\rtimes G\) is
\[
 \{P:J\rtimes G\not\subseteq I_P\rtimes G\}
 =\{P:J\not\subseteq I_P\}=U_J.
 \tag{3Q.29}
\]
This proves continuity. Every open set pulled back from the quasi-orbit quotient is invariant, so it is \(U_J\) for an invariant \(J\): the open-set/ideal correspondence (3Q.1) is injective, and translating an open set translates its ideal. Conversely such a \(U_J\) is saturated under equal orbit closures, because its membership is determined by \(I_P\). Equation (3Q.29) sends all these opens to the corresponding opens of \(\operatorname{Prim}(B)\). The bijection is therefore open as well as continuous, proving the homeomorphism and completing Theorem 3.7. \(\square\)

The quasi-orbit conclusion is part of Green's primitive-ideal theory and the Gootman–Rosenberg theorem. The local normalization (3Q.17)–(3Q.26) follows the mechanism of the proof of Step V in Williams's author draft, pp.298–309, with all stabilizers trivial. The prime-ideal construction, the measurable primitive-space model, the ideal-centre decomposition, the two norm comparisons and the topology argument above supply the specialized proof used in this lesson.

## Exercises

**Exercise 1 (basic).** Let \(x\in A\rtimes_r\Gamma\). Prove that \(E(x^*x)=0\) implies \(x=0\), including nonunital \(A\) and uncountable \(\Gamma\). For a polynomial, calculate its transported sum of squares.

**Solution.** Represent \(A\) faithfully and nondegenerately on \(H\). Equation (7) gives
\(\|xV_t v\|^2=\langle v,\rho(\alpha_{t^{-1}}E(x^*x))v\rangle=0\).
Hence every column of \(x\) vanishes on \(H\). The finite-coordinate vectors span a dense subspace of the Hilbert direct sum, so \(x=0\). This does not require a unit vector \(\delta_e\) with coefficient \(1_A\). In multiplying \(p^*p\), a term with indices \(g,h\) contributes at the identity exactly when \(h=g\). Its coefficient is \(\alpha_{g^{-1}}(a_g^*a_g)\). Adding these gives (8).

**Exercise 2 (intermediate).** For a topologically free homeomorphism \(T\) of compact \(X\), carry out the compression for a polynomial supported at powers \(-N,\ldots,N\), and deduce that a representation of \(C(X)\rtimes_r\mathbb Z\) faithful on \(C(X)\) is faithful everywhere.

**Solution.** Given positive \(b\) and a polynomial \(p\) with \(\|b-p\|<\varepsilon\), choose \(x_0\) where \(E(b)\) is within \(\varepsilon\) of its maximum and outside the fixed-point sets of \(T^n\), \(0<|n|\le N\). This is possible because those finitely many sets are closed with empty interior. Choose \(U\) with \(U\cap T^nU=\varnothing\) for those powers, and a positive contraction \(h\) supported in \(U\), equal to one at \(x_0\). Then \(h a_nu^n h=a_n h(h\circ T^{-n})u^n=0\) for \(n\ne0\). Thus \(hph=hE(p)h\), giving (14).

Let \(\pi\) be the representation. If \(b\ge0\) belongs to its kernel, isometry of \(\pi\) on \(C(X)\) gives
\(\|E(b)\|-\varepsilon<\|\pi(hE(b)h)\|<2\varepsilon\).
Therefore \(E(b)=0\) and \(b=0\). For arbitrary \(y\in\ker\pi\), apply this to \(y^*y\). This proves faithfulness.

**Exercise 3 (intermediate).** Prove that the full rotation algebra for rational angle \(p/q\) is not simple. Exhibit a proper nonzero kernel rather than only a failed simplicity hypothesis.

**Solution.** Choose an orbit \(O\) of \(R_{p/q}\). Restriction \(C(\mathbb T)\to C(O)\) is equivariant and surjective, so full quotient functoriality gives a surjection onto \(C(O)\rtimes\mathbb Z\). The latter is nonzero because its coefficient copy is faithful. A nonzero continuous function vanishing on the finite set \(O\) belongs to the kernel, since the coefficient embedding in the source is faithful. The kernel is proper because the quotient is nonzero. It is therefore a proper nonzero ideal. The same construction with reduced functoriality proves the reduced statement (18).

**Exercise 4 (advanced).** For a free homeomorphism \(T\) of compact Hausdorff \(X\), prove that restriction gives a bijection between tracial states of \(C(X)\rtimes\mathbb Z\) and invariant probability measures. Explain why full/reduced equality is unnecessary for this trace assertion.

**Solution.** Restriction of a trace is a probability measure by Riesz representation, and conjugation by \(u\) makes it \(T\)-invariant. For any nonzero integer \(n\), freeness says \(T^n x\ne x\) at every point. Cover \(X\) by finitely many neighborhoods disjoint from their \(T^n\)-translates. Take \(h_i\) subordinate to them with \(\sum h_i^2=1\). The trace of \(f u^n\) is
\(\sum_i T(h_i f u^n h_i)=0\), since every compressed term vanishes. Hence its values are exactly the integration of the identity coefficient.

Conversely, an invariant measure gives an invariant coefficient state, and Proposition 3.2, composed with the full-to-reduced quotient, gives a trace on the full algebra. Its restriction is the given measure. Density of finite sums proves uniqueness. All the vanishing computations hold in the universal algebra itself. Its expectation may be nonfaithful; neither faithfulness nor equality of the two completions was used.

**Exercise 5 (advanced).** Let \(G=\mathbb Z/3\) act on six points by two disjoint three-cycles, and on \(A=\bigoplus_{p=1}^6M_2(\mathbb C)\) by permuting its summands. Determine the invariant ideals, quasi-orbits and crossed product. In the covariant representation on \(\bigoplus_p\mathbb C^2\), show directly how scalar compression recovers \(f(e)\).

**Solution.** The primitive ideals correspond to the six summands. Their orbits are the two three-point sets, so there are two quasi-orbits and four invariant ideals, obtained by choosing either orbit, both or neither. On one orbit the diagonal coefficient matrices and the cyclic permutation generate all \(3\times3\) matrix units tensored with \(M_2\): a coefficient supported at one point, multiplied by the appropriate permutation, has a prescribed row and column. Thus the crossed product is \(M_6\oplus M_6\). The full and reduced norms agree because the group is finite. If \(E_p\) is the scalar projection onto the \(p\)-th coefficient fibre, then \(\sum_p E_pR(f)E_p=\pi(f(e))\): every nonidentity permutation moves each fibre and has zero diagonal compression. This is the finite version of (3Q.21)–(3Q.22). Restricting the covariant representation to one orbit kills exactly the extended coefficient ideal supported on the other orbit.

**Exercise 6 (intermediate).** Explain why contraction in (3Q.5) uses multipliers for a nondiscrete group. Then show why freeness cannot be omitted from the kernel comparison by considering the trivial action of \(\mathbb Z/2\) on \(\mathbb C\).

**Solution.** For the trivial action of \(\mathbb R\) on \(\mathbb C\), the coefficient unit is the identity multiplier of \(C^*(\mathbb R)\cong C_0(\widehat{\mathbb R})\). It does not belong to this nonunital algebra. The multiplier definition measures whether all its products vanish in the quotient and remains meaningful. In the second example let \(u\) be the generator of \(\mathbb Z/2\). Its trivial covariant representation has faithful scalar coefficients but kills \(1-u\). The regular representation of the same coefficient representation sends \(u\) to the flip on \(\mathbb C^2\), so \(1-u\) has norm two. Hence \(\ker R\subseteq\ker\operatorname{Reg}\pi\) fails. The nonidentity element fixes the sole primitive ideal, exactly where the freeness hypothesis fails.

## Proofs and prerequisites

We import the faithful regular realization, coefficient embedding, canonical multiplier action and quotient functoriality from the preceding two lessons. The matrix, expectation, trace, intersection and simplicity assertions above are proved here. We use the usual foundational facts about positivity in faithful C*-representations, closed ideals of \(C_0(X)\), approximate identities, Riesz representation, finite partitions of unity and density of trigonometric polynomials.

Theorem 3.7 proves the general free primitive-space ideal and quasi-orbit theorem for a separable C*-algebra and a second countable locally compact amenable group. The prime and orbit-core construction, Polish measurable model, ideal-centre decomposition, local support normalization, Schur estimate, regular-kernel comparison and final topology argument are all included. The exact written foundational providers for GNS, Kaplansky density, scalar Riesz representation and Radon–Nikodym are linked at their points of use. The amenable norm comparison is the compression proof in Lesson 4, which uses Lesson 2 absorption and can be read before this structural section. Compare [Blackadar 2006], [Williams 2006] and [Gootman–Rosenberg 1979].

Equality of full and reduced crossed products for \(\mathbb Z\) and finite groups is proved in the next lesson. It then transfers our reduced simplicity results to the usual unambiguous rotation and odometer crossed products. The trace theorem above already applies to both completions separately. We do not prove the classification or K-theory of Bunce–Deddens algebras here.

## References

- **[Williams 2006]** Dana P. Williams, *Crossed Products of C*-Algebras*, author's draft version 3.1, 6 September 2006. [Author's accessible draft](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf). Relevant passages: §8.2, pp.239–242, and Chapter 9, Step V, pp.298–309.
- **[Gootman–Rosenberg 1979]** Elliot C. Gootman and Jonathan Rosenberg, *The structure of crossed product C*-algebras: a proof of the generalized Effros–Hahn conjecture*, Inventiones Mathematicae 52 (1979), 283–298. [Original article](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0052/LOG_0020.pdf). The free-action case is proved in this lesson.
- **[Archbold–Spielberg 1994]** R. J. Archbold and J. S. Spielberg, *Topologically free actions and ideals in discrete C*-dynamical systems*, Proceedings of the Edinburgh Mathematical Society 37 (1994), 119–124, Theorem 1 and its corollary. [Original article](https://doi.org/10.1017/S0013091500018733).
- **[Exel 2017]** Ruy Exel, *Partial Dynamical Systems, Fell Bundles and Applications*, Mathematical Surveys and Monographs 224, American Mathematical Society, 2017. Chapter 29, especially Theorem 29.5 and Corollary 29.8; the global-action case is the setting here. [Author manuscript, 2017 revision](https://arxiv.org/abs/1511.04565v2).
- **[Blackadar 2006]** Bruce Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006, II.10.4.12 and II.10.6.1–3. [Author's revised edition, 2017](https://bruceblackadar.com/Mathematics/Cycr.pdf).
- **[Blackadar 1998]** Bruce Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, 10.10.1 and Exercise 10.11.6. [Author's second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- **[Emerson 2024]** Heath Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §4.6, for comparison with proper actions and their stabilizers.
