# Localization, local properties and support

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

To examine an equation near a point, we should allow division by functions that do not vanish there. Localization does exactly this. The same operation works for modules, so it lets us examine a relation, a kernel or a system of generators near each prime. The surprise is how much global information these examinations retain: localization is exact, and the examinations at all maximal ideals detect exactness.

We use [*Spectra of rings*](spectra-of-rings.md), together with elementary module theory, tensor products, determinants, the Chinese remainder theorem and Gauss's lemma for polynomials over a unique factorization domain. A finite module means a finitely generated module. A local ring has exactly one maximal ideal; it need not be Noetherian. Throughout, rings are commutative with identity, and a multiplicative set contains \(1\) and is closed under multiplication. We allow \(0\) in that set.

Basic references are the Stacks project, Timothy Ford's *Commutative Algebra*, and Ravi Vakil's *The Rising Sea*. Our route starts with the algebra of division, passes through the geometry of fibres, and then uses finite generation to control local data.

## 1. Division without cancellation

Fix a ring \(R\), a multiplicative set \(S\), and an \(R\)-module \(M\). A fraction is a pair \((m,s)\in M\times S\). Define

\[
(m,s)\sim(n,t)\quad\Longleftrightarrow\quad
u(tm-sn)=0\text{ for some }u\in S.
\]

The extra factor \(u\) is essential when multiplication by a denominator has a kernel.

**Construction 1.1.** The equivalence classes, denoted \(m/s\), form an \(S^{-1}R\)-module \(S^{-1}M\), with operations

\[
\frac m s+\frac n t=\frac{tm+sn}{st},
\qquad \frac a u\frac m s=\frac{am}{us}.
\]

For \(M=R\), this is a ring with product \((a/s)(b/t)=ab/(st)\) and identity \(1/1\).

**Verification.** Reflexivity and symmetry are immediate. For transitivity, if \(u(tm-sn)=0\) and \(v(wn-t\ell)=0\), multiply the first equality by \(vw\), the second by \(us\), and add. The result is \(uvt(wm-s\ell)=0\), with \(uvt\in S\). Thus the relation is transitive.

To check addition, suppose \(u(s'm-sm')=0\) and \(v(t'n-tn')=0\). The difference between the cross-multiplied proposed sums is

\[
tt'(s'm-sm')+ss'(t'n-tn'),
\]

which \(uv\) kills. The scalar action is checked by the same cross-multiplication: replacing a numerator fraction changes a product by a multiple of its killed cross-difference. The module axioms follow by bringing finitely many fractions to a common denominator; the ring axioms follow likewise. This proves that the construction is well defined. Its most useful elementary test is

\[
\frac m s=0\quad\Longleftrightarrow\quad um=0\text{ for some }u\in S.
\tag{1.1}
\]

In particular, \(S^{-1}R=0\) exactly when \(0\in S\): if \(1/1=0\), equation (1.1) gives an element \(u=0\) of \(S\).

**Proposition 1.2 (universal properties).** A ring map \(R\to A\) sending every element of \(S\) to a unit extends uniquely to \(S^{-1}R\to A\). If every \(s\in S\) acts invertibly on an \(R\)-module \(N\), every \(R\)-linear map \(M\to N\) extends uniquely to \(S^{-1}M\to N\).

**Proof.** The only possible ring map is \(a/s\mapsto\varphi(a)\varphi(s)^{-1}\). A cross-difference killed by \(u\in S\) maps to zero because \(\varphi(u)\) is a unit, so the map is well defined. The fraction rules prove it is a ring map. For modules the only possible extension is \(m/s\mapsto s_N^{-1}\alpha(m)\), where \(s_N\) denotes multiplication by \(s\) on \(N\). The same killed cross-difference proves well-definedness. Additivity and linearity follow from the fraction rules. \(\square\)

The modules on which \(S\) acts invertibly are exactly the \(S^{-1}R\)-modules, with their underlying \(R\)-module structures. To recover the extended action, let \(a/s\) act by \(a_Ns_N^{-1}\). This respects the fraction relation, and the two constructions are inverse, on maps as well as on modules.

