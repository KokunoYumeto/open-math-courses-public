# Constructing the real numbers

Rational approximations can specify a number without naming its decimal expansion. We construct an ordered field from such approximations, prove its least-upper-bound property, and identify its elements with Dedekind cuts. This supplies the complete ordered field used in real analysis on closed intervals.

The cut material in Section 7 and the cut calculation in Exercise 3 follow Tim Button's contribution to *The Open Logic Text*. Its Cauchy-sequence treatment also informs the construction. The unit, including the detailed sequence-field proofs, completions and worked solutions, is written by GPT-6 Astra (OpenAI), Ultra, in Codex. Self-checked by the writing AI. Original text: public domain (CC0). Its source and edition notice identifies the source material.

## Starting knowledge

We start with the ordered field of rational numbers, natural-number induction and recursion, sets, functions and equivalence classes. In particular, rational inequalities and the usual rules for fractions are available. Every error bound in the construction is rational until the field has been constructed. Real completeness, a real limit, a square root or a decimal expansion is not a starting input.

A rational sequence is a function from the positive integers to \(\mathbb Q\). It is **Cauchy** when, for every rational \(\varepsilon>0\), some \(N\) satisfies \(|a_m-a_n|<\varepsilon\) for all \(m,n\geq N\). It is **null** when, for every rational \(\varepsilon>0\), eventually \(|a_n|<\varepsilon\). Absolute value has its ordered-field meaning: \(|q|=q\) for \(q\geq0\), and \(|q|=-q\) otherwise. Its product rule and triangle inequality follow by splitting into signs, or by multiplying and adding the bounds \(-|q|\leq q\leq|q|\).

## 1 Rational error bounds

**Lemma 1 (small rational scales).** For every positive rational \(\varepsilon\) there is a positive integer \(N\) with \(1/N<\varepsilon\). For every positive rational \(D\), the rational sequence \(D2^{-n}\) is null.

**Proof.** Write \(\varepsilon=r/s\) with positive integers \(r,s\). Any integer \(N>s\) has \(1/N<1/s\leq r/s\). Given any rational \(q\), an integer greater than its absolute numerator plus its positive denominator is greater than \(|q|\). Thus integers exceed any specified rational bound. Induction gives \(2^n\geq n+1\). Choose \(N\) with \(N+1>D/\varepsilon\). Then for \(n\geq N\), \(D2^{-n}\leq D/(n+1)<\varepsilon\). No real limit was used. \(\square\)

Changing finitely many terms of a null or Cauchy sequence does not change either property: increase the threshold past those terms. A null sequence is Cauchy, since two sufficiently late terms differ by less than \(\varepsilon/2+\varepsilon/2\).

## 2 Arithmetic of approximations

**Lemma 2 (bounded sequences and their operations).** Every rational Cauchy sequence is bounded. Sums, negatives and products of Cauchy sequences are Cauchy. Sums and negatives of null sequences are null, and a null sequence multiplied by a bounded sequence is null.

**Proof.** Choose \(N\) such that \(|a_n-a_N|<1\) for \(n\geq N\). An integer larger than \(|a_N|+1\) and the finitely many earlier absolute values bounds every term. Finite maxima exist by repeatedly choosing the larger of two rational numbers.

The sum estimate is
\[
|(a_m+b_m)-(a_n+b_n)|\leq|a_m-a_n|+|b_m-b_n|.
\]
Make each term less than \(\varepsilon/2\). Negation leaves differences unchanged in absolute value. For products, choose positive rational bounds \(A,B\) with \(|a_n|\leq A\), \(|b_n|\leq B\). Then
\[
|a_mb_m-a_nb_n|
\leq A|b_m-b_n|+B|a_m-a_n|.
\]
Make the two differences smaller than \(\varepsilon/(2A)\) and \(\varepsilon/(2B)\), respectively. The same sum estimate, with one index omitted, proves the null-sequence assertion. If \(|b_n|\leq B\), then \(|a_nb_n|\leq B|a_n|\); a null \(a\) eventually has \(|a_n|<\varepsilon/B\). \(\square\)

