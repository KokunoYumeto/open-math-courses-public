# Roth's theorem and its consequences

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; sections 6–8 by Claude Opus 5.5 (Anthropic). Self-checked by the writing AI. Original material is public domain (CC0).*

The two previous lessons supply opposite index bounds. An integer polynomial can have large index at an algebraic point, with height exponential in its degree. At rational points with separated denominators and degrees, that height forces its index to be small. Good approximation would make all the low-weight derivatives too small to be nonzero rationals. This is the contradiction which proves Roth's theorem.

The second half extends this method to products of local approximation boxes. We prove the necessary lattice and algebraic-point index estimates, construct a polynomial on a product of boxes, and use exterior powers to obtain the Subspace theorem. Its two-dimensional case gives Lang's and Ridout's theorems. Its higher-dimensional case proves finiteness for nondegenerate \(S\)-unit equations and hence Thue–Mahler equations. The number-field foundations are identified where used; the approximation arguments and all four exercise solutions are supplied here.

We use Theorem 10.7 of The index method for rational approximation and Theorem 11.3 of Wronskians and Roth's rational-point lemma. Their complete parameter conditions are retained below. The finite Taylor formula and coefficient norm are proved in Lemmas 10.3–10.4. The normalization used below is still Solution 3 of Lesson 10; the construction is Theorem 10.7 and the rational-point bound is Theorem 11.3.

## 1. The complete approximation proof

### Theorem 12.1. Roth's theorem

For every real irrational algebraic number \(\alpha\) and every \(\delta>0\), there are only finitely many reduced rationals \(p/q\), \(q>0\), with

\[
                           |\alpha-p/q|<q^{-2-\delta}.
                           \tag{12.1}
\]

**Proof.** The fractional linear normalization proved in Lesson 10, Solution 3, reduces the assertion to an algebraic integer \(\alpha\) with \(|\alpha|<1\). That reduction sends infinitely many exceptional approximations of exponent \(2+\delta\) to infinitely many of some exponent strictly above two, so proving every positive parameter in the normalized case suffices. Suppose, for contradiction, that such a normalized \(\alpha\) has infinitely many approximations (12.1). Reducing the parameter if necessary, assume \(0<\delta\leq1/2\). Set

\[
                     \varepsilon=\delta/20,
 \qquad m\geq\max\{2,d/(2\varepsilon^2)\},
                     \tag{12.2}
\]

where \(d=\deg\alpha\). Write \(C_\alpha\) for the index-construction constant in Theorem 10.7 and \(C=C(m,\varepsilon)\) for the rational-point constant in Theorem 11.3. Neither depends on the variable degrees chosen next.

The exceptional reduced denominators are unbounded: a bounded denominator admits only finitely many rationals in a bounded interval. Choose the first approximation so large that

\[
 q_1\geq2^{2mC},\qquad
 \log q_1\geq Cm\log C_\alpha,\qquad
 \varepsilon\log q_1>\log(8C_\alpha).
 \tag{12.3}
\]

Choose subsequent exceptional approximations successively with

\[
                   \log q_{j+1}>(1+\varepsilon)C\log q_j.
                   \tag{12.4}
\]

There is no upper bound on these denominators; that is exactly why an assumed infinite set supplies each choice. Now choose a positive integer \(d_1\) with \(\varepsilon d_1\log q_1\geq\log q_m\), put \(L=d_1\log q_1\), and for \(j\geq2\) set

\[
                d_j=\left\lceil L/\log q_j\right\rceil.
\]

Then every \(d_j\) is positive and

\[
 L\leq d_j\log q_j\leq(1+\varepsilon)L,
 \qquad d_j>C d_{j+1}.
 \tag{12.5}
\]

For the first inequality use \(\log q_j\leq\log q_m\leq\varepsilon L\) to control ceiling error; for \(j=1\) equality holds at the lower endpoint. For the ratio divide the two inequalities in (12.5) and multiply by (12.4):
\(d_j/d_{j+1}\geq(1+\varepsilon)^{-1}\log q_{j+1}/\log q_j>C\).

Theorem 10.7 now gives a nonzero integer polynomial \(P\) with these variable-degree bounds, height \(H(P)\leq C_\alpha^D\), \(D=\sum d_j\leq md_1\), and index at \(\boldsymbol\alpha=(\alpha,\ldots,\alpha)\) greater than \(m(1-\varepsilon)/2\). The second condition in (12.3) gives

\[
                       H(P)\leq q_1^{d_1/C}.
\]

All hypotheses of Theorem 11.3 hold: degree separation is (12.5), every denominator is at least \(q_1\), and \(q_j^{d_j}\geq q_1^{d_1}\) is the first part of (12.5). That theorem therefore gives index at the rational point \(\boldsymbol p/\boldsymbol q\) at most \(\varepsilon\).

We prove the opposite inequality by showing that every derivative \(Q=D_{\boldsymbol i}P\) with \(\sum i_j/d_j\leq\varepsilon\) is zero at that point. The Taylor coefficients of \(P(\boldsymbol\alpha+\boldsymbol T)\) have sum of absolute values at most

\[
 \sum_{\boldsymbol j}|p_{\boldsymbol j}|(1+|\alpha|)^{|\boldsymbol j|}
          \leq2^D\prod_j(d_j+1)H(P)\leq4^D H(P).
\]

Differentiating this expansion by a divided derivative multiplies each surviving coefficient by a product of binomial coefficients at most \(2^D\). Thus the sum for the shifted expansion of \(Q\) is at most

\[
                (8C_\alpha)^D<\exp(\varepsilon mL).
                \tag{12.6}
\]

The index derivative rule of Lemma 10.4 shows that every nonzero shifted coefficient of \(Q\) has weight greater than

\[
              \frac m2(1-\varepsilon)-\varepsilon
                       \geq\frac m2(1-3\varepsilon).
\]

For such an exponent vector \(\boldsymbol j\), the approximation bounds and the lower bounds in (12.5) give

\[
 \prod_r|p_r/q_r-\alpha|^{j_r}
     <\exp\left(-(2+\delta)L\sum_r j_r/d_r\right)
     \leq\exp\left(-mL(1+\delta/2)(1-3\varepsilon)\right).
\]

Together with (12.6), this yields

\[
 |Q(\boldsymbol p/\boldsymbol q)|
       <\exp\left[-mL\bigl((1+\delta/2)(1-3\varepsilon)
                                      -\varepsilon\bigr)\right].
       \tag{12.7}
\]

Its exponent factor exceeds \(1+\varepsilon\), since

\[
 (1+\delta/2)(1-3\varepsilon)-\varepsilon-(1+\varepsilon)
   =\delta/2-5\varepsilon-3\delta\varepsilon/2>0
\]

for \(\varepsilon=\delta/20\), \(0<\delta\leq1/2\). On the other hand, \(Q\) has integer coefficients and its value is rational with denominator dividing \(\prod q_j^{d_j}\). Any nonzero value has absolute value at least its reciprocal. Equation (12.5) bounds that product above by \(\exp((1+\varepsilon)mL)\), while (12.7) is strictly below its reciprocal. The value must be zero. A zero derivative polynomial already has zero value, so this conclusion holds for every \(\boldsymbol i\) of weight at most \(\varepsilon\).

The rational-point index is therefore greater than \(\varepsilon\), contradicting its upper bound from Theorem 11.3. This rules out an infinite exceptional set and proves the theorem. \(\square\)

The proof also completes Proposition 10.2: every irreducible integer binary form of degree at least three has finitely many solutions to a fixed integer value. The case of value zero and the common-divisor issue were included there. No effective upper bound for the solutions is asserted.

## 2. Lacunary series become transcendental

### Corollary 12.2. A series with cubic gaps

For every integer \(b\geq2\), the real number

\[
                             \xi_b=\sum_{n=0}^\infty b^{-3^n}
                             \tag{12.8}
\]

is transcendental.

**Proof.** Its \(N\)-th truncation is \(p_N/q_N\), with \(q_N=b^{3^N}\). The numerator is congruent to one modulo every prime dividing \(b\), because its last term contributes one and all earlier terms contain a positive power of \(b\). The fraction is reduced. Its positive tail satisfies

\[
             0<\xi_b-p_N/q_N<2b^{-3^{N+1}}=2q_N^{-3}.
             \tag{12.9}
\]

For the bound, the first omitted term is \(T=q_N^{-3}\leq1/8\); subsequent terms are \(T^3,T^9,\ldots\), bounded by \(T^2,T^3,\ldots\), so their sum with \(T\) is at most \(T/(1-T)<2T\).

The number is irrational. If it were \(a/c\) in reduced form, its nonzero difference from any truncation would be at least \(1/(cq_N)\), contradicting (12.9) for large \(q_N\). If it were irrational algebraic, (12.9) would be smaller than \(q_N^{-5/2}\) for all large \(N\), giving infinitely many exceptions to Theorem 12.1 with \(\delta=1/2\). Thus it is transcendental. \(\square\)

These fixed-exponent approximations do not constitute a Liouville number proof: their exponent is three, whereas Liouville's lower bound depends on a putative algebraic degree that could be three or larger. Roth removes that dependence.

## 3. Small values of a binary form

### Corollary 12.3. A lower bound outside finitely many pairs

For an irreducible binary form \(F\in\mathbb Z[X,Y]\) of degree \(d\geq3\) and any \(\varepsilon>0\), all but finitely many nonzero integer pairs satisfy

\[
              |F(x,y)|\geq\max(|x|,|y|)^{d-2-\varepsilon}.
              \tag{12.10}
\]

**Proof.** There is no nonzero rational zero of \(F\), as in Proposition 10.2. If \(\varepsilon\geq d-2\), its nonzero integer value already has absolute value at least one. Assume \(0<\varepsilon<d-2\). For primitive pairs, near each real root \(\alpha\) of \(F(T,1)\), the other distinct factors are bounded below, \(|y|\) is comparable with \(H=\max(|x|,|y|)\), and Roth's theorem with parameter \(\varepsilon/2\) gives

\[
                      |F(x,y)|\geq cH^{d-2-\varepsilon/2}
\]

