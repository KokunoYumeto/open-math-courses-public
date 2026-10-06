# The projective line over F_1 and the ABC conjecture

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Public domain (CC0).*

## Introduction

Let \(X\) be a curve over a perfect field and \(f\) a nonconstant rational function on \(X\). Then \(f\) is a map
from \(X\) to the projective line. If \(f\) is separable, the Riemann–Hurwitz formula bounds its ramification: the sum
of the numbers \((e_P-1)\deg P\) over any set of points \(P\) is at most \(2\deg f+2g-2\), where \(e_P\) is the
ramification index and \(g\) the genus of \(X\). When \(X\) is the projective line itself, this bound is the theorem
of Mason and Stothers, the ABC theorem for polynomials.

The field \(\mathbb Q\) resembles the function field of a curve. Its places, the primes and \(\infty\), play the role
of the points, and the product formula says that a principal divisor has degree zero. [Smirnov 1992] asks for the
Hurwitz inequality in this setting. Two things are missing: a field of constants, and the projective line over it.
Smirnov defines by hand a set that stands for the projective line over the field with one element. For every rational
number \(q\ne0,\pm1\), Smirnov defines a map \(\tau_q\) from the places of \(\mathbb Q\) to this set, with ramification
indices and defects, states a Hurwitz inequality for \(\tau_q\) as a conjecture, and proves that it implies the ABC
conjecture. This lesson gives these definitions with their reasons and proves what can be proved about them. It then
presents the account of the same objects in monoid geometry, which is due to [Jarra 2023b].

The lesson proves the following.

1. The Riemann–Hurwitz formula for a separable map from a curve to the projective line, the Hurwitz inequality, and
   the theorem of Mason and Stothers, with two proofs (Section 1).
2. The places of \(\mathbb Q\) form an "arithmetic curve": a principal divisor has degree zero, the constants are
   \(0,1,-1\), and the degree of a rational number is its logarithmic height (Section 2).
3. The closed points of the projective line over a finite field are \(0\), \(\infty\) and the Frobenius orbits of
   roots of unity. This is the reason for Smirnov's definition: the points of the projective line over
   \(\mathbb F_1\) are \([0]\), \([\infty]\) and one point \([n]\) of degree \(\varphi(n)\) for every \(n\ge1\)
   (Section 3).
4. For the map \(\tau_q\): every fibre is finite; the fibres over \([0]\) and \([\infty]\) have degree exactly
   \(\deg\tau_q\); the fibre over \([n]\) has degree \(\log\lvert\Phi_n(a,b)\rvert\) minus an explicit correction,
   where \(q=a/b\) and \(\Phi_n\) is the cyclotomic polynomial, and this is \(\varphi(n)\deg\tau_q\) up to an explicit
   error term; the empty fibres are determined by the theorem of Zsigmondy, which is proved (Section 4).
