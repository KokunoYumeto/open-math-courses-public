# The multiplicative group of a local field

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is not yet recorded. Public domain (CC0).*

*NT-ADL bundled edition, source-reconciled on 5 October 2026 by GPT-6.1 Sol (OpenAI), Ultra. This adaptation retains the provider lesson's mathematical scope and adds the source comparisons identified below. The upstream provider draft is unchanged. Original AI-written exposition is CC0; human reference works and genuinely reused human expression retain their own terms.*

A local field's multiplicative group has one discrete direction, a finite group visible in its residue field, and a compact group of principal units. In characteristic zero, a sufficiently deep part of that last group becomes additive under the logarithm. This determines its rank, its torsion and the exact index of every power subgroup. In characteristic \(p\), taking \(p\)-th powers behaves very differently.

Let \(K\) be a nonarchimedean local field. Write \(\mathcal O\) for its integer ring, \(\mathfrak m=(\pi)\) for its maximal ideal, \(\kappa=\mathbf F_q\) for its residue field, with \(q=p^f\), and normalize \(v(K^\times)=\mathbf Z\). Put
\[
U=\mathcal O^\times,\qquad U^0=U,\qquad U^r=1+\mathfrak m^r\quad(r\geq1).
\]
The absolute value in the power-index formula will be the Haar-normalized one,
\[
|x|_K=q^{-v(x)}.
\tag{0.1}
\]
We use **Local fields: classification and Haar measure** and **Unramified and totally ramified extensions** for the field classification, completeness, finite residue field and integral-basis results.

## 1. Three factors and the unit filtration

**Proposition 1.1.** A choice of uniformizer gives a topological group isomorphism
\[
K^\times\simeq\pi^{\mathbf Z}\times\mu_{q-1}(K)\times U^1.
\tag{1.1}
\]
Here \(\pi^{\mathbf Z}\simeq\mathbf Z\) has the discrete topology, and reduction identifies \(\mu_{q-1}(K)\) with \(\kappa^\times\). Moreover,
\[
U/U^1\simeq\kappa^\times,\qquad
U^r/U^{r+1}\simeq(\kappa,+)\quad(r\geq1).
\tag{1.2}
\]
The group \(U^1\) is a compact abelian pro-\(p\) group.

*Proof.* Every \(x\ne0\) has the unique form \(x=\pi^{v(x)}u\), \(u\in U\). The valuation fibers are open, so this is a topological product with the discrete valuation factor.

Simple-root Hensel lifting gives a unique root of \(X^{q-1}-1\) over every nonzero residue class. Denote this lift by \([a]\). Uniqueness gives \([a][b]=[ab]\), so these lifts form \(\mu_{q-1}(K)\) and reduction is an isomorphism. For \(u\in U\), the quotient \(u/[\bar u]\) lies in \(U^1\). This factorization is unique; residue classes are open, so it and its inverse are continuous. This proves (1.1) and the first quotient in (1.2).

For the second quotient use
\[
(1+a\pi^r)U^{r+1}\longmapsto\bar a.
\]
Products add coefficients modulo \(\mathfrak m^{r+1}\), because \(2r\geq r+1\). The kernel and surjectivity are immediate. This coordinate isomorphism uses \(\pi\).

The groups \(U^r\) form a neighborhood basis of identity and have intersection \(\{1\}\). Completeness and compactness give
\[
U^1\simeq\varprojlim_{r\geq1}U^1/U^r.
\tag{1.3}
\]
For example, a compatible sequence of cosets specifies a Cauchy sequence of units and its unique limit. Successive quotient sizes show that \(U^1/U^r\) has order \(q^{r-1}\), a power of \(p\). Hence (1.3) makes \(U^1\) pro-\(p\). \(\square\)

There is consequently a canonical \(\mathbf Z_p\)-module structure on \(U^1\), written multiplicatively. For \(a\in\mathbf Z_p\), define \(u^a\) by taking integer powers whose exponents converge to \(a\). In any fixed finite quotient in (1.3), sufficiently close exponents give the same power, since that quotient has \(p\)-power exponent. This proves existence, independence of the integer approximation, and joint continuity of \((a,u)\mapsto u^a\). The module identities follow from the integer ones in every finite quotient.

