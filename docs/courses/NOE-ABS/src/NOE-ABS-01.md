# Noether's axioms for Dedekind domains

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The two factorizations \(6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5})\) show that elements can fail to factor uniquely. Ideals recover the missing structure. This lesson explains why a short list of ring properties forces every nonzero ideal to be invertible and then to factor uniquely. The proof takes place in the fraction field throughout; it does not infer factorization from discrete valuations.

We assume basic module theory and integral dependence. In Noetherian and Artinian rings, Proposition 1.2 gives finite generation of submodules over a Noetherian ring, Theorem 4.2 gives the dimension-zero Artinian criterion, and Theorem 3.3 gives finite length under both chain conditions [Stacks, Tags 00FP, 00KH and 00KJ]. We also use lying over and incomparability for integral extensions [Stacks, Tags 00GQ and 00GT], with dimension comparison [Tag 00OJ]; these are proved in Integral extensions: lying over, going up and going down, Theorems 3.2, 3.3 and 5.1. The local characterization by DVRs [Tag 034X] is treated in **Discrete valuation rings, normal rings and Serre’s criterion** and is used here only in examples. Basic references are [Noether], [Milne] and [Stacks]. Continue with The converse and composition series.

## 1. The five axioms and the question they answer

All rings in this lesson are commutative. For a nonzero ring \(R\), Noether's axioms in modern form are:

1. Every ascending chain of ideals stabilizes.
2. For every nonzero ideal \(J\), descending chains of ideals containing \(J\) stabilize.
3. There is an identity element.
4. A product of two nonzero elements is nonzero.
5. Every element of \(K=\operatorname{Frac}(R)\) integral over \(R\) belongs to \(R\).

The first axiom says that every ideal is finitely generated. To see this equivalence, if an ideal were not finite, repeatedly adjoining a new element would give a strictly ascending chain. Conversely, the union of an ascending chain is an ideal; finitely many generators lie at one stage and force stabilization.

In the presence of the first axiom, the second says that every nonzero prime is maximal. Indeed, it makes \(R/J\) Artinian, so its primes are maximal. Conversely, if nonzero primes are maximal, then \(R/J\) is Noetherian of dimension zero and hence Artinian. Thus the five axioms say that \(R\) is a Noetherian integrally closed domain of dimension at most one. A field is allowed. We call such a ring a **Dedekind domain**. Another definition requires unique prime factorization of nonzero ideals; this lesson and the next prove the equivalence. [Stacks, Tags 034W and 034X] use these two descriptions.

For a nonzero ideal \(I\), put

\[
 I^{-1}=(R:I)=\{x\in K:xI\subseteq R\}.
\]

It is an \(R\)-submodule of \(K\) containing \(R\). If \(0\ne a\in I\), it lies in \(a^{-1}R\), so it has a common denominator. The main task is to prove \(II^{-1}=R\).

## 2. Two global devices

**Lemma 2.1.** In a Noetherian domain, every nonzero proper ideal contains a finite product of nonzero prime ideals.

**Proof.** Suppose not. Among the nonzero counterexamples choose a maximal one \(I\), using the ascending chain condition. It is not prime, because a prime contains itself. Choose \(a,b\notin I\) with \(ab\in I\). Each of \(I+(a)\) and \(I+(b)\) is larger than \(I\), so each contains a product of nonzero primes. If one is \(R\), use the empty product \(R\). Their product is contained in

\[
 (I+(a))(I+(b))=I^2+aI+bI+(ab)\subseteq I.
\]

Combining the two products gives the required product in \(I\), a contradiction. The empty product cannot result for proper \(I\). \(\square\)

**Lemma 2.2, the determinant trick.** Let \(M\subseteq K\) be a nonzero finitely generated \(R\)-module. If \(xM\subseteq M\), then \(x\) is integral over \(R\).

