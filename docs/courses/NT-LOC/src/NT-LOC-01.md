# Absolute values, valuations and Ostrowski's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is not yet recorded. Public domain (CC0).*

Two rational numbers can be close because their difference is small in the real sense. They can also be close because their difference is divisible by a large power of a prime. These notions of distance lead to different limits, and eventually to different complete fields. The purpose of this lesson is to discover which measurements are possible, which measurements describe the same place, and how several places can be used at once.

We prove Ostrowski's classification for the rational numbers, the correspondence between non-archimedean places of a number field and its prime ideals, and the weak approximation theorem of Artin and Whaples. The product formula for the rational numbers explains why the normalizations at the different places fit together.

We assume elementary field theory, prime factorization and Bézout's identity for integers, polynomial division, and the notions of metric topology and convergence from *Point-Set Topology*. From *Discrete valuation rings and Dedekind domains* we use the properties explicitly recalled below. We do not assume that an absolute value extends to a larger field or that any completion has already been constructed. Those questions belong to *Completions, the p-adic numbers and complete discretely valued fields* and *Extensions of complete valued fields*.

The freely available reference is [Milne ANT]. For valuation rings, [Stacks] also treats valuations with more general ordered value groups. Here additive valuations take values in the real numbers, with an extra value for zero.

## 1. Distance and the triangle inequality

An **absolute value** on a field \(K\) is a function \(|\cdot|:K\to\mathbb R_{\geq0}\) satisfying

\[
|x|=0\Longleftrightarrow x=0,\qquad
|xy|=|x||y|,\qquad
|x+y|\leq |x|+|y|.
\]

Multiplicativity gives \(|1|=1\), \(|-1|=1\), \(|-x|=|x|\), and \(|x^{-1}|=|x|^{-1}\) for \(x\ne0\). If \(\zeta^m=1\) with \(m>0\), then \(|\zeta|^m=1\), so \(|\zeta|=1\).

The **trivial absolute value** is zero at zero and one everywhere else. Every absolute value defines the metric

\[
d(x,y)=|x-y|.
\]

Definiteness and symmetry follow from the first axiom and \(|-x|=|x|\); applying the triangle inequality to \(x-y=(x-z)+(z-y)\) gives the metric triangle inequality. Its open balls are \(B(a,r)=\{x:|x-a|<r\}\), with \(r>0\). Thus \(x_j\to a\) means \(|x_j-a|\to0\) as real numbers. The trivial absolute value gives the discrete topology. A nontrivial absolute value has an element \(u\) with \(0<|u|<1\): invert an element of value greater than one if necessary. Then the distinct nonzero elements \(u^j\) converge to zero. Its topology is therefore not discrete.

Applying the ordinary triangle inequality to \(x=(x-y)+y\), and then exchanging \(x,y\), gives the useful estimate \(\big||x|-|y|\big|\leq|x-y|\). In particular, the absolute-value function is continuous in its own metric.

We call an absolute value **non-archimedean** if the values of the integer multiples \(n\cdot1_K\) are bounded. Otherwise it is **archimedean**. The following result replaces a condition about integers by a condition about every pair of field elements.

**Proposition 1.1 (the strong triangle inequality).** The following conditions are equivalent:

1. \(|\cdot|\) is non-archimedean.
2. \(|n\cdot1_K|\leq1\) for every \(n\in\mathbb Z\).
3. \(|x+y|\leq\max(|x|,|y|)\) for every \(x,y\in K\).

When these conditions hold and \(|x|\ne|y|\), one has

\[
|x+y|=\max(|x|,|y|).
\]

*Proof.* Condition 3 bounds a sum of any finite number of ones by one, and also handles negative integers because \(|-1|=1\). Thus it implies condition 2, which implies condition 1.

Suppose condition 1 holds with bound \(C\geq1\). For every integer \(m\) and positive integer \(r\), multiplicativity gives

\[
|m\cdot1_K|^r=|m^r\cdot1_K|\leq C.
\]

Taking \(r\)-th roots and letting \(r\to\infty\) proves condition 2.

Now assume condition 2. Write \(M=\max(|x|,|y|)\). If \(M=0\), there is nothing to prove. For \(r\geq1\), the binomial expansion and the ordinary triangle inequality give

\[
|x+y|^r
\leq \sum_{j=0}^r\left|\binom rj\cdot1_K\right||x|^j|y|^{r-j}
\leq (r+1)M^r.
\]

Since \((r+1)^{1/r}\to1\), taking roots proves condition 3.

Finally, suppose \(|x|<|y|\). The strong inequality bounds \(|x+y|\) by \(|y|\). Applying it to \(y=(x+y)-x\) shows

\[
|y|\leq\max(|x+y|,|x|).
\]

The second entry is smaller than \(|y|\), so the first must equal \(|y|\). The other case follows by exchanging \(x\) and \(y\). \(\square\)

The strong triangle inequality is also called the **ultrametric inequality**. Its equality assertion is the **isosceles principle**: if two sides of a triangle have different lengths, the third has the larger length. In particular, a sum with a unique summand of largest absolute value cannot be zero. Indeed, the sum of the other terms has smaller absolute value, so the isosceles principle applies.

