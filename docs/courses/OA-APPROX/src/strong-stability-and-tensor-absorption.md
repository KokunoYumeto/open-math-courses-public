# Strong stability and tensor absorption

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

An approximately central matrix algebra is a small piece of the hyperfinite factor. Repeatedly placing such pieces in exact relative commutants creates mutually commuting matrix algebras. A summable commutator estimate then forces their infinite product to split off as a spatial tensor factor. This is the mechanism behind strong stability.

We use the central sequence algebra and exact lifting theorem, the [noncommutative-corner theorem](fullness-hypercentrality-and-ultrafilter-corners.md), and the tracial infinite product and [AFD uniqueness](hyperfinite-finite-factors.md) proofs. Other inputs are compact-unitary Haar averaging, finite matrix coordinates and normal state GNS representations. The general theory of weights and conditional expectations stays with its designated prerequisite producer; the finite matrix averages used here are constructed explicitly.

## 1. Stable and strongly stable factors

A factor \(M\) is **stable** if \(M\cong M\bar\otimes M_p(\mathbb C)\) for every positive integer \(p\). It is **strongly stable** if
\[
M\cong M\bar\otimes R,
\tag{1}
\]
where \(R\) is the separable AFD \(\mathrm{II}_1\) factor. These are normal von Neumann algebra isomorphisms.

The product constructions already proved give \(R\bar\otimes R\cong R\). For example, the two countable tracial \(M_2\) strings can be interleaved into one. Also \(M_p\bar\otimes R\cong R\): it is a separable AFD \(\mathrm{II}_1\) factor, so the finite factor uniqueness theorem applies. Therefore strong stability implies stability.

## 2. Averaging a finite matrix factor