5. The sum of the defects over the points of degree one has a closed formula (Proposition 5.2). With it, Smirnov's
   conjecture for \(\mathbb Q\) becomes an inequality between integers. The conjecture implies the ABC conjecture
   (Smirnov's theorem, with all constants), the ABC conjecture implies the conjecture, and the inequality fails if the
   term \(\varepsilon\) is left out. A stronger conjecture of Smirnov, in which the remainder is a function of the
   real number \(q\), does not hold; with a function of \(\deg\tau_q\) in its place it is the conjecture again
   (Section 5).
6. The set of places with one more point is a monoidal space \(\overline{\operatorname{Spec}\mathbb Z}\) whose monoid
   of global sections is \(\{0,1,-1\}\). Smirnov's projective line is the set of non-generic points of the strong
   congruence space of the monoid scheme \(\mathbb P^1_{\mathbb F_1}\), and \(\tau_q\) extends to a continuous map
   between these spaces. For the extensions \(\mathbb F_{1^n}\) the lesson classifies the points of the corresponding
   space and determines when it is a quotient of the projective line over \(\mathbb F_{1^\infty}\) by a Galois group
   (Section 6).

Section 7 says what is proved and what is open. Section 8 contains exercises with solutions.

**What is assumed.** Curves over a field, their differentials and the degree of the canonical divisor, as in the
lesson *Weil's proof for curves and what is missing over the integers*; the facts used are listed in Section 1. From
the same lesson: the places of \(\mathbb Q\) and the product formula. From *Commutative monoids and their spectra*:
monoids, prime ideals, congruences. From *Monoid schemes*: monoidal spaces, morphisms to an affine monoid scheme, and
the projective line \(\mathbb P^1_{\mathbb F_1}\). Each of these is restated where it is used. The lesson also uses
cyclotomic fields: for a primitive \(n\)-th root of unity \(\zeta\), the field \(\mathbb Q(\zeta)\) has degree
\(\varphi(n)\) over \(\mathbb Q\), so its Galois group is \((\mathbb Z/n)^\times\) and acts transitively on the
primitive \(n\)-th roots of unity [Milne 2020, Theorem 6.4].

Basic references are [Smirnov 1992], [Jarra 2023b], [Le Bruyn 2016] and [Lorscheid 2018b]. The thesis
[Jarra 2024, Chapter 2] contains the text of [Jarra 2023b].

**Conventions.** \(\log\) is the natural logarithm and \(\varphi\) is Euler's function. For a nonzero integer \(N\),
\(\operatorname{rad}(N)\) is the product of the primes that divide \(N\); so \(\operatorname{rad}(\pm1)=1\). For a
prime \(p\), \(v_p\) is the \(p\)-adic valuation on \(\mathbb Q\). For \(n\ge2\), \(P(n)\) is the largest prime factor
of \(n\). A rational number \(q\ne0\) is written \(q=a/b\) *in lowest terms*: \(a,b\) are coprime integers and
\(b\ge1\). A *monoid* is a commutative monoid, written multiplicatively, with a unit \(1\) and an absorbing element
\(0\); \((R,\cdot)\) is the multiplicative monoid of a ring \(R\); \(\mathbb F_1=\{0,1\}\). Roots of unity are taken in
\(\mathbb C\): \(\mu_n\) is the group of \(n\)-th roots of unity, \(\mu_\infty\) is the union of all \(\mu_n\), and
\(\mathbb F_{1^n}=\{0\}\cup\mu_n\), \(\mathbb F_{1^\infty}=\{0\}\cup\mu_\infty\).

## 1. The model: the Hurwitz inequality for a curve

A reference for this section is [Smirnov 1992, §1].

### 1.1 Setting and the facts that are used

Let \(k\) be a perfect field. As in *Weil's proof for curves and what is missing over the integers*, a *curve over*
\(k\) is a scheme \(X\) of dimension one that is smooth and projective over \(k\) and geometrically irreducible. Then
\(H^0(X,\mathcal O_X)=k\) [Stacks, Tag [0BUG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-proper-geometrically-reduced-global-sections)]. Let \(K\) be the function field of \(X\) and \(g\) its genus
[Stacks, Tag [0BY7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-definition-genus)]. A closed point \(P\) of \(X\) has a local ring \(\mathcal O_P\subset K\), a valuation \(v_P\) of
\(K\), a residue field \(\kappa(P)\), which is a finite extension of \(k\), and the degree
\(\deg P=[\kappa(P):k]\). A *uniformizer* at \(P\) is an element \(u\in K\) with \(v_P(u)=1\).

The projective line \(\mathbb P^1_k\) has the coordinate \(t\). Its closed points are \(\infty\) and the points
\(Q_\pi\) given by the monic irreducible polynomials \(\pi\in k[t]\), with \(\deg Q_\pi=\deg\pi\) and
\(\deg\infty=1\). We fix the uniformizers \(s_Q=\pi(t)\) at \(Q=Q_\pi\) and \(s_\infty=1/t\) at \(\infty\).

Let \(f\in K\) be nonconstant, that is \(f\notin k\). It defines a morphism \(f\colon X\to\mathbb P^1_k\) under which
\(t\) pulls back to \(f\) [Stacks, Tag [0BY1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-theorem-curves-rational-maps)]. The *degree* of \(f\) is \(\deg f=[K:k(f)]\). Let \(P\) be a closed
point of \(X\). If \(v_P(f)<0\), then \(f(P)=\infty\). Otherwise \(f\in\mathcal O_P\), and \(f(P)=Q_\pi\), where
\(\pi\) is the minimal polynomial over \(k\) of the residue class of \(f\) in \(\kappa(P)\). Write
\(f^{\ast}s_Q\) for the pullback of the uniformizer at \(Q=f(P)\): it is \(\pi(f)\), respectively \(1/f\). The
*ramification index* of \(f\) at \(P\) is
\[
e_P=v_P(f^{\ast}s_Q)\ \ge1 .
\]
We call \(f\) *separable* if the field extension \(K/k(f)\) is separable. We use three facts.

- **(K1)** For every closed point \(Q\) of \(\mathbb P^1_k\),
  \(\sum_{f(P)=Q}e_P\deg P=\deg f\cdot\deg Q\) [Stacks, Tag [0AYZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-pullback-map-proper-curves)]. For \(Q=Q_t\) and \(Q=\infty\) this says that the
  divisor of zeros and the divisor of poles of \(f\) both have degree \(\deg f\).
- **(K2)** The differentials of \(K\) over \(k\) form a vector space \(\Omega_K\) of dimension one over \(K\). If
  \(u\) is a uniformizer at \(P\), then \(du\ne0\), and for every \(h\in\mathcal O_P\) we have \(dh=h'\,du\) with
  \(h'\in\mathcal O_P\). For \(\omega=h\,du\in\Omega_K\) put \(v_P(\omega)=v_P(h)\). This does not depend on \(u\):
  another uniformizer is \(uw\) with a unit \(w\) of \(\mathcal O_P\), and \(d(uw)=(w+uw')\,du\) with \(w+uw'\) a
  unit. If \(\omega\ne0\), then \(v_P(\omega)=0\) for all but finitely many \(P\), and
  \[
  \sum_Pv_P(\omega)\deg P=2g-2 .
  \]
  The sum is the degree of the sheaf of differentials [Stacks, Tag [0C1A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-smooth)]. The local description needs that
  \(\kappa(P)\) is separable over \(k\), which holds because \(k\) is perfect; compare the section on the
  Riemann–Hurwitz formula [Stacks, Tag [0C1B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-section-riemann-hurewitz)].
- **(K3)** \(f\) is separable if and only if \(df\ne0\) [Stacks, Tag [0C1C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-generically-etale)].

### 1.2 The Riemann–Hurwitz formula and the Hurwitz inequality

**Theorem 1.1 (Riemann–Hurwitz formula for a map to the line).** Let \(X\) be a curve of genus \(g\) over the perfect
field \(k\), and let \(f\in K\) be nonconstant and separable. For a closed point \(P\) of \(X\) with image \(Q=f(P)\)
put \(d_P=v_P\big(d(f^{\ast}s_Q)\big)\). This is an integer: the proof of (b) shows that \(d(f^{\ast}s_Q)\ne0\).

(a) \(d_P\ge e_P-1\), with equality if and only if the characteristic of \(k\) does not divide \(e_P\).

(b) \(d_P=0\) for all but finitely many \(P\), and
\[
2g-2=-2\deg f+\sum_Pd_P\deg P .
\]

*Proof.* (a) Let \(u\) be a uniformizer at \(P\) and \(e=e_P\). Then \(f^{\ast}s_Q=u^ew\) with a unit \(w\) of
\(\mathcal O_P\), and by (K2)
\[
d(u^ew)=(e\,w+u\,w')\,u^{e-1}\,du ,\qquad w'\in\mathcal O_P .
\]
So \(d_P=e-1+v_P(ew+uw')\ge e-1\). If the characteristic does not divide \(e\), then \(ew\) is a unit and \(uw'\) is
not, so \(ew+uw'\) is a unit and \(d_P=e-1\). If it divides \(e\), then \(ew=0\) and \(v_P(uw')\ge1\).

(b) By (K3), \(df\ne0\). We compare \(v_P(df)\) with \(d_P\).

Let \(f(P)=Q_\pi\). Then \(d(\pi(f))=\pi'(f)\,df\), where \(\pi'\) is the derivative of the polynomial \(\pi\). Since
\(k\) is perfect, \(\pi\) is separable, so there are \(A,B\in k[t]\) with \(A\pi+B\pi'=1\). Substituting \(f\) gives
\(A(f)\pi(f)+B(f)\pi'(f)=1\). Here \(A(f),B(f),\pi'(f)\in\mathcal O_P\) and \(v_P(\pi(f))\ge1\). So \(\pi'(f)\) is a
unit of \(\mathcal O_P\), and \(v_P(df)=d_P\).

Let \(f(P)=\infty\) and \(s=1/f\). Then \(df=-s^{-2}\,ds\), so \(v_P(df)=d_P-2e_P\).

By (K2), \(v_P(df)=0\) for all but finitely many \(P\), and only finitely many \(P\) lie over \(\infty\). So
\(d_P=0\) for all but finitely many \(P\), and
\[
2g-2=\sum_Pv_P(df)\deg P=\sum_Pd_P\deg P-2\sum_{f(P)=\infty}e_P\deg P=\sum_Pd_P\deg P-2\deg f
\]
by (K1) for \(Q=\infty\). \(\square\)

*Reference:* [Stacks, Tag [0C1D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-rh)] is the formula for a separable morphism between two curves.
[Smirnov 1992, formulas (1.1) to (1.4)] writes it in the form above.

**Corollary 1.2 (Hurwitz inequality).** In the situation of Theorem 1.1, for every set \(S\) of closed points of
\(X\),
\[
\sum_{P\in S}(e_P-1)\deg P\ \le\ 2g-2+2\deg f .
\]
If \(S\) is the set of all closed points, equality holds if and only if the characteristic of \(k\) divides no
\(e_P\).

*Proof.* All terms are \(\ge0\), and \(e_P-1\le d_P\). So the sum is at most \(\sum_Pd_P\deg P=2g-2+2\deg f\). The
statement about equality is Theorem 1.1(a). \(\square\)

**Corollary 1.3 (the fibres over a finite set).** In the situation of Theorem 1.1, let \(T\) be a finite set of closed
points of \(\mathbb P^1_k\), and put \(\deg T=\sum_{Q\in T}\deg Q\). Then
\[
\sum_{P\in f^{-1}(T)}\deg P\ \ge\ (\deg T-2)\deg f+2-2g .
\]

*Proof.* By (K1), \(\sum_{P\in f^{-1}(T)}e_P\deg P=\deg f\cdot\deg T\). Subtract the inequality of Corollary 1.2 for
\(S=f^{-1}(T)\). \(\square\)

So a map of large degree cannot have small fibres over three or more points of degree one. This is the content of the
Hurwitz inequality that the rest of the lesson imitates.

**Definition 1.4 (defects).** In the situation of Theorem 1.1, the *defect* of \(f\) at a closed point \(P\) of \(X\),
and at a closed point \(Q\) of \(\mathbb P^1_k\), is
\[
\delta_P=\frac{(e_P-1)\deg P}{\deg f},\qquad
\delta_Q=\sum_{f(P)=Q}\delta_P=\deg Q-\frac{1}{\deg f}\sum_{f(P)=Q}\deg P .
\]
The second expression for \(\delta_Q\) follows from (K1). So \(0\le\delta_Q<\deg Q\), and Corollary 1.2 reads
\[
\sum_{Q\in T}\delta_Q\ \le\ 2-\frac{\chi(X)}{\deg f},\qquad\chi(X)=2-2g, \tag{1.1}
\]
for every set \(T\) of closed points of \(\mathbb P^1_k\). *Reference:* [Smirnov 1992, §1.2 and §1.3], where
\(\delta_P\) is called the tame defect. The name "arithmetic defect" is used for its analogue over \(\mathbb Q\) in
[Le Bruyn 2016, Section 7] and [Jarra 2023b, Introduction].

### 1.3 The theorem of Mason and Stothers

For a nonzero polynomial \(F\) over a field \(k\) let \(n_0(F)\) be the number of distinct roots of \(F\) in an
algebraic closure of \(k\). If \(k\) is perfect, it is the degree of the product of the distinct monic irreducible
factors of \(F\).

**Theorem 1.5 (Mason, Stothers).** Let \(k\) be a field and let \(a,b,c\in k[t]\) satisfy \(a+b=c\) and
\(\gcd(a,b)=1\). Assume that the derivatives \(a',b',c'\) are not all zero. Then \(a,b,c\) are nonzero and
\[
\max(\deg a,\deg b,\deg c)\ \le\ n_0(abc)-1 .
\]

*Proof.* A common divisor of two of the polynomials \(a,b,c\) divides the third, so \(a,b,c\) are pairwise coprime.
If one of them were zero, the other two would be coprime and equal up to sign, hence constants, and all three
derivatives would vanish. So \(a,b,c\ne0\). Put
\[
W=ab'-a'b .
\]
Using \(a+b=c\) and \(a'+b'=c'\) we get \(W=a(c'-a')-a'(c-a)=ac'-a'c\) and \(W=(c-b)b'-(c'-b')b=cb'-c'b\).

*Step 1: \(W\ne0\).* Suppose \(W=0\). Then \(a\) divides \(a'b\), hence \(a\) divides \(a'\), and since
\(\deg a'<\deg a\) or \(a'=0\), we get \(a'=0\). In the same way \(b'=0\), and then \(c'=0\). This contradicts the
hypothesis.

*Step 2.* For \(F\in\{a,b,c\}\) let \(G_F=\gcd(F,F')\). The three expressions for \(W\) show that \(G_a\), \(G_b\) and
\(G_c\) divide \(W\). They are pairwise coprime, so their product divides \(W\), and
\[
\deg G_a+\deg G_b+\deg G_c\le\deg W .
\]
Over an algebraic closure, \(F\) is a constant times \(\prod_i(t-\alpha_i)^{m_i}\) with distinct \(\alpha_i\), and
\(\prod_i(t-\alpha_i)^{m_i-1}\) divides both \(F\) and \(F'\). The greatest common divisor does not change when the
field is enlarged. So \(\deg G_F\ge\sum_i(m_i-1)=\deg F-n_0(F)\). Since \(a,b,c\) are pairwise coprime,
\(n_0(a)+n_0(b)+n_0(c)=n_0(abc)\). Hence
\[
\deg a+\deg b+\deg c-n_0(abc)\le\deg W .
\]
*Step 3.* From \(W=ab'-a'b\) we get \(\deg W\le\deg a+\deg b-1\), and then \(\deg c\le n_0(abc)-1\). The other two
expressions for \(W\) give the same bound for \(\deg b\) and \(\deg a\). \(\square\)

*Reference:* due to Stothers and to Mason. [Oesterlé 1988, Section I.3, Théorème 2] states the theorem for an
arbitrary field, with the same hypothesis on the derivatives, and proves it with the determinant \(W\), as above.

*Second proof, from the Hurwitz inequality.* Neither the hypotheses nor the conclusion change when \(k\) is replaced
by an algebraic closure. So let \(k\) be algebraically closed. Let \(X=\mathbb P^1_k\) with coordinate \(t\), so
\(g=0\), and let \(f=a/c\in k(t)\). By Step 1 above, \(df=(a'c-ac')\,c^{-2}\,dt=-W\,c^{-2}\,dt\ne0\). So \(f\) is
nonconstant, and it is separable by (K3). The zeros of \(f\) are the roots of \(a\), with their multiplicities, and
the point \(\infty\) with multiplicity \(\deg c-\deg a\) if this number is positive. By (K1),
\[
\deg f=\deg a+\max(0,\deg c-\deg a)=\max(\deg a,\deg c)=\max(\deg a,\deg b,\deg c),
\]
because \(b=c-a\) has degree at most \(\max(\deg a,\deg c)\). Let \(T=\{0,1,\infty\}\). A point \(\alpha\in k\) of
\(X\) lies in \(f^{-1}(T)\) if and only if \(a(\alpha)=0\), or \(a(\alpha)=c(\alpha)\), or \(c(\alpha)=0\), that is,
if and only if \(\alpha\) is a root of \(abc\). So \(f^{-1}(T)\) has at most \(n_0(abc)+1\) points: the roots of
\(abc\), and possibly the point \(\infty\) of \(X\). By Corollary 1.3, \(f^{-1}(T)\) has at least \(\deg f+2\)
points. Hence \(\deg f+2\le n_0(abc)+1\). \(\square\)

In the second proof the theorem is the Hurwitz inequality for the three points \(0,1,\infty\): by Definition 1.4 it
says \(\delta_0+\delta_1+\delta_\infty\le2-2/\deg f\). Theorem 5.6 below is the same argument for \(\mathbb Q\).

**Examples 1.6.**

(a) *The bound is sharp.* Let \(n\ge1\) be prime to the characteristic of \(k\), and \(a=t^n\), \(b=1-t^n\), \(c=1\).
Then \(\max\deg=n\) and \(n_0(abc)=n+1\).

(b) *The hypothesis on the derivatives is needed.* Let \(k\) have characteristic \(p>0\), and \(a=t^p\),
\(b=1-t^p=(1-t)^p\), \(c=1\). Then \(a'=b'=c'=0\), \(\max\deg=p\) and \(n_0(abc)=2\). The bound fails.

(c) *Defects.* For \(a=t^n\), \(c=1\) as in (a), the map \(f=t^n\) has \(e=n\) at the points \(0\) and \(\infty\) and
\(e=1\) at the \(n\) points over \(1\). So \(\delta_0=\delta_\infty=1-1/n\) and \(\delta_1=0\), and (1.1) is an
equality: \(2-2/n\).

## 2. The arithmetic curve

A reference for this section is [Smirnov 1992, §2.1, §2.2 and §2.6].

A *place* of \(\mathbb Q\) is an equivalence class of nontrivial absolute values. By Ostrowski's theorem, which is
proved in *Weil's proof for curves and what is missing over the integers*, the places of \(\mathbb Q\) are the primes
\(p\) and \(\infty\). They are the points of the arithmetic curve.

**Definition 2.1.** Let \(\mathcal V\) be the set of places of \(\mathbb Q\). For \(q\in\mathbb Q^\times\) and
\(v\in\mathcal V\) let
\[
v(q)=v_p(q)\ \text{ if } v=p,\qquad v(q)=-\log\lvert q\rvert\ \text{ if } v=\infty ,
\]
and put \(\deg p=\log p\) and \(\deg\infty=1\). The *divisor* of \(q\) is the formal sum
\(\operatorname{div}(q)=\sum_{v\in\mathcal V}v(q)\,[v]\). Its coefficients at the primes are integers, almost all of
them zero, and its coefficient at \(\infty\) is a real number. The *degree* of a formal sum \(\sum_vc_v[v]\) is
\(\sum_vc_v\deg v\).

**Proposition 2.2.**

(a) \(\deg\operatorname{div}(q)=0\) for every \(q\in\mathbb Q^\times\). If real numbers \(w_v\), \(v\in\mathcal V\),
satisfy \(\sum_vv(q)\,w_v=0\) for all \(q\in\mathbb Q^\times\), then \(w_p=w_\infty\log p\) for every prime \(p\).

(b) The set of \(q\in\mathbb Q\) with \(q=0\) or \(v(q)\ge0\) for all \(v\in\mathcal V\) is \(\{0,1,-1\}\).

(c) Let \(q=a/b\ne0\) be in lowest terms, and put
\[
\operatorname{div}_0(q)=\sum_{v(q)>0}v(q)\,[v],\qquad\operatorname{div}_\infty(q)=\sum_{v(q)<0}(-v(q))\,[v] .
\]
Both have the degree \(h(q)=\log\max(\lvert a\rvert,\lvert b\rvert)\).

*Proof.* (a) Write \(q=\pm\prod_pp^{v_p(q)}\). Then \(\log\lvert q\rvert=\sum_pv_p(q)\log p\), which is the claim. For
the second statement take \(q=p\): then \(w_p-w_\infty\log p=0\). (b) If \(v_p(q)\ge0\) for all primes \(p\), then
\(q\) is an integer, and an integer with \(\lvert q\rvert\le1\) is \(0\) or \(\pm1\). (c) For a prime \(p\) we have
\(v_p(q)>0\) if and only if \(p\) divides \(a\), and then \(v_p(q)=v_p(a)\). Also \(v_\infty(q)>0\) if and only if
\(\lvert a\rvert<\lvert b\rvert\). So
\(\deg\operatorname{div}_0(q)=\log\lvert a\rvert+\max(0,\log\lvert b\rvert-\log\lvert a\rvert)=h(q)\). By (a),
\(\deg\operatorname{div}_\infty(q)=\deg\operatorname{div}_0(q)\). \(\square\)

Part (a) says that the degrees \(\log p\) and \(1\) are forced, up to a common factor, by the requirement that
principal divisors have degree zero. Part (b) says that the functions without poles, the *constants* of the arithmetic
curve, are \(0\), \(1\) and \(-1\). They form the monoid \(\mathbb F_{1^2}\), not a field. The number \(h(q)\) is the
*logarithmic height* of \(q\). By (c) it is the degree of the divisor of zeros of \(q\), which for a function on a
curve is the degree of the function (K1). We have \(h(q)=h(1/q)=h(-q)\), and \(h(q)=0\) exactly for \(q=\pm1\).

The dictionary so far:

| Curve \(X\) over \(k\), function \(f\) | The integers, rational number \(q\) |
|---|---|
| closed point \(P\), with \(\deg P\) | place \(v\), with \(\deg p=\log p\) and \(\deg\infty=1\) |
| valuation \(v_P\) | \(v_p\), and \(-\log\lvert\ \rvert\) at \(\infty\) |
| \(\deg\operatorname{div}f=0\) | product formula (Proposition 2.2(a)) |
| constants: the field \(k\) | constants: the monoid \(\{0,1,-1\}\) |
| \(\deg f\), the degree of the divisor of zeros | \(h(q)=\log\max(\lvert a\rvert,\lvert b\rvert)\) |
| the projective line \(\mathbb P^1_k\) | Section 3 |
| the map \(f\colon X\to\mathbb P^1_k\), \(e_P\), \(\delta_P\) | Section 4 |
| Hurwitz inequality (1.1) | Conjecture 5.3 |

## 3. The projective line over the field with one element

A reference for this section is [Smirnov 1992, §2.2 and §2.3]. See also [Le Bruyn 2016, Section 2].

### 3.1 The model: the projective line over a finite field

**Proposition 3.1.** Let \(\mathbb F_r\) be a finite field with \(r\) elements, of characteristic \(\ell\). Let
\(\overline{\mathbb F}_r\) be an algebraic closure and \(\sigma(x)=x^r\) its Frobenius automorphism.

(a) Every element of \(\overline{\mathbb F}_r^{\,\times}\) is a root of unity of order prime to \(\ell\). For every
\(n\) prime to \(\ell\), the \(n\)-th roots of unity in \(\overline{\mathbb F}_r\) form a cyclic group of order \(n\).

(b) The closed points of \(\mathbb P^1_{\mathbb F_r}\) correspond to the orbits of \(\sigma\) on the set
\(\overline{\mathbb F}_r\cup\{\infty\}\), and the degree of a closed point is the number of elements of its orbit.

(c) The orbits are \(\{0\}\), \(\{\infty\}\), and orbits of roots of unity. For \(n\) prime to \(\ell\), the
\(\varphi(n)\) elements of order \(n\) form \(\varphi(n)/o_n(r)\) orbits with \(o_n(r)\) elements each, where
\(o_n(r)\) is the order of \(r\) in \((\mathbb Z/n)^\times\).

*Proof.* (a) An element \(x\ne0\) lies in a finite subfield with \(r^j\) elements, so \(x^{r^j-1}=1\), and
\(r^j-1\) is prime to \(\ell\). For \(n\) prime to \(\ell\) the polynomial \(X^n-1\) has no multiple root, because
its derivative \(nX^{n-1}\) vanishes only at \(0\). So it has \(n\) roots, and a finite subgroup of the multiplicative
group of a field is cyclic. (b) The closed points other than \(\infty\) are the points \(Q_\pi\) of Section 1.1. Let
\(\alpha\) be a root of \(\pi\) and \(d=\deg\pi\). The field \(\mathbb F_r(\alpha)\) has \(r^d\) elements, and its
automorphism group over \(\mathbb F_r\) is generated by \(\sigma\) and has order \(d\). So the roots of \(\pi\) are
the \(d\) different elements \(\alpha,\sigma(\alpha),\dots,\sigma^{d-1}(\alpha)\), one orbit with \(d\) elements.
Every orbit in \(\overline{\mathbb F}_r\) arises in this way, from the minimal polynomial of one of its elements. The
point \(\infty\) has degree one and is fixed by \(\sigma\). (c) Let \(x\) have order \(n\). Then
\(\sigma^j(x)=x^{r^j}\) equals \(x\) if and only if \(r^j\equiv1\) modulo \(n\). \(\square\)

So the projective line over \(\mathbb F_r\) can be described with roots of unity alone. Its geometric points are
\(0\), \(\infty\) and the roots of unity of order prime to \(\ell\). Its closed points are the orbits of a group that
acts on the roots of unity of order \(n\) through a subgroup of \((\mathbb Z/n)^\times\), here the subgroup generated
by \(r\). The degree of a closed point is the number of geometric points in it.

### 3.2 Smirnov's definition

For \(\mathbb Q\) there is no characteristic to exclude, and the group that acts on roots of unity is a Galois group.
Let
\[
G=\operatorname{Gal}(\mathbb Q(\mu_\infty)/\mathbb Q).
\]
For every \(L\ge1\) the restriction \(G\to\operatorname{Gal}(\mathbb Q(\mu_L)/\mathbb Q)=(\mathbb Z/L)^\times\) is
surjective, and \(u\in(\mathbb Z/L)^\times\) acts on \(\mu_L\) by \(\zeta\mapsto\zeta^u\).

**Definition 3.2 ([Smirnov 1992, §2.3]).** The set of *geometric points* of the projective line is
\[
\mathbb P^1(\mathbb F_{1^\infty})=\{0,\infty\}\cup\mu_\infty=\mathbb F_{1^\infty}\cup\{\infty\}.
\]
The group \(G\) acts on it, trivially on \(0\) and \(\infty\). For a subgroup \(\Gamma\subseteq G\) let
\(\mathbb P^1_\Gamma\) be the set of orbits of \(\Gamma\) on \(\mathbb P^1(\mathbb F_{1^\infty})\). The *degree* of a
point of \(\mathbb P^1_\Gamma\) is the number of elements of the orbit. Three cases have names.

- \(\mathbb P^1_{\mathrm{Sm}}=\mathbb P^1_G\) is *Smirnov's projective line over* \(\mathbb F_1\).
- For \(N\ge1\) let \(\Gamma_N\subseteq G\) be the subgroup of the elements that fix every element of \(\mu_N\); it is
  \(\operatorname{Gal}(\mathbb Q(\mu_\infty)/\mathbb Q(\mu_N))\). Then \(\mathbb P^1_{\Gamma_N}\) is the projective
  line over \(\mathbb F_{1^N}\).
- For a number field \(K\subset\mathbb C\) let
  \(\Gamma_K=\operatorname{Gal}(\mathbb Q(\mu_\infty)/K\cap\mathbb Q(\mu_\infty))\). The set \(\mathbb P^1_{\Gamma_K}\)
  is the projective line that [Smirnov 1992, §2.3] attaches to \(K\).

In [Smirnov 1992] the monoids \(\mathbb F_{1^N}\) and \(\mathbb F_{1^\infty}\) are written \(F_N\) and \(F_\infty\),
and \(\mathbb P^1_{\Gamma_N}\) is written \(\mathbb P^1/F_N\). The notation \(\mathbb F_{1^n}\) for the monoid
\(\{0\}\cup\mu_n\), and the description of the affine line over \(\mathbb F_1\) as \(0\) together with all roots of
unity, go back to unpublished work of Kapranov and Smirnov.

**Proposition 3.3.**

(a) The points of \(\mathbb P^1_{\mathrm{Sm}}\) are \([0]=\{0\}\), \([\infty]=\{\infty\}\), and for every \(n\ge1\)
the set \([n]\) of all roots of unity of order \(n\). We have \(\deg[0]=\deg[\infty]=1\) and
\(\deg[n]=\varphi(n)\). The points of degree one are \([0]\), \([\infty]\), \([1]=\{1\}\) and \([2]=\{-1\}\).

(b) Let \(N,M\ge1\). The roots of unity of order \(M\) form \(\varphi(\gcd(M,N))\) points of
\(\mathbb P^1_{\Gamma_N}\), each of degree \(\varphi(M)/\varphi(\gcd(M,N))\). The points of degree one of
\(\mathbb P^1_{\Gamma_N}\) are \(0\), \(\infty\) and the elements of \(\mu_N\) if \(N\) is even, of \(\mu_{2N}\) if
\(N\) is odd. In particular \(\mathbb P^1_{\Gamma_1}=\mathbb P^1_{\Gamma_2}=\mathbb P^1_{\mathrm{Sm}}\).

(c) If \(\Gamma'\subseteq\Gamma\), every point of \(\mathbb P^1_\Gamma\) is a disjoint union of points of
\(\mathbb P^1_{\Gamma'}\), and its degree is the sum of their degrees.

*Proof.* (a) The group \(G\) preserves the order of a root of unity, and it acts on the roots of unity of order
\(n\) through \((\mathbb Z/n)^\times\), which acts transitively on them. There are \(\varphi(n)\) of them, and
\(\varphi(n)=1\) only for \(n=1,2\).

(b) Let \(L\) be the least common multiple of \(M\) and \(N\). An element of \(G\) lies in \(\Gamma_N\) if and only if
its image \(u\in(\mathbb Z/L)^\times\) satisfies \(u\equiv1\) modulo \(N\). So \(\Gamma_N\) acts on \(\mu_L\) through
the group \(U=\{u\in(\mathbb Z/L)^\times: u\equiv1\bmod N\}\). This group has \(\varphi(L)/\varphi(N)\) elements,
because \((\mathbb Z/L)^\times\to(\mathbb Z/N)^\times\) is surjective. Let \(\zeta\) have order \(M\). If \(u\in U\)
fixes \(\zeta\), then \(u\equiv1\) modulo \(M\) and modulo \(N\), so \(u=1\). Hence every orbit of \(\Gamma_N\) on the
roots of unity of order \(M\) has \(\varphi(L)/\varphi(N)\) elements. Comparing the powers of each prime gives
\(\varphi(L)\,\varphi(\gcd(M,N))=\varphi(M)\,\varphi(N)\). So an orbit has \(\varphi(M)/\varphi(\gcd(M,N))\)
elements, and there are \(\varphi(\gcd(M,N))\) orbits.

The orbits have one element if and only if \(\varphi(L)=\varphi(N)\). Write \(L=Nm\) and \(m=m_1m_2\), where every
prime factor of \(m_1\) divides \(N\) and \(m_2\) is prime to \(N\). Then
\(\varphi(L)=\varphi(N)\,m_1\,\varphi(m_2)\). This equals \(\varphi(N)\) if and only if \(m_1=1\) and
\(m_2\in\{1,2\}\), that is, if and only if \(L=N\), or \(L=2N\) with \(N\) odd. So \(\zeta\) is a point of degree one
if and only if \(M\) divides \(N\), or \(N\) is odd and \(M\) divides \(2N\). For \(N=1\) and \(N=2\) the group \(U\)
is all of \((\mathbb Z/L)^\times\), so \(\Gamma_1\) and \(\Gamma_2\) have the same orbits as \(G\).

(c) A \(\Gamma\)-orbit is a union of \(\Gamma'\)-orbits. \(\square\)

**Remarks 3.4.**

1. *The reason for the group \(G\).* Proposition 3.1 suggests to take orbits of roots of unity as points. Which
   group to take is decided by the maps of Section 4: a rational number, reduced modulo a prime, determines a root of
   unity only up to the action of \(G\) (Proposition 4.3). An element of a number field \(K\) determines a root of
   unity up to \(\Gamma_K\) [Smirnov 1992, §2.5, Lemma 1].
2. *Four points of degree one.* The projective line over a field with \(r\) elements has \(r+1\) points of degree
   one. Smirnov's line has four: \([0]\), \([\infty]\), \([1]\), \([2]\). They are \(0\), \(\infty\) and the two
   nonzero constants \(1\) and \(-1\) of Proposition 2.2(b). So \(\mathbb P^1_{\mathrm{Sm}}\) is a projective line
   over the monoid of constants \(\mathbb F_{1^2}\), which has three elements, and by Proposition 3.3(b) it is the
   same set as the projective line over \(\mathbb F_{1^2}\). [Smirnov 1992, §3.6] says this as follows: the field of
   constants is \(F_2\), and \(\mathbb P^1/F_2\) has four rational points.
3. *Comparison with monoid schemes.* For even \(N\) the projective line over \(\mathbb F_{1^N}\) has \(N+2\) points of
   degree one. This is also the number of points of the monoid scheme \(\mathbb P^1\) with values in
   \(\mathbb F_{1^N}\), computed in *Monoid schemes*. For odd \(N\) Smirnov's line has \(2N+2\) points of degree one,
   because the field \(\mathbb Q(\mu_N)\) contains \(-1\) and hence \(\mu_{2N}\).

## 4. The map attached to a rational number

A reference for this section is [Smirnov 1992, §2.4 to §2.6 and §3.2].

Throughout Sections 4 and 5, \(q\) is a rational number different from \(0\), \(1\) and \(-1\), written \(q=a/b\) in
lowest terms, and \(H=\max(\lvert a\rvert,\lvert b\rvert)\). So \(h(q)=\log H>0\).

### 4.1 The map

**Definition 4.1.** For a prime \(p\) that does not divide \(ab\), let \(\operatorname{ord}_p(q)\) be the order of the
residue class of \(ab^{-1}\) in \(\mathbb F_p^\times\). The map
\(\tau_q\colon\mathcal V\to\mathbb P^1_{\mathrm{Sm}}\) is given by
\[
\tau_q(p)=\begin{cases}[0]&\text{if } p\mid a,\\ [\infty]&\text{if } p\mid b,\\ [\operatorname{ord}_p(q)]&\text{if }
p\nmid ab,\end{cases}\qquad\qquad
\tau_q(\infty)=\begin{cases}[0]&\text{if }\lvert q\rvert<1,\\ [\infty]&\text{if }\lvert q\rvert>1.\end{cases}
\]

In terms of the valuations of Definition 2.1: \(\tau_q(v)=[0]\) if \(v(q)>0\), and \(\tau_q(v)=[\infty]\) if
\(v(q)<0\), for primes and for \(\infty\) alike. The primes with \(v_p(q)=0\) go to the points \([n]\). The numbers
\(\pm1\) are excluded because they are the constants; for them \(v_\infty(q)=0\), and the rule gives no value at
\(\infty\). *Reference:* [Smirnov 1992, §2.5].

The value \([\operatorname{ord}_p(q)]\) is the analogue of the value \(f(P)\) of a function at a point: it is the set
of roots of unity to which \(q\) is congruent modulo \(p\). To say this precisely one needs a lemma.

**Lemma 4.2.** Let \(n\ge1\), let \(\zeta\) be a root of unity of order \(n\), and let \(\mathfrak P\) be a prime
ideal of the ring \(\mathbb Z[\zeta]\) that contains a prime number \(p\) not dividing \(n\). Then the classes of
\(1,\zeta,\dots,\zeta^{n-1}\) modulo \(\mathfrak P\) are pairwise different.

*Proof.* Putting \(X=1\) in \(1+X+\dots+X^{n-1}=\prod_{j=1}^{n-1}(X-\zeta^j)\) gives
\(n=\prod_{j=1}^{n-1}(1-\zeta^j)\). The ideal \(\mathfrak P\) does not contain \(n\), because it contains \(p\) and
does not contain \(1\). So no factor \(1-\zeta^j\) lies in \(\mathfrak P\). For \(0\le i<j<n\) we have
\(\zeta^i-\zeta^j=\zeta^i(1-\zeta^{j-i})\notin\mathfrak P\), because \(\zeta^i\) is a unit. \(\square\)

**Proposition 4.3 (the map as reduction of roots of unity).** Let \(p\) be a prime that does not divide \(ab\), and
\(n=\operatorname{ord}_p(q)\).

(a) For every root of unity \(\zeta\) of order \(n\) there is a prime ideal \(\mathfrak P\) of \(\mathbb Z[\zeta]\)
with \(p\in\mathfrak P\) and \(a-b\zeta\in\mathfrak P\).

(b) Let \(\varepsilon\) be a root of unity whose order \(m\) is prime to \(p\), and let \(\mathfrak P\) be a prime
ideal of \(\mathbb Z[\varepsilon]\) with \(p\in\mathfrak P\) and \(a-b\varepsilon\in\mathfrak P\). Then \(m=n\).

So \([n]\) is the set of all roots of unity \(\varepsilon\) of order prime to \(p\) such that
\(q\equiv\varepsilon\) modulo some prime ideal of \(\mathbb Z[\varepsilon]\) above \(p\).

*Proof.* Let \(\Phi_d\in\mathbb Z[X]\) be the \(d\)-th cyclotomic polynomial, the monic polynomial whose roots are
the roots of unity of order \(d\). Then \(X^n-1=\prod_{d\mid n}\Phi_d\), and \(\Phi_n\) is the minimal polynomial of
\(\zeta\) over \(\mathbb Q\) [Milne 2020, Theorem 6.4]. Division with remainder by the monic polynomial \(\Phi_n\)
shows \(\mathbb Z[\zeta]\cong\mathbb Z[X]/(\Phi_n)\).

(a) Let \(x\in\mathbb F_p\) be the class of \(ab^{-1}\). Then \(x^n=1\), and \(x^d\ne1\) for \(0<d<n\). For a divisor
\(d<n\) of \(n\) this gives \(\Phi_d(x)\ne0\), because \(\Phi_d\) divides \(X^d-1\). Since
\(0=x^n-1=\prod_{d\mid n}\Phi_d(x)\) in the field \(\mathbb F_p\), we get \(\Phi_n(x)=0\). So there is a ring
homomorphism \(\psi\colon\mathbb Z[\zeta]\to\mathbb F_p\) with \(\psi(\zeta)=x\). Its kernel \(\mathfrak P\) is a
prime ideal, it contains \(p\), and it contains \(a-b\zeta\) because \(\psi(a-b\zeta)\) is the class of \(a-b\cdot
ab^{-1}=0\).

(b) The ring \(\mathbb Z[\varepsilon]/\mathfrak P\) is an integral domain, and
\(\mathfrak P\cap\mathbb Z=p\mathbb Z\). So it contains \(\mathbb F_p\), the class of \(b\) is not zero, and the
class of \(\varepsilon\) equals the class \(x\) of \(ab^{-1}\), which has order \(n\). By Lemma 4.2 the class of
\(\varepsilon\) has order \(m\). So \(m=n\). \(\square\)

*Reference:* This is how the map is defined in [Smirnov 1992, §2.5(b)], for an element of a number field. Lemma 1
there states that the set so defined is an orbit of the Galois group; its proof is omitted there. Proposition 4.3
proves it for the field \(\mathbb Q\).

### 4.2 The fibres

**Theorem 4.4 (the fibres of \(\tau_q\)).**

(a) \(\tau_q^{-1}([0])\) consists of the primes that divide \(a\), and of \(\infty\) if \(\lvert q\rvert<1\). And
\(\tau_q^{-1}([\infty])\) consists of the primes that divide \(b\), and of \(\infty\) if \(\lvert q\rvert>1\).

(b) For \(n\ge1\), \(\tau_q^{-1}([n])\) is the set of primes \(p\nmid ab\) with \(\operatorname{ord}_p(q)=n\). All of
them divide the integer \(a^n-b^n\), which is not zero.

(c) Every fibre of \(\tau_q\) is finite, and both \(\tau_q^{-1}([0])\) and \(\tau_q^{-1}([\infty])\) are non-empty.

(d) \(\tau_{1/q}=\iota\circ\tau_q\), where \(\iota\) exchanges \([0]\) and \([\infty]\) and fixes every \([n]\).

*Proof.* (a) and the first sentence of (b) repeat the definition. If \(\operatorname{ord}_p(q)=n\), then
\(a^n\equiv b^n\) modulo \(p\). If \(a^n=b^n\), then \(\lvert a\rvert=\lvert b\rvert\), and since \(a,b\) are coprime
both are \(1\), so \(q=\pm1\). (c) A nonzero integer has finitely many prime divisors. One of the two fibres contains
\(\infty\). The other one is the set of prime divisors of the one of \(a,b\) that has the larger absolute value, which
is at least \(2\). (d) Up to a common sign, \(1/q=b/a\), and an element of a group and its inverse have the same
order. \(\square\)

### 4.3 Ramification indices, degree and defects

**Definition 4.5.** Let \(v\in\mathcal V\). The *ramification index* of \(\tau_q\) at \(v\) is
\[
e_v(q)=\begin{cases}v(q)&\text{if }\tau_q(v)=[0],\\ v(1/q)=-v(q)&\text{if }\tau_q(v)=[\infty],\\
v_p(q^n-1)=v_p(a^n-b^n)&\text{if } v=p\text{ and }\tau_q(p)=[n].\end{cases}
\]
The *degree* of \(\tau_q\) is \(\deg\tau_q=h(q)=\log H\). The *defect* of \(\tau_q\) at a place \(v\), and at a point
\([x]\) of \(\mathbb P^1_{\mathrm{Sm}}\), is
\[
\delta_v(q)=\frac{(e_v(q)-1)\deg v}{\deg\tau_q},\qquad\delta_{[x]}(q)=\sum_{\tau_q(v)=[x]}\delta_v(q).
\]

So \(e_p(q)\) is a positive integer for every prime \(p\), and \(e_\infty(q)=\lvert\log\lvert q\rvert\rvert\) is a
positive real number. The definition follows the one for curves in Section 1.1, where
\(e_P=v_P(f^{\ast}s_Q)\) for a uniformizer \(s_Q\) at the image point.

- At \([0]\) and \([\infty]\) the uniformizers are the coordinate and its inverse, and \(e_v\) is \(v(q)\),
  respectively \(v(1/q)\).
- The point \([n]\) is the set of roots of the cyclotomic polynomial \(\Phi_n\), as the closed point \(Q_\pi\) of
  \(\mathbb P^1_k\) is the set of roots of \(\pi\). By Lemma 4.7 below, \(v_p(q^n-1)=v_p(\Phi_n(q))\) if
  \(\tau_q(p)=[n]\). So \(e_p=v_p(\Phi_n(q))\), in analogy with \(e_P=v_P(\pi(f))\).
- The degree is the degree of the divisor of zeros, as in (K1); see Proposition 4.6.

There is one new feature. The number \(e_\infty\) is a real number and need not be an integer, and it is smaller
than \(1\) if \(e^{-1}<\lvert q\rvert<e\). Then the defect \(\delta_\infty\) is negative. For example
\(\delta_\infty(2)=(\log2-1)/\log2=-0.4427\). At the primes all defects are \(\ge0\).

*Reference:* [Smirnov 1992, §3.2] defines the defects at the places over the four points of degree one, with
\(e_p=v_p(q-1)\) over \([1]\) and \(e_p=v_p(q+1)\) over \([2]\); these agree with Definition 4.5 (see the proof of
Proposition 5.2). The definition over \([n]\) for all \(n\) is in [Le Bruyn 2016, Section 7] and
[Jarra 2023b, Introduction]. By Proposition 4.12 it is the number \(v_p(q^p-q)\) used in
[Smirnov 1992, §5.4]. [Jarra 2023b, Introduction] states \(e_{[\infty]}=-\log\lvert q\rvert\); this is negative for
\(\lvert q\rvert>1\), and the value in [Smirnov 1992, §3.2(a),(b)] is the one above, \(v(q)\) or \(v(1/q)\),
whichever is positive.

**Proposition 4.6 (the fibres over \([0]\) and \([\infty]\)).**
\[
\sum_{\tau_q(v)=[0]}e_v(q)\deg v=\sum_{\tau_q(v)=[\infty]}e_v(q)\deg v=\deg\tau_q .
\]

*Proof.* The two sums are the degrees of \(\operatorname{div}_0(q)\) and \(\operatorname{div}_\infty(q)\). Apply
Proposition 2.2(c). \(\square\)

So over the points \([0]\) and \([\infty]\) the analogue of (K1) holds exactly. It is the product formula.

### 4.4 The fibre over the point \([n]\)

For \(n\ge1\) let
\[
\Phi_n(x,y)=\prod_{\zeta\ \text{of order } n}(x-\zeta y)=y^{\varphi(n)}\,\Phi_n(x/y)\ \in\mathbb Z[x,y].
\]
It is homogeneous of degree \(\varphi(n)\), and \(x^n-y^n=\prod_{d\mid n}\Phi_d(x,y)\). For example
\(\Phi_1(x,y)=x-y\) and \(\Phi_2(x,y)=x+y\). Since \(a^n\ne b^n\), all numbers \(\Phi_n(a,b)\) are nonzero integers.

**Lemma 4.7 (the prime factors of \(\Phi_n(a,b)\)).** Let \(p\) be a prime and \(n\ge1\).

(a) If \(p\) divides \(ab\), then \(p\) does not divide \(\Phi_n(a,b)\).

(b) Let \(p\nmid ab\) and \(d=\operatorname{ord}_p(q)\). Then
\[
v_p(\Phi_n(a,b))=\begin{cases}v_p(a^d-b^d)\ \ge1&\text{if } n=d,\\ 1&\text{if } n=dp^j\text{ with } j\ge1,\text{ and }
(p,j)\ne(2,1),\\ v_2(a+b)&\text{if } p=2\text{ and } n=2,\\ 0&\text{in all other cases.}\end{cases}
\]

(c) If \(p\) is odd, \(p\nmid ab\), and \(m\ge1\) is divisible by \(d=\operatorname{ord}_p(q)\), then
\(v_p(a^m-b^m)=v_p(a^d-b^d)+v_p(m/d)\). If \(a,b\) are odd and \(m\) is even, then
\(v_2(a^m-b^m)=v_2(a-b)+v_2(a+b)+v_2(m)-1\).

(d) If \(p\nmid ab\) and \(n=dp^j\) with \(d=\operatorname{ord}_p(q)\) and \(j\ge1\), then \(p=P(n)\).

*Proof.* (a) \(\Phi_n(x,y)\) is congruent to \(x^{\varphi(n)}\) modulo \(y\) and to \(\pm y^{\varphi(n)}\) modulo
\(x\), because the constant term of \(\Phi_n(X)\) is an integer and a product of roots of unity. If \(p\) divides
\(a\), then \(\Phi_n(a,b)\equiv\pm b^{\varphi(n)}\) modulo \(p\), and \(p\) does not divide \(b\). The case
\(p\mid b\) is the same.

(c) We use two facts about integers \(x,y\) with \(p\nmid xy\) and \(p\mid x-y\).

*Fact 1.* If \(p\nmid m\), then \(v_p(x^m-y^m)=v_p(x-y)\). Indeed
\(x^m-y^m=(x-y)\sum_{i=0}^{m-1}x^{m-1-i}y^i\), and the sum is congruent to \(mx^{m-1}\) modulo \(p\), which is not
zero.

*Fact 2.* If \(p\) is odd, or if \(p=2\) and \(4\mid x-y\), then \(v_p(x^p-y^p)=v_p(x-y)+1\). Indeed, write
\(x=y+p^ku\) with \(k=v_p(x-y)\ge1\) and \(p\nmid u\). Then
\[
x^p-y^p=\sum_{i=1}^{p}\binom pi\,y^{p-i}\,p^{ki}\,u^i .
\]
The term with \(i=1\) has valuation exactly \(k+1\). For \(2\le i\le p-1\) the binomial coefficient is divisible by
\(p\), so the term has valuation at least \(1+2k\ge k+2\). The term with \(i=p\) has valuation \(kp\), and
\(kp\ge k+2\) if \(p\ge3\), or if \(p=2\) and \(k\ge2\).

Now let \(p\) be odd and \(m=d\,p^s\,m'\) with \(p\nmid m'\). Put \(x=a^d\) and \(y=b^d\), so \(p\mid x-y\). Applying
Fact 2 \(s\) times and then Fact 1 to \(x^{p^s},y^{p^s}\) and \(m'\) gives \(v_p(a^m-b^m)=v_p(a^d-b^d)+s\). Let
\(p=2\), \(a,b\) odd and \(m=2^sm'\) with \(s\ge1\) and \(m'\) odd. Put \(x=a^2\) and \(y=b^2\). Odd squares are
congruent to \(1\) modulo \(8\), so \(4\mid x-y\). Applying Fact 2 \(s-1\) times and then Fact 1 gives
\(v_2(a^m-b^m)=v_2(a^2-b^2)+s-1\).

(b) For \(m\ge1\) put \(F(m)=v_p(a^m-b^m)\), and \(f(m)=v_p(\Phi_m(a,b))\ge0\). From
\(a^m-b^m=\prod_{e\mid m}\Phi_e(a,b)\) we get
\[
F(m)=\sum_{e\mid m}f(e)\qquad\text{for all } m\ge1. \tag{4.1}
\]
These equations determine \(f\): by induction, \(f(m)=F(m)-\sum_{e\mid m,\ e<m}f(e)\). Let \(g(m)\) be the right
side of the formula in (b). It is enough to show that \(g\) satisfies (4.1).

We have \(F(m)>0\) if and only if \(d\) divides \(m\). Let \(p\) be odd. The divisors of \(m\) of the form
\(dp^j\) exist only if \(d\mid m\), and then they are \(d,dp,\dots,dp^s\) with \(s=v_p(m/d)\); note that \(p\nmid d\),
because \(d\) divides \(p-1\). So \(\sum_{e\mid m}g(e)\) is \(0\) if \(d\nmid m\), and
\(v_p(a^d-b^d)+s\) if \(d\mid m\). By (c) this is \(F(m)\). Let \(p=2\). Then \(a,b\) are odd and \(d=1\). If \(m\) is
odd, \(\sum_{e\mid m}g(e)=g(1)=v_2(a-b)=F(m)\) by Fact 1. If \(s=v_2(m)\ge1\), then
\(\sum_{e\mid m}g(e)=g(1)+g(2)+\dots+g(2^s)=v_2(a-b)+v_2(a+b)+(s-1)\), which is \(F(m)\) by (c).

(d) \(d\) divides \(p-1\), so every prime factor of \(d\) is smaller than \(p\). \(\square\)

**Theorem 4.8 (the degree of the fibre over \([n]\)).** Let \(n\ge1\), and let
\(t=\min(\lvert a\rvert,\lvert b\rvert)/H\), so \(0<t<1\).

(a) \(\displaystyle\lvert\Phi_n(a,b)\rvert=c_n(q)\prod_{p\in\tau_q^{-1}([n])}p^{\,e_p(q)}\), where \(c_1(q)=1\);
\(c_2(q)=2^{v_2(a+b)}\) if \(ab\) is odd and \(c_2(q)=1\) if \(ab\) is even; and for \(n\ge3\), \(c_n(q)=P(n)\) if
\(P(n)\nmid ab\) and \(n=\operatorname{ord}_{P(n)}(q)\cdot P(n)^j\) for some \(j\ge1\), and \(c_n(q)=1\) otherwise.

(b) \(\displaystyle\sum_{p\in\tau_q^{-1}([n])}e_p(q)\deg p=\log\lvert\Phi_n(a,b)\rvert-\log c_n(q)\).

(c) \(\displaystyle\big\lvert\log\lvert\Phi_n(a,b)\rvert-\varphi(n)\deg\tau_q\big\rvert\le\varphi(n)\,
\log\frac{1}{1-t}\).

*Proof.* (a) By Lemma 4.7(a) and (b), a prime \(p\) divides \(\Phi_n(a,b)\) in two cases. Either \(p\nmid ab\) and
\(\operatorname{ord}_p(q)=n\), that is \(p\in\tau_q^{-1}([n])\); then
\(v_p(\Phi_n(a,b))=v_p(a^n-b^n)=e_p(q)\). Or \(p\nmid ab\) and \(n=\operatorname{ord}_p(q)\,p^j\) with \(j\ge1\). In
the second case \(n\ge2\). If \(n=2\), then \(p=2\), \(ab\) is odd, and the exponent is \(v_2(a+b)\). If \(n\ge3\),
then \(p=P(n)\) by Lemma 4.7(d), and the exponent is \(1\). (b) Take logarithms in (a). (c) For a complex number
\(\zeta\) of absolute value \(1\) we have \(H(1-t)\le\lvert a-\zeta b\rvert\le H(1+t)\). So
\(\log\lvert\Phi_n(a,b)\rvert-\varphi(n)\log H\) lies between \(\varphi(n)\log(1-t)\) and \(\varphi(n)\log(1+t)\),
and \(\log(1+t)\le-\log(1-t)\). \(\square\)

So the analogue of (K1) holds over \([n]\) only approximately. For \(n\ne2\) the fibre over \([n]\) has the degree
\(\deg[n]\cdot\deg\tau_q\) up to an error of absolute value at most \(\varphi(n)\log\frac1{1-t}+\log n\), because
\(c_n(q)\le n\). The first term is small when \(t=e^{-e_\infty(q)}\) is small, that is, when \(q\) is far from
\(\pm1\) at the place \(\infty\). For \(n=2\) and \(ab\) odd there is the further term \(v_2(a+b)\log2\), which is not
bounded: the prime \(2\) divides \(a+b\), but it lies over \([1]\). For example the fibre of \(\tau_7\) over \([2]\)
is empty, because \(7+1=2^3\). *Reference:* [Smirnov 1992, Conclusion, item 1] notes that the relation
\(\deg f^{\ast}(Q)=\deg(f)\deg(Q)\) holds only approximately.

The prime \(P(n)\), in the case \(c_n(q)=P(n)\), divides \(\Phi_n(a,b)\) but does not lie in the fibre: it lies in the
fibre over \([n/P(n)^j]\). For example \(\Phi_6(2,1)=3\) and \(\tau_2(3)=[2]\).

### 4.5 Empty fibres and the theorem of Zsigmondy

**Theorem 4.9 (Zsigmondy).** Let \(A>B\ge1\) be coprime integers and \(n\ge1\). There is a prime \(p\nmid AB\) such
that \(A/B\) has order \(n\) modulo \(p\), except in the following cases:

1. \(n=1\) and \(A-B=1\);
2. \(n=2\) and \(A+B\) is a power of \(2\);
3. \(n=6\), \(A=2\) and \(B=1\).

Equivalently: outside these cases \(A^n-B^n\) has a prime divisor that divides no \(A^m-B^m\) with \(1\le m<n\).

*Proof.* Let \(q=A/B\). The primes in question are the elements of \(\tau_q^{-1}([n])\); they are also the primes
that divide \(A^n-B^n\) and no \(A^m-B^m\) with \(m<n\), because a prime divisor of \(A^n-B^n\) does not divide
\(AB\).

For \(n=1\) the fibre is the set of prime divisors of \(A-B\). For \(n=2\) it is the set of odd prime divisors of
\(A+B\): an odd prime divisor of \(A+B\) does not divide \(A-B\), and \(2\) has \(\operatorname{ord}_2(q)=1\) if
\(AB\) is odd. This gives cases 1 and 2.

Let \(n\ge3\) and suppose that the fibre is empty. By Theorem 4.8(a), \(\lvert\Phi_n(A,B)\rvert=c_n(q)\) is \(1\) or
\(p=P(n)\). The roots of unity of order \(n\) come in pairs of complex conjugates, and
\(\lvert A-\zeta B\rvert>A-B\) for \(\zeta\ne1\). So
\[
\Phi_n(A,B)>(A-B)^{\varphi(n)}\ge1 .
\]
Hence \(\Phi_n(A,B)=p\), and \(c_n(q)=p\) means: \(p\nmid AB\) and \(n=dp^j\) with \(d=\operatorname{ord}_p(q)\) and
\(j\ge1\). Here \(d\) divides \(p-1\), so \(\varphi(n)=\varphi(d)\varphi(p^j)\ge p-1\).

*Case \(A-B\ge2\).* Then \(\Phi_n(A,B)>2^{\varphi(n)}\ge2^{p-1}\ge p\), a contradiction.

*Case \(A-B=1\).* Then \(AB\) is even, so \(p\) is odd. Put \(A_1=A^{p^{j-1}}\) and \(B_1=B^{p^{j-1}}\). If \(z\)
is a root of unity of order \(dp^i\) with \(0\le i\le j\), then \(z^{p^j}\) has order \(d\), because \(p\) does not
divide \(d\); so \(z\) is a root of \(\Phi_d(X^{p^j})\). There are \(\varphi(d)\,p^j\) such \(z\), and this is the
degree of \(\Phi_d(X^{p^j})\). So \(\Phi_d(X^{p^j})=\prod_{i=0}^{j}\Phi_{dp^i}(X)\). Dividing this identity by the
same identity for \(j-1\) and making it homogeneous gives
\[
\Phi_n(A,B)=\frac{\Phi_d(A_1^{\,p},B_1^{\,p})}{\Phi_d(A_1,B_1)} .
\]
Each factor \(\lvert A_1^p-\xi B_1^p\rvert\) of the numerator is at least \(A_1^p-B_1^p\), and each factor
\(\lvert A_1-\xi B_1\rvert\) of the denominator is at most \(A_1+B_1\). So
\[
p=\Phi_n(A,B)\ \ge\ \rho^{\varphi(d)}\ \ge\ \rho,\qquad\rho=\frac{A_1^p-B_1^p}{A_1+B_1},
\]
provided \(\rho\ge1\). Now \(A_1^p-B_1^p=(A_1-B_1)\sum_{i=0}^{p-1}A_1^{p-1-i}B_1^{\,i}\ge
\sum_{i=0}^{p-1}A_1^{p-1-i}B_1^{\,i}\).

If \(p\ge5\), the sum is at least \(A_1^{p-1}+A_1^{p-2}B_1=A_1^{p-2}(A_1+B_1)\). So
\(\rho\ge A_1^{p-2}\ge2^{p-2}>p\), a contradiction.

If \(p=3\), the sum is \(A_1^2+A_1B_1+B_1^2\ge\tfrac34(A_1+B_1)^2\). So \(\rho\ge\tfrac34(A_1+B_1)\), and
\(\rho\le3\) forces \(A_1+B_1\le4\). Since \(A=B+1\) and \(A_1\ge A\), \(B_1\ge B\), this leaves \(B=1\), \(A=2\) and
\(A_1=2\), so \(j=1\). Then \(d=\operatorname{ord}_3(2)=2\) and \(n=dp=6\). This is case 3, and indeed
\(2^6-1=3^2\cdot7\) with \(\operatorname{ord}_3(2)=2\) and \(\operatorname{ord}_7(2)=3\). \(\square\)

*Reference:* [Zsigmondy 1892]. [Le Bruyn 2016, Section 7] uses this theorem, for \(n>1\), to describe the rational
numbers \(q\) for which \(\tau_q\) is not surjective.

To treat negative \(q\) we need to know how the order changes with the sign.

**Lemma 4.10 (change of sign).** For \(r\ge1\) put \(r^{\ast}=2r\) if \(r\) is odd, \(r^{\ast}=r/2\) if
\(r\equiv2\) modulo \(4\), and \(r^{\ast}=r\) if \(4\mid r\). Then \(r\mapsto r^{\ast}\) is an involution of the
positive integers. If \(p\) is an odd prime and \(x\in\mathbb F_p^\times\) has order \(r\), then \(-x\) has order
\(r^{\ast}\). So for every odd prime \(p\nmid ab\): \(\tau_{-q}(p)=[\operatorname{ord}_p(q)^{\ast}]\). If \(ab\) is
odd, then \(\tau_q(2)=\tau_{-q}(2)=[1]\).

*Proof.* If \(r\) is odd, then \(-1\) and \(x\) have coprime orders \(2\) and \(r\), so \(-x\) has order \(2r\). Let
\(r=2s\). Then \(x^s\) has order \(2\), so \(x^s=-1\), the only element of order \(2\) of the cyclic group
\(\mathbb F_p^\times\). Hence \(-x=x^{s+1}\), which has order \(2s/\gcd(2s,s+1)\). If \(s\) is odd, then
\(\gcd(2s,s+1)=2\gcd(s,(s+1)/2)=2\), and the order is \(s=r/2\). If \(s\) is even, then
\(\gcd(2s,s+1)=\gcd(s,s+1)=1\), and the order is \(r\). The map is an involution: an odd \(r\) goes to \(2r\equiv2\)
modulo \(4\), which goes back to \(r\). \(\square\)

**Corollary 4.11 (the empty fibres of \(\tau_q\)).** Let \(q\ne0,\pm1\), and write \(\lvert q\rvert\) or
\(1/\lvert q\rvert\) as \(A/B\) with coprime integers \(A>B\ge1\). Let \(n\ge1\).

(a) If \(q>0\), the fibre \(\tau_q^{-1}([n])\) is empty exactly in the three cases of Theorem 4.9.

(b) If \(q<0\), the fibre \(\tau_q^{-1}([n])\) is empty exactly in two cases: \(n=2\) and \(A-B\) is a power of \(2\)
(the power \(2^0=1\) included); or \(n=3\), \(A=2\) and \(B=1\).

So \(\tau_q\) is surjective except for the listed \(q\), and it never misses more than two points.

*Proof.* By Theorem 4.4(d) we may replace \(q\) by \(1/q\), so let \(\lvert q\rvert=A/B\). (a) is Theorem 4.9. (b)
Let \(q=-A/B\). By Lemma 4.10 the odd primes in \(\tau_q^{-1}([n])\) are the odd primes in
\(\tau_{A/B}^{-1}([n^{\ast}])\), and \(2\) lies in \(\tau_q^{-1}([1])\) if \(AB\) is odd, and in no fibre over a
point \([n]\) otherwise.

For \(n=1\): \(n^{\ast}=2\), and the fibre is the set of all primes that divide \(A+B\). It is not empty, because
\(A+B\ge3\). For \(n=2\): \(n^{\ast}=1\), and the fibre is the set of odd primes that divide \(A-B\). For \(n\ge3\)
we have \(n^{\ast}\ge3\), the prime \(2\) plays no role, and the fibre is \(\tau_{A/B}^{-1}([n^{\ast}])\). By
Theorem 4.9 it is empty only if \(n^{\ast}=6\), that is \(n=3\), and \(A/B=2\). For the last sentence: in (a), cases 1
and 3 can occur together, for \(q=2\), and case 2 excludes the other two; in (b) the two cases occur together for
\(q=-2\). \(\square\)

*Reference:* [Dickson 1919, Chapter VII] reports the theorem of [Zsigmondy 1892] for integers of either sign. The
case \(n=2\), \(a+b=\pm1\), for example \(a=2\) and \(b=-1\), is an exception that is missing from the list given
there; it is the case \(A-B=1\) of (b).

### 4.6 Ramified primes and an example

**Proposition 4.12.** For every prime \(p\nmid ab\): \(e_p(q)=v_p(q^{p-1}-1)=v_p(q^p-q)\). So \(\tau_q\) is ramified
at \(p\), that is \(e_p(q)\ge2\), if and only if \(q^p\equiv q\) modulo \(p^2\).

*Proof.* Let \(n=\operatorname{ord}_p(q)\). For \(p=2\) we have \(n=1=p-1\). For odd \(p\), \(n\) divides \(p-1\) and
\(p\nmid(p-1)/n\), so \(v_p(a^{p-1}-b^{p-1})=v_p(a^n-b^n)\) by Lemma 4.7(c). Finally
\(q^{p-1}-1=(a^{p-1}-b^{p-1})/b^{p-1}\) and \(q^p-q=q(q^{p-1}-1)\), where \(q\) and \(b\) are units at \(p\).
\(\square\)

The primes with \(v_p(q)=0\) and \(q^p\equiv q\) modulo \(p^2\) are called singular in [Smirnov 1992, §5.4]. By
Proposition 4.12 they are the primes not dividing \(ab\) at which \(\tau_q\) is ramified.

**Example 4.13 (\(q=2\)).** Here \(\deg\tau_2=\log2\), \(\tau_2(2)=[0]\) and \(\tau_2(\infty)=[\infty]\), with
\(e_2=1\) and \(e_\infty=\log2\). For odd \(p\), \(\tau_2(p)=[n]\) with \(n\) the order of \(2\) modulo \(p\):

| \(p\) | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 |
|---|---|---|---|---|---|---|---|---|---|---|
| \(\tau_2(p)\) | [2] | [4] | [3] | [10] | [12] | [8] | [18] | [11] | [28] | [5] |

The fibres over \([n]\) for \(n\le12\), read off from the factorizations of \(2^n-1\):

| \(n\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| \(\tau_2^{-1}([n])\) | none | 3 | 7 | 5 | 31 | none | 127 | 17 | 73 | 11 | 23, 89 | 13 |

The fibres over \([1]\) and \([6]\) are empty, as Corollary 4.11 says, and \(\tau_2\) is surjective onto the
complement of these two points. Theorem 4.8 for \(n=6\): \(\Phi_6(2,1)=3\) and \(c_6(2)=3\), because
\(\operatorname{ord}_3(2)=2\) and \(6=2\cdot3\). For \(n=3\): \(\Phi_3(2,1)=7\), \(c_3(2)=1\), and the fibre
\(\{7\}\) has degree \(\log7=1.95\), while \(\deg[3]\cdot\deg\tau_2=2\log2=1.39\); the bound of Theorem 4.8(c) is
\(2\log2\). The map is unramified at every odd prime below \(1093\). It is ramified at \(1093\), which lies over
\([364]\), and at \(3511\), which lies over \([1755]\), with \(e=2\) in both cases; these are the only ramified primes
below \(4000\). The defect at \(\infty\) is negative, and \(\delta_{[0]}(2)=0\).

For \(q=3\) the prime \(11\) is ramified: \(\Phi_5(3,1)=121=11^2\), so \(\tau_3^{-1}([5])=\{11\}\) with
\(e_{11}=2\). This fibre has degree \(2\log11=4.80\), and \(\deg[5]\cdot\deg\tau_3=4\log3=4.39\).

## 5. The Hurwitz inequality for the integers and the ABC conjecture

A reference for this section is [Smirnov 1992, §3 and §5.1].

### 5.1 The sum of the defects over the points of degree one

In the Hurwitz inequality (1.1) the sum may run over any set of points of the projective line. For \(\tau_q\),
[Smirnov 1992, §3] sums over the points of degree one. By Proposition 3.3(a) these are \([0]\), \([\infty]\),
\([1]\) and \([2]\).

**Definition 5.1.** Put
\[
S_3(q)=\delta_{[0]}(q)+\delta_{[\infty]}(q)+\delta_{[1]}(q),\qquad S_4(q)=S_3(q)+\delta_{[2]}(q).
\]
So \(S_4(q)\) is the sum of the defects \(\delta_v(q)\) over the set \(X(q)\) of all places \(v\) such that
\(\tau_q(v)\) has degree one.

**Proposition 5.2 (closed formulas).**
\[
S_3(q)=2+\frac{\log\lvert a-b\rvert-\log\operatorname{rad}\big(ab(a-b)\big)-1}{\log H}, \tag{5.1}
\]
\[
S_4(q)=2+\frac{\log\dfrac{\lvert a^2-b^2\rvert}{2^{\,v_2(a+b)}}-\log\operatorname{rad}\big(ab(a^2-b^2)\big)-1}
{\log H}. \tag{5.2}
\]
Moreover \(\delta_{[2]}(q)\ge0\), so \(S_3(q)\le S_4(q)\); \(S_3(1/q)=S_3(q)\) and \(S_4(1/q)=S_4(q)\); and
\(S_3(q)\le3-1/\log H\) and \(S_4(q)<4\).

*Proof.* We compute, for each of the four fibres, the sum of \(e_v\deg v\) and the sum of \(\deg v\).

By Proposition 4.6 the sum of \(e_v\deg v\) over the fibre of \([0]\) is \(\log H\), and the same holds for
\([\infty]\). The two fibres together consist of the primes that divide \(ab\) and of \(\infty\), so their sum of
\(\deg v\) is \(\log\operatorname{rad}(ab)+1\).

The fibre over \([1]\) is the set of primes that divide \(a-b\): such a prime \(p\) does not divide \(ab\), and
\(q\equiv1\) modulo \(p\). There \(e_p=v_p(q-1)=v_p(a-b)\). So the sum of \(e_p\log p\) is \(\log\lvert a-b\rvert\),
and the sum of \(\log p\) is \(\log\operatorname{rad}(a-b)\).

The fibre over \([2]\) is the set of odd primes that divide \(a+b\). Indeed, an odd prime divisor \(p\) of \(a+b\)
does not divide \(ab\), and \(q\equiv-1\not\equiv1\) modulo \(p\); conversely, if \(\operatorname{ord}_p(q)=2\), then
\(q\equiv-1\) modulo \(p\) and \(p\ne2\). An odd prime that divides \(a+b\) does not divide \(a-b\), so there
\(e_p=v_p(a^2-b^2)=v_p(a+b)=v_p(q+1)\). Let \(k=\lvert a+b\rvert/2^{v_2(a+b)}\). The sum of \(e_p\log p\) over this
fibre is \(\log k\), and the sum of \(\log p\) is \(\log\operatorname{rad}(k)\).

Since \(\log H\cdot\delta_v=e_v\deg v-\deg v\), we get
\[
\log H\cdot S_3(q)=2\log H+\log\lvert a-b\rvert-\log\operatorname{rad}(ab)-\log\operatorname{rad}(a-b)-1 .
\]
The integers \(a\), \(b\), \(a-b\) are pairwise coprime, so
\(\operatorname{rad}(ab)\operatorname{rad}(a-b)=\operatorname{rad}(ab(a-b))\). This is (5.1). Adding
\(\log k-\log\operatorname{rad}(k)\) gives (5.2): first \(\lvert a-b\rvert\,k=\lvert a^2-b^2\rvert/2^{v_2(a+b)}\);
second \(\operatorname{rad}(ab(a-b))\operatorname{rad}(k)=\operatorname{rad}(ab(a^2-b^2))\), because \(k\) is odd
and prime to \(ab(a-b)\), and if \(a+b\) is even, then so is \(a-b\).

The defect \(\delta_{[2]}\) is a sum over primes, and \(e_p\ge1\) at every prime. The right sides of (5.1) and (5.2)
do not change when the pair \((a,b)\) is replaced by \((b,a)\) or by \((-b,-a)\), and one of these two pairs is
\(1/q\) in lowest terms. Finally, one of \(a,b,a-b\) is even, so \(\operatorname{rad}(ab(a-b))\ge2\), and
\(\lvert a-b\rvert\le2H\); this gives \(S_3(q)\le2+(\log H-1)/\log H\). One of \(a,b,a-b,a+b\) is divisible by
\(3\), so \(\operatorname{rad}(ab(a^2-b^2))\ge6\), and \(\lvert a^2-b^2\rvert<H^2\); this gives \(S_4(q)<4\).
\(\square\)

Formula (5.1) has the same shape as the second proof of Theorem 1.5. There the three fibres over \(0,1,\infty\)
had \(n_0(abc)+1\) points at most, the \(+1\) being the point \(\infty\) of the curve. Here the three fibres have the
total degree \(\log\operatorname{rad}(ab(a-b))+1\), the \(+1\) being the place \(\infty\). There is one difference.
The fibres over \([0]\) and \([\infty]\) have the full degree \(\log H\), but the fibre over \([1]\) has the degree
\(\log\lvert a-b\rvert\), which is only approximately \(\log H\) (Theorem 4.8).

### 5.2 The conjecture

**Conjecture 5.3 (Hurwitz inequality for \(\mathbb Q\); Smirnov).** For every \(\varepsilon>0\) there is a real
number \(C_\varepsilon\) such that for all rational numbers \(q\ne0,\pm1\)
\[
S_4(q)\ \le\ 2+\varepsilon+\frac{C_\varepsilon}{\deg\tau_q}.
\]

*Reference:* [Smirnov 1992, §3.5 and §3.6]. There §3.5 states a conjecture \(B(K)\) for every number field \(K\)
(Conjecture 5.12 below), and §3.6 writes out the case \(K=\mathbb Q\): for \(q=m/n\) with coprime integers
\(m>n>0\) it is the inequality
\(\delta_\infty+\delta_0+\delta_1+\delta_2\le2+\varepsilon+C(\varepsilon)/\log m\), called \(B(\mathbb Q)\), with
four defects given by formula (3.3) there. These are \(\delta_{[\infty]},\delta_{[0]},\delta_{[1]},\delta_{[2]}\),
and formula (3.3) agrees with the proof of Proposition 5.2.

Compare with (1.1). The constant \(2\) is the same. The term \(-\chi(X)/\deg f\) is replaced by
\(\varepsilon+C_\varepsilon/\deg\tau_q\); Proposition 5.10 shows that \(\varepsilon\) cannot be left out. Two points
of the statement need care.

*Which points.* The sum runs over the places whose image has degree one, and there are four such points, not three.
In [Smirnov 1992, §3.1] the set \(X(q)\) is defined by the conditions \(v(q)\ne0\) or \(v(q-\epsilon)>0\) for a root
of unity \(\epsilon\in\mathbb Q\), and \(\epsilon=-1\) gives the fibre over \([2]\). [Jarra 2023b, Introduction]
describes \(X(q)\) as the set of places whose image has degree one and also as
\(\tau_q^{-1}(\{[0],[1],[\infty]\})\); the second description leaves out the fibre over \([2]\), which has degree
\(\varphi(2)=1\) and is not empty in general: for \(q=2\) it contains the prime \(3\).
[Le Bruyn 2016, Section 7] sums over the fibres of \([0]\), \([1]\) and \([\infty]\). We call the inequality
\(S_3(q)\le2+\varepsilon+C_\varepsilon/\deg\tau_q\) the *three-point form* of the conjecture. Since \(S_3\le S_4\),
it follows from Conjecture 5.3 with the same constants. Corollary 5.9 shows that the two forms are equivalent.

*Which \(q\).* [Smirnov 1992, §3.6] states \(B(\mathbb Q)\) for \(q>1\) only. Since \(S_4(1/q)=S_4(q)\), this covers
all \(q>0\). For \(q<0\) the inequality is a different one. By (5.2), if \(ab\) is odd, then
\[
S_4(-q)-S_4(q)=\frac{\big(v_2(a+b)-v_2(a-b)\big)\log2}{\log H},
\]
and this is not zero, because exactly one of the even numbers \(a+b\), \(a-b\) is divisible by \(4\). For example
\(S_4(3)=0.090\) and \(S_4(-3)=0.721\). So the defect sum is not invariant under \(q\mapsto-q\). Corollary 5.9 shows
that the conjecture for all \(q\) follows from the conjecture for \(q>1\).

**Conjecture 5.4 (ABC).** For every \(\varepsilon>0\) there is a real number \(K_\varepsilon\) such that
\[
C\ \le\ K_\varepsilon\,\operatorname{rad}(ABC)^{1+\varepsilon}
\]
for all coprime positive integers \(A,B\) and \(C=A+B\).

*Reference:* [Oesterlé 1988, Section I.3, Conjecture 3] states the conjecture for nonzero coprime integers
\(a,b,c\) with \(a+b+c=0\), in the form
\(\max(\lvert a\rvert,\lvert b\rvert,\lvert c\rvert)\le C(\varepsilon)\operatorname{rad}(abc)^{1+\varepsilon}\), and
says that it arose from a discussion between Masser and Oesterlé in 1985. This is the statement above: two of the
three numbers have the same sign, and the third is minus their sum. The form above, for positive integers, is due to Masser.

**Lemma 5.5.** Conjecture 5.4 holds if and only if for every \(\varepsilon\) with \(0<\varepsilon<1\) there is a
real number \(K'_\varepsilon\) such that \(C^{1-\varepsilon}\le K'_\varepsilon\operatorname{rad}(ABC)\) for all
coprime positive integers \(A,B\) and \(C=A+B\). More precisely: from constants \(K'_\varepsilon\) one gets
\(K_\eta=(K'_{\eta/(1+\eta)})^{1+\eta}\), and from constants \(K_\varepsilon\) one gets
\(K'_\varepsilon=K_\varepsilon^{1/(1+\varepsilon)}\).

*Proof.* Write \(R=\operatorname{rad}(ABC)\). Let \(\eta>0\) and \(\varepsilon=\eta/(1+\eta)\). Then
\(1/(1-\varepsilon)=1+\eta\), and \(C^{1-\varepsilon}\le K'_\varepsilon R\) gives
\(C\le(K'_\varepsilon R)^{1+\eta}\). Conversely \(C\le K_\varepsilon R^{1+\varepsilon}\) gives
\(C^{1/(1+\varepsilon)}\le K_\varepsilon^{1/(1+\varepsilon)}R\), and
\(C^{1-\varepsilon}\le C^{1/(1+\varepsilon)}\) because \(C\ge1\) and \(1-\varepsilon\le1/(1+\varepsilon)\).
\(\square\)

### 5.3 The conjecture and the ABC conjecture are equivalent

**Theorem 5.6 (Smirnov).** Let \(0<\varepsilon<1\) and let \(C_\varepsilon\) be a real number such that
\[
S_3(q)\ \le\ 2+\varepsilon+\frac{C_\varepsilon}{\deg\tau_q}\qquad\text{for all rational numbers } q>1 .
\]
Then for all coprime positive integers \(A,B\) and \(C=A+B\)
\[
C^{1-\varepsilon}\ \le\ 2\,e^{1+C_\varepsilon}\,\operatorname{rad}(ABC).
\]
Consequently Conjecture 5.3 implies Conjecture 5.4, and already its three-point form for \(q>1\) does. The
constants are \(K_\eta=\big(2e^{1+C_\varepsilon}\big)^{1+\eta}\) with \(\varepsilon=\eta/(1+\eta)\).

*Proof.* Let \(a=C\) and \(b=\min(A,B)\), and \(q=a/b\). Then \(a,b\) are coprime, \(q>1\), \(H=C\), and
\(a-b=\max(A,B)\). So \(\operatorname{rad}(ab(a-b))=\operatorname{rad}(ABC)\), and by (5.1)
\[
S_3(q)=2+\frac{\log\max(A,B)-\log\operatorname{rad}(ABC)-1}{\log C}.
\]
The hypothesis, multiplied by \(\log C>0\), gives
\[
\log\max(A,B)-\log\operatorname{rad}(ABC)-1\ \le\ \varepsilon\log C+C_\varepsilon .
\]
Now \(\max(A,B)\ge C/2\). So \(\log C-\log2-\log\operatorname{rad}(ABC)-1\le\varepsilon\log C+C_\varepsilon\), which
is the claim. The last statement follows from \(S_3\le S_4\) and Lemma 5.5. \(\square\)

*Reference:* [Smirnov 1992, Theorem 1]. The form of the ABC conjecture obtained there is the one of Conjecture 5.4:
\(C\le\text{const}\cdot\operatorname{rad}(ABC)^{1+\varepsilon}\) for coprime positive integers \(A\), \(B\) and
\(C=A+B\), with a constant that depends only on \(\varepsilon\).

**Example 5.7 (a numerical check).** Take \(A=3\), \(B=125\), \(C=128\). Then
\(\operatorname{rad}(ABC)=30\), and the proof uses \(q=128/3\), with \(\deg\tau_q=\log128=4.8520\). The four fibres
are: over \([0]\) the prime \(2\) with \(e_2=7\); over \([\infty]\) the prime \(3\) with \(e_3=1\) and the place
\(\infty\) with \(e_\infty=\log(128/3)=3.7534\); over \([1]\) the prime \(5\) with \(e_5=3\), because
\(128-3=5^3\); over \([2]\) the prime \(131\) with \(e_{131}=1\), because \(128+3=131\) is prime. So
\[
\delta_{[0]}=\frac{6\log2}{\log128}=0.8571,\quad\delta_{[\infty]}=\frac{0+(3.7534-1)}{4.8520}=0.5675,\quad
\delta_{[1]}=\frac{2\log5}{\log128}=0.6634,\quad\delta_{[2]}=0 ,
\]
and \(S_3=S_4=2.0880\). Formula (5.1) gives the same number:
\(2+(\log125-\log30-1)/\log128=2+0.4271/4.8520\). The sum exceeds \(2\), so this \(q\) forces
\(C_\varepsilon\ge0.4271-4.8520\,\varepsilon\) in Conjecture 5.3. Conversely, with a constant \(C_\varepsilon\) the
proof of Theorem 5.6 gives \(125\le e^{1+C_\varepsilon}\cdot128^{\varepsilon}\cdot30\), and then
\(128^{1-\varepsilon}\le2e^{1+C_\varepsilon}\cdot30\). For \(C_\varepsilon=0.4271-4.8520\,\varepsilon\) the first
inequality is an equality: \(e^{1.4271}=4.1667=125/30\). The second one then reads \(128\le250\).

**Theorem 5.8 (the converse).** Assume that Conjecture 5.4 holds with constants \(K_\eta\). Then for every
\(\varepsilon>0\) and every rational number \(q\ne0,\pm1\)
\[
S_4(q)\ <\ 2+\varepsilon+\frac{\log K_{\varepsilon/4}-1}{\deg\tau_q}.
\]
So Conjecture 5.3 holds with \(C_\varepsilon=\log K_{\varepsilon/4}-1\).

*Proof.* Let \(Z=H^2=\max(a^2,b^2)\), \(X=\min(a^2,b^2)\) and \(Y=Z-X=\lvert a^2-b^2\rvert\). These are positive
integers, \(X\) and \(Y\) are coprime, and \(X+Y=Z\). Their radical is
\(R=\operatorname{rad}(XYZ)=\operatorname{rad}(ab(a^2-b^2))\). Let \(\eta=\varepsilon/4\). Conjecture 5.4 gives
\(H^2\le K_\eta R^{1+\eta}\). Since \(R\le\lvert ab(a^2-b^2)\rvert<H^4\), we have \(R^\eta<H^{4\eta}=H^\varepsilon\).
So
\[
\frac{\lvert a^2-b^2\rvert}{2^{\,v_2(a+b)}}\ \le\ \lvert a^2-b^2\rvert\ <\ H^2\ \le\ K_\eta\,R\,H^{\varepsilon}.
\]
Take logarithms, subtract \(\log R+1\), divide by \(\log H\), and use (5.2). \(\square\)

**Corollary 5.9.** The following statements are equivalent.

1. The ABC conjecture (Conjecture 5.4).
2. Conjecture 5.3.
3. The inequality of Conjecture 5.3 for all rational \(q>1\); this is \(B(\mathbb Q)\) of [Smirnov 1992, §3.6].
4. The three-point form of Conjecture 5.3, for all \(q\ne0,\pm1\).
5. The three-point form for all rational \(q>1\).

*Proof.* Since \(S_3\le S_4\), (2) implies (3) and (4), and each of these implies (5). Theorem 5.6 shows that (5)
implies (1), and Theorem 5.8 shows that (1) implies (2). \(\square\)

By (5.1), the three-point inequality for one number \(q\) says
\[
\lvert a-b\rvert\ \le\ e^{1+C_\varepsilon}\,H^{\varepsilon}\,\operatorname{rad}\big(ab(a-b)\big).
\]
This is an inequality of ABC type for the three integers \(b\), \(a-b\) and \(a\). So over \(\mathbb Q\) the Hurwitz
inequality and the ABC conjecture are two ways to write one statement. *Reference:* [Smirnov 1992, Theorem 1] proves
that (3) implies (1), and the Introduction there describes the Hurwitz inequality over \(\mathbb Q\) as a
strengthening of the ABC conjecture. For the inequality \(B(\mathbb Q)\), Theorem 5.8 shows that the converse
implication holds too. Conjecture 5.11 below is a stronger statement, and Proposition 5.15 shows that it does not
hold.

**Proposition 5.10 (the term \(\varepsilon\) cannot be left out).** For \(k\ge1\) let \(q_k=3^{2^k}\). Then
\[
S_3(q_k)\ \ge\ 2+\frac{(k+1)\log2-\log3-1}{\deg\tau_{q_k}},\qquad\deg\tau_{q_k}=2^k\log3 .
\]
So there is no real number \(C\) with \(S_3(q)\le2+C/\deg\tau_q\) for all \(q>1\), and none for \(S_4\). With
\(m=q_k\) the bound reads \(S_3(q_k)\ge2+(\log\log m-1.5)/\log m\).

*Proof.* Here \(a=3^{2^k}\), \(b=1\) and \(H=a\). By Lemma 4.7(c),
\(v_2(a-1)=v_2(3-1)+v_2(3+1)+v_2(2^k)-1=k+2\). So \(\operatorname{rad}(a-1)\le2(a-1)/2^{k+2}\), and
\(\operatorname{rad}(ab(a-b))=3\operatorname{rad}(a-1)\le3(a-1)/2^{k+1}\). Now (5.1) gives the first bound. Its
numerator tends to infinity with \(k\), and \(S_4\ge S_3\). For the last statement,
\(\log m=2^k\log3\) gives \((k+1)\log2=\log\log m+\log2-\log\log3\), and
\(1+\log3+\log\log3-\log2=1.4995\). \(\square\)

For \(k=3\), that is \(q=6561\), the bound gives \(S_3\ge2.0767\); here \(6560=2^5\cdot5\cdot41\), and the bound is
the exact value.

*Reference:* The triples \(1+(3^{2^k}-1)=3^{2^k}\) show that the ABC conjecture fails without \(\varepsilon\); the example is due to Jastrzebowski and Spielman.
Stewart and Tijdeman proved more [Stewart–Tijdeman 1986, Theorem 2]: for every \(\delta>0\) there are infinitely many coprime positive
integers \(A,B\) and \(C=A+B\) with \(C>R\exp\big((4-\delta)\sqrt{\log R}/\log\log R\big)\), where
\(R=\operatorname{rad}(ABC)\). [Le Bruyn 2016, Section 7] derives from the three-point inequality with a constant in
place of \(\varepsilon\deg\tau_q+C_\varepsilon\) the bound \(C\le C'\operatorname{rad}(ABC)\), and calls it too
strong. Proposition 5.10 shows that this inequality fails. Further families of examples are in
[Smirnov 1992, §4]; see Section 7.2.

### 5.4 Number fields: the conjectures A and B(K) of Smirnov

This subsection states the two general conjectures of [Smirnov 1992, §3.4 and §3.5]. It proves that the
inequality of the first gives the second (Proposition 5.13), and that the first does not hold, already for
\(K=\mathbb Q\) (Proposition 5.15). For \(K=\mathbb Q\), an inequality of the first kind whose remainder is a
function of the degree is equivalent to the second (Proposition 5.16).

Let \(K\) be a number field. Let \(X_{na}\) be the set of its non-archimedean places and \(X_a\) the set of its
archimedean places, and \(X=X_{na}\cup X_a\). For \(\pi\in X_{na}\) let \(v_\pi\) be the valuation of \(K\) with
value group \(\mathbb Z\), \(k_\pi\) the residue field, and \(\deg\pi=\log\#k_\pi\). For \(\pi\in X_a\) let
\(K_\pi\) be the completion, which is \(\mathbb R\) or \(\mathbb C\), let \(f_\pi\in K_\pi\) be the image of
\(f\in K\), and put
\[
\varepsilon(\pi)=[K_\pi: \mathbb R],\qquad v_\pi(f)=-\varepsilon(\pi)\log\lvert f_\pi\rvert,\qquad\deg\pi=1 .
\]
With these conventions \(\sum_{\pi\in X}v_\pi(f)\deg\pi=0\) for all \(f\in K^\times\); this is the product formula
[Milne 2020, Theorem 7.15]. The *degree* of \(f\) is \(\deg f=\sum_{v_\pi(f)>0}v_\pi(f)\deg\pi\). An element
\(f\in K^\times\) is *exceptional* if \(\lvert f_\pi\rvert=1\) for some \(\pi\in X_a\). For a non-exceptional \(f\)
let \(X(f)\) be the set of the places \(\pi\) such that \(v_\pi(f)\ne0\), or \(v_\pi(f-\epsilon)>0\) for some root of
unity \(\epsilon\in K\). For \(\pi\in X(f)\) define \(e_\pi\) as follows: \(e_\pi=v_\pi(f)\) if \(v_\pi(f)>0\);
\(e_\pi=v_\pi(1/f)\) if \(v_\pi(f)<0\); and if \(v_\pi(f)=0\) and \(v_\pi(f-\epsilon)>0\), then \(\pi\) is
non-archimedean, of residue characteristic \(p\) say, and \(e_\pi=v_\pi(f-\epsilon_0)\), where
\(\epsilon=\epsilon_0\epsilon_1\) with \(\epsilon_0\) of order prime to \(p\) and \(\epsilon_1\) of order a power of
\(p\). The defect is \(\delta_\pi=(e_\pi-1)\deg\pi/\deg f\). Finally let \(d_K\) be the discriminant of \(K\),
\(r_2\) the number of complex places, \(\gamma\) a real constant, and
\[
\chi(K)=-\log\lvert d_K\rvert-r_2\gamma .
\]
[Smirnov 1992, §2.7] proposes the value \(\gamma=-2\log(\pi/2)\), where \(\pi=3.14\dots\).

**Conjecture 5.11 (Smirnov, Conjecture A).** There is a function \(R_1\colon\mathbb R^\times\to\mathbb R\) with the
properties

(a) \(R_1\) is continuous;

(b) \(R_1(x)=R_1(-x)=R_1(1/x)\) for all \(x\);

(c) \(R_1(x)/\log x\to0\) for \(x\to+\infty\);

such that for every number field \(K\) and every non-exceptional \(f\in K^\times\)
\[
\sum_{\pi\in X(f)}\delta_\pi\ \le\ 2-\frac{\chi(K)}{\deg f}+\sum_{\pi\in X_a}\frac{R_{\varepsilon(\pi)}(f_\pi)}
{\deg f},\qquad\text{where } R_2(z)=2R_1(\lvert z\rvert)+1-\gamma\ \text{ for } z\in\mathbb C^\times .
\]

*Reference:* [Smirnov 1992, §3.4], with the definitions of §2.1, §2.4, §2.7, §3.1, §3.2 and §3.3 there.

**Conjecture 5.12 (Smirnov, Conjecture B(K)).** Let \(K\) be a number field. For every \(\varepsilon>0\) there is a
real number \(C=C(\varepsilon,K)\) such that for every non-exceptional \(f\in K^\times\)
\[
\sum_{\pi\in X(f)}\delta_\pi\ \le\ 2+\varepsilon+\frac{C}{\deg f}.
\]

*Reference:* [Smirnov 1992, §3.5].

**Proposition 5.13.**

(a) For \(K=\mathbb Q\), Conjecture 5.12 is Conjecture 5.3, and the inequality of Conjecture 5.11 reads
\(S_4(q)\le2+R_1(q)/\deg\tau_q\) for all \(q\ne0,\pm1\).

(b) Let \(K\) be a number field. If a function \(R_1\) with the properties (a), (b), (c) of Conjecture 5.11
satisfies the inequality of Conjecture 5.11 for all non-exceptional \(f\in K^\times\), then Conjecture 5.12 holds
for \(K\).

*Proof.* (a) For \(K=\mathbb Q\) there is one archimedean place, it is real, \(d_{\mathbb Q}=1\) and \(r_2=0\), so
\(\chi(\mathbb Q)=0\). The exceptional numbers are \(\pm1\). The roots of unity in \(\mathbb Q\) are \(\pm1\). By
the proof of Proposition 5.2, a prime \(p\nmid ab\) satisfies \(v_p(q-1)>0\) or \(v_p(q+1)>0\) if and only if
\(\tau_q(p)\) is \([1]\) or \([2]\). So \(X(q)\) is the set of Definition 5.1. The numbers \(e_\pi\) agree with
Definition 4.5: for an odd prime \(p\) over \([1]\) or \([2]\) we have \(\epsilon_0=\epsilon=\pm1\), and for
\(p=2\) we have \(\epsilon_0=1\) for both \(\epsilon=1\) and \(\epsilon=-1\), so \(e_2=v_2(q-1)\).

(b) Let \(\varepsilon>0\). By property (c) there is \(x_0>1\) with
\(\lvert R_1(x)\rvert\le\tfrac{\varepsilon}{4}\log x\) for \(x\ge x_0\). By property (a), \(\lvert R_1\rvert\) is
bounded on \([1,x_0]\), say by \(M\). With property (b) this gives
\(\lvert R_1(x)\rvert\le\tfrac{\varepsilon}{4}\big\lvert\log\lvert x\rvert\big\rvert+M\) for all
\(x\in\mathbb R^\times\). Hence for a real place \(R_1(f_\pi)\le\tfrac\varepsilon4\lvert v_\pi(f)\rvert+M\), and for
a complex place, where \(\lvert v_\pi(f)\rvert=2\big\lvert\log\lvert f_\pi\rvert\big\rvert\),
\(R_2(f_\pi)\le\tfrac\varepsilon4\lvert v_\pi(f)\rvert+2M+\lvert1-\gamma\rvert\). By the product formula the
places with \(v_\pi(f)<0\) contribute \(\deg f\) to \(\sum_\pi\lvert v_\pi(f)\rvert\deg\pi\), as do those with
\(v_\pi(f)>0\). So \(\sum_{\pi\in X_a}\lvert v_\pi(f)\rvert\le2\deg f\), and
\[
\sum_{\pi\in X_a}R_{\varepsilon(\pi)}(f_\pi)\ \le\ \frac\varepsilon2\deg f+n_K\big(2M+\lvert1-\gamma\rvert\big),
\]
where \(n_K\) is the number of archimedean places. Since \(f\) is not exceptional, \(\deg f>0\). So the inequality
of Conjecture 5.11 implies that of Conjecture 5.12 with
\(C=-\chi(K)+n_K(2M+\lvert1-\gamma\rvert)\). \(\square\)

By (5.2), for every rational number \(q\ne0,\pm1\),
\[
(S_4(q)-2)\deg\tau_q=\log\frac{\lvert a^2-b^2\rvert}{2^{\,v_2(a+b)}}-\log\operatorname{rad}\big(ab(a^2-b^2)\big)-1 .
\tag{5.3}
\]
By Proposition 5.13(a), Conjecture 5.11 for \(K=\mathbb Q\) asks for a function \(R_1\) of the real number \(q\)
alone that is at least as large as the number (5.3) for every \(q\), is continuous, and grows more slowly than
\(\log q\). The next proposition shows that no such function exists.

**Lemma 5.14.** Let \(1<c<d\) be coprime integers and \(N\ge1\). There are integers \(r,s\ge1\) with
\[
0<\lvert r\log c-s\log d\rvert<\frac{\log c}{N}.
\]

*Proof.* Let \(\theta=\log d/\log c\), so \(\theta>1\). The \(N+1\) numbers \(j\theta-\lfloor j\theta\rfloor\) with
\(0\le j\le N\) lie in the interval \([0,1)\), which is the union of \(N\) intervals of length \(1/N\). So two of
them, for indices \(j_1<j_2\), differ by less than \(1/N\). Put \(s=j_2-j_1\) and
\(r=\lfloor j_2\theta\rfloor-\lfloor j_1\theta\rfloor\). Then \(\lvert r-s\theta\rvert<1/N\), and
\(r>s\theta-1/N>0\). Multiplying by \(\log c\) gives \(\lvert r\log c-s\log d\rvert<(\log c)/N\). This number is not
zero: \(c^r\) and \(d^s\) are coprime integers greater than \(1\), so they are different. \(\square\)

**Proposition 5.15 (the inequality of Conjecture 5.11 has no solution).**

(a) For every real number \(M\) there is a rational number \(q\) with \(2\le q<4\) and
\((S_4(q)-2)\deg\tau_q>M\).

(b) Let \(1<c<d\) be coprime integers and \(r,s\ge1\). Put \(m=\max(c^r,d^s)\), \(n=\lvert c^r-d^s\rvert\) and
\(q=m/n\). If \(m>2n\), then
\[
(S_4(q)-2)\deg\tau_q\ \ge\ \log q-\log(2cd)-1 .
\]
For every real number \(x_0\ge2\) there are \(r,s\) with \(q>x_0\).

(c) Let \(R_1\colon\mathbb R^\times\to\mathbb R\) be a function with \(S_4(q)\le2+R_1(q)/\deg\tau_q\) for all
rational \(q\ne0,\pm1\). Then \(R_1\) is not bounded on the interval \([2,4]\), and \(R_1(x)/\log x\) does not tend
to \(0\) for \(x\to+\infty\). So \(R_1\) has neither property (a) nor property (c) of Conjecture 5.11, and
Conjecture 5.11 does not hold.

*Proof.* (a) Let \(u\ge1\) and \(N=4\cdot5^{u-1}\). This is the order of the group \((\mathbb Z/5^u)^\times\), so
\(x^N\equiv1\) modulo \(5^u\) for every integer \(x\) prime to \(5\). By Lemma 5.14 there are \(r,s\ge1\) such that
\(\lambda=\lvert r\log2-s\log3\rvert\) satisfies \(0<N\lambda<\log2\). Let \(t\) be the least positive integer with
\(tN\lambda\ge\log2\). Then \(tN\lambda<\log2+N\lambda<2\log2\). Let \(a\) be the larger and \(b\) the smaller of
the two numbers \(2^{tNr}\) and \(3^{tNs}\), and let \(q=a/b\). Then \(\log q=tN\lambda\), so \(2\le q<4\). Both
numbers are \(N\)-th powers of integers prime to \(5\). So \(a\equiv b\equiv1\) modulo \(5^u\), and \(5^u\) divides
\(a^2-b^2\). A positive integer that is divisible by \(5^u\) is at least \(5^{u-1}\) times its radical. The numbers
\(a\), \(b\) and \(a^2-b^2\) are pairwise coprime, \(\operatorname{rad}(ab)=6\), and \(a+b\) is odd. So
\(\operatorname{rad}(ab(a^2-b^2))\le6(a^2-b^2)/5^{u-1}\), and (5.3) gives
\[
(S_4(q)-2)\deg\tau_q\ \ge\ (u-1)\log5-\log6-1 .
\]
This exceeds \(M\) if \(u\) is large.

(b) The integers \(c^r\) and \(d^s\) are coprime, so \(m\) and \(n\) are coprime and \(n\ge1\). So \(q=m/n>2\) is
in lowest terms, with \(H=m\). The numbers \(m\) and \(m-n\) are \(c^r\) and \(d^s\) in some order, so
\(\operatorname{rad}(m)\operatorname{rad}(m-n)\le cd\). Let \(k=(m+n)/2^{v_2(m+n)}\). A prime that divides
\(mn(m-n)(m+n)\) divides \(m\), \(n\), \(m-n\) or \(k\), because \(2\) divides \(m-n\) if it divides \(m+n\). So
\(\operatorname{rad}(mn(m^2-n^2))\le cd\,n\,k\), and (5.3) gives
\[
(S_4(q)-2)\deg\tau_q\ \ge\ \log\big((m-n)k\big)-\log(cd\,n\,k)-1=\log\frac{m-n}{n}-\log(cd)-1 .
\]
Since \(m-n>m/2\), this is at least \(\log q-\log(2cd)-1\). For the last statement let \(N\ge1\). By Lemma 5.14
there are \(r,s\ge1\) such that \(\lambda=\lvert r\log c-s\log d\rvert\) satisfies \(0<\lambda<(\log c)/N\). Then
\(n/m=1-e^{-\lambda}<\lambda\). So \(q=m/n\) exceeds \(x_0\) if \(N\) is large.

(c) By assumption, \(R_1(q)\ge(S_4(q)-2)\deg\tau_q\) for all rational \(q\ne0,\pm1\). By (a), \(R_1\) takes
arbitrarily large values on \([2,4)\). By (b) with \(c=2\) and \(d=3\), there are arbitrarily large rational
numbers \(q\) with \(R_1(q)\ge\log q-\log12-1\), and for them \(R_1(q)/\log q\ge1-(\log12+1)/\log q\). A continuous
function on \(\mathbb R^\times\) is bounded on \([2,4]\). By Proposition 5.13(a), the inequality assumed here is the
inequality of Conjecture 5.11 for \(K=\mathbb Q\). \(\square\)

For example \(q=2^{19}/3^{11}=524288/177147=2.9596\) has \(a-b=347141\), a prime, and
\(a+b=5\cdot7^3\cdot409\). So the number (5.3) is \(2\log7-\log6-1=1.100\), and \(S_4(q)=2.0835\). In (b), the
powers \(3^{12}=531441\) and \(2^{19}\) give \(n=7153\) and \(q=74.30\); here the number (5.3) is \(1.503\), and the
bound of (b) is \(0.823\).

The proof of (a) gives more. Let \(1<x_1<x_2\) be real numbers, and let \(u\) and \(N\) be as in that proof. By
Lemma 5.14 there are \(r,s\ge1\) such that \(\lambda=\lvert r\log2-s\log3\rvert\) satisfies
\(0<N\lambda<\log(x_2/x_1)\). Let \(t\) be the least positive integer with \(tN\lambda\ge\log x_1\). Then
\(tN\lambda<\log x_2\), the numbers \(a,b\) defined as before give \(x_1\le q<x_2\), and the lower bound
\((u-1)\log5-\log6-1\) holds as before. So a function \(R_1\) as in (c) is unbounded on every interval
\([x_1,x_2]\) with \(1<x_1<x_2\).

*Reference:* [Smirnov 1992, §3.4] states Conjecture 5.11. About the function \(R_1\), [Smirnov 1992, §3.3] reports
the following. An earlier version of that paper assumed \(R_1(x)\sim\log\log x\) for \(x\to+\infty\). This came from
a heuristic formula, (3.1) there, which gives \(R_1(x)=\log(1+\log(1/\lvert x\rvert))\) for \(0<\lvert x\rvert<1\),
hence \(\log(1+\log\lvert x\rvert)\) for \(\lvert x\rvert>1\) by property (b); and the first five families of
examples in §4 there seemed to confirm it. A paper of Masser, reference [5] there, forces a larger order of growth,
at least \(\sqrt{\log x}\); see §4.6 there. For this reason that paper keeps, for now, only condition (c).
Reference [5] is [Masser 1990]. It proves that for every \(\delta>0\) there are coprime integers \(a,b,c\) with
\(a+b+c=0\), with \(S=\operatorname{rad}(abc)\) as large as one likes, and with
\(\lvert abc\rvert\ge S^3\exp\big((12-\delta)\sqrt{\log S}/\log\log S\big)\) [Masser 1990, Section 1, Proposition].
It also quotes the theorem of Stewart and Tijdeman (see the reference after Proposition 5.10) in the form
\(\max(\lvert a\rvert,\lvert b\rvert,\lvert c\rvert)\ge S\exp\big((4-\delta)\sqrt{\log S}/\log\log S\big)\), and
this is the statement that [Smirnov 1992, §4.6] uses.

All lower bounds in [Smirnov 1992, §4] are stated in terms of \(m=e^{\deg\tau_q}\). Proposition 5.15 adds two
statements in terms of the real number \(q\). By (b), in the family of [Smirnov 1992, §4.1, Proposition 1] the
number (5.3) is at least \(\log q-\log(2cd)-1\). So a function \(R_1\) that satisfies the inequality has
\(R_1(x)\ge\log x-\log(2cd)-1\) for arbitrarily large \(x\), which excludes condition (c) and the order
\(\log\log x\). By (a), a function of \(q\) alone that satisfies the inequality is unbounded on \([2,4]\), whatever
its growth at infinity; so no continuous function of \(q\) and no locally bounded function of \(q\) can be the
remainder. For the number \(q=2^{19}/3^{11}\) above, the function \(\log(1+\log\lvert x\rvert)\) has the value
\(0.735\), and the number (5.3) is \(1.100\).

The proof uses that \(R_1(q)\) depends on the real number \(q\) and not on \(\deg\tau_q\). It says nothing against
Conjecture 5.3, where the remainder \(\varepsilon\deg\tau_q+C_\varepsilon\) grows with the degree. In (a) the
lower bound \((u-1)\log5-\log6-1\) is smaller than \(\log\deg\tau_q\), because
\(\deg\tau_q=\log a\ge N\log2>5^{u-1}\). The next proposition makes this precise.

**Proposition 5.16 (the remainder as a function of the degree).** Conjecture 5.3 holds if and only if there is a
function \(\rho\colon(0,\infty)\to\mathbb R\) with \(\rho(t)/t\to0\) for \(t\to\infty\) such that
\[
S_4(q)\ \le\ 2+\frac{\rho(\deg\tau_q)}{\deg\tau_q}\qquad\text{for all rational numbers } q\ne0,\pm1 .
\]

*Proof.* Let \(\rho\) be such a function and \(\varepsilon>0\). There is \(t_0\) with \(\rho(t)\le\varepsilon t\) for
\(t\ge t_0\). The numbers \(\deg\tau_q=\log H\) below \(t_0\) are finitely many, because \(H\) is an integer. Let
\(C_\varepsilon\ge0\) be a bound for \(\rho\) on them. Then
\(\rho(\deg\tau_q)\le\varepsilon\deg\tau_q+C_\varepsilon\) for all \(q\), and this gives the inequality of
Conjecture 5.3. Conversely, let \(C_\varepsilon\) be constants as in Conjecture 5.3, and put
\(\rho(t)=\inf_{\varepsilon>0}\max(0,\varepsilon t+C_\varepsilon)\). For every \(q\) and every \(\varepsilon>0\) we
have \((S_4(q)-2)\deg\tau_q\le\varepsilon\deg\tau_q+C_\varepsilon\), hence
\((S_4(q)-2)\deg\tau_q\le\rho(\deg\tau_q)\). And \(0\le\rho(t)/t\le\max(0,\varepsilon+C_\varepsilon/t)\) for every
\(\varepsilon>0\), so \(\rho(t)/t\to0\). \(\square\)

So the statement that is equivalent to the ABC conjecture has a remainder that depends on the height
\(H=e^{\deg\tau_q}\) of \(q\). The inequality of Conjecture 5.11 for \(K=\mathbb Q\) has a remainder that depends
on the archimedean absolute value \(\lvert q\rvert\). This is the difference between the two statements. In terms
of \(\rho\), Proposition 5.10 says \(\rho(t)\ge\log t-1.5\) for \(t=2^k\log3\), and the lower bounds of
[Smirnov 1992, §4] are lower bounds for \(\rho(\log m)\).

## 6. The account in monoid geometry

A reference for this section is [Jarra 2023b]. The spaces of congruences that it uses are those of
[Lorscheid–Ray 2024] and [Jarra 2023a].

Sections 3 and 4 defined a set of points and a map by hand. This section shows that both come from general
constructions with monoids. The set of places becomes a monoidal space. Smirnov's projective line becomes a space
attached to the monoid scheme \(\mathbb P^1_{\mathbb F_1}\), and \(\tau_q\) becomes a continuous map between the
two. The degrees, the ramification indices and the Hurwitz inequality are not part of this account.

### 6.1 The compactification of Spec Z as a monoidal space

We recall three notions from *Monoid schemes*. A *monoidal space* is a topological space with a sheaf of monoids
whose stalks are not the zero monoid. A morphism \(\varphi\colon M\to N\) of nonzero monoids is *local* if
\(\varphi^{-1}(N^\times)=M^\times\). A *morphism of monoidal spaces* is a continuous map together with a morphism of
the sheaves of monoids that is local on all stalks. Forgetting the addition of the structure sheaf of a scheme \(Y\)
gives a monoidal space \(Y^{\mathrm{mon}}\).

**Definition 6.1.** As a set, \(\overline{\operatorname{Spec}\mathbb Z}=\mathcal V\cup\{\eta\}\), where \(\eta\) is
one more point, the *generic point*. For \(x\in\mathbb Q\) put \(\lvert x\rvert_p=p^{-v_p(x)}\),
\(\lvert x\rvert_\infty=\lvert x\rvert\), and \(\lvert x\rvert_\eta=1\) for \(x\ne0\), with
\(\lvert0\rvert_v=0\) for all \(v\). The closed subsets of \(\overline{\operatorname{Spec}\mathbb Z}\) are the whole
space and the finite subsets of \(\mathcal V\). So a non-empty open set contains \(\eta\) and all but finitely many
places. For a non-empty open set \(U\) put
\[
\mathcal O(U)=\{x\in\mathbb Q: \lvert x\rvert_v\le1\ \text{for all } v\in U\},
\]
a submonoid of \((\mathbb Q,\cdot)\), and let \(\mathcal O(\emptyset)\) be the zero monoid. The restriction maps
between non-empty open sets are the inclusions.

**Proposition 6.2.**

(a) \(\mathcal O\) is a sheaf of monoids. Its stalks are \(\mathcal O_\eta=(\mathbb Q,\cdot)\),
\(\mathcal O_p=(\mathbb Z_{(p)},\cdot)\), the monoid of the rational numbers with denominator prime to \(p\), and
\(\mathcal O_\infty=(\mathbb Q\cap[-1,1],\cdot)\). So \(\overline{\operatorname{Spec}\mathbb Z}\) is a monoidal space.

(b) The open subspace \(\overline{\operatorname{Spec}\mathbb Z}\setminus\{\infty\}\), with the restricted sheaf, is
\((\operatorname{Spec}\mathbb Z)^{\mathrm{mon}}\).

(c) The monoid of global sections is \(\{0,1,-1\}=\mathbb F_{1^2}\).

(d) \(\overline{\operatorname{Spec}\mathbb Z}\) is not a monoid scheme.

*Proof.* (a) Let a non-empty open set \(U\) be covered by open sets \(U_i\), and let \(s_i\in\mathcal O(U_i)\) be
sections that agree on the intersections. Empty members of the cover carry the only section of the zero monoid and
can be left out. Two non-empty open sets meet, because both contain \(\eta\), and the restriction maps are
inclusions of subsets of \(\mathbb Q\). So all \(s_i\) are one rational number \(s\), and \(s\in\mathcal O(U)\),
because every \(v\in U\) lies in some \(U_i\). This \(s\) is the only section with the restrictions \(s_i\). The
stalk at a point \(v\) is the union of the monoids \(\mathcal O(U)\) with \(v\in U\). It lies in
\(\{x: \lvert x\rvert_v\le1\}\). Conversely let \(x\ne0\) with \(\lvert x\rvert_v\le1\). The set
\(U_x=\{w: \lvert x\rvert_w\le1\}\) contains \(v\) and \(\eta\), and its complement is finite, because
\(\lvert x\rvert_p=1\) for all primes \(p\) that divide neither the numerator nor the denominator of \(x\). So
\(U_x\) is open and \(x\in\mathcal O(U_x)\). This gives the three stalks, and none of them is the zero monoid.

(b) The point \(\eta\) corresponds to the ideal \((0)\) and \(p\) to \((p)\). The non-empty open subsets of
\(\operatorname{Spec}\mathbb Z\) are the complements of the finite sets of closed points, as here. If \(U\) is the
complement of \(\{p_1,\dots,p_j,\infty\}\), then \(\mathcal O(U)\) is the set of \(x\) with \(v_p(x)\ge0\) for all
primes \(p\) other than the \(p_i\). This is the ring \(\mathbb Z[1/(p_1\cdots p_j)]\) of sections of the structure
sheaf of \(\operatorname{Spec}\mathbb Z\) over \(U\), and on both sides the restriction maps are inclusions.

(c) This is Proposition 2.2(b).

(d) A non-empty affine monoid scheme has exactly one closed point (*Monoid schemes*). An open set that contains a
place contains infinitely many places, and each of them is a closed point of it. So no place has an open
neighbourhood that is an affine monoid scheme. \(\square\)

*Reference:* [Jarra 2023b, Section 4] defines this monoidal space for the ring of integers of any number field.
There \(\mathcal O(U)\) is given by the same formula for all open sets, which for \(U=\emptyset\) gives
\((\mathbb Q,\cdot)\); the sheaf condition requires the zero monoid there.

Part (c) is the analogue of \(H^0(X,\mathcal O_X)=k\) for a curve. The stalk at \(\infty\) is the monoid
\(\mathbb Q\cap[-1,1]\), which is closed under multiplication and not under addition. This is why
\(\overline{\operatorname{Spec}\mathbb Z}\) is a space with a sheaf of monoids and not a scheme.

### 6.2 Strong congruence spaces

We recall from *Commutative monoids and their spectra*: a *congruence* on a monoid \(M\) is an equivalence relation
\(\sim\) such that \(x\sim y\) implies \(xz\sim yz\); the quotient \(M/{\sim}\) is a monoid; the *kernel congruence*
of a morphism \(\varphi\) is the relation \(\varphi(x)=\varphi(y)\); a congruence is *prime* if \(M/{\sim}\) is
cancellative, that is, \(1\not\sim0\), and \(xz\sim yz\) implies \(z\sim0\) or \(x\sim y\). We write
\(\langle x\sim y\rangle\) for the smallest congruence that contains the pair \((x,y)\).

**Definition 6.3.** A monoid is a *domain* if it is isomorphic to a submonoid of \((K,\cdot)\) for some field
\(K\). A *strong prime congruence* on \(M\) is a congruence whose quotient is a domain. The set
\(\operatorname{SCong}M\) of strong prime congruences carries the topology generated by the sets
\(U_{x,y}=\{\sim\ :\ x\not\sim y\}\) for \(x,y\in M\). So the sets \(V_{x,y}=\{\sim\ :\ x\sim y\}\) are closed, and
every closed set is an intersection of finite unions of sets \(V_{x,y}\).

*Reference:* [Jarra 2023a, Definition 3.1]. The space of all prime congruences with this topology is the congruence
space of [Lorscheid–Ray 2024, Definition 2.9].

**Lemma 6.4.**

(a) The closure of a point \(\mathfrak c\) of \(\operatorname{SCong}M\) is the set of all
\(\mathfrak c'\in\operatorname{SCong}M\) with \(\mathfrak c\subseteq\mathfrak c'\).

(b) Let \(\varphi\colon M\to N\) be a morphism and \(\mathfrak c\in\operatorname{SCong}N\). The kernel congruence
\(\varphi^{\ast}\mathfrak c\) of \(M\to N\to N/\mathfrak c\) lies in \(\operatorname{SCong}M\), and
\(\varphi^{\ast}\colon\operatorname{SCong}N\to\operatorname{SCong}M\) is continuous.

(c) Let \(R\) be a ring and \(\varphi\colon M\to(R,\cdot)\) a morphism. The map
\(\operatorname{Spec}R\to\operatorname{SCong}M\) that sends a prime ideal \(\mathfrak p\) to the kernel congruence
of \(M\to(R/\mathfrak p,\cdot)\) is continuous.

*Proof.* (a) If \(\mathfrak c\subseteq\mathfrak c'\), every set \(V_{x,y}\) that contains \(\mathfrak c\) contains
\(\mathfrak c'\), so every closed set that contains \(\mathfrak c\) contains \(\mathfrak c'\). If
\(\mathfrak c\not\subseteq\mathfrak c'\), choose \((x,y)\) in \(\mathfrak c\) and not in \(\mathfrak c'\); then
\(V_{x,y}\) is a closed set that contains \(\mathfrak c\) and not \(\mathfrak c'\). (b) The quotient
\(M/\varphi^{\ast}\mathfrak c\) is isomorphic to a submonoid of \(N/\mathfrak c\), so it is a domain. The preimage
of \(U_{x,y}\) is \(U_{\varphi(x),\varphi(y)}\). (c) The image of \(M\) in \(R/\mathfrak p\) is a submonoid of the
multiplicative monoid of the fraction field of \(R/\mathfrak p\). The preimage of \(U_{x,y}\) is the set of
\(\mathfrak p\) that do not contain \(\varphi(x)-\varphi(y)\), which is open. \(\square\)

*Reference:* [Lorscheid–Ray 2024, Lemma 2.11]; [Jarra 2023a, Lemma 3.7 and Section 4.1].

**Proposition 6.5 (the affine line and the torus over \(\mathbb F_1\)).** Let
\(\mathbb F_1[T]=\{0,1,T,T^2,\dots\}\).

(a) The strong prime congruences on \(\mathbb F_1[T]\) are the trivial congruence \(\mathfrak c_\xi\), which is
equality; \(\mathfrak c_0=\langle T\sim0\rangle\); and \(\mathfrak c_n=\langle T^n\sim1\rangle\) for \(n\ge1\), in
which \(T^i\sim T^j\) if and only if \(n\) divides \(i-j\). The quotients are \(\mathbb F_1[T]\), \(\mathbb F_1\)
and \(\mathbb F_{1^n}\). Every prime congruence on \(\mathbb F_1[T]\) is strong.

(b) The closed subsets of \(\operatorname{SCong}\mathbb F_1[T]\) are the whole space and the sets
\(\{\mathfrak c_n: n\in D\}\cup E\), where \(D\) is a finite set of positive integers that contains every divisor of
each of its elements, and \(E\subseteq\{\mathfrak c_0\}\).

(c) The strong prime congruences on \(\mathbb F_1[T,T^{-1}]\) are the trivial one and
\(\langle T^n\sim1\rangle\) for \(n\ge1\). The map \(\operatorname{SCong}\mathbb F_1[T,T^{-1}]\to
\operatorname{SCong}\mathbb F_1[T]\) of Lemma 6.4(b) is a homeomorphism onto the open subset
\(U_{T,0}\), the complement of \(\mathfrak c_0\).

*Proof.* (a) Let \(\sim\) be a prime congruence on \(\mathbb F_1[T]\). Then \(1\not\sim0\). If \(T^i\sim0\) for some
\(i\ge1\), then \(T\sim0\), because the quotient has no zero divisors. If \(T\sim0\), the classes are \(\{1\}\) and
the set of all other elements, and \(\sim\) is \(\mathfrak c_0\). Suppose \(T\not\sim0\) and \(\sim\) is not
trivial. Then \(T^i\sim T^j\) for some \(i<j\), and cancelling \(T^i\) gives \(1\sim T^{j-i}\). Let \(n\ge1\) be the
least number with \(T^n\sim1\). If \(T^i\sim T^j\) with \(i\le j\), write \(j-i=un+r\) with \(0\le r<n\). Then
\(1\sim T^{j-i}\sim T^r\), so \(r=0\). Hence \(\sim\) is \(\mathfrak c_n\). The three kinds of quotients are
domains: \(\mathbb F_1[T]\) embeds in \((\mathbb Q,\cdot)\) by \(T\mapsto2\), and
\(\mathbb F_1\subset\mathbb F_{1^n}\subset(\mathbb C,\cdot)\).

(b) For \(i\ge1\) the set \(V_{T^i,0}\) is \(\{\mathfrak c_0\}\), and \(V_{1,0}\) is empty. For \(i<j\) the set
\(V_{T^i,T^j}\) consists of the \(\mathfrak c_n\) with \(n\mid j-i\), and of \(\mathfrak c_0\) if \(i\ge1\). So the
sets \(V_{x,y}\) with \(x\ne y\) are \(\emptyset\), \(\{\mathfrak c_0\}\), the sets
\(\{\mathfrak c_n: n\mid m\}\) and these sets with \(\mathfrak c_0\) added. Their finite unions are the sets in the
statement, and this family is stable under intersections.

(c) In a prime congruence on a group with zero no unit is equivalent to \(0\), so the congruence is the coset
relation of the subgroup of the units that are equivalent to \(1\). The subgroups of \(\{T^i: i\in\mathbb Z\}\) are
the trivial one and those generated by \(T^n\), and the quotients are domains as in (a). The map to
\(\operatorname{SCong}\mathbb F_1[T]\) sends \(\langle T^n\sim1\rangle\) to \(\mathfrak c_n\) and the trivial
congruence to \(\mathfrak c_\xi\). The sets \(V_{x,y}\) with \(x\ne y\) of
\(\operatorname{SCong}\mathbb F_1[T,T^{-1}]\) are \(\emptyset\) and the sets
\(\{\langle T^n\sim1\rangle: n\mid m\}\). So the closed sets correspond to the closed sets of the subspace
\(U_{T,0}\) described in (b). \(\square\)

*Reference:* The list in (a) is the case \(n=1\) of [Lorscheid–Ray 2024, Example 2.15].

Recall from *Monoid schemes* that \(\mathbb P^1_{\mathbb F_1}\) is glued from
\(D_0=\operatorname{Spec}\mathbb F_1[T]\) and \(D_\infty=\operatorname{Spec}\mathbb F_1[T^{-1}]\) along
\(\operatorname{Spec}\mathbb F_1[T,T^{-1}]\). It has three points: the closed points \(x_0\in D_0\) and
\(x_\infty\in D_\infty\), and the point \(\xi\), which lies in every non-empty open set. Its non-empty affine open
subsets are \(D_0=\{\xi,x_0\}\), \(D_\infty=\{\xi,x_\infty\}\) and \(D_0\cap D_\infty=\{\xi\}\).

**Definition 6.6.** The *strong congruence space* of a monoid scheme \(X\) is the colimit of the spaces
\(\operatorname{SCong}\mathcal O_X(U)\) over the affine open subsets \(U\) of \(X\)
[Jarra 2023a, Definition 3.8]. For \(X=\mathbb P^1_{\mathbb F_1}\) this is the space
\(\widetilde{\mathbb P}^1_{\mathbb F_1}\) obtained by gluing \(\operatorname{SCong}\mathbb F_1[T]\) and
\(\operatorname{SCong}\mathbb F_1[T^{-1}]\) along \(\operatorname{SCong}\mathbb F_1[T,T^{-1}]\), by the open
embeddings of Proposition 6.5(c). We write \(\tilde\xi\) for the point given by the trivial congruences, \([0]\)
for \(\langle T\sim0\rangle\), \([\infty]\) for \(\langle T^{-1}\sim0\rangle\), and \([n]\) for the point given by
\(\langle T^n\sim1\rangle\).

**Theorem 6.7 (Smirnov's projective line as a strong congruence space).**

(a) The points of \(\widetilde{\mathbb P}^1_{\mathbb F_1}\) are \(\tilde\xi\), \([0]\), \([\infty]\) and \([n]\)
for \(n\ge1\). So \([x]\mapsto[x]\) is a bijection from \(\mathbb P^1_{\mathrm{Sm}}\) onto the set of points other
than \(\tilde\xi\).

(b) The closed subsets are the whole space and the sets \(\{[n]: n\in D\}\cup E\), with \(D\) as in Proposition 6.5(b)
and \(E\subseteq\{[0],[\infty]\}\). In particular the closure of \([n]\) is \(\{[d]: d\mid n\}\); the closed points
are \([0]\), \([\infty]\) and \([1]\); and \(\tilde\xi\) lies in every non-empty open set.

(c) The map \(\pi\colon\widetilde{\mathbb P}^1_{\mathbb F_1}\to\mathbb P^1_{\mathbb F_1}\) with
\(\pi([0])=x_0\), \(\pi([\infty])=x_\infty\) and \(\pi=\xi\) at all other points is continuous.

*Proof.* (a) and (b) follow from Proposition 6.5: a subset of the glued space is closed if and only if its
intersections with the two charts are closed, and the closure of a point is the smallest closed set that contains
it. (c) The preimages of the open sets \(\{\xi\}\), \(D_0\) and \(D_\infty\) are the complements of
\(\{[0],[\infty]\}\), \(\{[\infty]\}\) and \(\{[0]\}\), which are open by (b). \(\square\)

*Reference:* (a) is [Jarra 2023b, Corollary 3.4], which is Theorem A of the Introduction there. The map \(\pi\)
sends a congruence to the prime ideal of the elements equivalent to \(0\)
[Lorscheid–Ray 2024, Proposition 2.14].

So the projective line of Definition 3.2 is not the monoid scheme \(\mathbb P^1_{\mathbb F_1}\), which has three
points, but the space of its strong prime congruences. The points \([n]\) all lie over the generic point \(\xi\):
they are the torsion points of the torus \(\operatorname{Spec}\mathbb F_1[T,T^{-1}]\). The next statement shows
where they come from in the projective line over \(\mathbb Z\).

**Proposition 6.8 (the map from the projective line over \(\mathbb Z\)).** Let \(\mathbb P^1_{\mathbb Z}\) be the
projective line over \(\mathbb Z\) with the coordinate \(T\), covered by \(\operatorname{Spec}\mathbb Z[T]\) and
\(\operatorname{Spec}\mathbb Z[T^{-1}]\). For a point \(x\) of the first chart, with residue field \(\kappa(x)\),
let \(\gamma(x)\) be the kernel congruence of \(\mathbb F_1[T]\to(\kappa(x),\cdot)\), \(T\mapsto T(x)\). For a point
of the second chart use \(T^{-1}\) in the same way. This defines a continuous surjective map
\(\gamma\colon\mathbb P^1_{\mathbb Z}\to\widetilde{\mathbb P}^1_{\mathbb F_1}\), and
\[
\gamma(x)=\begin{cases}[0]&\text{if } T(x)=0,\\ [\infty]&\text{if } T^{-1}(x)=0,\\ [n]&\text{if } T(x)\text{ is a
root of unity of order } n\text{ in }\kappa(x),\\ \tilde\xi&\text{otherwise.}\end{cases}
\]
The preimage of \([n]\) lies in the closed subset where \(\Phi_n(T)=0\).

*Proof.* The kernel congruences are strong, because their quotients are submonoids of \((\kappa(x),\cdot)\). Let
\(u=T(x)\). The kernel congruence of \(T\mapsto u\) is \(\mathfrak c_0\) if \(u=0\), \(\mathfrak c_n\) if \(u\) has
order \(n\) in \(\kappa(x)^\times\), and trivial otherwise. If \(x\) lies in both charts, then \(u\ne0\), and the
two definitions give the same point, because both are restrictions of the kernel congruence of
\(\mathbb F_1[T,T^{-1}]\to(\kappa(x),\cdot)\). On each chart \(\gamma\) is continuous by Lemma 6.4(c). It is
surjective: the generic point goes to \(\tilde\xi\), because \(T\) is not a root of unity in \(\mathbb Q(T)\); the
points with \(T=0\) or \(T^{-1}=0\) go to \([0]\) and \([\infty]\); and the point \(\Phi_n(T)=0\) of the fibre over
\(\mathbb Q\), whose residue field is \(\mathbb Q(\mu_n)\), goes to \([n]\). If \(u\) has order \(n\), then
\(\Phi_n(u)=0\) by the argument in the proof of Proposition 4.3(a). \(\square\)

*Reference:* [Jarra 2023a, Theorem 4.1 and Corollary 4.11] construct such a map \(\gamma\) from the base change to
\(\mathbb Z\) of any monoid scheme to its strong congruence space, and prove that it is surjective.

### 6.3 The map attached to a rational number

**Definition 6.9 (residue monoids).** Let \(v\) be a point of \(\overline{\operatorname{Spec}\mathbb Z}\). Let
\(\mathcal O_v\) be the stalk at \(v\) (Proposition 6.2) and \(\mathfrak m_v=\{x: \lvert x\rvert_v<1\}\) its ideal of
non-units. The *residue monoid* \(\kappa(v)\) and the *reduction* \(\rho_v\colon\mathcal O_v\to\kappa(v)\) are:

- \(\kappa(\eta)=(\mathbb Q,\cdot)\), and \(\rho_\eta\) is the identity;
- \(\kappa(p)=(\mathbb F_p,\cdot)\), and \(\rho_p\) is the reduction modulo \(p\) of \(\mathbb Z_{(p)}\);
- \(\kappa(\infty)=\{0,1,-1\}\), and \(\rho_\infty(x)=x\) if \(\lvert x\rvert=1\), \(\rho_\infty(x)=0\) if
  \(\lvert x\rvert<1\).

Each \(\rho_v\) is a surjective morphism of monoids with \(\rho_v^{-1}(0)=\mathfrak m_v\), and each \(\kappa(v)\) is
a submonoid of the multiplicative monoid of a field. For \(\rho_\infty\): a product has absolute value \(1\) if and
only if both factors have. The monoid \(\kappa(\infty)\) is the quotient of \(\mathcal O_\infty\) by the ideal
\(\mathfrak m_\infty\), and it is the monoid of constants \(\mathbb F_{1^2}\).

*Reference:* [Jarra 2023b, Section 4] writes \(\kappa(v)=\mathcal O_v/\mathfrak m_v\) at every place, for the monoid
\(\mathcal O_v\) and its ideal \(\mathfrak m_v\). Read as the quotient of a monoid by an ideal, this is the monoid
above at \(\infty\). At a prime \(p\) it is the group of units of \(\mathbb Z_{(p)}\) with a zero, which is not
\((\mathbb F_p,\cdot)\), and the embeddings of [Jarra 2023b, Theorem 5.2 and Remark 5.3] do not exist for it:
\(2\) has order \(3\) in \(\mathbb F_7^\times\), so the image of the prime \(7\) is \([3]\), and
\(\mathbb Z_{(7)}^\times\) has no element of order \(3\). They exist for the residue field, which we use.

**Theorem 6.10 (the map of a rational number).** Let \(q\in\mathbb Q^\times\); the values \(q=\pm1\) are allowed.

(a) Let \(v\) be a point of \(\overline{\operatorname{Spec}\mathbb Z}\). If \(q\in\mathcal O_v\), let
\(\check q(v)\) be the kernel congruence of \(\mathbb F_1[T]\to\kappa(v)\), \(T\mapsto\rho_v(q)\). If
\(q^{-1}\in\mathcal O_v\), let \(\check q(v)\) be the kernel congruence of \(\mathbb F_1[T^{-1}]\to\kappa(v)\),
\(T^{-1}\mapsto\rho_v(q^{-1})\). This defines a map
\(\check q\colon\overline{\operatorname{Spec}\mathbb Z}\to\widetilde{\mathbb P}^1_{\mathbb F_1}\).

(b) If \(q\ne\pm1\), then \(\check q(\eta)=\tilde\xi\), and \(\check q(v)=\tau_q(v)\) for every place
\(v\in\mathcal V\).

(c) \(\check q\) is continuous.

(d) There is a morphism of monoidal spaces
\(\psi_q\colon\overline{\operatorname{Spec}\mathbb Z}\to\mathbb P^1_{\mathbb F_1}\) whose map on sections sends
\(T\in\mathcal O(D_0)\) to \(q\) and \(T^{-1}\in\mathcal O(D_\infty)\) to \(q^{-1}\). Its underlying map is
\(\pi\circ\check q\): it sends \(v\) to \(x_0\) if \(\lvert q\rvert_v<1\), to \(x_\infty\) if \(\lvert q\rvert_v>1\),
and to \(\xi\) if \(\lvert q\rvert_v=1\).

(e) Let \(\varphi_q\colon\operatorname{Spec}\mathbb Z\to\mathbb P^1_{\mathbb Z}\) be the morphism of schemes given
by \(T\mapsto q\). Then \(\check q=\gamma\circ\varphi_q\) on
\(\operatorname{Spec}\mathbb Z=\overline{\operatorname{Spec}\mathbb Z}\setminus\{\infty\}\).

*Proof.* (a) At every point, \(\lvert q\rvert_v\le1\) or \(\lvert q\rvert_v\ge1\). The kernel congruences are
strong, because \(\kappa(v)\) is a submonoid of the multiplicative monoid of a field. If \(q\) and \(q^{-1}\) both
lie in \(\mathcal O_v\), then \(u=\rho_v(q)\) is a unit of \(\kappa(v)\) and \(\rho_v(q^{-1})=u^{-1}\); the two
congruences are the restrictions of the kernel congruence of \(\mathbb F_1[T,T^{-1}]\to\kappa(v)\),
\(T\mapsto u\), so they are the same point of \(\widetilde{\mathbb P}^1_{\mathbb F_1}\).

(b) At \(\eta\): \(q^i=q^j\) only for \(i=j\), so the kernel congruence is trivial. At a prime \(p\nmid b\):
\(\rho_p(q)\) is the class of \(ab^{-1}\). It is \(0\) if \(p\mid a\), which gives \(\mathfrak c_0=[0]\). Otherwise
it has order \(n=\operatorname{ord}_p(q)\), which gives \(\mathfrak c_n=[n]\). At a prime \(p\mid b\):
\(\rho_p(q^{-1})=0\), which gives \([\infty]\). At \(\infty\): \(\rho_\infty(q)=0\) if \(\lvert q\rvert<1\), and
\(\rho_\infty(q^{-1})=0\) if \(\lvert q\rvert>1\).

(c) Let \(Z\) be a closed subset other than the whole space. By Theorem 6.7(b), \(Z\) is a finite set of points
different from \(\tilde\xi\). If \(q\ne\pm1\), then \(\check q^{-1}(Z)\) is a finite union of fibres of \(\tau_q\),
by (b). These are finite by Theorem 4.4(c). So \(\check q^{-1}(Z)\) is a finite subset of \(\mathcal V\), which is
closed. For \(q=\pm1\) see Example 6.11.

(d) By *Monoid schemes*, a morphism from a monoidal space \(Y\) to \(\operatorname{Spec}M\) is the same as a
morphism of monoids \(M\to\mathcal O_Y(Y)\); the point \(y\) goes to the prime ideal of the elements of \(M\) whose
image in the stalk at \(y\) is not a unit. Let \(Y_0=\{v: \lvert q\rvert_v\le1\}\) and
\(Y_\infty=\{v: \lvert q\rvert_v\ge1\}\). Both are open, they cover the space, \(q\in\mathcal O(Y_0)\) and
\(q^{-1}\in\mathcal O(Y_\infty)\). So \(T\mapsto q\) defines a morphism \(\psi_0\colon Y_0\to D_0\), and
\(T^{-1}\mapsto q^{-1}\) defines \(\psi_\infty\colon Y_\infty\to D_\infty\). A point \(v\in Y_0\) goes to \(x_0\)
if \(q\) is not a unit of \(\mathcal O_v\), that is if \(\lvert q\rvert_v<1\), and to \(\xi\) otherwise. On
\(Y_0\cap Y_\infty\) both morphisms are the morphism to \(\operatorname{Spec}\mathbb F_1[T,T^{-1}]\) given by
\(T\mapsto q\), so they glue to a morphism \(\psi_q\). The null ideal of \(\check q(v)\) contains \(T\) if and only
if \(\rho_v(q)=0\), that is \(\lvert q\rvert_v<1\). So \(\pi\circ\check q\) is the underlying map of \(\psi_q\).

(e) Since \(a\) and \(b\) are coprime, \(\operatorname{Spec}\mathbb Z\) is covered by the open sets where \(b\),
respectively \(a\), is invertible. The ring homomorphisms \(\mathbb Z[T]\to\mathbb Z[1/b]\), \(T\mapsto q\), and
\(\mathbb Z[T^{-1}]\to\mathbb Z[1/a]\), \(T^{-1}\mapsto q^{-1}\), agree where both are defined, and give
\(\varphi_q\). For a prime \(p\nmid b\) the point \(\varphi_q(p)\) has the residue field \(\mathbb F_p\), and
\(T\) takes the value \(\rho_p(q)\) there. So \(\gamma(\varphi_q(p))=\check q(p)\). The primes that divide \(b\) and
the generic point are treated in the same way. \(\square\)

*Reference:* [Jarra 2023b, Theorem 5.2], which is Theorem B of the Introduction there, for the ring of integers of
a number field and an element that is not exceptional.

By (c) and the proof of (c), the continuity of \(\check q\) is the statement that the fibres of \(\tau_q\) are
finite. By (e), on the primes the map \(\tau_q\) is forced by the general map \(\gamma\). The value at \(\infty\) is
given by the same recipe, with the residue monoid \(\kappa(\infty)=\mathbb F_{1^2}\).

**Example 6.11 (the constants).** For \(q=1\) we have \(\rho_v(1)=1\) at every point, so \(\check q(v)=[1]\) for
all \(v\), the point \(\eta\) included. For \(q=-1\), the element \(\rho_v(-1)\) has order \(2\) in
\(\kappa(v)\), except at \(v=2\), where \(-1=1\) in \(\mathbb F_2\). So \(\check q(v)=[2]\) for \(v\ne2\), and
\(\check q(2)=[1]\). Both maps are continuous: a closed set other than the whole space that contains \([2]\)
contains \([1]\), so the preimage of a closed set is everything, or \(\{2\}\), or empty. On a curve a constant
function is a constant map to a point of degree one. Here the constant \(1\) is the constant map to \([1]\), and
the constant \(-1\) maps to the closure \(\{[2],[1]\}\) of the point \([2]\).

**Remark 6.12 (ramification in the projective line over \(\mathbb Z\)).** Let \(p\nmid b\) and
\(\tau_q(p)=[n]\). The function \(\Phi_n(T)\) on \(\mathbb P^1_{\mathbb Z}\) pulls back under \(\varphi_q\) to the
rational number \(\Phi_n(q)=\Phi_n(a,b)/b^{\varphi(n)}\), and \(v_p(\Phi_n(q))=e_p(q)\) by Lemma 4.7(b). So
\(e_p(q)\) is the order of vanishing at \(p\) of the equation of the curve \(\Phi_n(T)=0\), restricted to the
section \(\varphi_q\) of \(\mathbb P^1_{\mathbb Z}\). By Theorem 4.8(a), for \(n\ge3\) this restriction vanishes at
the primes of the fibre \(\tau_q^{-1}([n])\) and at most at one more prime, \(P(n)\). There
\(\gamma(\varphi_q(P(n)))\) is not \([n]\) but a point \([d]\) with \(d\) a proper divisor of \(n\).

### 6.4 The extensions of \(\mathbb F_1\) and quotients by Galois groups

Let \(F\) be a submonoid of \(\mathbb F_{1^\infty}=\{0\}\cup\mu_\infty\). Every element of \(F^\times=F\setminus\{0\}\)
has finite order, so \(F^\times\) is a subgroup of \(\mu_\infty\). Examples are \(\mathbb F_{1^N}\) and
\(\mathbb F_{1^\infty}\). Let \(F[T]\) be the monoid that consists of \(0\) and the monomials \(\lambda T^i\) with
\(\lambda\in F^\times\) and \(i\ge0\), and define \(F[T^{-1}]\) and \(F[T,T^{-1}]\) in the same way. For
\(\zeta\in\mu_\infty\) let \(\operatorname{ord}_F(\zeta)\) be the least \(w\ge1\) with \(\zeta^w\in F\).

**Definition 6.13.** Let \(A\) be a monoid that contains \(F\) as a submonoid. An *\(F\)-congruence* on \(A\) is a
strong prime congruence in which no two different elements of \(F\) are equivalent. The space
\(\operatorname{SCong}_FA\) is the set of \(F\)-congruences with the topology induced from
\(\operatorname{SCong}A\). The space \(\widetilde{\mathbb P}^1_F\) is glued from
\(\operatorname{SCong}_FF[T]\) and \(\operatorname{SCong}_FF[T^{-1}]\) along
\(\operatorname{SCong}_FF[T,T^{-1}]\).

*Reference:* [Jarra 2023a, Definition 3.1]; [Jarra 2023b, Section 3].

**Theorem 6.14 (the points of \(\widetilde{\mathbb P}^1_F\)).** Let \(F\subseteq\mathbb F_{1^\infty}\) be a
submonoid. Call a pair \((n,\lambda)\) with \(n\ge1\) and \(\lambda\in F^\times\) *admissible* if for every prime
\(p\) that divides \(n\) and satisfies \(\mu_p\subseteq F\), the element \(\lambda\) is not a \(p\)-th power of an
element of \(F\).

(a) The \(F\)-congruences on \(F[T]\) are the trivial congruence, \(\langle T\sim0\rangle\), and the congruences
\(\mathfrak c_{n,\lambda}=\langle T^n\sim\lambda\rangle\) for the admissible pairs \((n,\lambda)\). Different
admissible pairs give different congruences.

(b) For \(\zeta\in\mu_\infty\) the kernel congruence of \(F[T]\to\mathbb F_{1^\infty}\), \(T\mapsto\zeta\), is
\(\mathfrak c_{n,\lambda}\) with \(n=\operatorname{ord}_F(\zeta)\) and \(\lambda=\zeta^n\). Every admissible pair
arises in this way.

(c) Two elements \(\zeta,\zeta'\in\mu_\infty\) give the same congruence in (b) if and only if
\(\zeta'=\sigma(\zeta)\) for some \(\sigma\) in the group \(G_F=\{\sigma\in G: \sigma(x)=x\text{ for all } x\in F\}\).

So the points of \(\widetilde{\mathbb P}^1_F\) are the generic point given by the trivial congruences, \([0]\),
\([\infty]\), and one point \([n,\lambda]\) for every admissible pair. The map
\[
\Phi_F\colon\mathbb P^1(\mathbb F_{1^\infty})\to\widetilde{\mathbb P}^1_F,\qquad0\mapsto[0],\quad
\infty\mapsto[\infty],\quad\zeta\mapsto[\operatorname{ord}_F(\zeta),\zeta^{\operatorname{ord}_F(\zeta)}],
\]
is a surjection onto the set of non-generic points, and its fibres are the orbits of \(G_F\).

*Proof.* *Step 1: the shape of an \(F\)-congruence.* Let \(\sim\) be an \(F\)-congruence on \(F[T]\). If
\(T\sim0\), then every \(\lambda T^i\) with \(i\ge1\) is equivalent to \(0\), the elements of \(F\) are pairwise
inequivalent, and \(\sim\) is \(\langle T\sim0\rangle\), with quotient \(F\). Let \(T\not\sim0\). Then no
\(\lambda T^i\) is equivalent to \(0\), because the quotient has no zero divisors. Suppose
\(\lambda T^i\sim\lambda'T^j\) with \(i\le j\). Cancelling gives \(T^{j-i}\sim\lambda/\lambda'\); if \(i=j\) this
forces \(\lambda=\lambda'\). So if \(\sim\) is not trivial, there is a least \(n\ge1\) with \(T^n\sim\lambda\) for
some \(\lambda\in F^\times\), and \(\lambda\) is unique. Division with remainder, as in the proof of
Proposition 6.5(a), shows
\[
\lambda'T^i\sim\lambda''T^j\iff n\mid j-i\ \text{ and }\ \lambda'=\lambda''\lambda^{(j-i)/n}. \tag{6.1}
\]
The relation (6.1) is the smallest congruence that contains \((T^n,\lambda)\). So
\(\sim\ =\mathfrak c_{n,\lambda}\), and \((n,\lambda)\) is determined by \(\sim\). For every \(n\ge1\) and
\(\lambda\in F^\times\), (6.1) defines a congruence whose quotient is a group with zero \(Q\), which contains
\(F\); the class \(t\) of \(T\) satisfies \(t^n=\lambda\), and \(t^w\notin F\) for \(0<w<n\). It remains to decide
when \(Q\) is a domain.

*Step 2: if \(Q\) is a domain, then \((n,\lambda)\) is admissible.* Let \(p\) be a prime that divides \(n\), with
\(\mu_p\subseteq F\) and \(\lambda=\theta^p\) for some \(\theta\in F\). The \(p\) elements \(\theta\epsilon\) with
\(\epsilon\in\mu_p\) lie in \(F\), and the \(p\) elements \(t^{n/p}\epsilon\) do not. All \(2p\) elements have the
\(p\)-th power \(\lambda\). In a submonoid of the multiplicative monoid of a field the equation \(x^p=\lambda\) has
at most \(p\) solutions. So \(Q\) is not a domain.

*Step 3: if \((n,\lambda)\) is admissible, there is \(\omega\in\mu_\infty\) with \(\omega^n=\lambda\) and
\(\operatorname{ord}_F(\omega)=n\).* Choose \(\omega_0\in\mu_\infty\) with \(\omega_0^n=\lambda\). The other
solutions are \(\omega=\omega_0\epsilon\) with \(\epsilon\in\mu_n\). The set of \(w\in\mathbb Z\) with
\(\omega^w\in F\) is a subgroup that contains \(n\), so \(\operatorname{ord}_F(\omega)\) divides \(n\), and it is
\(n\) if and only if \(\omega^{n/p}\notin F\) for every prime \(p\mid n\). Fix such a \(p\). The element
\(\omega^{n/p}=\omega_0^{n/p}\epsilon^{n/p}\) is a \(p\)-th root of \(\lambda\), and \(\epsilon^{n/p}\) depends only
on the component \(\epsilon_p\) of \(\epsilon\) in the \(p\)-primary part of \(\mu_n\); as \(\epsilon_p\) varies,
\(\epsilon^{n/p}\) takes every value in \(\mu_p\). If \(\lambda\) is not a \(p\)-th power in \(F\), no \(p\)-th root
of \(\lambda\) lies in \(F\), and every \(\epsilon_p\) is good. Otherwise \(\mu_p\not\subseteq F\) by
admissibility, so \(\mu_p\cap F=\{1\}\), exactly one \(p\)-th root of \(\lambda\) lies in \(F\), and exactly one
value of \(\epsilon^{n/p}\) has to be avoided. The components \(\epsilon_p\) for the different primes can be chosen
independently. So a suitable \(\epsilon\) exists.

*Step 4: proof of (a) and (b).* The trivial congruence is an \(F\)-congruence, because
\(\lambda T^i\mapsto2^i\lambda\) embeds \(F[T]\) in \((\mathbb C,\cdot)\). The congruence \(\langle T\sim0\rangle\) is
one, because its quotient is \(F\). Let \(\zeta\in\mu_\infty\), \(n=\operatorname{ord}_F(\zeta)\) and
\(\lambda=\zeta^n\). The kernel congruence of \(T\mapsto\zeta\) is an \(F\)-congruence with \(T\not\sim0\), and it
is not trivial. By Step 1 it is \(\mathfrak c_{n',\lambda'}\), where \(n'\) is the least exponent with
\(\zeta^{n'}\in F\); so \(n'=n\) and \(\lambda'=\lambda\). Its quotient is a submonoid of
\((\mathbb C,\cdot)\), so by Step 2 the pair is admissible. Conversely let \((n,\lambda)\) be admissible and
\(\omega\) as in Step 3. Then \(\mathfrak c_{n,\lambda}\) is the kernel congruence of \(T\mapsto\omega\), so it is
an \(F\)-congruence. With Step 1 this proves (a) and (b).

*Step 5: proof of (c).* An element \(\sigma\in G_F\) fixes \(F\), so \(\sigma(\zeta)^w\in F\) if and only if
\(\zeta^w\in F\), and \(\sigma(\zeta)^n=\sigma(\zeta^n)=\zeta^n\). So \(\zeta\) and \(\sigma(\zeta)\) give the same
pair. Conversely let \(\zeta,\zeta'\) give the same pair \((n,\lambda)\). Let \(S\) be the subgroup of
\(\mu_\infty\) generated by \(F^\times\) and \(\zeta\). Every element of \(S\) is \(\lambda'\zeta^i\) with
\(\lambda'\in F^\times\), and by (6.1), \(\lambda'\zeta^i=\lambda''\zeta^j\) if and only if
\(\lambda'\zeta'^{\,i}=\lambda''\zeta'^{\,j}\). So \(\lambda'\zeta^i\mapsto\lambda'\zeta'^{\,i}\) is an injective
homomorphism \(\sigma_0\) from \(S\) to \(\mu_\infty\) that fixes \(F^\times\). For each \(N\) the finite group
\(S\cap\mu_N\) is cyclic, \(\sigma_0\) maps it to itself, because a finite subgroup of \(\mu_\infty\) is determined
by its order, and \(\sigma_0\) acts on it by \(x\mapsto x^u\) for some \(u\) prime to its order. Such a \(u\) is
the reduction of an element of \((\mathbb Z/N)^\times\). So the set \(\Sigma_N\) of the elements of
\((\mathbb Z/N)^\times=\operatorname{Aut}(\mu_N)\) that agree with \(\sigma_0\) on \(S\cap\mu_N\) is finite and not
empty, and for \(N\mid N'\) reduction maps \(\Sigma_{N'}\) to \(\Sigma_N\). The inverse limit of these sets is not
empty. To see this, put \(N_k=k!\). For fixed \(k\) the images of \(\Sigma_{N_j}\) in \(\Sigma_{N_k}\), for
\(j\ge k\), form a decreasing sequence of non-empty finite sets, so they are equal to one set \(\Sigma'_k\) for all
large \(j\). Every element of \(\Sigma'_k\) is the image of an element of \(\Sigma'_{k+1}\), because for large \(j\)
the map \(\Sigma_{N_j}\to\Sigma_{N_k}\) factors through \(\Sigma_{N_{k+1}}\). So one can choose
\(u_k\in\Sigma'_k\) step by step such that \(u_{k+1}\) reduces to \(u_k\). The automorphisms of the fields
\(\mathbb Q(\mu_{N_k})\) given by the \(u_k\) are compatible, and \(\mathbb Q(\mu_\infty)\) is the union of these
fields. So they define an element \(\sigma\) of \(G\), and \(\sigma\) agrees with \(\sigma_0\) on every
\(S\cap\mu_{N_k}\), hence on \(S\). It fixes \(F\) and maps \(\zeta\) to \(\zeta'\).

The statements about \(\widetilde{\mathbb P}^1_F\) follow. The chart \(F[T^{-1}]\) is treated in the same way. An
\(F\)-congruence on the group with zero \(F[T,T^{-1}]\) is the coset relation of a subgroup of the group of units
that contains no element of \(F^\times\) other than \(1\). Such a subgroup maps injectively to the group of the
powers of \(T\), so it is trivial or generated by one element \(\lambda^{-1}T^n\). So the congruence is trivial or
generated by one relation \(T^n\sim\lambda\), and the points \([n,\lambda]\) of the two charts are identified as
for \(\mathbb F_1\). \(\square\)

*Reference:* [Jarra 2023b, Lemma 3.2 and Proposition 3.3] state the classification (a) with the condition that
\(\theta^d\ne\lambda\) for every divisor \(d>1\) of \(n\) and every \(\theta\in F\). For \(F=\mathbb F_1\) this
excludes every \(n>1\), but \(\langle T^2\sim1\rangle\) has the quotient \(\mathbb F_{1^2}\), a domain
(Proposition 6.5(a)); so we prove the classification with the condition of admissibility. The description of the
fibres of \(\Phi_F\) by \(\operatorname{ord}_F\) is stated in [Jarra 2023b, Section 3].

**Examples 6.15.**

(a) \(F=\mathbb F_1\): no prime \(p\) has \(\mu_p\subseteq F\), every pair \((n,1)\) is admissible, and
Theorem 6.14 gives Theorem 6.7(a) again. The fibre of \(\Phi_{\mathbb F_1}\) over \([n]=[n,1]\) is the set of roots
of unity of order \(n\). So \(\deg[n]=\varphi(n)\) is the number of geometric points over \([n]\)
[Jarra 2023b, Remark 3.6].

(b) \(F=\mathbb F_{1^\infty}\): every prime \(p\) has \(\mu_p\subseteq F\), and every element of \(F\) is a
\(p\)-th power. So only \(n=1\) is admissible, the non-generic points are \([0]\), \([\infty]\) and
\([1,\lambda]\) for \(\lambda\in\mu_\infty\), and \(\Phi_F\) is a bijection from
\(\mathbb P^1(\mathbb F_{1^\infty})\) onto them [Jarra 2023b, Corollary 3.5].

(c) \(F=\mathbb F_{1^2}\): the only prime to consider is \(2\), and \(1\) is a square in \(F\) while \(-1\) is not.
The admissible pairs are \((n,1)\) with \(n\) odd and \((n,-1)\) with \(n\) arbitrary.

**Theorem 6.16 (quotients by Galois groups).** Let \(\Gamma\) be a subgroup of \(G\), and let
\(F=F_\Gamma\) consist of \(0\) and the roots of unity that are fixed by every element of \(\Gamma\).

(a) \(\Phi_F\) is constant on the orbits of \(\Gamma\). So it induces a surjection \(b_\Gamma\) from
\(\mathbb P^1_\Gamma\) onto the set of non-generic points of \(\widetilde{\mathbb P}^1_F\).

(b) \(b_\Gamma\) is bijective if and only if \(\Gamma\) and \(G_F\) have the same image in
\((\mathbb Z/N)^\times\) for every \(N\ge1\). This holds if and only if the fixed field of \(\Gamma\) in
\(\mathbb Q(\mu_\infty)\) is generated by roots of unity.

(c) \(b_\Gamma\) is bijective for \(\Gamma=G\), where \(F=\mathbb F_{1^2}\); for \(\Gamma=\Gamma_N\), where
\(F^\times=\mu_N\) if \(N\) is even and \(F^\times=\mu_{2N}\) if \(N\) is odd; and for the trivial group, where
\(F=\mathbb F_{1^\infty}\).

(d) Let \(\Gamma\) be the group of all \(\sigma\in G\) with \(\sigma(\sqrt2)=\sqrt2\). Then \(F=\mathbb F_{1^2}\),
and \(b_\Gamma\) is not injective: the four roots of unity of order \(8\) form two points of
\(\mathbb P^1_\Gamma\) and one point \([4,-1]\) of \(\widetilde{\mathbb P}^1_F\).

*Proof.* (a) \(\Gamma\subseteq G_F\), and \(\Phi_F\) is constant on the orbits of \(G_F\) and surjective, by
Theorem 6.14.

(b) By Theorem 6.14(c), \(b_\Gamma\) is injective if and only if every orbit of \(G_F\) on \(\mu_\infty\) is an orbit
of \(\Gamma\). Let \(\zeta\) have order \(N\). The group \((\mathbb Z/N)^\times\) acts freely on the roots of unity
of order \(N\). So the orbit of \(\zeta\) under a subgroup of \(G\) has as many elements as the image of the
subgroup in \((\mathbb Z/N)^\times\). Since \(\Gamma\subseteq G_F\), the two orbits of \(\zeta\) agree if and only
if the two images agree. For the second statement let \(E\) be the fixed field of \(\Gamma\) and
\(E_F=\mathbb Q(F^\times)\subseteq E\). The image of \(\Gamma\) in
\(\operatorname{Gal}(\mathbb Q(\mu_N)/\mathbb Q)\) is a subgroup with the fixed field \(E\cap\mathbb Q(\mu_N)\). The
group \(G_F\) is \(\operatorname{Gal}(\mathbb Q(\mu_\infty)/E_F)\), its fixed field is \(E_F\)
[Stacks, Tag [0BML](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-theorem-inifinite-galois-theory)], and so its image has the fixed field \(E_F\cap\mathbb Q(\mu_N)\). By the Galois correspondence
for \(\mathbb Q(\mu_N)/\mathbb Q\) [Stacks, Tag [09DW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-theorem-galois-theory)], the two images agree if and only if
\(E\cap\mathbb Q(\mu_N)=E_F\cap\mathbb Q(\mu_N)\). This holds for all \(N\) if and only if \(E=E_F\).

(c) Let \(\Gamma=\Gamma_N\). Then \(\mu_N\subseteq F\), so \(G_F\subseteq\Gamma_N\subseteq G_F\). The elements of
\(F^\times\) are the points of degree one of \(\mathbb P^1_{\Gamma_N}\) in \(\mu_\infty\), which are given by
Proposition 3.3(b). The group \(G\) is \(\Gamma_1\). For the trivial group, \(G_F\) is trivial.

(d) Let \(\zeta=e^{2\pi i/8}\). Then \(\sqrt2=\zeta+\zeta^{-1}\). If \(\sigma\in G\) acts on \(\mu_8\) by
\(\zeta\mapsto\zeta^u\), then \(\sigma(\sqrt2)=\zeta^u+\zeta^{-u}\), which is \(\sqrt2\) for
\(u\equiv\pm1\) and \(-\sqrt2\) for \(u\equiv\pm3\) modulo \(8\). So \(\Gamma\) is the group of the \(\sigma\) that
act on \(\mu_8\) by \(u\equiv\pm1\). Let \(\epsilon\in F^\times\) have order \(M\), and let \(L\) be the least
common multiple of \(M\) and \(8\). There is \(\sigma\in G\) that acts on \(\mu_L\) by \(x\mapsto x^{-1}\). It lies
in \(\Gamma\), so \(\epsilon=\sigma(\epsilon)=\epsilon^{-1}\), and \(M\) divides \(2\). Hence
\(F=\{0,1,-1\}\) and \(G_F=G\). Every root of unity \(z\) of order \(8\) has \(\operatorname{ord}_F(z)=4\) and
\(z^4=-1\), so \(\Phi_F(z)=[4,-1]\). The orbits of \(\Gamma\) on these roots are \(\{\zeta,\zeta^{-1}\}\) and
\(\{\zeta^3,\zeta^{-3}\}\). \(\square\)

*Reference:* [Jarra 2023b, Theorem 3.8 and Remark 3.10], which give Theorem D of the Introduction there, state that
\(b_\Gamma\) is bijective for every closed subgroup \(\Gamma\) of \(G\). The group of (d) is closed: it is the
preimage of a subgroup of \((\mathbb Z/8)^\times\). So this fails, and we prove the criterion (b), which holds for all
subgroups. For the group \(\Gamma_K\) of a number field \(K\) (Definition 3.2) the criterion says that the field
\(K\cap\mathbb Q(\mu_\infty)\) is generated by roots of unity. It fails for \(K=\mathbb Q(\sqrt2)\).

**Remark 6.17 (the topologies).** The bijections of Theorem 6.16 are not homeomorphisms in general. The map
\(\Phi_F\) is the restriction of congruences from \(\mathbb F_{1^\infty}[T]\) to \(F[T]\), extended to the generic
points; it is continuous by Lemma 6.4(b).

1. In \(\widetilde{\mathbb P}^1_{\mathbb F_{1^\infty}}\) every point \([1,\lambda]\) is closed, because
   \(\{[1,\lambda]\}=V_{T,\lambda}\). So in the quotient of this space by \(G\) every orbit \([n]\) is a closed
   point. In \(\widetilde{\mathbb P}^1_{\mathbb F_{1^2}}\), the target of \(b_G\), the point \([3,1]\) lies in the
   closure of \([9,1]\), by Lemma 6.4(a): \(\langle T^9\sim1\rangle\subseteq\langle T^3\sim1\rangle\). So \(b_G\)
   is a continuous bijection for the quotient topology, and not a homeomorphism. This is the conclusion of
   [Jarra 2023b, Remark 3.9], where the two points are named in the opposite order.
2. Restriction of congruences from \(\mathbb F_{1^2}[T]\) to \(\mathbb F_1[T]\) gives a continuous map
   \(\widetilde{\mathbb P}^1_{\mathbb F_{1^2}}\to\widetilde{\mathbb P}^1_{\mathbb F_1}\). By (6.1) it sends
   \([n,1]\) to \([n]\) and \([n,-1]\) to \([2n]\). By Example 6.15(c) it is bijective. It is not a homeomorphism:
   the point \([1,-1]\) is closed, because \(\{[1,-1]\}=V_{T,-1}\), but its image \([2]\) is not closed
   (Theorem 6.7(b)). *Reference:* [Jarra 2023b, Remark 3.7] states that this map is a homeomorphism.

## 7. What is proved and what is open

### 7.1 The two sides

| | Curve \(X\) over \(k\), function \(f\) | The integers, rational number \(q\) |
|---|---|---|
| The map | a morphism \(X\to\mathbb P^1_k\) | the map \(\tau_q\) (Definition 4.1); a continuous map and a morphism of monoidal spaces (Theorem 6.10) |
| Its fibres | finite and non-empty | finite (Theorem 4.4); non-empty except over at most two points (Corollary 4.11) |
| Degree of a fibre | \(\deg f\cdot\deg Q\), by (K1) | \(\deg\tau_q\) over \([0]\) and \([\infty]\) (Proposition 4.6); \(\varphi(n)\deg\tau_q\) up to an error over \([n]\) (Theorem 4.8) |
| Ramification indices | positive integers | positive integers at the primes, a positive real number at \(\infty\) |
| Hurwitz inequality | a theorem (Corollary 1.2) | a conjecture (Conjecture 5.3), equivalent to the ABC conjecture (Corollary 5.9) |
| Remainder term | \(-\chi(X)/\deg f\) | \(\varepsilon+C_\varepsilon/\deg\tau_q\); \(\varepsilon\) is needed (Proposition 5.10), and no term \(R_1(q)/\deg\tau_q\) with a continuous function \(R_1\) can replace it (Proposition 5.15) |
| Consequence for three points | the theorem of Mason and Stothers | the ABC conjecture |
| Source of the proof | differentials and the degree \(2g-2\) of (K2) | no analogue is known |

On the side of the integers the following are theorems of this lesson: the statements on the fibres of \(\tau_q\)
and their degrees (Section 4); the closed formulas for the defect sums, the bounds \(S_3(q)\le3-1/\log H\) and
\(S_4(q)<4\), the equivalence of Conjecture 5.3 with the ABC conjecture, and the failure of Conjecture 5.11
(Section 5); and the description of the spaces and of the map in monoid geometry (Section 6). The Hurwitz
inequality itself is not proved. The bound \(S_3(q)<3\) is trivial, and the conjecture asks for
\(2+\varepsilon\). By Theorem 5.6, already one inequality
\(S_3(q)\le2+\varepsilon+C_\varepsilon/\deg\tau_q\) with a fixed \(\varepsilon<1\) gives
\(C\le K\operatorname{rad}(ABC)^{1/(1-\varepsilon)}\) for all coprime positive \(A+B=C\). Stewart and Tijdeman state the existence of a bound of this kind, with some exponent, as a problem posed by Oesterlé, and prove \(\log C<c\operatorname{rad}(ABC)^{15}\) with a constant \(c\) [Stewart–Tijdeman 1986, Theorem 1]. A later theorem of Stewart and Yu gives \(\log C<c\,R^{1/3}(\log R)^3\), with \(R=\operatorname{rad}(ABC)\) and an effectively computable constant \(c\) [Stewart–Yu 2001, Theorem 1]; in particular \(\log C\) is at most a constant, depending on \(\varepsilon\), times \(R^{1/3+\varepsilon}\).
In terms of defects this improves the bound \(S_3(q)\le3-1/\log H\) only by a term of the order
\(\log\log H/\log H\).

### 7.2 Sharpness: the examples of Smirnov

Proposition 5.10 shows that the constant \(2\) in Conjecture 5.3 cannot be replaced by a smaller one, and that the
remainder cannot be \(C/\deg\tau_q\) with a constant \(C\): for \(q=3^{2^k}\) the defect sum exceeds \(2\) by
\((\log\log m-1.5)/\log m\), where \(m=e^{\deg\tau_q}\). [Smirnov 1992, §4] contains six families of this kind.
In each of them \(q=m/n>1\), and the statement is a lower bound for \(S_4(q)\) for infinitely many members of the
family.

1. *Proposition 1 (the torus).* Fix coprime integers \(a>b>1\). For infinitely many pairs \((r,s)\), which the
   proof takes among the convergents \(s/r\) from below of \(\log a/\log b\), the number \(q=a^r/(a^r-b^s)\)
   satisfies \(S_4(q)\ge2+\log\log m/\log m-\text{const}/\log m\). Here \(\delta_{[0]}\) and \(\delta_{[1]}\) tend
   to \(1\). Proposition 5.15(b) proves the bound \(S_4(q)\ge2+(\log q-\log(2ab)-1)/\log m\) for these numbers,
   if \(q>2\).
2. *Proposition 2 (Pythagorean triples).* The same bound holds for \(q=c^2/b^2\), for infinitely many
   Pythagorean triples with hypotenuse \(c\) and a leg \(b\). The proof there uses the triples
   \((2xy,\ x^2-y^2,\ x^2+y^2)\) with \(x=2^r\), \(y=2^r-1\) and \(r=2\cdot3^\alpha\), and the leg
   \(b=x^2-y^2\). The lower bounds for the defects at \([\infty]\), \([1]\), \([0]\) tend to \(3/4\), \(3/4\),
   \(1/2\).
3. *Propositions 3, 4 and 5 (elliptic curves).* Let \(P_1\) be a rational point of infinite order on one of the
   curves \(AX^3+AY^3=BZ^3\); \(AY^2Z^2=B(X^4-Z^4)\); \(A(X^2+Y^2)=BZ^2,\ C(X^2-Y^2)=DT^2\). Let \(x_r,y_r,z_r\) be
   coprime integer coordinates of the multiple \(rP_1\). For \(q=Bz_r^3/(Ay_r^3)\), respectively
   \(q=Bx_r^4/(Ay_r^2z_r^2)\), respectively \(q=x_r^2/y_r^2\), and infinitely many \(r\):
   \(S_4(q)\ge2+\tfrac12\log\log m/\log m-\text{const}/\log m\). The lower bounds for the defects tend to
   \(2/3,2/3,2/3,0\) for the first curve, to \(3/4,3/4,1/2,0\) for the second, and to \(1/2,1/2,1/2,1/2\) for the
   third. The third family is the only one in which the fibre over \([2]\) enters the lower bound.
4. *Proposition 6.* From the theorem of Stewart and Tijdeman on triples \(a+b+c=0\), in the form quoted in [Masser 1990, Section 1]: for all
   \(\varepsilon,\delta>0\) there are infinitely many coprime pairs \(m>n>0\) with
   \(S_4(m/n)\ge2+(4-\delta)(\log m)^{1/2-\varepsilon}/\log m-\text{const}/\log m\).

So the excess over \(2\) can be of the order \(\log\log m/\log m\) in explicit families, and it is at least of the
order \((\log m)^{-1/2-\varepsilon}\) infinitely often. [Smirnov 1992, §3.3] explains the excess as wild
ramification at the place \(\infty\). It reports that an earlier version assumed \(R_1(x)\sim\log\log x\) for the
function of Conjecture 5.11, that a paper of Masser forces a larger order of growth, and that for this reason only
condition (c) is kept for now; the details are in the reference after Proposition 5.15. By Proposition 5.15 no
continuous function of the real number \(q\) bounds the number \((S_4(q)-2)\deg\tau_q\): it takes arbitrarily large
values for \(2\le q<4\). As a function of the degree, the remainder is the one of Conjecture 5.3
(Proposition 5.16). Apart from the bound of Proposition 5.15(b), the lesson does not prove the statements of this
list.

### 7.3 The status of the conjectures

- *Conjecture 5.3.* By Corollary 5.9 it is equivalent to the ABC conjecture, in all of its forms: with three or
  four points, for all \(q\) or for \(q>1\). So its status is that of the ABC conjecture.
  [Lorscheid 2018b, Section 3] reports that a proof of the ABC conjecture has been claimed by Mochizuki, and that its
  acceptance by the community at large was not clear at the time of writing. According to the same section, that
  proof follows a different line of thought, and it contains ideas from \(\mathbb F_1\)-geometry.
- *Conjecture 5.12.* For \(K=\mathbb Q\) it is Conjecture 5.3. For other number fields the lesson proves nothing
  about it.
- *Conjecture 5.11.* It does not hold: by Proposition 5.15 there is no function \(R_1\) with the required
  properties, already for \(K=\mathbb Q\). For \(K=\mathbb Q\), a remainder that is a function of the degree in
  place of the archimedean value gives Conjecture 5.3 (Proposition 5.16). For other number fields the lesson does not
  examine which remainder term could take its place.
- *Consequences.* [Smirnov 1992, §5] derives further statements: from \(B(\mathbb Q)\), an inequality of Szpiro type
  for stable elliptic curves over \(\mathbb Q\) (Theorem 2 there) and a lower bound for
  \(\lvert a\log m-b\log n\rvert\) (Theorem 3 there); from Conjecture A, a bound for the primes \(p\) with
  \(q^p\equiv q\) modulo \(p^2\) (Theorem 4 there), which are the ramified primes of Proposition 4.12. By
  Corollary 5.9 the first two are consequences of the ABC conjecture. The third is derived there from
  Conjecture 5.11, which does not hold; the lesson does not examine whether it follows from a weaker statement.
- *What is missing.* For a curve, the Hurwitz inequality is proved with the differential \(df\) and the degree of the
  canonical divisor. Nothing of this kind is defined for \(\overline{\operatorname{Spec}\mathbb Z}\) in this lesson:
  Section 6 provides spaces and maps, but no degrees, no ramification and no differentials.
  [Smirnov 1992, §3 and Conclusion, item 6] says the same about the theory there: only the tame part of the defect
  is defined, the full defect is not, and the main difficulty is to define the order of the derivative of an
  element of a local field with respect to a local parameter.

For the lesson *What a unified theory must contain*, the requirements that come from this lesson are three. First,
objects \(\overline{\operatorname{Spec}\mathbb Z}\) and \(\mathbb P^1\) over \(\mathbb F_1\) such that every
rational number \(q\ne0,\pm1\) defines a morphism between them; Theorem 6.10 provides this on the level of
monoidal spaces and of spaces of congruences. Second, degrees and ramification indices for which the degree of every
fibre is \(\deg\tau_q\) times the degree of the point; Theorem 4.8 shows that the definitions of Section 4 satisfy
this only approximately over the points \([n]\). Third, an invariant that plays the role of \(2g-2\) and a proof of
the inequality; by Corollary 5.9 such a proof would be a proof of the ABC conjecture. By Proposition 5.15 the
remainder term of the inequality cannot be a locally bounded function of the real number \(q\) alone. So it is not a
contribution of the place \(\infty\) of the kind proposed in [Smirnov 1992, §3.3]. If the inequality of
Conjecture 5.3 holds, it holds with a remainder that is a function of \(\deg\tau_q\) (Proposition 5.16).

## 8. Exercises

**Exercise 1 (a wildly ramified map).** Let \(k\) be an algebraically closed field of characteristic \(p>0\), let
\(X=\mathbb P^1_k\) with coordinate \(t\), and \(f=t^p-t\). Show that \(f\) is separable of degree \(p\), compute
\(e_P\) and \(d_P\) at all points, check the formula of Theorem 1.1, and show that the inequality of Corollary 1.2
is strict when \(S\) is the set of all closed points. Show that in characteristic \(0\) every polynomial of degree
\(d\ge2\) is ramified at some point of the affine line.

*Solution.* \(df=(pt^{p-1}-1)\,dt=-dt\ne0\), so \(f\) is separable by (K3). Its only pole is \(\infty\), of order
\(p\), so \(\deg f=p\) by (K1). Let \(\alpha\in k\) and \(\beta=f(\alpha)\). With \(u=t-\alpha\), the pullback of
the uniformizer \(t-\beta\) is \(t^p-t-\alpha^p+\alpha=u^p-u\). So \(e_\alpha=1\), and \(d(u^p-u)=-du\) gives
\(d_\alpha=0\). At \(\infty\) take \(u=1/t\). Then \(1/f=u^p/(1-u^{p-1})\), so \(e_\infty=p\), and
\[
d\Big(\frac{u^p}{1-u^{p-1}}\Big)=\frac{pu^{p-1}(1-u^{p-1})+(p-1)u^{2p-2}}{(1-u^{p-1})^2}\,du
=-\frac{u^{2p-2}}{(1-u^{p-1})^2}\,du ,
\]
so \(d_\infty=2p-2\). This is larger than \(e_\infty-1=p-1\), in agreement with Theorem 1.1(a), since \(p\) divides
\(e_\infty\). The formula reads \(-2p+(2p-2)=-2=2g-2\). The sum of the \(e_P-1\) is \(p-1\), which is smaller than
\(2g-2+2\deg f=2p-2\). In characteristic \(0\) let \(f\) be a polynomial of degree \(d\ge2\). Then \(e_\infty=d\)
and \(d_\infty=d-1\), and all \(d_P=e_P-1\). Theorem 1.1 gives \(\sum_{P\ne\infty}(e_P-1)=2d-2-(d-1)=d-1>0\).

**Exercise 2 (Fermat's equation for polynomials).** Let \(k\) be a field of characteristic \(0\) and \(n\ge3\).
Show that there are no pairwise coprime polynomials \(x,y,z\in k[t]\), not all constant, with \(x^n+y^n=z^n\). Show
that the statement fails for \(n=2\), and that it fails in characteristic \(p\) for \(n=p\).

*Solution.* Apply Theorem 1.5 to \(a=x^n\), \(b=y^n\), \(c=z^n\). They are coprime. None of \(x,y,z\) is zero: if
for example \(x=0\), then \(y^n=z^n\) with \(y,z\) coprime, so \(y\) and \(z\) are constants. In characteristic
\(0\) the derivative \(nx^{n-1}x'\) of \(x^n\) vanishes only if \(x\) is constant, so not all three derivatives
vanish. Since \(n_0(x^ny^nz^n)=n_0(xyz)\le\deg x+\deg y+\deg z\), the theorem gives
\(n\deg x\le\deg x+\deg y+\deg z-1\), and the same for \(y\) and \(z\). Adding the three inequalities, with
\(D=\deg x+\deg y+\deg z>0\), gives \(nD\le3D-3\), so \(n<3\). For \(n=2\): \((1-t^2)^2+(2t)^2=(1+t^2)^2\). In
characteristic \(p\): \(t^p+1^p=(t+1)^p\).

**Exercise 3 (the map of \(q=3/2\)).** Determine \(\tau_q(v)\) for \(v=\infty\) and for the primes
\(p\le13\). Determine the fibres over \([n]\) for \(n\le6\) and the ramification indices in them. Compute the
defects at the four points of degree one and compare with (5.2). Check Theorem 4.8 for \(n=6\).

*Solution.* Here \(a=3\), \(b=2\), \(H=3\) and \(\deg\tau_q=\log3=1.0986\). We have \(\tau_q(3)=[0]\) with
\(e_3=1\), \(\tau_q(2)=[\infty]\) with \(e_2=1\), and \(\tau_q(\infty)=[\infty]\) with
\(e_\infty=\log\tfrac32=0.4055\). The class of \(3\cdot2^{-1}\) is \(4\) modulo \(5\), \(5\) modulo \(7\), \(7\)
modulo \(11\) and \(8\) modulo \(13\), of orders \(2\), \(6\), \(10\) and \(4\). So \(\tau_q(5)=[2]\),
\(\tau_q(7)=[6]\), \(\tau_q(11)=[10]\) and \(\tau_q(13)=[4]\). The numbers \(3^n-2^n\) for \(n=1,\dots,6\) are
\(1\), \(5\), \(19\), \(65=5\cdot13\), \(211\), \(665=5\cdot7\cdot19\), and \(211\) is prime. So the fibres over
\([1],\dots,[6]\) are \(\emptyset\), \(\{5\}\), \(\{19\}\), \(\{13\}\), \(\{211\}\), \(\{7\}\), with \(e_p=1\)
everywhere. The fibre over \([1]\) is empty because \(3-2=1\) (Corollary 4.11). The defects are
\(\delta_{[0]}=0\), \(\delta_{[\infty]}=(0.4055-1)/1.0986=-0.5412\), \(\delta_{[1]}=0\) and \(\delta_{[2]}=0\). So
\(S_4(q)=-0.5412\). Formula (5.2): \(\lvert a^2-b^2\rvert=5\), \(v_2(a+b)=0\) and
\(\operatorname{rad}(ab(a^2-b^2))=30\), so \(S_4=2+(\log5-\log30-1)/\log3=2-2.5412\). For \(n=6\):
\(\Phi_6(x,y)=x^2-xy+y^2\), so \(\Phi_6(3,2)=7\); \(P(6)=3\) divides \(ab\), so \(c_6(q)=1\); the fibre
\(\{7\}\) has degree \(\log7=1.9459\), and \(\varphi(6)\deg\tau_q=2.1972\). The difference \(0.2513\) is below the
bound \(\varphi(6)\log\frac{1}{1-2/3}=2.1972\).

**Exercise 4 (negative \(q\)).** Let \(A>B\ge1\) be coprime integers, \(C=A+B\) and \(q=-A/B\).

(a) Show that \(S_3(q)=2+\big(\log C-\log\operatorname{rad}(ABC)-1\big)/\log A\).

(b) Assume \(S_3(q)\le2+\varepsilon+C_\varepsilon/\deg\tau_q\) for all rational \(q<-1\). Show that
\(C\le e^{1+C_\varepsilon}A^{\varepsilon}\operatorname{rad}(ABC)\) for all such \(A,B\). Compare with Theorem 5.6.

(c) Compute the four defects for \(A=27\), \(B=5\).

*Solution.* (a) In lowest terms \(q=a/b\) with \(a=-A\) and \(b=B\). Then \(\lvert a-b\rvert=C\), \(H=A\) and
\(\operatorname{rad}(ab(a-b))=\operatorname{rad}(ABC)\). Apply (5.1). (b) Multiply the inequality by
\(\log A>0\) and use (a): \(\log C-\log\operatorname{rad}(ABC)-1\le\varepsilon\log A+C_\varepsilon\). Compared
with Theorem 5.6 the factor \(2\) is gone, because for negative \(q\) the fibre over \([1]\) is the set of primes
that divide \(C\) itself. The triple \((1,1,2)\) is not covered. (c) Here \(q=-27/5\) and
\(\deg\tau_q=\log27=3.2958\). Over \([0]\): the prime \(3\) with \(e_3=3\), so
\(\delta_{[0]}=2\log3/\log27=0.6667\). Over \([\infty]\): the prime \(5\) with \(e_5=1\), and \(\infty\) with
\(e_\infty=\log(27/5)=1.6864\), so \(\delta_{[\infty]}=0.6864/3.2958=0.2083\). Over \([1]\): the primes that divide
\(a-b=-32\), that is \(2\) with \(e_2=5\), so \(\delta_{[1]}=4\log2/\log27=0.8412\). Over \([2]\): the odd primes
that divide \(a+b=-22\), that is \(11\) with \(e_{11}=1\), so \(\delta_{[2]}=0\). The sum is \(1.7162\), and (a)
gives \(2+(\log32-\log30-1)/\log27=2-0.2838\).

**Exercise 5 (another family).** For \(k\ge1\) let \(q_k=4^{3^k}\). Show that
\(S_3(q_k)\ge2+(k\log3-\log2-1)/(3^k\log4)\), and compute \(S_3(q_2)\).

*Solution.* Here \(a=4^{3^k}\), \(b=1\). The prime \(3\) does not divide \(ab\), and \(\operatorname{ord}_3(4)=1\).
By Lemma 4.7(c), \(v_3(a-1)=v_3(4-1)+v_3(3^k)=k+1\). So \(\operatorname{rad}(a-1)\le(a-1)/3^k\) and
\(\operatorname{rad}(ab(a-b))=2\operatorname{rad}(a-1)\le2(a-1)/3^k\). Formula (5.1) gives the bound. For \(k=2\):
\(a=262144\) and \(a-1=3^3\cdot7\cdot19\cdot73\), so \(\operatorname{rad}(a-1)=(a-1)/9\) and the bound is an
equality: \(S_3(q_2)=2+(2\log3-\log2-1)/\log262144=2+0.5041/12.4766=2.0404\).

**Exercise 6 (the projective line over \(\mathbb F_{1^4}\)).** Let \(F=\mathbb F_{1^4}=\{0,1,-1,i,-i\}\).

(a) Determine the admissible pairs of Theorem 6.14.

(b) By (6.1), restriction of congruences to \(\mathbb F_1[T]\) sends \([n,\lambda]\) to \([m]\) with
\(m=n\cdot\operatorname{ord}(\lambda)\). For \(m\le8\) list the points of \(\widetilde{\mathbb P}^1_F\) over
\([m]\) and their fibres under \(\Phi_F\).

(c) Compare with Proposition 3.3(b) and Theorem 6.16(c).

*Solution.* (a) The only prime \(p\) with \(\mu_p\subseteq F\) is \(2\), and the squares in \(F^\times\) are
\(1\) and \(-1\). So \((n,\lambda)\) is admissible if and only if \(n\) is odd, or \(\lambda=\pm i\).

(b) For \(m=2\) the pairs with \(n\operatorname{ord}(\lambda)=m\) are \((2,1)\) and \((1,-1)\), and only the second
is admissible. For \(m=4\) they are \((4,1)\), \((2,-1)\), \((1,i)\), \((1,-i)\), and the last two are admissible.
For \(m=6\): \((6,1)\) and \((3,-1)\), and the second is admissible. For \(m=8\): \((8,1)\), \((4,-1)\),
\((2,i)\), \((2,-i)\), and the last two are admissible. For odd \(m\) the only pair is \((m,1)\). With
\(\zeta_8=e^{2\pi i/8}\) the result is:

| \(m\) | points over \([m]\) | their fibres under \(\Phi_F\) |
|---|---|---|
| 1 | \([1,1]\) | \(\{1\}\) |
| 2 | \([1,-1]\) | \(\{-1\}\) |
| 3 | \([3,1]\) | the two roots of unity of order 3 |
| 4 | \([1,i]\), \([1,-i]\) | \(\{i\}\), \(\{-i\}\) |
| 5 | \([5,1]\) | the four roots of unity of order 5 |
| 6 | \([3,-1]\) | the two roots of unity of order 6 |
| 7 | \([7,1]\) | the six roots of unity of order 7 |
| 8 | \([2,i]\), \([2,-i]\) | \(\{\zeta_8,\zeta_8^5\}\), \(\{\zeta_8^3,\zeta_8^7\}\) |

For example a root of unity \(z\) of order \(6\) has \(z^3=-1\in F\) and \(z,z^2\notin F\), so
\(\operatorname{ord}_F(z)=3\) and \(\Phi_F(z)=[3,-1]\); and \(\zeta_8^2=\zeta_8^{10}=i\).

(c) Here \(\Gamma=\Gamma_4\) and \(F^\times=\mu_4\). Proposition 3.3(b) with \(N=4\) predicts
\(\varphi(\gcd(M,4))\) points among the roots of unity of order \(M\), each of degree
\(\varphi(M)/\varphi(\gcd(M,4))\): one point for \(M=1,2,3,5,6,7\), of degrees \(1,1,2,4,2,6\), and two points for
\(M=4\) and \(M=8\), of degrees \(1\) and \(2\). This is the table. So \(b_{\Gamma_4}\) is bijective, as
Theorem 6.16(c) says.

## 9. What this lesson does not prove

1. The facts (K1), (K2), (K3) on curves, and the fact that a nonconstant function defines a morphism to the
   projective line: [Stacks, Tags [0AYZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-pullback-map-proper-curves), [0C1A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-smooth), [0C1B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-section-riemann-hurewitz), [0C1C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-generically-etale), [0BY1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-theorem-curves-rational-maps)]. The fact \(H^0(X,\mathcal O_X)=k\) and the
   definition of the genus: [Stacks, Tags [0BUG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-proper-geometrically-reduced-global-sections), [0BY7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-definition-genus)]. The Riemann–Hurwitz formula for a separable morphism
   between two arbitrary curves is [Stacks, Tag [0C1D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-rh)]; the lesson proves the case of a map to the projective line
   from (K1) to (K3).
2. Ostrowski's theorem. It is proved in *Weil's proof for curves and what is missing over the integers*.
3. The degree of a cyclotomic field [Milne 2020, Theorem 6.4], and the product formula for number fields
   [Milne 2020, Theorem 7.15]. The second one is used only in Proposition 5.13(b).
4. The Galois correspondence for \(\mathbb Q(\mu_\infty)/\mathbb Q\) [Stacks, Tag [0BML](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-theorem-inifinite-galois-theory)] and for finite extensions
   [Stacks, Tag [09DW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-theorem-galois-theory)]. They are used only in the second statement of Theorem 6.16(b).
5. From *Monoid schemes*: a morphism from a monoidal space to an affine monoid scheme is a morphism of monoids to
   the global sections; morphisms glue; an affine monoid scheme has one closed point; the description of
   \(\mathbb P^1_{\mathbb F_1}\).
6. The construction of the strong congruence space and of the map \(\gamma\) for an arbitrary monoid scheme, and the
   surjectivity of \(\gamma\) [Jarra 2023a, Definition 3.8, Theorem 4.1, Corollary 4.11]. The lesson uses these
   only for \(\mathbb P^1_{\mathbb F_1}\), where it proves what it uses. The analogues of Proposition 6.2 and
   Theorem 6.10 for the ring of integers of a number field are [Jarra 2023b, Section 4 and Theorem 5.2].
7. The examples of [Smirnov 1992, §4, Propositions 1 to 6], the theorem of Stewart and Tijdeman behind Proposition 6, and the statement quoted from [Masser 1990, Section 1] after Proposition 5.15. For the first family
   the lesson proves the bound of Proposition 5.15(b), and not the bound with \(\log\log m\).
8. The consequences of the conjectures in [Smirnov 1992, §5, Theorems 2, 3 and 4].
9. The theorems of Stewart and Yu and of Stewart and Tijdeman bounding \(\log C\) [Stewart–Yu 2001, Theorem 1],
   [Stewart–Tijdeman 1986, Theorems 1 and 2].
10. Conjectures 5.3, 5.4 and 5.12 are open. The lesson proves relations between them and no case of them.
    Conjecture 5.11 does not hold (Proposition 5.15).

## References

Result numbers of the preprints refer to the arXiv versions. [Smirnov 1992] is cited by the section, formula and
theorem numbers of the Russian original.

- [Dickson 1919] L. E. Dickson, *History of the Theory of Numbers, Volume I: Divisibility and Primality*, Carnegie
  Institution of Washington, Publication No. 256, 1919. Free at https://archive.org/details/historyoftheoryo01dick
- [Jarra 2023a] M. Jarra, *Strong congruence spaces and dimension in \(\mathbb F_1\)-geometry*, [arXiv:2305.15953](https://arxiv.org/pdf/2305.15953).
- [Jarra 2023b] M. Jarra, *On Smirnov's approach to the abc conjecture*, [arXiv:2306.16637](https://arxiv.org/pdf/2306.16637).
- [Jarra 2024] M. Jarra, *Matroids with coefficients and \(\mathbb F_1\)-geometry*, PhD thesis, University of
  Groningen and IMPA, 2024, DOI 10.33612/diss.987821370. Free at https://doi.org/10.33612/diss.987821370
- [Le Bruyn 2016] L. Le Bruyn, *Absolute geometry and the Habiro topology*, [arXiv:1304.6532](https://arxiv.org/pdf/1304.6532).
- [Lorscheid 2018b] O. Lorscheid, *\(\mathbb F_1\) for everyone*, [arXiv:1801.05337](https://arxiv.org/pdf/1801.05337).
- [Lorscheid–Ray 2024] O. Lorscheid, S. Ray, *The topological shadow of \(\mathbb F_1\)-geometry: congruence
  spaces*, [arXiv:2305.12801](https://arxiv.org/pdf/2305.12801).
- [Masser 1990] D. W. Masser, *Note on a conjecture of Szpiro*, Astérisque 183 (1990), 19–23. Free at https://www.numdam.org/item/AST_1990__183__19_0/
- [Milne 2020] J. S. Milne, *Algebraic Number Theory*, course notes, version 3.08, 2020. Free at https://www.jmilne.org/math/CourseNotes/ANT.pdf
- [Oesterlé 1988] J. Oesterlé, *Nouvelles approches du "théorème" de Fermat*, Séminaire Bourbaki 1987–88, exposé
  694, Astérisque 161–162 (1988), 165–186. [Read the original exposé on Numdam](https://www.numdam.org/item/SB_1987-1988__30__165_0.pdf).
- [Smirnov 1992] A. L. Smirnov, *Hurwitz inequalities for number fields*, Algebra i Analiz 4 (1992), no. 2, 186–209
  (Russian); English translation in St. Petersburg Math. J. 4 (1993), no. 2, 357–375. Free at https://www.mathnet.ru/eng/aa316
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tag 0BML carries such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
- [Stewart–Tijdeman 1986] C. L. Stewart, R. Tijdeman, *On the Oesterlé–Masser conjecture*, Monatsh. Math. 102
  (1986), 251–257. Free at https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/log_0023.pdf
- [Stewart–Yu 2001] C. L. Stewart, K. Yu, *On the abc conjecture, II*, Duke Math. J. 108 (2001), 169–181. Free at
  https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s0012-7094-01-10815-6.pdf
- [Zsigmondy 1892] K. Zsigmondy, *Zur Theorie der Potenzreste*, Monatshefte für Mathematik und Physik 3 (1892),
  265–284. Free at https://zenodo.org/record/2131326