There is a related change in the geometry of balls. If \(b\in B(a,r)\), then \(B(b,r)=B(a,r)\). For example, if \(x\in B(b,r)\), then

\[
|x-a|\leq\max(|x-b|,|b-a|)<r;
\]

the reverse inclusion follows in the same way. Every point of an ultrametric ball can serve as its center.

In positive characteristic the integer multiples of one form a finite set. Proposition 1.1 therefore proves that every absolute value on such a field is non-archimedean. This does not say that it is trivial: rational function fields will provide counterexamples.

**Examples.** On \(\mathbb Q\), the usual real absolute value is archimedean. Its square root is also an absolute value, since

\[
\sqrt{|x+y|}\leq\sqrt{|x|+|y|}\leq\sqrt{|x|}+\sqrt{|y|}.
\]

Its square is not: \(|1+1|^2=4>2=|1|^2+|1|^2\). An absolute value on a finite field is trivial. For every nonzero element, two of its powers agree, so some positive power is one, and its absolute value is one.

## 2. Recording smallness by an additive valuation

For a non-archimedean absolute value define

\[
v(x)=-\log|x|\quad(x\ne0),\qquad v(0)=\infty.
\]

Here \(\log\) is the natural logarithm. The symbol \(\infty\) is larger than every real number, and \(\infty+a=\infty\), including \(a=\infty\). Then

\[
v(xy)=v(x)+v(y),\qquad
v(x+y)\geq\min(v(x),v(y)),\qquad
v(x)=\infty\Longleftrightarrow x=0.
\]

A function with these properties is an **additive valuation**. Conversely, for an additive valuation and a real number \(A>1\), the formula

\[
|x|=A^{-v(x)},\qquad A^{-\infty}=0,
\]

defines a non-archimedean absolute value. These assertions follow respectively by taking logarithms and exponentiating the defining inequalities. Larger valuations mean smaller absolute values. The function \(-\log|x|\) for an archimedean absolute value need not satisfy the valuation inequality; for example, its value at \(1+1\) is negative although its values at both summands are zero.

**Proposition 2.1 (the ring belonging to a valuation).** Let \(v\) be an additive valuation on \(K\). Then

\[
\mathcal O_v=\{x:v(x)\geq0\},\qquad
\mathfrak m_v=\{x:v(x)>0\}
\]

are a subring of \(K\) and its unique maximal ideal. Their unit group and residue field are

\[
\mathcal O_v^\times=\{x\ne0:v(x)=0\},\qquad
\kappa(v)=\mathcal O_v/\mathfrak m_v.
\]

The fraction field of \(\mathcal O_v\) is \(K\), and for every nonzero \(x\), either \(x\) or \(x^{-1}\) belongs to \(\mathcal O_v\).

*Proof.* The valuation identities give \(v(1)=0\), \(v(-x)=v(x)\), and \(v(x^{-1})=-v(x)\). They prove closure of \(\mathcal O_v\) under addition, subtraction, and multiplication. They also show that \(\mathfrak m_v\) is an ideal: adding two elements of positive valuation preserves positive valuation, and multiplying one by an element of nonnegative valuation does the same. It is proper because it excludes one.

An element of value zero has its inverse in \(\mathcal O_v\). An element of positive value does not. Consequently every element outside \(\mathfrak m_v\) is a unit, and every proper ideal is contained in \(\mathfrak m_v\). This proves maximality and uniqueness, and the quotient is a field. Finally, \(v(x)\) and \(v(x^{-1})\) have opposite signs. If \(x\notin\mathcal O_v\), write \(x=1/x^{-1}\) to see that it is in its fraction field. \(\square\)

A subring with this last alternative is a **valuation ring**. This agrees with the ring-theoretic notion in [Stacks, Tag 00I8]. The subgroup

\[
\Gamma_v=v(K^\times)\subseteq(\mathbb R,+)
\]

is its **value group**. Multiplication and inverses prove that it is a subgroup. It is zero for the trivial valuation. More general valuation rings can have ordered value groups that do not embed in \(\mathbb R\); the present discussion concerns real-valued valuations.

A nontrivial valuation is **discrete** if \(\Gamma_v\) is discrete in \(\mathbb R\). In that case \(\Gamma_v=\gamma\mathbb Z\) for some \(\gamma>0\). To see this, choose \(\eta>0\) such that no nonzero group element has absolute value less than \(\eta\). Distinct group elements are at least \(\eta\) apart, so there are only finitely many in any bounded interval. The positive elements therefore have a least element \(\gamma\). Subtracting an integer multiple of \(\gamma\) from any group element leaves a remainder in \([0,\gamma)\), which must be zero. Dividing \(v\) by \(\gamma\) gives a **normalized discrete valuation**, with value group \(\mathbb Z\).

We recall two facts from *Discrete valuation rings and Dedekind domains*. The valuation ring of a normalized discrete valuation is a **discrete valuation ring**, or **DVR**. A DVR has a generator \(\pi\) of its maximal ideal, called a **uniformizer**, and each nonzero element of its fraction field has a unique expression

\[
x=u\pi^m,\qquad u\in\mathcal O_v^\times,\quad m\in\mathbb Z.
\]

