# The rigidity theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An automorphism of the Turing degrees is a bijection of the set of degrees that preserves the order in both directions. This lesson proves the theorem of [OpenAI-R]: every automorphism is the identity. The proof has one input that is not proved in this course. By a theorem of T. Slaman and W. H. Woodin, an automorphism is always induced by a Borel function on the sets of natural numbers. Such a function, restricted to the cuts of real numbers, satisfies the assumptions of the theorem on recovery from four values. That theorem shows that the degree of a real number \(t\) lies below the image of the join of the degrees of \(t\) and of two auxiliary real numbers; and the auxiliary numbers can be removed by the avoidance lemma.

- Representations of automorphisms and the hypothesis (SW) (Section 1).
- From a representation to a function on the real line (Lemma 2.1).
- An automorphism with a Borel representation moves no degree downwards (Theorem 3.1).
- Rigidity (Theorem 3.2).

The lesson follows [OpenAI-R, Sections 3 and 5]. It uses all three earlier lessons of the course: [Relative computability and the Turing degrees](relative-computability-and-the-turing-degrees.md), [Category and computability](category-and-computability.md) and [Recovery from four values](recovery-from-four-values.md).

## 1. Representations

**Definition.** Let \(\pi\) be an automorphism of the degrees. A function \(\widehat F:2^{\mathbb N}\to2^{\mathbb N}\) *represents* \(\pi\) if for every set \(A\)
\[
\deg\bigl(\widehat F(A)\bigr)=\pi\bigl(\deg(A)\bigr).
\]

A representation chooses one set in the degree \(\pi(\deg A)\) for every set \(A\). It need not be one-to-one, and it need not give the same value at two sets of the same degree. Every automorphism has representations, by a choice of one set in every degree; the question is how regular a representation can be.

**Hypothesis (SW).** Every automorphism of the Turing degrees is represented by a Borel function.

This is a theorem of Slaman and Woodin. It is stated in [Slaman, Corollary 4.25], and in a stronger form, with a function that is definable in arithmetic, in [Slaman, Theorem 4.29]; the notion of a representation is [Slaman, Definition 4.20]. According to [Slaman], the proofs are in a manuscript of Slaman and Woodin of 2005 that is not published; they use the method of forcing. The theorem is not proved in this course, and the course does not check it. The important point of the statement is that the equation holds for every set \(A\), not only for sets outside a small exceptional set.

## 2. From a representation to a function on the line

**Lemma 2.1.** Let \(\pi\) be an automorphism of the degrees and \(\widehat F\) a Borel function that represents it. Let \(F(x)=\widehat F(C(x))\) for real \(x\). Then

1. \(F:\mathbb R\to2^{\mathbb N}\) is a Borel function;
2. \(\deg(F(x))=\pi(d(x))\) for every real \(x\);
3. \(F\) has countable fibres;
4. \(F(x+y)\le_TF(x)\oplus F(y)\) for all real \(x,y\).

**Proof.** (1) For a string \(\sigma\), the set of the \(x\) with \(\sigma\prec C(x)\) is an interval; so \(C\) is a Borel function. The sets \(S\subset2^{\mathbb N}\) whose preimage under \(C\) is a Borel set form a family that is closed under complements and countable unions and contains the open sets; so it contains the Borel sets, among them the preimages of open sets under \(\widehat F\).

(2) holds by the definition of a representation.

(3) If \(F(x)=F(y)\), then \(\pi(d(x))=\pi(d(y))\), so \(d(x)=d(y)\): the cut \(C(y)\) lies in the degree of \(C(x)\). A degree is a countable set of sets, and \(C\) is one-to-one (Lemmas 3.2 and 5.1 of the lesson on relative computability).

(4) By Lemma 5.1 (2) of that lesson, \(d(x+y)\le d(x)\vee d(y)\). An automorphism preserves the order and joins (Lemma 3.3 of that lesson), so
\[
\begin{aligned}
\deg F(x+y)&=\pi(d(x+y))\\
&\le\pi(d(x))\vee\pi(d(y))\\
&=\deg\bigl(F(x)\oplus F(y)\bigr).
\end{aligned}
\]
\(\blacksquare\)

Part (3) is the place where the proof uses that \(\pi\) is one-to-one.

## 3. The theorem

