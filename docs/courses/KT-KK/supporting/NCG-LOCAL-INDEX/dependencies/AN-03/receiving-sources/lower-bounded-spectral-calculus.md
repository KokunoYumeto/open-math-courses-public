# Spectral measures with the original operator domain retained

**AN-03 · Prerequisite companion AN03-P005.**

A sharp spectral cutoff can be constructed without an eigenbasis. This companion builds the scalar measures, the bounded positive-operator calculus, and the exact passage back to a lower-bounded self-adjoint operator. Every product keeps its actual operator domain. The construction applies to the unchanged weighted Hilbert space in the elliptic course, including noncompact domains.

The first two parts supply the measure and Hilbert foundations used by the operator proof. The third constructs the full calculus from positive Bernstein polynomial weights. The fourth recovers the original lower-bounded operator, its recursive powers, and both endpoints of a sharp cutoff. The final part gives continuous and atomic models with complete domain calculations. Inner products are linear in the first variable throughout.

## AN03-SPC-001 — Constructing the scalar measure from a positive functional

The space throughout is \(K=[0,1]\), with its usual metric and relative topology. All Borel sets and all supports below are relative to \(K\). A positive complex-linear functional means a complex-linear map \(L:C(K;\mathbb C)\to\mathbb C\) such that \(L(f)\) is a nonnegative real number whenever \(f\) is real and nonnegative. Inner products and all sesquilinear forms are linear in their first argument and conjugate-linear in their second argument.

This proof constructs the measure, proves countable additivity and regularity, develops the integration facts used, and then proves the exact complex-measure statements for operator pairings. Its measure-theoretic input is set theory and elementary compactness of the interval; it does not use a representation theorem or a spectral theorem. Completeness of a Hilbert space is used only in the final operator-representation step, whose proof is also included.

### IPM-001. Positivity and the mass constant

Let \(L\) be positive, and put \(M=L(1)\geq0\). For real continuous \(u\), the functions \(u_+=\max(u,0)\) and \(u_-=\max(-u,0)\) are continuous and nonnegative, so \(L(u)=L(u_+)-L(u_-)\) is real. Consequently \(L(\overline f)=\overline{L(f)}\) for complex continuous \(f\). If \(u\leq v\) are real, positivity gives \(L(u)\leq L(v)\).

For complex \(f\), if \(L(f)\ne0\), choose a scalar \(\zeta\) of modulus one with \(\zeta L(f)=|L(f)|\). Then \(\operatorname{Re}(\zeta f)\leq|f|\) pointwise, and complex linearity and the preceding real-valued property give

\[
|L(f)|=L(\operatorname{Re}(\zeta f))\leq L(|f|)\leq M\|f\|_\infty.
\tag{PR1}
\]

The same inequality holds when \(L(f)=0\). Thus positivity implies boundedness, \(\|L\|\leq M\), and evaluation on \(1\) gives \(\|L\|=M\). In particular \(M=0\) implies \(L=0\). This case is included in every construction below.

### IPM-002. Mass assigned to open sets

For each open \(U\subset K\), define

\[
c(U)=\sup\{L(f):f\in C(K;\mathbb R),\ 0\leq f\leq1,\ \operatorname{supp}f\subset U\}.
\tag{PR2}
\]

The zero function is allowed, and the empty support causes no exception. We have \(0\leq c(U)\leq M\), \(c(\varnothing)=0\), \(c(K)=M\), and \(c\) is monotone under inclusion.

We first prove the finite decomposition needed for countable subadditivity. Let \(S\subset\bigcup_{i=1}^rU_i\) be a nonempty compact set, with each \(U_i\) open. Put \(d_i(x)=\operatorname{dist}(x,K\setminus U_i)\) when \(U_i\ne K\), and put \(d_i=1\) when \(U_i=K\). These functions are continuous, nonnegative, and positive at exactly the points of \(U_i\). The continuous function \(\max_i d_i\) is positive on \(S\), so its minimum there is positive. Choose \(\delta>0\) smaller than that minimum and also smaller than one. Set

\[
h_i=(d_i-\delta/2)_+,\qquad h_0(x)=\operatorname{dist}(x,S),\qquad
\psi_i=\frac{h_i}{h_0+\sum_{j=1}^rh_j}.
\tag{PR3}
\]

The denominator is positive on \(S\) by the choice of \(\delta\), and positive off \(S\) because \(h_0>0\) there. Thus each \(\psi_i\) is continuous and between zero and one. Its support is contained in the compact set \(\{d_i\geq\delta/2\}\subset U_i\). On \(S\), the sum of the \(\psi_i\) is one.

Suppose that \(U\subset\bigcup_{j=1}^\infty U_j\), with all these sets open, and take an admissible \(f\) in (PR2) for \(U\). If \(f=0\), there is nothing to prove. Otherwise its compact support \(S\) has a finite subcover from the \(U_j\). Apply (PR3) to that subcover and set \(f_i=f\psi_i\). Each \(f_i\) is admissible for its corresponding \(U_i\), and \(\sum_i f_i=f\): on \(S\) the partition sums to one, and off \(S\) the function \(f\) is zero. Therefore

\[
L(f)=\sum_iL(f_i)\leq\sum_{j=1}^\infty c(U_j).
\quad\text{Hence}\quad
c(U)\leq\sum_{j=1}^\infty c(U_j).
\tag{PR4}
\]

For finitely many pairwise disjoint open sets \(U_1,\ldots,U_r\), admissible functions \(f_i\) have disjoint supports, so \(0\leq\sum_i f_i\leq1\) and its support is contained in \(\bigcup_iU_i\). Approximating each supremum in (PR2) within an arbitrarily small positive error gives \(c(\bigcup_iU_i)\geq\sum_i c(U_i)\). Combined with (PR4), this proves equality. For countably many disjoint open sets, monotonicity gives the lower bound by every finite partial sum, while (PR4) gives the upper bound. Thus \(c\) is countably additive on disjoint open unions.

### IPM-003. Outer measure and separation by positive distance

For every subset \(E\subset K\), define

\[
\mu^*(E)=\inf\{c(U):U\subset K\text{ open},\ E\subset U\}.
\tag{PR5}
\]

The family is never empty, since \(K\) is allowed. The function \(\mu^*\) is monotone, vanishes on the empty set, and is at most \(M\). For subsets \(E_j\) and \(\epsilon>0\), choose open \(U_j\supset E_j\) with \(c(U_j)\leq\mu^*(E_j)+\epsilon2^{-j}\), where indices begin at one. By (PR4),

\[
\mu^*\Bigl(\bigcup_jE_j\Bigr)
\leq c\Bigl(\bigcup_jU_j\Bigr)
\leq\sum_j\mu^*(E_j)+\epsilon.
\tag{PR6}
\]

Letting \(\epsilon\downarrow0\) proves countable subadditivity. Thus \(\mu^*\) is an outer measure. For open \(U\), (PR5) and monotonicity of \(c\) show \(\mu^*(U)=c(U)\); in particular \(\mu^*(K)=M\).

If nonempty subsets \(A,B\) have distance \(d>0\), take any open \(U\supset A\cup B\) and form
\(U_A=U\cap\{x:\operatorname{dist}(x,A)<d/3\}\) and
\(U_B=U\cap\{x:\operatorname{dist}(x,B)<d/3\}\).
They are disjoint open supersets of \(A,B\). To see disjointness, a point in both would admit points of \(A,B\) whose distance is less than \(2d/3\) plus arbitrarily small errors, contradicting the definition of \(d\). Open-set additivity and monotonicity give
\(c(U)\geq c(U_A)+c(U_B)\geq\mu^*(A)+\mu^*(B)\).
Take the infimum over \(U\) and use outer subadditivity for the reverse inequality. The result, also immediate if one set is empty, is

\[
\operatorname{dist}(A,B)>0
\quad\Longrightarrow\quad
\mu^*(A\cup B)=\mu^*(A)+\mu^*(B).
\tag{PR7}
\]

### IPM-004. Borel measurability and countable additivity

Call a set \(A\subset K\) measurable for \(\mu^*\) when, for every subset \(E\subset K\),

\[
\mu^*(E)=\mu^*(E\cap A)+\mu^*(E\setminus A).
\tag{PR8}
\]

First every closed set \(F\) satisfies (PR8). The cases \(F=\varnothing,K\) are immediate. Otherwise the function \(d_F(x)=\operatorname{dist}(x,F)\) is continuous and satisfies \(|d_F(x)-d_F(y)|\leq|x-y|\), by the triangle inequality and taking infima. Fix any subset \(E\), and put

\[
E_i=\{x\in E:d_F(x)\geq1/i\},\qquad
A_j=\{x\in E:1/(j+1)\leq d_F(x)<1/j\}.
\tag{PR9}
\]

The set \(E_i\) has distance at least \(1/i\) from \(E\cap F\). Hence (PR7) and monotonicity give
\(\mu^*(E)\geq\mu^*(E\cap F)+\mu^*(E_i)\).
The sets \(A_j\) with indices of one fixed parity are separated from one another by positive distance in each finite collection: for indices \(j,j+2\), the gap between the indicated distance intervals is at least \(1/(j+1)-1/(j+2)>0\), and the distance function is 1-Lipschitz. Iterating (PR7) over a finite collection of even indices, and then over odd indices, shows that each of the two series of their outer masses has sum at most \(M\). Therefore \(\sum_{j\geq1}\mu^*(A_j)\) converges and its tails tend to zero.

The set \(E\setminus F\) is contained in \(E_i\cup\bigcup_{j\geq i}A_j\). Outer subadditivity now gives

\[
\mu^*(E\setminus F)
\leq\mu^*(E_i)+\sum_{j\geq i}\mu^*(A_j).
\tag{PR10}
\]

Combining the preceding two inequalities and letting \(i\to\infty\) proves
\(\mu^*(E)\geq\mu^*(E\cap F)+\mu^*(E\setminus F)\).
Outer subadditivity gives the opposite inequality. This proves (PR8) for every closed \(F\), without assuming continuity from below for an outer measure.

Here is the complete algebra argument for the measurable sets. Complementation preserves (PR8). If \(A,B\) satisfy (PR8), split \(E\) first by \(A\), then split \(E\setminus A\) by \(B\). This gives
\(\mu^*(E)=\mu^*(E\cap A)+\mu^*((E\setminus A)\cap B)+\mu^*(E\setminus(A\cup B))\).
The first two terms are at least \(\mu^*(E\cap(A\cup B))\) by subadditivity. Together with the reverse subadditivity bound, this proves (PR8) for \(A\cup B\). Thus the measurable sets form an algebra.

For pairwise disjoint measurable \(A_j\), repeated splitting gives, with \(A=\bigcup_jA_j\),

\[
\mu^*(E)\geq\sum_{j=1}^r\mu^*(E\cap A_j)+\mu^*(E\setminus A)
\qquad(r\geq1).
\tag{PR11}
\]

Let \(r\to\infty\). The sum is at least \(\mu^*(E\cap A)\) by countable subadditivity. Again the reverse inequality is automatic, so \(A\) is measurable. Any countable union can be made disjoint by replacing its terms by their differences from the finite preceding union; those differences belong to the algebra. Consequently the measurable sets form a sigma-algebra. Since they contain every closed set, they contain every Borel set.

For disjoint measurable \(A_j\), take \(E=\bigcup_jA_j\) in (PR11) and compare with countable subadditivity. The result is exact countable additivity. Restriction to Borel sets therefore gives a finite positive Borel measure

\[
\mu(E)=\mu^*(E)\quad(E\text{ Borel}),\qquad
\mu(K)=M,\qquad \mu(U)=c(U)\quad(U\text{ open}).
\tag{PR12}
\]

No representation or integration theorem has been used to obtain this measure.

### IPM-005. Outer and inner regularity

Equation (PR5), together with (PR12), gives for every Borel set \(E\)

\[
\mu(E)=\inf_{U\supset E,\ U\text{ open}}\mu(U).
\tag{PR13}
\]

