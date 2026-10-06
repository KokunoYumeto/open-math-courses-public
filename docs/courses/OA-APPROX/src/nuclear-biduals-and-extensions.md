# Nuclear biduals and extensions

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

A C*-algebra is nuclear precisely when its universal enveloping von Neumann algebra is injective. This connects norm approximation in the original algebra to approximation tested by normal functionals in its bidual. It also gives a short proof that an extension is nuclear precisely when its ideal and quotient are nuclear.

Prerequisites are [Tensor positivity and nuclearity](tensor-positivity-nuclearity.md), [Finite models of a von Neumann algebra](semidiscrete-finite-models.md), and [Averaging, crossed products, and injectivity](averaging-crossed-products-injectivity.md). We use the GNS dominated-functional complete order isomorphism from [Completely positive maps](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/completely-positive-maps.html), Theorem 7.3. Its precise order bounds and the nonunital cyclic construction are explained below.

The bidual input is the following theorem from the foundations of modular theory: every C*-algebra \(A\) has a canonical von Neumann algebra \(A^{**}\), with predual \(A^*\), and a faithful normal realization by the direct sum of all state GNS representations. The embedded \(A\) is ultraweakly dense. A nondegenerate representation \(\pi\) extends to a normal surjection \(A^{**}\to\pi(A)''\), whose restriction to a central summand is a normal isomorphism. Second adjoints of *-homomorphisms are normal *-homomorphisms. For an inclusion \(I\hookrightarrow A\), the second adjoint identifies \(I^{**}\) with the ultraweak closure of \(I\) in \(A^{**}\). These exact inputs are proved in *Every bounded functional becomes normal in one representation*, UB-03–09. We also use central supports of projections and induced representations.

All algebras may be nonunital, and all Hilbert spaces and index sets may be arbitrary. Zero algebras have the unique zero interpretation. Inner products are linear in the second variable. Brown's freely readable notes describe the bidual and extension route; the complete dilation and order methods used here are supported by Arveson's paper, with exact locators below.

## 1. Cyclic representations detect injectivity of the bidual

The commutant of a direct sum of representations can contain operators between different summands. It need not be the product of the separate commutants. Central supports provide the passage we need instead.

**Lemma 1.1.** Suppose that \(\pi_\varphi(A)''\) is injective for every state \(\varphi\) on \(A\). Then \(A^{**}\) is injective.

**Proof.** Put \(M=A^{**}\) in its faithful normal universal representation on \(H\). We first show that every nonzero central projection \(z\in M\) contains a nonzero central projection \(w\) for which \(Mw\) is injective.

Choose a unit vector \(\xi\in zH\), and set
\[
\varphi(a)=\langle\xi,a\xi\rangle,\qquad a\in A.
\]
This is a state even when \(A\) is nonunital: a positive contractive approximate identity of \(A\) converges strongly to \(1\) in this nondegenerate representation, so its values under \(\varphi\) tend to one.

Let \(e\) be the projection onto \(K=\overline{A\xi}\). This subspace reduces \(A\), hence \(M\), so \(e\in M'\). It lies under \(z\). The representation of \(A\) on \(K\), with cyclic vector \(\xi\), is its GNS representation for \(\varphi\). Normal induction gives
\[
M\longrightarrow Me|_K,\qquad x\longmapsto xe|_K,
\qquad \ker=M(1-w),\qquad w=c_{M'}(e).
\]
Here \(w\) is the central support of \(e\) in \(M'\); the centers of \(M\) and \(M'\) agree. For the kernel assertion, \(xe=0\) means that \(x\) vanishes on \(eH\), and, because \(x\) commutes with \(M'\), on \(\overline{M'eH}=wH\). The converse is immediate. Thus \(Mw\) is normally isomorphic to the induced algebra. That induced algebra is \(\pi_\varphi(A)''\): it is the normal image of \(M\), and the ultraweakly dense coefficient algebra induces \(\pi_\varphi(A)\). By hypothesis it is injective. Also \(0\ne w\le z\), since \(0\ne e\le z\).

Now choose a maximal family \((w_j)\) of mutually orthogonal nonzero central projections whose summands are injective. If their sum were smaller than one, the remaining central projection would contain another such \(w\), contradicting maximality. Consequently
\[
M\cong\prod_j Mw_j.
\]
Products of injective algebras are injective, as proved in the averaging lesson. This proves the lemma without a countable decomposition or a faithful normal state on \(M\). \(\square\)

By the commutant theorem, the lemma's hypothesis can equivalently ask that every \(\pi_\varphi(A)'\) be injective.