**Proof.** Choose generators \(m_1,\ldots,m_n\) and coefficients \(a_{ij}\in R\) such that \(xm_i=\sum_j a_{ij}m_j\). Multiply the equation \((x\operatorname{id}-A)m=0\) by the adjugate matrix. It gives \(\det(x\operatorname{id}-A)m_i=0\) for every \(i\). Some \(m_i\ne0\); since we are in a field, \(\det(x\operatorname{id}-A)=0\). The polynomial \(\det(T\operatorname{id}-A)\) is monic in \(R[T]\). \(\square\)

Finite generation gives an equation; integral closedness turns that equation into membership in the ring. This is the mechanism behind invertibility.

## 3. From prime inverses to factorization

**Lemma 3.1.** Suppose \(R\) is a Noetherian domain of dimension at most one, and \(\mathfrak p\) is a nonzero prime. Then \(\mathfrak p^{-1}\supsetneq R\).

**Proof.** Choose \(0\ne a\in\mathfrak p\). By Lemma 2.1 choose a product \(\mathfrak p_1\cdots\mathfrak p_r\subseteq(a)\) with \(r\) as small as possible. Since this product lies in \(\mathfrak p\), some \(\mathfrak p_i\subseteq\mathfrak p\). Both are nonzero maximal ideals, so they are equal. Relabel with \(\mathfrak p_1=\mathfrak p\). Minimality says that \(\mathfrak p_2\cdots\mathfrak p_r\nsubseteq(a)\); for \(r=1\), this means \(R\nsubseteq(a)\). Choose \(b\) in that product outside \((a)\). Then \(b/a\notin R\), but \((b/a)\mathfrak p\subseteq R\). \(\square\)

**Proposition 3.2.** In a Dedekind domain every nonzero prime is invertible.

**Proof.** We have \(\mathfrak p\subseteq\mathfrak p\mathfrak p^{-1}\subseteq R\). Since \(\mathfrak p\) is maximal, the middle ideal is either \(\mathfrak p\) or \(R\). In the first case every \(x\in\mathfrak p^{-1}\) stabilizes the finite nonzero module \(\mathfrak p\). Lemma 2.2 and axiom 5 then give \(x\in R\), contradicting Lemma 3.1. Hence \(\mathfrak p\mathfrak p^{-1}=R\). \(\square\)

**Theorem 3.3, Noether's global factorization theorem.** Every nonzero integral ideal in a Dedekind domain is a unique finite product of nonzero prime ideals. The unit ideal is the empty product.

**Proof of existence.** If there are counterexamples, choose a maximal one \(I\). Choose a maximal ideal \(\mathfrak p\supseteq I\); it is nonzero. Then \(J=I\mathfrak p^{-1}\) is an integral ideal, because \(I\subseteq\mathfrak p\), and \(I\subseteq J\). This inclusion is strict: equality would make every element of \(\mathfrak p^{-1}\) stabilize \(I\), and the determinant trick would contradict Lemma 3.1. By maximality, \(J\) factors. Multiplying its factorization by \(\mathfrak p\) gives \(I=J\mathfrak p\), the desired contradiction.

**Proof of uniqueness.** If \(\mathfrak p_1\cdots\mathfrak p_r=\mathfrak q_1\cdots\mathfrak q_s\), then the right side lies in \(\mathfrak p_1\). Primality gives \(\mathfrak q_j\subseteq\mathfrak p_1\) for some \(j\); maximality makes them equal. Multiplication by their inverse cancels that factor. Repeating proves equality of the multisets. A nonempty product of proper ideals cannot equal \(R\), so the cancellation process ends simultaneously. \(\square\)

Every nonzero ideal is therefore invertible. An inverse constructed as a product of prime inverses agrees with \((R:I)\): if \(IJ=R\) and \(xI\subseteq R\), then \(x=xIJ\subseteq J\).

**Corollary 3.4.** The nonzero fractional ideals form a free abelian group with basis the nonzero primes.

**Proof.** A fractional ideal means a nonzero \(R\)-submodule of \(K\) with a common denominator. Over our Noetherian ring it is automatically finite. Choose \(0\ne d\in R\) with \(dI\subseteq R\). Factor \(dI\) and \((d)\), and subtract their prime exponents to write \(I\) as a finite product of integer powers of primes. Uniqueness follows by clearing negative exponents and applying Theorem 3.3. \(\square\)