Declare \(a\sim b\) when \(a-b\) is null. Reflexivity follows from the zero sequence, symmetry from negation, and transitivity from addition of null sequences. Thus this is an equivalence relation on the set \(C\) of rational Cauchy sequences. Let
\[
R=C/{\sim},\qquad [a]+[b]=[a+b],\qquad [a][b]=[ab],\qquad -[a]=[-a].
\]
These definitions do not depend on the representatives. For addition this follows by adding the two null differences. For multiplication use
\[
ab-a'b'=a(b-b')+(a-a')b'
\]
and Lemma 2. Constant sequences represent \(0\) and \(1\). Associativity and commutativity of both operations, both identity laws, the additive-inverse law and distributivity hold term by term in \(\mathbb Q\), hence in the quotient. This proves every commutative-ring law, not just its independence of representatives. Also \([1]\ne[0]\), since the constant sequence 1 is not null.

## 3 Division and nonzero numbers

**Lemma 3 (separation from zero).** If a rational Cauchy sequence is not null, then for some rational \(d>0\) it eventually satisfies either \(a_n>d\) for every late \(n\), or \(a_n<-d\) for every late \(n\).

**Proof.** Failure to be null supplies a rational \(\eta>0\) such that arbitrarily late indices satisfy \(|a_n|\geq\eta\). Choose a Cauchy threshold \(N\) with \(|a_m-a_n|<\eta/2\) for \(m,n\geq N\), and choose \(k\geq N\) with \(|a_k|\geq\eta\). If \(a_k\geq\eta\), every \(a_n\) with \(n\geq N\) exceeds \(\eta/2\). If \(a_k\leq-\eta\), every such term is less than \(-\eta/2\). Take \(d=\eta/2\). \(\square\)

**Theorem 4 (the quotient is a field).** Every nonzero element of \(R\) has a multiplicative inverse.

**Proof.** For a representative \(a\) of a nonzero class choose \(N,d\) as in Lemma 3. Set \(b_n=1/a_n\) for \(n\geq N\), and set the finitely many earlier terms to zero. For \(m,n\geq N\),
\[
|b_m-b_n|=\frac{|a_m-a_n|}{|a_ma_n|}\leq d^{-2}|a_m-a_n|.
\]
The Cauchy condition for \(a\), with error \(d^2\varepsilon\), therefore gives that for \(b\). Moreover \(a_nb_n=1\) eventually, so \([a][b]=[1]\). Inverses in a commutative ring with identity are unique: if \(xy=xz=1\), then \(y=y(xz)=(yx)z=z\). Consequently the construction is independent of the chosen representative and threshold. Together with the verified ring laws and \(0\ne1\), this proves that \(R\) is a field. \(\square\)

## 4 Order and the rational copy

Call \([a]\) **positive** if some rational \(d>0\) satisfies \(a_n>d\) eventually. If \(a-b\) is null, eventually \(|a_n-b_n|<d/2\), so \(b_n>d/2\). Positivity is therefore well-defined. Define \(x<y\) when \(y-x\) is positive, and \(x\leq y\) when \(x<y\) or \(x=y\).

**Theorem 5 (ordered field and embedding).** This order makes \(R\) an ordered field. The constant-sequence map \(q\mapsto\bar q\) is an injective order-preserving field homomorphism \(\mathbb Q\to R\).

**Proof.** Lemma 3 shows that every nonzero class is positive or has positive negative. Neither can occur for the zero class, and both cannot occur for one class, because eventual positive and negative lower bounds would contradict each other. Sums and products of positive classes are positive: if representatives exceed \(d,e>0\) eventually, their sum exceeds \(d+e\), and their product exceeds \(de\). Thus exactly one of \(x<y\), \(x=y\), \(y<x\) holds. Transitivity follows from closure of positivity under addition. Reflexivity and antisymmetry of \(\leq\) now follow directly. Translating both sides leaves \(y-x\) unchanged. Multiplying a strict inequality by a positive element preserves it by closure of positivity under products; multiplication by zero gives equality. These are all the order-compatibility conditions.

