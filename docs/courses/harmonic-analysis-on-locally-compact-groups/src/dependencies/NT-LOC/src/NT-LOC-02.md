# Completions, the p-adic numbers and complete discretely valued fields

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is not yet recorded. Public domain (CC0).*

*NT-ADL bundled edition, source-reconciled on 5 October 2026 by GPT-6.1 Sol (OpenAI), Ultra. This adaptation retains the provider lesson's mathematical scope and adds the source comparisons identified below. The upstream provider draft is unchanged. Original AI-written exposition is CC0; human reference works and genuinely reused human expression retain their own terms.*

## Introduction

An absolute value tells us which approximations become accurate. Completion supplies limits for all Cauchy approximations without changing the arithmetic already present. For the p-adic absolute value, accuracy means agreement modulo a high power of a prime. This makes the completed ring of integers both an inverse limit of finite rings and a space of infinite digit sequences.

We construct completions, develop the arithmetic and topology of \(\mathbb Q_p\), and extend the digit construction to every complete discretely valued field. We then prove that the complete archimedean fields are precisely \(\mathbb R\) and \(\mathbb C\), with powers of their usual absolute values. This identifies all archimedean places of a number field.

The prerequisites are *Absolute values, valuations and Ostrowski's theorem* and [*Real Analysis I*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10). We assume the absolute-value axioms, the ultrametric inequality, and the elementary real-analysis facts about completeness and compactness. The precise algebraic facts used without proof are collected at the end. Basic references are [Milne] and [Sutherland]. The local arithmetic developed here also underlies the discussion of places in *Weil's proof for curves and what is missing over the integers*.

Write \(K_v\) for completion at a place \(v\), and \(\mathbb N=\{0,1,\ldots\}\). For a nonarchimedean absolute value, its valuation ring and residue field are

\[
\mathcal O=\{x:|x|\le1\},\qquad
\mathfrak m=\{x:|x|<1\},\qquad
\kappa=\mathcal O/\mathfrak m.
\]

An additive discrete valuation is normalized to have image \(\mathbb Z\), and \(v(0)=+\infty\). A uniformizer \(\pi\) has \(v(\pi)=1\). Thus \(|x|=c^{v(x)}\) for a fixed \(0<c<1\).

## Completing a field

A sequence \((a_n)\) is *Cauchy* if for every \(\varepsilon>0\), eventually \(|a_n-a_m|<\varepsilon\) for all \(n,m\). It is *null* if \(|a_n|\to0\). Completion identifies two Cauchy sequences when their difference is null.

**Theorem 2.1 (completion).** Every field \(K\) with an absolute value admits a complete valued field \(\widehat K\) containing \(K\) isometrically and densely. Every isometric field embedding from \(K\) to a complete valued field extends uniquely to an isometric embedding from \(\widehat K\). Consequently two completions have a unique isometric field isomorphism that respects their embeddings of \(K\).

If the absolute value is nonarchimedean, so is its extension, and

\[
|\widehat K^{\times}|=|K^{\times}|,
\qquad \kappa\xrightarrow{\sim}\widehat\kappa.
\]

Here \(\widehat\kappa\) denotes the residue field of \(\widehat K\). There is no discreteness hypothesis in these last assertions.

**Proof.** Every Cauchy sequence is bounded: its tail lies within distance \(1\) of a fixed term, and its initial segment is finite. Let \(C\) be the ring of Cauchy sequences, with coordinatewise operations. The estimate

\[
|a_nb_n-a_mb_m|
\le |a_n|\,|b_n-b_m|+|b_m|\,|a_n-a_m|
\]

shows that products are Cauchy. Boundedness also shows that the null sequences form an ideal \(N\). Set \(\widehat K=C/N\).

The reverse triangle inequality makes \((|a_n|)\) a Cauchy sequence of real numbers. Define

\[
|[(a_n)]|=\lim_n|a_n|.
\]

This is independent of the representative. It vanishes exactly on \(N\); multiplication and the triangle inequality pass to limits. If the class is nonzero, \(|a_n|\) is eventually bounded below by a positive number. On that tail,

\[
|a_n^{-1}-a_m^{-1}|=\frac{|a_n-a_m|}{|a_n|\,|a_m|}.
\]

Hence the reciprocal sequence, with arbitrary initial terms, defines an inverse. Thus \(\widehat K\) is a field. Constant sequences embed \(K\) isometrically.

For \(A=[(a_n)]\), the elements \(a_n\in K\) converge to \(A\): the Cauchy condition bounds \(\lim_m|a_m-a_n|\) by any prescribed positive tolerance for large \(n\). This proves density.