**Proposition 1.3 (tensor description).** There is a natural isomorphism

\[
S^{-1}R\otimes_R M\cong S^{-1}M.
\]

**Proof.** Send \((a/s)\otimes m\) to \(am/s\). This is balanced and additive. Conversely send \(m/s\) to \((1/s)\otimes m\). If \(u(tm-sn)=0\), the difference of these proposed tensor values equals

\[
\frac1{st}\otimes(tm-sn)
=\frac1{ust}\otimes u(tm-sn)=0.
\]

Thus the inverse is well defined. The two maps are inverse on the displayed generators. \(\square\)

We write \(M_f\) when \(S=\{1,f,f^2,\ldots\}\), and \(M_{\mathfrak p}\) when \(S=R\setminus\mathfrak p\). The ring \(R_f\) agrees with \(R[t]/(ft-1)\) from the preceding lesson, because they have the same universal property. For a domain, inverting all nonzero elements gives its fraction field. In an arbitrary nonzero ring, inverting all nonzerodivisors gives the total ring of fractions; the map into it is injective by (1.1).

## 2. Relations survive localization

Localization sends a map \(\alpha:M\to N\) to \(m/s\mapsto\alpha(m)/s\). These maps preserve compositions and identities.

**Theorem 2.1 (exactness).** If \(L\xrightarrow\alpha M\xrightarrow\beta N\) is exact, so is its localization at any multiplicative set.

**Proof.** The localized composite is zero. If \(m/s\) maps to zero, there is \(u\in S\) with \(\beta(um)=0\). Exactness gives \(\ell\in L\) with \(\alpha(\ell)=um\). Then \(\ell/(us)\) maps to \(m/s\). This proves equality of image and kernel. It also includes preservation of injections by taking \(L=0\), and preservation of surjections by taking \(N=0\). \(\square\)

Consequently submodules localize as submodules, and

\[
S^{-1}(M/L)\cong S^{-1}M/S^{-1}L.
\]

Localization commutes with arbitrary sums of submodules: every element of a sum already uses finitely many summands. It commutes with finite intersections: apply exactness to the kernel of \(L\oplus K\to M\), \((\ell,k)\mapsto\ell-k\). This gives \(S^{-1}(L\cap K)=S^{-1}L\cap S^{-1}K\). Infinite intersections require separate hypotheses and are not asserted here. Localization also commutes with direct sums, by the fraction construction and finite support of each tuple.

**Theorem 2.2 (localizing Hom).** If \(M\) is finitely presented, the natural map

\[
S^{-1}\operatorname{Hom}_R(M,N)
\longrightarrow
\operatorname{Hom}_{S^{-1}R}(S^{-1}M,S^{-1}N)
\]

is an isomorphism for every \(N\).

**Proof.** Choose a finite presentation \(R^b\xrightarrow A R^a\to M\to0\). A map from \(M\) to \(N\) is a tuple in \(N^a\) satisfying the finitely many relations, so

\[
\operatorname{Hom}_R(M,N)=\ker(N^a\xrightarrow{A^*}N^b).
\]

Exactness and commutation with finite direct sums identify the localization of this kernel with the kernel of \((S^{-1}N)^a\to(S^{-1}N)^b\). The localized presentation identifies that kernel with the Hom module on the right. These identifications are precisely the natural map. \(\square\)

Finiteness of the presentation has a real role: it lets one denominator clear finitely many relations. If \(M\) is only finite, the natural map is still injective. Indeed, if a fraction \(\alpha/s\) becomes zero, finitely many generators of \(M\) allow a product of finitely many elements of \(S\) to kill every value of \(\alpha\). Surjectivity can fail.

For a concrete failure with a cyclic source, set

\[
R=k[t,x_1,x_2,\ldots]/(t^i x_i:i\geq1),
\quad I=(x_1,x_2,\ldots),\quad M=R/I,
\quad S=\{t^n:n\geq0\}.
\]