Conversely this expression defines the normalized valuation of a DVR by \(v(x)=m\). The ring characterizations are [Stacks, Tag 00PD]. The nontriviality requirement matters: the trivial valuation has \(\mathcal O_v=K\), \(\mathfrak m_v=0\), and value group zero. A field is a valuation ring, but is not a DVR.

Recall that a **Dedekind domain** is a Noetherian integrally closed domain of Krull dimension one; this convention excludes fields. For a Dedekind domain \(R\) with fraction field \(K\), and a nonzero prime ideal \(\mathfrak p\), the localization

\[
R_{\mathfrak p}=\{a/s:a\in R,\ s\in R\setminus\mathfrak p\}
\]

is a DVR [Stacks, Tag 034X]. Its normalized valuation \(v_{\mathfrak p}(x)\) is the exponent of \(\mathfrak p\) in the factorization of the principal fractional ideal \(xR\) [Milne ANT, Theorem 3.20 and Example 3.26(c)]. We use these results without reproving ideal factorization.

**Example: divisibility at one rational prime.** For a prime \(p\) and a nonzero rational number \(x=a/b\), put

\[
v_p(x)=v_p(a)-v_p(b),\qquad |x|_p=p^{-v_p(x)},
\]

where \(v_p(a)\) counts the factors of \(p\) in the nonzero integer \(a\). Set \(v_p(0)=\infty\) and \(|0|_p=0\). These definitions are independent of the fraction representing \(x\). Unique factorization proves additivity under products. Writing two fractions over a common denominator proves

\[
v_p(x+y)\geq\min(v_p(x),v_p(y));
\]

the sum of two integers divisible by \(p^r\) remains divisible by \(p^r\). Thus \(|\cdot|_p\) is an absolute value. Its valuation ring is \(\mathbb Z_{(p)}\), the rationals representable with denominator prime to \(p\), and its residue field is \(\mathbb F_p\). Reduction sends \(a/b\) to \(\overline a\,\overline b^{-1}\); it is onto and its kernel consists of the elements of positive valuation.

In this metric, \(p^j\to0\). At a different prime \(q\), all these terms have value one. For \(p=5\), the usual large integer \(125\) has absolute value \(1/125\).

## 3. When two absolute values describe one place

Changing a measurement can preserve all limits. For example, the usual absolute value and its square root give the same open sets on \(\mathbb Q\). Two absolute values are **equivalent** when they induce the same topology on the field.

**Proposition 3.1 (equivalence).** For two nontrivial absolute values \(|\cdot|_1,|\cdot|_2\) on \(K\), the following are equivalent:

1. Their metric topologies agree.
2. \(\{x:|x|_1<1\}=\{x:|x|_2<1\}\).
3. There is a real number \(c>0\) such that \(|x|_1=|x|_2^c\) for every \(x\in K\).

In fact, even the one-direction implication \(|x|_1<1\Rightarrow |x|_2<1\) implies equivalence.

*Proof.* For any absolute value, \(x^r\to0\) as \(r\to\infty\) exactly when \(|x|<1\). Equal topologies therefore give condition 2.

Suppose now only that the stated one-direction implication holds. Choose \(t\in K\) with \(|t|_1>1\). Applying the implication to \(t^{-1}\) gives \(|t|_2>1\). For \(x\ne0\), define real numbers

\[
\alpha=\frac{\log|x|_1}{\log|t|_1},\qquad
\beta=\frac{\log|x|_2}{\log|t|_2}.
\]

If integers \(m,n\), with \(n>0\), satisfy \(m/n>\alpha\), then \(|x^nt^{-m}|_1<1\). The implication yields \(|x^nt^{-m}|_2<1\), hence \(\beta<m/n\). If \(m/n<\alpha\), use \(t^mx^{-n}\) instead to obtain \(m/n<\beta\). Rational numbers approach \(\alpha\) from both sides, so \(\alpha=\beta\). This holds also when \(\alpha\) is zero or negative. Consequently

\[
\log|x|_1=c\log|x|_2,
\qquad c=\frac{\log|t|_1}{\log|t|_2}>0.
\]

This proves condition 3, including at zero. Condition 2 implies the one-direction hypothesis we just used. Finally, under condition 3,

\[
|x-a|_1<r\Longleftrightarrow |x-a|_2<r^{1/c},
\]

so the balls give the same topology. \(\square\)

A **place** is an equivalence class of nontrivial absolute values. An exponent \(c\) changes radii but leaves the place unchanged. For non-archimedean values it also leaves the valuation ring and maximal ideal unchanged, and rescales the additive valuation. Being archimedean or non-archimedean is preserved by equivalence, since positive powers preserve boundedness of the integer values. A power of an archimedean absolute value need not itself satisfy the triangle inequality; equivalence here compares functions that are already absolute values.

## 4. All measurements on the rational numbers

Write \(|\cdot|_\infty\) for the usual real absolute value on \(\mathbb Q\). Alongside it are the absolute values \(|\cdot|_p\) constructed in Section 2.

**Theorem 4.1 (Ostrowski).** Every nontrivial absolute value on \(\mathbb Q\) is equivalent to exactly one of

\[
|\cdot|_\infty,\quad |\cdot|_2,\quad |\cdot|_3,\quad |\cdot|_5,\quad\ldots.
\]