for all sufficiently large such pairs. On a compact set away from the roots, or where \(|x/y|\) is large, homogeneity and the nonzero leading coefficient instead give \(|F(x,y)|\geq c'H^d\). The finitely many roots permit one positive constant to cover the first bound. Its ratio to the desired right-hand side tends to infinity like \(H^{\varepsilon/2}\).

For an arbitrary pair write \((x,y)=g(x_0,y_0)\) with a primitive pair and \(g>0\). If its primitive pair is sufficiently large, homogeneity improves the ratio to the requested bound by \(g^{2+\varepsilon}\), so the bound still holds. Only finitely many primitive pairs remain. Each has \(F(x_0,y_0)\ne0\), and the same ratio tends to infinity as \(g\to\infty\). There are only finitely many exceptional multiples of these finitely many pairs. \(\square\)

## 4. Why the proof gives finiteness without a denominator bound

The constants in Theorems 10.7 and 11.3 precede the choice of approximations. In (12.3)–(12.4), an assumed infinite set then supplies denominators beyond every chosen threshold. The contradiction proves that this supply cannot continue. It gives no way to find how far the finite actual set extends. The theorem is therefore ineffective in the assertion of a last exceptional denominator.

This distinction does not weaken the finiteness conclusions, but it matters when solving an equation. To list its solutions, one needs an explicit search bound or another termination argument. The existing logarithms-course lesson Thue equations, effectively, Section 4, treats the later effective improvement through lower bounds for linear forms in logarithms. The statement is Fel'dman's theorem of 1971 (Evertse, *Diophantine Approximation*, Chapter 6, Theorem 6.5): for every algebraic \(\alpha\) of degree \(n\geq3\), a computable \(\tau(\alpha)>0\) and a computable positive constant give \(|\alpha-p/q|\geq c q^{-n+\tau(\alpha)}\) for every rational approximation. It is a later application of the logarithm bounds, whereas the present Roth proof does not compute its exceptions.

### Bounding how many exceptions there are

The proof does give a computable bound on their number, even though it does not bound the largest denominator. Here is a direct, deliberately large bound. In the normalized case of Theorem 12.1, let \(Q_0\ge2^{2/\delta}\) also meet every threshold in (12.3). Choose an integer \(K_0\ge1\) with

\[
                    (1+\delta/2)^{K_0}>(1+\varepsilon)C.
\]

There are at most \((m-1)K_0\) exceptional reduced fractions of denominator at least \(Q_0\).

**Proof.** Two different reduced fractions with denominators \(q'\ge q\ge Q_0\) differ by at least \(1/(qq')\). If both are exceptional, their difference is less than \(2q^{-2-\delta}\), so \(q'>q^{1+\delta}/2\ge q^{1+\delta/2}\). In particular they cannot have equal denominators. After \(K_0\) steps in the ordered list, the log denominator grows by more than \((1+\varepsilon)C\). A list of \(1+(m-1)K_0\) exceptions would therefore supply \(m\) fractions meeting (12.3)–(12.4). The rest of the proof of Theorem 12.1 applies to that finite list without any infinitude assumption and gives the same contradiction.

The constants \(C_\alpha\) and \(C\) are computable from the formulas in Theorem 10.7 and (11.9); so are \(m,Q_0,K_0\). At denominators below \(Q_0\), the error inequality admits at most three numerators for each denominator, giving a further bound \(3\lceil Q_0\rceil\). For an arbitrary real algebraic irrational choose a positive integer \(A\) making \(A\alpha\) integral and put \(\beta=A\alpha-\lfloor A\alpha\rfloor\). This is an irrational algebraic integer in \((0,1)\). The rational map \(r\mapsto Ar-\lfloor A\alpha\rfloor\) is injective, its reduced denominators lie between \(q/A\) and \(q\), and its error is multiplied by \(A\). For sufficiently large, computably bounded \(q\), an original exponent \(2+\delta\) gives an image exponent \(2+\delta/2\). Apply the normalized count bound and add the finitely many smaller denominators. \(\square\)

A bound on cardinality is compatible with an exceptional denominator being extremely large. It does not tell a search when the last exception has been found. The classical quantitative result of this kind is due to Davenport and Roth (1955). Evertse's *Diophantine Approximation*, Chapter 6, §6.2, explains the same mechanism for Thue's method: a gap principle between solutions, and a contradiction obtained from finitely many suitably spaced solutions (the remark before Theorem 6.14, and Exercise 6.8).

### A numerical illustration

For \(\alpha=\sqrt[3]2\), the following table gives the first thirteen continued-fraction convergents and \(|\alpha-p/q|q^{2.1}\). The digits were checked using rational lower and upper bounds for \(\alpha\) whose cubes straddle two, at 110 decimal places.

| index | convergent \(p/q\) | \(\lvert\sqrt[3]2-p/q\rvert q^{2.1}\) |
|---:|---:|---:|
| 0 | \(1/1\) | 0.25992105 |
| 1 | \(4/3\) | 0.73743436 |
| 2 | \(5/4\) | 0.18234070 |
| 3 | \(29/23\) | 0.68655100 |
| 4 | \(34/27\) | 0.67078682 |
| 5 | \(63/50\) | 0.29187018 |
| 6 | \(286/227\) | 0.81160019 |
| 7 | \(349/277\) | 0.90861242 |
| 8 | \(635/504\) | 0.19639266 |
| 9 | \(5429/4309\) | 1.95018960 |
| 10 | \(6064/4813\) | 0.14770181 |
| 11 | \(90325/71691\) | 2.62850530 |
| 12 | \(96389/76504\) | 0.27260088 |

The values fluctuate. Roth says that only finitely many convergents have this scaled error below one; it predicts no monotonic trend and this finite table proves no bound for the remaining denominators.

## 5. Heights and boxes at several places

The extensions use simultaneous inequalities at real, complex and finite places. Fix a number field \(K\), put \(d=[K:\mathbb Q]\), and normalize its absolute values by

\[
 |a|_v=|\sigma_v(a)|^{d_v/d}\quad(v\mid\infty),\qquad
 |a|_v=(N\mathfrak p_v)^{-\operatorname{ord}_{\mathfrak p_v}(a)/d}
       \quad(v\nmid\infty),
 \tag{12.11}
\]

where \(d_v=1\) at a real place and \(d_v=2\) at a complex place. Thus \(\prod_v|a|_v=1\) for \(a\ne0\). For \(x\in K^N\setminus\{0\}\), write

\[
 \|x\|_v=\max_i|x_i|_v,\qquad H([x])=\prod_v\|x\|_v,\qquad h([x])=\log H([x]).
 \tag{12.12}
\]

The brackets emphasize that this height is projective: multiplication of all coordinates by the same nonzero scalar does not change it. Lesson 2 proves the height estimates and Northcott finiteness used here. The exact number-field foundations are the lessons Places of number fields in extensions and the product formula, Theorems 5.1 and 5.5, and Extensions of complete valued fields, Theorem 4.2. Their local-degree and product-formula normalization is the one used in (12.11).

Let \(S\) contain all infinite places. The ring \(\mathcal O_{K,S}\) consists of elements integral outside \(S\), and an \(S\)-unit has absolute value one outside \(S\). We will use the logarithmic \(S\)-unit lattice in the hyperplane \(\sum_{v\in S}t_v=0\). Its prerequisite is Dirichlet's unit theorem, Theorem 9.4.  Rescale that lesson's logarithms by \(1/d\) to obtain (12.11).

For each \(v\in S\), let \(L_{v,1},\ldots,L_{v,N}\) be independent \(K\)-linear forms. Boxes of the following shape encode the approximation inequalities:

\[
 \Pi(Q)_v=\{x:|L_{v,i}(x)|_v\le Q^{c_{v,i}}\ (1\le i\le N)\}
 \quad(v\in S),\qquad
 \Pi(Q)_v=\mathcal O_v^N\quad(v\notin S).
 \tag{12.13}
\]

At a finite place, replace each prescribed radius by the largest member of its value group not exceeding it. The ratio of the two radii lies between two fixed positive constants. This replacement affects volume comparisons by a fixed factor; it never changes their exponent of \(Q\).

Use ordinary Lebesgue measure at real places and on the two real coordinates of a complex place, and normalize finite Haar measure by \(\operatorname{vol}(\mathcal O_v)=1\). In this convention multiplication by \(a\) on one local coordinate multiplies measure by \(|a|_v^d\). Consequently

\[
 \operatorname{vol}\Pi(Q)\asymp_{K,S,L}Q^{d\sum_{v,i}c_{v,i}}.
 \tag{12.14}
\]

Here and below \(\asymp\) denotes upper and lower bounds by positive constants independent of \(Q\). Complex coordinates count twice in Lebesgue measure, as the factor \(d_v=2\) requires.

### Lemma 12.4. A successive-minima comparison

Let \(C\subset\mathbb R^M\) be a compact convex symmetric body with nonempty interior, let \(\Lambda\) be a full lattice, and let \(\lambda_1\le\cdots\le\lambda_M\) be its successive minima. Then

\[
 \frac{2^M}{M!}\det\Lambda
 \le \operatorname{vol}(C)\prod_{i=1}^M\lambda_i
 \le 2^M M!\det\Lambda.
 \tag{12.15}
\]

**Proof.** Write \(\|x\|_C=\inf\{t:x\in tC\}\). Choose independent lattice vectors \(v_i\in\lambda_i C\); the minima are attained because bounded sets contain only finitely many lattice points. The cross-polytope with vertices \(\pm v_i/\lambda_i\) lies in \(C\). Its volume is \(2^M|\det(v_1,\ldots,v_M)|/(M!\prod\lambda_i)\), and the determinant is a positive integer multiple of \(\det\Lambda\). This proves the lower bound.

For the upper bound choose a rational complete flag \(F_0\subset\cdots\subset F_M\) such that every lattice vector of gauge less than \(\lambda_i\) belongs to \(F_{i-1}\). Such a flag exists: for each distinct minimum, include the span of the strictly shorter vectors, then extend within the span of vectors at that minimum. Repeated minima form one block in this construction. Each subgroup \(\Lambda\cap F_i\) is saturated in \(\Lambda\). Successive extension of a basis of a saturated subgroup gives a lattice basis \(b_1,\ldots,b_M\) adapted to the flag. This elementary extension follows by the integer Euclidean algorithm: a primitive vector has coordinates with greatest common divisor one and can be made the first coordinate vector by integer row operations; apply the same argument in the free quotient.

For \(T>0\), define positive integers, backwards, by

\[
 q_M=\lfloor2T/\lambda_M\rfloor+1,\qquad
 q_i=q_{i+1}\left(\left\lfloor\frac{2T}{\lambda_iq_{i+1}}\right\rfloor+1\right).
\]

Then \(q_i>2T/\lambda_i\), \(q_{i+1}\mid q_i\), and

\[
 q_i\le 2T\sum_{j=i}^M\lambda_j^{-1}+1
       \le (M-i+1)(2T/\lambda_i+1).
\]

Reduction modulo \(\sum_iq_i\mathbb Zb_i\) is injective on \(\Lambda\cap TC\). Otherwise a nonzero difference \(z\) belongs to \(2TC\) and to this subgroup. If \(k\) is its largest nonzero basis index, divisibility of the \(q_i\) implies \(z/q_k\in\Lambda\setminus F_{k-1}\). But \(\|z/q_k\|_C\le2T/q_k<\lambda_k\), contradicting the flag property. Therefore

\[
 \#(\Lambda\cap TC)\le\prod_iq_i
             \le M!\prod_i(2T/\lambda_i+1).
\]

Finally \(\#(\Lambda\cap TC)/T^M\to\operatorname{vol}(C)/\det\Lambda\). To see this directly, tile space by a bounded fundamental parallelepiped of \(\Lambda\). All cells meeting \(TC\) lie in an outer enlargement of fixed thickness, and all cells lying in \(TC\) cover its inner enlargement. Since \(C\) contains a ball, these enlargements are contained in \((T+A)C\) and contain \((T-A)C\), respectively, for one fixed \(A\). Their volumes divided by \(T^M\) have the same limit. Divide the preceding count by \(T^M\) and take the limit to obtain the upper bound. \(\square\)

### Lemma 12.5. The number-field version needed for the boxes

Suppose an adelic body \(\Pi\) has convex symmetric archimedean factors, complex-balanced at complex places, and full \(\mathcal O_v\)-lattices at finite places, equal to \(\mathcal O_v^N\) almost everywhere. Let \(\lambda_i\) be the least archimedean dilation giving \(i\) linearly independent \(K\)-vectors. Finite factors are held fixed during this dilation. Then

\[
               \operatorname{vol}(\Pi)\prod_{i=1}^N\lambda_i^d
                           \asymp_{K,N}1.
               \tag{12.16}
\]

**Proof.** The simultaneous finite conditions cut out a full \(\mathcal O_K\)-lattice \(\Lambda\subset K^N\). Its Minkowski embedding has covolume

\[
 \det j(\Lambda)
     =\left(2^{-r_2}\sqrt{|\operatorname{disc}K|}\right)^N
          \left(\prod_{v\nmid\infty}\operatorname{vol}\Pi_v\right)^{-1}.
 \tag{12.17}
\]

For an integral sublattice this follows from its finite index: the index is the product of the local indices, while covolume is multiplied by that index. Clearing a common denominator gives the same identity for a fractional lattice. The number-field foundations are Norms of ideals, the ideal class group, and modules over Dedekind domains, Proposition 4.1 and Theorem 4.3, and Lattices, Minkowski's theorem and the Minkowski embedding, Proposition 7.2. They provide the module structure, local ideal indices and covolume, for every number field; they do not provide the successive-minima estimate, which we prove here.

Let \(\nu_1,\ldots,\nu_{dN}\) be the ordinary real successive minima of \(j(\Lambda)\) in the archimedean body. Choose an integral basis \(\beta_1,\ldots,\beta_d\) and put \(B=\max(1,|\sigma(\beta_j)|)\), over all embeddings and indices. Multiplication by \(\beta_j\) preserves the finite lattices. At an infinite place it takes the local body into its \(B\)-dilate; this uses symmetry and convexity over \(\mathbb R\), and complex balance over \(\mathbb C\). Thus

\[
 \lambda_i\le\nu_{d(i-1)+1}\le\nu_{di}\le B\lambda_i.
\]

For the first inequality, \(d(i-1)+1\) rationally independent vectors must have \(K\)-rank at least \(i\). For the last, multiply \(i\) independent \(K\)-vectors by the integral basis: the resulting \(di\) vectors are rationally independent. It follows that

\[
 \prod_i\lambda_i^d\le\prod_j\nu_j\le B^{dN}\prod_i\lambda_i^d.
\]

Apply (12.15) in real dimension \(dN\) and then use (12.17). This proves (12.16). \(\square\)

For (12.13), a negative sum \(\sum c_{v,i}\le-\rho<0\) consequently implies \(\lambda_N\gg Q^{\rho/N}\). In particular the \(K\)-span of the vectors in \(\Pi(Q)\) has dimension at most \(N-1\) for large \(Q\). This is the geometric input in the Subspace theorem proof; sharp constants in Minkowski's second theorem are unnecessary.

## 6. The algebraic-point index bound

Lesson 11 bounded the index of an integer polynomial at a rational point. Approximation at several places of a number field leads to algebraic points instead, still with rapidly decreasing weights. The induction of Lesson 11 carries over; only the one-variable step changes, because an algebraic root costs its whole minimal polynomial. We write \(\operatorname{ind}_{\boldsymbol\beta,\boldsymbol r}\) for the index (10.6) of The index method for rational approximation and use its rules from Lemma 10.4: a derivative of weighted order \(w\) lowers the index by at most \(w\), the index of a product is the sum of the indices, and the index of a sum is at least the smaller of the two.

### Lemma 12.6. Roth's index lemma at algebraic points

Fix positive integers \(r_1,\ldots,r_m\) and a nonzero \(P\in\mathbb Z[T_1,\ldots,T_m]\) with \(\deg_{T_i}P\le r_i\). Let \(h(P)\) be the logarithm of the largest absolute value of a coefficient of \(P\). Let \(\beta_1,\ldots,\beta_m\) be algebraic numbers, let \(0<\eta\le1/2\), and put \(t=\eta^{2^{m-1}}\). If

\[
 \frac{r_{i+1}}{r_i}\le t\quad(1\le i<m)
 \qquad\text{and}\qquad
 t\,r_i\,h(\beta_i)\ge h(P)+6mr_1\quad(1\le i\le m),
 \tag{12.18}
\]

then \(\operatorname{ind}_{\boldsymbol\beta,\boldsymbol r}P\le2m\eta\).

**Proof.** The second condition in (12.18) forces every \(h(\beta_i)\) to be positive. We first record what one algebraic root costs. Let \(U\in\mathbb Z[T]\) be nonzero of degree at most \(e\), and let \(\beta\) be a root of \(U\) of multiplicity \(\ell\). The primitive irreducible polynomial \(f\in\mathbb Z[T]\) of \(\beta\) divides \(U\) to the power \(\ell\), as shown after Lemma 10.4, and by Gauss's lemma the cofactor has integer coefficients. Mahler measure is multiplicative and at least one on nonzero integer polynomials, so \(M(f)^\ell\le M(U)\). In Heights of algebraic numbers, Theorem 2.4 gives \(\log M(f)=\deg(\beta)\,h(\beta)\ge h(\beta)\) and Proposition 2.2 gives \(M(U)\le\sqrt{e+1}\,H(U)\). Since \(\tfrac12\log(e+1)\le e\),

\[
 \ell\,h(\beta)\le h(U)+e .
\]

For \(m=1\) this is the whole proof: take \(U=P\), \(e=r_1\) and \(\ell=r_1\operatorname{ind}P\); then (12.18) gives \(\operatorname{ind}P\le(h(P)+r_1)/(r_1h(\beta_1))\le t=\eta\).

Now let \(m\ge2\), and assume the lemma in \(m-1\) variables for every admissible \(\eta\). As \(\eta\le1/2\), we have \(t\le1/4\); hence \(r_i\le t^{\,i-1}r_1\), \(\sum_ir_i\le\tfrac43r_1\) and \(r_m\le\tfrac14r_1\).

*The separating determinant.* Section 2 of Wronskians and Roth's rational-point lemma writes \(P=\sum_{j=1}^kA_j(\boldsymbol T')B_j(T_m)\), with \(\boldsymbol T'=(T_1,\ldots,T_{m-1})\) and least length \(k\le r_m+1\). It chooses derivative rows \(D_{\boldsymbol i_\ell}\) in \(\boldsymbol T'\) with \(|\boldsymbol i_\ell|\le\ell-1\), and shows in (11.3)–(11.4) that