Now let \((A_j)\) be Cauchy in \(\widehat K\). Choose \(b_j\in K\) with \(|A_j-b_j|<1/j\). The triangle inequality shows that \((b_j)\) is Cauchy in \(K\). Its class \(B\) satisfies \(b_j\to B\), so \(A_j\to B\) as well. This proves completeness.

If \(f:K\to L\) is isometric and \(L\) is complete, send \([(a_n)]\) to \(\lim_n f(a_n)\). Equivalent sequences give the same limit; addition, multiplication and absolute values commute with this operation. Density makes this the only isometric extension. Applying the construction in both directions between two completions gives inverse maps.

In the nonarchimedean case the ultrametric inequality passes to limits. If \(x\in\widehat K\) is nonzero, choose \(a\in K\) with \(|x-a|<|x|\). The strict-dominance rule for an ultrametric gives \(|a|=|x|\), proving equality of value sets. This argument also shows that the valuation ring \(\widehat{\mathcal O}\) is the closure of \(\mathcal O\): approximations sufficiently close to an integral element remain integral, and the valuation ring is closed. To represent the residue of \(x\in\widehat{\mathcal O}\), approximate it by \(a\in K\) with \(|x-a|<1\). Then \(a\in\mathcal O\) and the residues agree. The kernel of the induced residue map is exactly \(\mathfrak m\). ∎

Uniqueness here includes the embedding of the original field. It does not say that the completed field has no other automorphisms. A trivially valued field is already complete, since every Cauchy sequence is eventually constant.

## Congruences as p-adic accuracy

Fix a prime \(p\). The field \(\mathbb Q_p\) is the completion of \(\mathbb Q\) for \(|x|_p=p^{-v_p(x)}\). Define

\[
\mathbb Z_p=\{x\in\mathbb Q_p:v_p(x)\ge0\}.
\]

Theorem 2.1 extends \(v_p\) with the same integer value group and residue field \(\mathbb F_p\). In particular,

\[
x\equiv y\pmod{p^n\mathbb Z_p}
\quad\Longleftrightarrow\quad |x-y|_p\le p^{-n}.
\]

An *inverse limit* of the rings \(\mathbb Z/p^n\mathbb Z\) consists of compatible residues:

\[
\varprojlim_{n\ge1}\mathbb Z/p^n\mathbb Z
=\{(r_n):r_{n+1}\bmod p^n=r_n\}.
\]

Operations are coordinatewise. Each quotient is given the discrete topology, and the limit has the subspace topology from their product. Specifying a residue modulo \(p^n\) specifies an open neighborhood.

**Proposition 2.2.** The closure of \(\mathbb Z\) in \(\mathbb Q_p\) is \(\mathbb Z_p\). Reduction gives an isomorphism of topological rings

\[
\mathbb Z_p\xrightarrow{\sim}
\varprojlim_{n\ge1}\mathbb Z/p^n\mathbb Z.
\]

The ring \(\mathbb Z_p\) is compact. The field \(\mathbb Q_p\) is locally compact and totally disconnected.

**Proof.** By Theorem 2.1, \(\mathbb Z_p\) is the closure of \(\mathbb Z_{(p)}=\{a/b\mid p\nmid b\}\). For every \(a/b\in\mathbb Z_{(p)}\) and \(n\ge1\), choose an integer \(c\) such that \(bc\equiv a\pmod{p^n}\). Then \(|a/b-c|_p\le p^{-n}\). Thus \(\mathbb Z\) has the same closure.

Density shows that every coset modulo \(p^n\mathbb Z_p\) contains an integer. An integer belongs to this ideal exactly when it is divisible by \(p^n\), so

\[
\mathbb Z_p/p^n\mathbb Z_p\simeq\mathbb Z/p^n\mathbb Z.
\]

The resulting map to the inverse limit is injective, because a nonzero element has a finite valuation. For a compatible family \((r_n)\), take its integer representatives \(0\le c_n<p^n\). Compatibility gives \(|c_m-c_n|_p\le p^{-n}\) when \(m\ge n\). Their limit lies in \(\mathbb Z_p\) and has all the prescribed residues. This proves surjectivity. The fibers of reduction modulo \(p^n\) are the cosets of \(p^n\mathbb Z_p\), which form a neighborhood basis. Thus both directions are continuous.

Compatibility also gives unique digits \(a_i\in\{0,\ldots,p-1\}\) with

\[
c_n=\sum_{i=0}^{n-1}a_ip^i,
\qquad x=\sum_{i\ge0}a_ip^i.
\]