## 2. Logarithm and exponential in characteristic zero

Assume now that \(K\) has characteristic zero. It is finite over \(\mathbf Q_p\). Put
\[
e=v(p),\qquad d=[K : \mathbf Q_p]=ef.
\]
For integers \(j\ne0\), \(v(j)=e\,v_p(j)\).

Define the series
\[
\log(1+x)=\sum_{j\geq1}\frac{(-1)^{j+1}x^j}{j},
\qquad
\exp(z)=\sum_{j\geq0}\frac{z^j}{j!}.
\tag{2.1}
\]

**Proposition 2.1 (convergence and the deep-unit isomorphism).** The logarithm converges for \(v(x)>0\) and defines a continuous homomorphism \(U^1\to(K,+)\). The exponential converges for
\[
v(z)>\frac e{p-1}.
\]
For every integer \(r>e/(p-1)\), the maps
\[
\log:U^r\longrightarrow\mathfrak m^r,\qquad
\exp : \mathfrak m^r\longrightarrow U^r
\tag{2.2}
\]
are mutually inverse topological group isomorphisms. For nonzero inputs in this range,
\[
v(\log(1+x))=v(x),\qquad
v(\exp(z)-1)=v(z).
\tag{2.3}
\]

*Proof.* If \(a=v(x)>0\), then
\[
v(x^j/j)=ja-e\,v_p(j)\geq ja-e\log_p j\longrightarrow\infty.
\]
In a complete nonarchimedean field a series converges when its terms tend to zero: the valuation of a finite tail is at least the least valuation of its terms. Thus the logarithm converges. This bound is uniform for \(v(x)\geq1\), so the partial polynomials converge uniformly there and the resulting function is continuous.

Count the multiples of \(p,p^2,\ldots\) among \(1,\ldots,j\). This gives
\[
v_p(j!)=\sum_{k\geq1}\left\lfloor j/p^k\right\rfloor
=\frac{j-s_p(j)}{p-1}\leq\frac{j-1}{p-1},
\tag{2.4}
\]
where \(s_p(j)\geq1\) is the sum of the base-\(p\) digits of \(j\). Consequently, if \(a=v(z)>e/(p-1)\),
\[
v(z^j/j!)\geq
a+(j-1)\left(a-\frac e{p-1}\right)\longrightarrow\infty.
\]
This proves exponential convergence, uniformly on every \(\mathfrak m^r\) in (2.2). For \(j>1\), each exponential term has value strictly greater than \(a\), so its linear term alone has least value. This gives the second equality in (2.3).

We also have \(v_p(j)\leq(j-1)/(p-1)\). To see it, write \(j=p^k b\) with \(p\nmid b\); then \(j-1\geq p^k-1\geq k(p-1)\). The same estimate for logarithm terms shows that, in the deep range, every term after \(x\) has strictly larger value. This gives the first equality in (2.3) and shows that both maps have the indicated targets.

For completeness, the formal identities used here are
\[
\begin{aligned}
\log((1+X)(1+Y))&=\log(1+X)+\log(1+Y),\\
\exp(X+Y)&=\exp(X)\exp(Y),\\
\exp(\log(1+X))&=1+X,\qquad
\log(\exp X)=X.
\end{aligned}
\tag{2.5}
\]
They are identities over \(\mathbf Q\): formal differentiation and the constant terms prove the logarithm and inverse identities, while the binomial formula proves the exponential identity.

Their evaluations are legitimate in the stated domains. For the first identity, put \(a=\min(v(x),v(y))>0\). Expanding the \(j\)-th term of \(\log(1+x+y+xy)\) gives finitely many terms, each of value at least \(ja-e\log_p j\); this tends to infinity. Regrouping by total degree is therefore allowed and evaluates the formal identity. The exponential product identity similarly follows by regrouping its binomial expansion; for total degree \(D\), factorial denominators have \(p\)-adic value at most \(D/(p-1)\).