Every \(x_i\) vanishes after localization, so \(M_t=R_t\). The identity of \(R_t\) cannot come from \(\operatorname{Hom}_R(M,R)_t=(\operatorname{Ann}_R I)_t\). If it were represented by \(a/t^n\), equality with one would give \(t^j(a-t^n)=0\), hence \(t^{j+n}\in\operatorname{Ann}I\). But no power \(t^d\) kills \(I\): choose \(i>d\), and map \(R\) to \(k[t,x]/(t^i x)\) by retaining \(x_i=x\) and killing the other \(x_j\). The monomial \(t^d x\) is nonzero there. This proves the failure. Even finite generation is absent in the example \(\operatorname{Hom}_{\mathbb Z}(\mathbb Q,\mathbb Z)=0\), whereas after rational localization the corresponding Hom is \(\mathbb Q\). The first equality holds because an integer divisible by every positive integer is zero.

## 3. Points left after division, and fibres

**Theorem 3.1 (prime and ideal correspondence).** Every ideal of \(S^{-1}R\) is extended from \(R\). Contraction induces a homeomorphism

\[
\operatorname{Spec}(S^{-1}R)\cong
\{\mathfrak p\in\operatorname{Spec}R:\mathfrak p\cap S=\varnothing\},
\]

with the subspace topology on the right. Its inverse is \(\mathfrak p\mapsto S^{-1}\mathfrak p\).

**Proof.** If \(J\) is an ideal upstairs, \(a/s\in J\) exactly when \(a/1\in J\), because \(s/1\) is a unit. Thus \(J\) is the extension of its contraction. A prime upstairs contracts to a prime disjoint from \(S\). Conversely, for a prime \(\mathfrak p\) disjoint from \(S\), the ring

\[
(S^{-1}R)/(S^{-1}\mathfrak p)\cong
\overline S^{-1}(R/\mathfrak p)
\]

is a nonzero domain. This proves primality of the extension; the injection of \(R/\mathfrak p\) into this domain proves the required contraction equality. Finally \(D(a/s)\) upstairs corresponds to \(D(a)\) intersected with the displayed subspace. These bases prove the topological assertion. \(\square\)

The subset in this theorem is not generally open. For \(R_{\mathfrak p}\), it is the primes contained in \(\mathfrak p\), not the primes containing it. This reverses the apparent direction of the closed locus \(V(\mathfrak p)\).

The ring \(R_{\mathfrak p}\) is local, with maximal ideal \(\mathfrak pR_{\mathfrak p}\). A fraction whose numerator is outside \(\mathfrak p\) has the reversed fraction as an inverse. A fraction with numerator in \(\mathfrak p\) cannot be a unit, by the prime correspondence. Its residue field is

\[
\kappa(\mathfrak p)=R_{\mathfrak p}/\mathfrak pR_{\mathfrak p}
\cong\operatorname{Frac}(R/\mathfrak p).
\]

**Theorem 3.2 (fibres).** For \(\varphi:R\to A\) and \(\mathfrak p\in\operatorname{Spec}R\), the fibre over \(\mathfrak p\) is naturally homeomorphic to

\[
\operatorname{Spec}(A\otimes_R\kappa(\mathfrak p)).
\]

It is nonempty exactly when this tensor product is a nonzero ring.

**Proof.** First invert \(S=R\setminus\mathfrak p\) in \(A\), and then quotient by the extended ideal \(\mathfrak p\). The resulting ring is

\[
S^{-1}A/\mathfrak p S^{-1}A\cong A\otimes_R\kappa(\mathfrak p),
\]

by Proposition 1.3 and the quotient property of tensor products. Its primes correspond exactly to primes \(Q\) of \(A\) containing \(\varphi(\mathfrak p)\) and avoiding \(\varphi(S)\). These conditions say \(\varphi^{-1}(Q)=\mathfrak p\). The homeomorphisms for localization and quotient identify the induced subspace topologies at each step. Finally a ring has a prime exactly when it is nonzero, as proved in the preceding lesson. \(\square\)

