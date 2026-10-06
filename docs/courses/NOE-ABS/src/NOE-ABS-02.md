# The converse and composition series

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Ideal factorization appears to be a conclusion about multiplication. In fact, it also forces finite generation, dimension one and integral closedness. We first recover these properties from unique factorization, then read prime multiplicities from the simple constituents of quotient modules. This connects ideal theory to a general invariant, module length.

Read Noether's axioms for Dedekind domains first. We use basic localization, the Chinese remainder theorem, and Jordan–Hölder from Noetherian and Artinian rings, Theorem 3.2: two composition series of the same module have isomorphic simple factors with the same multiplicities. For the factorization theorem by local DVRs, compare Discrete valuation rings and Dedekind domains, Theorem 3.2. Basic references are [Noether], [Stacks] and [Milne].

## 1. Invertibility cannot be assumed in the converse

Let \(R\) be a domain with identity in which every nonzero integral ideal has a unique finite factorization into nonzero prime ideals. We have not assumed any chain condition. The equality \(\mathfrak p=\mathfrak p^2\) is impossible: its two sides would be distinct factorizations of the same nonzero ideal. Thus choose \(x\in\mathfrak p\setminus\mathfrak p^2\).

**Lemma 1.1.** Every nonzero prime \(\mathfrak p\) is a factor of a nonzero principal ideal, and hence is invertible.

**Proof.** For any \(y\in\mathfrak p\), factor \((x,y^2)\). At least one factor is contained in \(\mathfrak p\), by primality. At most one is: two such factors would put \(x\) in \(\mathfrak p^2\). After localization at \(\mathfrak p\), all the other factors become unit ideals. Therefore \((x,y^2)R_{\mathfrak p}\) is a prime ideal. It contains \(y^2\), hence \(y\), so

\[
 y=ax+by^2\quad\text{in }R_{\mathfrak p}.
\]

Since \(by\) belongs to the maximal ideal, \(1-by\) is a unit. It follows that \(y\in(x)R_{\mathfrak p}\). As this works for every \(y\in\mathfrak p\),

\[
 \mathfrak pR_{\mathfrak p}=(x)R_{\mathfrak p}.
\]

Now factor \((x)\). Exactly one factor \(\mathfrak q\) is contained in \(\mathfrak p\), by the same argument; therefore \(\mathfrak qR_{\mathfrak p}=(x)R_{\mathfrak p}=\mathfrak pR_{\mathfrak p}\). Contraction of a localized prime contained in \(\mathfrak p\) recovers that prime, giving \(\mathfrak q=\mathfrak p\). Write \((x)=\mathfrak pJ\). Then \(\mathfrak p(x^{-1}J)=R\), as required. \(\square\)

This argument uses localization only to find a principal multiple. The forward factorization theorem in the previous lesson remains a global argument. The next steps of the converse also take place globally.

**Lemma 1.2.** An invertible fractional ideal is finitely generated.

**Proof.** If \(IJ=R\), choose a finite expression \(1=\sum_{i=1}^n a_i b_i\), where \(a_i\in I\), \(b_i\in J\). For \(a\in I\),

\[
 a=\sum_i(ab_i)a_i,
\]

and every coefficient \(ab_i\) belongs to \(R\). Hence the \(a_i\) generate \(I\). \(\square\)

All nonzero ideals factor into invertible primes, so all are invertible and finite. The zero ideal is finite too. Thus \(R\) is Noetherian.

**Lemma 1.3.** Every nonzero prime is maximal.

**Proof.** Suppose \(0\ne\mathfrak p\subseteq\mathfrak m\), with \(\mathfrak m\) maximal. Since \(\mathfrak m\) is invertible, \(J=\mathfrak p\mathfrak m^{-1}\) is a nonzero integral ideal. Then \(\mathfrak p=J\mathfrak m\). Unique factorization forces \(J=R\) and \(\mathfrak p=\mathfrak m\). \(\square\)