For the inverse identities, suppose the input has value \(a>e/(p-1)\). A term of total degree \(D=j_1+\cdots+j_k\), with all \(j_\ell\geq1\), in the expanded composition \(\exp(\log(1+x))\) has denominator \(k!j_1\cdots j_k\). Its \(p\)-adic value is at most
\[
\frac{k-1}{p-1}+\sum_{\ell=1}^k\frac{j_\ell-1}{p-1}
=\frac{D-1}{p-1}.
\]
For \(\log(\exp z)\), the corresponding denominator is \(k\,j_1!\cdots j_k!\), with the same bound. Hence every expanded term of either composition has value at least
\[
a+(D-1)\left(a-\frac e{p-1}\right)\longrightarrow\infty.
\]
There are only finitely many choices at a fixed total degree. The expanded sums are therefore summable and can be regrouped by degree, proving that their values equal the formal compositions in (2.5). These estimates also hold uniformly on every depth in (2.2).

The first identity makes log a homomorphism on all of \(U^1\). The remaining identities make (2.2) inverse homomorphisms. Uniform convergence proves continuity of both, so they are homeomorphisms. \(\square\)

The strict depth bound is indispensable. For \(\mathbf Q_2\), it gives \(r\geq2\), hence the exponential is defined on \(4\mathbf Z_2\). At \(z=2\), the terms with \(j=2^k\) have \(2\)-adic valuation \(s_2(2^k)=1\), so they do not tend to zero.

## 3. The compact principal-unit group

**Theorem 3.1 (characteristic-zero structure).** There is an integer \(a\geq0\) and a topological group isomorphism
\[
U^1\simeq\mu_{p^a}(K)\times\mathbf Z_p^d,
\tag{3.1}
\]
where \(\mu_{p^a}(K)\) is exactly the group of all \(p\)-power roots of unity in \(K\), of order \(p^a\). Consequently,
\[
K^\times\simeq
\mathbf Z\times\mathbf Z/(q-1)\mathbf Z
\times\mathbf Z/p^a\mathbf Z\times\mathbf Z_p^d.
\tag{3.2}
\]
The free-factor splitting need not be canonical.

*Proof.* Choose \(r>e/(p-1)\). The integer ring is free of rank \(d\) over \(\mathbf Z_p\), by the integral-basis theorem for \(K/\mathbf Q_p\). Multiplication by \(\pi^r\) and Proposition 2.1 identify \(U^r\) with \(\mathfrak m^r\simeq\mathbf Z_p^d\). These are also \(\mathbf Z_p\)-module identifications: the logarithm converts integer powers to integer multiples, and continuity extends the equality to \(p\)-adic scalars.

The quotient \(U^1/U^r\) is finite. Lifts of all its finitely many classes, together with a module basis of \(U^r\), generate \(U^1\) over \(\mathbf Z_p\): subtract a class representative multiplicatively and the remaining unit lies in \(U^r\). Thus \(U^1\) is a finitely generated module over the PID \(\mathbf Z_p\). Its free rank is \(d\), because the finite quotient disappears after tensoring with \(\mathbf Q_p\).

The module structure theorem gives a finite torsion part and a free part of rank \(d\). Every torsion element is a root of unity. Its order is a power of \(p\), since its image in every finite quotient of the pro-\(p\) group has \(p\)-power order, and the quotients separate points. Conversely, every \(p\)-power root of unity reduces to identity: \(\kappa^\times\) has order prime to \(p\). It therefore lies in \(U^1\).

A finite subgroup of a field's multiplicative group is cyclic. Hence the finite torsion group is precisely \(\mu_{p^a}(K)\) for some \(a\). An algebraic module splitting yields (3.1). Its map from the finite group times \(\mathbf Z_p^d\) is continuous by continuity of scalar powers. It is a bijection from a compact space to a Hausdorff space, so its inverse is continuous. Proposition 1.1 now gives (3.2). \(\square\)

