# Ordinary multipliers and predual compactness

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text: public domain (CC0).*

Ordinary convergence gives a multiplier algebra that works for every free ultrafilter simultaneously. Its small-vector test must control both adjoints. Its predual counterpart is relative weak compactness of quadratic functional orbits; it does not assert preservation of every weakly-null sequence of functionals.

Let \(M\ne0\) have a faithful normal state \(\varphi\). No factor or separable-predual hypothesis is imposed. Put
\[
\|x\|_\varphi=\varphi(x^*x)^{1/2},\qquad
\|x\|_\#=\left(\frac{\varphi(x^*x)+\varphi(xx^*)}{2}\right)^{1/2}.
\tag{1}
\]
The latter gives strong* convergence on bounded sets. We use the predual weak compactness theorem: a set \(K\subset M_*\) is relatively weakly compact precisely when it is norm bounded and there is \(\rho\in M_*^+\) such that, for every \(\varepsilon>0\), some \(\delta>0\) makes
\[
\|x\|\le1,\quad \rho(x^*x+xx^*)<\delta
\ \Longrightarrow\
\sup_{\psi\in K}|\psi(x)|<\varepsilon.
\tag{2}
\]
This is the selected weak compactness result from the foundations course, with its full proof compared. It is also a form of Akemann's predual compactness theorem. Normality, functional polar decomposition, Banach weak compactness and the faithful-state bounded topology are its declared prerequisites.

## 1. The ordinary ideal and its multiplier test

