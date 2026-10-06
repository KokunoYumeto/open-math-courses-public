# Roth's theorem and its consequences

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol at Ultra. Original material is public domain (CC0), except the adapted sections 6–8, which retain CC BY 4.0 with the source credit and change notice in section 7.*

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

The Subspace theorem needs index at algebraic points, whereas Lesson 11 used rational points. The following argument preserves the degree weights and supplies that extension.

### Lemma 12.6. Roth's index lemma at algebraic points

Let \(P\in\mathbb Z[T_1,\ldots,T_m]\setminus\{0\}\), with \(\deg_{T_i}P\le r_i\), and put \(h(P)=\log\max|\text{coefficient of }P|\). Let \(\beta_i\) be algebraic and \(0<\eta\le1/2\). If

\[
 t=\eta^{\,2^{m-1}},\qquad
 r_{i+1}/r_i\le t,\qquad
 t\min_i r_i h(\beta_i)\ge h(P)+6mr_1,
 \tag{12.18}
\]

then \(\operatorname{Ind}_{\boldsymbol\beta,\boldsymbol r}P\le2m\eta\).

**Proof.** In one variable, a zero \(\beta\) of multiplicity \(l\) forces the primitive minimal polynomial of \(\beta\) to divide \(P\) to that multiplicity. By multiplicativity of Mahler measure and Lesson 2's identity \(\log M(\beta)=\deg(\beta)h(\beta)\),

\[
 l h(\beta)\le\log M(P)\le h(P)+r_1.
\]

The last inequality follows from \(M(P)\le\sqrt{r_1+1}\max|\text{coefficient}|\) and \(\tfrac12\log(r_1+1)\le r_1\). It implies the assertion for \(m=1\).

For \(m\ge2\), use the minimal separation and Wronskian construction of Lesson 11, Lemmas 11.1–11.2. There is a nonzero integer determinant \(V\), with \(k\le r_m+1\) rows, that factors as \(cU_1(T_m)U_2(T_1,\ldots,T_{m-1})\). Choose the disjoint-variable factors primitive over \(\mathbb Z\); Gauss's lemma gives \(c\in\mathbb Z\setminus\{0\}\). The entries are divided derivatives of \(P\), with derivative order at most \(r_m\) in the first \(m-1\) variables and orders \(0,\ldots,k-1\) in the last. In particular

\[
 h(U_1)+h(U_2)\le h(V)
 \le k h(P)+2k\Bigl(\sum_i r_i\Bigr)\log2+\log(k!)
 \le k(h(P)+3r_1).
 \tag{12.19}
\]

For the middle bound, each divided derivative costs at most \((\sum r_i)\log2\); multiplying \(k\) coefficient arrays costs at most \((k-1)(\sum r_i)\log2\). These follow respectively from the binomial coefficient bound and from the number of entries in each array. The determinant contributes \(\log(k!)\). Since \(t\le1/4\), \(\sum r_i\le4r_1/3\) and \(\log(k!)\le k r_m\le k r_1/4\), giving the final bound.

The one-variable multiplicity estimate applied to \(U_1\), of degree at most \(kr_m\), now gives index with the original weight \(r_m\) at most \(kt\). The induction hypothesis applied to \(U_2\), with weights \(kr_i\) and parameter \(\eta^2\), gives index with the original weights at most \(2k(m-1)\eta^2\). Indeed \((\eta^2)^{2^{m-2}}=t\), and

\[
 h(U_2)+6(m-1)kr_1
       \le k(h(P)+6mr_1)
       \le t\min_{i<m}kr_i h(\beta_i).
\]

Put \(u=\operatorname{Ind}_{\boldsymbol\beta,\boldsymbol r}P\). Additivity of index and the derivative loss bound, proved in Lesson 10, give

\[
 \operatorname{Ind}V
    \ge\sum_{j=0}^{k-1}\max(u-j/r_m,0)-k r_m/r_{m-1}.
 \tag{12.20}
\]

The sum is at least \(ku^2/(2m)\). If \(u>(k-1)/r_m\), its exact arithmetic-progression sum is at least \(ku/2\), and \(u\le m\). Otherwise integrate the decreasing function \(\max(u-s/r_m,0)\) over \(0\le s\le r_mu\); its integral is \(r_mu^2/2\). Here \(k\ge2\) unless \(u=0\), and \(r_m\ge k-1\ge k/2\), so this is at least \(ku^2/4\). Both cases give the stated bound.