In characteristic \(p\), \(U^1\) is torsion-free. Indeed a torsion element in a pro-\(p\) group has \(p\)-power order, while
\((1+x)^{p^b}=1+x^{p^b}\) cannot equal \(1\) unless \(x=0\).
The complete structure in characteristic \(p\) has a direct coefficient proof.

**Theorem 3.2 (characteristic-\(p\) principal units).** If \(K\) is a local field of characteristic \(p\), then
\[
U^1\simeq\prod_{j=1}^\infty\mathbf Z_p
\quad\text{as topological groups}.
\tag{3.3}
\]
*Proof.* The classification theorem identifies \(K\) with \(\mathbf F_q((T))\). Write \(q=p^f\), and choose an \(\mathbf F_p\)-basis \(b_1,\ldots,b_f\) of \(\mathbf F_q\). For each positive \(m\) prime to \(p\), put
\[
u_{m,j}=1+b_jT^m,\qquad 1\leq j\leq f.
\]
Proposition 1.1 defines \(u_{m,j}^{a}\) continuously for \(a\in\mathbf Z_p\). Consider
\[
\Theta: \prod_{\substack{m\geq1\\ p\nmid m}}\mathbf Z_p^f
\longrightarrow U^1,\qquad
(a_{m,j})\longmapsto\prod_{\substack{m\geq1\\ p\nmid m}}\prod_{j=1}^f
u_{m,j}^{a_{m,j}}.
\tag{3.4}
\]
The product converges: its factors for \(m>D\) all lie in \(U^{D+1}\), for every choice of exponents. Each finite initial product is continuous, so this uniform tail bound proves continuity of \(\Theta\). Commutativity and the same bound prove it is a homomorphism.

We describe its first nonzero coefficient. If \(a\ne0\), write \(a=p^kc\) with \(c\in\mathbf Z_p^\times\). In characteristic \(p\),
\[
u_{m,j}^{p^k}=1+b_j^{p^k}T^{mp^k}.
\]
For an integer exponent, the first coefficient of \((1+z)^c\) is \(c z\). Approximating the \(p\)-adic integer \(c\) by integers, and using continuity modulo \(U^{mp^k+1}\), proves that the first coefficient of \(u_{m,j}^a-1\) is
\[
\bar c\,b_j^{p^k}\quad\text{at degree }mp^k.
\tag{3.5}
\]
Now suppose an exponent family is nonzero. Among its first degrees \(mp^{v_p(a_{m,j})}\), choose the smallest \(N\). The representation \(N=mp^k\) with \(p\nmid m\) is unique. Only this \(m,k\) can contribute to the degree-\(N\) coefficient of the product. That coefficient is a nonzero \(\mathbf F_p\)-linear combination of the \(b_j^{p^k}\): at least one corresponding leading digit is nonzero. Frobenius is an automorphism of \(\mathbf F_q\), so these elements form a basis and the combination cannot vanish. Hence \(\Theta\) is injective.

For surjectivity, start with any \(w\in U^1\) and remove its coefficients successively. At degree \(N\), write \(N=mp^k\) as above. There are unique digits \(c_j\in\{0,\ldots,p-1\}\) whose linear combination \(\sum_j c_jb_j^{p^k}\) equals the degree-\(N\) coefficient of the remaining unit. Divide that remaining unit by \(\prod_j u_{m,j}^{c_jp^k}\). Formula (3.5) kills exactly that coefficient without changing any lower one. Continue through \(N=1,2,\ldots\). For each \(m,j\), the chosen digits give \(a_{m,j}=\sum_{k\geq0}c_{m,j,k}p^k\in\mathbf Z_p\). The residual unit tends to \(1\), and convergence of the products in (3.4) proves \(\Theta((a_{m,j}))=w\).

Thus \(\Theta\) is a continuous bijection from a compact product to the Hausdorff group \(U^1\), and therefore a homeomorphism. There are countably infinitely many indices \(m\) prime to \(p\), and \(f\) is positive and finite, so its source is a countable product of copies of \(\mathbf Z_p\), proving (3.3). This coordinate description depends on \(T\) and the residue basis. The classical statement is Fesenko–Vostokov, Chapter I, Proposition (6.2), and Chapter IV, (1.4). \(\square\)