**Theorem 3.1.** Let \(\pi\) be an automorphism of the Turing degrees that is represented by a Borel function. Then
\[
\pi^{-1}(\mathbf a)\le\mathbf a\qquad\text{for every degree }\mathbf a ;
\]
equivalently, \(\mathbf a\le\pi(\mathbf a)\) for every degree.

**Proof.** Let \(F\) be the function of Lemma 2.1. Since \(\pi^{-1}(\mathbf 0)=\mathbf 0\), and every other degree is \(d(t)\) for an irrational \(t\) with \(0<t<1\) (Lemma 5.1 (3) of the lesson on relative computability), it suffices to prove \(\pi^{-1}(d(t))\le d(t)\) for such \(t\). Fix \(t\).

*A bound with two auxiliary numbers.* By Lemma 2.1, \(F\) satisfies the assumptions of Theorem 1.1 of the lesson on recovery. Let \(G_t\) be the comeager set of that theorem and \((u,v)\in G_t\); let \(\delta\) be the rational number of the theorem for this pair. The four numbers
\[
\begin{gathered}
u,\qquad u-v,\\
v-u+\delta t,\qquad v-u+\delta(t-1)
\end{gathered}
\]
are rational combinations of \(t,u,v\) and \(1\). So by Lemma 5.1 (2) of the lesson on relative computability their degrees are at most
\[
\mathbf b=d(t)\vee d(u)\vee d(v).
\]
By Lemma 2.1 (2) the degrees of the four values of \(F\) at these numbers are at most \(\pi(\mathbf b)\), and so is the degree of their join. By Theorem 1.1 of the lesson on recovery, \(C(t)\) is computable from this join. Hence \(d(t)\le\pi(\mathbf b)\), and for all \((u,v)\in G_t\)
\[
\pi^{-1}(d(t))\le d(t)\vee d(u)\vee d(v).
\]

*Removing the auxiliary numbers.* Let \(Y\) be a set of the degree \(\pi^{-1}(d(t))\). By the last display, \(Y\le_TC(t)\oplus C(u)\oplus C(v)\) for all \((u,v)\in G_t\). Suppose that \(Y\) is not computable from \(C(t)\). Then by Lemma 4.1 of the lesson on category, with \(A=C(t)\), the set of the pairs \((u,v)\) with \(Y\le_TC(t)\oplus C(u)\oplus C(v)\) is meager. It contains the comeager set \(G_t\). So the plane is the union of two meager sets, which contradicts Baire's theorem (Theorem 1.1 of that lesson). Therefore \(Y\le_TC(t)\), that is, \(\pi^{-1}(d(t))\le d(t)\).

The second form of the statement follows by applying \(\pi\) to both sides. \(\blacksquare\)

The set \(Y\) is fixed before the pair \((u,v)\) varies. The reductions of \(Y\) to \(C(t)\oplus C(u)\oplus C(v)\) may be different for different pairs; the avoidance lemma allows this.

**Theorem 3.2 (rigidity).** Assume (SW). Then every automorphism of the Turing degrees is the identity.

**Proof.** Let \(\pi\) be an automorphism and \(\mathbf a\) a degree. By (SW), \(\pi\) is represented by a Borel function, so \(\mathbf a\le\pi(\mathbf a)\) by Theorem 3.1. The inverse \(\pi^{-1}\) is an automorphism as well, and by (SW) it is represented by a Borel function; Theorem 3.1 for \(\pi^{-1}\) gives \(\pi(\mathbf a)\le\mathbf a\). So \(\pi(\mathbf a)=\mathbf a\). \(\blacksquare\)

The second step uses (SW) for \(\pi^{-1}\). It does not use an inverse of the function that represents \(\pi\); that function need not be one-to-one.

**What is proved.** Theorem 3.1 is proved in this course without a hypothesis: an automorphism that has a Borel representation moves every degree upwards or leaves it fixed, and if its inverse has a Borel representation too, it is the identity. Theorem 3.2 is proved from the hypothesis (SW), which the course does not prove. So the rigidity of the Turing degrees is established here as far as the theorem of Slaman and Woodin is.

According to [Slaman, Theorem 4.28], it was known before that every automorphism fixes all degrees above the degree \(\mathbf 0''\) of the second jump of the empty set. According to [Slaman, Theorem 5.9], the rigidity of the degrees is equivalent to a statement on definability, the bi-interpretability of the partial order of the degrees with second order arithmetic, which Slaman and Woodin had conjectured. [OpenAI-R] states this consequence as a corollary. The equivalence is not proved in this course.