Define
\[
I_\infty=\{(z_n)\in\ell^\infty(\mathbb N,M):\|z_n\|_\#\to0\},
\qquad
N_\infty=\{a:aI_\infty\subset I_\infty,\ I_\infty a\subset I_\infty\}.
\tag{3}
\]
The bounded strong* description makes \(I_\infty\) independent of \(\varphi\). It is a norm-closed self-adjoint algebra, and \(N_\infty\) is a unital \(C^*\)-algebra with \(I_\infty\) as a closed two-sided ideal. The coordinate central projections supported at one index identify it with the abstract multiplier algebra of \(I_\infty\), exactly as in the [ultrafilter proof](multiplier-ultraproducts-and-normal-embeddings.md#proposition-1-1). The proof uses coordinate support identities, rather than a supposed norm approximate identity of finite-coordinate projections.

**Theorem 1.1.** A bounded sequence \(a=(a_n)\) belongs to \(N_\infty\) if and only if, for every \(\varepsilon>0\), there are \(\delta>0\) and \(N\) such that
\[
n\ge N,\quad\|x\|\le1,\quad\|x\|_\#<\delta
\ \Longrightarrow\
\|a_nx\|_\#+\|xa_n\|_\#<\varepsilon.
\tag{4}
\]
Equivalently one may test the two nonautomatic one-sided seminorms
\[
\|xa_n\|_\varphi+\|xa_n^*\|_\varphi<\varepsilon.
\tag{5}
\]
Each condition can also be made uniform over all \(n\), by shrinking \(\delta\) for the finitely many initial operators.

**Proof.** The symmetric test directly makes both products with a bounded strong*-null sequence vanish; rescale it to a contraction sequence. Conversely, if (4) fails, choose \(\varepsilon>0\), increasing indices \(n_j\), and contractions \(x_j\) with \(\|x_j\|_\#<1/j\) but
\[
\|a_{n_j}x_j\|_\#+\|x_ja_{n_j}\|_\#\ge\varepsilon.
\tag{6}
\]
Use \(z_{n_j}=x_j\) and \(z_n=0\) elsewhere. Then \(z\in I_\infty\), whereas at least one of its two product seminorms fails to tend to zero. This contradicts the multiplier property.

For the equivalence with (5), let \(C=\sup_n\|a_n\|\). The estimates
\[
\|a_nx\|_\varphi\le C\|x\|_\varphi,\qquad
\|a_n^*x\|_\varphi\le C\|x\|_\varphi
\tag{7}
\]
are automatic. The remaining square seminorms of the two products are \(\|xa_n\|_\varphi\) and, after replacing \(x\) by \(x^*\), \(\|xa_n^*\|_\varphi\). Thus (5), (7) and the symmetric formula give (4) after adjusting constants. The converse follows by applying (4) to \(a\) and its adjoint. Adjoint sequences are multipliers because (3) is self-adjoint.

Finally each fixed multiplication map preserves bounded strong* convergence, so for the finite initial set one can take a common positive modulus. Its minimum with the tail modulus works for all indices. \(\square\)

**Corollary 1.2.** A bounded sequence lies in \(N_\infty\) if and only if it lies in \(N_\omega\) for every free ultrafilter \(\omega\).

**Proof.** A uniform tail modulus in (4) is an ultrafilter modulus for every \(\omega\), proving one implication. If ordinary membership fails, use the witness sequence in (6) and a free ultrafilter containing \(\{n_j:j\ge1\}\). The same null sequence is in \(I_\omega\), while its product-seminorm sum has ultralimit at least \(\varepsilon\). Thus \(a\notin N_\omega\) for that filter. \(\square\)

## 2. A faithful-state version of predual compactness

**Lemma 2.1.** Under the faithful-state hypothesis, (2) is equivalent to norm boundedness of \(K\) and the test
\[
\forall\varepsilon>0\ \exists\delta>0:\quad
\|x\|\le1,\ \|x\|_\#<\delta
\ \Longrightarrow\ \sup_{\psi\in K}|\psi(x)|<\varepsilon.
\tag{8}
\]

**Proof.** If (8) holds, use \(\rho=\varphi\) in (2), with the factor two in (1). Conversely take the controlling \(\rho\) from (2). On the unit ball, a small \(\varphi\)-symmetric seminorm makes \(\rho(x^*x+xx^*)\) uniformly small: otherwise there would be a contraction sequence with its first seminorm tending to zero and the second bounded away from zero. That contradicts the faithful-state characterization of bounded strong* convergence. The resulting modulus gives (8). \(\square\)

Here “relatively weakly compact” means that the weak closure is compact in \(\sigma(M_*,M)\). A union need not itself be closed or compact.

For \(a=(a_n)\), define the normal functional maps
\[
F_n(\psi)(x)=\psi(a_n^*xa_n),\qquad
G_n(\psi)(x)=\psi(a_nxa_n^*).
\tag{9}
\]
This explicit definition fixes both functional multiplication conventions.

## 3. The valid compactness characterization

**Theorem 3.1.** For a bounded sequence \(a_n\), the following are equivalent:

1. \(a\in N_\infty\).
2. Both sets \(\{F_n(\varphi):n\ge1\}\) and \(\{G_n(\varphi):n\ge1\}\) are relatively weakly compact in \(M_*\).
3. For every relatively weakly compact \(K\subset M_*\), both
\(\bigcup_nF_n(K)\) and \(\bigcup_nG_n(K)\) are relatively weakly compact.

It is enough in the last condition to test weakly compact \(K\).

**Proof of 1 implies 3.** Write \(C=\sup_n\|a_n\|\). If \(C=0\), the orbit unions consist of zero and the assertions are immediate. Assume \(C>0\). The multiplier criterion for \(a\) and \(a^*\) makes
\[
x\longmapsto a_n^*xa_n,\qquad x\longmapsto a_nxa_n^*
\tag{10}
\]
uniformly strong*-continuous at zero on the unit ball. To check the first, first make \(xa_n\) small with the common multiplier modulus, and then multiply on the left by \(a_n^*\), using its common modulus after rescaling the intermediate norm bound. The second is identical. Finite initial maps were included in Theorem 1.1.

For \(K\), Lemma 2.1 gives a common small symmetric-seminorm test making every \(\psi\in K\) small. The operators in (10) have norm at most \(C^2\); rescale that test and compose its modulus with the preceding uniform continuity. This yields (8) for each orbit union in condition 3. Both unions are bounded by \(C^2\sup_{\psi\in K}\|\psi\|\). Lemma 2.1 proves their relative weak compactness.

**Proof of 3 implies 2.** Use \(K=\{\varphi\}\).

**Proof of 2 implies 1.** Lemma 2.1 makes both positive orbit families uniformly small on contractions of small symmetric seminorm. For a contraction \(x\),
\[
\|x^*x\|_\#^2=\varphi((x^*x)^2)
\le\varphi(x^*x)\le2\|x\|_\#^2.
\tag{11}
\]
Apply the common functional test to \(x^*x\). By (9),
\[
\begin{aligned}
\|xa_n\|_\varphi^2&=F_n(\varphi)(x^*x),\\
\|xa_n^*\|_\varphi^2&=G_n(\varphi)(x^*x).
\end{aligned}
\tag{12}
\]
Both are uniformly small when \(\|x\|_\#\) is small. This gives (5) and hence membership.

Finally, testing compact \(K\) suffices because the weak closure of a relatively compact set is compact and contains that set. \(\square\)

The two positive orbit families encode the two adjoint directions that a nontracial multiplier requires. The last condition transfers relative compactness of a set of functionals, rather than specifying the limit of an individually moving functional.

## 4. A scalar test that omits the adjoint

In \(M=B(\ell^2(\mathbb N_0))\), use the basis \(\xi_j\), \(p_j=|\xi_j\rangle\langle\xi_j|\), and
\[
\varphi(x)=\sum_{j\ge0}\lambda_j\langle\xi_j,x\xi_j\rangle,
\qquad \lambda_j=2^{-j-1}.
\tag{13}
\]
Let \(a_n=|\xi_0\rangle\langle\xi_n|\). For any contraction \(x\),
\[
\|a_nx\|_\varphi\le\|x\|_\varphi\le\sqrt2\|x\|_\#,
\qquad
\|xa_n\|_\varphi=\sqrt{\lambda_n}\|x\xi_0\|\le\sqrt{\lambda_n}.
\tag{14}
\]
Thus the test \(\|a_nx\|_\varphi+\|xa_n\|_\varphi<\varepsilon\), with small \(\|x\|_\#\) and large \(n\), holds. But \(p_n\to0\) strong*, whereas
\[
a_np_n=a_n,\qquad
\|a_n\|_\#^2=(\lambda_n+\lambda_0)/2\ge1/4.
\tag{15}
\]
So \(a\notin N_\infty\). The omitted adjoint direction is essential. The symmetric test (4), or the two right-multiplication tests (5), retains both required adjoint directions.

## 5. Weakly-null functionals need not stay weakly null

Take the Bernoulli probability space
\[
\Omega=\{-1,1\}^{\mathbb N},\qquad
M=L^\infty(\Omega,\mu),\quad \varphi(f)=\int f\,d\mu.
\tag{16}
\]
Let \(r_n\) be its \(n\)-th coordinate function, \(a_n=(1+r_n)/2\), and
\(\psi_n(f)=\int r_nf\,d\mu\). The \(r_n\) are orthonormal in \(L^2\). Since every \(f\in L^\infty\) lies in \(L^2\), Bessel's inequality gives \(\psi_n(f)\to0\); thus \(\psi_n\to0\) weakly in \(M_*=L^1\).

This finite commutative algebra has a faithful normal trace. Every bounded sequence is a multiplier, because both tracial \(2\)-norm multiplication inequalities are bounded by its operator norm. In particular \(a\in N_\infty\). Nevertheless
\[
F_n(\psi_n)(1)=G_n(\psi_n)(1)
=\int r_na_n^2\,d\mu
=\frac12.
\tag{17}
\]
Neither transformed sequence is weakly null. Thus multiplier membership does not imply that every weakly null sequence of normal functionals remains weakly null under the two transformations, even in a finite commutative algebra. Theorem 3.1 asserts relative compactness, which permits nonzero weak cluster points.

The orbit union in the compactness criterion also needs its weak closure. For \(M=\mathbb C\), \(a_n=1/n\) and \(K=\{\varphi\}\), the orbit is
\[
\{\varphi/n^2:n\ge1\}.
\tag{18}
\]
It omits its weak limit zero, so is not weakly compact. Its closure is compact. Thus even the valid compactness equivalence requires **relatively** weakly compact orbit unions, or their weak closures.

## 6. Exercises with complete solutions

**Exercise 1.** Show that the ordinary null algebra has the same coordinate multiplier identification as the ultrafilter null algebra.

*Solution.* Each one-coordinate projection belongs to \(I_\infty\), is central there, and has a unital coordinate algebra \(M\). For an abstract multiplier \(m\), its products with that projection agree and define a bounded coordinate \(a_n\). Coordinates of \(mz,zm\) are \(a_nz_n,z_na_n\), so the multiplier is exactly a relative normalizer sequence. Coordinate tests and the product norm bounds give the isometric identification.

**Exercise 2.** Why does the witness in (6) give an ordinary null sequence?

*Solution.* The nonzero entries occur at increasing \(n_j\), and their seminorms are less than \(1/j\). Every sufficiently large coordinate is either zero or belongs to a sufficiently high witness index. Hence its seminorm tends ordinarily to zero. The uniform lower product bound persists at those witness coordinates.

**Exercise 3.** Identify the automatic and nonautomatic seminorms of \(a_nz_n,z_na_n\).

*Solution.* The first seminorm of \(a_nz_n\) is bounded by \(C\|z_n\|_\varphi\). The adjoint seminorm of \(z_na_n\) is bounded by \(C\|z_n^*\|_\varphi\). The remaining two are \(\|z_na_n\|_\varphi\) and \(\|z_n^*a_n^*\|_\varphi\), requiring right multiplication by both \(a_n\) and \(a_n^*\).

**Exercise 4.** Prove the all-free-ultrafilters criterion when ordinary membership fails.

*Solution.* Choose the witness subsequence from (6) and a free ultrafilter containing its index set. The same input sequence is null along that filter, whereas the product-seminorm sum stays at least \(\varepsilon\) on its large set. Thus at least one multiplier condition fails for that filter.

**Exercise 5.** Why can the controlling normal functional in (2) be replaced by \(\varphi\) on bounded inputs?

*Solution.* If no such modulus existed, choose contractions with symmetric \(\varphi\)-seminorm tending to zero but the desired controlling seminorm bounded away from zero. The faithful-state criterion makes those contractions strong*-null, which makes every fixed normal positive seminorm tend to zero. This contradiction gives the common modulus.

**Exercise 6.** Check the positive-square estimate (11).

*Solution.* For a contraction \(x\), \(0\le x^*x\le1\), hence \((x^*x)^2\le x^*x\). The operator \(x^*x\) is self-adjoint, so its symmetric seminorm squared is \(\varphi((x^*x)^2)\). Formula (1) bounds \(\varphi(x^*x)\) by \(2\|x\|_\#^2\).

**Exercise 7.** Explain why compactness of the two state orbits suffices for all weakly compact \(K\).

*Solution.* The state orbit test gives both right-multiplication moduli through (12), hence the full multiplier condition. Its composition controls the quadratic operator maps (10) uniformly on bounded small inputs. Every relatively compact \(K\) has its common functional modulus by Lemma 2.1. Composing these moduli proves relative compactness of both full orbit unions.

**Exercise 8.** Compute the lower bound in the missing-adjoint example.

*Solution.* Here \(a_n^*a_n=p_n\) and \(a_na_n^*=p_0\). Their state values are \(\lambda_n,\lambda_0=1/2\); averaging gives (15), with lower bound \(1/4\). Meanwhile \(\|p_n\|_\#^2=\lambda_n\to0\), so multiplication truly fails on a bounded strong*-null sequence.

**Exercise 9.** Verify weak convergence of the Bernoulli functionals against every element of \(M\).

*Solution.* Bessel's inequality gives \(\sum_n|\int r_nf\,d\mu|^2\le\|f\|_2^2\) for each \(f\in L^2\). Thus each coefficient tends to zero. Every \(L^\infty\) function is in \(L^2\) because \(\mu\) is a probability measure. These are all the test elements of \((M_*)^*=M\), so the convergence is the full Banach weak convergence.

**Exercise 10.** Compute the transformed Bernoulli functional at \(1\).

*Solution.* Since \(r_n^2=1\), \(a_n^2=a_n=(1+r_n)/2\). Therefore \(r_na_n=(r_n+1)/2\). Integrating gives \(1/2\), since \(\int r_n=0\). This is the nonzero value in (17).

**Exercise 11.** Why does the orbit in (18) fail to be weakly compact?

*Solution.* In the one-dimensional predual, weak and norm topologies agree. The sequence \(\varphi/n^2\) converges to zero, which is absent from the orbit. A compact set in a Hausdorff space is closed, so that orbit cannot be compact. Its closure, obtained by adjoining zero, is compact.

**Exercise 12.** What is the valid conclusion for a weakly-null sequence \(\psi_n\) under multiplier membership?

*Solution.* The set \(\{\psi_n:n\ge1\}\cup\{0\}\) is weakly compact. Theorem 3.1 makes both full transformed orbit unions relatively weakly compact, hence also the two diagonal sequences \(F_n(\psi_n),G_n(\psi_n)\). It supplies weakly convergent subsequences. It does not force their limits to be zero; (17) prevents that conclusion.

## References

C. A. Akemann, [*The dual space of an operator algebra*](https://www.ams.org/journals/tran/1967-126-02/S0002-9947-1967-0206732-8/S0002-9947-1967-0206732-8.pdf), *Transactions of the American Mathematical Society* 126 (1967), 286–302, Theorem II.3 and Lemmas II.3a–II.3c, supplies the controlling-functional compactness proof. That proof relies on the normal/singular decomposition, commutative compactness and the Eberlein–Šmulian theorem.

Adrian Ocneanu, [*Actions of discrete amenable groups on factors*](https://wrap.warwick.ac.uk/id/eprint/110062/1/WRAP_Theses_Ocneanu_1982.pdf), Section 5.1, printed p.47 (PDF p.61), states its ultrafilter multiplier criterion for separable preduals. Section 1 here proves the full ordinary-convergence criterion and the all-free-ultrafilters equivalence directly. The rank-one, Bernoulli and one-dimensional examples fully establish why both adjoints, relative compactness and the absence of a prescribed weak limit matter. No factor or separable-predual assumption is added.