## 4. Power indices and finite-index subgroups

**Theorem 4.1 (characteristic-zero power index).** For every positive integer \(n\),
\[
(K^\times:K^{\times n})
=\frac{n\,|\mu_n(K)|}{|n|_K}.
\tag{4.1}
\]
The power subgroup is open and closed.

*Proof.* Apply the \(n\)-th power map to (3.2). The valuation factor contributes index \(n\). On the finite torsion group
\[
C=\mu_{q-1}(K)\times\mu_{p^a}(K),
\]
the index \(|C/C^n|\) equals the kernel size \(|\mu_n(K)|\), by counting the fibers of the homomorphism \(c\mapsto c^n\). All roots of unity in \(K\) lie in \(C\), since \(\mathbf Z\) and \(\mathbf Z_p^d\) have no torsion.

On \(\mathbf Z_p^d\), write \(n=p^b m\), \(p\nmid m\). Multiplication by \(m\) is an automorphism and multiplication by \(p^b\) has index \(p^{bd}\). Since \(d=ef\),
\[
|n|_K=q^{-eb}=p^{-db}.
\]
Multiplying the three indices proves (4.1).

The subgroup \(n\mathbf Z\) is open in the discrete factor, every subgroup of a finite discrete factor is open, and \(n\mathbf Z_p^d\) is open. Thus their product, \(K^{\times n}\), is open. It has finite index, and its complement is a finite union of open cosets; it is therefore closed. \(\square\)

**Corollary 4.2.** In characteristic zero every subgroup of finite index in \(K^\times\) is open and closed. In characteristic \(p\), the subgroup \(K^{\times p}\) is closed and has infinite index; finite-index subgroups need not be open.

*Proof.* In characteristic zero, if a subgroup \(A\) has index \(n\), the finite abelian quotient \(K^\times/A\) has order \(n\). Lagrange's theorem gives \(K^{\times n}\subseteq A\). Theorem 4.1 supplies an open subgroup inside \(A\), making \(A\) a union of open cosets. Its finite-index complement is also open.

In characteristic \(p\), identify \(K\) with \(\mathbf F_q((T))\) by the local-field classification. The \(p\)-th power map sends
\[
\sum_j a_j T^j\longmapsto\sum_j a_j^p T^{pj},
\]
and \(\mathbf F_q\) is perfect. Its image consists exactly of Laurent series supported at exponents divisible by \(p\).

The classes \(1+T^r\), as \(r\) ranges over positive integers prime to \(p\), are pairwise distinct modulo \(K^{\times p}\). For distinct \(r,s\), the difference from \(1\) of their ratio has valuation \(\min(r,s)\), prime to \(p\). But if that ratio were \(y^p\), its difference from \(1\) would be \((y-1)^p\), with valuation divisible by \(p\). This contradiction proves infinite index.

For closedness use \(K^\times=\pi^{\mathbf Z}\times U\). The power subgroup corresponds to \(p\mathbf Z\times U^p\). The first factor is closed in a discrete group, and \(U^p\) is the continuous image of the compact group \(U\), hence compact and closed. Thus \(K^{\times p}\) is closed.

To exhibit a finite-index subgroup that is not open, use the stated structure (3.3). Reduction of every coordinate modulo \(p\) gives a continuous surjection
\[
U^1\longrightarrow V=\prod_{j=1}^\infty\mathbf F_p.
\]
The direct-sum subspace \(V_0=\bigoplus_j\mathbf F_p\) is dense and is proper, since the vector with every coordinate \(1\) is not finitely supported. Choose an algebraic linear functional \(\ell:V\to\mathbf F_p\) that vanishes on \(V_0\) and takes value \(1\) on that vector. Such a functional exists by extending a vector-space basis of \(V_0\) with that vector and then to a basis of \(V\).