*Proof.* First suppose \(|\cdot|\) is non-archimedean. Every integer has value at most one. If all nonzero integers had value one, multiplicativity would make every nonzero rational have value one. Thus some integer has value less than one. Factoring that integer shows that there is a prime \(p\) with \(|p|<1\).

There cannot be two such primes. For distinct primes \(p,q\), Bézout's identity gives integers \(a,b\) with \(ap+bq=1\). If both prime values were less than one, then

\[
1=|ap+bq|\leq\max(|a||p|,|b||q|)<1,
\]

since \(|a|,|b|\leq1\). This is impossible. All primes other than \(p\) therefore have value one. The prime factorization of a nonzero rational number now gives

\[
|x|=|p|^{v_p(x)}=|x|_p^c,
\qquad c=-\frac{\log|p|}{\log p}>0.
\]

Now suppose \(|\cdot|\) is archimedean. We need an estimate that does not assume in advance that every integer greater than one has value greater than one. Fix integers \(m,b\geq2\), and set \(A_b=\max(1,|b|)\). Expand \(m^r\) in base \(b\):

\[
m^r=d_0+d_1b+\cdots+d_\ell b^\ell,
\qquad 0\leq d_j<b,
\qquad \ell\leq\frac{r\log m}{\log b}.
\]

The ordinary triangle inequality bounds \(|d_j|\) by \(d_j\leq b\). Therefore

\[
|m|^r\leq b(\ell+1)A_b^\ell
\leq b\left(1+\frac{r\log m}{\log b}\right)
A_b^{r\log m/\log b}.
\]

Taking \(r\)-th roots and letting \(r\to\infty\) gives

\[
|m|\leq\max(1,|b|)^{\log m/\log b}. \tag{4.1}
\]

Archimedeanness supplies an integer \(b\geq2\) with \(|b|>1\). If some integer \(m\geq2\) had \(|m|\leq1\), applying (4.1) with the roles of \(m,b\) reversed would give \(|b|\leq1\), a contradiction. Thus \(|m|>1\) for every \(m\geq2\).

We can now drop the maximum in (4.1). Applying the estimate in both directions shows

\[
\frac{\log|m|}{\log m}=\frac{\log|b|}{\log b}=\alpha>0
\]

for every \(m,b\geq2\). Multiplicativity, inverses, and \(|-1|=1\) extend \(|m|=m^\alpha\) to

\[
|x|=|x|_\infty^\alpha\qquad(x\in\mathbb Q).
\]

The original triangle inequality at \(1+1\) also gives \(2^\alpha\leq2\), so \(0<\alpha\leq1\).

For uniqueness, the ordinary absolute value is archimedean, whereas every \(p\)-adic one is non-archimedean. Distinct primes give distinct places: \(|p|_p<1\) but \(|p|_q=1\) for \(q\ne p\), contradicting condition 2 of Proposition 3.1 if they were equivalent. \(\square\)

*Reference:* [Milne ANT, Theorem 7.12].

The trivial absolute value is excluded from this list of places. The archimedean branch also explains the restriction on exponents: positive powers describe the topology, but powers greater than one of the usual absolute value fail the defining triangle inequality.

## 5. Approximating several targets at once

For two inequivalent absolute values, a sequence can tend to zero in one metric and grow in the other. The next construction turns that separation into simultaneous approximation. It uses only the ordinary triangle inequality, so it includes archimedean places.

**Lemma 5.1 (separating one place from the others).** For pairwise inequivalent nontrivial absolute values \(|\cdot|_1,\ldots,|\cdot|_n\), there exists \(z\in K\) such that

\[
|z|_1>1,\qquad |z|_i<1\quad(2\leq i\leq n).
\]

*Proof.* For \(n=1\), use nontriviality. For \(n=2\), the last assertion of Proposition 3.1, applied in both directions, supplies nonzero elements \(u,w\) with

\[
|u|_1<1,\quad |u|_2\geq1,
\qquad |w|_2<1,\quad |w|_1\geq1.
\]

Then \(z=w/u\) has the required strict inequalities.

Inductively choose \(b\) separating place 1 from places \(2,\ldots,n-1\), and \(c\) separating place 1 from place \(n\). If \(|b|_n<1\), use \(b\). If \(|b|_n=1\), use \(cb^r\) for sufficiently large \(r\): its value grows at place 1, tends to zero at places \(2,\ldots,n-1\), and stays \(|c|_n<1\) at place \(n\).

If \(|b|_n>1\), use

\[
c\frac{b^r}{1+b^r}.
\]

The denominator is never zero because \(|b|_1>1\). In any absolute value, the reverse triangle inequality gives

\[
|1+b^r|\geq\big||b|^r-1\big|.
\]

If \(|b|>1\), then

\[
\left|\frac{b^r}{1+b^r}-1\right|
\leq\frac1{|b|^r-1}\longrightarrow0.
\]

If \(|b|<1\), then

\[
\left|\frac{b^r}{1+b^r}\right|
\leq\frac{|b|^r}{1-|b|^r}\longrightarrow0.
\]

Consequently the proposed element tends to \(c\) at places 1 and \(n\), and to zero at all intermediate places. Its required strict inequalities hold for large \(r\). Here we use continuity of absolute value, which follows from \(\big||x|-|y|\big|\leq|x-y|\). This completes the induction. \(\square\)

