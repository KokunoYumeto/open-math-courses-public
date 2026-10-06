# Finite-field towers and prescribed MASA multiplicities

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text: public domain (CC0).*

The [affine construction](group-masas-and-singular-affine-examples.md) turns a subgroup of index \(n\) in the multiplicative group of a countably infinite field into a singular MASA with \(n+1\) double cosets. The [left/right commutant calculation](double-cosets-and-intrinsic-masa-multiplicity.md) then gives homogeneous type \(\mathrm I_n\) on the complement of the MASA trace space. We construct such a field and subgroup for every positive integer \(n\).

Two compatibility points matter. Nested finite fields require divisibility of degrees. Also, the largest power of a composite integer dividing a group order need not be a direct-summand order. The construction below uses all the relevant prime-primary parts and proves that their complements are compatible along the entire tower. The polynomial, field and finite-group arguments are supplied below, starting with integer arithmetic and the definitions of the algebraic objects.

## 0. Algebra used in the construction

We use integers, finite sequences and the definitions of a field, a group and a vector space. The facts about polynomials, finite extensions and group orders needed below follow from the following arguments.

<a id="integer-divisibility"></a>
**Integer divisibility.** For a positive integer \(b\) and an integer \(a\), choose the largest integer \(q\) with \(qb\le a\). This exists because the eligible integers are bounded above, and gives \(a=qb+r\), \(0\le r<b\). For positive integers \(a,b\), the least positive integer \(g\) of the form \(ua+vb\), \(u,v\in\mathbb Z\), divides both \(a\) and \(b\): division of either by \(g\) would otherwise produce a smaller positive integer of the same form. Every common divisor divides \(g\), so \(g=\gcd(a,b)\), with a Bezout expression. In particular, if a prime \(\ell\) divides \(ab\) but not \(a\), multiplying a Bezout expression for \(\gcd(\ell,a)=1\) by \(b\) shows \(\ell\mid b\).

Every integer \(N>1\) has a prime divisor: its least divisor greater than \(1\) cannot have a proper divisor greater than \(1\). Repeated division produces a prime factorization, since each positive quotient is smaller. The preceding prime-divisor property proves uniqueness by cancellation of one prime at a time. Thus the exponent \(v_\ell(N)\) is defined and satisfies \(v_\ell(AB)=v_\ell(A)+v_\ell(B)\); divisibility is the comparison of all these exponents. These facts also give the least common multiple of a finite list by taking the largest exponent of each prime. If \(\ell\) is prime, the nonzero residues modulo \(\ell\) have inverses by Bezout, so \(\mathbb Z/\ell\mathbb Z\) is a field.

The rational field \(\mathbb Q\) can be constructed from pairs \((a,b)\) of integers with \(b\ne0\), identifying \((a,b)\) with \((c,d)\) when \(ad=bc\). Cancellation of nonzero integers proves transitivity; reflexivity and symmetry are immediate. Set \((a,b)+(c,d)=(ad+bc,bd)\) and \((a,b)(c,d)=(ac,bd)\). Multiplying the equalities defining two changes of representatives proves that both formulas give the same equivalence classes. Associativity, commutativity and distributivity follow by expanding the integer products; the classes of \((0,1)\) and \((1,1)\) are the two identities. Negation is \((-a,b)\), and a nonzero class has \(a\ne0\) and inverse \((b,a)\). The map \(a\mapsto(a,1)\) embeds the integers, proving characteristic zero.

There are infinitely many odd primes. Given a finite list of odd primes \(q_1,\ldots,q_v\), the odd integer \(2q_1\cdots q_v+1>1\) has a prime divisor; that divisor is neither \(2\) nor any \(q_i\), by its remainders. This includes the empty list, with product \(1\). The integers are countable by listing \(0,1,-1,2,-2,\ldots\); pairs of entries are countable by listing them in order of the sum of their indices. Their fraction classes therefore make \(\mathbb Q\) countable as well.