Constant sequences preserve the two operations and their identities. A nonzero constant rational is separated from zero, so its class is nonzero. A constant is positive in \(R\) exactly when it is positive in \(\mathbb Q\), proving the last assertion. \(\square\)

If \(a_n\leq b_n\) eventually, then \([a]\leq[b]\): a negative difference class would be eventually less than a fixed negative rational, contradicting the termwise inequality. The converse assertion with chosen representatives is false; an example appears in the exercises.

From now on we identify \(q\) with \(\bar q\). Field subtraction, absolute values, reciprocals and rational constants in expressions involving \(R\) have thereby been justified.

## 5 Approximation and density

**Lemma 6 (rational approximation).** For \(x=[a]\) and every positive rational \(\varepsilon\), all sufficiently late \(n\) satisfy \(|x-a_n|\leq\varepsilon\) in \(R\). Every \(x\in R\) lies between two integers. If \(x<y\), some rational \(q\) satisfies \(x<q<y\).

**Proof.** Choose \(N\) with \(|a_m-a_n|<\varepsilon\) for \(m,n\geq N\). Fix \(n\geq N\) and pass the inequalities \(-\varepsilon\leq a_m-a_n\leq\varepsilon\) to classes using the last paragraph of Section 4. This gives the approximation claim. A positive integer bounding all terms of \(a\), increased by 1, bounds its class strictly on both sides.

For density let \(x=[a]<[b]=y\). There are rational \(d>0\) and \(N_0\) such that \(b_n-a_n>d\) for \(n\geq N_0\). Take \(n\) beyond this threshold and the two approximation thresholds with error \(d/8\). Put \(q=a_n+d/2\). Then
\[
x\leq a_n+d/8<q<a_n+7d/8<b_n-d/8\leq y.
\]
Every inequality used here holds in the ordered field already proved. \(\square\)

In particular, every positive element of \(R\) exceeds a positive rational. Together with Lemma 1, this means that rational error bounds suffice even when we later define convergence using positive errors in \(R\).

## 6 Completeness by nested intervals

**Theorem 7 (least upper bounds).** Every nonempty subset \(S\subset R\) bounded above has a least upper bound in \(R\).

**Proof.** Choose \(s_0\in S\) and an upper bound \(u\). Lemma 6 supplies rational numbers \(l_1<s_0\) and \(u_1>u\). In particular \(u_1\) is an upper bound of \(S\), whereas \(l_1\) is not. Recursively form the rational midpoint \(m_n=(l_n+u_n)/2\). If \(m_n\) is an upper bound of \(S\), set
\[
(l_{n+1},u_{n+1})=(l_n,m_n).
\]
Otherwise set \((l_{n+1},u_{n+1})=(m_n,u_n)\). This is one exhaustive two-case definition: the lower endpoint always remains a non-upper-bound. We use classical logic to decide the case in the definition; no numerical decision algorithm for arbitrary \(S\) is asserted.

Induction gives
\[
l_n\leq l_{n+1}<u_{n+1}\leq u_n,
\qquad u_n-l_n=(u_1-l_1)2^{1-n}.
\]
If \(m\geq n\), both later endpoints lie in \([l_n,u_n]\); hence their differences from the corresponding \(n\)-th endpoints are at most its width. Lemma 1 proves that both endpoint sequences are Cauchy and their difference is null. Define \(x=[l]=[u]\). For each fixed \(n\), passing the eventual endpoint inequalities to classes gives \(l_n\leq x\leq u_n\).

Suppose some \(s\in S\) satisfies \(s>x\). Lemma 6 gives a positive rational \(e<s-x\). Choose \(n\) with \(u_n-l_n<e\). Since \(x\geq l_n\),
\[
u_n\leq x+(u_n-l_n)<x+e<s,
\]
contradicting that \(u_n\) is an upper bound. Thus \(x\) is an upper bound of \(S\).