**Truth-table degrees.** Kjos-Hanssen adapted the argument to truth-table reducibility [KH]. If an automorphism \(\pi\) of the truth-table degrees is induced on some comeager set of sets of natural numbers by a continuous function, then \(\pi\) is the identity [KH, Theorem 1.1]; in particular this holds when \(\pi\) is induced by a Baire measurable function [KH, Corollary 1.2], and the same statements hold for the weak truth-table degrees [KH, Theorem 1.5]. For a function continuous on all of Cantor space his proof uses only the Baire category theorem [KH, Theorem 1.3]. No analogue of (SW) is known for these degrees: the rigidity of the truth-table degrees is equivalent to the statement that every automorphism is induced on some comeager set by a continuous function [KH, Question 1.6]. Under the axiom of determinacy every automorphism has this property, so every automorphism of the truth-table degrees is the identity [KH, Section 5 and Theorem 1.4]; in ZFC the question is open.

## 4. Exercises

**4.1.** Show that the identity automorphism is represented by the identity function, and by the function \(A\mapsto\{2n:n\in A\}\). Which of the two is one-to-one on each degree?

**4.2.** Let \(\pi\) be an automorphism with \(\mathbf a\le\pi(\mathbf a)\) for all \(\mathbf a\). Show that \(\pi^{-1}(\mathbf a)\le\mathbf a\) for all \(\mathbf a\), and that \(\pi\) is the identity if also \(\mathbf a\le\pi^{-1}(\mathbf a)\) for all \(\mathbf a\).

**4.3.** In the proof of Theorem 3.1, why can one not take \(u=v=0\)?

**4.4.** Let \(\pi\) be represented by a Borel function \(\widehat F\). Show directly that for every real \(x\) and every rational \(c\ne0\), the sets \(\widehat F(C(x))\) and \(\widehat F(C(cx))\) are Turing equivalent.

**4.5.** Which statements of the three earlier lessons are used in the proof of Theorem 3.1, and for what?

## 5. Solutions

**4.1.** Both functions send a set to a set of the same degree: \(A\) and \(\{2n:n\in A\}\) are computable from each other by reductions that read one bit. Both are one-to-one everywhere.

**4.2.** Apply the inequality to \(\pi^{-1}(\mathbf a)\): \(\pi^{-1}(\mathbf a)\le\pi(\pi^{-1}(\mathbf a))=\mathbf a\). If also \(\mathbf a\le\pi^{-1}(\mathbf a)\), then \(\pi^{-1}(\mathbf a)=\mathbf a\) for all \(\mathbf a\).

**4.3.** The theorem on recovery gives its conclusion only for the pairs of a comeager set \(G_t\), and a single pair such as \((0,0)\) need not belong to it. For \(u=v=0\) the four values would be \(F(0)\), \(F(0)\), \(F(\delta t)\), \(F(\delta(t-1))\), of degrees \(\mathbf 0\) and \(\pi(d(t))\); the conclusion would be \(d(t)\le\pi(d(t))\) at once, but nothing gives it.

**4.4.** \(d(cx)=d(x)\) by Lemma 5.1 (2) of the lesson on relative computability, applied to \(cx\) and to \(c^{-1}(cx)\). So both sets have the degree \(\pi(d(x))\).

**4.5.** From the first lesson: joins and automorphisms (Lemma 3.3), countable degrees (Lemma 3.2), the cuts (Lemma 5.1), and, inside the theorem on recovery, the iteration lemma (Lemma 4.1). From the second: Baire's theorem, continuity on a comeager set and the Borel index function, inside the theorem on recovery, and the avoidance lemma (Lemma 4.1) to remove \(u\) and \(v\). From the third: Theorem 1.1.

## References

- [OpenAI-R] OpenAI, *Rigidity of the Turing degrees*, OpenAI Math Release preprint, 24 September 2026, Sections 3 and 5. https://github.com/openai/math/tree/main/preprints/Rigidity-of-the-Turing-degrees-September-24-2026
- [Slaman] T. A. Slaman, *Global properties of the Turing degrees and the Turing jump*, author's version. https://math.berkeley.edu/~slaman/papers/IMS_slaman.pdf
- [KH] B. Kjos-Hanssen, *Baire measurable functions and automorphisms of the truth-table degrees*, arXiv:2610.16059 (October 2026). https://arxiv.org/abs/2610.16059