## 2. Integral closedness from exponents

Factor fractional ideals by clearing a denominator, exactly as in the preceding lesson. For a nonzero prime \(\mathfrak p\), define \(v_{\mathfrak p}(I)\) to be its exponent in the fractional ideal \(I\), and write \(v_{\mathfrak p}(x)=v_{\mathfrak p}((x))\) for \(x\in K^\times\). Product exponents add. Furthermore,

\[
 I\subseteq J\iff v_{\mathfrak p}(I)\ge v_{\mathfrak p}(J)\text{ for every }\mathfrak p.
\]

For the forward direction \(IJ^{-1}\) is integral and so has nonnegative exponents; the reverse direction follows by factoring it. In particular, \(x\in R\) if and only if all its exponents are nonnegative.

**Lemma 2.1.** For fractional ideals \(I,J\),

\[
 v_{\mathfrak p}(I+J)=\min(v_{\mathfrak p}(I),v_{\mathfrak p}(J)).
\]

**Proof.** Put \(H=I+J\). The integral ideals \(IH^{-1}\) and \(JH^{-1}\) sum to \(R\). They cannot both lie in \(\mathfrak p\). Their \(\mathfrak p\)-exponents are therefore nonnegative with at least one zero. Subtracting \(v_{\mathfrak p}(H)\) proves the formula. \(\square\)

Consequently \(v_{\mathfrak p}(x+y)\ge\min(v_{\mathfrak p}(x),v_{\mathfrak p}(y))\) when \(x+y\ne0\). If the two exponents differ, equality holds: a strict inequality, applied to \(x=(x+y)-y\), would contradict the smaller exponent. Thus a sum with one term of strictly smallest exponent cannot vanish.

**Theorem 2.2, the converse.** A domain with identity and unique prime factorization of nonzero ideals satisfies all five axioms of the preceding lesson.

**Proof.** Noetherianity and dimension at most one were proved in Section 1. For normality, suppose

\[
 x^n+c_1x^{n-1}+\cdots+c_n=0,\qquad c_i\in R.
\]

If \(x\notin R\), choose \(\mathfrak p\) with \(v_{\mathfrak p}(x)<0\). Then the first term has exponent \(nv_{\mathfrak p}(x)\), strictly smaller than every nonzero later term, because \(v_{\mathfrak p}(c_i)\ge0\). The preceding observation makes the sum nonzero, a contradiction. Hence \(x\in R\). The identity and domain axioms were hypotheses, and the Artinian criterion supplies the descending chain axiom. \(\square\)

*Reference:* [Noether, Section 9] gives the converse; [Stacks, Tag 034X] gives the equivalent characterizations. The exponent argument above proves integral closedness without using the local normality criterion.

## 3. Quotients record multiplicities

We recall three isomorphisms for modules. A homomorphism \(f:M\to N\) induces \(M/\ker f\simeq\operatorname{im}f\), by sending a coset to its image. If \(U,V\subseteq M\), the same map applied to \(U\to(U+V)/V\) gives \(U/(U\cap V)\simeq(U+V)/V\). Finally, for \(U\subseteq V\subseteq M\), mapping the coset of \(m+U\) to \(m+V\) gives \((M/U)/(V/U)\simeq M/V\). These are the isomorphism theorems used below.

**Lemma 3.1.** If \(J\) is a nonzero invertible integral ideal and \(\mathfrak p\) a nonzero prime, then \(J/J\mathfrak p\simeq R/\mathfrak p\).

**Proof.** It is a vector space over \(R/\mathfrak p\). Write \(1=\sum a_i b_i\) with \(a_i\in J\), \(b_i\in J^{-1}\). At least one \(a_i b_i\notin\mathfrak p\). In \(R_{\mathfrak p}\) that product is a unit, and \(J_{\mathfrak p}=a_iR_{\mathfrak p}\): for \(a\in J\), \(a/a_i=(ab_i)/(a_i b_i)\) lies in \(R_{\mathfrak p}\). Therefore its quotient by \(\mathfrak p\) is one-dimensional. Localization does not change a module annihilated by the maximal ideal \(\mathfrak p\), since all inverted scalars act as nonzero field elements. The original quotient is consequently one-dimensional too. \(\square\)