Combine (12.19)–(12.20) and the two factor indices:

\[
 \frac{k u^2}{2m}\le kt+2k(m-1)\eta^2+kt
                      \le2km\eta^2.
\]

Hence \(u\le2m\eta\). \(\square\)

### Corollary 12.7. Index along hyperplanes

Let \(P\) be a nonzero integer multihomogeneous polynomial in \(m\) blocks of \(N=n+1\ge2\) variables, of block degrees at most \(d_j\). For nonzero algebraic linear forms \(M_j\), define its index by membership in the ideals generated by

\[
 \prod_j M_j^{a_j},\qquad \sum_j a_j/d_j\ge t.
\]

If \(0<\sigma\le1/2\), \(d_{j+1}/d_j\le\sigma\), and

\[
 \min_j d_jh([M_j])\ge
                 n\sigma^{-1}\bigl(h(P)+6md_1\bigr),
 \tag{12.21}
\]

then the index is at most \(2m\sigma^{1/2^{m-1}}\).

**Proof.** In each block choose a nonzero coefficient \(b_0\) of \(M_j\). Since

\[
 h([b_0:\cdots:b_n])
 \le\sum_{i=1}^n h([b_0:b_i]),
\]

one pair has height at least \(h([M_j])/n\). Relabel it as \((b_0,b_1)\). Its positive height in (12.21) ensures \(b_1\ne0\).

Remove the highest power of each discarded coordinate dividing \(P\), then set that coordinate to zero. Repeat until only coordinates 0 and 1 remain in every block. The polynomial stays nonzero and its coefficient height does not increase. Division by a discarded coordinate does not change hyperplane index: that coordinate has index zero, and weighted initial forms multiply in a polynomial domain. Specialization sends the weighted hyperplane ideal into the corresponding specialized ideal. Consequently index can increase under specialization, which is the direction needed here.

Dehomogenize by setting each retained coordinate 0 equal to one. The resulting nonzero integer polynomial has degrees at most \(d_j\); its point coordinates are \(-b_0/b_1\), of heights \(h([b_0:b_1])\). Its point index equals the binary homogeneous hyperplane index, with the same weights \(d_j\). Apply Lemma 12.6 with \(\eta=\sigma^{1/2^{m-1}}\). If \(\eta>1/2\), the requested upper bound exceeds \(m\), the trivial degree bound; otherwise (12.21) is exactly its height hypothesis. The original index is no larger than the specialized index, proving the result. \(\square\)

The exponential \(2^{m-1}\) in these lemmas is essential: the induction replaces \(\eta\) by \(\eta^2\). A linear exponent \(2m-1\) would not satisfy that induction.

## 7. Auxiliary polynomials on products of boxes