Let \(D\subset M\) be a unital copy of \(M_p(\mathbb C)\), with matrix units \(e_{ij}\), and put \(D^c=D'\cap M\). There is a canonical normal matrix decomposition
\[
M\cong M_p(D^c),\qquad
x=\sum_{i,j}e_{ij}a_{ij},\qquad
a_{ij}=\sum_k e_{ki}xe_{jk}\in D^c.
\tag{2}
\]
Indeed, multiplying \(a_{ij}\) on either side by \(e_{ab}\) gives \(e_{ai}xe_{jb}\), so it commutes with every matrix unit. Summing \(e_{ij}a_{ij}\) recovers \(\sum_{i,j}e_{ii}xe_{jj}=x\). Conversely, applying the coefficient formula to \(e_{\ell m}a\), \(a\in D^c\), gives \(\delta_{i\ell}\delta_{jm}a\). The matrix unit relations show multiplicativity and preservation of adjoints. These finite coordinate maps are normal, and identify the algebra with the spatial product \(D\bar\otimes D^c\).

Define
\[
E_D(x)=\int_{\mathcal U(D)}uxu^*\,du
=\frac1p\sum_{i,j}e_{ij}xe_{ji}.
\tag{3}
\]
The second expression follows from (2): Haar averaging a scalar matrix keeps its normalized trace, so on \(D\bar\otimes D^c\) it is \(\operatorname{tr}_p\otimes\operatorname{id}\). The finite formula proves normality and complete positivity directly. It is unital, fixes \(D^c\), has range \(D^c\), and is a \(D^c\)-bimodule map. It is faithful: if \(x\ge0\) and \(E_D(x)=0\), each positive summand \(e_{ij}xe_{ji}\) is zero. In particular \(e_{ii}xe_{ii}=0\) for every \(i\), so \(x^{1/2}e_{ii}=0\) for every \(i\), hence \(x=0\).

**Lemma 2.1.** For every normal functional \(\psi\),
\[
\|\psi-\psi\circ E_D\|
\le p^{3/2}\max_{i,j}\|[e_{ij},\psi]\|.
\tag{4}
\]
If \(M\) has a faithful normal tracial state, then
\[
\|x-E_D(x)\|_2
\le p^{3/2}\max_{i,j}\|[e_{ij},x]\|_2.
\tag{5}
\]

**Proof.** Averaging first gives
\[
\|\psi-\psi\circ E_D\|
\le\int\|\psi-\psi\circ\operatorname{Ad}(u)\|\,du
=\int\|[u,\psi]\|\,du.
\tag{6}
\]
The predual integrand is norm continuous on the compact finite-dimensional unitary group, so this is a Bochner integral inequality. If \(u=\sum\lambda_{ij}e_{ij}\), then
\(\sum|\lambda_{ij}|^2=p\). Cauchy–Schwarz gives
\[
\|[u,\psi]\|
\le\sqrt p\left(\sum_{i,j}\|[e_{ij},\psi]\|^2\right)^{1/2}
\le p^{3/2}\max_{i,j}\|[e_{ij},\psi]\|.
\tag{7}
\]
This proves (4). In the tracial case, integrate
\(\|x-uxu^*\|_2=\|[x,u]\|_2\) and use the identical coefficient estimate. \(\square\)

## 3. Summability produces a spatial tensor factor

**Theorem 3.1.** Let \(M\) have separable predual, without requiring it to be a factor. Let \(D_\nu\subset M\) be mutually commuting unital matrix factors of sizes \(p_\nu\), with infinitely many \(p_\nu\ge2\). Suppose that for a norm-dense sequence of normal states \(\psi_j\),
\[
\sum_{\nu\ge1}\|\psi_j-\psi_j\circ E_{D_\nu}\|<\infty
\qquad\text{for every }j.
\tag{8}
\]
Then
\[
R_0=\bigvee_{\nu\ge1}D_\nu\cong R,\qquad
M\cong R_0\bar\otimes R_0^c,
\quad R_0^c=R_0'\cap M.
\tag{9}
\]

**Proof.** Write \(E_\nu=E_{D_\nu}\). Commuting matrix algebras have commuting conjugation actions, so their averages commute. Each finite composition is a faithful normal conditional expectation onto the intersection of the corresponding commutants.

For \(N\ge m\), put \(F_{m,N}=E_m\cdots E_N\). Commutativity and contractivity give, for \(L>N\),
\[
\|\psi_j\circ F_{m,L}-\psi_j\circ F_{m,N}\|
\le\sum_{\nu=N+1}^L\|\psi_j-\psi_j\circ E_\nu\|.
\tag{10}
\]
To see the individual telescoping bound, move the newest \(E_\nu\) next to \(\psi_j\); the remaining composition is contractive on the predual.
The states' linear span is dense in \(M_*\), and all compositions are contractions. Thus \(\psi\circ F_{m,N}\) converges in norm for every \(\psi\in M_*\). Its bounded predual limit defines a normal map \(T_m:M\to M\). Ultraweak limits at every matrix level preserve positivity, so \(T_m\) is unital completely positive. Its range is
\[
N_m=\bigcap_{\nu\ge m}D_\nu'\cap M.
\tag{11}
\]
Indeed, \(E_\nu T_m=T_m\) for every \(\nu\ge m\); conversely all finite compositions fix (11). Their bimodule property passes to the limit, so \(T_m\) is a conditional expectation onto \(N_m\). Also
\[
\|\psi_j-\psi_j\circ T_m\|
\le\sum_{\nu\ge m}\|\psi_j-\psi_j\circ E_\nu\|
\longrightarrow0.
\tag{12}
\]
Density gives the same convergence for every normal functional; in particular \(T_m(x)\to x\) ultraweakly.

Let \(E=T_1\). Its range is \(R_0^c\). Crucially, \(E\) is faithful. For \(x\ge0\), \(E(x)=0\) implies
\[
(E_1\cdots E_{m-1})(T_m(x))=0.
\tag{13}
\]
The finite head composition is faithful, so \(T_m(x)=0\). Letting \(m\to\infty\) in (12) gives \(x=0\).
Choose a faithful normal state \(\varphi\) on \(M\), and set \(\rho=\varphi\circ E\). This is a faithful normal state.

The finite head \(A_{m-1}=D_1\vee\cdots\vee D_{m-1}\) is a full matrix factor: the unital multiplication representation of the tensor product of its commuting full matrix factors is injective, since that finite full matrix algebra is simple. Formula (2) for \(A_{m-1}\) gives
\[
N_m=A_{m-1}\vee R_0^c.
\tag{14}
\]
In fact, the coefficients of any \(x\in N_m\) commute with the head by (2), and with all tail factors because these commute with the head matrix units. They therefore lie in \(R_0^c\). The converse inclusion is immediate.
Since \(T_m(x)\in N_m\) and converges ultraweakly to \(x\), (14) proves
\[
M=R_0\vee R_0^c.
\tag{15}
\]

On a finite head, \(E\) is its normalized trace: the head averages remove it to a scalar and the remaining averages fix that scalar. Thus \(\rho|_{R_0}\) is the normal tracial product state. Its faithfulness and the trace GNS product construction identify \(R_0\) normally with the tracial infinite product of the \(D_\nu\). Infinitely many nontrivial factors make this a separable AFD \(\mathrm{II}_1\) factor, hence \(R_0\cong R\).
For \(a\) in any finite head and \(b\in R_0^c\), the same average gives
\[
\rho(ab)=\tau_{R_0}(a)\varphi(b).
\tag{16}
\]
Normality extends this to every \(a\in R_0\).

Define on the product of the two normal state GNS spaces
\[
a\Omega_{\tau}\otimes b\Omega_{\varphi|_{R_0^c}}
\longmapsto ab\Omega_\rho.
\tag{17}
\]
Commutation of \(R_0,R_0^c\) and (16) show that inner products factor, so (17) is isometric. By (15) and Kaplansky density, products have dense cyclic span in the GNS space of \(M\), making it onto. It intertwines the two factor actions with their actions in \(M\). All three GNS representations are faithful and normal because their states are faithful normal. Hence (17) implements the spatial isomorphism (9). \(\square\)

The condition on nontrivial matrix factors is necessary for the type conclusion. If only finitely many \(p_\nu\ge2\), the generated \(R_0\) is a finite type I matrix factor. Taking every \(D_\nu=\mathbb C1\) satisfies (8) but gives \(R_0=\mathbb C\). In the absorption application below all sizes are \(2\).

**Theorem 3.2.** If \(M\) instead has a faithful normal tracial state \(\tau\), the same tensor decomposition follows when
\[
\sum_{\nu\ge1}\|x_j-E_\nu(x_j)\|_{2,\tau}<\infty
\tag{18}
\]
for a \(2\)-norm dense sequence in its unit ball. This conclusion also retains nonfactor algebras.

**Proof.** All \(E_\nu\) are trace-preserving \(2\)-norm contractions. Commutativity yields the analogue of (10) on each \(x_j\):
\[
\|F_{m,L}(x_j)-F_{m,N}(x_j)\|_2
\le\sum_{\nu=N+1}^L\|x_j-E_\nu(x_j)\|_2.
\tag{19}
\]
Density and contraction extend Cauchy convergence to every \(x\in M\). The maps' uniform operator norm bounds and completeness of bounded operator balls in the faithful trace \(2\)-topology give limits \(T_m(x)\in M\). These are linear unital completely positive contractions, since bounded \(2\)-convergence gives strong convergence and positivity is strong-closed at every matrix level. They preserve \(\tau\).

They are normal. If \(0\le x_i\uparrow x\), let \(y=\sup_i T_m(x_i)\le T_m(x)\). Trace preservation and normality of \(\tau\) give
\[
\tau(T_m(x)-y)=\tau(x)-\lim_i\tau(x_i)=0,
\tag{20}
\]
so faithfulness gives equality. Their range and bimodule property are (11), by the same commuting-average argument.
Moreover \(T_m(x)\to x\) in \(2\)-norm, by the tails of (18) and density. Thus (14)–(15) hold again.

The head averages show directly
\(\tau(ab)=\tau_{R_0}(a)\tau(b)\) for \(a\in R_0,b\in R_0^c\), first on finite heads and then by normality. Faithful trace GNS now supplies (17) with \(\rho=\tau\). The same infinite product argument identifies \(R_0\cong R\). This proves the entire conclusion without merely substituting a norm in the preceding proof. \(\square\)

## 4. Removing a fixed finite matrix factor

**Lemma 4.1.** If \(M\) is a factor with separable predual and \(D\subset M\) is a unital finite matrix factor, the inclusion \(D^c\subset M\) induces a trace-preserving normal isomorphism
\[
(D^c)_\omega\cong M_\omega.
\tag{21}
\]
Every ordinary centralizing sequence in \(M\) is strong*-equivalent to an ordinary centralizing sequence in \(D^c\).

**Proof.** For a centralizing sequence \(x_n\), ordinary or along \(\omega\), centrality with each fixed matrix unit and (3) give
\[
E_D(x_n)-x_n
=\frac1p\sum_{i,j}[e_{ij},x_n]e_{ji}
\longrightarrow0\quad\text{strong*}.
\tag{22}
\]
Fixed right multiplication preserves bounded strong* convergence. The changed sequence remains centralizing in \(M\) by the strong*-small-change estimate.

For sequences already in \(D^c\), centralizing in \(D^c\) and in \(M\) are equivalent. If \(\eta\in(D^c)_*\), its normal extension \(\eta\circ E_D\) tests the commutator in \(M\), using the bimodule property. Conversely, write any \(z\in M\) in its finite matrix coordinates (2). For \(\psi\in M_*\), put \(\eta_{ij}(a)=\psi(e_{ij}a)\), \(a\in D^c\). The coefficients \(a_{ij}\) of a unit-ball \(z\) have norm at most one: each is the amplification of the corner coefficient \(e_{1i}ze_{j1}\). Since an \(x\in D^c\) commutes with \(e_{ij}\),
\
|[x,\psi|
\le\sum_{i,j}\|[x,\eta_{ij}]\|.
\tag{23}
\]
This proves the converse at either kind of limit.

Bounded strong* convergence of elements of \(D^c\) agrees with that in \(M\), by (2), or by restricting a faithful normal state. Thus inclusion preserves and reflects the zero ideals. It preserves scalar ultraweak limits and the quotient traces. Equation (22) proves surjectivity. A trace-preserving isomorphism of finite von Neumann algebras is normal, by the bounded \(2\)-norm characterization. Finally \(D^c\) is a factor with separable predual by (2), so its central sequence algebra uses exactly the same hypotheses. \(\square\)

## 5. Constructing commuting matrix pieces

**Theorem 5.1.** For a factor \(M\) with separable predual, the following are equivalent:

1. \(M\) is strongly stable.
2. \(M_\omega\) is noncommutative for some free ultrafilter.
3. \(M_\omega\) is noncommutative for every free ultrafilter.
4. \(M_\omega\) is type \(\mathrm{II}_1\) for some, equivalently every, free ultrafilter.
5. \(C(M)\ne H(M)\).
6. \(M\) has an ordinary centralizing sequence of mutually commuting unital two-by-two matrix unit systems.

**Proof.** The preceding hypercentrality and corner theorems equate statements 2–5. We prove the remaining implications constructively.

Suppose \(M\cong N\bar\otimes R\), as follows from statement 1 with \(N=M\). The matrix units in successive \(M_2\) legs of \(R\) form mutually commuting ordinary centralizing sequences. In the product, \(1\otimes e_{ij}(n)\) remains centralizing: on an elementary normal functional \(\eta\otimes\zeta\) its commutator norm is bounded by \(\|\eta\|\|[e_{ij}(n),\zeta]\|\). Finite sums of elementary normal functionals are norm dense in the spatial tensor predual, by approximating its vector functionals with finite tensor sums. Uniform bounds complete the assertion. Transfer by the normal isomorphism gives statement 6.

Conversely, given statement 6, select a subsequence of its matrix systems so that, for a norm-dense normal state sequence \(\psi_j\),
\[
\max_{i,j}\|[e_{ij}(n),\psi_k]\|\le2^{-n},
\qquad k\le n.
\tag{24}
\]
Mutual commutation survives the subsequence. By Lemma 2.1, the corresponding matrix averages satisfy (8). Theorem 3.1 gives \(M\cong R\bar\otimes R^c\). Therefore
\[
M\bar\otimes R
\cong R^c\bar\otimes R\bar\otimes R
\cong R^c\bar\otimes R
\cong M,
\tag{25}
\]
giving strong stability.

It remains to construct statement 6 from statement 4. Fix \(\omega\). The general halving theorem in the finite type \(\mathrm{II}_1\) algebra \(M_\omega\) gives a unital \(M_2\) system; its center need not be scalar. We build matrix factors \(D_n\) inductively, each commuting with the previously generated finite head \(A_{n-1}\), and satisfying (24).

At the first step, lift that quotient \(M_2\) system to exact coordinate matrix units in \(M\). Their \(\omega\)-centralizing property lets us choose one coordinate satisfying the first finite set of tests. Suppose \(D_1,\ldots,D_{n-1}\) have been chosen. Their commuting unital product \(A_{n-1}\) is a finite matrix factor. Lemma 4.1 identifies its relative commutant's central sequence algebra with \(M_\omega\), so a unital \(M_2\) system exists there. Exact lifting inside \(A_{n-1}'\cap M\) gives matrix units that centralize as sequences in \(M\), by (23). Choose one coordinate satisfying (24) for \(k\le n\). It commutes exactly with the entire preceding head.