<a id="finite-group-orders"></a>
**Finite group orders.** If \(x\) belongs to a finite group, two nonnegative powers coincide. Cancellation gives a positive power equal to \(1\); let \(s\) be its least positive exponent. Integer division proves \(x^t=1\) exactly when \(s\mid t\). The powers with exponents \(0,\ldots,s-1\) are distinct and form the subgroup \(\langle x\rangle\). More generally the left cosets of any subgroup \(U\) partition a finite group: two cosets that intersect are equal, and multiplication gives a bijection from \(U\) to each coset. Therefore \(|U|\) divides the group order. Applied to \(\langle x\rangle\), this proves that every element order divides the group order. It also proves \(|V/U|=|V|/|U|\) when \(V\) is finite and abelian.

A field with \(p^a\) elements, where \(p\) is prime, has characteristic \(p\). Its additive group is finite, so the additive order \(c\) of \(1\) exists and divides \(p^a\). It is greater than \(1\), since \(1\ne0\). If \(c=uv\) with \(1<u,v<c\), then both \(u\cdot1\) and \(v\cdot1\) are nonzero by minimality of \(c\), but their product is \(c\cdot1=0\), contradicting the field axioms. Hence \(c\) is prime. Unique prime factorization and \(c\mid p^a\) give \(c=p\). Integer division shows that the integer multiples of \(1\) have kernel exactly \(p\mathbb Z\); they therefore embed \(\mathbb F_p\) in the field.

If \(x\) has order \(s\), then \(x^t\) has order \(s/\gcd(s,t)\). Indeed \((x^t)^j=1\) is equivalent to \(s\mid tj\), and division by the gcd reduces this to \(s/\gcd(s,t)\mid j\), using Bezout for the remaining coprime factors. If commuting elements \(x,y\) have coprime orders \(s,t\), their cyclic subgroups have trivial intersection, because the order of an element in the intersection divides both \(s\) and \(t\). If \((xy)^j=1\), then \(x^j=y^{-j}\) lies in this intersection, so \(s\mid j\) and \(t\mid j\), whence \(st\mid j\). Conversely \((xy)^{st}=1\); thus the product has order \(st\). Iterating proves the corresponding fact for any finite list of commuting elements with pairwise coprime orders.

For a cyclic group \(\langle x\rangle\) of order \(m\), every subgroup has the form \(\langle x^a\rangle\) with \(a\mid m\). To see this, choose the least positive exponent \(a\) whose power belongs to the subgroup; \(m\) is eligible even for the trivial subgroup. Dividing any eligible exponent by \(a\) shows that its remainder is zero by minimality. Applying this to \(m\) gives \(a\mid m\). Its subgroup order is \(m/a\). Consequently the subgroup of any order \(d\mid m\) is unique, namely \(\langle x^{m/d}\rangle\). If the subgroups of orders \(d\) and \(m/d\) intersect trivially, multiplication from their product is injective and its \(m\) elements exhaust the group. Their intersection is trivial precisely when \(\gcd(d,m/d)=1\): a common element has order dividing that gcd; if a prime divides the gcd, the unique subgroup of that prime order lies in both factors. This proves the direct-factor criterion (1), including its necessity.

<a id="polynomial-division"></a>
**Polynomial division and roots.** Let \(E\) be a field. For \(f,g\in E[X]\), \(g\ne0\), subtract from \(f\) the monomial multiple of \(g\) that cancels its highest term, and repeat while the remainder has degree at least \(\deg g\). The degree drops at each step, giving \(f=qg+r\), with \(r=0\) or \(\deg r<\deg g\). The leading coefficient of a product of nonzero polynomials is the product of their nonzero leading coefficients. Hence degrees add, and subtraction of two proposed divisions proves uniqueness. The same algorithm works in \(\mathbb Z[X]\) whenever \(g\) is monic, since no coefficient division is then needed.