We now construct the polynomial whose small value will contradict the product formula. The construction and the exterior-power argument below follow the mathematical method of Shivani Goel, Rashi Lunia and Anwesh Ray, [*Diophantine approximation and the subspace theorem*, version 2](https://arxiv.org/pdf/2502.00731v2), §§4.4–5.3, PDF pp. 34–52. That exact version is available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Sections 6–8 of this lesson adapt that treatment, with new proofs of the supporting estimates, different counting constants, and corrected specialization and finite-exception arguments; those adapted sections retain CC BY 4.0. The other original sections are CC0. The linked paper supplies an openly licensed full treatment for further study, rather than a paid-book proof dependency.

### Lemma 12.8. A polynomial with balanced exponents

Keep the fixed forms in (12.13), put \(N=n+1\ge2\), and fix \(0<\eta<1/(4N)\). Choose an integer \(m\) so large that

\[
                  e^{-2\eta^2m}<(4dN|S|)^{-1}.
                  \tag{12.22}
\]

For all sufficiently large positive block degrees \(d_1,\ldots,d_m\), there is a nonzero integer multihomogeneous polynomial \(P(X_1,\ldots,X_m)\), of these degrees, with \(h(P)\le C\sum d_j\). If a divided derivative \(T=\partial^I P\) has weight \(\sum_j|I_j|/d_j\le m\eta\), every nonzero coefficient of its expression in the coordinates \(L_v(X_j)\) has exponents satisfying

\[
 \frac mN-2m\eta
  <\sum_j\frac{J_{j,i}}{d_j}
  <\frac mN+2m(N-1)\eta
                   \quad(1\le i\le N).
 \tag{12.23}
\]

The affine height of the entire transformed coefficient vector of \(T\), for each fixed \(v\), is at most \(C\sum d_j\). The constant depends on the fixed field, forms, \(m\) and \(\eta\), but not on the degrees.

**Proof.** A block of degree \(d_j\) has \(\binom{d_j+N-1}{N-1}\) coefficients. Impose the homogeneous \(K\)-linear conditions that a coefficient, in each \(L_v\)-coordinate system, vanish whenever

\[
                   \sum_j J_{j,i}/d_j\le m/N-m\eta
\]

for at least one coordinate \(i\). Their proportion among all coefficients tends, as every degree grows, to the corresponding volume proportion on a product of \(m\) standard simplices. This is the ordinary Riemann-sum limit; the defining hyperplane has volume zero.

For a uniformly distributed point of the simplex, a specified coordinate \(Z\) lies in \([0,1]\) and has mean \(1/N\), by symmetry. For independent copies \(Z_j\),

\[
 \Pr\left\{\sum Z_j\le m/N-m\eta\right\}\le e^{-2m\eta^2}.
\]

Here is an elementary proof of this bound. The second derivative of \(\log\mathbb E e^{tZ}\) is the variance of \(Z\) under the tilted probability measure. Every probability measure on \([0,1]\) has variance at most \(1/4\), since \(\mathbb E(Z-\tfrac12)^2\le1/4\). Integrating twice gives \(\mathbb E e^{t(Z-\mathbb EZ)}\le e^{t^2/8}\). Apply Markov's inequality to \(e^{-4\eta\sum(Z_j-1/N)}\). This proves the displayed estimate.

There are \(N|S|\) possible pairs \((i,v)\). By (12.22), the number \(M\) of imposed equations is, for large degrees, less than half the number of unknowns divided by \(d\).

We justify the needed number-field form of Siegel's lemma directly. If a \(K\)-matrix \(B\) has affine height \(h(B)\), its denominator ideal has norm at most \(e^{dh(B)}\). This norm, as a rational integer, clears every denominator: the order of the finite group \(\mathcal O_K/\mathfrak a\) kills that group. At each embedding the entries have size at most \(e^{dh(B)}\). After clearing denominators and expressing in a fixed integral basis, the integer entries are bounded by \(C_K e^{2dh(B)}\); the inverse embedding matrix supplies \(C_K\). Thus \(M\) equations become at most \(dM\) integer equations.

For \(V>2dM\) unknowns and integer coefficient bound \(A\), the pigeonhole argument of Lesson 10 yields a nonzero integer kernel vector of maximum size at most \(3VA+1\). Indeed put \(R=dM\), choose \(U=\lceil(3VA)^{R/(V-R)}\rceil\), and compare the \((U+1)^V\) integer inputs in a cube with at most \((3VAU)^R\) outputs; two have the same image. Their difference is a nonzero kernel vector, and \(U\le3VA+1\). The case \(R=0\) is immediate.

The coefficient matrix for our changes of variables has affine height \(O(\sum d_j)\). To verify this, at every place bound the entries of the fixed inverse matrices, use the multinomial formula, and at infinite places bound the number of resulting terms by \(N^{\sum d_j}\). The resulting local constants are one almost everywhere. Also \(\log V=O(\sum d_j)\). The preceding kernel bound therefore gives the claimed height of \(P\).

Differentiation in the original coordinates decreases the weighted exponent of any one \(L_v\)-coordinate by at most \(\sum|I_j|/d_j\). The imposed lower cutoff consequently gives the strict lower bound in (12.23). The total remaining weighted degree is at most \(m\), so the lower bounds for the other \(N-1\) coordinates give the upper bound. Finally divided derivatives multiply coefficients by binomial coefficients at most \(2^{\sum d_j}\). The same fixed-matrix estimate bounds the height of each full transformed coefficient vector by \(C\sum d_j\). \(\square\)

### Lemma 12.9. Height of a varying hyperplane

Suppose \(\sum c_{v,i}\le-\rho<0\), and let \(U(Q)\) be the span of the \(K\)-vectors in \(\Pi(Q)\). When \(\dim U(Q)=N-1\), either \(U(Q)\) belongs to one fixed finite family of hyperplanes, or

\[
                 h(U(Q))\ge\frac{\rho}{2|S|}\log Q-C.
                 \tag{12.24}
\]

The family and \(C\) are independent of \(Q\).

**Proof.** Choose a basis \(y_1,\ldots,y_{N-1}\) of \(U(Q)\) in the box. Its wedge, identified with a covector by the standard determinant pairing, is \(w\ne0\). It is integral outside \(S\). Let \(A_{v,i}(w)\) be the cofactor obtained by applying all the forms except \(L_{v,i}\) to this wedge. Determinant expansion gives

\[
             |A_{v,i}(w)|_v\le C_vQ^{\sum_jc_{v,j}-c_{v,i}}.
\]

If there are nonzero cofactors with indices \(i_v\) and \(\sum_vc_{v,i_v}\ge-\rho/2\), their product is at most \(CQ^{-\rho/2}\). Choose a nonzero coordinate \(w_k\). Because it is integral outside \(S\), the product formula gives \(\prod_{v\in S}|w_k|_v\ge1\). The same upper bound therefore holds for \(\prod_{v\in S}|A_{v,i_v}(w)/w_k|_v\). Each quotient has height at most \(h([w])+C_v'\): divide all coordinates of \(w\) by \(w_k\), whose coordinate is then one, and apply the fixed linear-functional height bound from Lesson 2. The lower product bound is \(e^{-|S|h([w])-C'}\). Comparing them proves (12.24).