**Theorem 3.2.** If \(I=\prod_{i=1}^r\mathfrak p_i^{e_i}\) with distinct primes, then \(R/I\) has finite length \(\sum_i e_i\). Its simple factors are \(R/\mathfrak p_i\), with multiplicity \(e_i\).

**Proof.** List the prime factors with repetitions as \(\mathfrak q_1,\ldots,\mathfrak q_N\), and form

\[
 R=J_0\supset J_1\supset\cdots\supset J_N=I,
 \qquad J_j=\mathfrak q_1\cdots\mathfrak q_j.
\]

Each quotient \(J_{j-1}/J_j\) is \(R/\mathfrak q_j\) by Lemma 3.1, hence simple and nonzero. Taking quotients by \(I\) gives a composition series. It has \(N=\sum e_i\) factors. Jordan–Hölder makes the multiset intrinsic. \(\square\)

The annihilator of the simple module \(R/\mathfrak p\) is exactly \(\mathfrak p\). Two such modules can be isomorphic only when their primes agree. Thus Jordan–Hölder yields a second proof of uniqueness of prime exponents once existence and invertibility are established. Length counts ideal factors, not the logarithm of the size of a quotient unless all residue fields have the same size.

For \(\mathbb Z/12\), the chain \(\mathbb Z\supset2\mathbb Z\supset4\mathbb Z\supset12\mathbb Z\) gives factors \(\mathbb Z/2,\mathbb Z/2,\mathbb Z/3\). In \(\mathbb Z[i]\), \((2)=(1+i)^2\) as ideals because \(2\) and \((1+i)^2\) differ by a unit. Hence \(\mathbb Z[i]/(2)\) has two factors \(\mathbb F_2\); its cardinality is four and its length is two.

## 4. Non-normal orders and the stronger theorem

Let \(R=\mathbb Z[s]\), \(s^2=-3\). The reduction modulo \(2\) is \(\mathbb F_2[s]/((s+1)^2)\), with its unique prime \(\mathfrak p=(2,1+s)\). Direct multiplication gives

\[
 \mathfrak p^2=(4,2+2s,(1+s)^2)=2\mathfrak p,
\]

since \((1+s)^2=2(s-1)=2(s+1)-4\). If \((2)\) were a product of primes, every factor would contain \((2)\) and therefore equal \(\mathfrak p\). Exponent one fails because \(1+s\notin(2)\). For \(n\ge2\), \(\mathfrak p^n=2^{n-1}\mathfrak p\subseteq2\mathfrak p\), and \(2\notin2\mathfrak p\). Thus no exponent works.

Similarly let \(R=k[t^2,t^3]\) and \(\mathfrak m=(t^2,t^3)\). The quotient \(R/(t^2)\) is \(k[t^3]/((t^3)^2)\), so \(\mathfrak m\) is the only prime containing \((t^2)\). The ideal \((t^2)\) is not \(\mathfrak m\), because \(t^3\notin(t^2)\). It is not \(\mathfrak m^n\) for \(n\ge2\), because those powers have no term of degree two. Again factorization fails.

**Matusita's strengthening.** In a domain with identity, it suffices to assume that every nonzero proper ideal is a finite product of prime ideals; uniqueness then follows and the ring is Dedekind. This is a stronger theorem than Theorem 2.2 because uniqueness was used there before invertibility had been proved. We state it without proof [Matusita, Section 2, following the formulation in the introduction]. It rules out interpreting uniqueness as an independent extra axiom in the final characterization.

## 5. Exercises