Its kernel is proper and dense, so cannot be open: an open subgroup is also closed. The inverse image in \(U^1\) has index \(p\) and is dense, since the coordinate reduction is an open map and the kernel of \(\ell\) is dense. It too is not open. Extend this subgroup by the full valuation and Teichmüller factors in (1.1); the resulting subgroup of \(K^\times\) has index \(p\), and is not open because its intersection with the open group \(U^1\) is not open. This construction uses an algebraic basis choice; it does not claim the functional is continuous. \(\square\)

For contrast, when \(p\nmid n\) in characteristic \(p\), simple-root Hensel lifting makes the \(n\)-th power map an automorphism of \(U^1\). Thus \(K^{\times n}\) is open and has index \(n|\mu_n(K)|\). To justify the automorphism, lift the residue root \(1\) of \(X^n-u\) for \(u\in U^1\); uniqueness proves injectivity and gives the inverse on principal units.

## 5. The Iwasawa logarithm

**Proposition 5.1.** For a characteristic-zero local field \(K\), there is a unique continuous homomorphism
\[
\operatorname{Log}_K:K^\times\longrightarrow(K,+)
\]
that agrees with the logarithm series on \(U^1\) and satisfies \(\operatorname{Log}_K(p)=0\).

*Proof.* Choose \(\pi\) and write, using (1.1),
\[
p=\pi^e\omega_p u_p,\qquad
\omega_p\in\mu_{q-1}(K),\quad u_p\in U^1.
\]
Define
\[
c=-\frac1e\log u_p,\qquad
\operatorname{Log}_K(\pi^m\omega u)=mc+\log u.
\tag{5.1}
\]
This is a homomorphism by the unique product decomposition and Proposition 2.1. It is continuous on each open valuation fiber, hence on all of \(K^\times\). It agrees with the series on \(U^1\), vanishes on Teichmüller roots, and gives \(ec+\log u_p=0\) at \(p\).

Conversely, any such homomorphism vanishes on finite-order roots, since the additive characteristic-zero field has no torsion. Its value at \(p\) forces its value at \(\pi\) to be \(c\), and the decomposition then forces (5.1) everywhere. This proves uniqueness and also independence of the uniformizer used in the construction. \(\square\)

The normalization concerns the rational prime \(p\). A general uniformizer need not have logarithm zero; its value is the number \(c\) above.

## 6. Examples

For odd \(p\), **Hensel's lemma, squares and roots of unity in p-adic fields** proves that \(\mu(\mathbf Q_p)=\mu_{p-1}\). Thus
\[
\mathbf Q_p^\times\simeq
\mathbf Z\times\mathbf Z/(p-1)\mathbf Z\times\mathbf Z_p.
\]
At \(p=2\), that lesson gives exactly the two roots \(1,-1\), so
\[
\mathbf Q_2^\times\simeq
\mathbf Z\times\mathbf Z/2\mathbf Z\times\mathbf Z_2.
\]
Concretely, \(\mathbf Z_2^\times=\{1,-1\}\times(1+4\mathbf Z_2)\), and log identifies the last factor with \(4\mathbf Z_2\simeq\mathbf Z_2\).

For cubes in \(\mathbf Q_3\), there is no nonidentity cube root of unity, and \(|3|_3=1/3\). Hence the index is \(3/(1/3)=9\). For cubes in \(\mathbf Q_7\), there are three cube roots of unity and \(3\) is a unit, so the index is \(3\cdot3=9\). The equal answers have different origins: a free \(p\)-adic factor contributes the extra \(3\) in the first case, while finite torsion contributes it in the second.

## 7. Exercises

1. Compute the cube-power indices for \(\mathbf Q_p\), \(p=3,7,13\), and the fourth-power index for \(\mathbf Q_2\).

2. Prove that log identifies \(1+p^r\mathbf Z_p\) with \(p^r\mathbf Z_p\) for \(r\geq1\) at odd \(p\), and \(r\geq2\) at \(p=2\). Explain why the excluded \(2\)-adic depth is different.

3. Prove that every finite-index subgroup is open in characteristic zero, and that the characteristic-\(p\) power subgroup has infinite index. Exhibit a characteristic-\(p\) finite-index subgroup that is not open.

