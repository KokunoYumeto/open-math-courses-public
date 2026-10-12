# The Cartier operator

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In characteristic \(p\) the derivative of a \(p\)-th power is zero. So a function on a curve cannot be recovered from its derivative, and a differential \(g\,dw\) need not be the differential of a function. The Cartier operator \(\mathcal C\) measures the obstruction: it reads off the part of \(g\) that stands at \(w^{p-1}\), where a derivative can never have a term, and takes a \(p\)-th root. This lesson constructs \(\mathcal C\) on the function field of a curve \(v^2=f(w)\) and proves its three basic properties (Theorem 4.1):

- \(\mathcal C(a^p\eta)=a\,\mathcal C(\eta)\);
- \(\mathcal C(dg)=0\);
- \(\mathcal C(dF/F)=dF/F\) for every nonzero function \(F\).

It then computes \(\mathcal C\) on the two differentials that carry the coefficient sums of [Truncated powers and points of a curve](truncated-powers-and-points-of-a-curve.md) (Theorem 6.1): on \(\omega=dw/v\) the operator multiplies by the coefficient \(H\), and on \(dw/((1-\lambda w)v)\) its value at the point \((0,1)\) is the sum \(S_f(\lambda)\). These are the identities on which the evaluation of the sums in [Jordan] rests.

The operator was introduced by P. Cartier [Cartier]. The proofs given here use only the field \(K\) of functions of the curve and its derivative. The third property is derived from a congruence for iterated derivatives (Lemma 3.1), proved by counting partitions.

The lesson uses fields of characteristic \(p\) and the notion of a derivation, and formal power series over a field (core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40)).

## 1. The function field

Let \(p\) be an odd prime, \(h=(p-1)/2\), and \(k\) a *perfect* field of characteristic \(p\): every element of \(k\) is a \(p\)-th power. Finite fields and algebraically closed fields are perfect. In a field of characteristic \(p\) the map \(a\mapsto a^p\) is additive, multiplicative and injective; so \(p\)-th roots are unique when they exist.

Let \(f\in k[w]\) be a polynomial of degree at least one without repeated root in an algebraic closure of \(k\). Then \(f\) is not a square in \(k(w)\): a square root would be a polynomial, because \(k[w]\) is integrally closed, and its roots would be repeated roots of \(f\). So \(X^2-f\) is irreducible over \(k(w)\), and
\[
K=k(w)[X]/(X^2-f)
\]
is a field. Write \(v\) for the class of \(X\). Every element of \(K\) is \(A+Bv\) with unique \(A,B\in k(w)\), and \(v^2=f\). The elements of \(K\) are the *functions* on the curve \(v^2=f(w)\).

For a subset \(L\) of a field write \(L^p\) for the set of \(p\)-th powers of its elements.

**Lemma 1.1.**

1. \(k(w)^p=k(w^p)\), and every element of \(k(w)\) is \(\sum_{i=0}^{p-1}a_iw^i\) with unique \(a_i\in k(w^p)\).
2. \(v^p=f^hv\), and \(K^p\) is the set of the elements \(a+bf^hv\) with \(a,b\in k(w^p)\).
3. Every \(g\in K\) is
\[
g=\sum_{i=0}^{p-1}u_i^pw^i
\]
with unique \(u_0,\dots,u_{p-1}\in K\).

**Proof.** (1) For a polynomial \(A=\sum a_nw^n\) we have \(A^p=\sum a_n^pw^{pn}\); since \(k\) is perfect, the \(p\)-th powers of polynomials are the polynomials in \(w^p\), and the same follows for quotients. A polynomial is \(\sum_{i<p}A_i(w^p)w^i\), by sorting its exponents modulo \(p\); a quotient \(A/B\) equals \(AB^{p-1}/B^p\) with \(B^p\in k[w^p]\). This gives existence. For uniqueness let \(\sum_ia_iw^i=0\) with \(a_i\in k(w^p)\); after multiplication by a common denominator in \(k[w^p]\) the \(a_i\) are polynomials in \(w^p\). The exponents in \(a_iw^i\) are congruent to \(i\) modulo \(p\), so the terms for different \(i\) cannot cancel: every \(a_i\) is \(0\).