1. **Easy.** Give the simple factors, their multiplicities and the length of \(\mathbb Z[i]/(6)\).
2. **Medium.** Explain why \(\mathfrak p\ne\mathfrak p^2\) follows from unique ideal factorization even before Noetherianity is known.
3. **Medium.** Prove finite generation of an invertible ideal and show that the argument actually exhibits it as a direct summand of a finite free module.
4. **Medium.** Prove that \((t^2)\) does not factor into prime ideals in \(k[t^2,t^3]\).
5. **Hard.** Reprove the integral-closedness step using prime exponents only, including the assertion that a uniquely smallest exponent prevents cancellation.

## 6. Solutions

**1.** The polynomial \(T^2+1\) is irreducible over \(\mathbb F_3\), so \((3)\) is prime with residue field \(\mathbb F_9\). The prime above \(2\) is \((1+i)\), of exponent two. Thus the factors are \(\mathbb F_2,\mathbb F_2,\mathbb F_9\), and length is three. Their cardinalities multiply to \(2\cdot2\cdot9=36\), agreeing with the rank-two lattice quotient by \(6\).

**2.** A nonzero prime itself is a factorization with one factor. Its square has the two-factor expression \(\mathfrak p\mathfrak p\). Equality would contradict equality of factor multisets. No finiteness assumption on the generators of \(\mathfrak p\) is involved.

**3.** Choose \(1=\sum a_i b_i\) as in Lemma 1.2. The map \(R^n\to I\), \((r_i)\mapsto\sum r_i a_i\), has a section \(I\to R^n\), \(a\mapsto(ab_i)_i\). Their composite on \(I\) is the identity. Thus \(I\) is finite and projective.

**4.** Every factor contains \((t^2)\). The quotient has only the prime \((t^3)\), so all factors are \(\mathfrak m\). The degree argument in Section 4 excludes each power, including exponent one. The empty product is \(R\) and is also excluded.

**5.** Lemma 2.1 gives the inequality for sums. If \(v(a)<v(b)\) and \(v(a+b)>v(a)\), apply it to \(a=(a+b)-b\) to obtain \(v(a)>v(a)\), a contradiction. Repeatedly adding higher-exponent terms leaves the smallest exponent unchanged; hence a sum with just one smallest term cannot be zero. For an integral equation and \(v(x)<0\), the exponents \(nv(x)\) and \(v(c_i)+(n-i)v(x)\) are strictly ordered with the first smallest. No such equation is possible, so all exponents of \(x\) are nonnegative and \((x)\subseteq R\).

## What this lesson does not prove

Jordan–Hölder and the general theory of length are prerequisite results [Stacks, Tags 00IU and 00IX]. Matusita's theorem is stated without proof. The converse, its global integral-closedness step, the composition series and both non-factorization examples are proved above.

## References

- **[Noether]** Emmy Noether, *Abstrakter Aufbau der Idealtheorie in algebraischen Zahl- und Funktionenkörpern*, Mathematische Annalen **96** (1927), 26–61, Sections 4, 9 and 10.
- **[Stacks]** The Stacks Project, Tags [034X](https://stacks.math.columbia.edu/tag/034X), [00IU](https://stacks.math.columbia.edu/tag/00IU) and [00IX](https://stacks.math.columbia.edu/tag/00IX), also in the corresponding sections of the [AI Integrated Stacks Project English algebra reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html). AI Integrated Stacks Project contains AI-proposed corrections and AI-written additions and is not reviewed by the Stacks Project's maintainers.
- **[Milne]** J. S. Milne, *Algebraic Number Theory*, Chapter 3, [author's notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- **[Matusita]** Kameo Matusita, *Über ein bewertungstheoretisches Axiomensystem für die Dedekind-Noethersche Idealtheorie*, Japanese Journal of Mathematics **19** (1944), 97–110, [journal edition](https://doi.org/10.4099/jjm1924.19.1_97).