If \(z<x\), choose a positive rational \(e<x-z\) and then \(n\) with width less than \(e\). Now \(l_n\geq x-(u_n-l_n)>z\). The number \(l_n\) is not an upper bound, so some \(s\in S\) has \(s>l_n>z\). Consequently \(z\) is not an upper bound. This proves that \(x\) is the least upper bound. \(\square\)

We may now write \(\mathbb R\) for \(R\). The field, its order and its completeness have all been constructed from rational sequences.

## 7 The cut description

The following definition and union argument follow Tim Button and the Open Logic Project. The notation is aligned with this lesson; nonemptiness is invoked separately from boundedness.

A **Dedekind cut** is a nonempty proper subset \(A\subset\mathbb Q\) that is downward closed and has no greatest element. Downward closed means that \(q\in A\) and \(p<q\) imply \(p\in A\). Order cuts by inclusion. This order is total: if neither \(A\subseteq B\) nor \(B\subseteq A\), choose \(a\in A\setminus B\) and \(b\in B\setminus A\). If \(a<b\), downward closure of \(B\) contradicts \(a\notin B\); if \(b<a\), downward closure of \(A\) gives the other contradiction; equality is impossible.

**Theorem 8 (supremum of cuts).** A nonempty family \(\mathcal S\) of cuts with an upper bound has supremum \(\bigcup\mathcal S\).

**Proof.** Set \(L=\bigcup\mathcal S\). Nonemptiness of \(\mathcal S\) and of each member gives \(L\ne\varnothing\). An upper cut contains every member, so \(L\) is proper. If \(p<q\in L\), some member contains \(q\) and hence \(p\). If \(p\in L\), a member containing it contains a larger rational too. Thus \(L\) is a cut. It contains every member of \(\mathcal S\); and any cut containing every member contains their union. These are exactly the upper-bound and leastness assertions. \(\square\)

**Theorem 9 (the two descriptions agree).** The map
\[
D(x)=\{q\in\mathbb Q:q<x\}
\]
is an order isomorphism from the constructed \(\mathbb R\) to the cuts.

**Proof.** Integer bounds show that \(D(x)\) is nonempty and proper. Transitivity makes it downward closed, and rational density gives no greatest element. If \(x\leq y\), then \(D(x)\subseteq D(y)\). If \(x>y\), choose a rational \(q\) strictly between them; it lies in \(D(x)\setminus D(y)\). Thus order is both preserved and reflected, and the map is injective.

For a cut \(A\), consider its rational elements as a subset of \(\mathbb R\). A rational outside \(A\) is an upper bound: any larger element of \(A\) would force it into \(A\) by downward closure. Let \(x=\sup A\), which exists by Theorem 7. If \(q\in A\), choose \(r\in A\) with \(r>q\). Then \(q<r\leq x\), so \(q\in D(x)\). Conversely if \(q<x\), then \(q\) is not an upper bound of \(A\), so some \(r\in A\) exceeds \(q\); downward closure gives \(q\in A\). Hence \(A=D(x)\), proving surjectivity. \(\square\)

The field operations on cuts can therefore be transported from the sequence construction without leaving any field axiom to an exercise. For example,
\[
D(x)+D(y)=\{p+q:p<x,\ q<y,\ p,q\in\mathbb Q\}=D(x+y).
\]
The forward inclusion follows by addition of strict inequalities. If rational \(r<x+y\), choose rational \(p\) with \(r-y<p<x\); then \(q=r-p<y\), giving the reverse inclusion. This also explains why a union of cuts naturally represents a least upper bound.

## 8 Uniqueness of the complete ordered field

**Theorem 10 (uniqueness).** Any complete ordered field \(F\) is uniquely isomorphic to the constructed \(\mathbb R\) by an order-preserving field isomorphism that fixes the rational numbers.