This induction produces the required mutually commuting systems. The finite tests and their bounds imply ordinary centralizing for every normal functional. This proves statement 6 and completes the equivalence. \(\square\)

For a fixed size \(p\ge2\), an ordinary centralizing sequence of mutually commuting unital \(p\)-by-\(p\) systems gives the same absorption conclusion: replace \(2^{3/2}\) by \(p^{3/2}\) in (4) and use the tracial infinite \(M_p\) product. The size-one case supplies no absorption information.

## 6. Exercises with complete solutions

**Exercise 1.** Verify the coefficient recovery formula in (2) on \(x=e_{\ell m}a\), with \(a\in D^c\).

*Solution.* The coefficient at \(i,j\) is
\(\sum_k e_{ki}e_{\ell m}a e_{jk}
=\delta_{i\ell}\delta_{mj}\sum_k e_{kk}a
=\delta_{i\ell}\delta_{mj}a\).
Thus each matrix coefficient is recovered exactly. Summing \(e_{ij}\) times those coefficients returns \(e_{\ell m}a\).

**Exercise 2.** Derive the constant \(p^{3/2}\) from a unitary's scalar matrix coefficients.

*Solution.* A unitary \(p\)-by-\(p\) matrix has squared Hilbert–Schmidt norm \(p\), so \((\sum|\lambda_{ij}|^2)^{1/2}=\sqrt p\). There are \(p^2\) commutator coefficients, whose square-sum norm is at most \(p\) times their maximum. Multiplying gives \(\sqrt p\,p=p^{3/2}\).