For \(\mathbb Z_{(p)}\), the surviving primes are \((0),(p)\). For \(\mathbb Z[1/p]\), every prime except \((p)\) survives. In \(k[x,y]_{(x,y)}\), the surviving primes are all those contained in \((x,y)\), whereas in \(k[x,y]_x\) they are all those avoiding \(x\). For example \((x)\) survives the first operation but not the second; \((x-1,y)\) survives the second but not the first.

## 4. Finite generators near a point

A nonzero ring is local exactly when its nonunits form an ideal. If it has a unique maximal ideal \(\mathfrak m\), every nonunit lies in some maximal ideal and therefore in \(\mathfrak m\), and no element of \(\mathfrak m\) is a unit. Conversely an ideal consisting of all nonunits contains every proper ideal; it is the unique maximal ideal. Equivalently, a nonzero ring is local if for every \(a\), at least one of \(a,1-a\) is a unit. In a local ring this follows because their sum is one. If two different maximal ideals existed, the Chinese remainder theorem would provide \(a\) congruent to zero in one and one in the other, making both \(a\) and \(1-a\) nonunits.

The Jacobson radical \(\operatorname{Jac}(R)\) is the intersection of maximal ideals. An element \(a\) lies in it exactly when \(1-ra\) is a unit for every \(r\in R\). For the forward direction, a maximal ideal containing \(1-ra\) would also contain \(ra\), a contradiction. For the reverse direction, if \(a\) survives in \(R/\mathfrak m\), choose \(r\) lifting its inverse in that field; then \(1-ra\) is in \(\mathfrak m\) and is not a unit.

**Lemma 4.1 (determinant trick).** If \(M\) is finite, \(I\subset R\) is an ideal, and an endomorphism \(\psi\) satisfies \(\psi(M)\subset IM\), then

\[
\psi^n+c_1\psi^{n-1}+\cdots+c_n=0,
\qquad c_j\in I^j,
\]

for some \(n\). If \(IM=M\), some \(1+i\), \(i\in I\), annihilates \(M\).

**Proof.** Choose generators \(m_1,\ldots,m_n\) and coefficients \(a_{ij}\in I\) with \(\psi(m_i)=\sum_j a_{ij}m_j\). In the column of generators, \((\psi\,1_n-A)m=0\). Its entries are commuting endomorphisms, so multiplication by its adjugate gives \(\det(\psi\,1_n-A)m=0\). The determinant is a monic polynomial in \(\psi\); a coefficient of degree \(n-j\) uses \(j\) entries of \(A\), hence lies in \(I^j\). It kills every generator and therefore \(M\). Taking \(\psi=1_M\) when \(IM=M\) gives an annihilator congruent to one modulo \(I\). For \(M=0\) the last assertion holds with annihilator one. \(\square\)

**Theorem 4.2 (Nakayama).** If \(M\) is finite, \(I\subset\operatorname{Jac}(R)\), and \(IM=M\), then \(M=0\). More generally, elements of a finite module over \((R,\mathfrak m)\) generate it exactly when their residues span \(M/\mathfrak mM\).

**Proof.** The annihilator \(1+i\) in Lemma 4.1 is a unit, so \(M=0\). For the generator assertion, let \(N\) be the submodule spanned by the proposed elements. Their residues span precisely when \(M=N+\mathfrak mM\). The finite quotient \(M/N\) is then equal to \(\mathfrak m(M/N)\), so vanishes. The reverse implication is immediate. \(\square\)

Thus the least number of generators of a finite local module is

\[
\dim_{R/\mathfrak m}M/\mathfrak mM.
\]

Lifting a vector-space basis proves attainability. Every generating family must span that vector space, proving minimality. An irredundant finite generating family has linearly independent residues: a residue dependence with a coefficient not in \(\mathfrak m\) lets one express a generator in the others and \(\mathfrak mM\); Nakayama then removes that generator. Finite generation cannot be omitted. The nonzero \(\mathbb Z_{(p)}\)-module \(\mathbb Q\) satisfies \(p\mathbb Q=\mathbb Q\).