**Proof.** First, \(F\) contains a canonical ordered rational field. The sums \(1,1+1,\ldots\) are positive and distinct, so the integer and fraction laws define an injective rational map. The natural numbers in \(F\) are unbounded: a least upper bound \(b\), if they were bounded, would have some natural \(n>b-1\), making \(n+1>b\). For \(u<v\) in \(F\), choose positive integer \(n\) with \(n(v-u)>1\). There is an integer \(k\) with \(k-1\leq nu<k\): take an integer \(B>|nu|+1\) and the least member greater than \(nu\) in the finite integer interval from \(-B\) to \(B\). Then \(u<k/n\leq u+1/n<v\). Thus rationals are dense in \(F\).

A rational Cauchy sequence \(a\) has a limit in \(F\). By Lemma 2 it is bounded. Set
\[
L_n=\inf_{k\geq n}a_k,\qquad U_n=\sup_{k\geq n}a_k,
\qquad t=\sup_n L_n.
\]
Infima exist as negatives of suprema of the negated sets. The \(L_n\) are increasing and bounded above. Each \(U_n\) bounds every \(L_m\): choose \(k\geq\max(m,n)\), giving \(L_m\leq a_k\leq U_n\). Therefore \(L_n\leq t\leq U_n\). Given any \(\varepsilon>0\) in \(F\), choose positive rational \(e<\varepsilon/3\). Past a Cauchy threshold, all terms lie between \(a_n-e\) and \(a_n+e\); hence \(U_n-L_n\leq2e<\varepsilon\). Every later \(a_k\) lies in the same interval, proving \(|a_k-t|<\varepsilon\).

Limits are unique: two limits separated by \(d>0\) contradict the triangle inequality with two errors less than \(d/3\). A rational null sequence tends to zero in \(F\), by rational density. Limits respect sums by the triangle inequality. They respect products because eventually \(|a_n|\leq |t|+1\), and
\[
|a_nb_n-ts|\leq |a_n|\,|b_n-s|+|s|\,|a_n-t|;
\]
choose the two errors smaller than \(\varepsilon/[2(|t|+1)]\) and \(\varepsilon/[2(|s|+1)]\). Therefore \(\Phi([a])=\lim_F a_n\) is well-defined and preserves addition and multiplication, as well as 0 and 1. If a sequence is eventually greater than rational \(d>0\), its limit is at least \(d\): a smaller limit contradicts eventual proximity with error \((d-t)/2\). Thus \(\Phi\) preserves positivity and is injective by Lemma 3. Being a field homomorphism, it also preserves inverses.

For \(t\in F\), choose rationals \(q_n\) with \(|q_n-t|<2^{-n}\). These choices require no countable-choice principle: enumerate fractions \(m/d\), \(m\in\mathbb Z,d\geq1\), by increasing \(|m|+d\), and take the first fraction satisfying the inequality. Density ensures one exists. Then \(q_n\) is rational Cauchy, since \(|q_n-q_m|<2^{-n}+2^{-m}\); the Archimedean property in \(F\) shows \(2^{-n}\) is smaller than any positive error eventually. Hence \(\Phi([q])=t\), proving surjectivity.

Finally, any order-preserving field isomorphism \(\Psi\) fixes the rational copy. For \(x=[a]\), Lemma 6 gives \(a_n-e\leq x\leq a_n+e\) eventually for each positive rational \(e\). Applying \(\Psi\) shows that the rational sequence \(a_n\) converges to \(\Psi(x)\) in \(F\). Uniqueness of limits forces \(\Psi(x)=\Phi(x)\). \(\square\)

## 9 Worked examples and exercises

**Exercise 1.** Why is eventual positivity of a representative insufficient to define a positive real number?

**Solution.** The rational sequence \(a_n=1/n\) is positive at every index, but Lemma 1 and the definition show it is null. Thus \([a]=0\), which is not positive. The uniform positive lower bound in Section 4 excludes this case. The sequence \(-1/n\) likewise represents zero despite being negative at every index. This also disproves the converse claim that \([a]\leq[b]\) forces \(a_n\leq b_n\) eventually for the chosen representatives: use \(a_n=1/n\) and \(b_n=0\). \(\square\)

**Exercise 2.** Show that \(a_n=1+1/n\) and the constant sequence 1 represent the same real number. Explain why taking reciprocals preserves this equality.