To prove inner regularity, choose open \(V\supset K\setminus E\) with
\(\mu(V)<\mu(K\setminus E)+\epsilon\), and put \(F=K\setminus V\).
Then \(F\) is compact and contained in \(E\). Finite additivity on the disjoint parts of \(V\) gives
\(\mu(E\setminus F)=\mu(E\cap V)=\mu(V)-\mu(K\setminus E)<\epsilon\).
It follows that

\[
\mu(E)=\sup_{F\subset E,\ F\text{ compact}}\mu(F).
\tag{PR14}
\]

Both inequalities also hold for empty sets and for zero mass. This is the claimed regularity on every Borel set, rather than only on open sets.

### IPM-006. Integration and the convergence statements actually used

The following construction and proofs apply to any finite positive measure \(\rho\) on a sigma-algebra, including \(\mu\) on the Borel sets. A nonnegative simple function can be written as \(s=\sum_{i=1}^ra_i1_{E_i}\) with disjoint measurable \(E_i\) and \(a_i\geq0\). Define \(\int s\,d\rho=\sum_i a_i\rho(E_i)\). Refining two finite partitions by their intersections proves independence of the representation, additivity for simple functions, and monotonicity. For a nonnegative measurable function \(f\), define

\[
\int f\,d\rho=\sup\{\int s\,d\rho:0\leq s\leq f,\ s\text{ simple}\}.
\tag{PR15}
\]

Countable additivity first implies continuity from below for sets. If \(E_k\uparrow E\), the disjoint sets \(E_1,E_2\setminus E_1,\ldots\) partition \(E\), so \(\rho(E_k)\uparrow\rho(E)\). Taking complements inside a set of finite mass also proves continuity from above.

If \(0\leq f_k\uparrow f\), monotonicity gives \(\lim_k\int f_k\leq\int f\). For the reverse inequality, take a nonnegative simple \(s\leq f\) and \(0<c<1\). On every point where \(s>0\), the increasing sequence \(f_k\) eventually exceeds \(cs\). Thus the sets \(E_k=\{f_k\geq cs\}\) increase to the entire underlying space (points where \(s=0\) already belong to every \(E_k\)). Continuity from below for each set in the finite simple partition gives \(\int s1_{E_k}\to\int s\), while \(f_k\geq cs1_{E_k}\). Hence \(\lim_k\int f_k\geq c\int s\). Take the supremum over \(s\) and then let \(c\uparrow1\). This proves monotone convergence, including infinite integrals:

\[
0\leq f_k\uparrow f\quad\Longrightarrow\quad
\int f_k\,d\rho\uparrow\int f\,d\rho.
\tag{PR16}
\]

Every nonnegative measurable \(f\) has the increasing simple approximants
\(s_k=2^{-k}\lfloor2^k\min(f,k)\rfloor\).
They are simple because the cap is finite, are measurable because their level sets are measurable, are increasing because the caps increase and each grid refines its predecessor, and tend pointwise to \(f\). Applying (PR16) to these approximants for \(f\), \(g\), and their sums proves
\(\int(f+g)=\int f+\int g\). Positive homogeneity follows in the same way or directly from (PR15).

For real \(f\) with \(\int|f|<\infty\), define \(\int f=\int f_+-\int f_-\). To prove additivity for real integrable \(f,g\), use the pointwise identity
\(f_++g_++(f+g)_-=f_-+g_-+(f+g)_+\).
All terms have finite integrals because \(|f+g|\leq|f|+|g|\); additivity for nonnegative functions and rearrangement therefore give \(\int(f+g)=\int f+\int g\). Positive homogeneity is already proved, and \((-f)_+=f_-\), \((-f)_-=f_+\) proves the negative-scalar case. For complex integrable \(f\), define its integral by its real and imaginary parts; real linearity and multiplication by \(i\) prove complex linearity. If its integral is nonzero, multiply by a constant phase making that integral positive real and use \(\operatorname{Re}(\zeta f)\leq|f|\), as in (PR1). This proves

\[
\left|\int f\,d\rho\right|\leq\int|f|\,d\rho.
\tag{PR17}
\]

Fatou's inequality follows directly from (PR16): for nonnegative measurable \(f_k\), set \(h_j=\inf_{k\geq j}f_k\). These measurable functions increase to \(\liminf f_k\), and \(\int h_j\leq\inf_{k\geq j}\int f_k\). Therefore

\[
\int\liminf_k f_k\,d\rho\leq\liminf_k\int f_k\,d\rho.
\tag{PR18}
\]

If complex measurable \(f_k\to f\) pointwise and \(|f_k|\leq g\) with \(\int g<\infty\), then \(|f|\leq g\). Apply (PR18) to the nonnegative functions \(2g-|f_k-f|\), whose limit is \(2g\). Their integrals are \(2\int g-\int|f_k-f|\), so the resulting inequality forces \(\limsup_k\int|f_k-f|\leq0\). Thus

\[
\int|f_k-f|\,d\rho\longrightarrow0,
\qquad
\int f_k\,d\rho\longrightarrow\int f\,d\rho.
\tag{PR19}
\]

The same proof applies to convergence outside a measurable null set by changing the functions to zero there. In particular, on a finite measure space, pointwise convergence of a uniformly bounded sequence of bounded Borel functions implies convergence of their integrals. All monotone and dominated convergence uses below refer to the proofs (PR16)–(PR19), not to a spectral-theoretic convergence assertion.

### IPM-007. Recovery of the original functional

Let \(f\in C(K;\mathbb R)\) be nonnegative, and let \(B=\|f\|_\infty\). If \(B=0\), the assertion is immediate. Otherwise fix \(\delta>0\), let \(r=\lceil B/\delta\rceil\), and put \(U_i=\{f>i\delta\}\), \(1\leq i\leq r\). For each \(i\), choose any function \(g_i\) admissible in (PR2) for \(U_i\). At a point \(x\), the number of indices with \(g_i(x)>0\) is at most the number of positive integers \(i\) for which \(i\delta<f(x)\). Therefore
\(0\leq\delta\sum_i g_i(x)\leq f(x)\).
Positivity and approximation of the finitely many suprema give

\[
L(f)\geq\delta\sum_{i=1}^r c(U_i)
=\int s_\delta\,d\mu,
\qquad
s_\delta=\delta\sum_{i=1}^r1_{\{f>i\delta\}}.
\tag{PR20}
\]

The approximation step is finite: choose each \(L(g_i)\) within \(\epsilon/(r\delta)\) of \(c(U_i)\), and then let \(\epsilon\downarrow0\). Pointwise \(0\leq f-s_\delta\leq\delta\), including values of \(f\) that are exact multiples of \(\delta\). By the integration facts already proved,
\(\int s_\delta\geq\int f-\delta M\).
Let \(\delta\downarrow0\); then \(L(f)\geq\int f\).

Apply this same inequality to the nonnegative continuous function \(B-f\). Since \(\mu(K)=M=L(1)\), it gives
\(BM-L(f)\geq BM-\int f\), hence \(L(f)\leq\int f\). Equality follows. Real continuous functions are differences of their continuous positive and negative parts, and complex continuous functions have real and imaginary parts. Linearity therefore proves

\[
L(f)=\int_K f\,d\mu\quad(f\in C(K;\mathbb C)),
\qquad \mu(K)=L(1).
\tag{PR21}
\]

This proves existence of the representing finite positive regular Borel measure for every positive bounded complex-linear functional.

### IPM-008. Uniqueness and lower semicontinuous approximation

For an open proper nonempty \(U\subset K\), the continuous functions
\(g_k(x)=\min(1,(k\operatorname{dist}(x,K\setminus U)-1)_+)\)
increase to \(1_U\). They are between zero and one, and each support lies in
\(\{x:\operatorname{dist}(x,K\setminus U)\geq1/k\}\subset U\).
For \(U=K\) use the constant sequence one, and for \(U=\varnothing\) use zero. If another finite positive Borel measure \(\nu\) has the integrals (PR21), monotone convergence for both measures gives
\(\nu(U)=\lim_k\int g_k\,d\nu=\lim_kL(g_k)=\mu(U)\).

We give the elementary set argument extending this equality to all Borel sets. A family \(\mathcal D\) containing \(K\), closed under complements in \(K\), and closed under disjoint countable unions is called a lambda-system. It is also closed under differences \(A\setminus B\) when \(B\subset A\) and both sets belong to it: take the complement of the disjoint union \((K\setminus A)\cup B\). A family \(\mathcal P\) closed under finite intersections is a pi-system. If a lambda-system contains a pi-system \(\mathcal P\) that contains \(K\), it contains the sigma-algebra generated by \(\mathcal P\). Here is a proof. Let \(\mathcal D_0\) be the smallest lambda-system containing \(\mathcal P\). For fixed \(A\in\mathcal P\), the sets \(B\) satisfying \(A\cap B\in\mathcal D_0\) form a lambda-system: the complement step uses the nested-difference property inside \(A\). This lambda-system contains \(\mathcal P\), so it contains \(\mathcal D_0\). Next fix \(B\in\mathcal D_0\) and repeat the argument with the sets \(A\) satisfying \(A\cap B\in\mathcal D_0\). The first step shows this new lambda-system contains \(\mathcal P\), hence \(\mathcal D_0\). Thus \(\mathcal D_0\) is closed under finite intersections. Complements and finite intersections give finite unions and differences, and disjointizing any countable union then proves it is a sigma-algebra. This proves the assertion.

The Borel sets \(E\) with \(\mu(E)=\nu(E)\) form a lambda-system: total masses agree, complementation subtracts from that common finite mass, and disjoint countable unions use countable additivity. The open sets are a pi-system containing \(K\) and generating the Borel sigma-algebra. The preceding argument proves \(\mu=\nu\) on every Borel set. No regularity assumption on the competing measure was needed.

For later use, let \(f:K\to[0,B]\) be lower semicontinuous. For every positive integer \(k\), set

\[
f_k(x)=\inf_{y\in K}\bigl(f(y)+k|x-y|\bigr).
\tag{PR22}
\]