Otherwise record the nonempty sets \(I_v=\{i:A_{v,i}(w)\ne0\}\). For each possible pattern choose, once and for all, a nonzero \(K\)-covector \(w_I\) satisfying \(A_{v,i}(w_I)=0\) for \(i\notin I_v\). Such a covector exists because the actual \(w\) is one solution. There are finitely many patterns, hence finitely many choices \(w_I\) of bounded height. Put \(W_I=\ker w_I\).

For \(x\in\Pi(Q)\cap K^N\), the determinant expansion of \(w_I(x)\) in the \(L_v\)-coordinates gives

\[
 |w_I(x)|_v\le C_{v,I}Q^{\max_{i\in I_v}c_{v,i}}\quad(v\in S).
\]

Outside \(S\) it is bounded by the coefficient norm of \(w_I\). If it were nonzero, the product formula would imply

\[
 1\le C_IQ^{\sum_v\max_{i\in I_v}c_{v,i}}<C_IQ^{-\rho/2},
\]

a contradiction for large \(Q\). Thus \(U(Q)\subset W_I\), hence equality by dimension. Bounded \(Q\) contributes only finitely many additional spans: all the relevant vectors lie in one bounded archimedean body with bounded finite denominators, hence in a finite subset of a fixed lattice. \(\square\)

Choosing \(w_I\) once for each pattern is essential. Choosing the varying covector \(w\) itself would not provide a fixed exceptional family.

### Lemma 12.10. A grid detects a nonzero polynomial

Let a nonzero polynomial in variables \(Z_1,\ldots,Z_s\) have degree at most \(e_i\) in \(Z_i\). For \(B>0\), there are integers \(|z_i|\le B\) and derivative orders \(0\le a_i\le e_i/B\) such that \(\partial^{\boldsymbol a}P(\boldsymbol z)\ne0\).

**Proof.** In one variable, otherwise every one of the \(2\lfloor B\rfloor+1\) grid points is a zero of multiplicity at least \(\lfloor e/B\rfloor+1\). Their product exceeds \(e\), because \(2\lfloor B\rfloor+1>B\). This contradicts the degree. For several variables choose any nonzero coefficient polynomial in the last variable, apply induction to it, and then apply the one-variable assertion to the resulting nonzero polynomial in that last variable. The chosen coefficient need not be the constant coefficient. \(\square\)

### Proposition 12.11. Boxes of codimension one have finitely many spans

For fixed \(K,S,L,c\) with \(\sum c_{v,i}\le-\rho<0\), the hyperplanes \(U(Q)\) of dimension \(N-1\) form a finite family.

**Proof.** Suppose they form an infinite family. Remove the finite exceptions in Lemma 12.9. Choose \(\eta\) satisfying Lemma 12.8 and so small that \(2N\eta\sum_{v,i}|c_{v,i}|<\rho/(4N)\). Choose \(m\) by (12.22), and put

\[
                       \sigma=(\eta/4)^{\,2^{m-1}}.
\]

Choose distinct remaining hyperplanes at \(Q_1,\ldots,Q_m\), with \(Q_1\) arbitrarily large and \(\log Q_{j+1}\ge2\sigma^{-1}\log Q_j\). Then choose \(D\) arbitrarily large and \(d_j=\lfloor D/\log Q_j\rfloor\). All degrees tend to infinity, \(d_{j+1}/d_j\le\sigma\), and \(d_j\log Q_j=D+o(D)\).