The quotient by the subgroup of principal fractional ideals is the **ideal class group**. It measures which ideal factorizations can be represented by element factorizations. Containment reverses exponent inequalities: \(I\subseteq J\) if and only if every exponent of \(I\) is at least the corresponding exponent of \(J\). Indeed, containment implies that \(IJ^{-1}\) is integral, and the converse follows by multiplying back.

## 4. Passing to a larger field

**Theorem 4.1.** If \(R\) is Dedekind and \(L/K\) is finite separable, its integral closure \(B\) in \(L\) is a finite \(R\)-module and is Dedekind.

**Proof.** For a nonfield \(R\), this is Decomposition of primes in extensions, Theorem 5.1, which proves the assertion for arbitrary Dedekind bases and finite separable fraction-field extensions. Its proof bounds the closure by a finite lattice using the inverse trace matrix. That lesson excludes fields in its Dedekind convention. If \(R\) is a field, then \(B=L\), a finite-dimensional \(R\)-module and a Dedekind domain in our convention. \(\square\)

The nondegeneracy of the separable field trace is Orders and the discriminant theorem, Lemma 1.2 [Milne, Proposition 2.26]. Trace integrality is a separate input: the trace of an integral element is integral [Milne, Corollary 2.21]. The cited trace-lattice argument applies to arbitrary Dedekind bases. For an inseparable extension the conclusion that \(B\) is Dedekind remains true, but module finiteness can fail. The precise replacement is Krull–Akizuki: if \(A\) is a one-dimensional Noetherian domain, \(L/\operatorname{Frac}(A)\) is finite, and \(A\subseteq C\subseteq L\), then \(C\) is Noetherian of dimension at most one [Stacks, Tag 00PG]. Applied to the integral closure, this gives the Dedekind conclusion [Stacks, Tag 09IG]. A DVR whose integral closure in a finite extension is not finite is exhibited in [Stacks, Tag 09E1]. These statements do not imply that all Dedekind domains are Japanese.

## 5. Arithmetic and geometric examples

Write \(s=\sqrt{-5}\). The ring of integers of \(\mathbb Q(s)\) is \(R=\mathbb Z[s]\), by the quadratic integral-basis criterion [Milne, Introduction; the trace-and-norm test is Proposition 2.11 and Remark 2.12]. Its prime ideals

\[
 \mathfrak p=(2,1+s),\qquad
 \mathfrak q=(3,1+s),\qquad
 \mathfrak q'=(3,1-s)
\]