(2) \(v^p=(v^2)^hv=f^hv\). So \((A+Bv)^p=A^p+B^pf^hv\), and \(A^p,B^p\) run through \(k(w^p)\) by (1).

(3) Let \(g=A+Bv\). By (1), \(A=\sum_ia_iw^i\) and \(B/f^h=\sum_ib_iw^i\) with \(a_i,b_i\in k(w^p)\). Then
\[
g=\sum_{i=0}^{p-1}(a_i+b_if^hv)\,w^i ,
\]
and \(a_i+b_if^hv\in K^p\) by (2). If \(\sum_i(a_i+b_if^hv)w^i=0\) with \(a_i,b_i\in k(w^p)\), then \(\sum_ia_iw^i=0\) and \(f^h\sum_ib_iw^i=0\), so all \(a_i\) and \(b_i\) vanish by (1). The \(u_i\) are unique because \(p\)-th roots are. \(\blacksquare\)

## 2. The derivative

For \(g=\sum_{i<p}u_i^pw^i\) as in Lemma 1.1(3) let
\[
D(g)=\sum_{i=1}^{p-1}i\,u_i^pw^{i-1}.
\]

**Lemma 2.1.**

1. \(D\) is additive, \(D(gg')=D(g)g'+gD(g')\) for \(g,g'\in K\), \(D(w)=1\), and \(D(a^pg)=a^pD(g)\).
2. On \(k(w)\), \(D\) is the usual derivative, and \(D(v)=f'/(2v)\).
3. \(D(g)=0\) exactly if \(g\in K^p\). An element \(g'\) is of the form \(D(g)\) exactly if its coefficient \(u_{p-1}\) is zero.
4. \(D^p=0\), and \(D^{p-1}(g)=-u_{p-1}^p\) for \(g=\sum_iu_i^pw^i\).

**Proof.** (1) Additivity and \(D(a^pg)=a^pD(g)\) follow from the uniqueness in Lemma 1.1(3), and \(D(w)=1\) from the definition. For the product rule let \(g=\sum_iu_i^pw^i\) and \(g'=\sum_jt_j^pw^j\); by additivity it suffices to treat \(g=u^pw^i\) and \(g'=t^pw^j\). If \(i+j<p\), then \(gg'=(ut)^pw^{i+j}\) and both sides are \((i+j)(ut)^pw^{i+j-1}\). If \(i+j\ge p\), then \(gg'=(utw)^pw^{i+j-p}\), and
\[
\begin{aligned}
D(gg')&=(i+j-p)(utw)^pw^{i+j-p-1}\\
&=(i+j)(ut)^pw^{i+j-1},
\end{aligned}
\]
because \(p=0\) in \(K\). This is again \(D(g)g'+gD(g')\).

(2) A map on \(k(w)\) with the properties in (1) that vanishes on \(k\subseteq K^p\) and has \(D(w)=1\) agrees with the usual derivative on polynomials, by the product rule and induction on the degree, and then on quotients. From \(v^2=f\) we get \(2vD(v)=f'\).

(3) If \(D(g)=0\), then \(iu_i^p=0\) for \(1\le i\le p-1\), so \(g=u_0^p\). The definition shows that \(D(g)\) has no term with \(w^{p-1}\). Conversely, an element \(\sum_{i\le p-2}t_i^pw^i\) is \(D(g)\) for
\[
g=\sum_{i=0}^{p-2}\frac{t_i^p}{i+1}\,w^{i+1}.
\]

(4) For \(n\ge1\),
\[
\begin{gathered}
D^n(u^pw^i)=u^p\,e\,w^{i-n},\\
e=i(i-1)\cdots(i-n+1).
\end{gathered}
\]
For \(n=p\) the product \(e\) of \(p\) consecutive integers is divisible by \(p\), so it is \(0\) in \(k\). For \(n=p-1\) and \(0\le i\le p-2\) one of the factors of \(e\) is \(0\); for \(i=p-1\), \(e=(p-1)!=-1\) in \(k\), by Wilson's theorem. \(\blacksquare\)

Wilson's theorem, \((p-1)!\equiv-1\pmod p\), follows from the factorization \(x^{p-1}-1=\prod_{a\ne0}(x-a)\) over \(\mathbb F_p\) by comparing constant terms.

## 3. A congruence for iterated derivatives

Let \(R\) be a commutative ring in which \(p=0\), with an additive map \(D\colon R\to R\) satisfying the product rule. For \(a\in R\) define \(P_0=1\) and
\[
P_{n+1}=D(P_n)+aP_n\qquad(n\ge0).
\]
So \(P_1=a\), \(P_2=D(a)+a^2\), \(P_3=D^2(a)+3aD(a)+a^3\).

**Lemma 3.1.** \(P_p=D^{p-1}(a)+a^p\).

**Proof.** A *partition* of a finite set is a set of pairwise disjoint nonempty subsets, its *blocks*, whose union is the set. For a partition \(\pi\) let
\[
m(\pi)=\prod_{B\in\pi}D^{|B|-1}(a).
\]
*For every \(n\ge1\), \(P_n\) is the sum of \(m(\pi)\) over all partitions \(\pi\) of \(\{1,\dots,n\}\).* For \(n=1\) the only partition has one block, and \(m=a=P_1\). Suppose the claim holds for \(n\). By the product rule, \(D(m(\pi))\) is the sum, over the blocks \(B\) of \(\pi\), of the product in which the factor of \(B\) is replaced by \(D^{|B|}(a)\); this is \(m(\pi')\) for the partition \(\pi'\) of \(\{1,\dots,n+1\}\) obtained by putting \(n+1\) into \(B\). And \(a\,m(\pi)=m(\pi'')\), where \(\pi''\) has the additional block \(\{n+1\}\). Every partition of \(\{1,\dots,n+1\}\) arises exactly once in one of these two ways, from the partition of \(\{1,\dots,n\}\) obtained by removing \(n+1\). So \(D(P_n)+aP_n\) is the sum over all partitions of \(\{1,\dots,n+1\}\).

*The case \(n=p\).* Identify \(\{1,\dots,p\}\) with the integers modulo \(p\), and let \(c\) be the map \(i\mapsto i+1\). It maps partitions to partitions, and \(m(c(\pi))=m(\pi)\), because \(m\) depends only on the sizes of the blocks. The partitions fall into classes \(\{\pi,c(\pi),c^2(\pi),\dots\}\). The number of elements of a class divides \(p\), so it is \(1\) or \(p\). A class with \(p\) elements contributes \(p\,m(\pi)=0\).

A class with one element is a partition \(\pi\) with \(c(\pi)=\pi\). Let \(B\) be its block containing \(0\). The sets \(c^j(B)\) are blocks of \(\pi\), and they cover everything. The set of \(j\) modulo \(p\) with \(c^j(B)=B\) is a subgroup of the integers modulo \(p\); it is everything or \(\{0\}\). In the first case \(c(B)=B\), so \(B\) is the whole set: \(\pi\) has one block, and \(m(\pi)=D^{p-1}(a)\). In the second case the \(p\) blocks \(c^j(B)\) are pairwise different, hence pairwise disjoint; \(p\) disjoint nonempty subsets of a set with \(p\) elements are singletons, and \(m(\pi)=a^p\). \(\blacksquare\)

**Proposition 3.2.** For every \(F\in K\), \(F\ne0\), the element \(a=D(F)/F\) satisfies
\[
D^{p-1}(a)=-a^p .
\]

**Proof.** For \(g\in K\), \(D(g)+ag=F^{-1}D(Fg)\). So the map \(g\mapsto D(g)+ag\), applied \(n\) times, is \(g\mapsto F^{-1}D^n(Fg)\). For \(g=1\) this gives \(P_n=F^{-1}D^n(F)\) with the \(P_n\) of Lemma 3.1. Since \(D^p=0\) (Lemma 2.1(4)), \(P_p=0\), and Lemma 3.1 gives \(D^{p-1}(a)+a^p=0\). \(\blacksquare\)

## 4. The operator

A *differential* of \(K\) is an expression \(g\,dw\) with \(g\in K\); differentials are added and multiplied by functions in the obvious way, so they form a vector space of dimension one over \(K\). For a function \(g\) let
\[
dg=D(g)\,dw ,
\]
and for \(F\ne0\) write \(dF/F\) for \(F^{-1}dF\), the *logarithmic differential* of \(F\). Then \(d(gg')=g\,dg'+g'\,dg\) and \(d(FF')/(FF')=dF/F+dF'/F'\).

The *Cartier operator* is the map on differentials
\[
\mathcal C\Bigl(\sum_{i=0}^{p-1}u_i^pw^i\,dw\Bigr)=u_{p-1}\,dw .
\]
It is well defined by Lemma 1.1(3). By Lemma 2.1(4),
\[
\begin{gathered}
\mathcal C(g\,dw)=u\,dw\\
\Longleftrightarrow\quad u^p=-D^{p-1}(g).
\end{gathered}
\]

**Theorem 4.1.** For differentials \(\eta,\eta'\) and functions \(a,g,F\) with \(F\ne0\):

1. \(\mathcal C(\eta+\eta')=\mathcal C(\eta)+\mathcal C(\eta')\) and \(\mathcal C(a^p\eta)=a\,\mathcal C(\eta)\);
2. \(\mathcal C(dg)=0\), and every differential \(\eta\) with \(\mathcal C(\eta)=0\) is \(dg\) for some \(g\);
3. \(\mathcal C(dF/F)=dF/F\).

**Proof.** (1) If \(\eta=\sum_iu_i^pw^i\,dw\), then \(a^p\eta=\sum_i(au_i)^pw^i\,dw\); additivity is clear from the uniqueness of the \(u_i\). (2) is Lemma 2.1(3). (3) Let \(a=D(F)/F\), so \(dF/F=a\,dw\). By Proposition 3.2, \(-D^{p-1}(a)=a^p\), so \(\mathcal C(a\,dw)=a\,dw\). \(\blacksquare\)

By (1) the operator is not linear over \(k\): for \(c\in k\), \(\mathcal C(c\eta)=c^{1/p}\mathcal C(\eta)\). It is linear over \(\mathbb F_p\).

## 5. Expansion at the origin

From here on \(f(0)=1\). The point \(O=(0,1)\) lies on the curve.

**Lemma 5.1.** There is exactly one power series \(s\in k[[w]]\) with \(s^2=f\) and constant term \(1\). The map
\[
\iota\colon K\to k((w)),\qquad A+Bv\mapsto A+Bs,
\]
is an injective homomorphism of fields into the field of Laurent series, where \(A,B\in k(w)\) are expanded at \(w=0\).

**Proof.** Write \(s=1+s_1w+s_2w^2+\cdots\) and \(f=1+f_1w+\cdots\). The coefficient of \(w^n\) in \(s^2\) is \(2s_n\) plus a polynomial in \(s_1,\dots,s_{n-1}\). Since \(2\) is invertible in \(k\), the equations \(s^2=f\) determine \(s_1,s_2,\dots\) one after another. The map \(\iota\) is the homomorphism of \(k(w)[X]/(X^2-f)\) that sends \(X\) to the root \(s\) of \(X^2-f\) in \(k((w))\); a homomorphism of fields is injective. \(\blacksquare\)

The series \(\iota(g)\) is the *expansion of \(g\) at \(O\)*. If it has no terms of negative degree, \(g\) is *regular at \(O\)*, and its constant term is the *value* \(g(O)\). For example \(w(O)=0\) and \(v(O)=1\).

**Lemma 5.2.** Let \(g\in K\) have the expansion \(\iota(g)=\sum_nb_nw^n\), and let \(\mathcal C(g\,dw)=u\,dw\). Then
\[
\iota(u)=\sum_jb_{pj+p-1}^{1/p}\,w^j .
\]
In particular, if \(g\) is regular at \(O\), then so is \(u\), and \(u(O)=b_{p-1}^{1/p}\).

**Proof.** Let \(g=\sum_iu_i^pw^i\), so \(u=u_{p-1}\) and \(\iota(g)=\sum_i\iota(u_i)^pw^i\). The \(p\)-th power of a Laurent series \(\sum_nc_nw^n\) is \(\sum_nc_n^pw^{pn}\). So \(\iota(u_i)^pw^i\) has only terms with exponents congruent to \(i\) modulo \(p\), and the terms of \(\iota(g)\) with exponents congruent to \(p-1\) are those of \(\iota(u_{p-1})^pw^{p-1}\):
\[
\iota(u_{p-1})^p=\sum_jb_{pj+p-1}w^{pj}.
\]
Taking the \(p\)-th root, which is unique, gives the formula. \(\blacksquare\)

So in terms of expansions \(\mathcal C\) keeps the coefficients at the exponents \(pj+p-1\) and takes their \(p\)-th roots. This is the form in which the operator is often defined.

## 6. The two differentials of the curve

Let \(f\) have degree at most four, and let \(c_m\), \(H=c_{p-1}\) and \(S_f(\lambda)\) be as in the lesson on truncated powers: \(f^h=\sum_mc_mw^m\), and \(S_f(\lambda)\) is the coefficient of \(w^{p-1}\) in the power series \(f^h/(1-\lambda w)\). There \(k\) was \(\mathbb F_p\); the definitions make sense for every \(k\) and \(\lambda\in k\). Let
\[
\begin{gathered}
\omega=\frac{dw}{v},\\
\theta_\lambda=\frac{dw}{(1-\lambda w)\,v}.
\end{gathered}
\]

**Theorem 6.1.** Let \(f\in k[w]\) have degree at most four, no repeated root, and \(f(0)=1\).

1. \(\mathcal C(\omega)=H^{1/p}\,\omega\).
2. For \(\lambda\in k\), \(\mathcal C(\theta_\lambda)=u_\lambda\,\omega\) with a function \(u_\lambda\in k(w)\) that is regular at \(O\), and
\[
u_\lambda(O)=S_f(\lambda)^{1/p}.
\]

If \(f\) has coefficients in \(\mathbb F_p\) and \(\lambda\in\mathbb F_p\), then \(H\) and \(S_f(\lambda)\) lie in \(\mathbb F_p\) and are their own \(p\)-th roots.

**Proof.** Since \(v^{p-1}=f^h\), we have \(1/v=v^{-p}f^h\). So
\[
\begin{gathered}
\omega=v^{-p}f^h\,dw,\\
\theta_\lambda=v^{-p}\,\frac{f^h}{1-\lambda w}\,dw ,
\end{gathered}
\]
and by Theorem 4.1(1) it suffices to apply \(\mathcal C\) to \(g\,dw\) with \(g=f^h\) and with \(g=f^h/(1-\lambda w)\), and to multiply the result by \(v^{-1}\).

(1) The polynomial \(f^h=\sum_mc_mw^m\) has degree at most \(2p-2\). Its terms with exponent congruent to \(p-1\) modulo \(p\) are the single term \(c_{p-1}w^{p-1}\). So \(f^h=\sum_iu_i^pw^i\) with \(u_{p-1}^p=H\), and \(\mathcal C(f^h\,dw)=H^{1/p}\,dw\).

(2) The function \(g=f^h/(1-\lambda w)\) lies in \(k(w)\) and is regular at \(O\); the coefficient of \(w^{p-1}\) in its expansion is \(S_f(\lambda)\). Let \(\mathcal C(g\,dw)=u_\lambda\,dw\). By Lemma 1.1(1) and the uniqueness in Lemma 1.1(3), \(u_\lambda\in k(w)\). By Lemma 5.2 it is regular at \(O\) with value \(S_f(\lambda)^{1/p}\). And \(\mathcal C(\theta_\lambda)=v^{-1}u_\lambda\,dw=u_\lambda\,\omega\). \(\blacksquare\)

Part (1), with Theorem 3.1 of the lesson on truncated powers, says that for a curve over \(\mathbb F_p\) the Cartier operator multiplies \(\omega\) by the trace of the curve modulo \(p\). Part (2) is the reason why the sums \(S_f(\lambda)\) can be approached through the curve: \(\theta_\lambda\) is a differential with two simple poles, at the two points over \(w=1/\lambda\), and such differentials can be compared with logarithmic differentials \(dF/F\), on which \(\mathcal C\) is the identity.

## 7. Exercises

**7.1.** For an integer \(n\), compute \(\mathcal C(w^n\,dw)\).

**7.2.** For \(a\in k\) show directly, without Proposition 3.2, that \(\mathcal C\bigl(dw/(w-a)\bigr)=dw/(w-a)\).

**7.3.** Check Lemma 3.1 for \(p=3\) from the formula for \(P_3\), and Proposition 3.2 for \(p=3\) and \(F=w^2+1\).

**7.4.** Let \(p=7\) and \(f=1+w^2+w^3\). Determine \(\mathcal C(\omega)\).

**7.5.** Show that \(\mathcal C\) is surjective, and that \(\mathcal C(g^{p-1}\,dg)=dg\) for every function \(g\).

## 8. Solutions

**7.1.** If \(p\) divides \(n+1\), say \(n=pj+p-1\), then \(w^n=(w^j)^pw^{p-1}\) and \(\mathcal C(w^n\,dw)=w^j\,dw\). Otherwise \(w^n=(w^j)^pw^i\) with \(i\le p-2\), and \(\mathcal C(w^n\,dw)=0\). In particular \(\mathcal C(dw/w)=dw/w\).

**7.2.** \(D^n\bigl((w-a)^{-1}\bigr)=(-1)^nn!\,(w-a)^{-n-1}\). For \(n=p-1\), which is even, this is \((p-1)!\,(w-a)^{-p}=-(w-a)^{-p}\). So \(-D^{p-1}\bigl((w-a)^{-1}\bigr)=\bigl((w-a)^{-1}\bigr)^p\), and \(\mathcal C\bigl(dw/(w-a)\bigr)=dw/(w-a)\).

**7.3.** In \(P_3=D^2(a)+3aD(a)+a^3\) the middle term vanishes when \(3=0\), so \(P_3=D^2(a)+a^3\). For \(F=w^2+1\) over a field of characteristic \(3\) we have \(a=2w/F\). The quotient rule gives
\[
\begin{aligned}
D(a)&=\frac{2F-4w^2}{F^2}=\frac{2-2w^2}{F^2},\\
D^2(a)&=\frac{-4wF-4w(2-2w^2)}{F^3}\\
&=\frac{4w^3-12w}{F^3}.
\end{aligned}
\]
In characteristic \(3\) this is \(w^3/F^3\), and \(a^3=8w^3/F^3=-w^3/F^3\). So \(D^2(a)=-a^3\).

**7.4.** By Example 1.4 of the lesson on truncated powers, \(H=4\). So \(\mathcal C(\omega)=4\omega\).

**7.5.** \(\mathcal C(u^pw^{p-1}\,dw)=u\,dw\), so every differential is a value of \(\mathcal C\). For the second statement: if \(g\in K^p\), both sides are \(0\). Otherwise \(g\ne0\), and \(g^{p-1}\,dg=g^p\,dg/g\); by Theorem 4.1(1) and (3), \(\mathcal C(g^p\,dg/g)=g\,dg/g=dg\).

## References

- [Jordan] D. Jordan, *Cartier–Miller evaluation of genus-one coefficient sums*, manuscript, revised 5 October 2026, equations (5) to (7). https://github.com/bbrhuft/Cartier-Miller-evaluation-of-genus-one-coefficient-sums
- [Cartier] P. Cartier, *Une nouvelle opération sur les formes différentielles*, Comptes rendus hebdomadaires des séances de l'Académie des sciences 244 (1957), 426–428.