Lemma 12.8 gives \(P\) of height \(O(\sum d_j)=O(mD/\log Q_1)\). Lemma 12.9 gives \(d_jh(U(Q_j))\ge\rho D/(4|S|)\) once \(Q_1,D\) are large. Therefore (12.21) holds, and the hyperplane index is at most \(m\eta/2\). In coordinates consisting of a defining form of each hyperplane and a complementary basis, this means that a derivative of total weighted order at most \(m\eta/2\) restricts nontrivially to their product. These directional derivatives are linear combinations of original-coordinate derivatives of the same block orders, so one original-coordinate derivative has nonzero restriction.

Parametrize each hyperplane by a basis \(y_{j,1},\ldots,y_{j,N-1}\) in \(\Pi(Q_j)\). Apply Lemma 12.10 to the restricted derivative with \(B=2(N-1)/\eta\). Each of its \((N-1)m\) parameter degrees is at most \(d_j\). The additional weighted derivative order is at most \(m\eta/2\). The chain rule consequently supplies an original-coordinate derivative \(T\) of \(P\), of weight at most \(m\eta\), nonzero at

\[
               x_j'=\sum_{\ell=1}^{N-1}z_{j,\ell}y_{j,\ell},
                       \qquad z_{j,\ell}\in\mathbb Z,\quad |z_{j,\ell}|\le B.
\]

At finite places these points satisfy the original box bounds. At infinite places their bounds gain at most the fixed factor \(((N-1)B)^{d_v/d}\).

Let \(A\) be the sum, over \(v\in S\), of the logarithm of the largest nonzero monomial value in the \(L_v\)-expansion of \(T(x_1',\ldots,x_m')\). Equation (12.23) and \(d_j\log Q_j=D+o(D)\) give

\[
 A\le\frac{mD}{N}\sum_{v,i}c_{v,i}
       +2Nm\eta D\sum_{v,i}|c_{v,i}|
       +o(D)+O\!\left(\sum d_j\right)
       \le-\frac{\rho mD}{2N}.
 \tag{12.25}
\]

First take \(Q_1\) large to control the fixed-factor term, then \(D\) large to control the floor error; the strict choice of \(\eta\) leaves room for both.