4. Prove the full index formula (4.1), keeping the absolute-value normalization explicit.

## 8. Complete solutions

**Solution 1.** For \(p=3\), the cube-root group has size \(1\) and \(|3|_3=1/3\), giving index \(9\). For \(p=7\) and \(13\), the residue unit group contains three cube roots, which lift uniquely, and \(3\) is a unit. Both indices are \(3\cdot3=9\). In \(\mathbf Q_2\), the fourth-root group has size \(2\), namely \(1,-1\); there is no fourth root of order four by the torsion calculation in the Hensel lesson. Since \(|4|_2=1/4\), formula (4.1) gives \(4\cdot2/(1/4)=32\).

**Solution 2.** Here \(e=1\). At odd \(p\), \(1/(p-1)<1\), so every integer \(r\geq1\) satisfies the strict exponential bound. At \(2\), it requires \(r>1\), hence \(r\geq2\). The term estimates in Proposition 2.1 show that log and exp preserve the value of their first nonzero term and are inverse homomorphisms on these groups. Their convergence is uniform at each indicated depth, so they are homeomorphisms. At depth one for \(\mathbf Q_2\), the group contains \(-1\), whose logarithm is zero because log is a homomorphism and \(2\log(-1)=\log1=0\). Thus log cannot be injective there. Also the exponential at \(2\) fails to converge, as its terms of degrees \(2^k\) all have valuation one.

**Solution 3.** If \(A\) has finite index \(n\) in characteristic zero, Lagrange's theorem in the finite abelian quotient gives \(K^{\times n}\subseteq A\). The structure theorem makes that power subgroup a product of \(n\mathbf Z\), a subgroup of finite torsion, and \(n\mathbf Z_p^d\); all are open. Hence \(A\) is open, and its complement, a union of finitely many open cosets, is open.

In characteristic \(p\), choose \(K=\mathbf F_q((T))\). Distinct principal units \(1+T^r\), for positive \(r\) prime to \(p\), give distinct power classes: their ratio differs from one at a valuation prime to \(p\), whereas every \(p\)-th power ratio differs from one at a valuation divisible by \(p\). Infinitely many such \(r\) prove infinite index. The subgroup is closed because in \(\pi^{\mathbf Z}\times U\) it is \(p\mathbf Z\times U^p\), with a closed discrete factor and compact unit factor.

For a finite-index counterexample, use \(U^1\simeq\prod_j\mathbf Z_p\). Coordinate reduction has target \(\prod_j\mathbf F_p\). Choose a nonzero algebraic functional that vanishes on all finitely supported vectors, by the basis extension explained in Corollary 4.2. Its kernel is dense and has index \(p\). The coordinate reduction is open, so its inverse-image kernel is dense and proper in \(U^1\); hence it is not open. Multiply it by the full valuation and finite-root factors to obtain an index-\(p\) subgroup of \(K^\times\) that is not open.

**Solution 4.** Write \(K^\times=\mathbf Z\times C\times\mathbf Z_p^d\) by Theorem 3.1, with \(C\) its finite torsion group. The valuation quotient modulo \(n\) has size \(n\). On \(C\), kernel and cokernel of the endomorphism \(c\mapsto c^n\) have equal size, namely \(|\mu_n(K)|\). Writing \(n=p^b m\), \(p\nmid m\), the quotient of the free factor has size \(p^{bd}\), since multiplication by \(m\) is invertible and each coordinate contributes \(p^b\). Finally, \(q=p^f\), \(v(n)=eb\), and \(d=ef\) give \(|n|_K=q^{-eb}=p^{-bd}\). Multiplying the three quotient sizes yields \(n|\mu_n(K)|/|n|_K\). All factors of the power subgroup are open, so the power subgroup is open and, having finite index, is also closed.

## Source comparison for this edition