**Theorem 5.2 (weak approximation; Artin–Whaples).** Let \(|\cdot|_1,\ldots,|\cdot|_n\) be pairwise inequivalent nontrivial absolute values on a field \(K\), with \(n\geq1\). For targets \(a_1,\ldots,a_n\in K\) and \(\varepsilon>0\), there exists \(x\in K\) such that

\[
|x-a_i|_i<\varepsilon\qquad(1\leq i\leq n).
\]

*Proof.* For each \(j\), reorder the places in Lemma 5.1 to obtain \(z_j\) with \(|z_j|_j>1\) and \(|z_j|_i<1\) for \(i\ne j\). Set

\[
e_{j,r}=\frac{z_j^r}{1+z_j^r}.
\]

The denominators are nonzero, as their vanishing would give \(|z_j|_j^r=1\). The estimates in the lemma prove

\[
e_{j,r}\longrightarrow
\begin{cases}1&\text{at place }j,\\0&\text{at every other listed place.}\end{cases}
\]

Let \(M=\max_{i,j}|a_j|_i\), a finite nonnegative real number, and choose

\[
\delta=\frac{\varepsilon}{2n(1+M)}.
\]

There are finitely many convergence conditions, so one sufficiently large \(r\) makes \(|e_{i,r}-1|_i<\delta\) and \(|e_{j,r}|_i<\delta\) for all \(i\ne j\). Put \(x=\sum_j a_je_{j,r}\). At place \(i\), the ordinary triangle inequality gives

\[
\begin{aligned}
|x-a_i|_i
&\leq |a_i|_i|e_{i,r}-1|_i
+\sum_{j\ne i}|a_j|_i|e_{j,r}|_i\\
&\leq nM\delta<\varepsilon.
\end{aligned}
\]

If \(M=0\), all targets are zero and \(x=0\) works as well. \(\square\)

*Reference:* [Milne ANT, Theorem 7.20]; the theorem is due to Artin and Whaples.

Equivalently, the diagonal map \(K\to K^n\) has dense image when the factors carry the respective metric topologies: a basic product neighborhood prescribes finitely many target balls, and one can use the smallest of their radii. This statement requires no completion.

The inequivalence hypothesis has content. For two identical absolute values, approximating the targets 0 and 1 with both errors less than 1/2 would give \(1\leq|x|+|1-x|<1\).

**Worked example.** The rational number \(x=272/299\) is within \(1/10\) of the target 1 in the real metric, the target 0 in the 2-adic metric, and the target 1 in the 3-adic metric:

\[
|x-1|_\infty=\frac{27}{299}<\frac1{10},\qquad
|x|_2=\frac1{16}<\frac1{10},\qquad
|x-1|_3=\frac1{27}<\frac1{10}.
\]

For the second equality, \(272=16\cdot17\) and 299 is odd. For the third, \(x-1=-27/299\) and 299 is prime to 3. An integer cannot meet these three requirements: the real condition forces it to be 1, whose 2-adic distance from zero is one. The theorem allows the rational denominator that makes all three conditions compatible.

## 6. Prime ideals as non-archimedean places

Let \(K\) be a number field, that is, a finite extension of \(\mathbb Q\), and let \(\mathcal O_K\) be its ring of algebraic integers. Recall that \(\mathcal O_K\) is a Dedekind domain [*Number fields*, lesson 3, Proposition 3.1]. It is free of rank \([K:\mathbb Q]\) over \(\mathbb Z\), and its fraction field is \(K\) [Milne ANT, Proposition 2.29 and its proof].

For a nonzero prime ideal \(\mathfrak p\), write

\[
N(\mathfrak p)=\#(\mathcal O_K/\mathfrak p).
\]

This is a finite integer greater than one. Indeed, choose \(0\ne a\in\mathfrak p\). A monic integer polynomial satisfied by \(a\) can be chosen with nonzero constant term, by removing powers of the variable if needed. Its equation shows that this constant term belongs to \(\mathfrak p\cap\mathbb Z\). Thus \(\mathfrak p\) contains a nonzero integer \(m\), and \(\mathcal O_K/\mathfrak p\) is a quotient of the finite group \(\mathcal O_K/m\mathcal O_K\). It is a domain because \(\mathfrak p\) is prime. A finite domain is a field: multiplication by a nonzero element is injective and hence surjective. This also verifies the meaning of its cardinality.

**Proposition 6.1 (prime ideals and places).** The non-archimedean places of \(K\) correspond bijectively to the nonzero prime ideals of \(\mathcal O_K\). The place belonging to \(\mathfrak p\) has representative

\[
|x|_{\mathfrak p}=N(\mathfrak p)^{-v_{\mathfrak p}(x)}.
\]

Its valuation ring is \((\mathcal O_K)_{\mathfrak p}\), and its residue field is \(\mathcal O_K/\mathfrak p\).

*Proof.* Let \(|\cdot|\) be a nontrivial non-archimedean absolute value on \(K\). Every integer has value at most one. If \(a\in\mathcal O_K\) satisfies

\[
a^d+c_{d-1}a^{d-1}+\cdots+c_0=0,\qquad c_j\in\mathbb Z,
\]

