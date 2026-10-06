# Scalar calculus and Euclidean topology — selected programme proofs

These are selected foundation sections from **Metric and topological foundations**, programme lesson AN03-P003. They retain the section and equation numbers of that earlier lesson. The selection and introductory note were prepared by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026.

The original course-writing task and OpenAI Codex credits, dedication and history are retained in [the original title page](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and [rights notice](notices/RIGHTS.md). This independently written programme selection carries **CC0 1.0 Universal**. The [CC0 dedication](https://creativecommons.org/publicdomain/zero/1.0/) gives the terms.

The original notice files describe the original course edition. [Selection history](SELECTION_HISTORY.md) describes these excerpts.

The mathematical entry is natural-number arithmetic with induction, ordinary set theory and countable choice. The real-field construction is in [the scalar foundations](metric-foundation-bridges.md#12-real-numbers-and-finite-dimensional-topology); complex arithmetic and finite algebra are in [the algebra foundations](stable-prerequisite-bridges.md#10-full-finite-linear-algebra-foundations); integration is in [the measure foundations](banach-foundation-bridges.md#15-0-constructing-the-measure-without-importing-a-convergence-theorem).

This selection supplies: The real field; Euclidean norm and compactness; continuous extrema and intermediate values; derivatives, integrals, exponential and trigonometric functions; smooth compact cutoffs.

## 12. Real numbers and finite-dimensional topology

The real field is constructed here with its full arithmetic, order and completeness. Its exact comparison with the real numbers used in this course retains the original values. The logical entry is natural-number arithmetic with induction, ordinary set theory and countable choice. The last two sections apply the construction to the original norms, quadratic forms, polynomial minima and spectral contours. These are standard foundations; no novelty is claimed.

### 12.1. Integer and rational arithmetic with all original fractions retained

Start with natural numbers and their addition, multiplication, order, cancellation and induction. Construct the integers as classes of pairs \((m,n)\in\mathbb N^2\), with
\[
(m,n)\sim(m',n')\quad\Longleftrightarrow\quad m+n'=m'+n.
\tag{RT1}
\]
Reflexivity and symmetry follow from equality. For transitivity, add the two defining equalities for consecutive pairs and cancel the common middle sum in \(\mathbb N\). Addition and multiplication are
\[
[(m,n)]+[(p,q)]=[(m+p,n+q)],\qquad
[(m,n)][(p,q)]=[(mp+nq,mq+np)].
\tag{RT2}
\]
Adding equalities in (RT1) proves addition independent of representatives. For multiplication, replacement of \((m,n)\) by \((m',n')\) follows by multiplying \(m+n'=m'+n\) by \(p\) and \(q\): the equality of the cross sums in (RT1) is the sum of those two equations, with terms reordered. Replacement of \((p,q)\) follows by the same explicit operation with \(m,n\); hence replacing both pairs is valid. The additive inverse is \([(n,m)]\); both inverse sums are \([(m+n,m+n)]=0\). The identities are \(0=[(0,0)]\) and \(1=[(1,0)]\).

Addition is associative and commutative by coordinate addition. Multiplication is commutative by its two coordinate formulas. For associativity, the coordinates of the left associated triple product are
\[
\begin{gathered}
mpr+nqr+mqs+nps,\\
mps+nqs+mqr+npr.
\end{gathered}
\tag{RT3}
\]
The right associated product has these same four terms in each coordinate, in the respective order \(mpr,mqs,nps,nqr\) and \(mps,mqr,npr,nqs\). Distributivity follows by expanding (RT2) against \((p+r,q+s)\): the first coordinate is \(mp+mr+nq+ns\), and the second is \(mq+ms+np+nr\), which are the coordinates of the sum of the two products. Thus every ring identity used here is proved.

Declare \([(m,n)]>0\) when \(m>n\). Equation (RT1) and cancellation preserve this comparison. Exactly one of positive, zero and negative holds. Two positive pairs have \(m=n+k\), \(p=q+l\) for positive natural numbers \(k,l\); their product's first coordinate exceeds its second by \(kl>0\), on expanding all terms in (RT2). Their sum is positive by addition of inequalities. It follows that this is an ordered ring. A nonzero integer and another nonzero integer have nonzero product: apply the positive-product assertion to their respective signs. In particular, multiplication by a nonzero integer permits cancellation.

Construct the rational numbers from pairs \((p,q)\in\mathbb Z^2\) with \(q\ne0\), without restricting the denominator's sign or reducing the fraction. Put
\[
\begin{gathered}
(p,q)\sim(p',q')\ \Longleftrightarrow\ pq'=p'q,\\
[p,q]+[p',q']=[pq'+p'q,qq'],\qquad
[p,q][p',q']=[pp',qq'],\\
-[p,q]=[-p,q],\quad 0=[0,1],\quad 1=[1,1],\quad
[p,q]^{-1}=[q,p]\quad(p\ne0).
\end{gathered}
\tag{RT4}
\]
Transitivity follows by multiplying \(pq'=p'q\) by \(q''\) and \(p'q''=p''q'\) by \(q\), then cancelling the nonzero \(q'\). For sums and products, cross multiplication after changing either representative expands into the defining integer equality times the unchanged numerator or denominator. Hence both operations and negation descend. Associativity, distributivity and commutativity follow by cross multiplication into the already proved integer identities: denominators are the full original products, and the numerator of a sum of three terms is \(pq'q''+p'qq''+p''qq'\). The product \(([p,q]+[p',q'])[r,s]\) has the original numerator \((pq'+p'q)r\) and denominator \(qq's\). Adding the two separate products by (RT4) instead gives the full pair \([prq's+p'rqs,qq's^2]\). These pairs have identical cross products, namely \((pq'+p'q)r\,qq's^2=(prq's+p'rqs)\,qq's\); each side is the same full integer sum. Every factor \(s\) and \(s^2\), including its sign, remains in this comparison. Both inverse products in (RT4) are \([pq,qp]=1\), with \(p,q\ne0\). This proves the field laws.

Declare \([p,q]>0\) precisely when \(pq>0\). If \(pq'=p'q\), multiply by \(qq'\) to obtain \(pq(q')^2=p'q'q^2\). Both denominator squares are positive, so signs agree. The numerator-times-denominator of a sum of two positive fractions is
\[
(pq'+p'q)(qq')=(pq)(q')^2+(p'q')q^2>0.
\tag{RT5}
\]
The product has numerator-times-denominator \((pq)(p'q')>0\). Trichotomy follows from the integer signs and nonzero denominator. The embedding \(z\mapsto[z,1]\) preserves all operations and order and is injective. Thus \(\mathbb Q\) is an ordered field with its full original numerator and denominator data.

For \(q\ne0\), \(|q|\ge1\), so \(|[p,q]|\le |p|\). The integer \(|p|+1\) is a strict upper bound. This proves the rational Archimedean property. Between rationals \(a<b\), the rational \((a+b)/2\) is strictly between them, since its differences from either endpoint are \((b-a)/2>0\). These facts use no real completeness.

### 12.2. Constructing the real field and its exact inverse operations

Let \(\mathcal C\) be the set of rational Cauchy sequences \(a=(a_n)_{n\ge1}\), where for every rational \(\varepsilon>0\) some \(N\) has \(|a_n-a_m|<\varepsilon\) for all \(m,n\ge N\). Let \(\mathcal N\) be the sequences converging to zero by the same rational definition. Define
\[
\begin{gathered}
a\sim b\ \Longleftrightarrow\ a-b\in\mathcal N,\qquad
\mathbb R_{\mathcal C}=\mathcal C/\mathcal N,\\
[a]+[b]=[(a_n+b_n)_n],\qquad
[a][b]=[(a_nb_n)_n],\qquad -[a]=[(-a_n)_n].
\end{gathered}
\tag{RT6}
\]
A Cauchy sequence is bounded: choose \(N\) with \(|a_n-a_N|<1\) for \(n\ge N\), and take the actual rational bound
\[
M_a=1+\max_{1\le j\le N}|a_j|.
\tag{RT7}
\]
This bounds every coordinate, including the entire initial segment. Sums are Cauchy by adding the two actual errors. For products use
\[
|a_nb_n-a_mb_m|
\le M_a|b_n-b_m|+M_b|a_n-a_m|.
\tag{RT8}
\]
Given \(\varepsilon>0\), choose the errors below \(\varepsilon/(2(M_a+M_b+1))\); the displayed sum is less than \(\varepsilon\). The same bound proves a bounded sequence times a null sequence null. The full identity
\[
a_nb_n-c_nd_n=(a_n-c_n)b_n+c_n(b_n-d_n)
\tag{RT9}
\]
proves the product independent of both representatives. Null sums, negations and the triangle inequality prove the equivalence relation and all other operations independent of representatives. Pointwise rational field identities now prove all commutative ring identities on the quotient.

If \([a]\ne0\), the negation of null convergence provides a rational \(\varepsilon>0\) such that arbitrarily late coordinates have \(|a_n|\ge\varepsilon\). Choose \(N\) making every tail difference less than \(\varepsilon/2\), and choose one \(k\ge N\) with \(|a_k|\ge\varepsilon\). Then every \(n\ge N\) has
\[
|a_n|>\varepsilon/2=:\delta>0.
\tag{RT10}
\]
Define \(b_n=1/a_n\) for \(n\ge N\), and \(b_n=1\) for \(n<N\). Its tail differences satisfy
\[
|b_n-b_m|=\frac{|a_m-a_n|}{|a_n||a_m|}
\le\delta^{-2}|a_m-a_n|.
\tag{RT11}
\]
Thus \(b\) is Cauchy. Both pointwise products equal \(1\) on the tail; their discrepancies on the explicitly retained initial coordinates form null sequences. Consequently \([a][b]=[b][a]=1\). Uniqueness of a multiplicative inverse follows from the ring identities, so this construction gives the same inverse for any representative. Constant rational sequences give an injective field map \(\iota:\mathbb Q\to\mathbb R_{\mathcal C}\).

Call \([a]\) positive if \(a_n\ge\delta>0\) eventually for some rational \(\delta\). Changing representatives preserves positivity by choosing their difference below \(\delta/2\). A nonzero sequence in (RT10) has one fixed tail sign: if \(a_k\ge\varepsilon\), then \(a_n>\varepsilon/2\) for \(n\ge N\); if \(a_k\le-\varepsilon\), then \(a_n<-\varepsilon/2\). Thus every nonzero class is either positive or negative, but cannot be both. Positive sums are bounded below by the sum of the two original positive gaps, and positive products by their product. This constructs an ordered field, with \(\iota\) preserving order.

For any \(x=[a]\), (RT7) gives
\[
-\iota(M_a+1)<x<\iota(M_a+1).
\tag{RT12}
\]
A rational upper bound therefore gives an integer upper bound. This proves the real Archimedean property directly in the constructed field. A positive \(x\) has a rational \(\delta/2\) with \(0<\iota(\delta/2)<x\), by its positive tail gap. Absolute values satisfy the triangle and product rules by the field order: \(-|x|\le x\le |x|\), addition gives \(-(|x|+|y|)\le x+y\le |x|+|y|\), and applying the four possible signs gives \(|xy|=|x||y|\).

For every rational \(\varepsilon>0\), sufficiently late \(n\) have
\[
|x-\iota(a_n)|<\iota(\varepsilon).
\tag{RT13}
\]
Indeed choose a rational Cauchy tail with differences less than \(\varepsilon/2\). The sequences representing \(\varepsilon-(a_m-a_n)\) and \(\varepsilon+(a_m-a_n)\) then have positive tail gaps at least \(\varepsilon/2\). This proves (RT13) by the exact order definition. In particular, between \(x<y\), choose a positive rational \(\varepsilon\) with \(4\iota(\varepsilon)<y-x\), approximate \(x\) by \(\iota(a_n)\) within \(\iota(\varepsilon)\), and take \(q=a_n+2\varepsilon\). Then \(x<\iota(q)<y\). All original values and all approximation factors remain in these inequalities.

### 12.3. Suprema, Cauchy completeness and comparison with the given real numbers

Let \(S\subset\mathbb R_{\mathcal C}\) be nonempty and bounded above by \(u\). Choose \(x_0\in S\). By (RT12)--(RT13), choose rational endpoints \(l_0,v_0\) with \(\iota(l_0)<x_0\) and \(u<\iota(v_0)\). In particular \(l_0<v_0\). Inductively put \(m_n=(l_n+v_n)/2\). If \(\iota(m_n)\) is an upper bound of \(S\), set \(l_{n+1}=l_n,v_{n+1}=m_n\). Otherwise set \(l_{n+1}=m_n,v_{n+1}=v_n\). At every step \(\iota(v_n)\) is an upper bound, while \(\iota(l_n)\) is not an upper bound. Moreover
\[
l_n\le l_{n+1}\le v_{n+1}\le v_n,\qquad
v_n-l_n=(v_0-l_0)2^{-n}.
\tag{RT14}
\]
Induction gives \(2^n\ge n+1\). The rational Archimedean property therefore shows that the right side of (RT14) tends to zero. Both endpoint sequences are rational Cauchy, since every later endpoint lies between the displayed endpoints; their difference is null. Define \(s=[(l_n)_n]=[(v_n)_n]\).

Formula (RT13) implies \(\iota(l_n)\to s\) and \(\iota(v_n)\to s\) in the field order, first for rational errors and then for any positive field error using the positive rational below it. If some \(x\in S\) had \(x>s\), eventually \(\iota(v_n)<x\), contradicting its upper-bound property. If an upper bound \(w\) had \(w<s\), eventually \(w<\iota(l_n)\); because \(\iota(l_n)\) is not an upper bound, there is \(x\in S\) with \(\iota(l_n)<x\), contradicting \(w\). Thus \(s\) is exactly the least upper bound. Its uniqueness follows by applying each least-upper-bound property to the other upper bound. Infima are \(-\sup(-S)\), with the full negation map proving both defining inequalities.

Every Cauchy sequence \(x_n\) in this ordered field converges. The argument also applies to any complete ordered field. A tail is bounded by \(|x_N|+1\), and finitely many initial terms give a bound for the whole sequence. Define the original tail endpoints
\[
L_n=\inf_{m\ge n}x_m,\quad U_n=\sup_{m\ge n}x_m,\quad
x=\sup_{n\ge1}L_n.
\tag{RT15}
\]
They exist by the proved least-upper-bound property; the \(L_n\) are increasing and bounded above. For every \(n,k\), \(L_k\le U_n\): for \(k<n\) use \(L_k\le L_n\), and for \(k\ge n\) every member of the smaller tail is at most \(U_n\). Hence \(L_n\le x\le U_n\). If all tail differences are less than \(\varepsilon\), each tail member is an upper bound of that tail minus \(\varepsilon\); taking supremum and then infimum gives \(U_n-L_n\le\varepsilon\). It follows that \(|x_n-x|\le\varepsilon\) on that tail. Taking initially \(\varepsilon/2\) proves the strict-error convergence definition for every \(\varepsilon>0\).

We now compare with the course's given real field \(F=\mathbb R\), without replacing it. In a complete ordered field the positive integers are unbounded: otherwise their supremum \(s\) would have \(s-1\) not an upper bound, giving an integer \(n>s-1\) and \(n+1>s\), a contradiction. For \(a<b\) in \(F\), choose an integer \(N>1/(b-a)\). Among the integers bracketing \(Na\), choose \(k\) with \(k\le Na<k+1\). Such a \(k\) exists by restricting to a finite integer interval whose endpoints exceed \(|Na|+1\), then choosing the largest integer at most \(Na\). Then \((k+1)/N>a\) and \((k+1)/N\le a+1/N<b\). Thus the unique rational field embedding \(\iota_F\), defined by the original integer multiples of \(1_F\) and actual nonzero denominators, has dense image.

Apply (RT15) in \(F\) to the embedded rational Cauchy sequence. Define
\[
\Phi:\mathbb R_{\mathcal C}\longrightarrow F,\qquad
\Phi([a])=\lim_{n\to\infty}\iota_F(a_n).
\tag{RT16}
\]
Null differences have limit zero, so this map is well defined. Limits are unique because two distinct limits have a positive distance and their two errors can each be made smaller than one third of that distance. Sums commute with limits by the triangle inequality. Products commute by the full difference
\[
\iota_F(a_n)\iota_F(b_n)-xy
=\iota_F(a_n)(\iota_F(b_n)-y)+y(\iota_F(a_n)-x),
\tag{RT17}
\]
bounded using the original \(M_a\) and \(|y|\). Both terms tend to zero by their actual finite bounds. Thus \(\Phi\) is a field homomorphism fixing every rational. A positive class has positive gap \(\delta\); its limit is at least \(\iota_F(\delta)>0\), since a smaller limit would contradict its tail lower bound. Consequently \(\Phi\) preserves positivity and is injective. For every \(x\in F\), rational density supplies \(a_n\) with \(|x-\iota_F(a_n)|<1/n\). This rational sequence is Cauchy, because its tail difference is at most \(1/n+1/m\), and \(\Phi([a])=x\). The map is surjective.

For every original rational sequence representative all coordinate values remain in (RT16)--(RT17). Conversely the approximation just constructed is an explicit inverse value for each original \(x\). Two choices differ by at most \(2/n\) and hence give the same class; thus the inverse is well defined. Any ordered field isomorphism fixing the rationals must preserve the two error bounds (RT13), so it must have the value (RT16). This proves uniqueness, both compositions and every domain/codomain. Suprema and infima are transported by \(\Phi\): an upper bound, and then the least such bound, correspond exactly under its order isomorphism. Hence all subsequent constructions may use the original \(\mathbb R\), with their complete construction and comparison already proved. The course complex scalar set is the literal ordered-pair set \(\mathbb R^2\). The coordinatewise comparison \(([a],[b])\mapsto(\Phi([a]),\Phi([b]))\) has the coordinatewise inverse already proved in (RT16). It preserves the full pair addition and the two-coordinate product by (RT17) in every real factor. The separate complete complex field-law calculation is (FA0a)--(FA0d); none of those later laws is needed to construct the real field.

### 12.4. Square roots and the full Euclidean distance

For \(a\ge0\) in the original \(\mathbb R\), take \(T=\{t\ge0:t^2\le a\}\). It contains \(0\) and is bounded by \(a+1\), because \((a+1)^2>a\). Let \(r=\sup T\). If \(r^2<a\), choose
\[
0<\eta<\min\left(1,\frac{a-r^2}{2(2r+1)}\right).
\tag{RT18}
\]
Then \((r+\eta)^2\le r^2+\eta(2r+1)<a\), contradicting the upper bound. If \(r^2>a\), then \(r>0\). Choose \(0<\eta<\min(r/2,1,(r^2-a)/(2(2r+1)))\). Now \((r-\eta)^2\ge r^2-\eta(2r+1)>a\). Every nonnegative \(t\ge r-\eta\) has \(t^2>a\), since \(t^2-(r-\eta)^2=(t-r+\eta)(t+r-\eta)\ge0\). Therefore \(r-\eta\) is an upper bound of \(T\), contradicting minimality of \(r\). We obtain \(r^2=a\). Nonnegative square roots are unique: their square difference factors as the difference times their sum, and a positive difference would make that product positive. The same factorization proves their order preservation.

For \(d\ge0\), use all original coordinates and define
\[
|x|_2=\left(\sum_{j=1}^d x_j^2\right)^{1/2},\qquad
\langle x,y\rangle_0=\sum_{j=1}^d x_jy_j,\qquad
\rho(x,y)=|x-y|_2.
\tag{RT19}
\]
When \(d=0\), the empty sum is zero and \(\mathbb R^0\) is the singleton empty tuple. For \(y\ne0\), expansion of the nonnegative square sum gives
\[
0\le\sum_{j=1}^d\left(x_j-\frac{\langle x,y\rangle_0}{|y|_2^2}y_j\right)^2
=|x|_2^2-\frac{\langle x,y\rangle_0^2}{|y|_2^2}.
\tag{RT20}
\]
Each of the two cross terms is retained in that expansion; their sum is minus twice the full original pairing, and the final square contribution is once its square divided by \(|y|_2^2\). For \(y=0\) the pairing is zero. Thus \(|\langle x,y\rangle_0|\le |x|_2|y|_2\). Expanding \(|x+y|_2^2\) and applying this bound proves the triangle inequality. The other metric axioms follow from the coordinate squares. For \(d>0\),
\[
\max_{1\le j\le d}|x_j|\le |x|_2
\le \sqrt d\max_{1\le j\le d}|x_j|.
\tag{RT21}
\]
No coordinate or dimensional factor is suppressed. Convergence and the Cauchy property are therefore equivalent to their coordinate versions. Coordinatewise Cauchy completeness from (RT15) proves completeness of the entire original Euclidean metric. For \(d=0\) every sequence is the constant empty tuple and the assertion follows directly.

Open sets are those containing a positive-radius metric ball about each of their points. Closed sets have open complements. Convergence in this metric has unique limits by the triangle inequality and the one-third-distance argument. Every limit of a sequence in a closed set stays in that set: an outside limit would have a ball in the complement, contradicting eventual membership in that ball and in the closed set.

### 12.5. Bounded subsequences in every original coordinate

First consider a bounded real sequence \(t_n\), with an original interval \([a_0,b_0]\) containing it. If its endpoints coincide the whole sequence is constant. Otherwise bisect this actual interval. At least one of the two closed halves contains infinitely many sequence indices, since their union contains every index and a union of two finite sets is finite. Choose such a half, retaining its infinite set of indices. Repeat within that half. This gives nested original intervals \([a_k,b_k]\) and nested infinite index sets \(I_k\) with
\[
b_k-a_k=(b_0-a_0)2^{-k},\qquad
t_n\in[a_k,b_k]\quad(n\in I_k).
\tag{RT22}
\]
Choose \(n_k\in I_k\) with \(n_k>n_{k-1}\); an infinite subset of natural numbers cannot be bounded, because a bounded subset is finite. The supremum \(t=\sup_k a_k\) exists. For any \(j,k\), nestedness gives \(a_j\le b_k\), so \(a_k\le t\le b_k\). Thus \(|t_{n_k}-t|\le(b_0-a_0)2^{-k}\to0\). Every original interval length and actual selected index is retained.

For a bounded sequence \(x_n\in\mathbb R^d\), (RT21) bounds every coordinate. Apply the preceding construction to coordinate one. From the selected subsequence apply it to coordinate two, and continue through all \(d\) coordinates. Earlier coordinate convergence is preserved under each later strictly increasing index map: any increasing natural-number map has its \(k\)-th value at least \(k\). The final subsequence has the full original index
\[
n(k)=n_1\bigl(n_2(\cdots n_d(k)\cdots)\bigr)
\tag{RT23}
\]
and converges in every coordinate, hence by (RT21) in the original Euclidean distance. When \(d=0\), take \(n(k)=k\). The resulting limit belongs to any closed set containing the original sequence by Section 4. This proves bounded subsequence existence without using compactness as its own prerequisite.

### 12.6. Open-cover compactness and the exact closed-and-bounded criterion

A subset \(K\subset\mathbb R^d\) is compact if every cover of \(K\) by open subsets of \(\mathbb R^d\) has a finite subcover. The empty set is compact because the empty subfamily covers it. A subset is sequentially compact if every sequence of its points has a subsequence converging to a point of that subset. Section 12.5 proves that every closed bounded set is sequentially compact, with all original coordinates retained.

We prove that sequential compactness supplies open-cover compactness in this metric. First it supplies finite ball covers at every radius \(\varepsilon>0\). Otherwise, for any finite number of stages, choose \(x_1\in K\) and, after \(x_1,\ldots,x_n\), choose
\[
x_{n+1}\in K\setminus\bigcup_{j=1}^n B(x_j,\varepsilon).
\tag{RT24}
\]
Every two distinct selected points in one finite tuple have distance at least \(\varepsilon\). If an infinite extension were already selected, a convergent subsequence would have two sufficiently late terms each within \(\varepsilon/3\) of its limit, giving mutual distance less than \(2\varepsilon/3\). Such an extension would contradict sequential compactness, but the finite extension rule alone does not select it under countable choice. The following independent countable construction proves that finitely many balls \(B(x_j,\varepsilon)\) with centers in \(K\) cover \(K\).

Here is that construction with the original Euclidean distance unchanged. The empty set needs no balls; in dimension zero the nonempty coordinate space is a singleton and one ball covers it. Suppose \(K\ne\varnothing\) and \(d\geq1\). Enumerate all open coordinate boxes \(Q_j=\prod_{i=1}^d(a_{ji},b_{ji})\) with rational endpoints \(a_{ji}<b_{ji}\). This enumeration follows from the existing integer-pair enumeration of rational numbers and the diagonal enumeration of finite tuples: each rational keeps its actual numerator and nonzero denominator. For an original \(x\in\mathbb R^d\) and \(r>0\), rational density gives endpoints on either side of each \(x_i\), within \(r/(2\sqrt d)\). That box contains \(x\), and every \(y\) in it has \(|y-x|<(\sum_{i=1}^d r^2/(4d))^{1/2}=r/2<r\). Thus these original boxes form a countable neighborhood basis, without assuming compactness.

Fix one \(x_0\in K\). For each already fixed box define the independent nonempty set
\[
 H_j=
 \begin{cases}
  K\cap Q_j,&K\cap Q_j\ne\varnothing,\\
  \{x_0\},&K\cap Q_j=\varnothing .
 \end{cases}
 \qquad z_j\in H_j .
 \tag{RT24a}
\]
Countable choice selects this sequence once. Its set of values \(S\) is dense in \(K\): for each \(x\in K\) and \(r>0\), the preceding basis calculation gives a box containing \(x\) inside \(B(x,r)\), and its selected \(z_j\) lies in that ball. If finitely many balls of radius \(\varepsilon/3\), with centres \(c_1,\ldots,c_q\in K\), covered \(S\), then for each original \(x\in K\) density gives \(z_j\) with \(|x-z_j|<\varepsilon/3\). Some cover ball contains \(z_j\), so
\[
 |x-c_i|\leq |x-z_j|+|z_j-c_i|
                  <2\varepsilon/3<\varepsilon .
 \tag{RT24b}
\]
These same finitely many centres would cover \(K\) by its original \(\varepsilon\)-balls. Under the assumed failure of such a cover, \(S\) therefore has no finite \(\varepsilon/3\)-ball cover.

Starting with \(w_1=z_1\), after \(w_1,\ldots,w_n\) take the least enumerated index \(j\) with \(z_j\) outside their finitely many open \(\varepsilon/3\)-balls, and let \(w_{n+1}=z_j\). The preceding failure of a finite cover proves that this least natural-number index exists. This is a deterministic recursion on the single chosen countable sequence; it needs no choices from history-dependent arbitrary sets. It gives
\[
 |w_i-w_j|\geq\varepsilon/3\quad(i\ne j).
 \tag{RT24c}
\]
Sequential compactness would give a convergent subsequence. Two sufficiently late terms have distances to its limit less than \(\varepsilon/6\), hence mutual distance less than \(\varepsilon/3\), contrary to (RT24c). This proves the required finite-ball covering conclusion using exactly the declared countable-choice foundation. The original finite extension formula (RT24), the original distance and its full coordinate norm, and all earlier comparison factors remain. No Zorn or dependent-choice axiom has been inserted.

For an open cover \(\mathcal U\) of nonempty \(K\), some \(\delta>0\) has this property: for every \(x\in K\), one member of \(\mathcal U\) contains \(B(x,\delta)\cap K\). If this failed, for every positive integer \(n\) choose \(x_n\in K\) such that no member contains \(B(x_n,1/n)\cap K\). Take a convergent subsequence \(x_{n_k}\to x\in K\). A member \(U\) containing \(x\) contains \(B(x,r)\) for some \(r>0\). For sufficiently large \(k\),
\[
|x_{n_k}-x|_2<r/2,\qquad 1/n_k<r/2,\qquad
B(x_{n_k},1/n_k)\subset B(x,r)\subset U.
\tag{RT25}
\]
The middle inclusion follows by adding the two original strict distance bounds. This contradicts the selection of \(x_{n_k}\). With the resulting \(\delta\), cover \(K\) by finitely many balls of radius \(\delta/2\) centered in \(K\), using the preceding result. For each center choose a member containing its radius-\(\delta\) ball intersected with \(K\). These finitely many original cover members cover \(K\). This proves open-cover compactness from sequential compactness.

Conversely a compact \(K\) is bounded. The balls \(B(0,n)\), \(n=1,2,\ldots\), cover \(\mathbb R^d\) by the Archimedean property. A finite subcover has maximal radius, giving an actual bound. The empty set is bounded by any nonnegative bound.

It is also closed. Fix \(a\notin K\). If \(K\) is empty its complement is the whole open space. Otherwise each \(x\in K\) has the original positive radius \(r_x=|x-a|_2/3\). Finitely many \(B(x_i,r_{x_i})\) cover \(K\). Put \(\delta=\min_i r_{x_i}>0\). For \(y\in K\), choose \(i\) with \(|y-x_i|_2<r_{x_i}\). Then
\[
|y-a|_2\ge |x_i-a|_2-|y-x_i|_2
>3r_{x_i}-r_{x_i}=2r_{x_i}\ge2\delta.
\tag{RT26}
\]
Thus \(B(a,\delta)\) is disjoint from \(K\). Every outside point has an open ball in the complement, proving closedness.

We have proved all three implications, so for every original finite dimension, including zero,
\[
K\text{ compact}\quad\Longleftrightarrow\quad
K\text{ closed and bounded}
\quad\Longleftrightarrow\quad
K\text{ sequentially compact}.
\tag{RT27}
\]
For the last implication from sequential compactness to closed and bounded, the just-proved route through open-cover compactness supplies it. No definition of compactness was substituted for another without proving the maps between their assertions.

A closed subset \(C\) of a compact set \(K\) is compact. To an open cover of \(C\) add the open complement of \(C\); the resulting family covers \(K\), and a finite subfamily still covers \(C\) after discarding that complement. If closedness is relative to \(K\), use an ambient open set whose intersection with \(K\) is the relative complement; the same cover argument applies. A finite union of compact sets is compact by taking a finite subcover for each member and then their finite union. Empty unions are covered by the already proved empty case.

Finite Cartesian products preserve the original coordinates. For \(K_j\subset\mathbb R^{d_j}\) compact, each factor is closed and bounded. The product is closed because an outside point has a coordinate outside one closed factor, and the inverse image of an open coordinate neighborhood is open by (RT21). If \(|x^{(j)}|_2\le M_j\) in that factor, the complete product satisfies
\[
\left|\bigl(x^{(1)},\ldots,x^{(r)}\bigr)\right|_2^2
=\sum_{j=1}^r |x^{(j)}|_2^2\le\sum_{j=1}^r M_j^2.
\tag{RT28}
\]
Consequently it is compact by (RT27), with every original bound retained. An empty factor gives the empty compact product; a product of no factors is the one-point zero-dimensional space.

### 12.7. Continuous maps, full extrema and uniform continuity

A map \(f:K\to\mathbb R^e\) is continuous at \(x\in K\) when for every \(\varepsilon>0\) some \(\delta>0\) ensures \(|f(y)-f(x)|_2<\varepsilon\) whenever \(y\in K\) and \(|y-x|_2<\delta\). This definition proves directly that inverse images of relatively open sets are relatively open: choose a ball about \(f(x)\) in the target open set, then its continuity preimage ball. Conversely that inverse-image property applied to every target ball gives the same definition. It also proves preservation of sequence limits, by applying the defining \(\delta\) to an eventually close sequence.

If \(K\) is compact, \(f(K)\) is compact: the inverse images of any open cover of \(f(K)\) are a relatively open cover of \(K\); the proved relative-cover formulation yields finitely many of them, whose original target members cover \(f(K)\). Thus continuous real functions on a compact set have bounded image.

If \(K\ne\varnothing\) and \(f:K\to\mathbb R\) is continuous, let \(s=\sup f(K)\), which exists by Section 3. For each positive integer \(n\), least-upper-bound minimality supplies \(x_n\in K\) with
\[
s-1/n<f(x_n)\le s.
\tag{RT29}
\]
Sequential compactness supplies \(x_{n_k}\to x\in K\). Continuity gives \(f(x_{n_k})\to f(x)\), whereas (RT29) gives convergence to \(s\). Uniqueness of limits therefore gives \(f(x)=s\). Applying this same proof to the function \(-f\) gives \(y\in K\) with \(f(y)=\inf f(K)\). This proves both extrema, with the exact hypotheses: the empty set has no attained extremum and is never assigned one.

The intermediate value property also follows from these exact foundations. Let \(f:[a,b]\to\mathbb R\) be continuous with \(a<b\), and \(f(a)\le c\le f(b)\). The set \(S=\{t\in[a,b]:f(t)\le c\}\) is nonempty and bounded above, so put
\[
t_0=\sup S.
\tag{RT29a}
\]
If \(f(t_0)>c\), continuity gives a neighborhood on which \(f>c\). Here \(t_0>a\), since \(f(a)\le c\). Shrink its positive radius below \(t_0-a\). Then \(t_0\) minus half that radius is still an upper bound of \(S\), contradicting the supremum. If \(f(t_0)<c\), then \(t_0<b\), since \(f(b)\ge c\). Shrink the continuity radius below \(b-t_0\); the point \(t_0\) plus half that radius belongs to \(S\), another contradiction. Thus \(f(t_0)=c\). If the endpoint inequalities are reversed, apply this proved argument to \(-f\) with the exact value \(-c\). If \(a=b\), only the common endpoint value is requested, and it is attained there.

For every integer \(q\ge1\) and \(a\ge0\), the polynomial \(t^q\) is continuous. Its values at \(0,a+1\) bracket \(a\), because \((a+1)^q\ge a+1>a\). The just-proved intermediate value property gives a nonnegative \(q\)-th root. For \(x>y\ge0\), the complete identity
\[
x^q-y^q=(x-y)\sum_{j=0}^{q-1}x^{q-1-j}y^j>0
\tag{RT29b}
\]
proves strict increase and uniqueness. Each summand is nonnegative, and the \(j=0\) term is positive, including \(q=1\), when it is \(1\). For \(a=0\) the unique root is zero. This supplies every positive-integer real root in the original polynomial-radius formulas without a calculus prerequisite.

Such a continuous map \(f:K\to\mathbb R^e\) is uniformly continuous. If not, some \(\varepsilon>0\) would supply pairs \(x_n,y_n\in K\) with \(|x_n-y_n|_2<1/n\) but \(|f(x_n)-f(y_n)|_2\ge\varepsilon\). Take \(x_{n_k}\to x\in K\). The full triangle inequality implies \(y_{n_k}\to x\), so both image sequences tend to \(f(x)\); their difference then has norm less than \(\varepsilon\) eventually, a contradiction. For empty \(K\) uniform continuity is vacuous. This gives the precise compact-set continuity needed in all later sup-norm arguments.

Addition and multiplication of real-valued continuous functions are continuous by the estimates for sums and (RT17), with local boundedness obtained from continuity at the point. Reciprocals are continuous on their exact nonzero domain: if \(f(x)\ne0\), choose a neighborhood with \(|f(y)-f(x)|<|f(x)|/2\), giving \(|f(y)|>|f(x)|/2\), and use
\[
\left|\frac1{f(y)}-\frac1{f(x)}\right|
=\frac{|f(y)-f(x)|}{|f(y)||f(x)|}
\le \frac{2}{|f(x)|^2}|f(y)-f(x)|.
\tag{RT30}
\]
Finite sums and products are continuous by induction. Absolute value is continuous since its two values differ by at most the difference of the original values. For nonnegative \(a,b\), \(|\sqrt a-\sqrt b|^2\le |a-b|\): when \(a\ge b\), \((\sqrt a-\sqrt b)^2\le(\sqrt a-\sqrt b)(\sqrt a+\sqrt b)=a-b\), and interchanging them covers the other order. This proves continuity of the square root, including zero.

Identify a complex number with its original pair of real coordinates as in [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) (FA0a)--(FA0d). Addition, multiplication, conjugation and squared modulus are exactly the full coordinate polynomials already proved there, so all are continuous. The modulus is the nonnegative square root of the full squared modulus and is therefore continuous. The two-coordinate inverse has the full nonzero denominator \(a^2+b^2\); (RT30) proves its continuity on its actual domain. These are exact maps on the original complex numbers, through the scalar comparison (RT16).

### 12.8. Countable coordinate neighborhoods and exact sequence choices

The set of rational \(d\)-tuples is countable: integers are enumerated by pairs of natural numbers, rational pairs by four such coordinates including their nonzero denominator restrictions, and finite tuples of these by their finite-coordinate enumerations. A finite tuple of natural numbers can be enumerated by first listing all tuples whose coordinate sum is at most \(N\), for \(N=0,1,\ldots\); each stage is finite and every tuple occurs. Hence no unstated identification between countability and compactness is used.

Rational coordinate tuples are dense in \(\mathbb R^d\). Given \(x\) and \(\varepsilon>0\), for \(d>0\) choose each rational coordinate \(q_j\) within \(\varepsilon/(2\sqrt d)\) of \(x_j\). Formula (RT21) gives \(|q-x|_2<\varepsilon/2\). For \(d=0\) the empty tuple is already the point. Balls with rational coordinate centers and positive rational radii form a countable basis. If \(B(x,\varepsilon)\) is contained in an open set, choose such \(q\) with \(|q-x|_2<\varepsilon/4\), and choose rational \(r\) with
\[
|q-x|_2<r<\varepsilon-|q-x|_2.
\tag{RT31}
\]
Rational density from Section 12.2 supplies it, since the endpoint gap is positive. Then \(x\in B(q,r)\subset B(x,\varepsilon)\). Both maps and both radius errors are explicit.

Consequently every open set is the union of a subfamily of this countable basis: for each of its points the preceding construction gives a basis ball contained in it. Any family of pairwise disjoint nonempty open subsets is countable: for each member choose the first rational-coordinate point in a fixed enumeration which it contains. Density guarantees a choice and disjointness makes the assignment injective. This proves the particular countability argument used in this lesson's supports section without assuming compactness implies countability.

For a continuous function \(f\), its support is the closure of \(\{x:f(x)\ne0\}\). Outside that support there is a neighborhood on which it is zero, by the definition of closure and its open complement. Derivatives which exist on such a neighborhood are zero there by their defining difference quotients, since every numerator is zero. This assertion uses the derivative definition only and makes no assertion of global differentiability.

If supports of functions form a locally finite family, each point has a neighborhood meeting only finitely many supports. A compact \(K\) admits finitely many such neighborhoods. Only the finite union of those finite member lists can meet \(K\). The same finite collection of neighborhoods gives an open neighborhood of \(K\) on which only those members may be nonzero. Derivative sums on that neighborhood, wherever the original derivatives exist, therefore consist of the same finite actual summands. This proves the exact compact-support receiving assertion without turning pointwise finiteness into local finiteness.

### 12.9. Every original finite norm and positive quadratic form

Let \(V\) be a finite-dimensional real vector space with its actual ordered basis \(b=(b_1,\ldots,b_d)\), coordinate bijection \(J_b\) from [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) (FA3), and its given norm \(N(v)\). We prove comparison with the coordinate metric while retaining \(N\) as the working norm. For \(d>0\), define the actual constant
\[
M_b=\left(\sum_{j=1}^d N(b_j)^2\right)^{1/2}>0.
\tag{RT32}
\]
The full coordinate expansion and (RT20) give
\[
N(J_bx)=N\left(\sum_{j=1}^d x_jb_j\right)
\le\sum_{j=1}^d |x_j|N(b_j)\le M_b|x|_2.
\tag{RT33}
\]
The reverse triangle inequality gives \(|N(J_bx)-N(J_by)|\le M_b|x-y|_2\). Thus the original norm in these coordinates is continuous, with the full original basis constant.

The coordinate sphere \(S=\{x:|x|_2=1\}\) is nonempty for \(d>0\), closed by norm continuity and bounded, hence compact. The function \(N(J_bx)\) has a minimum \(c_b\) on \(S\). At its minimizing point \(x_0\), injectivity of \(J_b\) and \(|x_0|_2=1\) give \(N(J_bx_0)>0\), so \(c_b>0\). For any original \(x\ne0\), the auxiliary radial comparison is the exact bijection
\[
x\longmapsto(|x|_2,\,|x|_2^{-1}x),\qquad
(r,u)\longmapsto ru,\quad r>0,\ |u|_2=1.
\tag{RT34}
\]
Both compositions are identities by the full scalar multiplication and its inverse, and the original vector remains \(x=|x|_2(|x|_2^{-1}x)\). Homogeneity of the given norm, with that entire factor retained, yields
\[
c_b|x|_2\le N(J_bx)\le M_b|x|_2
\quad\text{for every original }x.
\tag{RT35}
\]
The zero vector has both sides zero. In dimension zero \(V=\{0\}\); all topologies are the one-point topology and no sphere minimum or positive coordinate constant is inserted.

The identity coordinate map and its inverse now send balls according to the two exact constants in (RT35). They preserve open and closed sets and both sequence notions. A set is bounded in the original norm precisely when its coordinate set is bounded, and it is compact precisely when its coordinate set is compact, because both inverse-image cover maps are continuous bijections. A bounded original-norm sequence therefore has a convergent subsequence in that same original norm, with indices furnished by (RT23). Nothing replaces \(N\) by another working norm.

For a complex vector space with ordered complex basis \(b\), the exact underlying real-coordinate bijection is
\[
J_b^{\mathbb R}(a_1,c_1,\ldots,a_d,c_d)
=\sum_{j=1}^d(a_j+ic_j)b_j
=\sum_{j=1}^d(a_jb_j+c_j\,ib_j).
\tag{RT36}
\]
Its inverse is the original complex coordinate inverse followed by the original real and imaginary coordinate maps. This is a real basis consisting of all \(b_j,ib_j\), not a replacement of the complex basis. Apply (RT32)--(RT35) to it. Every basis norm, including \(N(ib_j)=N(b_j)\) for a complex norm, is retained in the full sum. Thus complex compactness and subsequence assertions use every original real and imaginary coordinate and both inverse maps.

For a given positive-definite real quadratic form \(Q(x)=x^{\mathsf T}Gx\), retain every entry of \(G\) and its exact Gram map from [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md) (FA15)--(FA18). Its norm \(N_Q(x)=\sqrt{Q(x)}\) obeys the norm identities proved there, so (RT35) applies to that same original form. Alternatively the more precise residual comparison from (FA22) gives its exact lower constant \(\sqrt{d_{\min}}/F_S\), with \(d_{\min}=\min_jd_j>0\), \(F_S=(\sum_{j,k}|S_{jk}|^2)^{1/2}\), the original residual lengths and full triangular map \(S\). Hence for \(r\ge0\),
\[
Q(x)\le r^2
\ \Longrightarrow\
|x|_2\le \frac{F_S}{\sqrt{d_{\min}}}\,r
\quad(d>0).
\tag{RT37}
\]
The full polynomial \(Q\) is continuous, so its sublevel set is closed and bounded and therefore compact. For \(r=0\) it is exactly \(\{0\}\); for negative \(r\), the literal set \(Q(x)\le r^2\) instead has the bound with \(|r|\), and no radius convention is silently changed. In dimension zero all these sets are the single empty-coordinate point. Unit-level sets are closed and bounded and hence compact; in dimension zero the unit level is empty. All determinant and volume comparisons in the receiving this lesson argument remain its original Gram comparisons, rather than consequences of changing its metric.

### 13.1. Limits with all original scalar and coordinate factors

For a map \(f:D\to\mathbb R\), a point \(x_0\) in the closure of \(D\setminus\{x_0\}\), and an original value \(L\), the limit \(f(x)\to L\) means that for every \(\epsilon>0\) some \(\delta>0\) gives \(|f(x)-L|<\epsilon\) whenever \(x\in D\) and \(0<|x-x_0|<\delta\). Sequences use the same inequality beyond an integer index. One-sided limits restrict the actual domain. A limit is unique: two distinct values at distance \(d>0\) would have a common domain point with both errors less than \(d/3\), contradicting their distance.

If \(f\to a\) and \(g\to b\), the following exact expansions prove sums, scalar multiples and products:

\[
\begin{aligned}
 (f+g)-(a+b)&=(f-a)+(g-b),\\
 cf-ca&=c(f-a),\\
 fg-ab&=(f-a)g+a(g-b),\\
 |fg-ab|&\le |f-a|(|b|+1)+|a||g-b|
 \quad\text{once }|g-b|<1.
\end{aligned}\tag{OC1}
\]

Choose the two errors below \(\epsilon/[2(|b|+|a|+2)]\) to obtain the product limit. If \(b\ne0\), take \(|g-b|<|b|/2\); then \(g\ne0\) and

\[
 \left|\frac1g-\frac1b\right|
 =\frac{|g-b|}{|g||b|}
 \le\frac{2}{|b|^2}|g-b|.
\tag{OC2}
\]

This proves the reciprocal and quotient rules, retaining both denominators. Absolute values are continuous because their difference is at most the original difference. Finite sums/products follow by induction. A function has a limit precisely when every sequence in its punctured domain tending to \(x_0\) has that limit. One implication is the definition. If the definition fails, choose, for each \(n\), a point with \(0<|x_n-x_0|<1/n\) and error at least the same fixed \(\epsilon\). This gives the countersequence. The analogous continuity assertion includes \(x=x_0\).

For an original basis \(b=(b_1,\ldots,b_d)\) of a finite real space \(V\), write \(J_bx=\sum_jx_jb_j\) and retain its given norm \(N\). The earlier finite-norm proof supplies the actual positive constants \(c_b,M_b\) when \(d>0\):

\[
 c_b\left(\sum_{j=1}^d x_j^2\right)^{1/2}
 \le N(J_bx)\le
 M_b\left(\sum_{j=1}^d x_j^2\right)^{1/2},
 \qquad
 M_b=\left(\sum_{j=1}^d N(b_j)^2\right)^{1/2}.
\tag{OC3}
\]

The lower constant is the minimum of the original norm on the actual coordinate unit sphere. Thus coordinate limits are equivalent to limits in \(N\), and coordinatewise real completeness makes every Cauchy sequence complete in the original norm. For a complex space use the exact real basis \(b_1,ib_1,\ldots,b_d,ib_d\), retaining all real and imaginary components. In dimension zero every map has the unique zero value; no positive sphere constant is assigned. Limits, finite sums and all the ensuing integral constructions pass through these proved maps and their actual inverses.

### 13.2. Derivatives, extrema and the mean value theorem

For \(f:I\to\mathbb R\) on an interval, its derivative at an interior \(x\) is the limit of the actual quotient \([f(x+h)-f(x)]/h\) over nonzero \(h\) with \(x+h\in I\). At a finite endpoint use the corresponding one-sided limit if asserted. Differentiability gives the exact remainder

\[
 f(x+h)=f(x)+h f'(x)+h r_x(h),
 \qquad r_x(h)\longrightarrow0.
\tag{OC4}
\]

It implies continuity at \(x\). If an interior point is a local maximum, quotients for positive \(h\) are nonpositive and for negative \(h\) are nonnegative, so their common limit is zero. The same argument with signs reversed proves the minimum case.

Let \(f\) be continuous on \([a,b]\), \(a<b\), differentiable on \((a,b)\), and satisfy \(f(a)=f(b)\). If it is constant its derivative is zero at every interior point. Otherwise the proved compact extrema include a value distinct from the common endpoint value; an attaining maximum or minimum must then be interior, and the preceding argument gives a point where \(f'=0\). This proves Rolle's theorem without an integral prerequisite.

For arbitrary such \(f\), subtract the actual affine secant

\[
 F(t)=f(t)-f(a)-\frac{f(b)-f(a)}{b-a}(t-a).
\tag{OC5}
\]

It has equal endpoint values. Rolle gives some \(c\in(a,b)\) with \(F'(c)=0\), and hence \(f(b)-f(a)=(b-a)f'(c)\). Constants and affine derivatives follow directly from their original quotients. Consequently a zero derivative on an interval gives a constant, and a derivative bounded in absolute value by \(M\) gives \(|f(b)-f(a)|\le M|b-a|\). A nonnegative derivative gives a nondecreasing function; a strictly positive derivative gives a strictly increasing one by the actual secant formula. Unbounded intervals follow by applying the statement to each pair of their points.

Apply this to each coordinate of a vector-valued map. It gives coordinate bounds and then (OC3), rather than asserting a single vector-valued mean-value point. For example, if each coordinate derivative has bound \(M_j\), then

\[
 N(f(b)-f(a))
 \le M_b |b-a|\left(\sum_{j=1}^d M_j^2\right)^{1/2}.
\tag{OC6}
\]

Here \(M_b\) is the original basis constant, not the interval endpoint. Dimension zero gives the zero inequality. Complex-valued functions are handled by both real coordinates.

### 13.3. Constructing the full oriented Riemann integral

For a bounded real function \(f\) on an original interval \([a,b]\), \(a<b\), take a finite partition \(P:a=t_0<\cdots<t_m=b\), and let

\[
\begin{aligned}
 L(f,P)&=\sum_{j=1}^m
   \inf_{[t_{j-1},t_j]}f\,(t_j-t_{j-1}),\\
 U(f,P)&=\sum_{j=1}^m
   \sup_{[t_{j-1},t_j]}f\,(t_j-t_{j-1}),\\
 S(f,P,\xi)&=\sum_{j=1}^m f(\xi_j)(t_j-t_{j-1}),
 \qquad \xi_j\in[t_{j-1},t_j].
\end{aligned}\tag{OC7}
\]

Every infimum and supremum exists by the original completeness theorem. Refinement increases \(L\) and decreases \(U\), by dividing each interval into its actual lengths. Any two partitions have their finite common refinement. Thus \(\sup_P L(f,P)\le\inf_P U(f,P)\). Their equality defines integrability and the value \(\int_a^bf\).

A continuous function on this compact interval is bounded and uniformly continuous. Given \(\epsilon>0\), choose \(\delta>0\) so that oscillation on any interval of length below \(\delta\) is less than \(\epsilon/(b-a+1)\). A finite uniform partition of mesh below \(\delta\) then satisfies

\[
 U(f,P)-L(f,P)
 \le \frac{\epsilon}{b-a+1}\sum_{j=1}^m(t_j-t_{j-1})
 =\frac{\epsilon(b-a)}{b-a+1}<\epsilon.
\tag{OC8}
\]

The upper and lower integrals therefore agree. For any integrable bounded \(f\), all tagged sums tend to this value as mesh tends to zero. To prove the assertion at its full bounded-function scope, first choose \(P_0\) with \(U(f,P_0)-L(f,P_0)<\epsilon/2\), and a bound \(|f|\le M\). Compare a fine tagged partition \(Q\) with the common refinement \(P_0\cup Q\). Intervals of \(Q\) not crossing an interior \(P_0\) endpoint have their tagged contribution between the corresponding refined lower and upper contributions. At most \(m_0-1\) intervals cross such endpoints; their total length is at most \((m_0-1)\operatorname{mesh}Q\). Both the refined contribution and the original tagged contribution on their union have absolute value at most \(M\) times that length. Consequently

\[
 \left|S(f,Q,\xi)-\int_a^bf\right|
 \le U(f,P_0)-L(f,P_0)
       +2M(m_0-1)\operatorname{mesh}Q.
\tag{OC9}
\]

Taking mesh less than \(\epsilon/[4(M+1)m_0]\) proves convergence. Multiple endpoints in one interval only reduce the count; tagged endpoints cause no extra interval length.

Conversely, if all sufficiently fine tagged sums lie within \(\epsilon\) of the same \(I\), take any one sufficiently fine partition. In each interval choose a value within \(\epsilon/(b-a+1)\) of its supremum, and separately a value within that error of its infimum. The corresponding sums lie arbitrarily close to \(U\) and \(L\). Hence \(U-L\le 2\epsilon+2\epsilon(b-a)/(b-a+1)\). Sending \(\epsilon\) to zero proves integrability, with value \(I\). This establishes the tagged-sum criterion, not merely one chosen sequence of sums.

Termwise operations on tagged sums prove linearity. Order passes to sums and limits; constants integrate to their original value times \(b-a\). A partition including an interior \(c\) splits its sums exactly, so the same limit proves interval additivity and integrability of restrictions. Bounded integrable sums and scalar multiples are integrable by the criterion. The absolute value is integrable: its interval oscillation is at most that of \(f\), and \(-|f|\le f\le|f|\). Retain the resulting bounds

\[
 \left|\int_a^b f(t)\,dt\right|
 \le\int_a^b|f(t)|\,dt
 \le(b-a)\sup_{[a,b]}|f|.
\tag{OC10}
\]

Define \(\int_a^a f=0\), and for \(b<a\) define \(\int_a^bf=-\int_b^af\). The sign is part of the definition and remains in additivity and substitution. Continuous vector functions integrate coordinatewise through the original \(J_b\); this value is the limit of the full vector tagged sums by (OC3). The triangle inequality in the given original norm, applied to each full sum, gives

\[
 N\left(\int_a^b f(t)\,dt\right)
 \le |b-a|\sup_{[\min(a,b),\max(a,b)]}N(f).
\tag{OC11}
\]

Linearity and this estimate also prove that uniform convergence passes through the integral. The actual interval length is never absorbed into a norm or an integral convention.

### 13.4. Fundamental theorem, substitution and integration by parts

#### 13.4.1. The primitive and both fundamental-theorem forms

For continuous \(f\) on \([a,b]\), define \(F(x)=\int_a^xf(t)\,dt\). The original uniform bound gives continuity of \(F\). At an interior \(x\), and with the appropriate one-sided interpretation at either endpoint, additivity gives

\[
 \frac{F(x+h)-F(x)}h-f(x)
 =\frac1h\int_x^{x+h}(f(t)-f(x))\,dt,
 \qquad
 \left|\frac{F(x+h)-F(x)}h-f(x)\right|
 \le\sup_{t\text{ between }x,x+h}|f(t)-f(x)|.
\tag{OC12}
\]

The oriented sign for \(h<0\) gives the same absolute bound, which tends to zero by continuity. Thus \(F'=f\). If \(g\) is continuous on \([a,b]\), differentiable on \((a,b)\), and its derivative has a continuous extension to \([a,b]\), use that extension for the proper Riemann integral. Then \(g-F\), where \(F(x)=\int_a^xg'(t)\,dt\), has zero derivative. The mean value theorem proves it constant, and

\[
 g(b)-g(a)=\int_a^b g'(t)\,dt.
\tag{OC13}
\]

The stronger form used in the metric lesson allows a bounded Riemann-integrable function on \([a,b]\) equal to \(g'\) on \((a,b)\), without continuity of that function. Assign its actual endpoint values as the extension denoted by \(g'\) in (OC13); Changing those two values does not change the proper integral. Indeed, for every tagged partition, only its first interval can use the left endpoint as its tag and only its last interval can use the right endpoint. The absolute change of its tagged sum is therefore at most its mesh times the sum of the two absolute endpoint-value changes. This bound tends to zero for every sequence of meshes tending to zero, uniformly over all tags. The full tagged-sum criterion (OC9) and its proved converse give integrability of the endpoint-modified function and the identical integral. This argument uses the actual endpoint values and neither an endpoint derivative nor an improper integral. For each tagged partition, the mean value theorem on every subinterval chooses \(\xi_j\) with \(g(t_j)-g(t_{j-1})=g'(\xi_j)(t_j-t_{j-1})\). Summing retains every endpoint and telescopes exactly to \(g(b)-g(a)\). The full tagged-sum criterion (OC9) gives (OC13). Endpoint derivatives need not exist for this argument. Coordinatewise application proves the vector statement with its original values and norms.

**Finitely many exceptional interior points.** Retain the original continuous \(F:[a,b]\to\mathbb R\) and bounded Riemann-integrable \(f:[a,b]\to\mathbb R\). Suppose \(F'(x)=f(x)\) for every interior \(x\) outside a finite set \(E\). If \(a<b\), list the distinct points of \(E\cap(a,b)\), keeping their actual coordinates, as
\[
 a=t_0<t_1<\cdots<t_q<t_{q+1}=b.
 \qquad
 F(b)-F(a)
 =\sum_{j=1}^{q+1}\bigl(F(t_j)-F(t_{j-1})\bigr)
 =\sum_{j=1}^{q+1}\int_{t_{j-1}}^{t_j}f(t)\,dt
 =\int_a^bf(t)\,dt.
 \tag{OC13a}
\]
On each actual closed subinterval \(F\) is continuous and differentiable at every interior point. The restriction of \(f\) is bounded and Riemann integrable: extending any partition of that subinterval by the two outside intervals shows its upper-minus-lower sum is at most the corresponding nonnegative full-interval difference. Full-interval partitions of arbitrarily small difference, refined by its endpoints, therefore prove the restriction criterion. The mean value theorem on each partition piece supplies derivative samples in its interior, where \(F'=f\). The full fine-tagged-sum criterion then proves the middle equality separately on each \([t_{j-1},t_j]\). Additivity of the original integral and the displayed telescoping endpoint differences prove the last equality. No derivative at a point of \(E\) is required, and no endpoint contribution is omitted.

For \(a=b\) both sides are zero. For reversed endpoints apply the result on the same ordered interval and retain the negative orientation. For a complex or fixed finite-dimensional target, apply the scalar proof to every real coordinate, including both real and imaginary parts of each complex coordinate, and reconstruct the original vector through its actual basis map. The resulting equality is in that original target, with every coordinate and endpoint unchanged. This is an additional proved form of the theorem; the preceding source statement and its proper-integral hypotheses remain identifiable. No novelty is claimed.

#### 13.4.2. Substitution and ordered integration by parts

The product and chain derivative rules are proved in Section 13.5 below directly from (OC4); using them here does not assume the integral theorem. If \(\phi:[c,d]\to[a,b]\) is \(C^1\) and \(f\) is continuous, the derivative of \(F\circ\phi\), for this actual \(F\), is \(f(\phi(t))\phi'(t)\). Thus

\[
 \int_c^d f(\phi(t))\phi'(t)\,dt
 =\int_{\phi(c)}^{\phi(d)}f(s)\,ds.
\tag{OC14}
\]

No monotonicity is needed for this signed derivative substitution. The right side retains its endpoint orientation; the statement does not identify integrals of absolute Jacobians for a noninjective map. Likewise for \(C^1\) scalar functions \(u,v\),

\[
 \int_a^b u'(t)v(t)\,dt
 =u(b)v(b)-u(a)v(a)-\int_a^b u(t)v'(t)\,dt.
\tag{OC15}
\]

For a bilinear map use its actual ordered product in this formula. Complex and matrix entries are integrated in their real coordinates. In particular no noncommuting factors are interchanged. Piecewise \(C^1\) paths are treated by summing over their actual finitely many subintervals; intermediate endpoints cancel only after their matching values are displayed.

### 13.5. Product, chain and full finite-coordinate derivative maps

#### 13.5.1. Pointwise product and chain maps

For scalar \(f,g\) differentiable at \(x\), subtraction of their actual product gives

\[
 \frac{f(x+h)g(x+h)-f(x)g(x)}h
 =\frac{f(x+h)-f(x)}h\,g(x+h)
   +f(x)\frac{g(x+h)-g(x)}h.
\tag{OC16}
\]

Limits from Section 13.1 give \((fg)'=f'g+fg'\). The same identity holds for a bilinear product with the factor order shown. For a nonzero \(g(x)\), write the reciprocal difference as \(-[g(x+h)-g(x)]/[g(x+h)g(x)]\); its quotient limit is \(-g'(x)/g(x)^2\). Every actual denominator remains present in its local domain.

Let \(g:I\to\mathbb R\) be differentiable at \(x\), and \(f\) differentiable at \(g(x)\). In (OC4) for \(f\), set \(\Delta=g(x+h)-g(x)\). Since \(\Delta=h[g'(x)+r_x(h)]\), it tends to zero. Put the remainder at \(\Delta=0\) equal to zero; its value there contributes zero. The exact composition difference is

\[
 f(g(x+h))-f(g(x))
 =f'(g(x))h[g'(x)+r_x(h)]
   +h[g'(x)+r_x(h)]\,r_{g(x)}(\Delta).
\tag{OC17}
\]

Dividing by \(h\) proves the chain rule. The outer function need be differentiable only at the image point; domain membership of the composed values is required. This includes the one-sided endpoint versions with their actual increments.

In finite real coordinates, \(f:U\subset\mathbb R^n\to\mathbb R^q\) is differentiable at \(x\) when it has a linear map \(A\) and remainder \(r(h)\) with \(|r(h)|_2/|h|_2\to0\) and \(f(x+h)=f(x)+Ah+r(h)\).

The derivative map is unique. For two such maps \(A,\widetilde A\), subtract their full remainder identities and set \(h=t e_j\), \(t\ne0\). Dividing by \(|t|\) shows that \(|(A-\widetilde A)e_j|_2\) tends to zero, so this fixed value is zero. Every column therefore agrees. When the domain dimension is zero there is only the unique zero linear map. In the composition below, \(g\)'s domain must contain \(f(x+h)\) for the asserted small increments, as it does when \(g\)'s domain is an open neighborhood of \(f(x)\).

For \(g\) with linear map \(B\) at \(f(x)\), let \(\Delta=Ah+r(h)\). The full composition remainder is

\[
 g(f(x+h))-g(f(x))-BAh
 =B r(h)+s(\Delta).
\tag{OC18}
\]

A finite matrix is bounded by its full entries, as proved in the finite-algebra foundation. Thus \(|\Delta|_2\le(\|A\|+1)|h|_2\) for small \(h\), and each term on the right, divided by \(|h|_2\), tends to zero. The \(\Delta=0\) case has \(s(0)=0\). This proves the finite-coordinate chain map \(BA\). Its \((k,j)\) coordinate is the full sum \(\sum_{\ell=1}^qB_{k\ell}A_{\ell j}\). For original domain and target bases the derivative is exactly \(J_cAJ_b^{-1}\); (OC3) on both sides proves the equivalence with differentiability in their original norms. No coordinate, intermediate dimension or zero-dimensional case is suppressed.

#### 13.5.2. Continuous partials and higher-coordinate tensors

If all first partial derivatives of \(f\) exist and are continuous in a neighborhood, take an actual coordinate box inside \(U\), and put \(h^{(j)}=(h_1,\ldots,h_j,0,\ldots,0)\). The one-variable fundamental theorem on each coordinate segment gives

\[
 \begin{aligned}
 f(x+h)-f(x)
 &=\sum_{j=1}^n h_j\int_0^1
       \partial_jf(x+h^{(j-1)}+s h_j e_j)\,ds,\\
 f(x+h)-f(x)-\sum_{j=1}^n h_j\partial_jf(x)
 &=\sum_{j=1}^n h_j\int_0^1
   [\partial_jf(x+h^{(j-1)}+s h_j e_j)-\partial_jf(x)]\,ds.
 \end{aligned}\tag{OC19}
\]

All the displayed points remain in that box and converge uniformly to \(x\) as \(h\to0\). The norm of the second line is at most
\(\sum_j|h_j|\) times the largest derivative difference. Since \(\sum_j|h_j|\le\sqrt n\,|h|_2\), the remainder divided by \(|h|_2\) tends to zero. This proves the derivative and its continuity. Conversely a continuous derivative has the asserted continuous partials by evaluation on the actual coordinate vectors.

For \(C^2\) functions, mixed partials commute. Here is the exact rectangle proof, including its integral input. A continuous function on a compact coordinate rectangle has uniformly continuous values. Finite rectangular tagged sums converge uniformly to either iterated integral: their error is bounded by rectangle area times the common oscillation on a small rectangle. The same sums therefore prove equality of the two iterated integrals, entry by entry, with the signed side lengths if orientation is reversed. Now subtract the four original corner values of \(f\) at \(x\), \(x+h e_j\), \(x+k e_\ell\) and \(x+h e_j+k e_\ell\). Applying (OC13) successively in the two orders gives

\[
 \begin{aligned}
 &f(x+h e_j+k e_\ell)-f(x+h e_j)-f(x+k e_\ell)+f(x)\\
 &=\int_0^h\int_0^k
    \partial_\ell\partial_jf(x+s e_j+t e_\ell)\,dt\,ds\\
 &=\int_0^k\int_0^h
    \partial_j\partial_\ell f(x+s e_j+t e_\ell)\,ds\,dt.
 \end{aligned}\tag{OC20}
\]

Divide by the actual nonzero product \(hk\) and let both increments tend to zero. Each normalized integral tends to its continuous integrand at \(x\), by the same uniform bound used in (OC12). This proves equality at every point, including each original component. For \(j=\ell\) there is only one derivative order. In \(C^r\), adjacent interchanges applied to the remaining \(C^2\) derivative prove every permutation of up to \(r\) partials. These assertions require the stated neighborhood regularity; existence of two pointwise mixed derivatives alone has not been used.

For clarity, the full higher derivative used below is the actual coordinate multilinear map

\[
 D^r f(x)[h_1,\ldots,h_r]
 =\sum_{j_1=1}^n\cdots\sum_{j_r=1}^n
    \partial_{j_1}\cdots\partial_{j_r}f(x)
       \prod_{\ell=1}^r h_{\ell,j_\ell},
 \qquad r\ge1.
\tag{OC20a}
\]

Here \(C^r\) means that all coordinate partial derivatives through order \(r\) exist and are continuous on the actual open domain. At \(r=1\), (OC19) proves this formula and its derivative remainder. For the induction, regard all order-\(r\) partials as their finite array of scalar or original vector coordinates. Apply (OC19) to that array: its derivative has precisely all order-\(r+1\) partials, with the additional last direction coordinate. Finite sums and the product in (OC20a) give the displayed next multilinear map, and finite-coordinate norm comparison gives its continuity in the actual multilinear operator norm. This proves that the coordinate \(C^r\) definition agrees with \(r\) continuous iterated derivatives, with both directions of the comparison: conversely evaluate each iterated derivative on the original coordinate vectors to recover every partial and its continuity. The derivative of a finite multilinear coordinate expression uses the same proved ordered product rule. Original bases transport this tensor by \(J_c\) on the output and by \(J_b^{-1}\) on every input separately, retaining every basis factor; no input norm is replaced. In dimension zero the sum at positive order is empty and the derivative is its unique zero multilinear map; order zero is the original value of \(f\). This also proves the exact tensor meanings used in the higher chain and Taylor formulas.

### 13.7. Uniform limits and differentiation of the actual series

A uniformly Cauchy sequence of maps into an original finite complete normed space has a pointwise limit by (OC3). Passing the Cauchy inequality to this pointwise limit proves uniform convergence, with the same error bound. A uniform limit of continuous functions is continuous: use one fixed approximant with uniform error below \(\epsilon/3\), then its continuity, then the second uniform error. This works on any domain where the uniform bound is asserted.

Let \(F_N\in C^1([a,b],V)\), assume \(F_N(a)\to v\) and \(F_N'\to G\) uniformly. The limit \(G\) is continuous, and (OC13) gives

\[
 F_N(x)=F_N(a)+\int_a^x F_N'(s)\,ds,\qquad
 F(x)=v+\int_a^x G(s)\,ds,
\tag{OC25}
\]

with
\(\sup_x N(F_N(x)-F(x))
\le N(F_N(a)-v)+(b-a)\sup_sN(F_N'(s)-G(s))\).
Thus \(F_N\to F\) uniformly, \(F'=G\), and both actual endpoint values are retained. Apply this argument to each derivative to obtain the theorem at every finite order when the corresponding derivative sequences converge uniformly. It does not permit differentiating an arbitrary pointwise convergent series. Matrix entries and complex values use their actual finite-coordinate maps and original norms.

Define the actual scalar series, retaining every coefficient,

\[
 E(z)=\sum_{k=0}^\infty\frac{z^k}{k!},\qquad
 E_N(z)=\sum_{k=0}^N\frac{z^k}{k!}.
\tag{OC26}
\]

For any fixed \(R\ge0\), choose an integer \(N\) with \(N+2\ge2R\). On \(|z|\le R\), the ratio of successive tail majorants is at most \(1/2\), and

\[
 \sum_{k=N+1}^\infty\frac{|z|^k}{k!}
 \le\frac{R^{N+1}}{(N+1)!}
       \sum_{\ell=0}^\infty2^{-\ell}
 =\frac{2R^{N+1}}{(N+1)!}.
\tag{OC27}
\]

The displayed leading term tends to zero: beyond the same threshold successive leading terms have ratio at most \(1/2\). The finite earlier terms are retained. For \(R=0\), all terms with positive degree vanish and the series is one. The \(r\)-th derivative along a real parameter of \(E_N(ct)\), where \(c\) is an original real or complex scalar, is
\(\sum_{k=r}^N c^k t^{k-r}/(k-r)!\).
Its absolute series is bounded by \(|c|^r E(|c|\,|t|)\); the same tail argument, with the shifted index, gives uniform convergence on every compact real interval. Therefore (OC25), starting with the actual values at zero, proves

\[
 \frac{d^r}{dt^r}E(ct)=c^rE(ct),\qquad E(0)=1.
\tag{OC28}
\]

For the complex variable \(z=u+iv\), apply this argument separately to \(u\) and \(v\). It proves continuous partial derivatives \(\partial_uE=E\) and \(\partial_vE=iE\) on every compact coordinate box. The full finite-coordinate derivative (OC19) is multiplication by the original scalar \(E(z)\), so the complex difference quotient also tends to \(E(z)\): its real-coordinate remainder has norm \(o(|h|)\), and division by the nonzero complex \(h\) has modulus \(1/|h|\). This proves complex differentiability here from the actual series, rather than assuming a complex Cauchy theorem.

Absolute convergence justifies the product of two scalar series at its exact coefficients. To see this without assuming rearrangement, truncate the double sum to a square; the error against the full product is bounded by one tail times the full absolute sum of the other series, in each of the two variables. Both tails tend to zero. The same bound lets the square be compared with a sufficiently large triangle, since the omitted terms have total degree tending to infinity and belong to the union of the two large-index tails. Within a finite triangle the binomial theorem is finite induction. Hence

\[
 E(z)E(w)
 =\sum_{m=0}^\infty\sum_{k=0}^m
       \frac{z^k w^{m-k}}{k!(m-k)!}
 =\sum_{m=0}^\infty\frac{(z+w)^m}{m!}
 =E(z+w),\qquad E(z)E(-z)=1.
\tag{OC29}
\]

All denominators and both inverse factors remain in the comparison. No rearrangement of a conditionally convergent series has been used.

### 13.8. Original exponential, logarithm and every real power

For real \(t\ge0\), every term in (OC26) is nonnegative, and \(E(t)\ge1+t>0\). For \(t<0\), (OC29) gives \(E(t)=1/E(-t)>0\). Its derivative \(E'=E\) and the mean value theorem therefore make \(E\) strictly increasing on the entire original real line. It tends to infinity at the positive end by \(E(t)\ge1+t\), and to zero at the negative end by its exact inverse. Continuity and the intermediate-value theorem show that its range is precisely \((0,\infty)\).

This is the course's original real exponential \(e^t\). The exact comparison is also forced if that exponential was introduced as the solution of \(f'=f\), \(f(0)=1\): for any such original \(f\), differentiation of \(E(-t)f(t)\) gives \(-E(-t)f(t)+E(-t)f'(t)=0\), so it is constantly one and both original inverse factors prove \(f(t)=E(t)\). The notation \(E\) records this comparison; it does not rescale \(t\) or replace the original function.

For \(x>0\), define

\[
 L(x)=\int_1^x\frac{ds}{s},\qquad
 L'(x)=\frac1x,\qquad L(1)=0.
\tag{OC30}
\]

The integrand is continuous on the actual compact interval between \(1\) and \(x\), with its original positive lower endpoint. The fundamental theorem proves the derivative. The chain rule gives
\((L(E(t)))'=E(t)/E(t)=1\);
the zero initial value gives \(L(E(t))=t\). Since \(E\) is onto the positive reals, \(E(L(x))=x\) for every \(x>0\). Thus \(L\) is exactly the original real logarithm, with both compositions and domains proved.

For fixed \(y>0\), the derivative in \(x>0\) of \(L(xy)-L(x)\) is \(y/(xy)-1/x=0\). At \(x=1\) it equals \(L(y)\), so \(L(xy)=L(x)+L(y)\). The same actual derivative, or the inverse product in (OC29), proves \(L(x^{-1})=-L(x)\). All these identities retain their original nonzero-domain restrictions.

For any original real exponent \(s\) and \(x>0\), the power is the exact map

\[
 x^s=E(sL(x)),\qquad
 \frac{d}{dx}x^s=\frac{s}{x}E(sL(x))
   =s\,x^{s-1}.
\tag{OC31}
\]

The final comparison uses \(E((s-1)L(x))E(L(x))=E(sL(x))\) and \(E(L(x))=x\); the original factor \(x^{-1}\) has not disappeared without a proved inverse identity. For integer \(s\ge0\), induction in (OC29) identifies this value with the full repeated product; for negative integers it gives the actual reciprocal. For \(s=p/q\), \(q\ge1\), it has \(q\)-th power \(x^p\) and is positive; the earlier unique positive-root proof identifies it with that original root. No rational approximation is required to define a general real exponent. The formulas \(x^{s+t}=x^sx^t\), \((xy)^s=x^sy^s\) and \((x^s)^t=x^{st}\) follow from the two exact inverse maps and (OC29)–(OC30), with \(x,y>0\).

Every further derivative is proved by induction:

\[
 \frac{d^r}{dx^r}x^s
 =\left(\prod_{j=0}^{r-1}(s-j)\right)x^{s-r},
 \qquad r\ge0.
\tag{OC32}
\]

For \(r=0\) the product is empty and equals one. Zero factors remain in the formula when \(s\) is an integer and the derivative vanishes. The working domain is \(x>0\); no differentiability at zero for arbitrary \(s\) is inferred. For negative \(s\), the sign in (OC31) proves decreasing powers on that domain, and for positive \(s\) it proves increasing powers. This supplies the original positive frequency-bracket bounds without changing their exponents.

### 13.9. Arctangent, circular parameters and the original pi

Define \(C(t)\) and \(S(t)\) by the real and imaginary coordinates of the actual \(E(it)\), not by assumed trigonometric derivatives. The absolute convergence above gives

\[
 \begin{aligned}
 C(t)&=\sum_{k=0}^\infty\frac{(-1)^k t^{2k}}{(2k)!},
 &S(t)&=\sum_{k=0}^\infty\frac{(-1)^k t^{2k+1}}{(2k+1)!},\\
 C'&=-S,\quad S'=C,\quad C(0)=1,\quad S(0)=0,
 &C(t)^2+S(t)^2&=1.
 \end{aligned}\tag{OC33}
\]

The last identity is the full product \(E(it)E(-it)=1\), since conjugating the original coefficients gives \(E(-it)=\overline{E(it)}\). The full addition laws are the two coordinates of (OC29):

\[
 C(s+t)=C(s)C(t)-S(s)S(t),\qquad
 S(s+t)=S(s)C(t)+C(s)S(t).
\tag{OC34}
\]

There is a first positive zero \(t_0\) of \(C\). Indeed continuity gives a zero-free positive neighborhood of zero. At \(t=2\), the first three terms have value \(1-2+2/3=-1/3\). The remaining terms can be grouped into negative/positive consecutive pairs starting at \(k=3\); the absolute terms strictly decrease because their successive ratio is \(4/[(2k+1)(2k+2)]<1\). Every pair is negative, so \(C(2)<-1/3\). Intermediate values give a zero in \((0,2)\); its least positive one is the attained minimum of the closed zero set outside the zero-free neighborhood. Before \(t_0\), continuity and the absence of zeros give \(C>0\), so \(S'=C>0\), and \(S(t_0)=1\) by (OC33). Oddness of \(S\) and evenness of \(C\) follow term by term. Thus on \((-t_0,t_0)\), \(C>0\) and

\[
 T(t)=\frac{S(t)}{C(t)},\qquad
 T'(t)=\frac{C(t)^2+S(t)^2}{C(t)^2}
       =1+T(t)^2.
\tag{OC35}
\]

The denominator is the actual \(C^2\), and the equality uses the previously proved full identity. \(T\) is strictly increasing, and tends to the respective infinities at the two endpoints because \(S\to\pm1\) and \(C\to0\) positively. It is therefore a bijection onto the original real line. Define

\[
 A(x)=\int_0^x\frac{ds}{1+s^2},\qquad
 A'(x)=\frac1{1+x^2}.
\tag{OC36}
\]

The denominator is strictly positive. The derivative of \(A(T(t))\) is \(T'(t)/(1+T(t)^2)=1\), and its value at zero is zero, so \(A(T(t))=t\). Surjectivity gives \(T(A(x))=x\) with \(A(x)\in(-t_0,t_0)\). This constructs the original principal arctangent with both inverse maps and its full domain. In particular \(A(x)\to t_0\) as \(x\to+\infty\): for each \(t<t_0\), \(x>T(t)\) implies \(A(x)>t\), and all \(A(x)<t_0\). The negative limit is \(-t_0\).

The actual circle parameter has its original pi, rather than a newly chosen scale. From \(E(it_0)=i\), (OC29) gives \(E(2it_0)=-1\) and \(E(4it_0)=1\). On \((0,t_0)\), \(S,C>0\). Formula (OC34) at twice \(t_0/2\) gives \(C(t_0/2)^2=S(t_0/2)^2\), hence \(T(t_0/2)=1\) and \(A(1)=t_0/2\). Thus the usual inverse-tangent definition \(\pi=4\arctan(1)\) gives exactly \(\pi=2t_0\).

The same comparison agrees with the geometric original circle constant. For any \(C^1\) real-coordinate curve \(\gamma:[a,b]\to\mathbb R^d\), its polygon length is the sum of the actual norms \(\sum_j|\gamma(t_j)-\gamma(t_{j-1})|_2\). The fundamental theorem writes each increment as the integral of \(\gamma'\). Choose a sample \(\xi_j\). Uniform continuity of \(\gamma'\) bounds the norm of the difference from \((t_j-t_{j-1})\gamma'(\xi_j)\) by \((t_j-t_{j-1})\omega(\operatorname{mesh}P)\), where \(\omega(\delta)\to0\). The reverse triangle inequality therefore shows that the polygon length differs from \(\sum_j|\gamma'(\xi_j)|_2(t_j-t_{j-1})\) by at most \((b-a)\omega(\operatorname{mesh}P)\). Consequently fine polygon lengths tend to \(\int_a^b|\gamma'|_2\). Any fixed coarser polygon is bounded by this integral, by (OC11) interval by interval; refinement increases polygon length by the triangle inequality. Their supremum is therefore the same integral.

For \(\gamma(t)=(C(t),S(t))\), \(|\gamma'|_2=(S^2+C^2)^{1/2}=1\). On \([0,t_0]\) this curve traverses the first quadrant exactly once: \(T\) increases from zero to infinity and \(C,S>0\) recover its unique unit vector. The addition laws at \(t_0,2t_0,3t_0\) give the other quadrants with the actual orientations and endpoints. Hence the circumference of the original unit circle is \(4t_0\), and its half-circumference definition also gives \(\pi=2t_0\). For radius \(r>0\), retain the map \(r(C,S)\); its speed and circumference are \(r\) and \(4rt_0=2\pi r\).

The exact quadrant inverse for an original unit vector \((u,v)\) with \(u>0,v\ge0\) is \(t=A(v/u)\). Indeed (OC35)–(OC36) give \(S(t)/C(t)=v/u\), while positivity and the full square sum give
\(C(t)=[1+(v/u)^2]^{-1/2}=u\) and
\(S(t)=(v/u)[1+(v/u)^2]^{-1/2}=v\).
The missing vertical endpoint is exactly \((0,1)=\gamma(t_0)\). Thus both the coordinate map and inverse, including their actual endpoint, have been proved. The same original rotations from (OC34) give the other three quadrant maps.

Thus the full original circular parameter \(e^{i\theta}=E(i\theta)\) is \(2\pi\)-periodic, and its derivative is \(iE(i\theta)\). Its integrals retain all constants:

\[
 \int_a^b E(i n\theta)\,d\theta
 =\begin{cases}
   [E(i n b)-E(i n a)]/(i n),&n\in\mathbb Z\setminus\{0\},\\
   b-a,&n=0.
 \end{cases}
\tag{OC37}
\]

For \([0,2\pi]\) the nonzero-integer numerator is zero by the proved original period, while the zero mode contributes \(2\pi\). This supplies the circular and rectangular contour computations without a hidden trigonometric or angular-scale assumption.

### 13.10. The actual smooth cutoff with all endpoint constants

Keep the function from this lesson:

\[
 \eta(s)=\begin{cases}0,&s\le0,\\ E(-1/s),&s>0.\end{cases}
 \qquad
 \chi(s)=\frac{\eta(3/2-s)}
               {\eta(3/2-s)+\eta(s-1)}.
\tag{OC38}
\]

For \(s>0\), chain and product differentiation give

\[
 \eta^{(r)}(s)=E(-1/s)P_r(1/s),\qquad
 P_0(u)=1,\quad
 P_{r+1}(u)=u^2[P_r(u)-P_r'(u)].
\tag{OC39}
\]

This exact recursion retains every polynomial coefficient, sign and power. If \(u>0\) and \(m\ge0\) is an integer, the positive series gives \(E(u)\ge u^{m+1}/(m+1)!\), whence

\[
 0\le u^mE(-u)
 \le\frac{(m+1)!}{u}\longrightarrow0
 \quad(u\longrightarrow+\infty).
\tag{OC40}
\]

Every term of \(P_r(u)\), and of \(uP_r(u)\), therefore tends to zero after multiplication by \(E(-u)\). It follows first that \(\eta\) is continuous at zero. Inductively, extend the positive-side \(r\)-th derivative by zero for \(s\le0\). It is continuous at zero, and its derivative there is the limit of \(E(-1/s)P_r(1/s)/s\), which is zero by the just-proved estimate. Its derivative away from zero is precisely the next recursion. This proves \(\eta\in C^\infty(\mathbb R)\) and every derivative zero at the original endpoint.

The denominator in \(\chi\) is strictly positive for every real \(s\). Otherwise both terms would vanish, requiring simultaneously \(s\ge3/2\) and \(s\le1\). The full reciprocal and product rules show that \(\chi\) is smooth, with \(0\le\chi\le1\), \(\chi=1\) for \(s\le1\), and \(\chi=0\) for \(s\ge3/2\). The function \(\chi\) itself is not asserted to have compact support on the whole real line: its negative half-line is one. On \([0,\infty)\) its support is exactly \([0,3/2]\).

The actual Euclidean cutoff is \(\theta(x)=\chi(\sum_{j=1}^d x_j^2)\). The inner function is a polynomial in every original coordinate. The proved full chain rules therefore make \(\theta\) smooth; it equals one when \(\sum_jx_j^2\le1\) and vanishes when \(\sum_jx_j^2\ge3/2\). Its support is the full closed ball \(\sum_jx_j^2\le3/2\), compact by the proved original topology. Every derivative is continuous on that support and zero outside it; compact extrema give its actual finite derivative bounds. In dimension zero the entire space is a point, the value is one and its support is compact; no nonexistent coordinate derivative is assigned.

For any specified original center \(x_0\) and radii \(0\le r<R\), the map
\[
 x\longmapsto
 \chi\left(1+\frac{\sum_{j=1}^d(x_j-x_{0j})^2-r^2}{2(R^2-r^2)}\right)
\tag{OC41}
\]
retains every translation, square and denominator. It equals one on the closed radius-\(r\) ball. Its nonzero set is exactly the open radius-\(R\) ball, because the full cutoff is positive precisely when its scalar input is below \(3/2\). Its support is therefore the full closed radius-\(R\) ball, including the outer sphere where the value itself is zero. In dimension zero the domain is its single point and these sets have that same one-point meaning. This is a proved coordinate construction, not a change to the original cutoff in (OC38). For an open domain and any one of its points, choose an outer ball whose closure lies inside that domain; the construction gives the required local compact cutoff.

For a locally finite family of supports, every point has a neighborhood meeting only finitely many of them. All other functions and all their derivatives vanish on that neighborhood. Its full sum and every derivative are therefore the corresponding finite sums there. The same argument applies to a compact set by its finite neighborhood subcover. No interchange of an uncontrolled infinite derivative sum is asserted.

## References

- [Lebl] Jiří Lebl, *Basic Analysis*, [author's LaTeX source](https://github.com/jirilebl/ra/tree/e21ec524ca7d54f800c693b948020c188d21d01f).
- [Axler] Sheldon Axler, *Measure, Integration & Real Analysis*, [author's online edition](https://measure.axler.net/).