**Exercise 3.** In Theorem 3.1, explain why summability for each dense state suffices for every normal functional's Cauchy property.

*Solution.* Finite linear combinations of the dense states are norm dense in \(M_*\), by positive-functional decomposition. For such a combination, use (10) term by term. Given an arbitrary \(\psi\), approximate it by one such combination \(\eta\). Since both compositions have predual norm at most one, their difference applied to \(\psi-\eta\) has norm at most \(2\|\psi-\eta\|\). First choose the approximation, then make the Cauchy tail for \(\eta\) small.

**Exercise 4.** Prove that the infinite average \(E\) is faithful using the tail maps, and explain why faithfulness of the finite averages alone would not justify the conclusion.

*Solution.* For positive \(x\) with \(E(x)=0\), (13) and faithfulness of the finite head give \(T_m(x)=0\) for every \(m\). Since \(T_m(x)\to x\) ultraweakly, \(x=0\). A limit of faithful positive maps can lose faithfulness; this argument uses the tail convergence guaranteed by the summability hypothesis, rather than passing faithfulness through a limit without proof.

**Exercise 5.** Show why infinitely many nontrivial \(D_\nu\) are needed for \(R_0\cong R\).

*Solution.* If all \(D_\nu=\mathbb C1\), every average is the identity and (8) holds with sum zero, but \(R_0=\mathbb C\). More generally finitely many nontrivial factors generate a finite full matrix algebra. Infinitely many factors of size at least two give arbitrarily large finite matrix stages and the diffuse tracial infinite product, which is type \(\mathrm{II}_1\).