and \(|a|>1\), its leading term has value \(|a|^d\), strictly larger than every other term. The observation following Proposition 1.1 rules this out. Therefore \(|a|\leq1\) on \(\mathcal O_K\).

Set

\[
\mathfrak p=\{a\in\mathcal O_K:|a|<1\}.
\]

The ultrametric inequality and the bound on \(\mathcal O_K\) make this a proper ideal. If \(ab\in\mathfrak p\) and \(a,b\in\mathcal O_K\), then \(|a||b|<1\) with both factors at most one; at least one is less than one. Thus \(\mathfrak p\) is prime. It is nonzero: otherwise every nonzero element of \(\mathcal O_K\) would have value one, and the fraction-field property would make the absolute value trivial on \(K\).

Put \(R=(\mathcal O_K)_{\mathfrak p}\). Its elements have value at most one, since a denominator outside \(\mathfrak p\) has value one. This ring is a DVR by the recalled Dedekind-domain theorem. Choose a uniformizer \(\pi\). Since \(\pi\in\mathfrak pR\), it can be written \(a/s\) with \(a\in\mathfrak p\), \(s\notin\mathfrak p\), so \(0<|\pi|<1\). For a unit \(u\in R^\times\), both \(u\) and \(u^{-1}\) have value at most one; hence \(|u|=1\).

The DVR expression \(x=u\pi^{v_{\mathfrak p}(x)}\) consequently gives

\[
|x|=|\pi|^{v_{\mathfrak p}(x)}
=|x|_{\mathfrak p}^{\,c},
\qquad c=-\frac{\log|\pi|}{\log N(\mathfrak p)}>0.
\]

It also proves that \(|x|\leq1\) precisely when \(x\in R\), so the entire valuation ring, not just its intersection with \(\mathcal O_K\), has been identified.

Conversely, the discrete valuation \(v_{\mathfrak p}\) defines the displayed nontrivial absolute value. For \(a\in\mathcal O_K\), positive valuation means \(a/1\in\mathfrak pR\), equivalently \(sa\in\mathfrak p\) for some \(s\notin\mathfrak p\). Primality makes this equivalent to \(a\in\mathfrak p\). Thus its elements of value less than one in \(\mathcal O_K\) are exactly \(\mathfrak p\). Equivalent absolute values have the same such set, so different prime ideals give different places. The two constructions are inverse. Finally, reduction \(R\to\mathcal O_K/\mathfrak p\), sending \(a/s\) to \(\overline a/\overline s\), has kernel \(\mathfrak pR\) and is onto. This proves the residue-field assertion. \(\square\)

The normalization here uses the size of the residue field. For \(K=\mathbb Q\), it gives \(N((p))=p\), and recovers the earlier \(p\)-adic value. We have classified the non-archimedean places of number fields without assuming an extension theorem for absolute values. The classification of their archimedean places and the product formula for general number fields are developed later in *Places of number fields in extensions and the product formula*.

## 7. A balance across all rational places

**Proposition 7.1 (the product formula for \(\mathbb Q\)).** With \(|p|_p=1/p\) and the usual \(|\cdot|_\infty\), every \(x\in\mathbb Q^\times\) satisfies

\[
\prod_v|x|_v=|x|_\infty\prod_{p\text{ prime}}|x|_p=1.
\]

Only finitely many factors differ from one.

*Proof.* Write \(x=\pm\prod_p p^{e_p}\), with integer exponents \(e_p\), almost all zero. Then

\[
|x|_\infty=\prod_p p^{e_p},\qquad |x|_p=p^{-e_p}.
\]

The finite products cancel. \(\square\)

**Worked example.** Since \(360/7=2^3 3^2 5\,7^{-1}\), the values are

| Place | \(2\) | \(3\) | \(5\) | \(7\) | \(\infty\) |
|---|---:|---:|---:|---:|---:|
| \(\lvert360/7\rvert_v\) | \(1/8\) | \(1/9\) | \(1/5\) | \(7\) | \(360/7\) |

All other values are one. Their product is \((1/8)(1/9)(1/5)7(360/7)=1\). A prime in the denominator gives a negative valuation and an absolute value greater than one.

The chosen representatives of the places are essential. Replacing only \(|\cdot|_\infty\) by its square root would make the product at \(x=2\) equal to \(1/\sqrt2\). Equivalence alone does not fix a product formula. Taking logarithms of the correctly normalized formula gives

\[
\log|x|_\infty=\sum_p v_p(x)\log p.
\]

This is the identity used to interpret a principal divisor as having degree zero in *The projective line over \(\mathbb F_1\) and the ABC conjecture*.

## 8. Exercises

**Exercise 1 (easy: powers of a measurement).** Prove that \(|\cdot|^c\) is an absolute value for \(0<c\leq1\). If \(|\cdot|\) is non-archimedean, prove this for every \(c>0\).

**Exercise 2 (easy: a balance of prime factors).** Verify the product formula for \(x=3/10\), giving every factor that differs from one.

**Exercise 3 (medium: algebraic constant fields).** Show that every absolute value on an algebraic extension of a finite field is trivial. The extension need not be finite.