A cylinder fixing the first \(n\) digits is a coset modulo \(p^n\); it has exactly \(p\) children fixing one more digit. To prove compactness directly, suppose an open cover has no finite subcover. Starting with the whole space, repeatedly choose a child cylinder with no finite subcover. The chosen compatible digits define a point \(x\). An open member of the cover containing \(x\) contains a sufficiently long cylinder in this chain, a contradiction.

The cosets \(a+p^n\mathbb Z_p\), for \(a\in\mathbb Q_p\) and \(n\in\mathbb Z\), are open and closed: small changes preserve membership, and the same holds for their complements. They are also compact, by translation and multiplication by \(p^n\). This proves local compactness. Given distinct points, choose such a coset containing one and excluding the other. Its intersection with any connected set separates those points, so every connected subset is a singleton. ∎

The whole field is not compact: the increasing open cover \(\mathbb Q_p=\bigcup_{m\ge0}p^{-m}\mathbb Z_p\) has no finite subcover. Compactness of the ring and local compactness of the field are different assertions.

## Digits in any complete discrete valuation

Let \(K\) be complete for a normalized discrete valuation \(v\), with ring \(\mathcal O\), residue field \(\kappa\), and uniformizer \(\pi\). Choose a set \(R\subset\mathcal O\) containing exactly one representative of each residue class, including \(0\). These representatives need not form a subring.

**Proposition 2.3 (expansions and series).** Every nonzero \(x\in K\) has a unique expansion

\[
x=\sum_{i\ge m}a_i\pi^i,
\qquad m=v(x),\quad a_i\in R,\quad a_m\ne0.
\]

Zero has the all-zero expansion. Allowing leading zero digits does not change the element, so the starting index is unique only with the stated normalization. A series \(\sum_{n\ge0}x_n\) in \(K\) converges if and only if \(x_n\to0\). Moreover,

\[
\mathcal O\xrightarrow{\sim}\varprojlim_{n\ge1}\mathcal O/\pi^n\mathcal O
\]

is an isomorphism of topological rings, with discrete quotients.

**Proof.** Necessity for series follows by subtracting consecutive partial sums. For sufficiency, the ultrametric inequality gives

\[
\left|\sum_{n=r}^{s}x_n\right|\le\max_{r\le n\le s}|x_n|.
\]

If the terms tend to zero, the partial sums are Cauchy and therefore converge. This argument actually works in every complete nonarchimedean field.

For \(y\in\mathcal O\), define \(y_0=y\). Choose \(a_j\in R\) representing \(y_j\bmod\pi\), and set

\[
y_{j+1}=\frac{y_j-a_j}{\pi}\in\mathcal O.
\]

Then

\[
y=\sum_{j=0}^{N-1}a_j\pi^j+\pi^Ny_N.
\]

The remainder has absolute value at most \(c^N\), so it tends to zero. For nonzero \(x\), apply this to \(y=\pi^{-v(x)}x\), a unit; its first digit is nonzero. Every prescribed digit sequence converges because \(|a_i\pi^i|\le c^i\).

If two expansions first differ at index \(j\), the difference of their digits at \(j\) is a unit: distinct representatives have distinct residues. The remaining tail has valuation at least \(j+1\). Thus the difference of the expansions has valuation exactly \(j\), proving uniqueness.

For the inverse limit, the kernel is \(\bigcap_n\pi^n\mathcal O=0\). Lift a compatible family of residues to elements \(b_n\in\mathcal O\). Then \(b_m-b_n\in\pi^n\mathcal O\) for \(m\ge n\), so they converge. The limit has each prescribed residue, since \(\pi^n\mathcal O\) is closed. The same cosets are basic neighborhoods on both sides, proving the topological assertion. ∎

The first \(N\) digits determine an integral element modulo \(\pi^N\). This is the useful meaning of truncation. Addition and multiplication may require carrying because \(R\) need not respect either operation. In mixed characteristic there is no reason for \(\kappa\) itself to embed as a coefficient field.

The ring \(\mathcal O\) is a DVR: its units have valuation zero, and in a nonzero ideal choose an element with least valuation. That element generates the ideal, since division by it leaves every other element in \(\mathcal O\). Its maximal ideal is \(\pi\mathcal O\). If \(\kappa\) is finite, the finite-cylinder argument of Proposition 2.2 proves that \(\mathcal O\) is compact and \(K\) is locally compact.

## Three computations

**Negative one.** For every prime \(p\),

\[
\sum_{i=0}^{N-1}(p-1)p^i=p^N-1.
\]

Since \(p^N\to0\) p-adically,

\[
-1=\sum_{i\ge0}(p-1)p^i.
\]

There is no conflict with the growth of the ordinary integer partial sums: the metric has changed.

**One third in \(\mathbb Q_5\).** Successive digit extraction gives