**Exercise 6.** Verify the isometry of the GNS map (17) on two product vectors.

*Solution.* Their inner product after mapping is
\(\rho((ab)^*a'b')=\rho(a^*a'b^*b')\),
because the two algebras commute. Equation (16) makes this
\(\tau(a^*a')\varphi(b^*b')\), which is exactly the product Hilbert-space inner product. Bilinearity handles finite sums, so the map extends isometrically.

**Exercise 7.** In the finite-trace proof, show that trace preservation forces normality of a positive limit map.

*Solution.* For \(x_i\uparrow x\), positivity gives \(y=\sup T(x_i)\le T(x)\). Normality of the original faithful trace gives
\(\tau(y)=\lim\tau(T(x_i))=\lim\tau(x_i)=\tau(x)=\tau(T(x))\).
Thus the positive difference \(T(x)-y\) has trace zero and is zero by faithfulness. Preservation of increasing positive suprema is normality.

**Exercise 8.** Given (24), prove (8) for each fixed \(\psi_k\).

*Solution.* For \(n\ge k\), Lemma 2.1 with size two bounds the \(n\)-th defect by \(2^{3/2}2^{-n}\). Their sum is finite. There are only finitely many terms with \(n<k\), each bounded by \(2\|\psi_k\|=2\), so the entire sum is finite.