The infimum is attained: a minimizing sequence has a convergent subsequence in compact \(K\), and lower semicontinuity gives a minimizing limit. The inequality
\(\big||x-y|-|x'-y|\big|\leq|x-x'|\)
implies \(|f_k(x)-f_k(x')|\leq k|x-x'|\) by comparing infima in both directions. Thus \(f_k\) is continuous. It satisfies \(0\leq f_k\leq f\) and increases with \(k\). If \(y_k\) is a minimizer for a fixed \(x\), then \(k|x-y_k|\leq f_k(x)\leq f(x)\leq B\), so \(y_k\to x\). Lower semicontinuity yields
\(\liminf_k f_k(x)\geq\liminf_k f(y_k)\geq f(x)\).
Together with \(f_k\leq f\), this proves \(f_k\uparrow f\). Lower semicontinuity makes \(f\) Borel because its strict upper level sets are open. Consequently, by (PR16),

\[
\int f\,d\mu
=\sup\{L(g):g\in C(K;\mathbb R),\ 0\leq g\leq f\}.
\tag{PR23}
\]

The inequality from right to left is monotonicity; the reverse inequality follows by choosing the functions (PR22).

### IPM-009. Finite complex measures, variation, and integration

The complex measures needed here will be finite linear combinations
\(\nu=\sum_{r=1}^sc_r\rho_r\)
of finite positive Borel measures. They are countably additive because every summand is. Define the positive measure \(\lambda=\sum_r|c_r|\rho_r\); then \(|\nu(E)|\leq\lambda(E)\). Define total variation by finite measurable partitions:

\[
|\nu|(E)=\sup\Bigl\{\sum_{j=1}^r|\nu(E_j)|:
 E=\bigsqcup_{j=1}^rE_j,\ E_j\text{ Borel}\Bigr\}.
\tag{PR24}
\]

It satisfies \(|\nu|(E)\leq\lambda(E)\). It is a measure, as follows directly. For disjoint Borel sets \(E_i\) and \(E=\bigcup_iE_i\), combine near-maximizing finite partitions of the first finitely many \(E_i\), together with the remaining subset of \(E\), to obtain
\(|\nu|(E)\geq\sum_{i=1}^r|\nu|(E_i)\) for every \(r\).
In the other direction, for any finite partition \(E=\bigsqcup_jF_j\), countable additivity and triangle inequality give
\(\sum_j|\nu(F_j)|\leq\sum_i\sum_j|\nu(F_j\cap E_i)|\leq\sum_i|\nu|(E_i)\).
Take the supremum over the partition and then let \(r\to\infty\) in the first inequality. This proves countable additivity of \(|\nu|\).

For complex simple \(s=\sum_jz_j1_{E_j}\) on a finite disjoint partition, define \(\int s\,d\nu=\sum_jz_j\nu(E_j)\). Refinement proves independence of the partition, and (PR24) gives
\(|\int s\,d\nu|\leq\int|s|\,d|\nu|\).
Every bounded complex Borel function has uniformly convergent simple approximants, obtained by rounding its real and imaginary parts to successively finer finite grids on their bounded ranges. The preceding inequality makes their integrals Cauchy, with a limit independent of the approximating sequence. This defines \(\int f\,d\nu\), proves linearity, and gives

\[
\left|\int f\,d\nu\right|\leq\int|f|\,d|\nu|,
\qquad
\int f\,d\nu=\sum_{r=1}^sc_r\int f\,d\rho_r
\quad(f\text{ bounded Borel}).
\tag{PR25}
\]

Both assertions follow first for simple functions, then by uniform approximation; \(\big||s|-|f|\big|\leq|s-f|\) handles the absolute-value integral. If \(f_k\to f\) pointwise and all functions are uniformly bounded, (PR19) for \(|\nu|\) and (PR25) show convergence of the complex integrals. More generally, if \(|f_k|\leq g\) with \(g\) integrable for \(|\nu|\), define integrals of such functions by truncation; the bound (PR25) makes the truncations Cauchy because the absolute-value tail integrals tend to zero by (PR19). The same bound and (PR19) prove dominated convergence in that case as well.

If the positive measures \(\rho_r\) are regular, so is \(\lambda\): for a Borel \(E\), choose compact subsets \(F_r\subset E\) and open supersets \(U_r\supset E\) making each \(|c_r|\rho_r(U_r\setminus F_r)\) as small as prescribed, ignoring zero coefficients. The compact union \(F=\bigcup_rF_r\) is contained in \(E\), and the open intersection \(U=\bigcap_rU_r\) contains \(E\). Since \(U\setminus F\subset U_r\setminus F_r\) for every \(r\), their weighted sum can be made arbitrarily small. As \(|\nu|\leq\lambda\), the same \(F,U\) prove regularity of \(|\nu|\), and
\(|\nu(E)-\nu(F)|\leq|\nu|(E\setminus F)\),
\(|\nu(U)-\nu(E)|\leq|\nu|(U\setminus E)\)
give the corresponding approximation for \(\nu\).

The uniqueness argument extends to any finite complex Borel measure of finite total variation. Indeed, once finiteness of (PR24) is given, the proof that variation is a measure and the integration construction above apply unchanged; the finite positive-measure decomposition was used to establish finiteness and regularity, not in those subsequent proofs. If \(\int f\,d\nu=0\) for every continuous \(f\), the continuous open-set approximants in IPM-008 and dominated convergence for \(|\nu|\) give \(\nu(U)=0\) for every open \(U\). The family of Borel sets on which \(\nu\) vanishes is a lambda-system, since \(\nu(K)=0\), and countable additivity handles disjoint unions. The pi-system argument already proved therefore gives \(\nu=0\). Applying this to a difference proves uniqueness whenever two finite complex measures have equal continuous integrals.


## AN03-SPC-002 — Complex measure pairings and Hilbert representation

### IPM-010. Polarization with the linear-first convention

Let \(H\) be a complex Hilbert space. Suppose \(F_f(x,y)\), for continuous complex \(f\), is complex-linear in \(f\), linear in \(x\), conjugate-linear in \(y\), and satisfies

\[
F_f(x,x)\geq0\quad\text{when }f\geq0,
\qquad
0\leq F_1(x,x)\leq C\|x\|^2
\quad(x\in H),
\tag{PR26}
\]

for a fixed finite \(C\geq0\). These are precisely the measure-stage hypotheses, for example when \(F_f(x,y)=\langle\Phi(f)x,y\rangle\) and \(\Phi\) is a positive linear map with \(\|\Phi(1)\|\leq C\). A unital continuous \(*\)-homomorphism has \(C=1\): for real \(f\geq0\), its continuous square root gives \(\Phi(f)=\Phi(\sqrt f)^*\Phi(\sqrt f)\geq0\), and \(\Phi(1)=I\).

For each \(x\), IPM-001 and IPM-007 give a unique finite positive regular measure \(\mu_x\) such that

\[
F_f(x,x)=\int f\,d\mu_x,\qquad
\mu_x(K)=F_1(x,x)\leq C\|x\|^2.
\tag{PR27}
\]

For any sesquilinear form \(B\) with the linear-first convention, writing \(q(z)=B(z,z)\) gives the algebraic identity

\[
B(x,y)=\frac14\sum_{k=0}^3i^kq(x+i^ky)
=\frac14\bigl(q(x+y)-q(x-y)+i q(x+iy)-i q(x-iy)\bigr).
\tag{PR28}
\]

This identity does not require \(B\) to be Hermitian. Indeed, for \(t=i^k\),
\(q(x+ty)=q(x)+q(y)+\overline t B(x,y)+tB(y,x)\).
After multiplication by \(t\) and summation, the constant terms vanish because \(\sum t=0\), the \(B(y,x)\) term vanishes because \(\sum t^2=0\), and the \(B(x,y)\) term is multiplied by \(\sum|t|^2=4\). This proves the formula and in particular fixes the plus sign before \(i q(x+iy)\).

Define the finite regular complex measure

\[
\mu_{x,y}=\frac14\bigl(\mu_{x+y}-\mu_{x-y}+i\mu_{x+iy}-i\mu_{x-iy}\bigr).
\tag{PR29}
\]

Equation (PR25), followed by (PR28) applied to \(F_f\), proves

\[
\int f\,d\mu_{x,y}=F_f(x,y)\qquad(f\in C(K;\mathbb C)).
\tag{PR30}
\]

The complex-measure uniqueness proved in IPM-009 now shows that \((x,y)\mapsto\mu_{x,y}\) is sesquilinear as a measure-valued map. For example, the continuous integrals of \(\mu_{ax+bz,y}-a\mu_{x,y}-b\mu_{z,y}\) vanish for all \(f\), so this measure is zero; the second variable is treated with conjugated scalars. The same uniqueness gives \(\mu_{x,x}=\mu_x\). This step proves sesquilinearity of the actual measures; it is not inferred just from the appearance of the polarization expression.

Fix a Borel set \(E\). Then \(B_E(x,y)=\mu_{x,y}(E)\) is a sesquilinear form with nonnegative real diagonal \(B_E(x,x)=\mu_x(E)\). Every such form is Hermitian and satisfies Cauchy–Schwarz. For completeness, reality of \(B_E(x+t y,x+t y)\) for real \(t\) gives that \(B_E(x,y)+B_E(y,x)\) is real; reality for \(it\) gives that \(i(B_E(y,x)-B_E(x,y))\) is real. Together these two equalities imply \(B_E(y,x)=\overline{B_E(x,y)}\). If \(B_E(y,y)>0\), substitute \(t=-B_E(x,y)/B_E(y,y)\) into the nonnegative quadratic expression for \(B_E(x+t y,x+t y)\). Its value is \(B_E(x,x)-|B_E(x,y)|^2/B_E(y,y)\), proving the inequality. If \(B_E(y,y)=0\) and \(B_E(x,y)\ne0\), substituting \(t=-sB_E(x,y)\) with large positive real \(s\) makes that quadratic expression negative, a contradiction. Thus

\[
\mu_{y,x}(E)=\overline{\mu_{x,y}(E)},\qquad
|\mu_{x,y}(E)|^2\leq\mu_x(E)\mu_y(E).
\tag{PR31}
\]

For a finite partition \(E=\bigsqcup_jE_j\), use (PR31), then the finite scalar Cauchy–Schwarz inequality, to obtain
\(\sum_j|\mu_{x,y}(E_j)|\leq\sum_j\sqrt{\mu_x(E_j)\mu_y(E_j)}\leq\sqrt{\mu_x(E)\mu_y(E)}\).
The scalar inequality itself follows from nonnegativity of \(\sum_j|u_j+t v_j|^2\) by the same quadratic minimization just used. Taking the supremum over partitions yields the sharper local variation estimate

\[
|\mu_{x,y}|(E)\leq\sqrt{\mu_x(E)\mu_y(E)},
\qquad
|\mu_{x,y}|(K)\leq C\|x\|\|y\|.
\tag{PR32}
\]

In particular this estimate handles zero vectors and zero diagonal mass exactly, without division by their norms or masses.

### IPM-011. Bounded Borel pairings and their convergence

For bounded complex Borel \(g\), define

\[
B_g(x,y)=\int g\,d\mu_{x,y}.
\tag{PR33}
\]

Measure-valued sesquilinearity and integration linearity show that this is a sesquilinear form. By (PR25) and (PR32),

\[
|B_g(x,y)|\leq C\|g\|_\infty\|x\|\|y\|.
\tag{PR34}
\]

It agrees with \(F_g\) for continuous \(g\), and \(B_g(x,x)=\int g\,d\mu_x\). It is positive when \(g\geq0\), and (PR31) gives
\(B_{\overline g}(x,y)=\overline{B_g(y,x)}\).

One additional estimate is useful for strong convergence. For a simple function \(g=\sum_jz_j1_{E_j}\) on a finite disjoint partition of \(K\), (PR31) and finite Cauchy–Schwarz give
\( |B_g(x,y)|\leq\sum_j|z_j|\sqrt{\mu_x(E_j)\mu_y(E_j)}\leq(\sum_j|z_j|^2\mu_x(E_j))^{1/2}\mu_y(K)^{1/2}\).
Uniform simple approximation extends this to every bounded Borel \(g\): uniform convergence of \(g_j\) implies uniform convergence of \(|g_j|^2\) because the sequence is uniformly bounded. Therefore

\[
|B_g(x,y)|^2\leq\left(\int|g|^2\,d\mu_x\right)\mu_y(K)
\leq C\|y\|^2\int|g|^2\,d\mu_x.
\tag{PR35}
\]

If \(g_k\) are uniformly bounded Borel functions and converge pointwise to \(g\), dominated convergence for \(|\mu_{x,y}|\) proves \(B_{g_k}(x,y)\to B_g(x,y)\) for every \(x,y\). In fact (PR35) applied to \(g_k-g\), with (PR19) for \(\mu_x\), proves

\[
\sup_{\|y\|\leq1}|B_{g_k-g}(x,y)|\longrightarrow0
\qquad(x\in H).
\tag{PR36}
\]

For \(0\leq g_k\uparrow g\) with a common finite bound, (PR16) also gives the increasing convergence \(B_{g_k}(x,x)\uparrow B_g(x,x)\). For bounded nonnegative lower semicontinuous \(g\), the explicit continuous functions (PR22) give
\(B_g(x,x)=\sup\{F_f(x,x):f\in C(K;\mathbb R),0\leq f\leq g\}\)
by (PR23). These conclusions specify the convergence and lower semicontinuous supremum used in the operator application.

### IPM-012. The corresponding bounded operators, with the Hilbert-space step proved

We first prove the Hilbert representation needed to turn (PR33) into an operator. Let \(\ell\) be a bounded conjugate-linear functional on a complex Hilbert space with the linear-first convention. If it is zero, its representing vector is zero. Otherwise \(F(y)=\overline{\ell(y)}\) is a nonzero bounded linear functional. The closed affine set \(A=\{y:F(y)=1\}\) is nonempty and has distance \(d>0\) from the origin, since \(1\leq\|F\|\|y\|\) on it. Choose \(v_k\in A\) with \(\|v_k\|\to d\). Its midpoints remain in \(A\), and the parallelogram identity yields

\[
\|v_k-v_l\|^2
=2\|v_k\|^2+2\|v_l\|^2-4\|(v_k+v_l)/2\|^2
\leq2\|v_k\|^2+2\|v_l\|^2-4d^2\longrightarrow0.
\tag{PR37}
\]

Completeness gives a limit \(v\in A\) of norm \(d\). For every \(w\in\ker F\), the vector \(v+t w\) lies in \(A\) for every complex \(t\). Expanding its squared norm and using the minimality of \(\|v\|\) for real \(t\) and for purely imaginary \(t\) proves \(\langle w,v\rangle=0\). Since \(y-F(y)v\in\ker F\), it follows that
\(\langle y,v\rangle=F(y)\|v\|^2\). Thus
\(\ell(y)=\langle v/\|v\|^2,y\rangle\).
Uniqueness follows by taking \(y\) equal to the difference of two representing vectors. Its norm equals \(\|\ell\|\): Cauchy–Schwarz gives one inequality, and evaluation at the unit vector in the representing vector's direction gives the other. The Cauchy–Schwarz inequality for the Hilbert inner product follows from the positive-form quadratic proof in IPM-010, so no separate representation result is being imported here.

For fixed \(g\) and \(x\), apply this result to \(\ell(y)=B_g(x,y)\). There is a unique vector \(\Psi(g)x\) with

\[
\langle\Psi(g)x,y\rangle=B_g(x,y)=\int g\,d\mu_{x,y}.
\tag{PR38}
\]

Linearity in \(x\) follows from sesquilinearity and uniqueness of the representing vector. The bound (PR34) gives \(\|\Psi(g)\|\leq C\|g\|_\infty\). Linearity in \(g\), positivity for \(g\geq0\), and \(\Psi(\overline g)=\Psi(g)^*\) follow by testing the corresponding vector equalities against every \(y\), using (PR33)–(PR34) and their conjugation identity. If the original pairings came from \(\Phi\), then \(\Psi(f)=\Phi(f)\) for continuous \(f\), by (PR30) and uniqueness. If \(F_1(x,y)=\langle x,y\rangle\), then \(\Psi(1)=I\).

Equation (PR35), followed by the equality between the norm of a vector and the norm of its represented functional, gives

\[
\|\Psi(g)x\|^2\leq C\int|g|^2\,d\mu_x.
\tag{PR39}
\]

Consequently uniformly bounded pointwise convergence of a sequence of Borel functions implies strong operator convergence on each vector, by (PR19):
\(\|\Psi(g_k)x-\Psi(g)x\|^2\leq C\int|g_k-g|^2\,d\mu_x\to0\).
Weak convergence follows as well. All convergence assertions here concern sequences.

The constructed map is the unique linear extension of its continuous-function values that preserves uniformly bounded pointwise sequential convergence in every operator pairing. To prove this, let \(\widetilde\Psi\) be another extension with that convergence property, and fix \(x,y\). The continuous approximants to \(1_U\) in IPM-008 show equality of the two pairings on indicators of open sets. The Borel sets on whose indicators the two pairings agree form a lambda-system: they include \(K\), complementation uses the common value on \(1\), and a disjoint countable union follows from linearity for partial sums of indicators followed by the assumed sequential convergence. The proved pi-system argument extends equality to all Borel indicators. Linearity gives equality on simple functions, and uniform simple approximation, which is in particular uniformly bounded pointwise sequential approximation, gives equality for every bounded Borel function. This is true for every \(x,y\), so the operators agree.

Multiplicativity is a further property when the original continuous map is a homomorphism; no multiplicativity follows from positivity alone, and none is assumed in the construction above. All representation, measure, polarization, variation, bounded-Borel pairing, regularity, uniqueness, and convergence assertions used in (PR38)–(PR39) have been proved here.

## AN03-SPC-003 — The full calculus of a bounded positive contraction

### 1. Foundations and exact statement

Let \(H\) be a complex Hilbert space and let \(S\in\mathcal B(H)\) satisfy
\[
 S=S^*,\qquad (Sx,x)\geq0,\qquad\|S\|\leq1,
 \qquad\ker S=\{0\}.
 \tag{BS1}
\]
Set \(K=[0,1]\). We prove that there is a unique strongly countably additive orthogonal projection-valued measure \(E\) on the Borel subsets of \(K\), with \(E(K)=I\), such that
\[
 S=\int_K t\,dE(t).
 \tag{BS2}
\]
For every bounded Borel function \(f:K\to\mathbb C\) the integral is a bounded operator. For every Borel function finite at each point, including unbounded functions, its closed densely defined integral has exactly the domain
\[
 D(f(S))=\left\{x\in H:\int_K|f|^2\,d\mu_x<\infty\right\},
 \quad\mu_x(B)=(E(B)x,x),
 \quad\|f(S)x\|^2=\int_K|f|^2\,d\mu_x.
 \tag{BS3}
\]
We prove all adjoint and product domains and \(E(\{0\})=0\). No claim that \(S\geq cI\) for a positive \(c\) is made.

The scalar interval measure theorem, integration, convergence and finite complex-measure uniqueness are proved in AN03-SPC-001. The representation of bounded Hilbert functionals is proved in AN03-SPC-002. The remaining foundations are the Hilbert-space axioms, completeness of bounded operators in operator norm, and the elementary algebra and compactness used below.

Every finite positive Borel measure \(\nu\) on the interval is regular: apply the already proved representation theorem to \(f\mapsto\int f\,d\nu\); its regular representing measure agrees with \(\nu\) by IPM-008, whose uniqueness proof does not assume regularity of the competing measure. If \(\mu\) is a finite complex measure of finite variation and \(f\) is bounded Borel, the set function \(f\mu:B\mapsto\int_B f\,d\mu\) is countably additive. Indeed the finite partial-union indicators converge boundedly pointwise, and dominated convergence for \(|\mu|\) passes the integrals to the union. Finite partitions give
\[
 |f\mu|(B)\leq\int_B|f|\,d|\mu|
                \leq\|f\|_\infty|\mu|(B).
\]
The finite positive measure \(|\mu|\) is regular by the preceding argument. Given a Borel \(B\), choose compact \(F\subset B\subset U\) with \(U\) open and \(|\mu|(U\setminus F)\) arbitrarily small. The displayed bound then gives arbitrarily small \(|f\mu|(U\setminus F)\). Thus \(f\mu\) is regular as well. This proves the weighted-measure fact used in the multiplicativity argument.

### 2. Elementary positivity facts and Bernstein operator weights

If \(B\) is a bounded positive self-adjoint operator, the scalar nonnegativity of \((B(x+zy),x+zy)\), for all \(z\in\mathbb C\), proves
\[
 |(Bx,y)|^2\leq(Bx,x)(By,y).
 \tag{BS4}
\]
Indeed, if \((By,y)>0\), choose the phase and modulus of \(z\) to minimize that quadratic expression. If \((By,y)=0\), any nonzero cross term would make the expression negative for a suitable phase and sufficiently large modulus; thus the cross term is zero. This proves (BS4) in both cases.

Write \(\beta=\sup_{\|x\|=1}(Bx,x)\). Taking the supremum over unit \(y\) in (BS4) gives \(\|Bx\|^2\leq\beta(Bx,x)\). Therefore \(\|B\|\leq\beta\), and the opposite inequality follows from Cauchy–Schwarz. We have proved
\[
 \|B\|=\beta,\qquad \|Bx\|^2\leq\|B\|(Bx,x).
 \tag{BS5}
\]
Apply this to \(S\). The assumptions imply that \(I-S\) is positive. Moreover
\[
 ((S-S^2)x,x)=(Sx,x)-\|Sx\|^2\geq0.
 \tag{BS6}
\]
Consequently all four operators \(I,S,I-S,S(I-S)\) are positive.

For integers \(n\geq1\) and \(0\leq k\leq n\), define
\[
 W_{n,k}=\binom nk S^k(I-S)^{n-k}.
 \tag{BS7}
\]
These operators are positive, as can be proved without taking an operator square root. Write \(k=2a+\varepsilon\) and \(n-k=2b+\delta\), where \(\varepsilon,\delta\in\{0,1\}\), and put \(Q=S^a(I-S)^b\). All factors are polynomials in the self-adjoint \(S\), so they commute, and \(Q=Q^*\). Then
\[
 W_{n,k}=\binom nk Q\,S^\varepsilon(I-S)^\delta Q.
\]
The middle factor is one of the four positive operators just proved positive. For each \(x\), the quadratic form is its nonnegative value at \(Qx\), multiplied by \(\binom nk\). This proves positivity. The binomial formula for the commuting operators \(S,I-S\) gives
\[
 \sum_{k=0}^nW_{n,k}=I.
 \tag{BS8}
\]

For a function \(f:K\to\mathbb C\), its scalar Bernstein polynomial and corresponding operator are
\[
 B_nf(t)=\sum_{k=0}^nf(k/n)\binom nk t^k(1-t)^{n-k},
 \qquad (B_nf)(S)=\sum_{k=0}^nf(k/n)W_{n,k}.
 \tag{BS9}
\]
If \(f\) is real and \(a\leq f\leq b\), then (BS7)–(BS8) imply
\[
 aI\leq(B_nf)(S)\leq bI.
 \tag{BS10}
\]

We next need convergence for a fixed polynomial in coefficient norm, rather than assuming that uniform convergence already implies operator convergence. For a nonnegative integer \(d\), let \(c_{d,j}\) be the number of partitions of a \(d\)-element set into \(j\) nonempty unlabeled subsets. Counting maps from that set to a \(k\)-element set by their fibers gives
\[
 k^d=\sum_{j=0}^d c_{d,j}(k)_j,
 \quad (k)_j=k(k-1)\cdots(k-j+1),
 \quad c_{d,d}=1.
 \tag{BS11}
\]
For \(d=0\), use \(c_{0,0}=1\). Directly canceling factorials in the binomial sum gives
\[
 \sum_{k=0}^n(k)_j\binom nk t^k(1-t)^{n-k}=(n)_j t^j.
\]
Terms with \(k<j\) are zero; after substituting \(k=j+\ell\), the remaining factor is the binomial expansion of \((t+(1-t))^{n-j}\). Thus, for fixed \(d\) and \(n\geq d\),
\[
 B_n(t^d)=\sum_{j=0}^dc_{d,j}\frac{(n)_j}{n^d}t^j.
 \tag{BS12}
\]
The coefficient at \(j=d\) tends to one, and every coefficient with \(j<d\) tends to zero. By linearity, \(B_np\to p\) in coefficient norm for every fixed polynomial \(p\). Since \(\|S^j\|\leq1\), the operator-norm difference between the two evaluated polynomials is at most the sum of the moduli of their coefficient differences. Hence
\[
 (B_np)(S)\longrightarrow p(S)\quad\hbox{in operator norm}.
 \tag{BS13}
\]
If a real polynomial \(q\) is nonnegative on \(K\), (BS10) and (BS13) show that \(q(S)\) is positive. Positivity is preserved in operator-norm limits because each scalar quadratic form converges.

For a complex polynomial \(p\), let \(M=\max_{t\in K}|p(t)|\). The real polynomial \(q(t)=M^2-\overline{p(t)}p(t)\), interpreted on the real variable \(t\), is nonnegative on \(K\). Polynomial algebra and \(S=S^*\) give
\[
 M^2I-p(S)^*p(S)=q(S)\geq0.
\]
Taking quadratic forms proves the exact bound
\[
 \|p(S)\|\leq\max_{0\leq t\leq1}|p(t)|.
 \tag{BS14}
\]
No spectral inclusion, spectral radius formula, compactness, or spectral theorem has been used.

### 3. Continuous functional calculus

For completeness, the Bernstein polynomials uniformly approximate every continuous complex function on \(K\). The nonnegative scalar weights in (BS9) have total mass one, mean \(t\), and squared displacement
\[
 \sum_{k=0}^n(k/n-t)^2\binom nk t^k(1-t)^{n-k}
 =\frac{t(1-t)}n\leq\frac1{4n}.
 \tag{BS15}
\]
The mean and second moment follow from the preceding factorial identity at \(j=1,2\), using \(k^2=(k)_2+k\). For \(\eta>0\), let \(\omega_f(\eta)=\sup_{|s-t|\leq\eta}|f(s)-f(t)|\). Separating indices with \(|k/n-t|\leq\eta\) and using (BS15) for the rest yields
\[
 \|B_nf-f\|_\infty
 \leq\omega_f(\eta)+\frac{2\|f\|_\infty}{4n\eta^2}.
 \tag{BS16}
\]
Uniform continuity makes the first term small by choosing \(\eta\), and then the second is made small by choosing \(n\). Therefore complex polynomials are uniformly dense in \(C(K)\).

For \(f\in C(K)\), take any polynomials \(p_n\to f\) uniformly and define
\[
 \Phi(f)=\lim_n p_n(S)
 \quad\hbox{in operator norm}.
 \tag{BS17}
\]
Inequality (BS14) makes the sequence Cauchy and proves that the limit is independent of the sequence. It also gives \(\|\Phi(f)\|\leq\|f\|_\infty\). The polynomial identities pass to these limits: for example, if \(p_n\to f\) and \(q_n\to g\) uniformly, then \(p_nq_n\to fg\), while boundedness of the approximating sequences and continuity of operator multiplication give \(p_n(S)q_n(S)\to\Phi(f)\Phi(g)\). Therefore
\[
 \Phi(1)=I,\quad\Phi(t)=S,\quad
 \Phi(fg)=\Phi(f)\Phi(g),\quad
 \Phi(\overline f)=\Phi(f)^*.
 \tag{BS18}
\]
Linearity is proved in the same way by polynomial sums and scalar multiples. If \(f\geq0\) is continuous, \(h=\sqrt f\) is continuous and (BS18) gives \(\Phi(f)=\Phi(h)^*\Phi(h)\geq0\). Alternatively positivity follows from the Bernstein approximants. This proves all continuous-calculus facts needed below.

### 4. Scalar measures with the correct complex convention

For each \(x\in H\), the functional \(L_x(f)=(\Phi(f)x,x)\) is positive and bounded on \(C(K)\). The scalar interval measure theorem gives a unique finite positive regular measure \(\mu_x\) such that
\[
 (\Phi(f)x,x)=\int_K f\,d\mu_x,
 \qquad\mu_x(K)=\|x\|^2.
 \tag{BS19}
\]
Define a finite complex measure for \(x,y\in H\) by
\[
 \mu_{x,y}=\frac14\sum_{k=0}^3i^k\mu_{x+i^k y}.
 \tag{BS20}
\]
To verify the sign, if \(f\) is real continuous, the form \((\Phi(f)x,y)\) is Hermitian, linear in \(x\) and conjugate-linear in \(y\). Expansion gives
\[
 (\Phi(f)(x+i^k y),x+i^k y)
 =L_x(f)+L_y(f)+i^{-k}(\Phi(f)x,y)
                         +i^k(\Phi(f)y,x).
\]
Multiplying by \(i^k\), summing, and dividing by four leaves exactly \((\Phi(f)x,y)\). Splitting a complex continuous \(f\) into its real and imaginary parts consequently proves
\[
 (\Phi(f)x,y)=\int_K f\,d\mu_{x,y}
 \qquad(f\in C(K)).
 \tag{BS21}
\]
Uniqueness of finite complex measures from their continuous integrals now proves that \((x,y)\mapsto\mu_{x,y}\) is linear in its first argument, conjugate-linear in its second, and satisfies \(\mu_{y,x}=\overline{\mu_{x,y}}\) and \(\mu_{x,x}=\mu_x\). For example, the measures representing \(\mu_{\alpha x+\beta z,y}\) and \(\alpha\mu_{x,y}+\beta\mu_{z,y}\) have equal integrals against every continuous \(f\) by (BS21), hence are equal. The other identities follow by the identical uniqueness argument.

For each Borel \(B\), the scalar form \((x,y)\mapsto\mu_{x,y}(B)\) is positive on the diagonal. The same quadratic argument as in (BS4) proves
\[
 |\mu_{x,y}(B)|^2\leq\mu_x(B)\mu_y(B).
 \tag{BS22}
\]
Taking a finite measurable partition \(B=\bigcup_jB_j\) and applying scalar Cauchy–Schwarz gives
\[
 \sum_j|\mu_{x,y}(B_j)|
 \leq\left(\sum_j\mu_x(B_j)\right)^{1/2}
      \left(\sum_j\mu_y(B_j)\right)^{1/2}.
\]
The supremum over finite partitions, which defines total variation, yields
\[
 |\mu_{x,y}|(B)\leq\mu_x(B)^{1/2}\mu_y(B)^{1/2},
 \qquad|\mu_{x,y}|(K)\leq\|x\|\|y\|.
 \tag{BS23}
\]
More generally, for nonnegative Borel \(h\),
\[
 \int_K h\,d|\mu_{x,y}|
 \leq\left(\int_Kh^2\,d\mu_x\right)^{1/2}\|y\|.
 \tag{BS24}
\]
For a nonnegative simple \(h=\sum_jc_j1_{B_j}\) on disjoint sets, use (BS23) on each set and Cauchy–Schwarz for the finite sum. Increasing simple approximation proves the displayed inequality in general, with infinity permitted. These estimates will control every unbounded cross integral below.

### 5. Bounded Borel operators and direct multiplicativity

For bounded Borel \(f\), the sesquilinear form
\[
 b_f(x,y)=\int_K f\,d\mu_{x,y}
\]
has modulus at most \(\|f\|_\infty\|x\|\|y\|\) by (BS23). Hilbert representation gives a unique vector \(\Psi(f)x\) such that
\[
 (\Psi(f)x,y)=\int_K f\,d\mu_{x,y}\quad(y\in H).
 \tag{BS25}
\]
The form is linear in \(x\), so uniqueness of the representing vector gives linearity of \(\Psi(f)\). Its norm is at most \(\|f\|_\infty\), so it is bounded. Representation is being used here for a conjugate-linear functional in \(y\): if \(F(y)\) is bounded and conjugate-linear, apply the ordinary linear-functional representation to \(\overline{F(y)}\), giving \(F(y)=(v,y)\). This accounts for the inner-product convention exactly.

The defining scalar integrals give linearity in \(f\), \(\Psi(1)=I\), and \(\Psi(f)=\Phi(f)\) for continuous \(f\). They also give
\[
 \Psi(f)^*=\Psi(\overline f),\qquad
 \Psi(f)\geq0\text{ if }f\geq0.
 \tag{BS26}
\]
For the adjoint formula, use \(\mu_{y,x}=\overline{\mu_{x,y}}\): the conjugate of \(\int\overline f\,d\mu_{y,x}\) is \(\int f\,d\mu_{x,y}\).

We prove multiplicativity rather than invoking a Borel extension theorem. First let \(g\) be continuous. For every continuous \(h\),
\[
 \int_Kh\,d\mu_{\Phi(g)x,y}
 =(\Phi(h)\Phi(g)x,y)
 =(\Phi(hg)x,y)=\int_Khg\,d\mu_{x,y}.
\]
The uniqueness of scalar complex measures implies
\[
 \mu_{\Phi(g)x,y}=g\,\mu_{x,y}.
 \tag{BS27}
\]
Hence, for bounded Borel \(f\), (BS25) gives
\[
 \Psi(f)\Phi(g)=\Psi(fg).
 \tag{BS28}
\]
Taking adjoints in (BS28), using (BS18) and (BS26), and then replacing \(f,g\) by their conjugates gives the opposite order
\[
 \Phi(g)\Psi(f)=\Psi(gf).
 \tag{BS29}
\]
Now keep \(f\) bounded Borel and test against any continuous \(h\):
\[
 \int_Kh\,d\mu_{\Psi(f)x,y}
 =(\Phi(h)\Psi(f)x,y)
 =(\Psi(hf)x,y)
 =\int_Khf\,d\mu_{x,y}.
\]
The measure \(f\mu_{x,y}\) is finite and regular, as specified in Section 1. Scalar uniqueness therefore proves the decisive identity
\[
 \mu_{\Psi(f)x,y}=f\,\mu_{x,y}.
 \tag{BS30}
\]
For any second bounded Borel \(g\), substitute (BS30) in (BS25):
\[
 (\Psi(g)\Psi(f)x,y)
 =\int_Kg\,d\mu_{\Psi(f)x,y}
 =\int_Kgf\,d\mu_{x,y}
 =(\Psi(gf)x,y).
\]
Since this holds for every \(x,y\),
\[
 \Psi(g)\Psi(f)=\Psi(gf).
 \tag{BS31}
\]
Together with (BS26), this proves the bounded Borel unital star algebra homomorphism without any Hilbert-space separability assumption. In particular
\[
 \|\Psi(f)x\|^2=(\Psi(|f|^2)x,x)
                  =\int_K|f|^2\,d\mu_x.
 \tag{BS32}
\]
If \(f_n\to f\) pointwise and \(\sup_n\|f_n\|_\infty<\infty\), then dominated convergence in (BS32) applied to \(f_n-f\) gives
\[
 \Psi(f_n)x\longrightarrow\Psi(f)x\qquad(x\in H).
 \tag{BS33}
\]
Thus bounded pointwise convergence produces strong operator convergence. Only a scalar measure associated with the particular vector is used; there is no countable enumeration of \(H\).

### 6. Projection-valued measure, exact bounded norms, and uniqueness

For a Borel set \(B\subset K\), define
\[
 E(B)=\Psi(1_B).
 \tag{BS34}
\]
Equations (BS26) and (BS31) give
\[
 E(B)^*=E(B),\quad E(B)^2=E(B),\quad
 E(B)E(C)=E(B\cap C),\quad E(K)=I,\quad E(\varnothing)=0.
 \tag{BS35}
\]
For disjoint Borel sets \(B_j\), the indicator functions of their finite unions converge boundedly pointwise to the indicator of their union. Linearity and (BS33) imply
\[
 E\left(\bigcup_{j\geq1}B_j\right)x
       =\lim_{N\to\infty}\sum_{j=1}^NE(B_j)x
       \quad(x\in H).
 \tag{BS36}
\]
More explicitly, the squared norm of the difference is
\(\mu_x((\bigcup_jB_j)\setminus(\bigcup_{j\leq N}B_j))\), which tends to zero by finite-measure continuity from above. This proves strong countable additivity. Countable additivity in operator norm is neither used nor claimed.

Taking \(f=1_B\) in (BS25) confirms
\[
 (E(B)x,y)=\mu_{x,y}(B),\qquad
 \mu_x(B)=\|E(B)x\|^2.
 \tag{BS37}
\]
For a Borel set \(N\), the following are equivalent: \(E(N)=0\); \(\mu_x(N)=0\) for every \(x\in H\); and \(E(N)x=0\) for every \(x\in H\). We call such a set \(E\)-null. For bounded Borel \(f\), its exact norm is
\[
 \|\Psi(f)\|
 =\inf\{c\geq0:E(\{|f|>c\})=0\}.
 \tag{BS38}
\]
For any \(c\) in this set, (BS32) gives \(\|\Psi(f)x\|\leq c\|x\|\). Conversely, if \(E(\{|f|>c\})\ne0\), choose a unit vector in the range of that projection. Its scalar measure is supported in \(\{|f|>c\}\), by (BS35)–(BS37), and has mass one. Thus its integral of \(|f|^2\) is strictly greater than \(c^2\); indeed \(|f|^2-c^2\) is positive at every point of a set of full scalar measure, and a nonnegative function with zero integral vanishes almost everywhere. Therefore \(\|\Psi(f)\|>c\). These implications prove (BS38), including the zero-space case. A sup norm over all of \([0,1]\) need not equal the operator norm if part of that interval is \(E\)-null.

For simple functions, \(\Psi(\sum_jc_j1_{B_j})=\sum_jc_jE(B_j)\). Every bounded complex Borel function has uniformly convergent finite-range Borel approximations, obtained, for example, by dividing its bounded real and imaginary ranges into intervals of length \(1/n\). Contractivity then identifies \(\Psi(f)\) with its bounded spectral integral. In particular \(\Psi(t)=\Phi(t)=S\), proving (BS2).

To prove uniqueness, suppose \(F\) is another orthogonal PVM on \(K\), with \(F(K)=I\), strong countable additivity, and \(\int_Kt\,dF(t)=S\). The integral of a simple function on disjoint sets is defined as above. Orthogonality gives
\[
 \left\|\sum_jc_jF(B_j)x\right\|^2
 =\sum_j|c_j|^2\|F(B_j)x\|^2
 \leq\max_j|c_j|^2\|x\|^2.
\]
Thus uniform simple approximation defines its bounded integrals and preserves sums, products, and conjugate adjoints, first checked on common finite partitions and then passed to norm limits. Consequently its polynomial integrals are \(p(S)\), and its continuous integrals are \(\Phi(f)\) by uniform polynomial approximation. For each \(x\), the positive finite measure \((F(\cdot)x,x)\) therefore has exactly the continuous integrals in (BS19). Scalar uniqueness gives \((F(B)x,x)=\mu_x(B)=(E(B)x,x)\) for all \(B,x\). Polarization with the convention in (BS20) gives \((F(B)x,y)=(E(B)x,y)\) for all \(x,y\), so \(F(B)=E(B)\). This proves the unique PVM assertion.

### 7. Unbounded Borel functions and the exact closed domain

Let \(f:K\to\mathbb C\) be Borel and finite at every point. Define
\[
 A_n=\{|f|\leq n\},\quad P_n=E(A_n),\quad
 f_n=f1_{A_n},\quad
 D_f=\left\{x:\int_K|f|^2\,d\mu_x<\infty\right\}.
 \tag{BS39}
\]
The sets \(A_n\) increase to \(K\), so \(P_n\to I\) strongly by (BS33). For any \(x\in H\), (BS32) gives
\[
 \|\Psi(f_n)x\|^2=\int_{A_n}|f|^2\,d\mu_x,
 \quad
 \|\Psi(f_n-f_m)x\|^2
 =\int_{A_n\setminus A_m}|f|^2\,d\mu_x\quad(n\geq m).
 \tag{BS40}
\]
The sequence \(\Psi(f_n)x\) is Cauchy if and only if \(x\in D_f\). Sufficiency follows from the vanishing tails of an integrable nonnegative function. For necessity a Cauchy sequence has bounded norms, so monotone convergence in the first formula gives a finite integral over \(K\). Define
\[
 T_fx=\lim_n\Psi(f_n)x\quad(x\in D_f).
 \tag{BS41}
\]
The set \(D_f\) is a vector space: the pointwise identity of the approximating operators gives
\(\|\Psi(f_n)(x+y)\|^2\leq2\|\Psi(f_n)x\|^2+2\|\Psi(f_n)y\|^2\); boundedness of these norms and (BS40) imply \(x+y\in D_f\). Scalar multiples are immediate. Limits in (BS41) then give linearity of \(T_f\). Equations (BS40)–(BS41) imply exactly
\[
 \|T_fx\|^2=\int_K|f|^2\,d\mu_x.
 \tag{BS42}
\]

The domain is dense. For any \(x\), \(P_nx\in D_f\) since its scalar measure is \(1_{A_n}\mu_x\), and hence its \(|f|^2\) moment is at most \(n^2\|x\|^2\). The asserted scalar measure formula follows from (BS35) and (BS37): \(\mu_{P_nx}(B)=\|E(B)P_nx\|^2=\mu_x(B\cap A_n)\). As \(P_nx\to x\), density follows.

For every Borel \(B\), this same argument shows \(E(B)D_f\subset D_f\). Passing the bounded commutation identities through the limit (BS41) gives
\[
 E(B)T_fx=T_fE(B)x\quad(x\in D_f),
 \qquad T_fP_nx=\Psi(f_n)x\quad(x\in H).
 \tag{BS43}
\]
For \(x\in D_f\), also \(P_nT_fx=\Psi(f_n)x\), by the first formula. Thus \(P_nx\to x\) in the graph norm of \(T_f\).

To prove closedness, let \(x_k\in D_f\), \(x_k\to x\), and \(T_fx_k\to y\). For fixed \(n\), boundedness and (BS43) imply
\[
 \Psi(f_n)x=\lim_k\Psi(f_n)x_k
           =\lim_k P_nT_fx_k=P_ny.
\]
Its squared norm is at most \(\|y\|^2\). Monotone convergence in (BS40) gives \(x\in D_f\). Letting \(n\to\infty\) in the last display gives \(T_fx=y\). This proves closedness with its full domain (BS39), not merely a closed restriction.

For \(x\in D_f\) and any \(y\in H\), (BS24) shows that \(f\) is integrable against \(\mu_{x,y}\), and dominated convergence gives
\[
 (T_fx,y)=\int_K f\,d\mu_{x,y},\qquad
 \left|\int_Kf\,d\mu_{x,y}\right|
 \leq\left(\int_K|f|^2\,d\mu_x\right)^{1/2}\|y\|.
 \tag{BS44}
\]
If \(f\) is bounded, the construction agrees with \(\Psi(f)\); if \(f\) is merely \(E\)-essentially bounded, (BS42) shows that its domain is all \(H\) and it equals a bounded representative with the exact norm (BS38). The operators only depend on \(f\) outside \(E\)-null sets, because the domain integrals and all approximating scalar integrals ignore those sets.

A function with an infinite value on an \(E\)-null Borel set is handled by replacing its value on that set by zero. The result is independent of that replacement. The assertion of dense domain in this theorem concerns functions finite \(E\)-almost everywhere; no dense-domain assertion is made for an infinite value on a set with nonzero spectral projection.

The same construction covers the completion of the Borel sigma-algebra by subsets of Borel \(E\)-null sets, without selecting a single dominating scalar measure. A countable union of \(E\)-null Borel sets is \(E\)-null: each \(\mu_x\) gives that union measure zero, and (BS37) applies. Each completed-measurable finite complex function has a Borel representative outside such a null set. To construct one, approximate its truncated real and imaginary parts by finite-range completed-measurable functions with pointwise errors at most \(1/n\). Replace the finitely many completed-measurable level sets of each approximation by Borel representatives. The discrepancies across all approximations are contained in one countable union of Borel \(E\)-null sets. The resulting sequence consists of Borel functions and converges to the original function off that union. On the Borel set where the sequence converges, take its limit; give it value zero on the complement. This is a Borel representative. Any two representatives agree off an \(E\)-null set, and the preceding domain and integral formulas show that they give the same operator. Thus “measurable” may also be read with this precise completed convention.

### 8. Full adjoint, product, and sum domains

We prove the unbounded adjoint formula in both directions. If \(v\in D(T_f^*)\), let \(w=T_f^*v\). For arbitrary \(h\in H\), \(P_nh\in D_f\), and the adjoint identity gives
\[
 (\Psi(f_n)h,v)=(T_fP_nh,v)=(P_nh,w).
\]
Bounded adjoints and self-adjointness of \(P_n\) turn this into
\[
 \Psi(\overline{f_n})v=P_nw.
 \tag{BS45}
\]
Taking norms and using monotone convergence yields
\(\int_K|f|^2\,d\mu_v\leq\|w\|^2\), so \(v\in D_{\overline f}\). Taking limits in (BS45) gives \(T_{\overline f}v=w\). Conversely, if \(v\in D_{\overline f}\) and \(u\in D_f\), bounded adjoint identities imply
\[
 (T_fu,v)=\lim_n(\Psi(f_n)u,v)
 =\lim_n(u,\Psi(\overline{f_n})v)
 =(u,T_{\overline f}v).
\]
Thus
\[
 T_f^*=T_{\overline f},\qquad
 D(T_f^*)=D_{\overline f}=D_f.
 \tag{BS46}
\]
The last equality concerns domain sets, not equality of actions for complex \(f\). Real functions give self-adjoint operators.

For \(x\in D_g\), (BS43) and (BS42) prove the scalar change-of-measure formula
\[
 \mu_{T_gx}(B)=\|E(B)T_gx\|^2
             =\|T_gE(B)x\|^2
             =\int_B|g|^2\,d\mu_x.
 \tag{BS47}
\]
Its last equality uses \(\mu_{E(B)x}=1_B\mu_x\). Equality of the measures then gives, for every nonnegative Borel \(h\),
\[
 \int_Kh\,d\mu_{T_gx}=\int_Kh|g|^2\,d\mu_x,
 \tag{BS48}
\]
first for simple \(h\), then by monotone convergence. Therefore the full domain of the product is
\[
 D(T_fT_g)
 =\{x\in D_g:T_gx\in D_f\}
 =D_g\cap D_{fg}.
 \tag{BS49}
\]
This proves both inclusions, since the second required integral is exactly \(\int|fg|^2\,d\mu_x\), with no discarded \(g\)-moment condition.

To identify the action, put \(C_n=\{|f|\leq n,|g|\leq n\}\) and \(Q_n=E(C_n)\). Then \(Q_n\to I\) strongly. On \(Q_nH\), the functions \(f,g,fg\) are all bounded; (BS31), (BS41), and (BS43) consequently give, for every \(x\) in the domain in (BS49),
\[
 Q_nT_fT_gx=\Psi(f1_{C_n})\Psi(g1_{C_n})x
           =\Psi(fg1_{C_n})x=Q_nT_{fg}x.
\]
Letting \(n\to\infty\) proves
\[
 T_fT_gx=T_{fg}x\quad(x\in D_g\cap D_{fg}).
 \tag{BS50}
\]
The intersection is essential. A complete example is \(H=\ell^2(\mathbb N)\), with \(Se_j=j^{-1}e_j\). Direct summation proves that \(S\) is positive, self-adjoint, injective, and has norm one. Define \(F(B)x\) by keeping precisely the coordinates for which \(j^{-1}\in B\). Coordinate multiplication proves the projection identities. For disjoint sets \(B_k\), the squared norm of the countable-additivity remainder is the sum of \(|x_j|^2\) over coordinates in their union not in the first \(N\) sets; this tends to zero by convergence of \(\sum_j|x_j|^2\). Thus \(F\) is a PVM. Its integral of \(t\) is \(S\), first for uniformly approximating simple functions and then by coordinate limits, so uniqueness identifies it with the constructed \(E\). Set \(f(t)=t\) and \(g(t)=1/t\) for \(t>0\), with \(g(0)=0\). The measure of \(\{0\}\) is zero for this PVM. The operator \(T_{fg}\) is the identity on \(H\), while
\[
 D(T_fT_g)=D_g=\left\{x:\sum_{j\geq1}j^2|x_j|^2<\infty\right\}.
\]
The vector \(x_j=1/j\) belongs to \(\ell^2\) and not to this domain. Hence the two operators have the same identity action on a proper subspace but different domains. This explicitly demonstrates why (BS49) cannot lose its intersection.

The product does have the precise closure
\[
 \overline{T_fT_g}=T_{fg}.
 \tag{BS51}
\]
Indeed (BS50) makes it a restriction of the closed operator \(T_{fg}\). For any \(x\in D_{fg}\), the vectors \(Q_nx\) above lie in \(D_g\cap D_{fg}\), and \(Q_nx\to x\), while \(T_{fg}Q_nx=Q_nT_{fg}x\to T_{fg}x\). Thus their product graphs approach every point of the graph of \(T_{fg}\), proving (BS51).

The sum \(T_f+T_g\) is defined on exactly \(D_f\cap D_g\). The inequality \(|f+g|^2\leq2|f|^2+2|g|^2\) puts this intersection inside \(D_{f+g}\). The same common cutoffs \(Q_n\), followed by strong limits, prove
\[
 (T_f+T_g)x=T_{f+g}x\quad(x\in D_f\cap D_g),
 \qquad\overline{T_f+T_g}=T_{f+g}.
 \tag{BS52}
\]
For the closure statement, use \(x\in D_{f+g}\), the approximants \(Q_nx\in D_f\cap D_g\), and \(T_{f+g}Q_nx=Q_nT_{f+g}x\). No equality of the initial sum domain with the full domain of the closed sum is assumed.

Applying (BS49)–(BS50) with \(\overline f,f\), and using \(|f|^2\leq1+|f|^4\), gives
\[
 \begin{split}
 D(T_f^*T_f)=D(T_fT_f^*)
 &=\left\{x:\int_K|f|^4\,d\mu_x<\infty\right\},\\
 T_f^*T_f&=T_fT_f^*=T_{|f|^2}.
 \end{split}
 \tag{BS53}
\]
Thus normality and the complete squared-modulus domain follow directly. Recursive powers also retain every intermediate-domain requirement. For an integer \(q\geq1\), a vector is in \(D(T_f^q)\) precisely when its successive images through \(T_f^{q-1}\) lie in \(D_f\). Induction using (BS49)–(BS50) proves
\[
 D(T_f^q)=\left\{x:\int_K|f|^{2q}\,d\mu_x<\infty\right\},
 \qquad T_f^q=T_{f^q}\text{ on that domain}.
 \tag{BS53a}
\]
At each step the higher moment implies all lower ones because \(|f|^{2k}\leq1+|f|^{2q}\) for \(0\leq k\leq q\), and \(\mu_x(K)=\|x\|^2<\infty\). Conversely, the product-domain equality requires the higher moment, so the implication is in both directions. The exact norm is \(\|T_f^qx\|^2=\int_K|f|^{2q}\,d\mu_x\), by (BS42). The case \(q=0\) is the identity on \(H\).

The kernels are also exact:
\[
 \ker T_f=E(\{f=0\})H.
 \tag{BS54}
\]
If \(T_fx=0\), (BS42) makes \(\mu_x(\{|f|>0\})=0\), by applying it to the union of sets \(\{|f|\geq1/n\}\). Equation (BS37) then gives \(x=E(\{f=0\})x\). Conversely any vector in that range has zero moment and zero image. In particular a function nonzero \(E\)-almost everywhere gives an injective multiplier.

### 9. The point zero and the inverse needed by the application

For \(S=\Psi(t)\), equation (BS32) gives
\[
 \|Sx\|^2=\int_Kt^2\,d\mu_x.
 \tag{BS55}
\]
If \(Sx=0\), the measure of \([1/n,1]\) is zero for every \(n\), since the integral is at least \(n^{-2}\mu_x([1/n,1])\). Hence \(\mu_x((0,1])=0\) and \(x=E(\{0\})x\). Conversely \(SE(\{0\})=\Psi(t1_{\{0\}})=0\). We have proved
\[
 \ker S=E(\{0\})H.
 \tag{BS56}
\]
The assumed injectivity therefore implies \(E(\{0\})=0\). This does not exclude spectral mass arbitrarily close to zero.

Define the finite-valued Borel function
\[
 r_0(t)=\begin{cases}t^{-1},&0<t\leq1,\\0,&t=0.\end{cases}
 \tag{BS57}
\]
Because the point zero is \(E\)-null, \(T_{tr_0}=I\) on \(H\). The product-domain theorem gives
\[
 D(T_{r_0}S)=D(S)\cap D(T_{tr_0})=H,
 \qquad T_{r_0}S=I\text{ on }H.
\]
In the opposite order, it gives
\[
 D(ST_{r_0})=D(T_{r_0}),\qquad ST_{r_0}=I\text{ on }D(T_{r_0}).
\]
The first identity says \(SH\subset D(T_{r_0})\), and the second says every \(u\in D(T_{r_0})\) equals \(S(T_{r_0}u)\), so the reverse inclusion also holds. Therefore
\[
 D(T_{r_0})=\operatorname{Ran}S,
 \quad T_{r_0}=S^{-1}\text{ on that exact domain},
 \quad\|S^{-1}u\|^2=\int_{(0,1]}t^{-2}\,d\mu_u.
 \tag{BS58}
\]
The range is dense: if \(y\perp\operatorname{Ran}S\), then \((Sx,y)=0\) for all \(x\), so \(Sy=0\) by self-adjointness and hence \(y=0\). This also agrees with the dense-domain conclusion already proved for \(T_{r_0}\).

## AN03-SPC-004 — The original lower-bounded operator and its sharp cutoff

### LB1. The bounded inverse is constructed on the actual domain

Let \(H\) be a complex Hilbert space and let \(A:D(A)\subset H\to H\) be densely defined and self-adjoint, with
\[
 (Au,u)\geq a\|u\|^2\qquad(u\in D(A)).
 \tag{LB1}
\]
Fix exactly a real number \(\rho\geq1+\max(0,-a)\), as in (DSP40), and write
\[
 T=A+\rho I,\quad D(T)=D(A),\qquad
 \delta=a+\rho\geq1.
 \tag{LB2}
\]
For \(u\in D(T)\), Cauchy–Schwarz and (LB1) give
\(\|Tu\|\geq\delta\|u\|\).
In particular \(T\) is injective. It is closed because \(A\) is closed: if \(u_n\to u\) and \(Tu_n\to v\), then \(Au_n\to v-\rho u\), so closedness of \(A\) gives \(u\in D(A)\) and \(Tu=v\).

Its range is closed. Indeed, if \(Tu_n\) converges, the displayed estimate makes \(u_n\) Cauchy. Its limit and the closed graph of \(T\) identify the limit of \(Tu_n\) as an element of \(\operatorname{Ran}T\). Also \(T^*=A^*+\rho I=T\), with domain \(D(A)\): subtract the bounded functional \(\rho(u,v)\) in the definition of the adjoint to obtain both inclusions of domains and the equality of values. The identity
\[
 (\operatorname{Ran}T)^\perp=\ker T^*=\{0\}
\]
follows directly from that same adjoint definition. Thus the range is both closed and dense, and equals \(H\).

Consequently the inverse
\[
 S=T^{-1}:H\longrightarrow H,\qquad
 \operatorname{Ran}S=D(A),\quad \ker S=\{0\},\quad
 \|S\|\leq\delta^{-1}\leq1
 \tag{LB3}
\]
exists everywhere and is bounded. The equalities \(TS=I\) on \(H\) and \(ST=I\) on \(D(T)\) follow from inverse bijectivity, with exactly the indicated domains. If \(x=Tu\), \(y=Tv\), then
\[
 (Sx,y)=(u,Tv)=(Tu,v)=(x,Sy),
 \qquad (Sx,x)=(u,Tu)\geq0.
 \tag{LB4}
\]
Every \(x,y\in H\) have such representations, so \(S=S^*\geq0\). There is no compactness assertion. The range is dense because \(D(A)\) is dense.

### LB2. The original real spectral coordinate is recovered

The construction in AN03-SPC-003 gives its unique projection-valued measure \(E\) on \([0,1]\), with
\[
 S=\int_{[0,1]}t\,dE(t),\qquad
 \mu_u(C)=(E(C)u,u),\qquad
 \|g(S)u\|^2=\int |g(t)|^2\,d\mu_u(t)
 \tag{LB5}
\]
on the exact square-integrability domain for a finite measurable \(g\). At a null endpoint a chosen finite value makes no difference. Injectivity implies \(E(\{0\})=0\): by (LB5), \(Su=0\) is equivalent to \(\mu_u((0,1])=0\), hence its kernel is exactly \(E(\{0\})H\).

Put \(c=\delta^{-1}\). The measure is concentrated on \([0,c]\). To prove this without assuming a spectral support theorem, fix \(b>c\). For \(u\in E([b,1])H\), (LB5) and the bounded calculus give
\[
 b\|u\|^2\leq(Su,u)\leq\|S\|\|u\|^2\leq c\|u\|^2.
\]
Thus \(E([b,1])=0\). The union of these sets for rational \(b>c\) is \((c,1]\), and strong countable additivity proves \(E((c,1])=0\). If \(c=1\) this set is empty. Combined with the preceding endpoint calculation, the full mass lies on
\[
 J=(0,\delta^{-1}],\qquad
 \kappa:J\longrightarrow[a,\infty),\quad
 \kappa(t)=t^{-1}-\rho,\qquad
 \kappa^{-1}(\lambda)=(\lambda+\rho)^{-1}.
 \tag{LB6}
\]
These are inverse continuous maps, with reversed order. Their exact endpoint relation is \(\kappa(\delta^{-1})=\delta-\rho=a\).

For a Borel set \(B\subset\mathbb R\), define
\[
 F(B)=E\bigl(\{t\in J:\kappa(t)\in B\}\bigr).
 \tag{LB7}
\]
Preimages preserve disjoint unions and intersections. Therefore \(F\) is a projection-valued measure, strongly countably additive, with \(F(\mathbb R)=E(J)=I\), and \(F((-\infty,a))=0\). Its scalar measures satisfy, first for indicator functions, then for nonnegative simple functions and increasing limits,
\[
 \int_{\mathbb R}h(\lambda)\,d(F(\lambda)u,u)
   =\int_J h(t^{-1}-\rho)\,d\mu_u(t)
 \tag{LB8}
\]
for every nonnegative Borel \(h\), with both sides allowed to be infinite. Linear decomposition gives the same change-of-variable identity for integrable complex \(h\). The notation on the left denotes integration against \(B\mapsto(F(B)u,u)\), not a derivative of a scalar distribution function.

### LB3. Equality of the closed operators, including their domains

Let \(G(t)=t^{-1}\) on \(J\), and give it value zero outside \(J\). Its value at zero is immaterial because that set is \(E\)-null. The unbounded calculus proved in AN03-SPC-003 defines the closed operator \(G(S)\).

If \(u=Sf\), the measure identity for multiplication by the bounded function \(t\) is
\[
 \mu_{Sf}(B)=\int_B t^2\,d\mu_f(t).
 \tag{LB9}
\]
Indeed \(E(B)S=SE(B)\), and the squared norm of \(SE(B)f\) is the displayed integral. Thus
\[
 \int_J t^{-2}\,d\mu_{Sf}(t)=\|f\|^2.
 \tag{LB10}
\]
So \(\operatorname{Ran}S\subset D(G(S))\) and the product identity gives \(G(S)Sf=f\). Conversely, if \(u\in D(G(S))\), put \(f=G(S)u\). Bounded multiplication by \(t\) gives \(Sf=u\), since \(tG(t)=1\) on the full-measure set \(J\). Therefore
\[
 D(G(S))=\operatorname{Ran}S=D(A),\qquad
 G(S)u=Tu.
 \tag{LB11}
\]
This proves the actual graph equality, not just an identity on a test core.

On \(J\), \(G=\kappa+\rho\). The elementary inequalities
\[
 |G|^2\leq2|\kappa|^2+2\rho^2,\qquad
 |\kappa|^2\leq2|G|^2+2\rho^2
 \tag{LB12}
\]
show equality of their square-integrability domains, since \(\mu_u(J)=\|u\|^2<\infty\). Bounded addition in the calculus consequently gives
\[
 D(\kappa(S))=D(A),\qquad
 \kappa(S)u=G(S)u-\rho u=Au.
 \tag{LB13}
\]
Thus the coordinate operator of \(F\) is exactly the given \(A\).

### LB4. Every measurable multiplier and every recursive power

For any finite-valued complex Borel \(m\) on \(\mathbb R\), define \(m(A)=(m\circ\kappa)(S)\), extending the composite arbitrarily across the \(E\)-null complement of \(J\). Equations (LB5) and (LB8) prove
\[
 \begin{aligned}
 D(m(A))&=\left\{u\in H:
       \int_{\mathbb R}|m(\lambda)|^2\,d(F(\lambda)u,u)<\infty\right\},\\
 \|m(A)u\|^2&=\int_{\mathbb R}|m(\lambda)|^2\,d(F(\lambda)u,u).
 \end{aligned}
 \tag{LB14}
\]
The bounded measure construction proves density and closedness of this operator, its full adjoint \(m(A)^*=\overline m(A)\), and the exact product rule
\[
 \begin{aligned}
 D(m_1(A)m_2(A))
   &=D(m_2(A))\cap D((m_1m_2)(A)),\\
 m_1(A)m_2(A)u&=(m_1m_2)(A)u
       \quad\text{on this domain}.
 \end{aligned}
 \tag{LB15}
\]
These statements transfer by (LB8) with both domains retained; no intersection is discarded. For bounded \(m\), (LB14) gives \(\|m(A)\|\leq\sup_{\lambda\geq a}|m(\lambda)|\). More exactly the norm is the essential supremum relative to \(F\): the upper bound follows by integration, and if \(F(\{|m|>b\})\ne0\), a unit vector in this projection range has image norm greater than \(b\). Taking all such \(b\) proves equality.

The power in (DSP1) is the recursively defined power of the original operator, not a newly assigned domain. For \(q=0\), it is \(I\) on \(H\); for \(q=1\), (LB13) proves the assertion. If the assertion holds for \(q\), the product rule gives
\[
 D(A^{q+1})
 =\left\{u:
 \int |\lambda|^{2q}\,d(F(\lambda)u,u)<\infty,\quad
 \int |\lambda|^{2q+2}\,d(F(\lambda)u,u)<\infty\right\}.
\]
The second integral implies the first because
\(|\lambda|^{2q}\leq1+|\lambda|^{2q+2}\).
Thus induction proves
\[
 D(A^q)=\left\{u:
       \int|\lambda|^{2q}\,d(F(\lambda)u,u)<\infty\right\},
 \qquad A^q=(\lambda\mapsto\lambda^q)(A).
 \tag{LB16}
\]
The opposite recursive convention \(A^qA\) has domain
\(D(A)\cap D((\lambda\mapsto\lambda^{q+1})(A))\) by (LB15).
The moment of order \(2q+2\) implies the moment of order two, because
\(|\lambda|^2\leq1+|\lambda|^{2q+2}\). Thus this domain and action
coincide with those of \(AA^q\). Both conventions give (LB16), including
the recurrence through \(Au\) used in (DSP39).

The same induction applies to \(T=A+\rho I\), giving its recursive powers with multiplier \((\lambda+\rho)^q\). The inequalities
\[
 |\lambda+\rho|^{2q}\leq 2^{2q-1}(|\lambda|^{2q}+\rho^{2q}),
 \qquad
 |\lambda|^{2q}\leq 2^{2q-1}(|\lambda+\rho|^{2q}+\rho^{2q})
\]
for \(q\geq1\) prove \(D(T^q)=D(A^q)\), without changing either operator.

Uniqueness is also preserved. Suppose a real projection-valued measure \(F'\)
represents the same closed \(A\), with its square-integrability multiplier domains.
Its lower concentration follows from the operator inequality itself. For
\[
 C_n=\{\lambda:|\lambda|\leq n,\ \lambda\leq a-1/n\},
\]
a vector \(u\in F'(C_n)H\) belongs to \(D(A)\), since the coordinate is bounded on
\(C_n\). Therefore
\[
 a\|u\|^2\leq(Au,u)
  =\int_{C_n}\lambda\,d(F'(\lambda)u,u)
  \leq(a-1/n)\|u\|^2.
\]
This forces \(F'(C_n)=0\). These sets increase to \((-\infty,a)\), so strong
countable additivity gives \(F'((-\infty,a))=0\).
On the full-mass half-line its multiplier \(r(\lambda)=(\lambda+\rho)^{-1}\),
extended as zero elsewhere, is bounded by \(\delta^{-1}\). The product rule shows
\((A+\rho I)r(F')=I\) on \(H\) and \(r(F')(A+\rho I)=I\) on \(D(A)\); all domain assertions follow from \((\lambda+\rho)r(\lambda)=1\). Therefore \(r(F')=S\). Push \(F'\) forward under \(r\) to a measure on \([0,1]\), assigning zero mass at zero. It represents \(S\), hence equals \(E\) by the uniqueness in the bounded construction. The inverse map \(\kappa\) then recovers \(F'=F\).

### LB5. The precise sharp projector in DSP010

For the original real parameter \(\lambda\), put \(E_\lambda=F((-\infty,\lambda])\). If \(\lambda<a\), this projection is zero. If \(\lambda\geq a\), its exact inverse-coordinate description is
\[
 E_\lambda
 =E\!\left([(\lambda+\rho)^{-1},(a+\rho)^{-1}]\right).
 \tag{LB17}
\]
Both endpoints are included. In particular the change of coordinate reverses the inequality and keeps any atom at \(\lambda\).

For \(u\in E_\lambda H\), its \(F\)-measure is supported in \([a,\lambda]\). All moments of this finite interval are bounded, so \(u\in D(A^q)=D(T^q)\) for every integer \(q\geq0\). Write \(L=\lambda+\rho\geq1\). On this interval \(1\leq a+\rho\leq t+\rho\leq L\). Therefore
\[
 \|T^ju\|\leq L^j\|u\|,\qquad
 \|A^ju\|\leq (L+\rho)^j\|u\|
             \leq(1+\rho)^jL^j\|u\|.
 \tag{LB18}
\]
Since \(L\geq1\) and \(1+\rho\geq1\), summing gives the explicit instance of (DSP40)
\[
 \sum_{j=0}^q\|A^ju\|
 \leq(q+1)(1+\rho)^qL^q\|u\|.
 \tag{LB19}
\]
This estimate is valid for every \(\lambda\geq a\); the later local kernel argument uses \(\lambda\geq1\) to compare \(L\) with \(\lambda\). If the projection is zero the estimate holds as well.

For a bounded Borel \(m\) supported in \((-\infty,b]\), bounded multiplicativity gives \(m(A)=E_bm(A)E_b\) exactly, including its value at \(b\). For a bounded Borel sequence \(m_n\) with a common uniform bound and pointwise convergence to \(m\), (LB14) applied to the differences and dominated convergence give \(m_n(A)u\to m(A)u\) for every \(u\in H\).

Finally, the entire proof applies directly to \(H=L^2(X,r\,dx)\) with its original weighted inner product. No unitary change of density, coordinate change, compactness assumption, boundary condition or alteration of the test-domain inclusion (DSP33) enters this spectral step. Every differential-domain and boundary-regularity assertion in AN03-DSP-010 consequently keeps its existing separate proof.

## AN03-SPC-005 — Two exact models and a solved domain exercise

The same coordinate correspondence can represent continuous spectrum or a sequence of eigenvalues. Here both models use the actual constants \(a=-2\), \(\rho=3\), \(\delta=1\), and the cutoff \(\lambda=4\).

### A weighted continuous model

Let
\[
 H=L^2([0,\infty),e^{-x}\,dx),\quad
 D(A)=\left\{u\in H:\int_0^\infty|x-2|^2|u(x)|^2e^{-x}\,dx<\infty\right\},
 \quad Au(x)=(x-2)u(x).
 \tag{SC1}
\]
This is densely defined: truncating any \(u\in H\) to \([0,n]\) gives domain elements converging in \(H\). Multiplication by the real function \(x-2\) is symmetric there. To identify its full adjoint, let \(v\in D(A^*)\) and put \(w=A^*v\). Test the adjoint identity with every \(u\in H\) supported in \([0,n]\), which belongs to \(D(A)\). It gives \(1_{[0,n]}w=(x-2)1_{[0,n]}v\) in \(H\). Letting \(n\) increase proves \(w=(x-2)v\) almost everywhere, so \(v\in D(A)\). The converse follows by the integrable Hilbert pairing. Thus \(A=A^*\) on exactly (SC1), and
\[
 (Au,u)=\int_0^\infty(x-2)|u(x)|^2e^{-x}\,dx\geq-2\|u\|^2.
\]
The integral is finite for \(u\in D(A)\) by Cauchy–Schwarz.

Here \(T=A+3I\) multiplies by \(x+1\), and \(S=T^{-1}\) multiplies by \((x+1)^{-1}\), with no density change. Its PVM on \([0,1]\) is
\[
 E(B)u(x)=1_B((x+1)^{-1})u(x).
 \tag{SC2}
\]
Indicator multiplication proves idempotence, adjoints and intersections; dominated convergence against \(|u|^2e^{-x}\,dx\) proves strong countable additivity. Its coordinate integral is \(S\), so bounded uniqueness identifies it with the constructed PVM. Therefore the real PVM and sharp projector are exactly
\[
 F(B)u(x)=1_B(x-2)u(x),\qquad
 E_\lambda u(x)=
 \begin{cases}1_{[0,\lambda+2]}(x)u(x),&\lambda\geq-2,\\
 0,&\lambda<-2.
 \end{cases}
 \tag{SC3}
\]
An eigenvector with eigenvalue \(b\) would vanish outside the singleton \(\{b+2\}\), which has measure zero for \(e^{-x}\,dx\); hence there are no nonzero eigenvectors. For \(\lambda>-2\), put \(c=\lambda+2>0\). The intervals \((c2^{-(j+1)},c2^{-j})\), \(j\geq0\), are pairwise disjoint subsets of \([0,c]\) with positive weighted measure. Their indicator functions, divided by the square roots of those exact measures, give infinitely many orthonormal vectors in \(E_\lambda H\). Thus this projection has infinite rank. A local spectral argument cannot infer finite rank from a finite spectral interval alone.

At the specified cutoff,
\[
 E_4u=1_{[0,6]}u,\qquad E_4=E([1/7,1]).
 \tag{SC4}
\]
The example keeps the nonconstant density and the original coordinate \(x\).

### An atomic model that detects the endpoint

On \(H=\ell^2(\mathbb N_0)\), define
\[
 D(A)=\left\{u:\sum_{j=0}^\infty|j-2|^2|u_j|^2<\infty\right\},
 \qquad(Au)_j=(j-2)u_j.
 \tag{SC5}
\]
Finite sequences are dense. Testing the adjoint identity on each coordinate vector forces the adjoint value to be \((j-2)v_j\); membership of that sequence in \(\ell^2\) is exactly the displayed domain. Conversely Cauchy–Schwarz proves the adjoint identity on that domain. Thus this is self-adjoint and lower-bounded by \(-2\). Its inverse \(S=(A+3I)^{-1}\) multiplies coordinate \(j\) by \((j+1)^{-1}\). The coordinate projections give its PVM directly, and
\[
 E_4u=(u_0,u_1,\ldots,u_6,0,\ldots),\qquad
 E_4=E([1/7,1]).
 \tag{SC6}
\]
Both equalities include coordinate \(j=6\). Replacing the lower endpoint \(1/7\) by an open endpoint deletes that eigenspace. This proves that the endpoint convention in (LB17) has observable mathematical content, even though the continuous model gives individual endpoints measure zero.

### Exercise and complete solution

For the atomic model, determine the domains and actions of \(S(A+3I)\) and of the multiplier obtained from the product \(t\cdot t^{-1}=1\) on \((0,1]\). Exhibit a vector that distinguishes them.

The operator \(A+3I\) has domain (SC5), and \(S\) is bounded on all of \(H\). Thus \(S(A+3I)\) has exactly domain \(D(A)\); its coordinate action there is \(u_j\mapsto(j+1)^{-1}(j+1)u_j=u_j\). The product function equals one outside the \(E\)-null point zero, so its multiplier is \(I\) on all of \(H\).

Take \(u_j=(j+1)^{-1}\). Its squared sum is finite: for \(k\geq2\), \(k^{-2}\leq[k(k-1)]^{-1}=(k-1)^{-1}-k^{-1}\), whose partial sums are bounded. But for \(j\geq5\), \((j-2)/(j+1)\geq1/2\), so the sum in (SC5) is infinite. Hence \(u\in H\setminus D(A)\). The two identity actions have different domains exactly as (LB15) states. The opposite composition \((A+3I)S\) is defined on all of \(H\), because multiplication by \((j+1)^{-1}\) places every sequence in \(D(A+3I)\), and its action is \(I\) there.

## Antecedents and use in the elliptic course

The measure representation is the classical Riesz representation theorem on the compact interval. The functional-calculus route has the human antecedent Markus Haase, [The Functional Calculus Approach to the Spectral Theorem, arXiv:2003.06130v2](https://arxiv.org/abs/2003.06130v2), especially the original TeX theorem labels con.t.ext-bdd, con.t.ext-cont, spt.t.bdd, and spt.t.unb. The original author LaTeX was consulted; all course arguments and examples above are independently written.

For the differential-operator application, [Dirichlet realizations, spectral projectors, and local extensions](dirichlet-spectral-projectors.md), AN03-DSP-010, supplies the exact expression, weighted Hilbert space and boundary-domain inclusion. AN03-SPC-004 proves the spectral facts on that unchanged Hilbert space. Its moment identity (LB14), recursive-power identity (LB16), closed endpoint (LB17), and explicit constant (LB19) provide precisely the spectral step in (DSP1) and (DSP40). The local differential regularity and kernel construction keep their complete proofs in that unit. No compactness or eigenbasis premise is added to that application.

This independently written programme text is dedicated under CC0 1.0 Universal, to the extent rights are held. External works retain their own rights.