**Solution.** Their difference is null by Lemma 1. For every \(n\), \(a_n\geq1\), and
\[
\left|\frac1{a_n}-1\right|=\frac{1/n}{1+1/n}\leq\frac1n.
\]
So the reciprocal difference is null too. This is the explicit instance of the separation estimate in Theorem 4. \(\square\)

**Exercise 3.** Let \(A=\{q\in\mathbb Q:q<0\text{ or }q^2<2\}\). Prove that it is a cut and that its real representative has square 2 and is not rational.

**Solution.** It contains 0 and omits 2. If \(p<q\in A\), either \(p<0\), or \(0\leq p<q\) and \(p^2<q^2<2\); hence it is downward closed. For \(q<0\), zero is a larger member. For \(q\geq0\) with \(q^2<2\), set \(r=(2q+2)/(q+2)\). Direct subtraction gives
\[
r-q=\frac{2-q^2}{q+2}>0,
\qquad 2-r^2=\frac{2(2-q^2)}{(q+2)^2}>0.
\]
Thus there is no greatest member. Let \(x\) be the real corresponding to \(A\) by Theorem 9; since \(1\in A\), \(1<x\leq2\).

If \(x^2<2\), choose positive rational \(e<\min(1,(2-x^2)/(2x+1))\), then rational \(r\) with \(x<r<x+e\). We have \(r^2<(x+e)^2\leq x^2+(2x+1)e<2\), so \(r\in A=D(x)\), a contradiction. If \(x^2>2\), choose positive rational \(e<\min(x/2,(x^2-2)/(2x))\), then rational \(r\) with \(x-e<r<x\). Now \(r>0\) and \(r^2>(x-e)^2>x^2-2xe>2\), so \(r\notin A\), again contradicting \(A=D(x)\). Thus \(x^2=2\).

If \(x=m/n\) with positive integers \(m,n\), choose a representation with least positive denominator. The equation gives \(m^2=2n^2\). An odd integer has odd square, since \((2k+1)^2=2(2k^2+2k)+1\), so \(m=2k\). Substitution gives \(n^2=2k^2\), making \(n\) even as well. Dividing both by 2 gives a smaller positive denominator, a contradiction. \(\square\)

**Exercise 4.** In Theorem 7, take \(S=\{q\in\mathbb Q:q<1\}\subset\mathbb R\), with \(l_1=0,u_1=2\). What happens at the first midpoint, and why must the upper-bound and non-upper-bound cases be complementary?

**Solution.** The midpoint is 1, an upper bound, so the next interval is \([0,1]\). Its lower endpoint is still not an upper bound. The construction then produces \(l_n=1-2^{2-n}\) for \(n\geq2\), while \(u_n=1\). The width tends to zero and both classes equal 1. Using the complementary non-upper-bound case retains the invariant needed in the leastness proof, including when a midpoint itself is the supremum. \(\square\)

## Sources

Tim Button and the Open Logic Project contributors, *The Open Logic Text*, Arithmetization chapter: [cuts](https://raw.githubusercontent.com/OpenLogicProject/OpenLogic/1e960beff9ed7835bf3e3f1335e21af3439cd107/content/sets-functions-relations/arithmetization/cuts.tex), [Cauchy sequences](https://raw.githubusercontent.com/OpenLogicProject/OpenLogic/1e960beff9ed7835bf3e3f1335e21af3439cd107/content/sets-functions-relations/arithmetization/cauchy.tex), and [ordered rings and fields](https://raw.githubusercontent.com/OpenLogicProject/OpenLogic/1e960beff9ed7835bf3e3f1335e21af3439cd107/content/sets-functions-relations/arithmetization/checking-details.tex). The [project](https://openlogicproject.org/) supplies native LaTeX and author attribution. Section 7 follows its cut definition and union proof, and Exercise 3 its no-greatest-element calculation. The lesson supplies detailed sequence-field verification, estimates, comparison and uniqueness proofs, with worked solutions. Source files, version and terms accompany the source and edition notice.