**Exercise 9.** Why can the induction choose \(D_n\) in the exact relative commutant, even though the original information is asymptotic?

*Solution.* The finite-head removal isomorphism (21) transfers the exact quotient \(M_2\) system into the central sequence algebra of \(A_{n-1}'\cap M\). The exact matrix lifting theorem then gives coordinate systems already lying in that relative commutant. Selecting one coordinate for the finite functional tests does not change this exact membership. Thus asymptotic centralizing controls the errors, while relative commutant membership ensures exact commutation.

**Exercise 10.** Give a stable factor which is not strongly stable.

*Solution.* \(B(\ell^2(\mathbb N))\bar\otimes M_p\cong B(\ell^2(\mathbb N)\otimes\mathbb C^p)\cong B(\ell^2(\mathbb N))\) for every finite \(p\), by a Hilbert-space unitary. It is therefore stable. Its central sequence algebra is \(\mathbb C\), as proved by the rank-one tests in the preceding lifting lesson. Theorem 5.1 excludes strong stability.

## References

Alain Connes, [*Outer conjugacy classes of automorphisms of factors*](https://numdam.org/item/ASENS_1975_4_8_3_383_0.pdf), Lemmas 2.3.5–2.3.6, printed pp.406–407 (PDF pp.25–26), is the free comparison source for finite matrix averaging and summability. Its matrix-functional estimate has constant p². Lemma 2.1 here proves the sharper p^(3/2) bound by averaging the finite matrix coefficients. Theorem 3.1 proves the full normal-functional summability construction for algebras with separable predual, retaining a nontrivial center; infinitely many nontrivial matrix factors are required. Theorem 3.2 supplies the separate finite-trace 2-norm construction.

The proof here establishes faithfulness from the tail maps, proves generation by the tensor factor and its relative commutant, and constructs the spatial isomorphism in the product GNS representation. These steps fill in the finite-factor and modular splitting references used in Connes's proof. The tracial infinite-product construction and finite AFD uniqueness remain separately recorded prerequisites, rather than being declared proved by that citation.

Connes's Theorem 2.2.1 and Lemma 2.2.2, printed pp.400–402 (PDF pp.19–21), compare the central-sequence conditions. Its final absorption implication cites Araki. Here Lemma 4.1 proves finite-head removal in full, and Theorem 5.1 constructs commuting matrix pieces by exact coordinate lifting before applying the summability theorem. The type II₁ central sequence algebra can have nontrivial center; its halving prerequisite retains that scope. The [companion automorphism lesson](centrally-trivial-automorphisms-and-decreasing-afd-factors.md) supplies the additional quotient-group and decreasing-subfactor results. No restricted edition is used as construction material and no primary source expression is imported.