But \(T\) has integer coefficients, and every \(x_j'\) is integral outside \(S\). Since its value is nonzero, the product formula gives \(\sum_{v\in S}\log|T(x_1',\ldots,x_m')|_v\ge0\). The height of each full transformed coefficient vector is \(O(\sum d_j)\), by Lemma 12.8. Summing the local triangle inequalities, including the archimedean number of monomials, therefore gives

\[
                        A\ge-C\sum d_j
                             \ge-\frac{CmD}{\log Q_1}.
 \tag{12.26}
\]

The constant is independent of the \(Q_j\) and \(D\). Choose \(\log Q_1>4NC/\rho\). Equations (12.25)–(12.26) contradict each other. The assumed infinite family cannot exist. \(\square\)

## 8. The Subspace theorem

### Lemma 12.12. A simultaneous change of basis

At each \(v\in S\), let \(A_{v,1},\ldots,A_{v,N}\) be independent \(K_v\)-linear forms. Suppose a \(K\)-basis \(x_1,\ldots,x_N\) satisfies

\[
 |A_{v,i}(x_j)|_v\le\mu_{v,j},\qquad
           0<\mu_{v,1}\le\cdots\le\mu_{v,N}.
\]

There are an upper triangular \(\mathcal O_{K,S}\)-change of basis with diagonal entries one, giving \(u_j=x_j+\sum_{i<j}\xi_{ji}x_i\), and a permutation \(\pi_v\) at each place, such that

\[
 |A_{v,\pi_v(i)}(u_j)|_v\le
 \begin{cases}
 C\min(\mu_{v,i},\mu_{v,j}),&v\mid\infty,\\
 \min(\mu_{v,i},\mu_{v,j}),&v\nmid\infty.
 \end{cases}
 \tag{12.27}
\]

The constant depends only on \(K,S,N\), so it remains uniform when the forms are rescaled.

**Proof.** We first justify the approximation used in the basis change. Given arbitrary \(\gamma_v\in K_v\) for \(v\in S\), there is \(\xi\in\mathcal O_{K,S}\) with \(|\xi-\gamma_v|_v\le1\) at finite places and with uniformly bounded error at infinite places. At the finite places clear denominators by an element supported on the primes in \(S\), then use the Chinese remainder theorem in \(\mathcal O_K\). Such a clearing element exists because a power of each relevant prime ideal is principal. After obtaining the finite-place approximation, subtract an element of \(\mathcal O_K\) to bring the archimedean error into a fixed fundamental parallelepiped of \(j(\mathcal O_K)\). This leaves the finite-place error integral. The number-field foundations are Discrete valuation rings and Dedekind domains, Theorem 3.2 and Proposition 3.3 on fractional-ideal factorization and the Chinese remainder theorem, and Finiteness of the class number, Corollary 8.2, together with the covolume provider already specified in Lemma 12.5. 

Now induct on \(N\). On the span of the first \(N-1\) vectors the \(N\) forms have one linear dependence. Normalize its largest coefficient to one and remove that form. The remaining restrictions are independent; the other dependence coefficients have absolute value at most one at that place. Apply induction to those restrictions.

At each place solve for a linear combination of the first \(N-1\) new vectors that cancels the remaining restricted forms on \(x_N\). Approximate the \(N-1\) local coefficients simultaneously by \(S\)-integers as above. Each residual restricted form is a sum of bounded coefficient errors times values bounded by \(\min(\mu_{v,i},\mu_{v,j})\), hence by a fixed multiple of \(\mu_{v,i}\) at infinite places and by \(\mu_{v,i}\) at finite places. For the removed form, its value on the first \(N-1\) vectors follows from the normalized dependence. On the new last vector subtract that same dependence: its residual equals its residual on \(x_N\), plus the already controlled restricted values. These are bounded by a fixed multiple of \(\mu_{v,N}\), or by \(\mu_{v,N}\) in the ultrametric case. This proves all entries of (12.27). Every constant used is a dimension factor or a fixed approximation constant, independent of the forms. \(\square\)

### Theorem 12.13. The projective Subspace theorem

Let \(K\) be a number field, \(N\ge2\), \(S\) a finite set of its places, and \(\varepsilon>0\). For each \(v\in S\) let \(L_{v,1},\ldots,L_{v,N}\) be independent linear forms with algebraic coefficients, evaluated using a fixed extension of \(|\cdot|_v\) to those coefficients. The points \([x]\in\mathbb P^{N-1}(K)\) satisfying

\[
       \prod_{v\in S}\prod_{i=1}^N
           \frac{|L_{v,i}(x)|_v}{\|x\|_v}
                    <H([x])^{-N-\varepsilon}
       \tag{12.28}
\]

lie in finitely many proper \(K\)-linear subspaces.

**Proof for coefficients in \(K\).** Enlarge \(S\) to include all infinite places and to make \(\mathcal O_{K,S}\) principal. Finiteness of the class group permits this last enlargement by inverting representatives of its generators. At added places use the coordinate forms; their product divided by the coordinate maximum to the power \(N\) is at most one. Thus enlargement retains every solution of the original inequality.

Choose primitive \(S\)-integral coordinates for each point by dividing by the generator of its coordinate ideal. Then \(\|x\|_v=1\) outside \(S\), and (12.28) becomes

\[
                         \prod_{v\in S,i}|L_{v,i}(x)|_v
                                  <H([x])^{-\varepsilon}.
                         \tag{12.29}
\]

Use the \(S\)-unit logarithmic lattice to balance these coordinates. If \(a_v=\log\|x\|_v\) and \(h=h([x])\), approximate the vector \((h/|S|-a_v)_{v\in S}\), whose coordinates sum to zero, by the logarithms of an \(S\)-unit. The resulting representative has affine height at most \(h+C\), since each of its local log norms is at least \(-C\). This multiplication preserves (12.29).

Solutions with some \(L_{v,i}(x)=0\) already lie in the corresponding finite family of hyperplanes. For the rest, the scalar height estimate gives \(|\log|L_{v,i}(x)|_v|\le h+C'\). Bounded \(h\) gives only finitely many projective points, by Northcott. For large \(h\), the vectors \((\log|L_{v,i}(x)|_v/h)_{v,i}\) belong to a fixed bounded cube. Subdivide it into finitely many boxes of side less than \(\varepsilon/(2N|S|)\), and take each upper corner as \((c_{v,i})\). Equation (12.29) gives \(\sum c_{v,i}\le-\varepsilon/2\). Every solution lies in \(\Pi(H([x]))\) for one of these finitely many fixed families. We prove the assertion for one such family, writing \(\rho=\varepsilon/2\).

Let \(R\) be the rank of \(\Pi(Q)\). Lemma 12.5 gives \(\lambda_N\gg Q^{\rho/N}\), so \(R\le N-1\) for large \(Q\). If \(R=0\) there is no solution vector. For \(R\ge1\), choose \(k\in[R,N-1]\) minimizing \(\lambda_k/\lambda_{k+1}\). Since \(\lambda_R\le1\),

\[
             \lambda_k/\lambda_{k+1}\ll Q^{-\rho/(N(N-1))}.
             \tag{12.30}
\]

Choose vectors realizing the minima and apply Lemma 12.12 after multiplying each \(L_{v,i}\) by a local scalar of absolute value \(Q^{-c_{v,i}}\), with \(\mu_{v,j}=\lambda_j^{d_v/d}\) at infinite places and \(\mu_{v,j}=1\) at finite places. At an infinite place the scalar's ordinary modulus is \(Q^{-dc_{v,i}/d_v}\). At a finite place use the reciprocal of the rounded radius. This changes only bounded factors in subsequent volume comparisons.

Put \(r=N-k\) and \(M=\binom Nr\). In \(\bigwedge^rK^N\), use the exterior forms
\(L_{v,\pi_v(i_1)}\wedge\cdots\wedge L_{v,\pi_v(i_r)}\).
The determinant expansion of (12.27) bounds each of their values on a basis wedge by its natural radius

\[
                  C\,Q^{\sum_{i\in I}c_{v,\pi_v(i)}}
                         \prod_{i\in I}\mu_{v,i}
\]

at an infinite place, and the same radius without \(C\) or the \(\mu\)-factor at a finite place. For \(I_0=\{k+1,\ldots,N\}\), every basis wedge except \(u_{k+1}\wedge\cdots\wedge u_N\) gains the additional factor \(\mu_{v,k}/\mu_{v,k+1}\): its index set contains an index at most \(k\), so in each determinant term the corresponding minimum replaces at least one factor \(\mu_{v,k+1}\).

Define a new box using these radii, with that extra factor on coordinate \(I_0\). It contains the \(M-1\) independent basis wedges other than the excluded one. Each original index occurs in \(b=\binom{N-1}{r-1}\) exterior coordinates. Therefore its volume satisfies

\[
 \operatorname{vol}(\Pi'(Q))^{1/d}
   \asymp \frac{\lambda_k}{\lambda_{k+1}}
       \left(\prod_j\lambda_j\,\operatorname{vol}(\Pi(Q))^{1/d}\right)^b
   \ll Q^{-\rho/(N(N-1))},
 \tag{12.31}
\]

by (12.16). Applying that comparison in dimension \(M\), the last minimum is greater than one for large \(Q\), while the first \(M-1\) are at most one. Thus this box has rank exactly \(M-1\).

To use Proposition 12.11 its exponents must be fixed. The minima satisfy \(Q^{-C}\ll\lambda_j\ll Q^C\). For the lower bound use one nonzero coordinate of a lattice vector, its finite-place bounds, and the product formula. For the upper bound multiply the standard coordinate vectors by a rational integer, with prime powers at the finite places in \(S\), large enough to meet all finite radii; its size and the required archimedean dilation are powers of \(Q\). These arguments give uniform \(C\) for the fixed original box.

Consequently the logarithms of the new radii divided by \(\log Q\) belong to a fixed bounded cube. Freeze \(k\) and the finitely many permutations, and subdivide the remaining cube into a sufficiently fine finite grid. Round each exponent upwards. The enlarged box still contains the \(M-1\) wedges, and the increase in its total exponent can be chosen less than \(\rho/(2N(N-1))\). Equation (12.31) leaves its total exponent strictly negative. Its rank remains exactly \(M-1\), by the same minimum argument. Proposition 12.11 now gives finitely many hyperplane spans for these enlarged boxes.

Their spans are precisely the spans of the \(M-1\) included wedges. Under the perfect pairing
\(\bigwedge^kK^N\times\bigwedge^{N-k}K^N\to\bigwedge^NK^N\),
such a hyperplane annihilates the line generated by \(u_1\wedge\cdots\wedge u_k\). It therefore determines the proper space \(W_k=\operatorname{span}_K(u_1,\ldots,u_k)\): this is the set of \(z\) with \(z\wedge(u_1\wedge\cdots\wedge u_k)=0\). Finitely many exterior hyperplanes give finitely many \(W_k\). Since \(k\ge R\), every vector of the original box lies in \(W_k\). Bounded \(Q\) contributes finitely many vectors, which can also be covered by proper subspaces. This proves (12.28) for \(K\)-coefficients.

**Algebraic coefficients.** Choose a finite Galois extension \(E/K\) containing every coefficient. For each \(v\in S\), fix the place of \(E\) inducing the chosen extension of \(|\cdot|_v\). At every other place \(w\mid v\), conjugate the coefficients so that their \(w\)-values agree with that chosen extension, with exponent
\(\tau_w=[E_w:K_v]/[E:K]\).
For \(x\in K^N\), the product over \(w\mid v\) of the normalized local factors is exactly the original \(v\)-factor, since \(\sum_{w\mid v}\tau_w=1\). The absolute projective height is unchanged by field extension. Apply the proved theorem over \(E\). The intersection of a proper \(E\)-hyperplane with \(K^N\) is a proper \(K\)-subspace: expand its nonzero coefficient vector in a \(K\)-basis of \(E\) to obtain at least one nonzero \(K\)-linear equation. Finitely many such intersections prove the assertion. \(\square\)

### Corollary 12.14. The \(S\)-integral form

If \(S\) contains the infinite places, all \(x\in\mathcal O_{K,S}^N\setminus\{0\}\) with

\[
                     \prod_{v\in S,i}|L_{v,i}(x)|_v<H([x])^{-\varepsilon}
                     \tag{12.32}
\]

lie in finitely many proper \(K\)-subspaces. Indeed \(\prod_{v\in S}\|x\|_v\ge H([x])\), because outside \(S\) the coordinate norm is at most one. Divide (12.32) by the \(N\)-th power of this product and apply (12.28). For primitive integer coordinates over \(\mathbb Q\), \(H([x])=\max|x_i|\). Common integer multiples are treated by the same subspaces, as required by the homogeneous theorem.

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
- Shivani Goel, Rashi Lunia and Anwesh Ray, [*Diophantine approximation and the subspace theorem*](https://arxiv.org/pdf/2502.00731v2), arXiv:2502.00731v2, 21 July 2026: Lemma 3.9, PDF pp. 21–24; Theorems 4.3–4.4 and Proposition 4.5, pp. 27–28; §§4.3–5.3, pp. 29–52. The [version-specific arXiv record](https://arxiv.org/abs/2502.00731v2) supplies its CC BY 4.0 licence. Sections 6–8 adapt the index, auxiliary-polynomial and exterior-power method under that licence. The successive-minima proof is supplied in section 5; the specialization index inequality, finite exceptional-family selection, integer-grid argument and local-radius rounding are explicit in the text.
- M. Waldschmidt, [*Diophantine approximation, irrationality and transcendence*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/IMPA2010Cours4.pdf), IMPA course notes, Course 4 (2010), §4.1.3, Theorems 46–49: Roth's theorem, Ridout's theorem for denominators composed of finitely many primes, and Schmidt's Subspace theorem with finitely many places.
- J.-H. Evertse, [*Diophantine Approximation*, Chapter 7: The Subspace Theorem](https://pub.math.leidenuniv.nl/~evertsejh/dio19-7.pdf), Leiden course notes, Theorem 7.1 and Corollary 7.2, for the classical Subspace theorem and its consequence for Roth's theorem.
- J.-H. Evertse, [*Diophantine Approximation*, Chapter 6: Approximation of algebraic numbers by rationals](https://pub.math.leidenuniv.nl/~evertsejh/dio19-6.pdf), Leiden course notes: Theorems 6.2–6.3 and Corollary 6.4 for Roth's theorem, squarefree binary forms and Thue equations; Theorem 6.5 for Fel'dman's effective improvement of Liouville's inequality; §6.2, Theorem 6.14 and Exercise 6.8, for the gap principle and the counting of exceptional approximations.

Original material outside sections 6–8 is dedicated under CC0. The adapted sections 6–8 are CC BY 4.0, with Goel, Lunia and Ray credited above and the changes identified; that notice applies in the Markdown, LaTeX and reading editions.

J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, July 19, 2020, Proposition 4.26, proves the lattice and discriminant covolume formula for ideals under the real-coordinate Minkowski embedding. This gives a parallel treatment of the normalization used in the number-field prerequisites of Section 7.