Division by \(X-z\) has remainder \(f(z)\). Therefore a root \(z\) can be factored off, and induction on degree proves that a nonzero polynomial of degree \(d\) has at most \(d\) distinct roots in any extension field. The formal derivative \((\sum c_iX^i)'=\sum_{i\ge1}ic_iX^{i-1}\) obeys the product rule by direct multiplication of monomials and addition. Writing \(f=(X-z)h\) gives \(f'(z)=h(z)\). Thus \(f(z)=f'(z)=0\) exactly when \((X-z)^2\) divides \(f\). In particular, a polynomial that splits and whose derivative is nonzero at each root has as many distinct roots as its degree.

<a id="finite-splitting-fields"></a>
**Finite splitting fields.** Repeated polynomial division gives a gcd and a Bezout expression in \(E[X]\): at each Euclidean step the remainder has smaller degree, and substitution backwards expresses the last nonzero remainder as a combination of the initial polynomials. Normalize that remainder to be monic. It divides the initial polynomials, and every common divisor divides it, by the same substitutions. Every nonconstant polynomial has an irreducible monic divisor: take a monic nonconstant divisor of least degree; a factorization into two nonconstant polynomials would supply a smaller such divisor.

If \(h\) is irreducible of degree \(s\), the quotient ring \(E[X]/(h)\) is a field. Every nonzero class has a unique representative \(u\) with \(\deg u<s\). Its gcd with \(h\) is \(1\), since a nonconstant common divisor would make the irreducible \(h\) divide \(u\). A Bezout expression \(vu+wh=1\) therefore supplies its inverse. Constant polynomials embed \(E\) in the quotient. The classes of \(1,X,\ldots,X^{s-1}\) are a basis: division proves spanning, and a relation of degree less than \(s\) cannot be a nonzero multiple of \(h\). The class of \(X\) is a root of \(h\).

Given a polynomial \(f\) of positive degree, adjoin a root of an irreducible divisor in this way, divide off the resulting linear factor, and repeat with the remaining polynomial over the new field. At most \(\deg f\) steps make it split. The resulting extension is finite dimensional over \(E\). Indeed, if \(b_1,\ldots,b_u\) is a basis for one extension and \(c_1,\ldots,c_v\) a basis for the next over it, the products \(b_ic_j\) span over \(E\). They are independent: a relation, first grouped by \(c_j\), has zero coefficients by the second basis, and then by the first. Induction treats the whole finite chain. Take inside this final field the subfield generated by \(E\) and all roots of \(f\). It is a splitting field and remains finite dimensional: any independent list in a subspace of a finitely spanned space has length bounded by the size of a spanning list. For completeness, that bound follows by replacing a spanning vector with the first independent vector having a nonzero coefficient, then successively replacing another vector for each new independent vector; once all spanning vectors have been replaced, an additional vector is dependent. The same finite procedure produces a basis of any such subspace. No uniqueness theorem for splitting fields is needed here.

If \(E\) has \(q\) elements and an extension has a basis of length \(s\), unique coordinates give exactly \(q^s\) elements. Conversely, an extension that is a finite set has a finite basis by successively adding any element outside the current span; the process cannot continue beyond the size of that set. These observations justify every field-size and degree count below.

<a id="frobenius"></a>
**Frobenius.** Expanding a product of \(p\) copies of \(x+y\) gives the binomial formula: the coefficient of \(x^iy^{p-i}\) counts the choices of its \(i\) positions. For \(0<i<p\), this integer coefficient is divisible by the prime \(p\), because
\[
i!(p-i)!\binom pi=p!,
\]
and the left-hand factorials are not divisible by \(p\), whereas \(p!\) is. The prime-divisor property above supplies the cancellation. In a field containing \(\mathbb F_p\), it follows that \((x+y)^p=x^p+y^p\). Multiplication also gives \((xy)^p=x^py^p\), and \(1^p=1\), so the \(p\)-th power map is a field homomorphism. Iteration proves the same facts for the \(p^k\)-th power map, including preservation of negatives and nonzero inverses.


## 1. Finite fields and their multiplicative groups

**Lemma 1.1.** For every prime \(p\) and positive integer \(k\), a field with \(p^k\) elements exists. If a field with \(p^a\) elements has been constructed and \(a\mid b\), it can be included in a field with \(p^b\) elements. Such an inclusion is impossible unless \(a\mid b\).

**Proof.** Take a splitting field of \(X^{p^k}-X\) over \(\mathbb F_p\). It can be constructed by successively adjoining roots: an irreducible factor \(f\) gives the field quotient \(F[X]/(f)\), and repeating finitely many times splits a polynomial of finite degree. Each extension is finite dimensional and therefore finite when its starting field is finite.

The derivative is \(-1\), so the polynomial has \(p^k\) distinct roots in its splitting field. Those roots form a field. Frobenius gives
\((x+y)^{p^k}=x^{p^k}+y^{p^k}\) and \((xy)^{p^k}=x^{p^k}y^{p^k}\); negatives and nonzero inverses are also roots. This root field contains \(\mathbb F_p\) and all the roots, hence is the entire splitting field. It has exactly \(p^k\) elements.

If \(a\mid b\), take the splitting field of \(X^{p^b}-X\) over the already chosen field of size \(p^a\). Every element of that earlier field satisfies \(x^{p^a}=x\), by the finite multiplicative group order theorem for nonzero elements, and by iteration satisfies \(x^{p^b}=x\). Thus the root field contains the earlier field and has size \(p^b\), as above.

Conversely a subfield of size \(p^a\) makes a field of size \(p^b\) a finite-dimensional vector space over it. If the dimension is \(d\), counting basis coordinates gives \(p^b=(p^a)^d\), hence \(b=ad\). \(\square\)

**Lemma 1.2.** Every finite subgroup of the multiplicative group of a field is cyclic.

**Proof.** Let \(F\) be such a subgroup. Since it is abelian, there is an element whose order is the least common multiple \(m\) of all element orders. To construct it, for each prime \(\ell\) dividing \(m\), choose an element whose order has the maximal \(\ell\)-power appearing in \(m\), raise it to eliminate its prime-to-\(\ell\) part, and multiply the resulting elements. They commute and have relatively prime orders, so the product has order \(m\).

Every element of \(F\) is a root of \(X^m-1\). A polynomial of degree \(m\) over a field has at most \(m\) roots, giving \(|F|\le m\). The constructed element has \(m\) distinct powers in \(F\), giving \(m\le|F|\). Equality makes it a generator. \(\square\)

Thus a field with \(p^k\) elements has a cyclic multiplicative group of order \(p^k-1\). In a cyclic group, there is a unique subgroup of every order dividing the group order. A subgroup of order \(d\) splits as a direct factor exactly when
\[
\gcd(d,m/d)=1,
\tag{1}
\]
where \(m\) is the group order: the unique subgroups of orders \(d\) and \(m/d\) then have trivial intersection and generate the group. If that gcd is greater than one, those subgroups have a nontrivial intersection, and no different complement of the required order exists.

## 2. A prime with the required congruence

**Lemma 2.1.** For every positive integer \(n\), there is a prime \(p\) such that \(n\mid p-1\). An elementary argument suffices for this existence statement.

**Proof.** For \(n=1\), take \(p=2\). Suppose \(n>1\). Construct a finite splitting field \(E\) of \(X^n-1\) over \(\mathbb Q\), using the polynomial argument in Section 0. In characteristic zero its derivative \(nX^{n-1}\) is nonzero at every root, so its roots are \(n\) distinct elements. They form a multiplicative subgroup: products and inverses remain roots. By Lemma 1.2 this subgroup is cyclic of order \(n\).

For each \(t\mid n\), define \(\Phi_t\in E[X]\) to be the product of \(X-z\) over the roots whose exact multiplicative order is \(t\). The unique order-\(t\) subgroup of the root group consists of all the roots of \(X^t-1\): it already supplies \(t\) roots, the maximum possible. Partitioning it by exact orders therefore gives
\[
X^t-1=\prod_{d\mid t}\Phi_d(X),\qquad t\mid n.
\tag{2}
\]
Each \(\Phi_t\) is monic and has positive degree, since the cyclic root group has an element of every order \(t\mid n\). These polynomials have integer coefficients. Indeed \(\Phi_1=X-1\); assume the proper-divisor factors for \(t\) already belong to \(\mathbb Z[X]\). Their product is monic. Divide \(X^t-1\) by it using monic division in \(\mathbb Z[X]\). Identity (2) and uniqueness of division over \(E\) show that the remainder is zero and the quotient is \(\Phi_t\). Induction on \(t\) proves the assertion. Evaluating (2) at zero then proves \(\Phi_t(0)=1\) for every \(t>1\): \(\Phi_1(0)=-1\), and all proper-divisor factors other than \(\Phi_1\) have constant term \(1\) by induction.

Write \(\Phi_n(X)=X^s+\sum_{i=0}^{s-1}c_iX^i\), and let \(B=\sum_{i=0}^{s-1}|c_i|\). Choose a positive multiple \(a\) of \(n\) with \(a>B+1\) and \(a\ge2\). Then
\[
\Phi_n(a)\ge a^s-Ba^{s-1}=a^{s-1}(a-B)>1.
\]
This integer has a prime divisor \(p\). If \(p\mid a\), reducing its polynomial value modulo \(p\) would give \(0=\Phi_n(a)=\Phi_n(0)=1\), a contradiction. Thus \(p\nmid a\); since \(n\mid a\), also \(p\nmid n\).

In \(\mathbb F_p\), the residue of \(a\) is a nonzero root of \(\Phi_n\), hence of \(X^n-1\). Let its order be \(d\); the order argument in Section 0 gives \(d\mid n\). If \(d<n\), identity (2) for \(t=d\), reduced modulo \(p\), makes this residue a root of some \(\Phi_c\), \(c\mid d\). Here a product can vanish only if one factor vanishes, because \(\mathbb F_p\) is a field. In (2) for \(n\), it would consequently be a root of two factors, \(\Phi_n\) and \(\Phi_c\). Factoring off \(X-a\) from each would make it a multiple root of \(X^n-1\). But the derivative \(nX^{n-1}\) at this nonzero residue is nonzero, since \(p\nmid n\). This contradiction gives \(d=n\). Finally its order divides \(|\mathbb F_p^\times|=p-1\), by the coset argument in Section 0. Therefore \(n\mid p-1\). \(\square\)

This proves the one-prime existence needed here. It invokes no theorem about the density or distribution of primes in arithmetic progressions.

## 3. Why divisible degrees and full primary factors are needed

Pukánszky's finite-field construction, Lemma 5(b), pp. 295–296, motivates the tower. Nesting the fields and splitting their multiplicative groups impose two different conditions.

Increasing degrees relatively prime to \(n\) need not give nested finite fields. For example, with \(n=2\) and \(p=3\), the degrees \(3\) and \(5\) are both relatively prime to \(2\), but no field of order \(3^3\) embeds in one of order \(3^5\), by Lemma 1.1. We will choose degrees satisfying both relative primality and successive divisibility.

The largest power \(n^s\) dividing \(p-1\) need not be a direct-summand order. For \(n=6\), \(p=13\), the largest such power is \(6\), but the multiplicative group of \(\mathbb F_{13}\) is cyclic of order \(12\). Its order-\(6\) subgroup has no complement, by (1). Explicitly, the unique order-\(2\) subgroup lies inside the order-\(6\) subgroup. The highest-power assertion itself remains true at degrees relatively prime to \(n\); its direct-summand inference does not.

For \(n>1\), the correct quantity is the entire part of \(p-1\) supported on primes dividing \(n\):
\[
d=\prod_{\ell\mid n}\ell^{v_\ell(p-1)}.
\tag{3}
\]
Here the product is over the distinct prime divisors of \(n\). We have \(n\mid d\), since \(n\mid p-1\). For \(n=1\) use \(p=2\), \(d=1\), an empty product; a “largest power of \(1\)” is unnecessary and undefined as a largest exponent.

## 4. Compatible primary subgroups and complements

Choose a prime \(r\) not dividing \(n\); for instance any prime divisor of \(n+1\) works. Put
\[
k_j=r^{j-1},\qquad j\ge1.
\tag{4}
\]
These degrees increase strictly, divide their successors and are relatively prime to \(n\). By Lemma 1.1, construct fields
\[
F_1\subset F_2\subset\cdots,\qquad
|F_j|=p^{k_j},\qquad K=\bigcup_{j\ge1}F_j.
\tag{5}
\]
The union is a field, since any two elements and their field operations occur in a common stage. It is countable and infinite, since the stages are finite with unbounded cardinalities.

For any \(k\) relatively prime to \(n\), write
\[
p^k-1=(p-1)S_k,\qquad
S_k=1+p+\cdots+p^{k-1}\equiv k\pmod n.
\tag{6}
\]
For every prime \(\ell\mid n\), this congruence implies \(\ell\nmid S_k\), and hence
\[
v_\ell(p^k-1)=v_\ell(p-1).
\tag{7}
\]
Thus \(d\) in (3) is the full relevant primary part at every stage, and
\[
m_j=\frac{p^{k_j}-1}{d},\qquad \gcd(d,m_j)=1.
\tag{8}
\]
Equation (7) also proves the highest-\(n\)-power observation when \(n>1\): every prime valuation determining divisibility by \(n^s\) remains unchanged.

By cyclicity, let \(L_j\subset F_j^\times\) be the unique subgroup of order \(d\), and \(C_j\) the unique subgroup of order \(m_j\). Equation (1) gives
\[
F_j^\times=L_j\times C_j.
\tag{9}
\]

**Lemma 4.1.** The inclusions in (5) identify all \(L_j\) with one fixed cyclic subgroup \(L\), and carry \(C_j\) into \(C_{j+1}\). Consequently
\[
K^\times=L\times C,\qquad C=\bigcup_j C_j.
\tag{10}
\]

**Proof.** A field inclusion preserves the exact order of every nonzero element. Its image of \(L_j\) is an order-\(d\) subgroup of \(F_{j+1}^\times\), hence equals \(L_{j+1}\) by uniqueness. An element of \(C_j\) has order relatively prime to \(d\). In the decomposition \(L_{j+1}\times C_{j+1}\), its \(L_{j+1}\) component must therefore be trivial, so it belongs to \(C_{j+1}\).

The union \(C\) is a subgroup. Every element of \(K^\times\) belongs to some stage and thus decomposes into an element of \(L\) and one of \(C\). Their intersection is trivial: any element in it occurs at a stage where the two factors in (9) meet trivially. This proves (10). \(\square\)

It is important to identify the complements as well as the finite primary subgroup. Equal embedded primary subgroups do not by themselves justify a direct-product decomposition of an arbitrary union.

## 5. Producing every positive finite multiplicity

Since \(L\) is cyclic of order \(d\) and \(n\mid d\), let \(L_0\subset L\) be its subgroup of order \(d/n\). Define
\[
H=L_0\times C\subset K^\times.
\tag{11}
\]
The quotient in (10) is
\[
K^\times/H\cong L/L_0\cong\mathbb Z/n\mathbb Z.
\tag{12}
\]
Thus the index is exactly \(n\). The subgroup \(H\) is infinite: the orders \(m_j\) of \(C_j\) tend to infinity, whereas \(d\) is fixed. It is countable and abelian.

**Theorem 5.1.** For every positive integer \(n\), there is a countable ICC group \(G\) and a singular MASA \(A\subset L(G)\), with \(L(G)\) a separable \(\mathrm{II}_1\) factor, for which
\[
(1-e_A)(A\vee JAJ)'(1-e_A)
\cong (A_H\bar\otimes A_H)\bar\otimes M_n(\mathbb C).
\tag{13}
\]
The MASAs corresponding to different \(n\) cannot be carried onto one another by an isomorphism of their ambient factors.

**Proof.** Take \(K,H\) from (5) and (11), and form \(G=K\rtimes H\). The affine results prove ICC, malnormality, the MASA property and singularity, using only infinitude of \(H\). They also identify the double cosets with \(H\) and the \(n\) cosets of \(H\) in \(K^\times\). The [double-coset theorem](double-cosets-and-intrinsic-masa-multiplicity.md#theorem-3-1) gives (13), and its [canonical trace-space argument](double-cosets-and-intrinsic-masa-multiplicity.md#theorem-4-1) makes \(n\) invariant under any isomorphism carrying the MASAs onto one another. The trace-preservation step is proved directly in [T04](regular-group-operator-foundations.md#t04): an abstract group-factor isomorphism preserves positive suprema, and the order-normal trace is fixed by the bounded conjugation-average proof. For \(n=1\), the same construction has \(H=K^\times\); its complement block is abelian of type \(\mathrm I_1\). \(\square\)

A countably infinite multiplicity is also easy to realize. Take \(K=\mathbb Q\) and \(H=\{2^j:j\in\mathbb Z\}\). Distinct odd primes lie in distinct cosets of \(H\): a ratio of two odd primes cannot be a power of \(2\) unless the primes coincide. There are infinitely many odd primes, by Euclid's argument. The index is therefore countably infinite. The same affine and double-coset proofs give a singular MASA whose complement block has type \(\mathrm I_\infty\).

## 6. Exercises with complete solutions

**Exercise 1.** Prove the field closure of the roots of \(X^{p^k}-X\), including inverses.

*Solution.* Frobenius iterated \(k\) times gives \((x+y)^{p^k}=x^{p^k}+y^{p^k}\), so sums and negatives of roots are roots. Products are roots by the analogous multiplicative equality. Both \(0\) and \(1\) are roots. If \(x\ne0\) is a root, then \((x^{-1})^{p^k}=(x^{p^k})^{-1}=x^{-1}\), so its inverse is a root. The root set is therefore a subfield.

**Exercise 2.** Why can fields of degrees \(3\) and \(5\) over \(\mathbb F_3\) not be nested, even though both degrees are relatively prime to \(2\)?

*Solution.* If the field of order \(3^5\) contained the field of order \(3^3\), it would be a vector space of some integer dimension \(d\) over the latter. Counting elements gives \(3^5=3^{3d}\), hence \(5=3d\), impossible. Relative primality to an external index gives no degree-divisibility condition.

**Exercise 3.** In \(\mathbb F_{13}^\times\), show concretely that the subgroup of order \(6\) is not a direct summand.

*Solution.* The element \(2\) has order \(12\): \(2^6=-1\pmod{13}\), \(2^4=3\), and no proper divisor \(1,2,3,4,6\) gives the identity. The order-\(6\) subgroup is \(\langle2^2\rangle\), and its unique possible order-\(2\) complement is \(\langle2^6\rangle\). But \(2^6=(2^2)^3\) belongs to the order-\(6\) subgroup. The intersection is nontrivial, so no direct complement exists.

**Exercise 4.** For \(n=6\), \(p=13\), compute the corrected \(d\) and the quotient subgroup \(L_0\).

*Solution.* The prime divisors of \(6\) are \(2,3\). Since \(12=2^2\cdot3\), (3) gives \(d=12\), rather than the largest \(6\)-power \(6\). The subgroup \(L_0\) has order \(d/n=2\). Thus \(L/L_0\) is cyclic of order \(6\); the construction needs a quotient of the primary factor, not an order-\(6\) direct factor of it.

**Exercise 5.** Evaluate (6) modulo a prime \(\ell\mid n\), and deduce (7) without a lifting-the-exponent theorem.

*Solution.* Since \(p\equiv1\pmod\ell\), every term of \(S_k\) is \(1\), so \(S_k\equiv k\pmod\ell\). Relative primality of \(k\) and \(n\) gives \(\ell\nmid k\), hence \(v_\ell(S_k)=0\). Multiplicativity of valuations in \(p^k-1=(p-1)S_k\) gives \(v_\ell(p^k-1)=v_\ell(p-1)\). This handles \(\ell=2\) as well.

**Exercise 6.** For \(n=6\), choose degrees as in (4) and identify the first three field orders when \(p=13\).

*Solution.* Choose \(r=7\), a prime divisor of \(n+1=7\). The degrees are \(1,7,49\), all relatively prime to \(6\), and each divides the next. The field orders are \(13\), \(13^7\), \(13^{49}\). The relevant \(2\)- and \(3\)-primary parts of their multiplicative orders are all \(12\), by (7), even though the full field sizes increase rapidly.

**Exercise 7.** Why does equality of the embedded \(L_j\) not alone prove (10), and how does the proof control \(C_j\)?

*Solution.* A compatible finite subgroup could lack a complement at a stage or in the union. Here each stage is cyclic, and (8) proves a complement exists. Its elements have orders relatively prime to \(d\). After embedding in the next stage, their orders remain unchanged, so their components in its order-\(d\) factor are trivial. Therefore \(C_j\subset C_{j+1}\), and the union is an actual complementary subgroup. This verifies surjectivity and trivial intersection in (10).

**Exercise 8.** Supply the square-free step in the proof of Lemma 2.1.

*Solution.* The selected prime \(p\) does not divide \(n\). A root \(z\) of \(X^n-1\) is nonzero, and the derivative at it is \(nz^{n-1}\ne0\) in characteristic \(p\). Thus all roots are simple. In a factorization into monic polynomials, a root shared by two factors would be a multiple root of the product. Hence a root of \(\Phi_n\) cannot simultaneously be a root of \(\Phi_c\) for a proper divisor \(c\) of \(n\). This forces the multiplicative order to be exactly \(n\).

**Exercise 9.** Trace the proof that the construction has precisely \(n\) in (13), rather than merely a multiplicity bounded by \(n\).

*Solution.* The quotient \(L/L_0\) has exactly \(d/(d/n)=n\) elements, so (12) gives exact multiplicative index. The affine double-coset calculation is a bijection between nonzero translation cosets and \(K^\times/H\), giving exactly \(n\) nontrivial double cosets. Malnormality makes each of them one full regular product representation, and their direct sum gives exactly \(n\) identical copies. The commutant is therefore homogeneous type \(\mathrm I_n\), as asserted.

**Exercise 10.** Prove that \(\mathbb Q^\times/\langle2\rangle\) has countably infinitely many cosets and explain the resulting type.

*Solution.* It has at most countably many cosets because \(\mathbb Q^\times\) is countable. For distinct odd primes \(q,q'\), an equality \(q/q'=2^j\) with \(j\ge0\) contradicts unique prime factorization unless \(j=0\) and \(q=q'\); negative \(j\) is handled by inversion. The odd-prime cosets are therefore all distinct, and there are infinitely many. The infinite dilation subgroup is malnormal in its affine group, so the complement consists of countably infinitely many regular product copies. Its commutant is \(D\bar\otimes B(\ell^2(\mathbb N))\), homogeneous type \(\mathrm I_\infty\).

## References

The algebraic proof route can be read freely in the following primary sources; the full arguments and the corrections remain supplied in this lesson.

- Keith Conrad, [*Finite Fields*](https://kconrad.math.uconn.edu/math5211s13/handouts/finitefield.pdf), author-hosted handout in the Spring 2013 course directory. Theorem 2.2, p. 3, proves finite-field existence; Theorem 2.6, p. 4, proves the divisor-degree subfield criterion; Lemma 1.6, p. 2, proves multiplicative cyclicity. Lemma 1.2 here also supplies the finite-abelian order argument used in that proof and treats every finite multiplicative subgroup.
- Abhinav Kumar, [MIT 18.781, Spring 2012, Lecture 12: *Cyclotomic Polynomials, Primes Congruent to 1 mod n*](https://ocw.mit.edu/courses/18-781-theory-of-numbers-spring-2012/resources/mit18_781s12_lec12/), Proposition 45(1)–(2), p. 2; Lemma 46, p. 3; and Theorem 47 with proof, pp. 3–4. These give the cyclotomic factorization, integrality and order argument. Lemma 2.1 uses this classical cyclotomic order method for the one-prime existence needed here; it constructs the roots algebraically and makes the large-integer estimate explicit. The index-one case is separate.
- Lajos Pukánszky, [*On Maximal Abelian Subrings of Factors of Type II₁*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9B7B38999C7306E6047079CB68C937B6/S0008414X00009949a.pdf/on-maximal-abelian-subrings-of-factors-of-type-ii.pdf), *Canadian Journal of Mathematics* 12 (1960), 289–296. Lemma 5 and its proof, pp. 295–296, give the original finite-field and index-to-double-coset route. Sections 3–4 here supply the divisible-degree choice and the full primary factors and compatible complements required by that route. Lemmas 1, 3 and 4, pp. 290 and 293–295, give the trace-space invariant and affine MASA mechanism used in the preceding lessons.
- Allan M. Sinclair and Roger R. Smith, [*The Pukánszky invariant for masas in group von Neumann factors*](https://people.tamu.edu/~rrsmith/papers/pukanszky.pdf), author-hosted manuscript of the 2005 article, Example 5.1 and proof, manuscript pp. 15–17. This gives an alternative rational affine construction for every finite or countably infinite multiplicity; it does not supply the finite-field tower. Example 5.2 concerns multiplicative families of invariants beyond the single multiplicity needed here.