\[
 W=\det\bigl(D_{\boldsymbol i_\ell}D_{j-1,T_m}P\bigr)_{\ell,j=1}^k=c\,U_0(\boldsymbol T')\,V_0(T_m),
\]

where \(c\) is a nonzero integer, \(U_0\) and \(V_0\) are primitive integer polynomials, \(\deg_{T_i}U_0\le kr_i\) for \(i<m\), \(\deg V_0\le kr_m\), and \(H(U_0),H(V_0)\le H(W)\).

*Its height.* Every entry of \(W\) is a divided derivative of \(P\). By Lemma 10.3 its coefficients are at most \(2^{\sum r_i}H(P)\), and it has at most \(\prod_i(r_i+1)\le2^{\sum r_i}\) monomials. A coefficient of a product \(FG\) is a sum of at most as many products of coefficients as \(F\) has monomials. Hence each of the \(k!\) terms of the determinant has coefficients at most \(2^{(2k-1)\sum r_i}H(P)^k\), and

\[
 h(U_0),\,h(V_0)\le h(W)\le k\,h(P)+(2k-1)\Bigl(\sum_ir_i\Bigr)\log2+\log k!\le k\bigl(h(P)+3r_1\bigr).
 \tag{12.19}
\]

The last step uses \((2k-1)\cdot\tfrac43r_1\log2<2kr_1\) and \(\log k!\le k(k-1)\le kr_m\le\tfrac14kr_1\).

*The index of \(W\) from above.* The factor \(V_0\) is a polynomial in \(T_m\) of degree at most \(kr_m\). By the one-root estimate and (12.19), its multiplicity \(\ell_0\) at \(\beta_m\) satisfies \(\ell_0\,h(\beta_m)\le k(h(P)+3r_1)+kr_m\le k(h(P)+6mr_1)\). With the weight \(r_m\) its index is \(\ell_0/r_m\), so (12.18) gives

\[
 \operatorname{ind}_{\beta_m,r_m}V_0\le\frac{k\,(h(P)+6mr_1)}{r_m\,h(\beta_m)}\le kt .
\]

The factor \(U_0\) has degree at most \(kr_i\) in \(T_i\). We apply the lemma in \(m-1\) variables to it, with the weights \(kr_1,\ldots,kr_{m-1}\) and with \(\eta^2\) in place of \(\eta\). Then \((\eta^2)^{2^{m-2}}=t\), the ratio condition is unchanged, and (12.19) gives

\[
 h(U_0)+6(m-1)\,kr_1\le k\bigl(h(P)+6mr_1\bigr)\le t\,(kr_i)\,h(\beta_i)\qquad(i<m).
\]

So \(U_0\) has index at most \(2(m-1)\eta^2\) for the weights \(kr_i\), and hence at most \(2k(m-1)\eta^2\) for the weights \(r_i\). A polynomial in \(\boldsymbol T'\) alone has the same index at \(\boldsymbol\beta\) as at \((\beta_1,\ldots,\beta_{m-1})\), and likewise for \(T_m\). By the product rule,

\[
 \operatorname{ind}_{\boldsymbol\beta,\boldsymbol r}W\le2k(m-1)\eta^2+kt .
\]

*The index of \(W\) from below.* Put \(u=\operatorname{ind}_{\boldsymbol\beta,\boldsymbol r}P\). Then \(u\le m\), because every Taylor coefficient of \(P\) at \(\boldsymbol\beta\) has weighted order at most \(\sum_ir_i/r_i\). By (11.5) and \(|\boldsymbol i_\ell|\le k-1\le r_m\), the entry of \(W\) in column \(j+1\) has index at least \(\max\{0,u-j/r_m\}-r_m/r_{m-1}\ge\max\{0,u-j/r_m\}-t\). Each term of the determinant takes one entry from every column, so the product and sum rules give

\[
 \operatorname{ind}_{\boldsymbol\beta,\boldsymbol r}W\ge\sum_{j=0}^{k-1}\max\{0,\,u-j/r_m\}-kt .
 \tag{12.20}
\]

Let \(\nu\ge1\) be the number of \(j\in\{0,\ldots,k-1\}\) with \(j\le r_mu\). These terms sum to \(\nu u-\nu(\nu-1)/(2r_m)\ge\nu u/2\), since \(\nu-1\le r_mu\). If \(\nu=k\), the sum is at least \(ku/2\ge ku^2/(2m)\). If \(\nu<k\), then \(\nu>r_mu\), so the sum is at least \(r_mu^2/2\); moreover \(k\ge2\) gives \(k\le r_m+1\le2r_m\), and the sum is again at least \(ku^2/4\ge ku^2/(2m)\).

Comparing the two bounds for the index of \(W\),

\[
 \frac{ku^2}{2m}\le2kt+2k(m-1)\eta^2\le2km\eta^2,
\]

because \(t\le\eta^2\). Hence \(u\le2m\eta\). \(\square\)

The squaring of \(\eta\) at each step is the source of the exponent \(2^{m-1}\): the factor in \(m-1\) variables is treated with the parameter \(\eta^2\), and its own ratio condition must again read \(t\).

### Corollary 12.7. Index along hyperplanes

Let \(N=n+1\ge2\). Let \(P\ne0\) be a polynomial with integer coefficients in \(m\) blocks \(\boldsymbol X_1,\ldots,\boldsymbol X_m\) of \(N\) variables, homogeneous in each block, of degree at most \(d_j\) in block \(j\). For each \(j\) let \(M_j(\boldsymbol X_j)=\sum_{i=0}^nb_{j,i}X_{j,i}\) be a nonzero linear form with algebraic coefficients. The *index of \(P\) along \(M_1,\ldots,M_m\)*, with the weights \(d_j\), is the largest \(\tau\) such that \(P\) lies in the ideal generated by the products \(\prod_jM_j^{a_j}\) with \(\sum_ja_j/d_j\ge\tau\). If \(0<\sigma\le1/2\), \(d_{j+1}/d_j\le\sigma\), and

\[
 d_j\,h([M_j])\ge n\sigma^{-1}\bigl(h(P)+6md_1\bigr)\qquad(1\le j\le m),
 \tag{12.21}
\]

then this index is at most \(2m\sigma^{1/2^{m-1}}\).

**Proof.** Choose, in every block, coordinates in which \(M_j\) is the first coordinate \(Z_{j,0}\). The ideals in the definition are then generated by monomials in the \(Z_{j,0}\), and the index is the least value of \(\sum_ja_j/d_j\) over the monomials of \(P\), where \(a_j\) is the exponent of \(Z_{j,0}\). Three consequences are used below. The index is additive on products, since lowest-order parts multiply without cancellation in a polynomial ring. A coordinate \(X_{j,i}\) that is not proportional to \(M_j\) has index zero. A ring homomorphism sending each \(M_j\) to a nonzero form \(M_j'\) maps each of the ideals for \(M_1,\ldots,M_m\) into the corresponding ideal for \(M_1',\ldots,M_m'\), so it cannot lower the index.

*Two coordinates per block.* Fix \(j\) and a nonzero coefficient \(b_{j,i_0}\). After scaling so that \(b_{j,i_0}=1\),

\[
 h([M_j])=\sum_v\log\max_i|b_{j,i}|_v\le\sum_{i\ne i_0}\sum_v\log\max(1,|b_{j,i}|_v)=\sum_{i\ne i_0}h([b_{j,i_0}:b_{j,i}]).
\]

So some \(i_1\ne i_0\) has \(h([b_{j,i_0}:b_{j,i_1}])\ge h([M_j])/n\). This height is positive by (12.21), so \(b_{j,i_1}\ne0\).

*Removing the other coordinates.* Let \(X\) be a coordinate of block \(j\) other than \(X_{j,i_0}\) and \(X_{j,i_1}\). Write \(P=X^eP_1\) with \(X\nmid P_1\), and let \(P_2\) be \(P_1\) with \(X\) set to zero. Then \(P_2\ne0\); it is homogeneous in each block of degree at most \(d_j\), and \(h(P_2)\le h(P_1)=h(P)\), because its coefficients are among those of \(P\). The index of \(P\) along the \(M_j\) equals that of \(P_1\), since \(X\) is not proportional to \(M_j\) (the coefficients \(b_{j,i_0}\) and \(b_{j,i_1}\) are nonzero). Setting \(X=0\) replaces \(M_j\) by the form with that coefficient deleted, so the index of \(P_2\) along the new forms is at least that of \(P_1\). Repeating this in every block, we reach a nonzero polynomial \(P^*\) in the pairs \((X_{j,i_0},X_{j,i_1})\) with \(h(P^*)\le h(P)\), whose index along the forms \(M_j^*=b_{j,i_0}X_{j,i_0}+b_{j,i_1}X_{j,i_1}\), with the same weights \(d_j\), is at least the index of \(P\).

*Dehomogenizing.* Set \(X_{j,i_0}=1\) and write \(T_j=X_{j,i_1}\). The result \(Q(T_1,\ldots,T_m)\in\mathbb Z[T_1,\ldots,T_m]\) is nonzero, with \(\deg_{T_j}Q\le d_j\) and \(h(Q)=h(P^*)\). Put \(\beta_j=-b_{j,i_0}/b_{j,i_1}\), so that \(M_j^*(1,T_j)=b_{j,i_1}(T_j-\beta_j)\). Expand \(P^*\) in the coordinates \(M_j^*,X_{j,i_0}\) of each block and then set \(X_{j,i_0}=1\). This gives the Taylor expansion of \(Q\) at \(\boldsymbol\beta=(\beta_j)\), with nonzero coefficients at exactly the same exponents. So the index of \(Q\) at \(\boldsymbol\beta\) with weights \(d_j\) equals the index of \(P^*\) along the \(M_j^*\). Also \(h(\beta_j)=h([b_{j,i_0}:b_{j,i_1}])\ge h([M_j])/n\).

*Applying Lemma 12.6.* Let \(\eta=\sigma^{1/2^{m-1}}\). If \(\eta>1/2\), the asserted bound \(2m\eta\) exceeds \(m\), which bounds the index of \(P\) because every monomial has \(\sum_ja_j/d_j\le m\). Otherwise \(\eta^{2^{m-1}}=\sigma\), the ratio condition of (12.18) holds, and by (12.21)

\[
 \sigma\,d_j\,h(\beta_j)\ge\sigma\,d_j\,h([M_j])/n\ge h(P)+6md_1\ge h(Q)+6md_1 .
\]

Lemma 12.6 bounds the index of \(Q\) at \(\boldsymbol\beta\) by \(2m\eta\), and the index of \(P\) is no larger. \(\square\)

## 7. Auxiliary polynomials on products of boxes

From here until the end of the proof of Theorem 12.13 for coefficients in \(K\), the forms \(L_{v,i}\) of (12.13) have coefficients in \(K\), the set \(S\) contains all infinite places, and \(N=n+1\ge2\). For \(Q\ge1\) we write \(\Pi(Q)\cap K^N\) for the set of \(x\in K^N\) that satisfy the local condition (12.13) at every place, and \(U(Q)\) for the \(K\)-span of this set. The goal of this section is Proposition 12.11: the spaces \(U(Q)\) of dimension \(N-1\) form a finite set. The method is Schmidt's. A polynomial in \(m\) blocks of variables whose monomials are balanced with respect to every \(L_v\) is small at points taken from \(m\) such hyperplanes of very different heights; but a nonzero \(S\)-integer cannot be small at every place of \(S\), and Corollary 12.7 prevents the polynomial from vanishing to high order on those hyperplanes. Goel, Lunia and Ray give a detailed modern account of this approach.

For \(v\in S\) and a block \(\boldsymbol X_j\) of \(N\) variables, the forms \(Y_{j,i}=L_{v,i}(\boldsymbol X_j)\), \(1\le i\le N\), are again coordinates. Every polynomial in \(\boldsymbol X_1,\ldots,\boldsymbol X_m\) can therefore be written as a polynomial in the \(Y_{j,i}\); we call its coefficients and its exponent vectors \(J=(J_{j,i})\) the \(L_v\)-coefficients and \(L_v\)-exponents. The affine height of finitely many elements \(a_1,\ldots,a_s\) of \(K\) is

\[
 h_{\mathrm{aff}}(a_1,\ldots,a_s)=\sum_v\log\max(1,|a_1|_v,\ldots,|a_s|_v),
\]

the sum running over all places of \(K\) with the normalization (12.11).

### Lemma 12.8. A polynomial with balanced exponents

Let \(0<\eta<1/(4N)\), and let \(m\) be a positive integer with

\[
 e^{-2\eta^2m}<\frac1{4dN|S|},\qquad d=[K:\mathbb Q].
 \tag{12.22}
\]

There is a constant \(C\), depending on \(K\), \(S\), the forms, \(m\) and \(\eta\), with the following property. For all positive integers \(d_1,\ldots,d_m\) there is a nonzero polynomial \(P\in\mathbb Z[\boldsymbol X_1,\ldots,\boldsymbol X_m]\), homogeneous of degree \(d_j\) in block \(j\), with \(h(P)\le C\sum_jd_j\), such that every divided derivative \(T=D_{\boldsymbol I}P\) of weighted order \(\sum_j|\boldsymbol I_j|/d_j\le m\eta\) has two properties at each \(v\in S\). First, every \(L_v\)-exponent \(J\) of \(T\) with nonzero \(L_v\)-coefficient satisfies

\[
 \frac mN-2m\eta<\sum_{j=1}^m\frac{J_{j,i}}{d_j}<\frac mN+2m(N-1)\eta\qquad(1\le i\le N).
 \tag{12.23}
\]

Second, the family of all \(L_v\)-coefficients of \(T\) has affine height at most \(C\sum_jd_j\). Here \(|\boldsymbol I_j|\) is the total order of \(\boldsymbol I\) in block \(j\).

**Proof.** *Conditions.* The unknowns are the \(V=\prod_j\binom{d_j+n}{n}\) rational coefficients \(p_{\boldsymbol a}\) of a polynomial homogeneous of degree \(d_j\) in block \(j\). Its \(L_v\)-exponents run through the same number of tuples \(J=(J_1,\ldots,J_m)\) with \(J_j\in\mathbb Z_{\ge0}^N\) and \(|J_j|=d_j\). Call such a \(J\) *low in \(i\)* if \(\sum_jJ_{j,i}/d_j\le m/N-m\eta\). We impose that the \(L_v\)-coefficient of \(P\) vanishes at every \(J\) that is low in some \(i\), for every \(v\in S\).

To count these conditions, pick \(J\) uniformly at random. Its blocks are independent, each uniformly distributed on \(\{J_j:|J_j|=d_j\}\). For fixed \(i\) the variable \(Z_j=J_{j,i}/d_j\) lies in \([0,1]\), and its mean is \(1/N\): permuting the \(N\) coordinates preserves the set \(\{|J_j|=d_j\}\), so the coordinates have equal means, and these add up to one. We show below that

\[
 \Pr\Bigl(\sum_{j=1}^mZ_j\le\frac mN-m\eta\Bigr)\le e^{-2m\eta^2}.
\]

Hence at most \(e^{-2m\eta^2}V\) exponents are low in a given \(i\), and the number of imposed \(K\)-linear conditions satisfies \(M\le N|S|e^{-2m\eta^2}V<V/(4d)\), by (12.22).

The probability bound is Hoeffding's inequality. Let \(Z_1,\ldots,Z_m\) be independent with values in \([0,1]\) and means \(p_j\), and let \(s>0\). Convexity gives \(e^{-sz}\le1-z+ze^{-s}\) on \([0,1]\), so \(\mathbb E\,e^{-s(Z_j-p_j)}\le e^{\varphi_j(s)}\), where \(\varphi_j(s)=sp_j+\log(1-p_j+p_je^{-s})\). Here \(\varphi_j(0)=\varphi_j'(0)=0\), and \(\varphi_j''=q(1-q)\le1/4\) with \(q=p_je^{-s}/(1-p_j+p_je^{-s})\in[0,1]\); thus \(\varphi_j(s)\le s^2/8\). By independence and Markov's inequality,

\[
 \Pr\Bigl(\sum_j(Z_j-p_j)\le-m\eta\Bigr)\le e^{-sm\eta}\,\mathbb E\,e^{-s\sum_j(Z_j-p_j)}\le e^{-sm\eta+ms^2/8},
\]

and \(s=4\eta\) gives \(e^{-2m\eta^2}\).

*Integer equations.* For \(v\in S\) let \(B_v\) be the inverse of the matrix with rows \(L_{v,1},\ldots,L_{v,N}\), so that \(\boldsymbol X_j=B_vY_j\), and choose a positive integer \(D_v\) such that \(D_vB_v\) has entries in \(\mathcal O_K\). The \(L_v\)-coefficient of \(P\) at \(J\) is \(\sum_{\boldsymbol a}p_{\boldsymbol a}\gamma_{v,\boldsymbol a,J}\), where \(\gamma_{v,\boldsymbol a,J}\) is the coefficient of \(Y^J\) in \(\prod_j(B_vY_j)^{\boldsymbol a_j}\). This is a sum of products of \(\sum_jd_j\) entries of \(B_v\) with nonnegative integer coefficients. Hence \(D_v^{\sum d_j}\gamma_{v,\boldsymbol a,J}\) is an algebraic integer. At every complex embedding \(\sigma\) of \(K\), its image has absolute value at most \((N\max|\sigma(D_vB_v)|)^{\sum d_j}\), the maximum over the entries. Algebraic integers of \(K\) have coordinates in a fixed integral basis bounded by \(C_K\) times their largest conjugate; \(C_K\) comes from inverting the matrix of conjugates of the basis. So each condition, multiplied by \(D_v^{\sum d_j}\), splits into \(d\) linear equations with integer coefficients of absolute value at most \(A=C_Kc^{\sum d_j}\), where \(c\ge1\) depends only on the forms. Altogether there are \(R\le dM<V/4\) integer equations in \(V\) unknowns.

*Siegel's lemma.* Lemma 10.5 supplies a nonzero integer solution with \(\max|p_{\boldsymbol a}|\le(VA)^{R/(V-R)}\le(VA)^{1/3}\). A coordinate vector serves if \(R=0\). Since \(\binom{d_j+n}n\le2^{d_j+n}\), we have \(\log V\le N\sum_jd_j\). Therefore \(h(P)\le\tfrac13\bigl(N\sum_jd_j+\log C_K+\log c\sum_jd_j\bigr)\le C\sum_jd_j\).

*The window (12.23).* Let \(T=D_{\boldsymbol I}P\) with \(\sum_j|\boldsymbol I_j|/d_j\le m\eta\), and fix \(v\). In block \(j\), a derivative in the \(\boldsymbol X\)-coordinates is a combination with constant coefficients of derivatives in the \(Y\)-coordinates of the same order. So \(T\) is a combination of \(Y\)-derivatives of \(P\) whose order in block \(j\) is \(|\boldsymbol I_j|\). Such a derivative sends \(Y^{J'}\) to a multiple of \(Y^{J'-I'}\), with \(|I'_j|=|\boldsymbol I_j|\). Every \(L_v\)-exponent \(J\) of \(T\) with nonzero coefficient is therefore of this form, with \(J'\) an \(L_v\)-exponent of \(P\) with nonzero coefficient. As \(J'\) is not low in \(i\),

\[
 \sum_j\frac{J_{j,i}}{d_j}\ge\sum_j\frac{J'_{j,i}}{d_j}-\sum_j\frac{|\boldsymbol I_j|}{d_j}>\Bigl(\frac mN-m\eta\Bigr)-m\eta .
\]

For the upper bound, \(\sum_{i=1}^N\sum_jJ_{j,i}/d_j=\sum_j(d_j-|\boldsymbol I_j|)/d_j\le m\). Subtracting the lower bounds for the \(N-1\) indices other than \(i\) leaves less than \(m-(N-1)(m/N-2m\eta)=m/N+2m(N-1)\eta\).

*Heights of the \(L_v\)-coefficients.* By Lemma 10.3, \(T\) has integer coefficients \(\tau_{\boldsymbol b}\) of absolute value at most \(2^{\sum d_j}e^{h(P)}\), at most \(V\) of them. Its \(L_v\)-coefficient at \(J\) is \(\sum_{\boldsymbol b}\tau_{\boldsymbol b}\gamma_{v,\boldsymbol b,J}\). At a finite place \(w\), the ultrametric inequality bounds it by \(\max(1,\max|B_v|_w)^{\sum d_j}\), which equals one for all but finitely many \(w\). At an infinite place it is at most \(V2^{\sum d_j}e^{h(P)}(N\max|\sigma(B_v)|)^{\sum d_j}\) in absolute value. Summing logarithms with the normalization (12.11) gives an affine height of at most \(C\sum_jd_j\), after enlarging \(C\). \(\square\)

### Lemma 12.9. Height of a varying hyperplane

Suppose \(\sum_{v\in S}\sum_ic_{v,i}\le-\rho<0\). There are a finite set \(\mathcal E\) of hyperplanes of \(K^N\) and a constant \(C\), both independent of \(Q\), such that whenever \(\dim U(Q)=N-1\), either \(U(Q)\in\mathcal E\) or

\[
 h(U(Q))\ge\frac{\rho}{2|S|}\log Q-C .
 \tag{12.24}
\]

The height of a hyperplane is the projective height of a nonzero linear form vanishing on it.

**Proof.** Suppose \(\dim U(Q)=N-1\), and choose a basis \(y_1,\ldots,y_{N-1}\) of \(U(Q)\) in \(\Pi(Q)\cap K^N\). The linear form \(w(x)=\det(y_1,\ldots,y_{N-1},x)\) vanishes exactly on \(U(Q)\). Its coefficients are minors of a matrix with entries in \(\mathcal O_{K,S}\), so they lie in \(\mathcal O_{K,S}\). For \(v\in S\) let \(G_v\) be the matrix with rows \(L_{v,1},\ldots,L_{v,N}\). Then \(\det(G_v)\,w(x)=\det(G_vy_1,\ldots,G_vy_{N-1},G_vx)\), and expansion along the last column gives

\[
 \det(G_v)\,w=\sum_{i=1}^N(-1)^{N+i}\,\lambda_{v,i}(w)\,L_{v,i},
\]

where \(\lambda_{v,i}(w)\) is the minor of \((L_{v,k}(y_l))_{k,l}\) with row \(i\) removed. Read as coordinates of \(w\) in the basis \(L_{v,1},\ldots,L_{v,N}\) of the dual space, each \(\lambda_{v,i}\) is a fixed \(K\)-linear function of \(w\), independent of \(Q\). Expanding the minor into \((N-1)!\) products of values \(|L_{v,k}(y_l)|_v\le Q^{c_{v,k}}\) gives

\[
 |\lambda_{v,i}(w)|_v\le\kappa_v\,Q^{s_v-c_{v,i}},\qquad s_v=\sum_kc_{v,k},
\]

where \(\kappa_v\) is \(((N-1)!)^{d_v/d}\) for infinite \(v\) and \(1\) for finite \(v\). For each \(v\) the \(\lambda_{v,i}(w)\) determine \(w\), so they are not all zero. Let \(I_v(w)=\{i:\lambda_{v,i}(w)\ne0\}\), and call \((I_v(w))_{v\in S}\) the pattern of \(w\).

*Case 1: some choice of \(i_v\in I_v(w)\) has \(\sum_vc_{v,i_v}\ge-\rho/2\).* Multiplying the bounds gives

\[
 \prod_{v\in S}|\lambda_{v,i_v}(w)|_v\le\kappa\,Q^{\sum_vs_v-\sum_vc_{v,i_v}}\le\kappa\,Q^{-\rho/2},\qquad\kappa=\prod_v\kappa_v .
\]

For a lower bound, choose a nonzero coordinate \(w_k\) and put \(w'=w/w_k\). One coordinate of \(w'\) equals one, so its affine height equals \(h([w])=h(U(Q))\). The numbers \(\alpha_v=\lambda_{v,i_v}(w')\) are nonzero, and \(h(\alpha_v)\le h([w])+C_1\), with \(C_1\) depending only on the forms. Indeed, if \(\ell_1,\ldots,\ell_N\) are the coefficients of \(\lambda_{v,i_v}\), then \(|\alpha_v|_u\le N^{\epsilon_u}\max_k|\ell_k|_u\max_k|w'_k|_u\) at every place \(u\), where \(\epsilon_u=d_u/d\) at infinite places and \(\epsilon_u=0\) at finite places; take \(\log\max(1,\cdot)\) and sum over \(u\). A nonzero \(\alpha\in K\) satisfies \(|\alpha|_v\ge\prod_u\min(1,|\alpha|_u)=H(\alpha)^{-1}\) at every place \(v\), by the product formula. Moreover \(\prod_{v\in S}|w_k|_v\ge1\), because \(w_k\) is a nonzero \(S\)-integer. Hence

\[
 \prod_{v\in S}|\lambda_{v,i_v}(w)|_v=\prod_{v\in S}|w_k|_v\prod_{v\in S}|\alpha_v|_v\ge e^{-|S|(h([w])+C_1)} .
\]

Comparing the two bounds proves (12.24) with \(C=C_1+|S|^{-1}\log\kappa\).

*Case 2: every choice has \(\sum_vc_{v,i_v}<-\rho/2\).* Equivalently, \(\sum_v\max_{i\in I_v(w)}c_{v,i}<-\rho/2\), which depends only on the pattern. There are finitely many patterns. For each pattern \(I=(I_v)\) of this kind that occurs for some \(Q\), fix once and for all a nonzero linear form \(w_I\) with \(\lambda_{v,i}(w_I)=0\) for all \(v\) and all \(i\notin I_v\); the form \(w\) of one occurrence is such a form. For any \(Q\) and any \(x\in\Pi(Q)\cap K^N\), the expansion of \(\det(G_v)w_I(x)\) involves only \(i\in I_v\), so

\[
 |w_I(x)|_v\le\kappa_{v,I}\,Q^{\max_{i\in I_v}c_{v,i}}\quad(v\in S),\qquad |w_I(x)|_u\le\|w_I\|_u\quad(u\notin S),
\]

and \(\|w_I\|_u=1\) for all but finitely many \(u\). If \(w_I(x)\ne0\), the product formula gives \(1\le\kappa_IQ^{\sum_v\max_{i\in I_v}c_{v,i}}<\kappa_IQ^{-\rho/2}\), which fails for \(Q>Q_I=\kappa_I^{2/\rho}\). So for \(Q>Q_I\) every vector of \(\Pi(Q)\cap K^N\) lies in \(\ker w_I\). If such a \(U(Q)\) has dimension \(N-1\) and pattern \(I\), it equals \(\ker w_I\).

Finally let \(Q_0\ge1\) be at least every \(Q_I\). For \(1\le Q\le Q_0\), all vectors of \(\Pi(Q)\cap K^N\) have coordinates in \(\mathcal O_{K,S}\), with absolute values bounded at the places of \(S\) independently of \(Q\). Their heights are therefore bounded, and Northcott's Theorem 2.6 leaves only finitely many such vectors, hence finitely many spaces \(U(Q)\). Let \(\mathcal E\) consist of these spaces and the hyperplanes \(\ker w_I\). \(\square\)

### Lemma 12.10. A grid detects a nonzero polynomial

Suppose \(F\ne0\) is a polynomial in \(Z_1,\ldots,Z_s\) over a field of characteristic zero, with \(\deg_{Z_i}F\le e_i\), and \(B>0\) is real. There are integers \(z_i\) with \(|z_i|\le B\) and integers \(0\le a_i\le e_i/B\) such that \(\bigl(\partial_{Z_1}^{a_1}\cdots\partial_{Z_s}^{a_s}F\bigr)(z_1,\ldots,z_s)\ne0\).

**Proof.** For \(s=1\), the interval \([-B,B]\) contains \(2\lfloor B\rfloor+1>B\) integers. If each of them were a root of multiplicity at least \(\lfloor e_1/B\rfloor+1>e_1/B\), \(F\) would have more than \(e_1\) roots counted with multiplicity, which is impossible. So some integer \(z\) in the interval is a root of multiplicity \(a\le e_1/B\), with \(a=0\) if it is not a root, and \(F^{(a)}(z)\ne0\).

For \(s\ge2\), write \(F=\sum_kF_k(Z_1,\ldots,Z_{s-1})Z_s^k\) and choose \(k\) with \(F_k\ne0\). By induction there are \(z_1,\ldots,z_{s-1}\) and \(a_1,\ldots,a_{s-1}\) as required for \(F_k\). The one-variable polynomial \(g(Z_s)=(\partial^{a_1}_{Z_1}\cdots\partial^{a_{s-1}}_{Z_{s-1}}F)(z_1,\ldots,z_{s-1},Z_s)\) has nonzero coefficient at \(Z_s^k\) and degree at most \(e_s\). The case \(s=1\) supplies \(z_s\) and \(a_s\). \(\square\)

### Proposition 12.11. Boxes of codimension one have finitely many spans

Fix \(K\), \(S\), the forms \(L_{v,i}\) and exponents \(c_{v,i}\) with \(\sum_{v,i}c_{v,i}\le-\rho<0\). Then only finitely many hyperplanes occur among the spaces \(U(Q)\), \(Q\ge1\).

**Proof.** Suppose they form an infinite set. By the proof of Lemma 12.9, bounded \(Q\) produce only finitely many spaces, so hyperplanes \(U(Q)\) outside the finite set \(\mathcal E\) of that lemma occur for arbitrarily large \(Q\); they satisfy (12.24). Choose, in this order:

1. \(\eta\) with \(0<\eta<1/(4N)\) and \(2N\eta\sum_{v,i}|c_{v,i}|<\rho/(4N)\);
2. \(m\) satisfying (12.22), and then \(\sigma=(\eta/4)^{2^{m-1}}\) and \(B=2(N-1)/\eta\);
3. \(Q_1\), large in terms of everything chosen so far, with \(U_1=U(Q_1)\) a hyperplane outside \(\mathcal E\); then \(Q_2,\ldots,Q_m\) with \(\log Q_{j+1}\ge2\sigma^{-1}\log Q_j\) and hyperplanes \(U_j=U(Q_j)\) outside \(\mathcal E\);
4. \(D\), large in terms of everything chosen so far, and \(d_j=\lfloor D/\log Q_j\rfloor\).

Then each \(d_j\ge1\), \(d_{j+1}/d_j\le\sigma\), \(D-\log Q_j<d_j\log Q_j\le D\), and \(\sum_jd_j\le mD/\log Q_1\). Let \(P\) be the polynomial of Lemma 12.8 for these degrees, with its constant \(C\), and let \(w_j\) be a nonzero linear form vanishing on \(U_j\).

*A derivative that survives on the product of hyperplanes.* By (12.24), \(d_j\,h([w_j])\ge\frac{\rho}{2|S|}(D-\log Q_m)-C_2D/\log Q_1\), with \(C_2\) the constant of (12.24). On the other hand \(n\sigma^{-1}(h(P)+6md_1)\le n\sigma^{-1}m(C+6)D/\log Q_1\). With \(Q_1\) and then \(D\) large, the first quantity exceeds \(\rho D/(4|S|)\) and the second is below it, so (12.21) holds. By Corollary 12.7, the index of \(P\) along \(w_1,\ldots,w_m\) is at most \(2m\sigma^{1/2^{m-1}}=m\eta/2\). In each block take coordinates consisting of \(w_j\) and \(n\) further linear forms, and pick a monomial of \(P\) whose exponents \(a_j\) of the \(w_j\) satisfy \(\sum_ja_j/d_j\le m\eta/2\). Differentiate \(a_j\) times with respect to the coordinate \(w_j\) in every block, and restrict to \(U_1\times\cdots\times U_m\). Monomials with a smaller exponent in some block are annihilated, and those with a larger exponent in some block vanish on the product. The monomials with exactly these exponents survive with the factor \(\prod_ja_j!\), so the restriction is nonzero. Each derivative with respect to \(w_j\) is a combination with constant coefficients of the derivatives \(\partial/\partial X_{j,k}\). Hence some divided derivative \(D_{\boldsymbol I_0}P\) with \(|\boldsymbol I_{0,j}|=a_j\) has nonzero restriction to \(U_1\times\cdots\times U_m\).

*An integral point of nonvanishing.* Let \(y_{j,1},\ldots,y_{j,n}\) be a basis of \(U_j\) in \(\Pi(Q_j)\cap K^N\). The polynomial \(G(\boldsymbol z)=(D_{\boldsymbol I_0}P)\bigl(\sum_lz_{1,l}y_{1,l},\ldots,\sum_lz_{m,l}y_{m,l}\bigr)\) in the \(mn\) variables \(z_{j,l}\) is nonzero and has degree at most \(d_j\) in each \(z_{j,l}\). Lemma 12.10 supplies integers \(|z_{j,l}|\le B\) and orders \(a_{j,l}\le d_j/B\) at which a derivative of \(G\) does not vanish. By the chain rule, \(\partial/\partial z_{j,l}\) acts as the derivative of \(D_{\boldsymbol I_0}P\) in the direction \(y_{j,l}\), a combination of first-order derivatives in block \(j\). Divided derivatives compose to nonzero multiples of divided derivatives. Hence some \(T=D_{\boldsymbol I}P\) with \(|\boldsymbol I_j|=a_j+\sum_la_{j,l}\) does not vanish at \(x'=(x'_1,\ldots,x'_m)\), where \(x'_j=\sum_lz_{j,l}y_{j,l}\). Its weighted order is at most \(m\eta/2+mn/B=m\eta\). The points \(x'_j\) have coordinates in \(\mathcal O_{K,S}\). At finite \(v\in S\) they satisfy \(|L_{v,i}(x'_j)|_v\le Q_j^{c_{v,i}}\), with the rounded radius, and at infinite \(v\) they satisfy \(|L_{v,i}(x'_j)|_v\le(nB)^{d_v/d}Q_j^{c_{v,i}}\).

*The value is small.* For \(v\in S\) write \(T=\sum_Jt_{v,J}\prod_{j,i}L_{v,i}(\boldsymbol X_j)^{J_{j,i}}\), and put \(\theta_i(J)=\sum_jJ_{j,i}/d_j\). Since \(d_j\log Q_j=D-\delta_j\) with \(0\le\delta_j<\log Q_j\), we get \(\sum_jJ_{j,i}\log Q_j\ge D\,\theta_i(J)-m\log Q_m\), and also \(\sum_jJ_{j,i}\log Q_j\le D\,\theta_i(J)\). For \(J\) with \(t_{v,J}\ne0\), (12.23) gives

\[
 \sum_ic_{v,i}\,\theta_i(J)\le\frac mN\sum_ic_{v,i}+2m(N-1)\eta\sum_i|c_{v,i}| .
\]

Let \(\mu_v\) be the largest value of \(\log\prod_{j,i}|L_{v,i}(x'_j)|_v^{J_{j,i}}\) over the \(J\) with \(t_{v,J}\ne0\), and let \(A=\sum_{v\in S}\mu_v\). Summing over \(v\), and using \(\sum c_{v,i}\le-\rho\) and the choice of \(\eta\),

\[
 A\le-\frac{3m\rho}{4N}D+\log(nB)\sum_jd_j+m\log Q_m\sum_{v,i}|c_{v,i}|\le-\frac{m\rho}{2N}D .
 \tag{12.25}
\]

The last inequality holds once \(\log Q_1\ge8N\log(nB)/\rho\), so that \(\log(nB)\sum_jd_j\le m\rho D/(8N)\), and then \(D\) is large enough to absorb the constant term.

*The value is not too small.* The coefficients of \(T\) are integers and the \(x'_j\) are \(S\)-integral, so \(T(x')\) is a nonzero element of \(\mathcal O_{K,S}\), and \(\prod_{v\in S}|T(x')|_v\ge1\). For \(v\in S\), \(|T(x')|_v\le V^{\epsilon_v}\max_J|t_{v,J}|_v\,e^{\mu_v}\), where \(\epsilon_v=d_v/d\) at infinite places and \(\epsilon_v=0\) at finite places, and \(V\le2^{N\sum d_j}\). By Lemma 12.8, \(\log\max_J|t_{v,J}|_v\le C\sum_jd_j\). Taking logarithms and summing over \(v\in S\),

\[
 A\ge-C_3\sum_jd_j\ge-C_3\frac{mD}{\log Q_1},
 \tag{12.26}
\]

where \(C_3=N\log2+|S|C\) depends only on choices 1–2. If \(\log Q_1>2NC_3/\rho\), then (12.25) and (12.26) are incompatible. So the set of hyperplanes cannot be infinite. \(\square\)

## 8. The Subspace theorem

### Lemma 12.12. A simultaneous change of basis

For every \(v\in S\) fix \(N\) linearly independent \(K_v\)-linear forms \(A_{v,1},\ldots,A_{v,N}\) on \(K_v^N\), and let \(x_1,\ldots,x_N\) be a basis of \(K^N\) with

\[
 |A_{v,i}(x_j)|_v\le\mu_{v,j},\qquad0<\mu_{v,1}\le\cdots\le\mu_{v,N},
\]

for all \(v\in S\) and all \(i,j\). There are elements \(\xi_{ji}\in\mathcal O_{K,S}\) and, for each \(v\in S\), a permutation \(\pi_v\) of \(\{1,\ldots,N\}\), such that \(u_j=x_j+\sum_{i<j}\xi_{ji}x_i\) satisfy

\[
 |A_{v,\pi_v(i)}(u_j)|_v\le
 \begin{cases}
 C\min(\mu_{v,i},\mu_{v,j}),&v\mid\infty,\\
 \min(\mu_{v,i},\mu_{v,j}),&v\nmid\infty,
 \end{cases}
 \tag{12.27}
\]

where \(C\) depends only on \(K\), \(S\) and \(N\). In particular \(C\) does not depend on the forms or on the \(\mu_{v,j}\).

**Proof.** *Approximation by \(S\)-integers.* Let \(\gamma_v\in K_v\) be given for \(v\in S\). We find \(\xi\in\mathcal O_{K,S}\) with \(|\xi-\gamma_v|_v\le1\) at the finite places of \(S\) and \(|\xi-\gamma_v|_v\le C_0\) at the infinite places, where \(C_0\) depends only on \(K\). Choose a positive integer \(D\) with \(D\gamma_v\in\mathcal O_v\) at the finite \(v\in S\), and let \(e_u\) be the exponent of the prime of a finite place \(u\) in \(D\). By the Chinese remainder theorem, Proposition 3.3 of Discrete valuation rings and Dedekind domains, applied to these prime powers, there is \(a\in\mathcal O_K\) with \(a\equiv D\gamma_v\) modulo the \(e_v\)-th power of the prime at each finite \(v\in S\) dividing \(D\), and \(a\equiv0\) modulo the \(e_u\)-th power at each \(u\notin S\) dividing \(D\). For the first kind of congruence, replace \(D\gamma_v\) by an element of \(\mathcal O_K\) congruent to it modulo that power; one exists because \(\mathcal O_K/\mathfrak p^e\to\mathcal O_v/\mathfrak p^e\mathcal O_v\) is onto. Then \(\alpha=a/D\) is integral at every finite place outside \(S\), and \(|\alpha-\gamma_v|_v\le1\) at every finite \(v\in S\). Now \(\mathcal O_K\) is a lattice in \(\prod_{v\mid\infty}K_v\), by Proposition 7.2 of Lattices, Minkowski's theorem and the Minkowski embedding. Choose \(\beta\in\mathcal O_K\) such that \((\alpha-\beta-\gamma_v)_{v\mid\infty}\) lies in a fixed fundamental parallelepiped. Then \(\xi=\alpha-\beta\) has the required properties, since \(\beta\) is integral at every finite place.

*Induction on \(N\).* For \(N=1\) take \(u_1=x_1\). Let \(N\ge2\), and let \(V'\) be the span of \(x_1,\ldots,x_{N-1}\). At each \(v\in S\), the restrictions of \(A_{v,1},\ldots,A_{v,N}\) to \(V'\otimes K_v\) satisfy a nontrivial relation \(\sum_i\gamma_{v,i}A_{v,i}|_{V'}=0\), unique up to a scalar, because exactly one line of forms vanishes on a hyperplane. Normalize it so that its largest coefficient is \(\gamma_{v,i_v}=1\); then \(|\gamma_{v,i}|_v\le1\) for all \(i\). The restrictions of the forms \(A_{v,i}\), \(i\ne i_v\), are independent on \(V'\otimes K_v\). The induction hypothesis for \(V'\), the basis \(x_1,\ldots,x_{N-1}\) and these forms supplies \(u_1,\ldots,u_{N-1}\) and bijections \(\pi'_v\colon\{1,\ldots,N-1\}\to\{1,\ldots,N\}\setminus\{i_v\}\). Put \(\pi_v(i)=\pi'_v(i)\) for \(i<N\) and \(\pi_v(N)=i_v\).

At each \(v\), the matrix \((A_{v,\pi_v(i)}(u_l))_{i,l<N}\) is invertible, so there are \(\zeta_{v,l}\in K_v\) with \(A_{v,\pi_v(i)}\bigl(x_N+\sum_{l<N}\zeta_{v,l}u_l\bigr)=0\) for all \(i<N\). Approximate each \(\zeta_{v,l}\) by an \(S\)-integer \(\xi_l\), simultaneously for all \(v\in S\), and put \(u_N=x_N+\sum_{l<N}\xi_lu_l\). This is again a unipotent upper triangular change of the \(x_j\) over \(\mathcal O_{K,S}\). For \(i<N\),

\[
 A_{v,\pi_v(i)}(u_N)=\sum_{l<N}(\xi_l-\zeta_{v,l})\,A_{v,\pi_v(i)}(u_l),
\]

and the induction bounds \(|A_{v,\pi_v(i)}(u_l)|_v\le C'\mu_{v,i}\) give \(|A_{v,\pi_v(i)}(u_N)|_v\le(N-1)^{d_v/d}C_0C'\mu_{v,i}\) at infinite places and \(\le\mu_{v,i}\) at finite places. As \(\mu_{v,i}=\min(\mu_{v,i},\mu_{v,N})\), this is (12.27) for these entries.

For the form \(A_{v,i_v}\), use \(\Gamma_v=\sum_i\gamma_{v,i}A_{v,i}\), which vanishes on \(V'\). On \(u_j\) with \(j<N\), \(A_{v,i_v}(u_j)=-\sum_{i\ne i_v}\gamma_{v,i}A_{v,i}(u_j)\) is bounded by a fixed multiple of \(\mu_{v,j}=\min(\mu_{v,N},\mu_{v,j})\). On \(u_N\), \(A_{v,i_v}(u_N)=\Gamma_v(x_N)-\sum_{i\ne i_v}\gamma_{v,i}A_{v,i}(u_N)\). Here \(|\Gamma_v(x_N)|_v\) is at most a fixed multiple of \(\mu_{v,N}\), by the hypothesis on \(x_N\), and the other terms were just bounded by multiples of \(\mu_{v,N}\). At finite places all these multiples equal one, by the ultrametric inequality. Every constant is a product of dimension factors and \(C_0\). \(\square\)

### Theorem 12.13. The projective Subspace theorem

Fix a number field \(K\), an integer \(N\ge2\), a real number \(\varepsilon>0\) and a finite set \(S\) of places of \(K\). At each \(v\in S\) take \(N\) linearly independent linear forms \(L_{v,1},\ldots,L_{v,N}\) whose coefficients are algebraic numbers, and compute their values at \(v\) with a fixed extension of \(|\cdot|_v\) to the field generated by the coefficients. Then the points \([x]\in\mathbb P^{N-1}(K)\) with

\[
 \prod_{v\in S}\prod_{i=1}^N\frac{|L_{v,i}(x)|_v}{\|x\|_v}<H([x])^{-N-\varepsilon}
 \tag{12.28}
\]

lie in finitely many proper \(K\)-linear subspaces of \(K^N\).

**Proof for coefficients in \(K\).** *Enlarging \(S\).* Add the infinite places to \(S\). Add also finitely many finite places whose primes have classes generating the class group, which is finite by Corollary 8.2 of Finiteness of the class number. Then every ideal of \(\mathcal O_{K,S}\) is principal: an ideal of \(\mathcal O_K\) is a principal fractional ideal times a product of powers of these primes, and the primes become units in \(\mathcal O_{K,S}\). At an added place use the coordinate forms \(X_1,\ldots,X_N\). Their factor \(\prod_i|x_i|_v/\|x\|_v\) is at most one, so every solution of (12.28) for the original set remains a solution for the enlarged one.

*Normalized representatives.* Each point has a representative \(x\in\mathcal O_{K,S}^N\) whose coordinates generate \(\mathcal O_{K,S}\). Then \(\|x\|_v=1\) for \(v\notin S\), so \(H([x])=\prod_{v\in S}\|x\|_v\), and (12.28) becomes

\[
 \prod_{v\in S}\prod_{i=1}^N|L_{v,i}(x)|_v<H([x])^{-\varepsilon}.
 \tag{12.29}
\]

The \(S\)-logarithms of \(S\)-units form a full lattice in the hyperplane \(\sum_{v\in S}t_v=0\), by Theorem 9.4 of Dirichlet's unit theorem, after rescaling the logarithms by \(1/d\). The vector \((h/|S|-\log\|x\|_v)_{v\in S}\), with \(h=h([x])\), lies in that hyperplane. So there is an \(S\)-unit \(\epsilon_0\) whose \(S\)-logarithm is within a fixed distance of it. Replacing \(x\) by \(\epsilon_0x\) keeps the coordinates generating \(\mathcal O_{K,S}\), leaves (12.29) unchanged because \(\prod_{v\in S}|\epsilon_0|_v=1\), and achieves \(|\log\|x\|_v-h/|S||\le C_5\) for \(v\in S\).

*Finitely many box families.* Solutions with some \(L_{v,i}(x)=0\) lie in the finitely many proper subspaces \(\ker L_{v,i}\). Solutions of bounded height are finitely many, by Northcott's Theorem 2.6. For the others, \(|L_{v,i}(x)|_v\le C_6\|x\|_v\) gives \(\log|L_{v,i}(x)|_v\le h+C_7\). In the other direction, \(L_{v,i}(x)\) is a nonzero element of height at most \(h+C_8\), by the estimate for values of linear forms in the proof of Lemma 12.9 and \(h_{\mathrm{aff}}(x)\le h+|S|C_5\); hence \(\log|L_{v,i}(x)|_v\ge-h-C_8\). For large \(h\), the vector \(\bigl(\log|L_{v,i}(x)|_v/h\bigr)_{v,i}\) therefore lies in \([-2,2]^{N|S|}\). Cover this cube by finitely many closed cubes of side \(\varepsilon/(2N|S|)\). If \(c=(c_{v,i})\) is the upper corner of a cube containing the vector, then \(|L_{v,i}(x)|_v\le H([x])^{c_{v,i}}\). Also \(\sum_{v,i}c_{v,i}<-\varepsilon+\varepsilon/2\), by (12.29). Thus every remaining solution satisfies \(x\in\Pi(Q)\cap K^N\) with \(Q=H([x])\), for one of finitely many exponent families \(c\) with \(\sum c_{v,i}\le-\rho\), where \(\rho=\varepsilon/2\). It remains to show, for one such family, that the vectors of all \(\Pi(Q)\cap K^N\) with large \(Q\) lie in finitely many proper subspaces.

*The gap between consecutive minima.* Let \(\lambda_1\le\cdots\le\lambda_N\) be the minima of \(\Pi(Q)\) in the sense of Lemma 12.5. By (12.14) and (12.16), \(\prod_j\lambda_j\asymp\operatorname{vol}(\Pi(Q))^{-1/d}\gg Q^{\rho}\), so \(\lambda_N\gg Q^{\rho/N}\). For large \(Q\) this exceeds one, and the dimension \(R\) of \(U(Q)\), which is the number of minima at most one, satisfies \(R\le N-1\). If \(R=0\) there is nothing to prove. Otherwise \(\lambda_R\le1\), and the \(N-R\le N-1\) ratios \(\lambda_j/\lambda_{j+1}\le1\), \(R\le j<N\), have product \(\lambda_R/\lambda_N\ll Q^{-\rho/N}\). Hence some \(k\) with \(R\le k\le N-1\) satisfies

\[
 \frac{\lambda_k}{\lambda_{k+1}}\ll Q^{-\rho/(N(N-1))}.
 \tag{12.30}
\]

The minima are polynomially bounded: \(Q^{-C_9}\ll\lambda_1\le\lambda_N\ll Q^{C_9}\). For the lower bound, a nonzero coordinate of a nonzero vector of \(\lambda_1\Pi(Q)\cap K^N\) is an \(S\)-integer whose product of absolute values over \(S\) is at least one. For the upper bound, multiply the standard basis vectors by a positive integer composed of the primes below the finite places of \(S\), large enough for the finite radii; the archimedean dilation needed is then a power of \(Q\).

*The change of basis.* Choose independent \(x_1,\ldots,x_N\in\mathcal O_{K,S}^N\) with \(x_j\in\lambda_j\Pi(Q)\). Then \(x_1,\ldots,x_R\) span \(U(Q)\). At each \(v\in S\) rescale the forms: \(A_{v,i}=s_{v,i}L_{v,i}\), where \(s_{v,i}\in K_v\) has \(|s_{v,i}|_v=Q^{-c_{v,i}}\) at infinite places and equals the reciprocal of the rounded radius at finite places. Lemma 12.12 applies with \(\mu_{v,j}=\lambda_j^{d_v/d}\) for infinite \(v\) and \(\mu_{v,j}=1\) for finite \(v\). It supplies \(u_1,\ldots,u_N\in\mathcal O_{K,S}^N\) and permutations \(\pi_v\) satisfying (12.27). The span \(W_k\) of \(u_1,\ldots,u_k\) equals that of \(x_1,\ldots,x_k\), so it contains \(U(Q)\).

*Exterior powers.* Put \(r=N-k\) and \(M=\binom Nr\ge2\). For an \(r\)-subset \(I=\{i_1<\cdots<i_r\}\) put \(u_I=u_{i_1}\wedge\cdots\wedge u_{i_r}\in\bigwedge^rK^N\cong K^M\); its coordinates are \(r\)-minors, hence \(S\)-integers. For \(v\in S\) and an \(r\)-subset \(J\), the \(K\)-linear form \(L^{\pi}_{v,J}=L_{v,\pi_v(j_1)}\wedge\cdots\wedge L_{v,\pi_v(j_r)}\) takes \(y_1\wedge\cdots\wedge y_r\) to \(\det\bigl(L_{v,\pi_v(j_a)}(y_b)\bigr)_{a,b}\). For each \(v\) these \(M\) forms are independent. Expanding the determinant of rescaled forms, a sum over bijections \(\tau\colon J\to I\), and using (12.27) factor by factor,

\[
 \bigl|\det\bigl(A_{v,\pi_v(j_a)}(u_{i_b})\bigr)\bigr|_v\le C'_v\prod_{j\in J}\mu_{v,j}.
\]

Let \(I_0=\{k+1,\ldots,N\}\). If \(J=I_0\) and \(I\ne I_0\), then \(I\) contains an index at most \(k\). Every bijection \(\tau\) then sends some \(j_0\in I_0\) to \(\tau(j_0)\le k\), and \(\min(\mu_{v,j_0},\mu_{v,\tau(j_0)})\le\mu_{v,k}\le(\mu_{v,k}/\mu_{v,k+1})\,\mu_{v,j_0}\). So in this case the bound improves by the factor \(\mu_{v,k}/\mu_{v,k+1}\). Undoing the rescaling, the \(M-1\) independent vectors \(u_I\), \(I\ne I_0\), lie in the box \(\Pi'(Q)\subset\bigwedge^rK^N\) defined at \(v\in S\) by the forms \(L^{\pi}_{v,J}\) with radii

\[
 \theta_{v,J}=C'_v\,Q^{\sum_{j\in J}c_{v,\pi_v(j)}}\prod_{j\in J}\mu_{v,j}\times
 \begin{cases}\mu_{v,k}/\mu_{v,k+1},&J=I_0,\\1,&J\ne I_0,\end{cases}
\]

and outside \(S\) by \(S\)-integrality. At finite places \(C'_v\) also absorbs the bounded ratio between the rounded radii and the powers of \(Q\). Each \(j\in\{1,\ldots,N\}\) lies in \(b=\binom{N-1}{r-1}\) of the subsets \(J\). Moreover \(\prod_{v\mid\infty}\mu_{v,j}=\lambda_j\), and \(\prod_{v\mid\infty}\mu_{v,k}/\mu_{v,k+1}=\lambda_k/\lambda_{k+1}\). Hence, by the volume computation (12.14) for these forms, by (12.16) and by (12.30),

\[
 \operatorname{vol}(\Pi'(Q))^{1/d}\asymp\frac{\lambda_k}{\lambda_{k+1}}\Bigl(Q^{\sum_{v,i}c_{v,i}}\prod_j\lambda_j\Bigr)^b\asymp\frac{\lambda_k}{\lambda_{k+1}}\ll Q^{-\rho/(N(N-1))}.
 \tag{12.31}
\]

By Lemma 12.5 in dimension \(M\), the minima \(\lambda'_1,\ldots,\lambda'_M\) of \(\Pi'(Q)\) satisfy \(\lambda'_{M-1}\le1\) and \((\lambda'_M)^d\gg\operatorname{vol}(\Pi'(Q))^{-1}\), which exceeds one for large \(Q\). So the \(K\)-vectors of \(\Pi'(Q)\) span exactly the hyperplane \(H(Q)\) spanned by the \(u_I\), \(I\ne I_0\).

*Fixing the exponents.* The polynomial bounds on the minima put the numbers \(\log\theta_{v,J}/\log Q\) in a fixed bounded set. Fix \(k\) and the permutations; there are finitely many choices. Cover that set by finitely many cubes of side \(\rho/(4N(N-1)M|S|)\). For the \(Q\) whose exponent vector lies in a given cube, enlarge every radius to \(Q^{c''_{v,J}}\), with \(c''\) the upper corner. If a cube contains only bounded \(Q\), its solutions are finitely many. Otherwise (12.31) gives \(\sum_{v,J}c''_{v,J}<-\rho/(2N(N-1))\). The enlarged box contains \(\Pi'(Q)\), and by the same minimum argument it still has rank exactly \(M-1\) for large \(Q\), with the same span \(H(Q)\). Proposition 12.11, applied to the \(K\)-linear forms \(L^{\pi}_{v,J}\) and the fixed exponents \(c''\), shows that \(H(Q)\) runs through a finite set of hyperplanes for each of the finitely many choices.

*Recovering the subspace.* Wedge product gives a perfect pairing \(\bigwedge^kK^N\times\bigwedge^rK^N\to\bigwedge^NK^N\cong K\). The vector \(\omega=u_1\wedge\cdots\wedge u_k\) pairs to zero with every \(u_I\), \(I\ne I_0\), and not with \(u_{I_0}\). Hence \(H(Q)\) is the kernel of \(\omega\wedge\cdot\), which determines the line \(K\omega\), and \(W_k=\{z\in K^N:z\wedge\omega=0\}\). Finitely many hyperplanes \(H(Q)\) therefore give finitely many proper subspaces \(W_k\), and these contain \(U(Q)\), hence every remaining solution. This proves the theorem for coefficients in \(K\).

**Algebraic coefficients.** Let \(E/K\) be a finite Galois extension containing all coefficients, and \(S_E\) the set of places of \(E\) above \(S\). For \(v\in S\), the fixed extension of \(|\cdot|_v\) is given by a place \(w_v\) of \(E\) above \(v\). Every place \(w\) of \(E\) above \(v\) has the form \(|a|_w=|g(a)|_{w_v}\) for some \(g\in\operatorname{Gal}(E/K)\). At \(w\), use the forms \(L_{w,i}\) obtained from \(L_{v,i}\) by applying \(g^{-1}\) to the coefficients. For \(x\in K^N\), \(L_{w,i}(x)=g^{-1}(L_{v,i}(x))\), so \(|L_{w,i}(x)|_w=|L_{v,i}(x)|_{w_v}\). In the normalization (12.11) over \(E\), both sides are raised to the power \(\tau_w=[E_w:K_v]/[E:K]\), and the same holds for \(\|x\|_w\). As \(\sum_{w\mid v}\tau_w=1\), the product over \(w\mid v\) of the factors of (12.28) over \(E\) equals the factor at \(v\) over \(K\). The absolute height does not change under extension of the field. So every solution of (12.28) is a solution of the corresponding inequality over \(E\), with \(S_E\) and the forms \(L_{w,i}\), which have coefficients in \(E\). The case already proved puts these solutions in finitely many proper \(E\)-subspaces of \(E^N\). If an \(E\)-subspace lies in the kernel of a nonzero form \(\sum_ie_iX_i\), write \(e_i=\sum_la_{il}\omega_l\) in a \(K\)-basis \((\omega_l)\) of \(E\). Its \(K\)-points then satisfy \(\sum_ia_{il}x_i=0\) for every \(l\), and for some \(l\) this equation is nonzero. So each intersection with \(K^N\) lies in a proper \(K\)-subspace. \(\square\)

### Corollary 12.14. The \(S\)-integral form

Assume that \(S\) contains every infinite place. Then the nonzero vectors \(x\in\mathcal O_{K,S}^N\) satisfying

\[
 \prod_{v\in S}\prod_{i=1}^N|L_{v,i}(x)|_v<H([x])^{-\varepsilon}
 \tag{12.32}
\]

are contained in finitely many proper \(K\)-subspaces. To see this, note that \(\|x\|_v\le1\) at the places outside \(S\), so \(H([x])\le\prod_{v\in S}\|x\|_v\). Dividing (12.32) by \(\prod_{v\in S}\|x\|_v^N\ge H([x])^N\) gives (12.28). Over \(\mathbb Q\), a vector of coprime integers has \(H([x])=\max_i|x_i|\). Integer multiples of a solution lie in the same subspaces, as the projective statement requires.

## 9. Approximation at several places

### Corollary 12.15. Lang's number-field form of Roth's theorem

Let \(S\) be a finite set of places of a number field \(K\), containing its infinite places. Choose a target \(\alpha_v\in\mathbb P^1(\overline{\mathbb Q})\) and an extension of (12.11) at each place. For every \(\varepsilon>0\), only finitely many \(\beta\in K\) satisfy

\[
         \prod_{v\in S}\min(1,|\alpha_v-\beta|_v)
                             \le H(\beta)^{-2-\varepsilon},
         \tag{12.33}
\]

where \(|\infty-\beta|_v=|1/\beta|_v\).

**Proof.** For a finite target take \(L_{v,1}=X_0\), \(L_{v,2}=X_1-\alpha_vX_0\), and \(x=(1,\beta)\). The local product in (12.28) is

\[
                      \frac{|\beta-\alpha_v|_v}{\max(1,|\beta|_v)^2}
                       \le C_v\min(1,|\beta-\alpha_v|_v).
\]

When the error is at most one this is immediate. Otherwise the triangle inequality bounds the numerator by a fixed multiple of \(\max(1,|\beta|_v)\). For target infinity take \(X_0,X_1\); the local quotient is \(|\beta|_v/\max(1,|\beta|_v)^2\le\min(1,|1/\beta|_v)\). Thus (12.33) implies (12.28) with parameter \(\varepsilon/2\) for large height. Theorem 12.13 gives finitely many \(K\)-lines in \(K^2\), and each line contains at most one point \((1,\beta)\). Bounded heights are finite by Northcott. Values equal to a target, including \(\beta=0\) when needed, contribute only finitely many additional elements. \(\square\)

### Corollary 12.16. Ridout's theorem and restricted denominators

Let \(\alpha\) be real algebraic, \(S_0\) a finite set of rational primes, and \(\varepsilon>0\). For reduced \(p/q\), \(q>0\), put \(H=\max(|p|,q)\). There are finitely many distinct rationals with

\[
            \left(\prod_{\ell\in S_0}|pq|_\ell\right)
                    |\alpha-p/q|<H^{-2-\varepsilon}.
            \tag{12.34}
\]

There are also finitely many with both \(|\alpha-p/q|<1\) and

\[
            \left(\prod_{\ell\in S_0}|pq|_\ell\right)
                    |\alpha-p/q|<q^{-2-\varepsilon}.
            \tag{12.35}
\]

In particular, if all primes dividing \(q\) lie in \(S_0\), the inequality
\(|\alpha-p/q|<q^{-1-\varepsilon}\) has finitely many rational solutions.

**Proof.** At infinity use the forms \(Q,P-\alpha Q\), and at the finite places in \(S_0\) use \(P,Q\). Their product on the integer vector \((p,q)\) is \(q^2|\alpha-p/q|\prod_{\ell\in S_0}|pq|_\ell\). Equation (12.34) makes it less than \(H^{-\varepsilon}\), so Corollary 12.14 applies. Its finitely many lines give finitely many ratios. The rationals with \(p=0\), or with exact error zero, form a finite set and can be handled separately.

For (12.35), the extra condition gives \(H\le(|\alpha|+1)q+q\), hence \(q^{-\varepsilon}<H^{-\varepsilon/2}\) for large \(q\); apply the same argument. Finally a denominator supported on \(S_0\) has \(\prod_{\ell\in S_0}|q|_\ell=1/q\), while the numerator product is at most one. An error \(<q^{-1-\varepsilon}\) satisfies (12.35), and is less than one except for a bounded denominator. \(\square\)

The bounded-neighbourhood condition in the denominator version cannot be discarded. For \(\alpha>0\), \(p=2^k\), \(q=1\), \(S_0=\{2\}\), and \(2^k>\alpha\), its left side is \(1-\alpha/2^k<1=q^{-2-\varepsilon}\), for infinitely many distinct integers. This explains the use of height in (12.34).

**Example.** Ridout proves that \(\sum_{n\ge0}b^{-2^n}\), \(b\ge2\), is transcendental. Its reduced truncation denominator is \(q_N=b^{2^N}\), and its positive tail is \(<2q_N^{-2}\). The denominator bound first proves irrationality. If the sum were algebraic, these \(S_0\)-supported denominators, with \(S_0\) the primes dividing \(b\), would contradict the last assertion of Corollary 12.16 with \(\varepsilon=1/2\). Ordinary Roth does not give this contradiction from these particular truncations, whose exponent is two.

## 10. \(S\)-unit equations and Thue–Mahler finiteness

### Corollary 12.17. Nondegenerate \(S\)-unit equations

Let \(K\) be a number field, \(S\) finite and containing its infinite places, and \(a_1,\ldots,a_m\in K^\times\). There are finitely many projective tuples of \(S\)-units \(u_i\) satisfying

\[
                    \sum_{i=1}^m a_iu_i=0
                    \tag{12.36}
\]

with no vanishing nonempty proper subsum. Equivalently, \(\sum_{i=1}^n a_iu_i=1\) has finitely many solutions with no vanishing nonempty subsum on the left.

**Proof.** Enlarge \(S\) to make all fixed coefficients units, and induct on \(m\). For \(m=2\) there is one ratio. For larger \(m\), divide by the last term and write
\(\sum_{i=1}^{n}x_i=1\), \(n=m-1\), with every \(x_i\) an \(S\)-unit.

At each place choose \(k_v\) attaining \(\max_i|x_i|_v\). Use the \(n\) independent forms consisting of the coordinate forms except \(X_{k_v}\), together with \(\sum_iX_i\). The local product divided by \(\|x\|_v^n\), multiplied over \(S\), equals

\[
                  \frac{\prod_{v\in S,i}|x_i|_v}{H([x])^{n+1}}
                              =H([x])^{-n-1}.
\]

Theorem 12.13, with any parameter between zero and one, therefore places the large-height solutions in finitely many hyperplanes. There are finitely many choices of the \(k_v\). Bounded projective height gives finitely many actual tuples: the equation \(\sum x_i=1\) implies \(H([1:x])\le nH([x])\), by the local triangle inequalities, so Northcott applies to each coordinate.

On one of these hyperplanes write \(\sum_i b_ix_i=0\), with some \(b_i\ne0\). Choose a minimal nonempty vanishing subsum, on an index set \(I\) of nonzero coefficients. It has at least two terms and at most \(n<m\). The induction hypothesis applied to this smaller homogeneous equation gives finitely many ratios \(x_i/x_{i_0}\), \(i\in I\). Fix such ratios, writing \(x_i=c_ix_{i_0}\). Their sum \(C=\sum_{i\in I}c_i\) is nonzero: otherwise a proper subsum of the original normalized equation would vanish. Collapse those terms into \(Cx_{i_0}\). The resulting equation, including the constant term \(-1\), has fewer than \(m\) terms and is still nondegenerate, since any vanishing proper subsum would lift to one in the original equation. Apply induction again, enlarging \(S\) for the finitely many new coefficients if needed. It gives finitely many normalized tuples, and reinstating the fixed ratios gives finitely many original tuples. The finitely many hyperplanes and index sets complete the induction. \(\square\)

The nondegeneracy condition is necessary. For instance \((t,-t,1)\), with arbitrary \(S\)-unit \(t\), gives infinitely many solutions to \(u_1+u_2+u_3=1\).

### Corollary 12.18. Mahler's theorem for a fixed binary-form value

Let \(F\in K[X,Y]\) be homogeneous of degree \(D\ge3\) and squarefree, let \(m\in K^\times\), and let \(S\) be finite. Then \(F(a,b)=m\) has finitely many solutions in \(\mathcal O_{K,S}^2\), with infinite places added to \(S\) if necessary.

**Proof.** Pass to a finite splitting field and enlarge \(S\) so that all linear-factor coefficients and \(m\) are integral units where needed. Write \(F=\prod_{i=1}^D L_i\), absorbing its leading constant into one factor. The factors are pairwise nonproportional. Each \(L_i(a,b)\) is integral outside \(S\); their nonzero product is an \(S\)-unit, so each is an \(S\)-unit. Three distinct factors have a relation \(c_1L_1+c_2L_2+c_3L_3=0\) with all \(c_i\ne0\). Its evaluated unit equation is nondegenerate: a one-term zero is impossible, and a two-term zero would force the remaining nonzero term to be zero. Corollary 12.17 gives finitely many ratios of their values.

The independent pair \(L_1,L_2\) then determines finitely many \((a:b)\). For a fixed representative \((a_0,b_0)\), the remaining scale satisfies \(t^DF(a_0,b_0)=m\), which has at most \(D\) roots. This gives finitely many pairs over the splitting field, hence over \(K\). \(\square\)

**The classical Thue–Mahler equation.** If \(F\in\mathbb Z[X,Y]\) is squarefree of degree at least three, \(m\ne0\), and \(S_0\) is a finite set of primes, then

\[
                F(x,y)=m\prod_{\ell\in S_0}\ell^{e_\ell},
       \qquad x,y\in\mathbb Z,\quad \gcd(x,y)=1,\quad e_\ell\ge0
       \tag{12.37}
\]

has finitely many solutions. Use the same three-factor unit argument: outside the enlarged set of places the right side is a unit, so all factor values are units. It gives finitely many rational slopes. Each slope has only two primitive integer representatives, and its nonzero value determines the exponents uniquely. The primitive condition matters: multiplying both coordinates by arbitrary powers of a prime in \(S_0\) would otherwise supply infinite families. Effective bounds for these equations are developed in S-unit equations and Thue–Mahler equations, §§2–3. The finiteness proofs here require no such effective bounds.

## 11. Exercises

1. **Easy — decimal gaps.** Show that \(\sum_{n\geq0}10^{-3^n}\) is transcendental by Roth's theorem. Explain why the displayed truncations alone do not give a Liouville proof.

2. **Medium — homogeneous lower bounds.** Prove (12.10) for every \(\varepsilon>0\), including nonprimitive integer pairs.

3. **Medium — two linear forms.** Show that Roth's theorem is equivalent to the following statement: for two independent linear forms \(L_1,L_2\) in two variables with algebraic coefficients, and every \(\varepsilon>0\), only finitely many integer pairs satisfy

   \[
          0<|L_1(x,y)L_2(x,y)|<\max(|x|,|y|)^{-\varepsilon}.
   \]

4. **Hard — simultaneous approximation.** From the Subspace theorem, deduce that if real algebraic \(\alpha_1,\ldots,\alpha_n\) have \(1,\alpha_1,\ldots,\alpha_n\) rationally independent, then
\(\max_j|\alpha_j-p_j/q|<q^{-1-1/n-\varepsilon}\)
has only finitely many integer solutions with \(q>0\).

## 12. Solutions

1. Apply Corollary 12.2 with \(b=10\). The reduced truncations have positive errors \(<2q_N^{-3}\), and irrationality follows first from the elementary rational denominator bound. Roth then excludes algebraicity, using any fixed parameter smaller than one. The exponent three does not exceed every possible algebraic degree, so these particular approximations do not give the arbitrary exponents needed for a Liouville construction.

2. The proof of Corollary 12.3 gives the primitive bound with the smaller parameter \(\varepsilon/2\), whose spare factor \(H^{\varepsilon/2}\) absorbs the fixed coefficient constants. For \((x,y)=g(x_0,y_0)\), the ratio of the two sides is the primitive ratio multiplied by \(g^{2+\varepsilon}\). Large primitive pairs therefore give no new exceptions, and each of the finitely many small primitive pairs has only finitely many exceptional multiples. For \(\varepsilon\geq d-2\), nonzero integrality makes the conclusion immediate.

3. An invertible coefficient matrix gives \(\max(|L_1|,|L_2|)\geq cH\), \(H=\max(|x|,|y|)\). The product condition forces the smaller nonzero form to have absolute value \(<C H^{-1-\varepsilon}\). If its coefficient ratio is nonreal, its real and imaginary parts are independent real forms and bound it below by a positive multiple of \(H\), impossible for large \(H\). If it is a multiple of a rational form, its nonzero value is bounded below by a fixed positive constant on integer pairs, again impossible.

   Otherwise write it as \(a(x-\alpha y)\), with \(\alpha\) real irrational algebraic. Smallness forces \(|y|\) comparable with \(H\), and gives \(|\alpha-x/y|<C'|y|^{-2-\varepsilon}\). After reduction, with denominator \(q\leq|y|\), this is also \(<C'q^{-2-\varepsilon}\), hence \(<q^{-2-\varepsilon/2}\) for large \(q\). Roth leaves finitely many reduced ratios. Each fixed ratio leaves only finitely many multiples, since its nonzero product grows quadratically in the multiple while the right-hand side decreases. Bounded reduced denominators have only finitely many ratios in the bounded neighbourhood in question. The same reasoning applies whichever form is smaller, proving finiteness.

   Conversely take \(L_1=X-\alpha Y\), \(L_2=Y\). Infinitely many reduced approximations of exponent \(2+\delta\) would give product \(<q^{-\delta}\), with \(H\) comparable with \(q\). For large \(q\) this is \(<H^{-\delta/2}\) and nonzero, contradicting the two-form assertion. This proves equivalence.

4. Take the independent forms \(L_0=X_0\) and \(L_j=\alpha_jX_0-X_j\), \(1\le j\le n\), on the integer vector \(x=(q,p_1,\ldots,p_n)\). The product is

   \[
       q\prod_{j=1}^n|\alpha_jq-p_j|
                  <q\left(q^{-1/n-\varepsilon}\right)^n
                  =q^{-n\varepsilon}.
   \]

   The ordinary coordinate maximum is at most \(Cq\), because the approximations keep \(p_j/q\) in fixed bounded intervals. For large \(q\) the displayed product is therefore less than that maximum to power \(-n\varepsilon/2\), hence also less than the projective height to that power. Corollary 12.14 puts all such integer vectors in finitely many proper rational subspaces. On each choose a nonzero rational relation \(a_0q+\sum_j a_jp_j=0\). Dividing by \(q\) and using the approximation inequality gives

   \[
      |a_0+\sum_j a_j\alpha_j|
             \le\sum_j|a_j|q^{-1-1/n-\varepsilon}.
   \]

   The left side is positive by the specified independence; thus that subspace admits no solutions for sufficiently large \(q\). If every \(a_j=0\) for \(j\ge1\), its equation already excludes \(q>0\). There are finitely many subspaces, so \(q\) is bounded for all solutions. At each bounded positive denominator the approximation intervals contain finitely many integer numerators. This proves finiteness, including nonprimitive vectors.

## References

- K. Soundararajan, [*Transcendental Number Theory*](https://math.stanford.edu/~ksound/TransNotes.pdf), Math 249A course notes, Stanford University, Fall 2010, written up by I. Petrow, §§15–18: Roth's theorem from the auxiliary polynomial, the index estimates and Roth's lemma, with the \(p\)-adic version and Lang's number-field form (Theorem 26).
- J.-H. Evertse, [*Diophantine Approximation*, Chapter 8: The p-adic Subspace Theorem](https://pub.math.leidenuniv.nl/~evertsejh/dio19-8.pdf), Leiden course notes, Theorems 8.6–8.7, 8.10 and 8.12–8.13: Roth's theorem with finitely many places, the \(p\)-adic Subspace theorem, Mahler's theorem on Thue–Mahler equations, and Lang's and the general finiteness theorems for nondegenerate unit equations. Theorem 3.2 of Goel, Lunia and Ray below is the number-field form.
- Shivani Goel, Rashi Lunia and Anwesh Ray, [*Diophantine approximation and the subspace theorem*](https://arxiv.org/abs/2502.00731v2), arXiv:2502.00731v2 (2026): a detailed account of Roth's lemma at algebraic points, auxiliary polynomials on products of boxes and the exterior-power proof of the Subspace theorem, the method of sections 6–8.
- M. Waldschmidt, [*Diophantine approximation, irrationality and transcendence*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/IMPA2010Cours4.pdf), IMPA course notes, Course 4 (2010), §4.1.3, Theorems 46–49: Roth's theorem, Ridout's theorem for denominators composed of finitely many primes, and Schmidt's Subspace theorem with finitely many places.
- J.-H. Evertse, [*Diophantine Approximation*, Chapter 7: The Subspace Theorem](https://pub.math.leidenuniv.nl/~evertsejh/dio19-7.pdf), Leiden course notes, Theorem 7.1 and Corollary 7.2, for the classical Subspace theorem and its consequence for Roth's theorem.
- J.-H. Evertse, [*Diophantine Approximation*, Chapter 6: Approximation of algebraic numbers by rationals](https://pub.math.leidenuniv.nl/~evertsejh/dio19-6.pdf), Leiden course notes: Theorems 6.2–6.3 and Corollary 6.4 for Roth's theorem, squarefree binary forms and Thue equations; Theorem 6.5 for Fel'dman's effective improvement of Liouville's inequality; §6.2, Theorem 6.14 and Exercise 6.8, for the gap principle and the counting of exceptional approximations.

J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, July 19, 2020, Proposition 4.26, proves the lattice and discriminant covolume formula for ideals under the real-coordinate Minkowski embedding. This gives a parallel treatment of the normalization used in the number-field prerequisites of Section 5.