**Exercise 4 (medium: the rational function field).** Classify the absolute values of \(\mathbb F_q(t)\) that are trivial on \(\mathbb F_q\), both as actual functions and up to equivalence. Include the trivial absolute value. Describe the valuation at infinity and normalized representatives of all the nontrivial places.

**Exercise 5 (hard: constructing simultaneous approximations).** Prove weak approximation for pairwise inequivalent nontrivial absolute values without taking Theorem 5.2 as a black box. Start from the one-direction criterion in Proposition 3.1, construct an element large at one place and small at the others, and convert it into approximations to 1 and 0. Give an explicit error bound for the final sum.

## 9. Complete solutions

**Solution 1.** Definiteness and multiplicativity survive every positive power. For \(a,b\geq0\) and \(0<c\leq1\), we claim \((a+b)^c\leq a^c+b^c\). If \(a+b>0\), put \(s=a/(a+b)\). Since \(s^c\geq s\) and \((1-s)^c\geq1-s\), multiplying their sum by \((a+b)^c\) proves the claim. If \(a+b=0\), it is immediate. Thus

\[
|x+y|^c\leq(|x|+|y|)^c\leq|x|^c+|y|^c.
\]

For an ultrametric value and any \(c>0\), monotonicity gives directly

\[
|x+y|^c\leq\max(|x|^c,|y|^c),
\]

which implies the ordinary triangle inequality. The square of the real absolute value from Section 1 shows why the exponent restriction is needed in the general assertion.

**Solution 2.** The nonzero valuations are \(v_2(x)=-1\), \(v_3(x)=1\), and \(v_5(x)=-1\). Therefore

\[
|x|_2=2,\qquad |x|_3=1/3,\qquad |x|_5=5,
\qquad |x|_\infty=3/10.
\]

All other finite-place values are one, and \(2(1/3)5(3/10)=1\).

**Solution 3.** Let \(L/\mathbb F_q\) be algebraic and \(a\in L^\times\). The field \(\mathbb F_q(a)\) has finite degree \(d\), and hence \(q^d\) elements: coordinates in any field basis have \(q\) choices each. Powers of \(a\) therefore repeat, so \(a^m=1\) for some \(m>0\). Multiplicativity gives \(|a|^m=1\), and \(|a|=1\). Every element is treated in its own finite subextension; no bound on \([L:\mathbb F_q]\) is needed. Thus the value is trivial on all of \(L\).

**Solution 4.** The constant field is finite, so every absolute value on it is automatically trivial. Positive characteristic and Proposition 1.1 make every absolute value on \(\mathbb F_q(t)\) ultrametric. Consider a nontrivial one. In the formulas below \(f,g\) are nonzero polynomials; the absolute values take zero to zero, and the additive valuations take zero to \(\infty\).

If \(|t|>1\), the nonzero terms of a polynomial \(f(t)=\sum a_it^i\) have distinct absolute values \(|t|^i\). The leading term is uniquely largest. The isosceles principle therefore gives

\[
|f|=|t|^{\deg f},\qquad
|f/g|=B^{\deg f-\deg g},\quad B=|t|>1.
\]

This is the place at infinity, whose normalized additive valuation is

\[
v_\infty(f/g)=\deg g-\deg f.
\]

It measures order of vanishing at zero after substituting \(t=1/s\): write

\[
\frac{f(1/s)}{g(1/s)}
=s^{\deg g-\deg f}
\frac{s^{\deg f}f(1/s)}{s^{\deg g}g(1/s)}.
\]

The last numerator and denominator have nonzero constant terms. In particular \(v_\infty(t)=-1\).

If \(|t|\leq1\), every polynomial has value at most one. The set

\[
I=\{f\in\mathbb F_q[t]:|f|<1\}
\]

is a proper prime ideal by the same multiplication and addition arguments as in Proposition 6.1. It is nonzero, for otherwise all nonzero polynomials, and hence all nonzero fractions, would have value one. Polynomial division makes \(\mathbb F_q[t]\) a principal ideal domain, so \(I=(P)\) for a unique monic irreducible polynomial \(P\). Explicitly, a monic element of least positive degree generates \(I\) by division; primality forces it to be irreducible. Put \(A=|P|\), so \(0<A<1\). If \(f=P^r f_0\) with \(P\nmid f_0\), then \(f_0\notin I\), and \(|f_0|=1\). Thus

\[
|f/g|=A^{\operatorname{ord}_P(f)-\operatorname{ord}_P(g)}.
\]

Conversely, each such formula, and each infinity formula with \(B>1\), is an absolute value. Products add orders or degrees. For sums, divisibility gives the valuation inequality at \(P\); at infinity, a common denominator and \(\deg(f+h)\leq\max(\deg f,\deg h)\) give it. These checks also show independence of the presentation as a fraction.

Distinct polynomials give distinct places because the set \(I\) recovers \(P\). The infinity place has \(|t|>1\), whereas all finite places have \(|t|\leq1\). Positive powers vary \(A\) through \((0,1)\), or \(B\) through \((1,\infty)\), so Proposition 3.1 gives exactly one place for each \(P\), and one at infinity. The trivial absolute value is the remaining actual function and is not a place.

Normalized representatives are

\[
|x|_P=q^{-\deg(P)\operatorname{ord}_P(x)},\qquad
|f/g|_\infty=q^{\deg f-\deg g}.
\]