| Current remainder \(y_j\) | Digit \(a_j\) modulo \(5\) | Next remainder \((y_j-a_j)/5\) |
|---|---:|---|
| \(1/3\) | \(2\) | \(-1/3\) |
| \(-1/3\) | \(3\) | \(-2/3\) |
| \(-2/3\) | \(1\) | \(-1/3\) |

The last two rows repeat. Thus, in increasing order of powers,

\[
\frac13=2+3\cdot5+5^2+3\cdot5^3+5^4+\cdots
=2+\sum_{j\ge0}(3\cdot5^{2j+1}+5^{2j+2}).
\]

As a check, the repeated block sums to \((15+25)/(1-25)=-5/3\), so the total is \(1/3\). The geometric series converges because \(|25|_5<1\).

**Laurent series.** For \(k=\mathbb F_q\), let \(k((t))\) consist of sums \(\sum_{i\ge m}a_it^i\) with \(a_i\in k\) and only finitely many negative powers. Addition and convolution multiplication are well defined: each coefficient of a product involves finitely many pairs. A nonzero series is \(a_mt^m(1+h)\), with \(h\in tk[[t]]\), and its inverse is

\[
a_m^{-1}t^{-m}\sum_{j\ge0}(-h)^j.
\]

Each coefficient of this expression stabilizes, and multiplication verifies the inverse. Thus these series form a field. Put \(v_t(x)=\min\{i:a_i\ne0\}\) and \(|x|=q^{-v_t(x)}\).

A Cauchy sequence has a common lower bound on its exponents after discarding finitely many terms; closeness to a fixed term proves this. At each exponent its coefficient eventually stabilizes. The stabilized coefficients give a Laurent series, and the sequence converges to it because agreement below any fixed exponent is eventually exact. Hence \(k((t))\) is complete. Its Laurent-polynomial truncations lie in \(k(t)\) and are dense. By Theorem 2.1,

\[
\widehat{k(t)}_{\,t}=k((t)),\qquad \mathcal O=k[[t]],\qquad\kappa=k.
\]

Here the representatives really do form a coefficient field, so no carrying is needed.

## Completing a number field at a prime

Let \(K\) be a number field, \(A=\mathcal O_K\) its ring of algebraic integers, and \(\mathfrak p\) a nonzero prime ideal. We use the fact that \(A\) is Dedekind and \(B=A_{\mathfrak p}\) is a DVR [Milne, Theorem 3.29 and Proposition 3.6]. Their fraction field is \(K\): multiplying any element of \(K\) by an integer divisible by the denominators of its monic rational polynomial makes it integral. Complete \(K\) for the valuation of \(B\), obtaining \(K_{\mathfrak p}\), and write \(\mathcal O_{\mathfrak p}\) for its valuation ring.

By Theorem 2.1, \(B\) is dense in \(\mathcal O_{\mathfrak p}\), with the same uniformizer \(\pi\) and residue field. For every \(n\ge1\), approximation modulo \(\pi^n\) gives

\[
B/\pi^nB\simeq
\mathcal O_{\mathfrak p}/\pi^n\mathcal O_{\mathfrak p}.
\]

Injectivity follows from equality of the valuations on \(B\); surjectivity follows from density.

Also \(A/\mathfrak p^n\simeq B/\mathfrak p^nB\). Indeed, the only maximal ideal containing \(\mathfrak p^n\) is \(\mathfrak p\). Thus every \(s\notin\mathfrak p\) becomes a unit in \(A/\mathfrak p^n\), and localizing that quotient changes nothing. Since \(\mathfrak pB=\pi B\), Proposition 2.3 yields

\[
\mathcal O_{\mathfrak p}\simeq
\varprojlim_{n\ge1}A/\mathfrak p^n,
\qquad
K\text{ is dense in }K_{\mathfrak p}.
\]

The displayed ring isomorphism is topological when the quotients are discrete. In particular \(A\) itself is dense in \(\mathcal O_{\mathfrak p}\), since it represents every finite quotient.

Localization and completion are separate operations. The ring \(B\) is not complete: it is countable, whereas the distinct digit sequences using just two residue representatives already give uncountably many elements in its completion. The general algebraic result [Stacks, Tag 0AP1] says that a Noetherian local ring is a DVR exactly when its maximal-ideal completion is a DVR. It agrees with the direct valuation construction here.

## Why the archimedean possibilities stop at two

An absolute value is *archimedean* when it does not satisfy the ultrametric inequality. The prerequisite result that bounded absolute values of integers force the ultrametric inequality implies that an archimedean field has characteristic zero. Its absolute value on \(\mathbb Q\) is \(|q|_\infty^s\) for \(s>0\), by Ostrowski's theorem on absolute values of \(\mathbb Q\). Since \(|n|\le n\), necessarily \(s\le1\).