## 5. Recovering global information

**Theorem 5.1 (local detection).** An element, module, kernel, cokernel or homology module is zero exactly when its localizations at every maximal ideal are zero. In particular, injectivity, surjectivity and exactness can be checked at all maximal ideals, or at all prime ideals.

**Proof.** If \(x\in M\) is nonzero, its annihilator is a proper ideal and lies in a maximal ideal \(\mathfrak m\). Equation (1.1) then says \(x/1\neq0\) in \(M_{\mathfrak m}\): a denominator killing \(x\) would belong both to its annihilator and to \(R\setminus\mathfrak m\). This proves the element assertion and hence the module assertion. Exactness of localization identifies localized kernels, cokernels and homology with the corresponding constructions on localized maps. Apply the module assertion to each of them. Maximal ideals are prime, so the version using all primes follows as well. \(\square\)

There is also a useful version for an open cover. If \(D(f_1),\ldots,D(f_r)\) cover the spectrum, vanishing can be checked on these finitely many localizations. Every maximal ideal belongs to some \(D(f_i)\), and localizing further at that maximal ideal proves the claim. Exactness and isomorphisms can therefore also be checked on this cover.

Finite generation glues on such a cover. If each \(M_{f_i}\) is finite, choose numerators of finitely many generators on each member and let \(N\subset M\) be generated by all those numerators. Then \((M/N)_{f_i}=0\) for all \(i\), so \(M=N\).