The finite residue field \(\mathbb F_q[t]/(P)\) has \(q^{\deg P}\) elements, explaining the finite normalization. At infinity put \(s=1/t\). The valuation ring consists of fractions regular at \(s=0\), namely \(\mathbb F_q[s]_{(s)}\). Taking the value at zero maps this ring onto \(\mathbb F_q\), with kernel generated by \(s\). Thus the uniformizer is \(1/t\), and the residue field is \(\mathbb F_q\). For example, over \(\mathbb F_2\), the fraction \((t^2+t+1)/t^3\) has values \(1/4\) at \(P=t^2+t+1\), \(8\) at \(t\), and \(1/2\) at infinity. Their product is one; all other finite values are one.

**Solution 5.** For two inequivalent places, failure of the one-direction criterion in each direction gives \(u,w\) with \(|u|_1<1\leq|u|_2\) and \(|w|_2<1\leq|w|_1\). Their quotient \(w/u\) is large at place 1 and small at place 2. For one place, nontriviality supplies a large element.

Inductively let \(b\) be large at place 1 and small at places \(2,\ldots,n-1\); let \(c\) be large at place 1 and small at place \(n\). If \(|b|_n\leq1\), the elements \(cb^r\) eventually have the desired values at every place: they grow at place 1, decay at the intermediate places, and at place \(n\) have value at most \(|c|_n<1\). If \(|b|_n>1\), use

\[
\frac{c}{1+b^{-r}}.
\]

At places 1 and \(n\), this tends to \(c\); at each intermediate place it tends to zero. For the last assertion, if \(D=|b|^{-r}>1\), the reverse triangle inequality bounds its value by \(|c|/(D-1)\). At a place with \(|b|>1\), its difference from \(c\) has value at most

\[
\frac{|c||b|^{-r}}{1-|b|^{-r}}\longrightarrow0.
\]

All denominators are nonzero because \(|b|_1>1\). This proves separation for any finite list, and reordering separates any chosen place.

Choose separators \(z_j\), one for each place, and set \(h_{j,r}=(1+z_j^{-r})^{-1}\). At place \(j\), \(h_{j,r}\to1\), with error at most \(|z_j|_j^{-r}/(1-|z_j|_j^{-r})\). At a different place \(i\), it tends to zero, with value at most \(1/(|z_j|_i^{-r}-1)\). Given the targets, put \(M=\max_{i,j}|a_j|_i\) and \(\delta=\varepsilon/[2n(1+M)]\). Take a common sufficiently large \(r\) so every specified error is less than \(\delta\). The element \(x=\sum_j a_jh_{j,r}\) then satisfies, for every \(i\),

\[
|x-a_i|_i\leq
|a_i|_i|h_{i,r}-1|_i+
\sum_{j\ne i}|a_j|_i|h_{j,r}|_i
\leq nM\delta<\varepsilon.
\]

If all targets are zero, simply use zero. This is the required theorem with the estimates and all induction cases supplied.

## 10. What this lesson does not prove

The ring-theoretic prerequisites used in Section 2 and Section 6 are the following. These are the prerequisites from *Discrete valuation rings and Dedekind domains*; we use the precise statements at the indicated source locators.

- For a number field \(K\), \(\mathcal O_K\) is a Noetherian integrally closed domain and every nonzero prime ideal is maximal [*Number fields*, lesson 3, Proposition 3.1]. It is free of rank \([K:\mathbb Q]\) over \(\mathbb Z\) and has fraction field \(K\) [Milne ANT, Proposition 2.29 and its proof].
- The valuation ring of a normalized discrete valuation is a DVR [Milne ANT, Proposition 3.27]. A Noetherian normal local domain of dimension one is a DVR; a DVR has the uniformizer expressions used above [Stacks, Tag 00PD]. For a Dedekind domain, localization at every nonzero prime ideal is a DVR [Stacks, Tag 034X]. The prime must be nonzero: localization at the zero prime is a field.
- Nonzero fractional ideals of a Dedekind domain factor uniquely as finite products of integer powers of nonzero prime ideals. For a principal fractional ideal, the exponent at \(\mathfrak p\) agrees with the normalized valuation of its localization [Milne ANT, Theorem 3.20 and Example 3.26(c)].

The general ring-theoretic comparison of definitions of a valuation ring is [Stacks, Tag 00I8]. Proposition 2.1 proves directly the properties needed for real-valued valuations here. No result about extensions of absolute values, completed fields, or the general number-field product formula is used in our proofs.

The written programme proofs are in *Number fields*: lesson 2, **Discriminants and integral bases**, Theorem 2.3 for the integer lattice; and lesson 3, **Discrete valuation rings and Dedekind domains**, Proposition 3.1, Theorem 3.2 and its two local characterizations for Dedekindness, unique fractional-ideal factorization and DVR localizations. These are preceding ring-theoretic dependencies, not external-book proof substitutes. The classical sources below give attribution and comparison.

## References

- J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, 19 July 2020. Free author notes; the precise results used for comparison are identified above.
- [The Stacks project](https://stacks.math.columbia.edu/) and the separately identified [AI Integrated Stacks Project English edition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/). The exact tags and scope of the comparisons are identified in the text.
