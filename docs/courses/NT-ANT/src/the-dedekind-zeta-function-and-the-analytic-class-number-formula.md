# The Dedekind zeta function and the analytic class number formula

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. No independent full-lesson review is claimed. Public domain (CC0).*

The number of ideals below a norm bound determines the first singularity of the Dedekind zeta function. Its main term becomes a pole, and its error becomes a holomorphic integral. The residue records the class number, regulator, roots of unity and discriminant in one constant.

Let \(K\) be a number field of degree \(n=r_1+2r_2\). All ideals in a sum are nonzero integral ideals of \(O_K\), and all prime ideals are nonzero. Write
\[
A_K(X)=\#\{\mathfrak a:N\mathfrak a\leq X\},\qquad
\theta=1-\frac1n,\qquad
C_K=\frac{2^{r_1}(2\pi)^{r_2}h_KR_K}
 {w_K\sqrt{|d_K|}}.
\tag{1}
\]
The regulator uses weight two at a complex place and a deleted-row determinant, as in [*Dirichlet's unit theorem*](dirichlets-unit-theorem.md); it is \(1\) in rank zero. The preceding lesson, [*Counting ideals of bounded norm*](counting-ideals-of-bounded-norm.md), proved
\[
A_K(X)=C_KX+O_K(X^\theta),\qquad X\geq1.
\tag{2}
\]
In particular \(C_K>0\). We use the basic complex analysis of normally convergent series and parameter integrals.

## The series and its Euler product

For \(\Re s>1\), define
\[
\zeta_K(s)=\sum_{\mathfrak a}(N\mathfrak a)^{-s},
\qquad t^{-s}=\exp(-s\log t)\quad(t>0).
\tag{3}
\]

**Proposition 16.1.** The series is absolutely convergent and holomorphic on \(\Re s>1\), and there
\[
\zeta_K(s)=\prod_{\mathfrak p}
 (1-(N\mathfrak p)^{-s})^{-1}.
\tag{4}
\]

**Proof.** If \(a_m\) is the number of ideals of norm \(m\), then \(\sum_{m\leq X}a_m=A_K(X)=O_K(X)\). Partial summation gives, for real \(\sigma>1\),
\[
\sum_{m\leq T}a_mm^{-\sigma}
=A_K(T)T^{-\sigma}
 +\sigma\int_1^T A_K(x)x^{-\sigma-1}\,dx.
\tag{5}
\]
The endpoint tends to zero and the integral converges. This proves absolute convergence. On a compact subset of \(\Re s>1\), choose \(\sigma_0>1\) below all real parts. The convergent positive series \(\sum a_mm^{-\sigma_0}\) dominates (3), giving normal convergence and holomorphy.

For a finite set \(S\) of prime ideals, expand the finite product of geometric series. Unique ideal factorization and multiplicativity of the norm give
\[
\prod_{\mathfrak p\in S}(1-(N\mathfrak p)^{-s})^{-1}
=\sum_{\operatorname{supp}(\mathfrak a)\subseteq S}
 (N\mathfrak a)^{-s}.
\]
As \(S\) exhausts the prime ideals, every ideal eventually appears. Absolute summability makes the omitted tail tend to zero, proving (4). Moreover the product itself converges absolutely: for \(q=N\mathfrak p\geq2\),
\[
\left|(1-q^{-s})^{-1}-1\right|
\leq\frac{q^{-\sigma}}{1-2^{-\sigma}},
\]
and the prime-ideal sum is a subseries of (3). \(\square\)

There is also a useful coarse bound. Above a rational prime \(p\), write the residue degrees \(f_1,\ldots,f_g\), so \(N\mathfrak p_i=p^{f_i}\), \(f_i\geq1\), and \(g\leq n\). The decomposition theorem proved in [*Decomposition of primes in extensions*](decomposition-of-primes-in-extensions.md) gives these facts. Consequently
\[
\zeta_K(\sigma)\leq
\prod_p(1-p^{-\sigma})^{-n}
=\zeta(\sigma)^n,\qquad \sigma>1,
\tag{6}
\]
where \(\zeta=\zeta_{\mathbf Q}\). Integer prime factorization proves the last Euler product in the same way.

## Turning the counting error into continuation

**Theorem 16.2 (analytic class number formula).** The function \(\zeta_K\) continues meromorphically to \(\Re s>\theta\). Its only pole there is a simple pole at \(1\), with
\[
\operatorname*{Res}_{s=1}\zeta_K(s)
=C_K
=\frac{2^{r_1}(2\pi)^{r_2}h_KR_K}
 {w_K\sqrt{|d_K|}}.
\tag{7}
\]
On the same half-plane, \(\zeta_K(s)-C_K\zeta(s)\) is holomorphic.

**Proof.** Apply (5) with complex \(s\), initially \(\Re s>1\), and let \(T\) tend to infinity. The endpoint vanishes and yields
\[
\zeta_K(s)=s\int_1^\infty A_K(x)x^{-s-1}\,dx.
\]
Set \(E_K(x)=A_K(x)-C_Kx\). Integrating the main term gives
\[
\zeta_K(s)=\frac{C_Ks}{s-1}
 +s\int_1^\infty E_K(x)x^{-s-1}\,dx.
\tag{8}
\]
By (2), \(|E_K(x)|\leq M_Kx^\theta\) for all \(x\geq1\). On a compact subset of \(\Re s>\theta\), choose \(\sigma_0>\theta\) below all real parts and bound \(|s|\). The integrand is dominated by a constant times
\[
x^{\theta-\sigma_0-1},
\]
which is integrable. Every derivative with respect to \(s\) introduces at most a fixed power of \(\log x\); these bounds remain integrable. Uniform convergence of the truncated holomorphic integrals, or differentiation under the integral, therefore proves that the integral term in (8) is holomorphic throughout this half-plane.

Equation (8) agrees with the original series where \(\Re s>1\), so it is the required continuation. The first term has a simple pole of residue \(C_K\); the second has no pole, and \(C_K>0\).

For the last assertion, the rational field has \(A_{\mathbf Q}(x)=\lfloor x\rfloor\), so the same argument gives
\[
\zeta(s)=\frac{s}{s-1}
 +s\int_1^\infty(\lfloor x\rfloor-x)x^{-s-1}\,dx
\quad(\Re s>0).
\]
Subtracting \(C_K\) times this identity from (8) gives the holomorphic integral
\[
\zeta_K(s)-C_K\zeta(s)
=s\int_1^\infty
 [A_K(x)-C_K\lfloor x\rfloor]x^{-s-1}\,dx.
\tag{9}
\]
Its bracket is \(O_K(x^\theta)\), since \(\theta\geq0\). This includes \(n=1\), when \(\theta=0\); no positive-rank or positive-error-exponent assumption was used. \(\square\)

The same proof applies to the ideals in a fixed class. Their counting constant is \(C_K/h_K\), so their partial zeta function has residue \(C_K/h_K\). Summing these residues recovers (7).

## Prime ideals of degree one

**Corollary 16.3.** For real \(s\) tending to \(1\) from above,
\[
\sum_{\mathfrak p}(N\mathfrak p)^{-s}
=\log\frac1{s-1}+O_K(1).
\tag{10}
\]
The prime ideals of residue degree one carry this entire logarithmic main term. In particular they have Dirichlet density one among the prime ideals of \(K\).

**Proof.** Positivity permits taking the real logarithm in (4):
\[
\log\zeta_K(s)=\sum_{\mathfrak p}(N\mathfrak p)^{-s}
 +\sum_{\mathfrak p}\sum_{k\geq2}
  \frac{(N\mathfrak p)^{-ks}}k.
\tag{11}
\]
The last double sum is uniformly bounded for \(s\geq1\). Indeed, if \(q=N\mathfrak p\geq2\),
\[
\sum_{k\geq2}\frac{q^{-ks}}k
\leq\frac{q^{-2s}}{1-q^{-s}}\leq2q^{-2s}.
\]
There are at most \(n\) prime ideals above \(p\), all with \(q\geq p\), so the total is at most \(2n\sum_p p^{-2}<\infty\).

Theorem 16.2 gives
\(\zeta_K(s)=C_K/(s-1)+O_K(1)\). Therefore
\(\log\zeta_K(s)=\log(1/(s-1))+\log C_K+o(1)\), which proves (10).

If \(f(\mathfrak p/p)\geq2\), then \(N\mathfrak p\geq p^2\). Hence, again uniformly for \(s\geq1\),
\[
\sum_{f(\mathfrak p/p)\geq2}(N\mathfrak p)^{-s}
\leq n\sum_p p^{-2}.
\tag{12}
\]
Subtract this bounded sum from (10). For clarity, the Dirichlet density of a set \(T\) of prime ideals is the limit, when it exists,
\[
\delta_K(T)=\lim_{s\downarrow1}
\frac{\sum_{\mathfrak p\in T}(N\mathfrak p)^{-s}}
 {\log(1/(s-1))}.
\tag{13}
\]
The degree-one set has limit \(1\), and its complement has limit \(0\). This is a statement about prime ideals of \(K\), with their norms; it does not assert density one for a set of rational primes. \(\square\)

## Quadratic factors and concrete residues

Let \(F=\mathbf Q(\sqrt D)\), where \(D\) denotes its fundamental discriminant, and let \(\chi_D(a)=(D/a)\) be the primitive quadratic Kronecker character. The character and the complete splitting law, including primes dividing \(D\), were established in [*Cyclotomic fields*](cyclotomic-fields.md) and *Decomposition of primes in extensions*.

For \(\Re s>1\), the character series and its absolutely convergent product are
\[
L(s,\chi_D)=\sum_{a\geq1}\frac{\chi_D(a)}{a^s}
=\prod_p(1-\chi_D(p)p^{-s})^{-1}.
\]
At a split prime, the two degree-one prime ideals contribute \((1-p^{-s})^{-2}\). At an inert prime, the single degree-two ideal contributes \((1-p^{-2s})^{-1}\). At a ramified prime, the single degree-one ideal contributes \((1-p^{-s})^{-1}\). These are respectively the factors of \(\zeta(s)L(s,\chi_D)\) when \(\chi_D(p)=1,-1,0\). Thus
\[
\zeta_F(s)=\zeta(s)L(s,\chi_D).
\tag{14}
\]
The factor at a ramified prime is included in this identity.

Here is the elementary analytic fact needed to evaluate the second factor at \(1\). If \(c_a\) is a bounded periodic sequence with period sum zero, its partial sums \(B(x)=\sum_{a\leq x}c_a\) are bounded. Partial summation gives
\[
\sum_{a\geq1}c_aa^{-s}
=s\int_1^\infty B(x)x^{-s-1}\,dx,\qquad \Re s>0.
\tag{15}
\]
For a finite cutoff, the missing endpoint is \(B(T)T^{-s}\), which tends to zero. Uniform compact bounds and integrable logarithmic derivatives prove convergence of the series and holomorphy of the integral on \(\Re s>0\). A nontrivial finite-group character has sum zero: multiply the group by an element on which the character is not \(1\). Extending it by zero to nonunits proves that \(\chi_D\) satisfies the hypothesis.

Taking residues in (14), using the residue \(1\) of \(\zeta\), now gives
\[
L(1,\chi_D)=C_F.
\tag{16}
\]
The identity initially holds on \(\Re s>1\), and (15) ensures the finite value needed for this limit.

For the Gaussian field, \(h=1,\ R=1,\ w=4,\ D=-4\). Therefore
\[
L(1,\chi_{-4})=\frac\pi4
=1-\frac13+\frac15-\frac17+\cdots.
\tag{17}
\]
The series is also the integral of \(1/(1+t^2)\) on \([0,1]\): integrate finite geometric sums and let the remainder tend to zero. This checks the archimedean factor in (7).

For \(\mathbf Q(\sqrt5)\), the earlier Minkowski bound gives \(h=1\), and *Dirichlet's unit theorem* gives the fundamental unit \(\varphi=(1+\sqrt5)/2\). With \(R=\log\varphi,\ w=2,\ D=5\), formula (7) becomes
\[
\operatorname*{Res}_{s=1}\zeta_{\mathbf Q(\sqrt5)}(s)
=\frac{2\log\varphi}{\sqrt5}
\approx0.430408941.
\tag{18}
\]
The fundamental unit has norm \(-1\); the ordinary class number and this regulator are the conventions used here.

## The full continuation from the adèle proof

The programme supplies the full proof in *Tate's global theory: continuation and functional equation*, Theorem 9.2 and its uniform theta lemma (source), followed by *Hecke L-functions and the Dedekind zeta function*, Theorem 10.2 and Proposition 10.3 (source). We use these results for the same arbitrary number field \(K\), with its ordinary ideal class number and weighted deleted-row regulator. Set
\[
\Gamma_{\mathbf R}(s)=\pi^{-s/2}\Gamma(s/2),\qquad
\Gamma_{\mathbf C}(s)=2(2\pi)^{-s}\Gamma(s),\qquad
\Lambda_K(s)=|d_K|^{s/2}
\Gamma_{\mathbf R}(s)^{r_1}\Gamma_{\mathbf C}(s)^{r_2}\zeta_K(s).
\tag{19}
\]
**Theorem 16.4.** The function \(\zeta_K\) is meromorphic on \(\mathbf C\), holomorphic away from its simple pole at \(1\), and
\[
\Lambda_K(s)=\Lambda_K(1-s).
\tag{20}
\]
The completed function has only simple poles at \(0\) and \(1\), with respective residues \(-2^{r_1+r_2}h_KR_K/w_K\) and \(2^{r_1+r_2}h_KR_K/w_K\).

**Proof from the programme results.** Write \(D=|d_K|\) and \(m=r_1+r_2\). The test used in the cited adèle proof is the integral-ring indicator at each finite place, \(e^{-\pi x^2}\) at each real place, and \(e^{-2\pi|z|^2}\) at each complex place. Finite multiplicative unit groups have volume one; the infinite multiplicative measures are \(dx/|x|\) and \(2\,du\,dv/(\pi|z|^2)\). Proposition 9.1 and the local Gaussian integrals give, initially on \(\Re s>1\),
\[
Z(f,1,s)=\Gamma_{\mathbf R}(s)^{r_1}
 \Gamma_{\mathbf C}(s)^{r_2}\zeta_K(s).
\]
Thus this is the same Euler product as (3), with exactly the factors in (19).

Theorem 9.2 constructs the continuation by splitting the idèle-class integral at norm one. Its large-norm theta integrals are entire, uniformly on compact parameter sets; Poisson summation turns the small-norm part into the transformed large-norm part and the two additive-zero terms. For the trivial character those terms are
\[
\kappa\left(\frac{\widehat f(0)}{s-1}
                 -\frac{f(0)}s\right),
\qquad \kappa=\operatorname{vol}(\mathcal C_K^1).
\]
Here \(\mathcal C_K^1\) denotes the norm-one idèle classes. The quotient measure uses counting measure on \(K^\times\) and \(dt/t\) in the norm direction. Proposition 10.3 computes its value as \(\kappa=2^mh_KR_K/w_K\), including \(m=1\) and \(R_K=1\). This volume computation uses the algebraic unit lattice and ideal class group; it does not assume the analytic residue (7).

The self-dual additive measures give \(f(0)=1\) and \(\widehat f(0)=D^{-1/2}\). The finite local different factors and the infinite Gaussian transformation give the trivial-character equation in Theorem 10.2; multiplying \(Z(f,1,s)\) by \(D^{s/2}\) makes it precisely (20). The two residues of this product are \(-\kappa\) and \(\kappa\). They are nonzero, and the entire large-norm terms permit no other poles.

To recover the finite zeta function, the reciprocal Gamma factors are entire. Their Euler-product proof is supplied in *Tate's local theory at the infinite places*, section “Mellin continuation without a functional equation,” equations (5)–(6) (source). Consequently dividing the completion introduces no poles. At zero, \(\Gamma_{\mathbf R}(s)=2/s+O(1)\) and \(\Gamma_{\mathbf C}(s)=2/s+O(1)\), so the residue \(-\kappa\) gives
\[
\zeta_K(s)=-\frac{h_KR_K}{w_K}s^{m-1}+O(s^m).
\]
Since \(m\geq1\), this is regular at zero. At one the Gamma factors are finite and nonzero, leaving the simple pole already proved in (7). The continuation agrees with (8) on their common half-plane by the identity theorem. \(\square\)

Equations (19)–(20) are therefore supported by complete written programme proofs. The direct counting argument above remains sufficient for Theorem 16.2 and Corollary 16.3.

## Exercises and complete solutions

**Exercise 1.** Check the residue numerically for \(\mathbf Q(i)\) and \(\mathbf Q(\sqrt{-3})\).

**Solution 1.** For \(\mathbf Q(i)\), the preceding data give \(\pi/4\approx0.7853981634\). For \(\mathbf Q(\sqrt{-3})\), the earlier ideal and unit calculations give \(h=1,\ R=1,\ w=6,\ |D|=3\), so the residue is
\[
\frac{2\pi}{6\sqrt3}=\frac{\pi}{3\sqrt3}
\approx0.6045997881.
\]
These numbers can be checked by character sums with controlled tails. For \(\chi_{-4}\) and \(\chi_{-3}\), ordinary partial sums lie in \([0,1]\). At \(N=20000\) both partial sums are zero. Applying finite partial summation to the tail at \(s=1\) gives
\[
L(1,\chi)-\sum_{a=1}^N\frac{\chi(a)}a
=\int_N^\infty B(x)x^{-2}\,dx,\qquad
0\leq\text{tail}\leq\frac1N.
\tag{21}
\]
The respective truncated sums are approximately \(0.7853731634\) and \(0.6045831222\). With outward rounding, (21) puts their limits in \((0.78537,0.78543)\) and \((0.60458,0.60464)\). Both predicted residues lie inside their certified intervals. Periodicity and the exact rational truncated sums justify the error bounds; numerical agreement alone is not the argument.

**Exercise 2.** Prove Corollary 16.3, including the degree-one assertion.

**Solution 2.** Expand the positive real logarithm of each Euler factor. The terms with exponent \(k=1\) are the required prime sum. For the rest,
\[
\sum_{\mathfrak p}\sum_{k\geq2}
\frac{(N\mathfrak p)^{-ks}}k
\leq2n\sum_p p^{-2}\qquad(s\geq1).
\]
On the other hand (8) gives
\(\log\zeta_K(s)=\log(1/(s-1))+O_K(1)\). Subtracting the bounded remainder proves (10). The primes of degree at least two contribute at most \(n\sum_p p^{-2}\), so removing them leaves the same main term. Division by the denominator in (13) proves the two density statements.

**Exercise 3.** Show that \(\zeta_K(s)>1\) for real \(s>1\), that it tends to \(+\infty\) as \(s\downarrow1\), and that there are infinitely many degree-one prime ideals.

**Solution 3.** The unit ideal contributes \(1\); the distinct ideal \(2O_K\), of norm \(2^n\), contributes \(2^{-ns}>0\). Thus the sum exceeds \(1\). Formula (8), with \(C_K>0\) and bounded holomorphic remainder near \(1\), gives divergence to \(+\infty\). If there were only finitely many degree-one prime ideals, their sum in (10) would remain bounded as \(s\downarrow1\). The complementary sum is bounded by (12), contradicting (10).

**Exercise 4.** Determine the class number of \(\mathbf Q(\sqrt{-5})\) from the residue and a numerical evaluation of \(L(1,\chi_{-20})\).

**Solution 4.** Here \(D=-20,\ R=1,\ w=2\), so (16) gives
\[
h=\frac{2\sqrt5}{\pi}L(1,\chi_{-20}).
\tag{22}
\]
The positive character residues modulo \(20\) are \(1,3,7,9\), and the negative ones are \(11,13,17,19\); all others have value zero. Each period's cumulative sums lie between \(0\) and \(4\). At \(N=20000\), the cumulative sum is zero. Consequently
\[
S_N\leq L(1,\chi_{-20})\leq S_N+\frac4N,\qquad
S_N=\sum_{a=1}^{20000}\frac{\chi_{-20}(a)}a
\approx1.4048629462.
\tag{23}
\]
Outward rounding gives \(1.40486<L(1,\chi_{-20})<1.40507\).

For an integer conclusion, even coarse constants suffice. The exact rational sum and (23) give \(1<L<3/2\). The inequalities \(2<\sqrt5<3\) and \(3<\pi<4\) imply
\[
1<\frac{2\sqrt5}{\pi}<2.
\]
The bounds for \(\pi\) follow, for example, by comparing the circumference of the unit circle with an inscribed regular hexagon and a circumscribed square. Equation (22) therefore yields \(1<h<3\). Since the class number is an integer, \(h=2\). This obtains the answer from the residue calculation without inserting an already known class number into the character sum.

## Proof dependencies and further topics

The ideal-counting asymptotic and its full constant are imported from *Counting ideals of bounded norm*. Earlier lessons supply ideal factorization, quadratic decomposition, primitive Kronecker characters, and the class numbers and units used in the first examples. Basic normal-convergence and holomorphic-integral theorems come from complex analysis.

Theorem 16.4 imports the specific written proofs in adèle lessons 8–10 at the loci above. Their earlier programme dependencies are compactness of the norm-one idèle classes, the unit and ideal-class lattices, self-dual measures, adèlic Poisson summation, local Gaussian and different calculations, and quotient Haar integration. Those inputs remain dependencies of the adèle proofs; this receiving argument does not certify their entire earlier proof chain. Chebotarev's theorem and density laws for specified Frobenius classes are further topics and are not used here.

## References

- *Tate's global theory: continuation and functional equation*, Proposition 9.1, the uniform theta lemma and Theorem 9.2; *Hecke L-functions and the Dedekind zeta function*, Proposition 10.3, Theorem 10.2 and Corollary 10.4. These are the written programme proofs imported for (19)–(20).
- *Tate's local theory at the infinite places*, equations (5)–(6), for the proved entire reciprocal Gamma function and its exact zeros.
- Erich Hecke, [*Vorlesungen über die Theorie der algebraischen Zahlen*](https://archive.org/details/vorlesungenber00heckuoft), 1923, Chapter VI §42: Satz 123, printed p.163, and Satz 124–125, p.164, for the historical real residue limit and ideal Euler product. The complex continuation in (8) is proved above from the quantitative counting error.
- J. S. Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 8, “Applications of the Chebotarev density theorem,” printed pp.149–151, for the broader setting of splitting sets in Galois extensions.