We first justify a polynomial fact used in the proof. A nonconstant complex polynomial \(P\) satisfies \(|P(z)|_\infty\to\infty\) as \(|z|_\infty\to\infty\), so its modulus has a minimum at some \(z_0\). If \(P(z_0)\ne0\), write

\[
\frac{P(z_0+w)}{P(z_0)}=1+cw^k+O(|w|^{k+1}),\qquad c\ne0.
\]

Choose a unit complex number \(u\) with \(cu^k=-|c|_\infty\), and put \(w=ru\). For small positive \(r\), the modulus is at most \(1-|c|_\infty r^k+Cr^{k+1}<1\), contradicting minimality. Thus \(P\) has a root. Division and induction show that every complex polynomial factors into linear factors, counted with multiplicity. This proves the needed form of the fundamental theorem of algebra.

**Theorem 2.4 (Ostrowski's theorem on complete archimedean fields).** If a field \(K\) is complete for an archimedean absolute value, there is a field isomorphism \(\sigma:K\to\mathbb R\) or \(\sigma:K\to\mathbb C\) such that

\[
|x|=|\sigma(x)|_\infty^s\qquad(0<s\le1).
\]

Thus it is an isometry to the indicated field with that powered absolute value, and a topological field isomorphism to the field with its usual absolute value.

*Reference:* [Milne, Remark 7.49].

**Proof.** Normalize by setting \(\|x\|=|x|^{1/s}\). It is necessary to check the triangle inequality after taking this power. The binomial expansion, together with \(|n|=n^s\), gives for positive integers \(N\)

\[
|x+y|^N
\le\sum_{j=0}^{N}\binom Nj^s\|x\|^{sj}\|y\|^{s(N-j)}
\le(N+1)(\|x\|+\|y\|)^{sN}.
\]

Taking \(sN\)-th roots and letting \(N\to\infty\) proves the claim. The normalized absolute value has the same Cauchy sequences and agrees with the usual one on \(\mathbb Q\). Its closure in \(K\) is complete: a Cauchy sequence there converges in \(K\), and closedness keeps the limit there. Uniqueness of completion therefore embeds \(\mathbb R\) isometrically in \(K\).

Fix \(x\in K\). For \(z\in\mathbb C\), where \(\mathbb C\) is for now only a parameter space, put

\[
Q_z(T)=T^2-2\operatorname{Re}(z)T+|z|_\infty^2,
\qquad F(z)=\|Q_z(x)\|.
\]

Only real coefficients are evaluated in \(K\). If \(M=\|x\|\), the reverse triangle inequality gives

\[
F(z)\ge |z|_\infty^2-2|z|_\infty M-M^2.
\]

Thus \(F\) tends to infinity at infinity and attains a minimum \(m\). Among its minimizers choose \(z_0\) with maximal modulus. Suppose \(m>0\), choose \(0<\varepsilon<m\), and put \(Q=Q_{z_0}\). The roots \(z_1,\overline{z_1}\) of \(Q(T)+\varepsilon\) are nonreal conjugates, with

\[
|z_1|_\infty^2=|z_0|_\infty^2+\varepsilon.
\]

Consequently \(F(z_1)>m\).

For each \(n\ge1\), factor the real polynomial

\[
H_n(T)=Q(T)^n-(-\varepsilon)^n
=\prod_{j=1}^{2n}(T-\alpha_j),
\]

listing \(\alpha_1=z_1\). Its conjugate factorization gives the real-polynomial identity

\[
H_n(T)^2=\prod_{j=1}^{2n}Q_{\alpha_j}(T).
\]

Evaluation in \(K\), multiplicativity, and minimality yield

\[
F(z_1)m^{2n-1}
\le\|H_n(x)\|^2
\le(m^n+\varepsilon^n)^2.
\]

Hence \(F(z_1)/m\le(1+(\varepsilon/m)^n)^2\). Letting \(n\to\infty\) contradicts \(F(z_1)>m\). Therefore \(m=0\), and every element of \(K\) satisfies a monic real quadratic equation.

If \(K=\mathbb R\), we are done. Otherwise choose \(x\notin\mathbb R\). Its quadratic is irreducible over \(\mathbb R\), since a split quadratic would force \(x\) to be one of its real roots. Completing the square gives \(j\in K\) with \(j^2=-1\), embedding \(\mathbb C=\mathbb R(j)\). Every real quadratic now splits inside this subfield, so every element of \(K\) belongs to it. Thus \(K=\mathbb C\).

Finally, for \(z=a+bj\) we have \(\|j\|=1\), so

\[
\|z\|\le |a|_\infty+|b|_\infty\le\sqrt2\,|z|_\infty.
\]

Apply this to \(z^n\) and take \(n\)-th roots to get \(\|z\|\le|z|_\infty\). Applying it to \(z^{-1}\) proves the reverse inequality. Undoing the normalization proves the theorem. ∎

This theorem concerns complete fields, whereas the earlier Ostrowski theorem concerns absolute values on \(\mathbb Q\). Completeness is essential: \(\mathbb Q\) with its usual absolute value is archimedean but is neither of the two fields in the conclusion.

## Archimedean places of a number field

**Corollary 2.5.** For a number field \(K\), the archimedean places correspond bijectively to its real embeddings and its pairs of conjugate nonreal embeddings into \(\mathbb C\). Their completions are respectively \(\mathbb R\) and \(\mathbb C\). If the counts are \(r_1\) and \(r_2\), there are \(r_1+r_2\) archimedean places, and \([K:\mathbb Q]=r_1+2r_2\).

**Proof.** An embedding \(\sigma\) gives the absolute value \(|\sigma(x)|_\infty\). If its image is real, its closure is \(\mathbb R\), since it contains \(\mathbb Q\). If the image contains a nonreal \(\alpha\), it contains \(\mathbb Q+\mathbb Q\alpha\), dense in \(\mathbb C\): the real-linear map \((u,v)\mapsto u+v\alpha\) is an isomorphism \(\mathbb R^2\to\mathbb C\). These closures are the completions.

Conversely, Theorem 2.4 identifies any archimedean completion with one of these fields. Composing \(K\) with this identification gives an embedding whose usual absolute value represents the original place.

Suppose two embeddings give equivalent absolute values. Their restrictions to \(\mathbb Q\) are the same usual absolute value, so the exponent relating them is \(1\), as evaluation at \(2\) shows. The correspondence between their images therefore extends to an isometric isomorphism of their completions. Such a map fixes \(\mathbb Q\), hence \(\mathbb R\) by continuity. It cannot identify \(\mathbb R\) with \(\mathbb C\); on \(\mathbb C\) it sends \(i\) to \(i\) or \(-i\), so it is identity or conjugation. This proves the asserted bijection.

For the degree formula, express \(K\) as a finite tower adjoining algebraic generators. An embedding at each stage extends in precisely as many ways as the degree of the next minimal polynomial: its transformed polynomial splits in \(\mathbb C\), with distinct roots in characteristic zero. Multiplying these counts gives \([K:\mathbb Q]\) embeddings. Conjugation fixes exactly the real embeddings and pairs the others. ∎

For example, \(\mathbb Q(\sqrt6)\) has two real places and two real completions. The two embeddings of \(\mathbb Q(\sqrt{-6})\) form one conjugate pair, giving one complex place and completion. Distinct places can therefore have isomorphic completed fields.

## Exercises

Digits below are always in \(\{0,\ldots,p-1\}\), listed in increasing order of powers. A sequence is *eventually periodic* if \(a_{i+d}=a_i\) for some \(d\ge1\) and every sufficiently large \(i\).

**Exercise 1 (easy).** Compute the \(7\)-adic expansion of \(-1/6\) and prove that it is eventually periodic.

**Solution.** It is purely periodic:

\[
-\frac16=1+7+7^2+\cdots.
\]

The first \(N\) terms sum to \((7^N-1)/6\), whose difference from \(-1/6\) is \(7^N/6\), of valuation \(N\). The series converges to the claimed value, and uniqueness identifies every digit as \(1\).

**Exercise 2 (easy).** Prove \(\mathbb Z_p^{\times}=\mathbb Z_p\setminus p\mathbb Z_p\), and prove that \(\mathbb Z_p\) is a DVR with uniformizer \(p\).

**Solution.** A nonzero \(x\in\mathbb Z_p\) is invertible there exactly when \(v_p(x^{-1})=-v_p(x)\ge0\), which is equivalent to \(v_p(x)=0\). The remaining elements, including zero, form \(p\mathbb Z_p\). Thus this is the unique maximal ideal. In a nonzero ideal \(I\), choose \(x\) with the least valuation \(n\). Write \(x=p^nu\), with \(u\) a unit. For every \(y\in I\), \(y/p^n\in\mathbb Z_p\), so \(I=p^n\mathbb Z_p\). This proves that the ring is a local principal ideal domain, not a field, with uniformizer \(p\).

**Exercise 3 (medium).** Show that \(x\in\mathbb Q_p\) belongs to \(\mathbb Q\) exactly when its p-adic expansion is eventually periodic.

**Solution.** Multiplication by a power of \(p\) shifts finitely many indices, preserving both rationality and eventual periodicity. We may assume \(x\in\mathbb Z_p\).

If the tail starts at \(N\) and has period \(d\), put \(B_0=\sum_{j=0}^{d-1}a_{N+j}p^j\). Then

\[
x=\sum_{i<N}a_ip^i+\frac{p^NB_0}{1-p^d}\in\mathbb Q,
\]

by the convergent geometric series.

Conversely write \(x=A/B\), where \(A\in\mathbb Z\), \(B>0\), and \(p\nmid B\). Digit extraction has remainders \(A_i/B\), beginning with \(A_0=A\). The digit \(a_i\) is the unique member of \(\{0,\ldots,p-1\}\) congruent to \(A_iB^{-1}\pmod p\), and

\[
A_{i+1}=\frac{A_i-Ba_i}{p}\in\mathbb Z.
\]

For the ordinary absolute value,

\[
|A_{i+1}|_\infty\le\frac{|A_i|_\infty+B(p-1)}p.
\]

Thus all \(A_i\) lie in the finite integer interval \([-M,M]\), with \(M=\max(|A|_\infty,B)\). The next state and digit depend only on the current state. A state eventually repeats, after which the digits repeat. This includes a terminating expansion, whose tail consists of zeros.

**Exercise 4 (medium).** Show that \(\mathbb Z_p\) is homeomorphic to the middle-thirds Cantor set, for every prime \(p\).

**Solution.** Its digit map identifies \(\mathbb Z_p\) with \(D^{\mathbb N}\), where \(D=\{0,\ldots,p-1\}\) is discrete: agreeing on the first \(n\) coordinates means agreement modulo \(p^n\). To identify this with binary sequences, use the prefix code

\[
0,\ 10,\ 110,\ \ldots,\ 1^{p-2}0,\ 1^{p-1}
\]

for the \(p\) symbols, in order. For \(p=2\) it is just \(0,1\). Concatenation gives a binary sequence. Decoding is unique: read to the first zero, or stop after \(p-1\) ones, and repeat. Every infinite binary sequence decodes this way, so the map is bijective. Code lengths are between \(1\) and \(p-1\); hence agreement on \(n\) input symbols forces agreement on at least \(n\) bits, and agreement on \((p-1)n\) bits forces agreement on \(n\) decoded symbols. Both maps are continuous.

Finally send \((b_i)\in\{0,1\}^{\mathbb N}\) to

\[
\sum_{i\ge0}\frac{2b_i}{3^{i+1}}.
\]

The two choices at each stage select the left or right third of the remaining closed interval. Nested intervals have lengths tending to zero, giving exactly all points of the Cantor set. If sequences first differ at \(j\), their values differ by at least \(3^{-(j+1)}\), since the possible later tail cancels at most half the leading difference. Agreement on a long prefix bounds the difference above by the length of its interval. These bounds prove injectivity and continuity in both directions. Composing gives the desired homeomorphism. This concerns topology; the coding does not identify ring operations with ordinary real operations.

**Exercise 5 (hard).** Prove Theorem 2.4 by minimizing

\[
(t,u)\longmapsto\|x^2-tx+u\|
\]

over the whole real plane. Supply both the existence of a minimum and the argument forcing it to be zero.

**Solution.** Use the normalization and embedded \(\mathbb R\) established at the start of the theorem's proof. If \(x\in\mathbb R\), a quadratic vanishing at \(x\) is immediate. Suppose \(x\notin\mathbb R\). On the Euclidean unit circle the continuous function \((t,u)\mapsto\|tx-u\|\) is everywhere positive, since \(1,x\) are real-linearly independent. It has a positive minimum \(c_0\). Homogeneity implies

\[
\|tx-u\|\ge c_0\sqrt{t^2+u^2},
\qquad
\|x^2-tx+u\|\ge c_0\sqrt{t^2+u^2}-\|x^2\|.
\]

Thus the latter function is coercive. Its minimizers form a nonempty compact set. Choose \((t_0,u_0)\) maximizing \(u\) among them, and put \(Q(T)=T^2-t_0T+u_0\), \(m=\|Q(x)\|\).

Assume \(m>0\) and choose \(0<\varepsilon<m\). The roots \(\alpha,\beta\) of \(Q+\varepsilon\) are either real or conjugate. If conjugate, both have squared modulus \(u_0+\varepsilon>u_0\). If real, at least one has squared modulus at least \(|\alpha\beta|=|u_0+\varepsilon|>u_0\). Choose such a root \(\alpha\), and define \(Q_\alpha(T)=T^2-2\operatorname{Re}(\alpha)T+|\alpha|_\infty^2\). Its constant coefficient is larger than \(u_0\), so maximality gives \(\|Q_\alpha(x)\|>m\).

Factor \(H_n=Q^n-(-\varepsilon)^n\), with \(\alpha\) among its \(2n\) roots. The identity \(H_n^2=\prod_jQ_{\alpha_j}\) is valid because \(H_n\) has real coefficients. Every factor evaluated at \(x\) has norm at least \(m\), since the minimum was taken over all real quadratic coefficients. Hence

\[
\frac{\|Q_\alpha(x)\|}{m}
\le\left(1+\left(\frac\varepsilon m\right)^n\right)^2.
\]

Letting \(n\to\infty\) is a contradiction. Thus \(m=0\), and every \(x\) satisfies a real quadratic. The last two paragraphs of the theorem's proof then identify the field and its absolute value. This argument also explains why merely asserting that a continuous function on \(\mathbb R^2\) has a minimum would be insufficient: coercivity needs proof.

## Source comparison for this edition

Milne, Chapter 7, Theorem 7.23, Lemma 7.25 and Proposition 7.26, and Sutherland, Lecture 8, Propositions 8.11 and 8.17, treat the completion, residue and digit constructions. The Cauchy-sequence construction in Theorem 2.1 applies to an arbitrary ordinary absolute value; discreteness is imposed only when a uniformizer and integer-indexed digits are introduced. In particular, completion does not make a nondiscrete valuation discrete.

For the complete archimedean classification, Theorem 2.4 gives the real-polynomial factorization argument, and Exercise 5 gives the quadratic minimization alternative with the needed coercivity estimate on the whole plane. Both use the stated real-analysis prerequisites and the normalization check for a power of an absolute value. Milne, Remark 7.49, states the classification and sketches a further proof.

## What this lesson does not prove

- The prerequisite real-analysis foundations: completeness of \(\mathbb R\), compactness of closed bounded Euclidean sets, and the extreme-value theorem. These are the facts from *Real Analysis I* used in the minimization arguments. The polynomial factorization needed here was proved above.
- The criterion that an absolute value is nonarchimedean exactly when its values on integers are bounded, and the consequent characteristic-zero assertion for archimedean fields [Milne, Proposition 7.2 and Corollary 7.3].
- Ostrowski's classification of nontrivial absolute values on \(\mathbb Q\) [Milne, Theorem 7.12], and the equivalence criterion that two nontrivial absolute values give the same topology exactly when one is a positive power of the other [Milne, Proposition 7.8]. These belong to *Absolute values, valuations and Ostrowski's theorem*.
- For a Dedekind domain \(A\), its integral closure in a finite separable extension of its fraction field is Dedekind [Milne, Theorem 3.29]; every localization of \(A\) at a nonzero prime is a DVR [Milne, Proposition 3.6]. We use the first assertion for \(A=\mathbb Z\).
- For a Noetherian local ring \(A\), \(A\) is a DVR if and only if its maximal-ideal completion is a DVR [Stacks, Tag 0AP1]. This is a comparison with the more general algebraic theorem; the valued-field and DVR constructions needed in the lesson were proved directly.

Hensel's lemma and the classification of nonarchimedean local fields are developed in *Hensel's lemma, squares and roots of unity in p-adic fields* and *Local fields: classification and Haar measure*.

The written ring-theoretic providers are *Number fields*, lesson 3, [**Discrete valuation rings and Dedekind domains**](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ANT/discrete-valuation-rings-and-dedekind-domains.html), its local characterizations and Proposition 3.1, and lesson 5, [**Decomposition of primes in extensions**](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ANT/decomposition-of-primes-in-extensions.html), Theorem 5.1 for finite integral closure over an arbitrary Dedekind base in a finite separable field extension. The integer-bound criterion, equivalence criterion and rational classification are Proposition 1.1, Proposition 3.1 and Theorem 4.1 of **Absolute values, valuations and Ostrowski's theorem**; the references below credit the classical treatments.

## References

- [Milne] J. S. Milne, *Algebraic Number Theory*, version 3.08 (2020), especially Chapter 7, “Completions” and “Completions in the nonarchimedean case.” [Open lecture notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. The linked text of [Tag 0AP1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-completion-dvr) is in the AI Integrated Stacks Project, an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks project's maintainers.
- [Sutherland] A. V. Sutherland, *Complete fields and valuation rings*, MIT 18.785 Number Theory I, Fall 2021, Lecture 8, sections “Completions” and “Valuation rings in complete fields.” [Lecture notes](https://math.mit.edu/classes/18.785/2021fa/LectureNotes8.pdf).