have residue fields \(\mathbb F_2,\mathbb F_3,\mathbb F_3\). Direct multiplication gives \(\mathfrak p^2=(2)\) and \(\mathfrak q\mathfrak q'=(3)\), so

\[
 (6)=\mathfrak p^2\mathfrak q\mathfrak q'.
\]

There are three distinct primes and four factors counted with multiplicity. For example, \(\mathfrak p^2\) is generated by \(4,2+2s,-4+2s\); these generate \((2)\). For the product above \(3\), the generators include \(9,3(1+s),3(1-s),6\), which generate \((3)\). Moreover, \((1+s)=\mathfrak p\mathfrak q\) and \((1-s)=\mathfrak p\mathfrak q'\), as follows either by these generators or by containment and the index \(6\). Thus both element factorizations yield the same ideal factorization.

The ideal \(\mathfrak p\) is not principal: a generator \(a+bs\) would have absolute norm \(a^2+5b^2=2\), which has no integer solution. Its class is nontrivial, and its square is trivial. This proves a nontrivial class group without determining the whole group.

Let \(k\) have characteristic different from \(2\), and set \(C=k[x,y]/(y^2-x^3-x)\). The polynomial is irreducible because \(x^3+x\) is not a square in \(k(x)\). The two partial derivatives cannot vanish at a point of the curve, even after extending \(k\): \(2y=0\) gives \(y=0\), and if \(x^3+x=0\), then either \(x=0\), with derivative \(1\), or \(x^2=-1\), with derivative \(-2\). Thus the curve is smooth; its one-dimensional local rings are regular and hence DVRs [Vakil, 13.2.4/G, 13.2.7(b), 24.8.9 and 13.5.6; Stacks, Tag 00PD]. This smoothness argument works over any field of the stated characteristic. By the local normality criterion [Stacks, Tag 034X], \(C\) is normal. Since it is finite over \(k[x]\), it is precisely the integral closure of \(k[x]\) in its fraction field. The same ideal theory therefore applies to its finite places.

The domain \(\mathbb Z[\sqrt{-3}]\) is Noetherian and one-dimensional but not normal: \((1+\sqrt{-3})/2\) is integral and missing. The next lesson shows directly that \((2)\) does not factor into primes there. Meanwhile \(k[x,y]\) is normal and Noetherian but has the nonmaximal nonzero prime \((x)\). A descending chain above \((x)\) is

\[
 (x,y)\supsetneq(x,y^2)\supsetneq(x,y^3)\supsetneq\cdots.
\]

The ideal \(I=(x^2,y)\) cannot be a product of primes. Each factor would contain \(I\), hence contain its radical \(\mathfrak m=(x,y)\); maximality forces every factor to equal \(\mathfrak m\). But \(I\ne\mathfrak m\), since \(x\notin I\), and \(I\ne\mathfrak m^n\) for \(n\ge2\), since \(y\notin\mathfrak m^2\). This gives a direct failure of ideal factorization when axiom 2 is omitted.

## 6. Exercises

1. **Easy.** Factor \((6)\) in \(\mathbb Z[\sqrt{-5}]\), and prove that the class group has a nontrivial element.
2. **Medium.** For \(\mathfrak p=(2,1+\sqrt{-5})\), compute \(\mathfrak p^{-1}\) and verify \(\mathfrak p\mathfrak p^{-1}=R\) directly.
3. **Medium.** Show that \(R/I\) has finite length when \(R\) is Noetherian, every nonzero prime is maximal, and \(I\ne0\).
4. **Medium.** Let \(M\) be a finite module over a commutative ring \(R\), and \(u\in\operatorname{End}_R(M)\). Prove that some monic \(P\in R[T]\) satisfies \(P(u)=0\), without assuming faithfulness. Then let \(x\) belong to a commutative \(R\)-algebra \(S\), and suppose \(M\) is a faithful \(R[x]\)-module finite over \(R\). Prove that \(x\) is integral over \(R\). Explain why faithfulness over \(R\) alone does not suffice in this second assertion.
5. **Hard.** Let \(\operatorname{char}k\ne2\), let \(t^2=x\), and find the integral closure of \(k[x]\) in \(k(t)\). Factor the extensions of \((x)\) and \((x-1)\).

## 7. Solutions

**1.** The computation in Section 5 gives \((6)=\mathfrak p^2\mathfrak q\mathfrak q'\). Its quotient maps verify primality. If \(\mathfrak p=(a+b\sqrt{-5})\), its index would be \(a^2+5b^2=2\), impossible. Thus \([\mathfrak p]\ne1\), while \([\mathfrak p]^2=1\).

**2.** Since \(\mathfrak p^2=(2)\), multiplication shows that \(\mathfrak p/2\) is an inverse. Every inverse is \((R:\mathfrak p)\), as established after Theorem 3.3. Hence

\[
 \mathfrak p^{-1}=R+R(1+\sqrt{-5})/2.
\]

The second generator is outside \(R\). The product is generated by \(2,1+s,(1+s)^2/2\). The last generator is \(s-2\); subtracting it from \(1+s\) gives \(3\), and \(3-2=1\). Thus the product is \(R\).

**3.** The quotient is Noetherian. A prime of the quotient comes from a prime containing \(I\), hence is maximal. The dimension-zero Artinian criterion makes the quotient Artinian. A nonzero module satisfying both chain conditions has a composition series: choose a maximal proper submodule using finite generation, then repeat; the descending chain condition forces termination. Applied to \(R/I\), this gives finite length.

**4.** With generators \(m_i\) and an endomorphism \(u\), choose a matrix \(A\) representing its action on the generators. The adjugate identity gives \(\det(T\operatorname{id}-A)|_{T=u}M=0\). For scalar multiplication by an element of a larger ring, this is a monic equation annihilating \(M\). The endomorphism conclusion \(P(u)=0\) needs no faithfulness. For the scalar conclusion, the action map \(R[x]\to\operatorname{End}_R(M)\) must be injective: faithfulness over \(R[x]\) gives \(P(x)=0\) in that ring. Faithfulness only over \(R\) does not: take \(R=k\), \(S=k[T]\), \(M=S/(T)\) and \(x=T\). The module is faithful over \(k\) and \(x\) acts as zero, but \(T\) is not integral over \(k\). Without the stronger hypothesis, \(P(x)\) need only belong to the \(R[x]\)-annihilator. See [Stacks, Tag 05BT; Vakil, Exercise 8.2.I]. In Lemma 2.2 a nonzero submodule of a field is faithful, so cancellation supplies exactly this step.

**5.** The ring \(k[t]\) is a PID, hence integrally closed, and is integral and finite over \(k[t^2]\). If an element of \(k(t)\) is integral over \(k[t^2]\), the same equation makes it integral over \(k[t]\), so it lies in \(k[t]\). Thus the closure is \(k[t]\). The ideal \((x)\) becomes \((t)^2\), and \((x-1)\) becomes \((t-1)(t+1)\). The two latter primes are distinct because \(2\ne0\) in \(k\).

## What this lesson does not prove

The dimension-zero Artinian criterion, finite-submodule theorem, finite-length criterion, lying over and incomparability are prerequisite results with the locators in the opening paragraph. The separable closure theorem is cited from *Decomposition of primes in extensions*, Theorem 5.1, with the field case handled here. Its trace inputs are Orders and the discriminant theorem, Lemma 1.2, and Milne Corollary 2.21 for trace integrality. Krull–Akizuki, its integral-closure consequence and the non-Japanese DVR example are used in exactly the forms cited in Section 4. The local characterization by DVRs is [Stacks, Tag 034X]. The smooth-curve regularity and quadratic integral-basis criteria have the precise locators in Section 5. For the local route to factorization, compare Discrete valuation rings and Dedekind domains, Theorem 3.2. That lesson excludes fields in its definition; the present convention includes them, with vacuous nonzero-prime factorization. Its local proof and the global proof here are different routes to the same result for nonfields.

## References

- **[Noether]** Emmy Noether, *Abstrakter Aufbau der Idealtheorie in algebraischen Zahl- und Funktionenkörpern*, Mathematische Annalen **96** (1927), 26–61, especially Sections 1–3 and 5–8. The short announcements of 1924–1925 give the earlier context.
- **[Milne]** J. S. Milne, *Algebraic Number Theory*, Chapters 2–3, [author's course notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- **[Stacks]** The Stacks Project, Tags [034W](https://stacks.math.columbia.edu/tag/034W), [034X](https://stacks.math.columbia.edu/tag/034X), [00PG](https://stacks.math.columbia.edu/tag/00PG), [09IG](https://stacks.math.columbia.edu/tag/09IG) and [09E1](https://stacks.math.columbia.edu/tag/09E1). AI Integrated Stacks Project is an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks Project's maintainers; its [English algebra reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html) has the corresponding labels.

- **[Vakil]** Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Exercise 8.2.I, Sections 13.2 and 13.5, and 24.8.9.
- **Additional prerequisite tags:** [00FP](https://stacks.math.columbia.edu/tag/00FP), [00KH](https://stacks.math.columbia.edu/tag/00KH), [00KJ](https://stacks.math.columbia.edu/tag/00KJ), [00GQ](https://stacks.math.columbia.edu/tag/00GQ), [00GT](https://stacks.math.columbia.edu/tag/00GT), [00OJ](https://stacks.math.columbia.edu/tag/00OJ), [00PD](https://stacks.math.columbia.edu/tag/00PD), and [05BT](https://stacks.math.columbia.edu/tag/05BT).