Fesenko–Vostokov, Chapter I, (5.4)–(5.9) and (6.2)–(6.5), and Chapter IV, (1.4), give the valuation/unit decomposition, the unit filtration, the principal-unit structures and the openness of power subgroups. The proof of Lemma 2.4 in Chapter III of Milne's *Class Field Theory* gives the exponential and logarithm isomorphism near the identity, and Proposition 6.8 in Chapter VII gives the power indices. The digit and completeness background is in Fesenko–Vostokov, Chapter I, (5.2). The comparison keeps the different analytic domains: log converges throughout \(U^1\), while the mutually inverse log/exp maps are asserted at the strict depth \(r>e/(p-1)\). The characteristic-zero splitting into finite torsion and a rank-\([K:\mathbf Q_p]\) free \(\mathbf Z_p\)-module is a choice of topological isomorphism, not a canonical identification. The characteristic-\(p\) countable product of \(\mathbf Z_p\), its coordinate proof, the \(p\)-power contrast and the nonopen finite-index example are all retained.

For a positive integer \(n\) in characteristic zero, the valuation direction contributes \(n\), finite torsion contributes \(|\mu_n(K)|\), and the free unit factor contributes \(1/|n|_K\), with \(|x|_K=q^{-v(x)}\). This is precisely the index in (4.1), as in Milne's *Class Field Theory*, Chapter VII, Proposition 6.8, which treats characteristic zero. In characteristic \(p\) the \(p\)-power subgroups have infinite index, as in Fesenko–Vostokov, Chapter IV, (1.4); that case is proved separately here. Finally, the Iwasawa normalization in Proposition 5.1 is \(\operatorname{Log}_K(p)=0\). The decomposition \(p=\pi^e\omega_pu_p\) forces \(\operatorname{Log}_K(\pi)=-e^{-1}\log u_p\); it does not set the logarithm of every uniformizer to zero.

## 9. What this lesson does not prove

- The classification of nonarchimedean local fields as finite extensions of \(\mathbf Q_p\) in characteristic zero and \(\mathbf F_q((T))\) in characteristic \(p\) is Theorem 5.1 of **Local fields: classification and Haar measure**. Its Proposition 3.1 gives the finite residue field and compact integer ring, and Proposition 6.1 gives the modulus \(q^{-v(x)}\).
- The integral-basis theorem gives \(\mathcal O_K\simeq\mathbf Z_p^d\) and \(d=ef\): this is Theorem 3.1 of **Extensions of complete valued fields**, applied over \(\mathbf Q_p\). Hensel lifting and multiplicative residue representatives are Corollary 1.2 and Proposition 4.1 of **Hensel's lemma, squares and roots of unity in p-adic fields**; its Proposition 4.3 determines the roots of unity in \(\mathbf Q_p\).
- The characteristic-\(p\) product structure (3.3), its torsion-free consequence, power-index contrast and a nonopen finite-index subgroup are proved here. The field identification \(K\simeq\mathbf F_q((T))\) used in Theorem 3.2 is Theorem 5.1 of **Local fields: classification and Haar measure**.
- We use the structure theorem for finitely generated modules over the PID \(\mathbf Z_p\), cyclicity of finite subgroups of a field's multiplicative group, Lagrange's theorem, and vector-space basis extension. The formal rational power-series identities actually needed for log and exp are justified in Proposition 2.1.

For the finite-subgroup cyclicity used in Theorem 3.1 the exact open proof is [Stacks, Tag 09HX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-cyclic), using the polynomial root bound. Finitely generated PID modules and vector-space basis extension are the algebraic background from **Abstract Algebra II** and **Graduate Algebra**. Both characteristic-zero and characteristic-\(p\) local unit structures are proved in this lesson.

## References

I. B. Fesenko and S. V. Vostokov, [*Local Fields and Their Extensions*](https://ivanfesenko.org/wp-content/uploads/2021/10/vol.pdf), second edition, American Mathematical Society, 2002, Chapter I, §§5–6, especially (5.2), (5.4)–(5.9) and (6.2)–(6.5), and Chapter IV, (1.4).

J. S. Milne, [*Class Field Theory*](https://www.jmilne.org/math/CourseNotes/CFT.pdf), version 4.03 (6 August 2020), Chapter III, Lemma 2.4, and Chapter VII, Proposition 6.8.