Finite presentation glues too. We spell out the small algebraic point involved. If a module \(L\) is finitely presented, the kernel of any finite-free surjection \(F\to L\) is finite. Choose another finite-free surjection \(G\to L\) with finite kernel \(K\). The pullback of \(F\to L\leftarrow G\) is both \(K\oplus F\) and \(K'\oplus G\), where \(K'=\ker(F\to L)\); these splittings exist because \(F,G\) are free. Hence \(K'\) is finite as a direct summand of the finite module \(K\oplus F\). Now, if each \(M_{f_i}\) is finitely presented, the preceding paragraph makes \(M\) finite. Choose \(R^a\to M\) onto, with kernel \(K\). Each \(K_{f_i}\) is finite by the kernel observation. Gluing finite generation makes \(K\) finite, proving finite presentation of \(M\).

## 6. Where a module is visible

The support is

\[
\operatorname{Supp}_R M=\{\mathfrak p:M_{\mathfrak p}\neq0\}.
\]

**Proposition 6.1 (support calculus).** In a short exact sequence \(0\to L\to M\to N\to0\),

\[
\operatorname{Supp}M=\operatorname{Supp}L\cup\operatorname{Supp}N.
\]

If \(M\) is finite, then

\[
\operatorname{Supp}M=V(\operatorname{Ann}_R M).
\]

For any ideal \(I\), \(\operatorname{Supp}(R/I)=V(I)\).

**Proof.** The first assertion follows from localized exactness: the middle module vanishes exactly when the two outer modules vanish. If an annihilator of \(M\) is outside \(\mathfrak p\), it becomes a unit and kills \(M_{\mathfrak p}\), so that module vanishes. Conversely, if \(M_{\mathfrak p}=0\), choose finite generators \(m_i\) and denominators \(s_i\notin\mathfrak p\) killing them. Their product annihilates all of \(M\) and is outside \(\mathfrak p\). This proves the second assertion. Apply it to the cyclic module \(R/I\), whose annihilator is \(I\), to obtain the last assertion. \(\square\)

For finite modules \(M,N\),

\[
\operatorname{Supp}(M\otimes_R N)
=\operatorname{Supp}M\cap\operatorname{Supp}N.
\tag{6.1}
\]

Indeed, localization and tensor products commute by the universal properties. If either localized factor vanishes, so does the tensor product. If both are nonzero, Nakayama makes their quotients by the local maximal ideal nonzero. Their tensor product over \(\kappa(\mathfrak p)\) is nonzero: choose a nonzero vector in each and linear functionals taking them to one. This vector-space tensor product is a quotient of the localized tensor product, which therefore cannot vanish. The same argument gives \(\operatorname{Supp}(M/IM)=\operatorname{Supp}M\cap V(I)\) for finite \(M\).

Over \(\mathbb Z\), \(\operatorname{Supp}(\mathbb Z/n)\) is the set of \((p)\) with \(p\mid n\), for \(n\neq0\). On the other hand every localization of \(\mathbb Q\) is \(\mathbb Q\), so its support is the whole spectrum. Equality with its annihilator locus happens even though it is not finite. To see why finiteness matters, take \(E=\bigoplus_p\mathbb Z/p\). Its support is all closed points and excludes \((0)\). That set is not closed. Its annihilator is zero, because no nonzero integer is divisible by all positive primes. Thus its support differs from \(V(\operatorname{Ann}E)\).

Another instructive module over \(C=\prod_{n\geq1}\mathbb F_2\) is \(C/J\), where \(J\) is the finite-support ideal. At a coordinate prime it localizes to zero; at a non-coordinate prime, each finite-support idempotent vanishes locally, so \(J\) localizes to zero and \((C/J)_{\mathfrak p}=C_{\mathfrak p}\). Every localization is therefore free, of rank zero or one. Nevertheless \(C/J\) is not projective. If it were, the surjection \(C\to C/J\) would split and its kernel would be generated by an idempotent \(e\): the corresponding projection of \(C\) is multiplication by its value \(e\) at one. Since \(e\in J\) has finite support, \(eC\) cannot contain all coordinate idempotents, although \(J\) does. This contradiction shows why a pointwise freeness test needs a finiteness condition on relations.

## 7. The arithmetic line, now proved

For \(\mathbb Z\to\mathbb Z[x]\), Theorem 3.2 identifies the fibres over \((0)\) and \((p)\) with \(\operatorname{Spec}\mathbb Q[x]\) and \(\operatorname{Spec}\mathbb F_p[x]\). These are polynomial rings over fields, hence principal ideal domains. In the fibre over \((p)\), the primes are therefore \((p)\) and \((p,g)\), where \(\bar g\) is monic irreducible in \(\mathbb F_p[x]\). The latter ideals are maximal because their quotients are fields.

In the generic fibre, the zero prime contracts to zero. A nonzero prime is generated by an irreducible polynomial in \(\mathbb Q[x]\). Clearing denominators and dividing the coefficients by their greatest common divisor gives a primitive polynomial \(f\in\mathbb Z[x]\), irreducible over \(\mathbb Q\), unique up to sign. We need the following form of Gauss's lemma. A polynomial is primitive when no prime divides all its coefficients. The product of two primitive integer polynomials is primitive: reducing modulo any prime gives two nonzero polynomials over a field and therefore a nonzero product. Write a nonzero rational polynomial as \((a/b)h\), with \(h\) primitive integral and \(a,b\) coprime integers, \(b>0\). If \(g=f(a/b)h\) is integral, every coefficient of \(afh\) is divisible by \(b\). Since \(fh\) is primitive and \(a,b\) are coprime, this forces \(b=1\). Thus divisibility of an integer polynomial by \(f\) over \(\mathbb Q[x]\) is already divisibility in \(\mathbb Z[x]\), and the contraction is exactly \((f)\). Also \(f\) is irreducible in \(\mathbb Z[x]\): a nontrivial positive-degree factorization would persist over \(\mathbb Q\), while a nonunit constant factor would contradict primitivity.

Every prime contracts to a prime of \(\mathbb Z\), so we have exhausted all possibilities:

\[
(0),\quad(p),\quad(f),\quad(p,g).
\]

The symbols \(f\) and \(g\) have the conditions just stated. We have proved the classification of primes. To conclude that only \((p,g)\) are maximal also requires excluding maximal ideals in the generic fibre; *The Nullstellensatz and Jacobson rings* will give that conclusion. For a particular example, \((x)\) is already seen to be nonmaximal because its quotient is \(\mathbb Z\). It specializes to \((p,x)\) for every prime \(p\), exactly as the figure in *Spectra of rings* depicts.

## 8. Exercises

**Exercise 8.1 (first steps).** Let \(T=\{r\in R:ar\in S\text{ for some }a\in R\}\), the saturation of \(S\). Show that \(T\) is the inverse image of the units of \(S^{-1}R\), and that \(T^{-1}R\cong S^{-1}R\). Include the case \(0\in S\).

**Exercise 8.2 (first steps).** Compute the support of \(\mathbb Z/8\oplus\mathbb Q\). Compute also the support and annihilator of \(\bigoplus_p\mathbb Z/p\), and explain the different behavior of these two modules.

**Exercise 8.3 (structural).** Prove that a surjective endomorphism of a finite module over any commutative ring is invertible. No Noetherian hypothesis is allowed.

**Exercise 8.4 (structural).** Prove the tensor-product support identity for finite modules. Show explicitly why it fails for \(\mathbb Q\) and \(\mathbb Z/5\) over \(\mathbb Z\).

**Exercise 8.5 (arithmetic).** Determine the points of \(\operatorname{Spec}\mathbb Z[i]\) above each point of \(\operatorname{Spec}\mathbb Z\), including the generic point. Give the residue fields in the closed fibres.

**Exercise 8.6 (synthesis).** Prove that a finite projective module over a local ring is free, and identify its rank with its minimal number of generators.

## 9. Solutions

**Solution 8.1.** If \(ar=s\in S\), the element \(r/1\) has inverse \(a/s\). Conversely, if \((r/1)(a/s)=1\), then \(u(ra-s)=0\) for some \(u\in S\). Hence \((ua)r=us\in S\), so \(r\in T\). It follows that \(T\) is multiplicative and contains \(S\), since the preimage of the group of units is multiplicative. The maps between the two localizations given by their universal properties are inverse: their composites fix \(R\), so uniqueness makes them identities. If \(0\in S\), then \(T=R\) and both rings are zero. This includes the convention that the sole element of the zero ring is its identity and is a unit.

**Solution 8.2.** The torsion summand has support \(\{(2)\}\), and \(\mathbb Q\) has support all of \(\operatorname{Spec}\mathbb Z\). The direct-sum support is their union, hence the whole spectrum, a closed set. For \(E=\bigoplus_p\mathbb Z/p\), localization at \((q)\) leaves exactly its \(q\)-summand: every other summand is killed by a denominator \(p\notin(q)\). At \((0)\), each element uses finitely many summands and is killed by a nonzero integer, so its localization is zero. Thus the support is all closed points. Its annihilator is \(\bigcap_p p\mathbb Z=0\), whose vanishing locus also contains \((0)\). There is no single nonzero integer killing all generators. This is the step where the finite-module proof of Proposition 6.1 fails.

**Solution 8.3.** Give \(M\) an \(R[t]\)-module structure with \(t\) acting by the endomorphism \(\psi\). It is finite over \(R[t]\), since its original generators still generate it. Surjectivity means \(tM=M\). Lemma 4.1 supplies an annihilator \(1+tq(t)\) for some \(q(t)\in R[t]\). Translating the action gives \(1_M+\psi q(\psi)=0\). Hence \(-q(\psi)\) is a two-sided inverse to \(\psi\); polynomial expressions in \(\psi\) commute with \(\psi\). The radical form of Nakayama is not needed, because \((t)\) need not be in the Jacobson radical of \(R[t]\).

**Solution 8.4.** At a prime, a zero localized factor gives a zero tensor product. If both finite localized factors are nonzero, Nakayama makes their residue vector spaces nonzero. Tensoring those vector spaces gives a nonzero quotient of \((M\otimes N)_{\mathfrak p}\), proving the reverse inclusion. For the proposed infinite example, multiplication by \(5\) is invertible on \(\mathbb Q\) and zero on \(\mathbb Z/5\). Thus for a pure tensor \(q\otimes\bar a\), writing \(q=5(q/5)\) gives \(q\otimes\bar a=(q/5)\otimes5\bar a=0\). But the intersection of the two supports contains \((5)\). The identity therefore fails without the stated finiteness hypothesis.

**Solution 8.5.** Present \(\mathbb Z[i]=\mathbb Z[T]/(T^2+1)\). The generic fibre is \(\mathbb Q[T]/(T^2+1)=\mathbb Q(i)\), a field, so there is exactly one point over \((0)\), namely \((0)\). The fibre over \((p)\) is \(\mathbb F_p[T]/(T^2+1)\). If \(p=2\), the polynomial is \((T+1)^2\), giving one point \((2,i+1)=(1+i)\) with residue field \(\mathbb F_2\); the equality follows from \(2=-i(1+i)^2\) and \(i+1=1+i\), together with the quotient of order two.

For an odd prime, \(\mathbb F_p^\times\) is cyclic of order \(p-1\). Here is a proof of the needed fact. In any finite subgroup \(G\) of a field's multiplicative group, let \(e\) be the least common multiple of the element orders. For each prime power exactly dividing \(e\), choose an element whose order contains that power, and raise it to obtain an element of exactly that prime-power order. The product of these elements has order \(e\), because they commute and have pairwise coprime orders. Every element of \(G\) is a root of \(T^e-1\), so \(|G|\leq e\) by the polynomial root bound. The element of order \(e\) also gives \(e\leq|G|\). Thus \(G\) is cyclic.

A square root of \(-1\) exists exactly when \(4\mid p-1\): in a cyclic group, the unique order-two element is a square exactly when the group order is divisible by four. If \(p\equiv1\pmod4\), choose a root \(a\); there are two distinct primes \((p,i-a)\) and \((p,i+a)\), both with residue field \(\mathbb F_p\). If \(p\equiv3\pmod4\), the polynomial is irreducible, giving one prime \((p)\) with residue field \(\mathbb F_{p^2}\). These possibilities exhaust the points by Theorem 3.2.

**Solution 8.6.** Put \(r=\dim_\kappa P/\mathfrak mP\), lift a basis, and use Nakayama to obtain a surjection \(R^r\to P\). Projectivity splits it, so \(R^r=K\oplus P\) with \(K\) finite: a direct summand of a finite module is generated by the projections of its generators. Modulo \(\mathfrak m\), the induced map \(\kappa^r\to P/\mathfrak mP\) is an isomorphism, so the splitting gives \(K/\mathfrak mK=0\). Nakayama gives \(K=0\). Therefore \(P\cong R^r\). The number \(r\) is simultaneously its free rank and its minimal number of generators, by Section 4. The zero module is included with \(r=0\).

## What this lesson does not prove

All localization, local detection, Nakayama and support assertions taught above have been proved, as have the two elementary polynomial and finite-field facts needed for the arithmetic examples. We do not yet prove that every maximal ideal of \(\mathbb Z[x]\) contracts to a nonzero prime of \(\mathbb Z\); that result belongs to *The Nullstellensatz and Jacobson rings*.

## References

- The Stacks project authors, *The Stacks project*, Commutative Algebra: [Tag 00CP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#proposition-universal-property-localization), [Tag 00CS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#proposition-localization-exact), [Tag 0583](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-hom-from-finitely-presented), [Tag 00E3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-spec-localization), [Tag 00DV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-NAK), [Tag 00L2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#lemma-support-closed).
- Timothy J. Ford, *Commutative Algebra*, version of 23 September 2026, Chapter 1, Section 5 on Nakayama's Lemma; Chapter 3, Section 1 on localization and its local-to-global lemmas, and Section 3 on the prime spectrum; Chapter 7, Section 2 on the support of a module. [Author's version](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf).
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Section 8.2. [Author's public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).