## 2. A nuclear algebra gives a GNS commutant retraction

Fix a state \(\varphi\), its nondegenerate GNS representation \((\pi,H,\xi)\), and \(C=\pi(A)'\). The GNS dominated-functional theorem gives the complete order isomorphism
\[
R_\varphi:C\longrightarrow D_\varphi\subset A^*,\qquad
R_\varphi(c)(a)=\langle\xi,\pi(a)c\xi\rangle,
\]
where \(D_\varphi\) is the linear span of positive functionals dominated by scalar multiples of \(\varphi\). It sends \(1\) to \(\varphi\), and
\[
0\le f\le r\varphi
\quad\Longrightarrow\quad
0\le R_\varphi^{-1}(f)\le r1.
\]
The inverse need not be bounded for the ambient norm of \(A^*\). The displayed order bound will supply exactly the boundedness required here.

The full order proof is the cyclic construction in Section 2 of [Tensor positivity and nuclearity](tensor-positivity-nuclearity.md#2-keep-a-marginal-exactly-fixed), now applied to \(\pi(A)\xi\). Namely, for \(0\le f\le r\varphi\), define
\[
\langle\pi(a)\xi,z_f\pi(b)\xi\rangle=f(a^*b).
\]
Cauchy–Schwarz and domination bound this form by \(r\|\pi(a)\xi\|\|\pi(b)\xi\|\), so it represents a unique \(0\le z_f\le r1\). The form identity with \(a^*cb\), for \(c\in A\), shows that \(z_f\) commutes with \(\pi(A)\), hence belongs to \(C\). If \(A\) is nonunital, use a positive contractive approximate identity \((u_i)\): \(\pi(u_i)\xi\to\xi\) and \(f(u_i a)\to f(a)\) give
\[
R_\varphi(z_f)(a)=\langle\xi,\pi(a)z_f\xi\rangle=f(a).
\]
Commutation identifies all other form coefficients from this functional, proving injectivity. Conversely each \(0\le z\le r1\) gives the dominated positive vector functional \(R_\varphi(z)\le r\varphi\); decomposing an arbitrary element of \(C\) into four positive parts gives exactly the claimed linear range. At matrix level, positive matrices over the two commuting algebras pair positively, as proved in the tensor lesson. For the inverse, positivity of \([f_{ij}]\) gives
\[
\sum_{i,j}\langle\pi(a_i)\xi,z_{ij}\pi(a_j)\xi\rangle
=\sum_{i,j}f_{ij}(a_i^*a_j)\ge0,
\qquad z_{ij}=R_\varphi^{-1}(f_{ij}).
\]
Density of \(\pi(A)\xi\) proves \([z_{ij}]\ge0\). Thus both directions preserve every matrix cone even in the nonunital case, while no ambient inverse norm bound has been introduced.

**Proposition 2.1.** If \(A\) is nuclear, every state GNS commutant \(C=\pi_\varphi(A)'\) is injective.

**Proof.** The commuting actions of \(A\) and \(C\) give a positive functional
\[
\Omega\left(\sum_i a_i\otimes c_i\right)
=\left\langle\xi,\sum_i\pi(a_i)c_i\xi\right\rangle
\]
on \(A\otimes_{\max}C\). Its norm is one: it is at most one by the unit vector bound, and its values at \(u_i\otimes1\), for a positive contractive approximate identity \((u_i)\) of \(A\), tend to one. Nuclearity identifies this tensor product with \(A\otimes_{\min}C\), which embeds faithfully in \(A\otimes_{\min}B(H)\).

Extend \(\Omega\) to a positive functional \(\Psi\) of norm one on the latter algebra. This is the positive Hahn–Banach extension theorem, valid for a nonunital C*-subalgebra as well: unitize the larger algebra, adjoin its unit to the smaller algebra, extend by the norm at that unit, and apply the unital state extension theorem. Restriction to the larger original algebra still has norm one because its restriction to the smaller algebra does. In particular
\[
\Psi(a\otimes1)=\varphi(a).
\]
The positive tensor pairing, with its factors interchanged, gives a completely positive map
\[
\Theta:B(H)\longrightarrow A^*,\qquad
\Theta(b)(a)=\Psi(a\otimes b),\qquad \Theta(1)=\varphi.
\]
The matrix order here is the dual order from the tensor-positivity lesson. For \(b\ge0\), positivity of \(\Psi\) gives
\[
0\le\Theta(b)\le\|b\|\varphi.
\]
Every operator is a linear combination of four positive operators, so \(\Theta(B(H))\subseteq D_\varphi\). We may therefore define
\[
E=R_\varphi^{-1}\Theta:B(H)\longrightarrow C.
\]
Both maps preserve the indicated matrix orders, hence \(E\) is completely positive. It is unital because \(\Theta(1)=\varphi=R_\varphi(1)\). Thus it is contractive; alternatively the domination estimate gives \(0\le E(b)\le\|b\|1\) on positive operators. For \(c\in C\), the original functional is unchanged on \(a\otimes c\), so \(\Theta(c)=R_\varphi(c)\) and \(E(c)=c\). This is a ucp retraction onto \(C\), proving injectivity. \(\square\)

There is no claim that \(R_\varphi^{-1}\) is norm bounded on all of \(D_\varphi\). The composition is bounded because its positive inputs lie in controlled order intervals.

## 3. Nuclearity is injectivity of the universal bidual

**Theorem 3.1.** For any C*-algebra \(A\),
\[
A\text{ is nuclear}
\quad\Longleftrightarrow\quad
A^{**}\text{ is injective}.
\]
**Proof.** If \(A\) is nuclear, Proposition 2.1 makes every state GNS commutant injective. The commutant theorem makes every state GNS von Neumann algebra injective. Lemma 1.1 then gives injectivity of \(A^{**}\).

Conversely suppose \(M=A^{**}\) is injective. The full injective/semidiscrete equivalence gives pointwise norm cpc factorizations of its predual through matrix preduals:
\[
M_*\longrightarrow M_n^*\longrightarrow M_*.
\]
Here \(M_*=A^*\), isometrically and in the dual matrix orders. Norm convergence implies the pointwise weak* convergence used in Corollary 4.2 of the tensor-positivity lesson. That corollary proves that \(A\) is nuclear. The middle Banach norm is the trace norm on \(M_n^*\), not the operator norm on \(M_n\). \(\square\)

**Corollary 3.2.** If \(A\) is nuclear, the von Neumann algebra generated by every nondegenerate representation of \(A\) is injective and semidiscrete. Conversely, this property for the universal representation, or injectivity for every state GNS representation, implies nuclearity.

**Proof.** A nondegenerate represented closure is normally isomorphic to a central summand of \(A^{**}\). Central corners preserve injectivity, and injectivity gives semidiscreteness. The universal representation realizes the whole bidual. The last assertion follows from Lemma 1.1 and Theorem 3.1. \(\square\)

For a degenerate representation, the represented closure is understood on its essential Hilbert space. Taking the bicommutant in an ambient space with a zero representation summand adds an unrelated identity there; the normal extension theorem is applied to the essential space.

**Example 3.3.** For any set \(I\), \(c_0(I)^*=\ell^1(I)\) and \(c_0(I)^{**}=\ell^\infty(I)\). Coordinate truncations through \(\mathbb C^F\), directed by finite subsets \(F\subset I\), approximate the identity of \(c_0(I)\) in norm. On the bidual the same truncations approximate the identity ultraweakly, because every normal functional is an absolutely summable coordinate family. Both algebras therefore have the appropriate finite models, even when \(I\) is uncountable. The maps land in finite commutative algebras, which embed as diagonal matrix algebras with completely positive diagonal retractions.

## 4. An ideal splits the bidual

**Proposition 4.1.** Let \(I\) be a norm-closed two-sided ideal of \(A\), and let \(q:A\to A/I\) be the quotient map. There is a central projection \(p\in A^{**}\) such that
\[
I^{**}\cong pA^{**},\qquad
(A/I)^{**}\cong(1-p)A^{**},\qquad
A^{**}\cong I^{**}\oplus(A/I)^{**}.
\]
All identifications are normal *-isomorphisms; the first extends the inclusion of \(I\), and the second is induced by \(q^{**}\).

**Proof.** Work in the universal representation of \(M=A^{**}\). The ultraweak closure \(J\) of \(I\) is an ideal in \(M\): first multiply approximating elements of \(I\) by a fixed element of \(A\), then use ultraweak density of \(A\) and separate ultraweak continuity of multiplication to allow any fixed element of \(M\).

Choose a positive contractive approximate identity \((u_i)\) of \(I\). It converges strongly to the projection \(p\) onto \(\overline{IH}\). Indeed it tends to the identity on vectors \(a\eta\), \(a\in I\), by norm approximation of \(a\); it vanishes on the orthogonal complement, since that complement is killed by \(I\). Uniform boundedness extends the convergence to all vectors. The subspace \(\overline{IH}\) reduces \(A\), since \(I\) is a two-sided *-ideal, so \(p\in M'\). Also \(p\in M\), as the bounded strong limit of \((u_i)\). Thus \(p\) is central.

Every element of \(I\), and hence of \(J\), satisfies \(x=px\). Conversely \(u_i x\in J\) for \(x\in M\), and \(u_i x\to px\) ultraweakly. Hence \(J=pM\). The second adjoint of the inclusion identifies \(I^{**}\) normally and isometrically with this closure.

On the dual side \(q^*:(A/I)^*\to A^*\) is an isometry with range
\[
I^\perp=\{f\in A^*:f|_I=0\}.
\]
Therefore
\[
\ker q^{**}=(I^\perp)^\perp=J=pM.
\]
The middle equality follows from the weak* bipolar theorem. The map \(q^{**}\) is onto: a bounded functional on \(I^\perp\subset A^*\) extends to \(A^*\) by Hahn–Banach, and that extension is an element of \(A^{**}\) with the required image. It is a normal \*-homomorphism by the bidual theorem. Restricting to \((1-p)M\) gives a bijective normal \*-homomorphism onto \((A/I)^{**}\). Its inverse is normal: an order isomorphism preserves every existing supremum, in particular bounded increasing positive suprema. Combining the two central summands proves the decomposition. \(\square\)

The splitting takes place in \(A^{**}\). It does not assert that \(A\) is a direct sum of its ideal and quotient.

**Theorem 4.2.** For a closed two-sided ideal \(I\subseteq A\),
\[
A\text{ is nuclear}
\quad\Longleftrightarrow\quad
I\text{ and }A/I\text{ are nuclear}.
\]
**Proof.** By Theorem 3.1, nuclearity of \(A\) is injectivity of \(A^{**}\). Proposition 4.1 splits that bidual as \(I^{**}\oplus(A/I)^{**}\). A product is injective exactly when its coordinate algebras are injective. Apply Theorem 3.1 to each coordinate. \(\square\)

**Example 4.3.** Let \(A=C([0,1])\), and \(I=\{f:f(0)=0\}\cong C_0((0,1])\). Evaluation at zero gives \(A/I\cong\mathbb C\). The ideal and quotient are nuclear by the commutative finite-model construction, so the extension theorem gives nuclearity of \(A\). The central projection selecting \(I^{**}\) belongs to \(A^{**}\) and not to \(A\); the next exercise section verifies this directly.

## 5. Exercises with solutions

**Exercise 1.** Let \(A=\mathbb C\), and take the direct sum of two copies of its scalar representation on \(\mathbb C\). Compute the commutant of this sum and compare it with the product of the two separate commutants.

*Solution.* The summed representation is \(\lambda\mapsto\lambda1_2\), whose commutant is all of \(M_2\). The product of the separate commutants is the diagonal algebra \(\mathbb C\oplus\mathbb C\). Off-diagonal matrix units intertwine the identical summands. This is why Lemma 1.1 uses central supports rather than a product assertion about universal commutants.

**Exercise 2.** In Lemma 1.1, verify that \(w=c_{M'}(e)\le z\), although \(e\) need not belong to \(M\).

*Solution.* The projection \(z\) is central in both \(M\) and \(M'\), and \(e\le z\). The central support in \(M'\) is the least central projection of that algebra majorizing \(e\), so it is at most \(z\). Since \(e\ne0\), also \(w\ne0\). Normal induction therefore supplies a nonzero injective central summand inside the prescribed remainder \(zM\).

**Exercise 3.** Suppose a positive map \(\Theta:B\to A^*\) has \(\Theta(1)=\varphi\), where \(B\) is unital and \(\varphi\) is a state. Explain why \(R_\varphi^{-1}\Theta\) is defined on all of \(B\). If \(\Theta\) is completely positive, show that this composition has norm one.

*Solution.* For \(b\ge0\), the inequality \(b\le\|b\|1\) gives \(0\le\Theta(b)\le\|b\|\varphi\), placing \(\Theta(b)\) in \(D_\varphi\). Positive elements span \(B\), so every image belongs to that linear space. The complete order inverse makes the composition completely positive, and its value at the unit is \(R_\varphi^{-1}(\varphi)=1\). A unital completely positive map has norm one. No ambient norm bound for \(R_\varphi^{-1}\) is needed.

**Exercise 4.** For \(A=C([0,1])\) with the integration state \(\varphi(f)=\int_0^1f(t)\,dt\), let \(c_n\) be multiplication by \(1_{[0,1/n]}\) in the GNS commutant. Compute \(\|c_n\|\) and \(\|R_\varphi(c_n)\|\). What does this show about the inverse used in Proposition 2.1?

*Solution.* The multiplication projection has norm one. Its positive functional is \(f\mapsto\int_0^{1/n}f(t)\,dt\), with norm \(1/n\), attained at the unit. Thus \(R_\varphi^{-1}\) is unbounded in the inherited Banach norm of its range. Proposition 2.1 remains valid because the specific composition is completely positive and unital, with the required order bounds.

**Exercise 5.** In Example 3.3, prove ultraweak convergence of finite-coordinate truncations on \(\ell^\infty(I)\). Explain why their convergence on the unit is usually not norm convergence.

*Solution.* For \(x\in\ell^\infty(I)\), \(a\in\ell^1(I)\), and \(P_Fx=1_Fx\),
\[
|\langle a,x-P_Fx\rangle|
\le\|x\|_\infty\sum_{i\notin F}|a_i|\longrightarrow0.
\]
Every absolutely summable family has finite tails as small as desired, giving the directed convergence. If \(I\) is infinite, \(\|1-P_F1\|_\infty=1\) for every finite \(F\). Semidiscrete approximation is tested by normal functionals rather than the operator norm of the unit error.

**Exercise 6.** Verify surjectivity of \(q^{**}\) in Proposition 4.1 directly from \(q^*\), including its norm control.

*Solution.* Identify \((A/I)^*\) isometrically with \(I^\perp\) through \(q^*\). An element \(Y\in(A/I)^{**}\) becomes a bounded functional on \(I^\perp\) of norm \(\|Y\|\). Hahn–Banach extends it to \(X\in(A^*)^*=A^{**}\) with the same norm. The adjoint definition then gives \(q^{**}X=Y\). Multiplying \(X\) by \(1-p\) leaves its image unchanged and cannot increase its norm.

**Exercise 7.** In Example 4.3 use \(u_n(t)=\min(1,nt)\) as an approximate identity for \(I\). Determine the values of the central support projection \(p\in A^{**}\) under all point-evaluation states. Prove \(p\notin A\).

*Solution.* Uniform convergence \(u_nf\to f\) for \(f\in I\) follows by making \(f\) small near zero and using \(u_n=1\) away from zero for large \(n\). Hence \(u_n\to p\) strongly in the universal representation. The canonical normal extensions of evaluation at \(t\) take value zero on \(p\) when \(t=0\) and value one when \(t>0\). If \(p\) came from \(A\), that continuous function would have these point values, which is impossible at zero. Thus the bidual splitting uses a projection absent from the original C*-algebra.

**Exercise 8.** Show that the nuclearity–bidual theorem does not justify passing nuclearity to an arbitrary C*-subalgebra merely by inclusion. Identify the unsupported step in that attempted argument.

*Solution.* An inclusion \(B\subseteq A\) induces an inclusion \(B^{**}\subseteq A^{**}\). Injectivity of the larger algebra does not itself supply a ucp retraction onto this smaller von Neumann algebra. The permanence results proved here apply to corners, products, suitable directed limits and the explicit averaged fixed-point algebras. An arbitrary von Neumann subalgebra has not been shown to be one of those. Thus Theorem 3.1 cannot establish general subalgebra permanence by that argument; an additional extension or retraction mechanism would be required.

## References

Nathanial P. Brown, [The symbiosis of C*- and W*-algebras](https://arxiv.org/pdf/0812.1763v1), arXiv:0812.1763v1 (9 December 2008). Proposition 2.3.6, printed p.7, gives injectivity of the commutant of a nuclear represented algebra by an extension into the commuting range. Proposition 3.2.1, Theorem 3.2.2 and Corollary 3.2.3, printed p.10, describe the nuclearity–bidual equivalence and the ideal/quotient extension consequence. Brown leaves injectivity implying semidiscreteness to further von Neumann algebra theory; that implication here uses the full construction in [Averaging, crossed products, and injectivity](averaging-crossed-products-injectivity.md). The local proof of Proposition 2.1 instead constructs a retraction through the scalar tensor functional and the explicitly proved GNS complete order inverse. Lemma 1.1 supplies a central-support argument for arbitrary families of cyclic representations.

William B. Arveson, [Subalgebras of C*-algebras](https://projecteuclid.org/euclid.acta/1485889628), *Acta Mathematica* 123 (1969), 141–224. Theorem 1.2.3 proves the extension method behind Brown's commuting-range construction. Lemma 1.4.1 and Theorem 1.4.2 prove the dilation-commutant order correspondence. Section 2 above supplies the full scalar cyclic and nonunital form construction, including both matrix directions and the precise domination bound.

- [Bidual foundations] *Every bounded functional becomes normal in one representation*, UB-03–09, in the modular-theory course. Only the bidual, predual, normal-extension and second-adjoint results stated in the prerequisites are used.
- [GNS order] *Completely positive maps*, Theorem 7.3(1) and (4), in the existing foundations course. The inverse is used with domination by the distinguished state, with no unjustified ambient norm bound.
- [Central support] *Projections and types of von Neumann algebras*, Proposition 3.5, in the existing foundations course. The normal induction and central-support kernel are used in Lemma 1.1.
