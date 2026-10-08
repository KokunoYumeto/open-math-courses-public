# Noether's axioms for Dedekind domains

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

The two factorizations \(6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5})\) show that elements can fail to factor uniquely. Ideals recover the missing structure. This lesson explains why a short list of ring properties forces every nonzero ideal to be invertible and then to factor uniquely. The proof takes place in the fraction field throughout; it does not infer factorization from discrete valuations.

We assume basic module theory and integral dependence. In Noetherian and Artinian rings, Proposition 1.2 gives finite generation of submodules over a Noetherian ring, Theorem 4.2 gives the dimension-zero Artinian criterion, and Theorem 3.3 gives finite length under both chain conditions [Stacks, Tags 00FP, 00KH and 00KJ]. We also use lying over and incomparability for integral extensions [Stacks, Tags 00GQ and 00GT], with dimension comparison [Tag 00OJ]; these are proved in Integral extensions: lying over, going up and going down, Theorems 3.2, 3.3 and 5.1. The DVR and Dedekind localization characterizations are proved in Discrete valuation rings and Dedekind domains, under those two named results. They are used here only in examples. That lesson excludes fields; our convention includes them. Basic references are [Noether], [Milne] and [Stacks]. Continue with The converse and composition series.

## 1. The five axioms and the question they answer

All rings in this lesson are commutative. For a nonzero ring \(R\), Noether's axioms in modern form are:

1. Every ascending chain of ideals stabilizes.
2. For every nonzero ideal \(J\), descending chains of ideals containing \(J\) stabilize.
3. There is an identity element.
4. A product of two nonzero elements is nonzero.
5. Every element of \(K=\operatorname{Frac}(R)\) integral over \(R\) belongs to \(R\).

The first axiom says that every ideal is finitely generated. To see this equivalence, if an ideal were not finite, repeatedly adjoining a new element would give a strictly ascending chain. Conversely, the union of an ascending chain is an ideal; finitely many generators lie at one stage and force stabilization.

In the presence of the first axiom, the second says that every nonzero prime is maximal. Indeed, it makes \(R/J\) Artinian, so its primes are maximal. Conversely, if nonzero primes are maximal, then \(R/J\) is Noetherian of dimension zero and hence Artinian. Thus the five axioms say that \(R\) is a Noetherian integrally closed domain of dimension at most one. A field is allowed. We call such a ring a **Dedekind domain**. Another definition requires unique prime factorization of nonzero ideals; this lesson and the next prove the equivalence. [Stacks, Tags 034W and 034X] use these two descriptions.

For a nonzero ideal \(I\), put

\[
 I^{-1}=(R:I)=\{x\in K:xI\subseteq R\}.
\]

It is an \(R\)-submodule of \(K\) containing \(R\). If \(0\ne a\in I\), it lies in \(a^{-1}R\), so it has a common denominator. The main task is to prove \(II^{-1}=R\).

## 2. Two global devices

**Lemma 2.1.** In a Noetherian domain, every nonzero proper ideal contains a finite product of nonzero prime ideals.

**Proof.** Suppose not. Among the nonzero counterexamples choose a maximal one \(I\), using the ascending chain condition. It is not prime, because a prime contains itself. Choose \(a,b\notin I\) with \(ab\in I\). Each of \(I+(a)\) and \(I+(b)\) is larger than \(I\), so each contains a product of nonzero primes. If one is \(R\), use the empty product \(R\). Their product is contained in

\[
 (I+(a))(I+(b))=I^2+aI+bI+(ab)\subseteq I.
\]

Combining the two products gives the required product in \(I\), a contradiction. The empty product cannot result for proper \(I\). \(\square\)

**Lemma 2.2, the determinant trick.** Let \(M\subseteq K\) be a nonzero finitely generated \(R\)-module. If \(xM\subseteq M\), then \(x\) is integral over \(R\).

**Proof.** Choose generators \(m_1,\ldots,m_n\) and coefficients \(a_{ij}\in R\) such that \(xm_i=\sum_j a_{ij}m_j\). Multiply the equation \((x\operatorname{id}-A)m=0\) by the adjugate matrix. It gives \(\det(x\operatorname{id}-A)m_i=0\) for every \(i\). Some \(m_i\ne0\); since we are in a field, \(\det(x\operatorname{id}-A)=0\). The polynomial \(\det(T\operatorname{id}-A)\) is monic in \(R[T]\). \(\square\)

Finite generation gives an equation; integral closedness turns that equation into membership in the ring. This is the mechanism behind invertibility.

## 3. From prime inverses to factorization

**Lemma 3.1.** Suppose \(R\) is a Noetherian domain of dimension at most one, and \(\mathfrak p\) is a nonzero prime. Then \(\mathfrak p^{-1}\supsetneq R\).

**Proof.** Choose \(0\ne a\in\mathfrak p\). By Lemma 2.1 choose a product \(\mathfrak p_1\cdots\mathfrak p_r\subseteq(a)\) with \(r\) as small as possible. Since this product lies in \(\mathfrak p\), some \(\mathfrak p_i\subseteq\mathfrak p\). Both are nonzero maximal ideals, so they are equal. Relabel with \(\mathfrak p_1=\mathfrak p\). Minimality says that \(\mathfrak p_2\cdots\mathfrak p_r\nsubseteq(a)\); for \(r=1\), this means \(R\nsubseteq(a)\). Choose \(b\) in that product outside \((a)\). Then \(b/a\notin R\), but \((b/a)\mathfrak p\subseteq R\). \(\square\)

**Proposition 3.2.** In a Dedekind domain every nonzero prime is invertible.

**Proof.** We have \(\mathfrak p\subseteq\mathfrak p\mathfrak p^{-1}\subseteq R\). Since \(\mathfrak p\) is maximal, the middle ideal is either \(\mathfrak p\) or \(R\). In the first case every \(x\in\mathfrak p^{-1}\) stabilizes the finite nonzero module \(\mathfrak p\). Lemma 2.2 and axiom 5 then give \(x\in R\), contradicting Lemma 3.1. Hence \(\mathfrak p\mathfrak p^{-1}=R\). \(\square\)

**Theorem 3.3, Noether's global factorization theorem.** Every nonzero integral ideal in a Dedekind domain is a unique finite product of nonzero prime ideals. The unit ideal is the empty product.

**Proof of existence.** If there are counterexamples, choose a maximal one \(I\). Choose a maximal ideal \(\mathfrak p\supseteq I\); it is nonzero. Then \(J=I\mathfrak p^{-1}\) is an integral ideal, because \(I\subseteq\mathfrak p\), and \(I\subseteq J\). This inclusion is strict: equality would make every element of \(\mathfrak p^{-1}\) stabilize \(I\), and the determinant trick would contradict Lemma 3.1. By maximality, \(J\) factors. Multiplying its factorization by \(\mathfrak p\) gives \(I=J\mathfrak p\), the desired contradiction.

**Proof of uniqueness.** If \(\mathfrak p_1\cdots\mathfrak p_r=\mathfrak q_1\cdots\mathfrak q_s\), then the right side lies in \(\mathfrak p_1\). Primality gives \(\mathfrak q_j\subseteq\mathfrak p_1\) for some \(j\); maximality makes them equal. Multiplication by their inverse cancels that factor. Repeating proves equality of the multisets. A nonempty product of proper ideals cannot equal \(R\), so the cancellation process ends simultaneously. \(\square\)

Every nonzero ideal is therefore invertible. An inverse constructed as a product of prime inverses agrees with \((R:I)\): if \(IJ=R\) and \(xI\subseteq R\), then \(x=xIJ\subseteq J\).

**Corollary 3.4.** The nonzero fractional ideals form a free abelian group with basis the nonzero primes.

**Proof.** A fractional ideal means a nonzero \(R\)-submodule of \(K\) with a common denominator. Over our Noetherian ring it is automatically finite. Choose \(0\ne d\in R\) with \(dI\subseteq R\). Factor \(dI\) and \((d)\), and subtract their prime exponents to write \(I\) as a finite product of integer powers of primes. Uniqueness follows by clearing negative exponents and applying Theorem 3.3. \(\square\)

The quotient by the subgroup of principal fractional ideals is the **ideal class group**. It measures which ideal factorizations can be represented by element factorizations. Containment reverses exponent inequalities: \(I\subseteq J\) if and only if every exponent of \(I\) is at least the corresponding exponent of \(J\). Indeed, containment implies that \(IJ^{-1}\) is integral, and the converse follows by multiplying back.

## 4. Passing to a larger field

**Lemma 4.0, integral trace and norm.** Let \(R\) be integrally closed in its fraction field \(K\), let \(L/K\) be finite, and let \(z\in L\) be integral over \(R\). Then \(\operatorname{Tr}_{L/K}(z)\) and \(N_{L/K}(z)\) belong to \(R\). Separability is unnecessary for this assertion.

**Proof.** On the finite-dimensional \(K\)-vector space \(L\), multiplication by \(z\) is a \(K\)-linear operator. A monic equation for \(z\) over \(R\) annihilates this operator. Each eigenvalue over an algebraic closure of \(K\) therefore satisfies that monic equation and is integral over \(R\). Sums and products of finitely many integral elements are integral: the algebra they generate is spanned over \(R\) by finitely many bounded powers, and multiplication by their sum or product preserves this finite module. The adjugate calculation of Lemma 2.2, now in the algebraic closure field, gives a monic equation. The trace is the sum of the eigenvalues, and the determinant is their product, both with algebraic multiplicity. They already belong to \(K\) as the trace and determinant of the original \(K\)-linear operator. Integral closedness of \(R\) therefore places both in \(R\). \(\square\)

**Theorem 4.1.** If \(R\) is Dedekind and \(L/K\) is finite separable, its integral closure \(B\) in \(L\) is a finite \(R\)-module and is Dedekind.

**Proof.** For a nonfield \(R\), this is Decomposition of primes in extensions, Theorem 5.1, which proves the assertion for arbitrary Dedekind bases and finite separable fraction-field extensions. Its proof bounds the closure by a finite lattice using the inverse trace matrix. That lesson excludes fields in its Dedekind convention. If \(R\) is a field, then \(B=L\), a finite-dimensional \(R\)-module and a Dedekind domain in our convention. \(\square\)

The nondegeneracy of the separable field trace is proved in Discriminants and integral bases, Proposition 2.1, using the embeddings and primitive-element argument supplied in the preceding arithmetic lesson. It is also Orders and the discriminant theorem, Lemma 1.2. Lemma 4.0 supplies trace integrality over our arbitrary integrally closed base. The separable trace-lattice argument therefore has both required inputs. For inseparable extensions the integral closure remains Dedekind, but module finiteness can fail; the following proofs establish both assertions. They do not assume that every Dedekind domain is Japanese.

### Finite quotients without a finite normalization

The separability hypothesis controls finiteness of the normalization as a module. It is unnecessary for its Noetherian ideal theory. The useful estimate is a bound on quotients by one nonzero base element.

**Lemma 4.2, a length bound.** Let \(R\) be a one-dimensional Noetherian domain, \(K\) its fraction field, \(L/K\) a finite extension of degree \(n\), and \(R\subseteq C\subseteq L\) a ring. For \(0\ne a\in R\),

\[
 \operatorname{length}_R(C/aC)
 \leq n\operatorname{length}_R(R/aR)<\infty.
\]

**Proof.** If \(a\) is a unit in \(R\), both quotients vanish. Otherwise \(R/aR\) is Noetherian of dimension zero, so it has finite length by the two earlier results specified in the opening paragraph. Every finite torsion \(R\)-module also has finite length: a nonzero common annihilator \(d\) makes it a finite module over \(R/dR\), hence a quotient of a finite direct sum of this finite-length ring.

Let \(N\subseteq L\) be a finite \(R\)-submodule, of rank \(r=\dim_K(KN)\leq n\). Choose a \(K\)-basis from \(N\); its \(R\)-span \(M\) is free of rank \(r\). The finite quotient \(H=N/M\) is torsion. Multiplication by \(a\), and the inclusions \(M\subseteq N\), give the exact sequence

\[
 0\longrightarrow H[a]\longrightarrow M/aM
  \longrightarrow N/aN\longrightarrow H/aH\longrightarrow0,
\]

where \(H[a]=\{h:ah=0\}\). The first map sends the class of \(z\in N\) with \(az\in M\) to \(az\) modulo \(aM\). It is well-defined and injective because \(N\) is torsion-free; its image is exactly the kernel of the next map. The last two maps are induced by the inclusion and quotient, and the same representatives verify exactness there. Since \(H\) has finite length, its multiplication map shows that \(H[a]\) and \(H/aH\) have equal lengths. Additivity in the displayed sequence therefore gives

\[
 \operatorname{length}_R(N/aN)
    =r\operatorname{length}_R(R/aR).
\]

Every finite \(R\)-submodule of \(C/aC\) is the image of a finite \(R\)-submodule \(N\subseteq C\), obtained by lifting generators. That image is a quotient of \(N/aN\), so its length is at most \(n\operatorname{length}_R(R/aR)\). Choose one such image having the largest possible length. Adding any other finite image cannot increase this length, and hence cannot increase the submodule. Since every element belongs to a finite image, this chosen image is all of \(C/aC\). The required bound follows. \(\square\)

**Theorem 4.3, Krull–Akizuki.** If \(R\) is a one-dimensional Noetherian domain, \(L/\operatorname{Frac}(R)\) is finite, and \(R\subseteq C\subseteq L\), then \(C\) is Noetherian of dimension at most one. No separability or module-finiteness assumption on \(C/R\) is required.

**Proof.** Let \(I\subseteq C\) be a nonzero ideal and choose \(0\ne x\in I\). Its minimal polynomial over \(K\), after clearing denominators, gives

\[
 c_dx^d+\cdots+c_1x+c_0=0,
 \qquad c_i\in R,\quad c_0\ne0.
\]

Thus \(0\ne c_0\in I\cap R\). Put \(a=c_0\). The submodule \(I/aC\) of \(C/aC\) has finite length over \(R\), by Lemma 4.2, hence has finitely many \(R\)-generators. Lift them to \(I\). Those lifts and \(a\) generate \(I\) as a \(C\)-ideal: subtracting their \(R\)-linear combination leaves an element of \(aC\). The zero ideal is already finitely generated, so every ideal is finite and \(C\) is Noetherian.

For a nonzero prime \(\mathfrak q\subset C\), the same argument finds \(0\ne a\in\mathfrak q\cap R\). The ring \(C/aC\) is Artinian, since its ideals are \(R\)-submodules of the finite-length module in Lemma 4.2. Its prime quotient \(C/\mathfrak q\) is an Artinian domain and therefore a field: the chain \((z)\supseteq(z^2)\supseteq\cdots\) stabilizes for \(z\ne0\), and cancellation in \(z^m=z^{m+1}u\) gives \(zu=1\). Hence every nonzero prime of \(C\) is maximal, proving the dimension assertion. Compare [Stacks, Tag 00PG]. \(\square\)

**Corollary 4.4, inseparable integral closure.** The integral closure of a Dedekind domain in any finite fraction-field extension is Dedekind, even if the extension is inseparable. It need not be finite over the base.

**Proof.** For a nonfield base, Theorem 4.3 supplies Noetherianity and dimension at most one. The integral closure is integrally closed: if an element is integral over it, the finitely many coefficients in a monic equation are integral over the base. Adjoin those coefficients and the element; successive power bounds make the resulting algebra finite over the base, and the adjugate argument gives a monic equation over the base for that element. It therefore belongs to the integral closure. These are precisely our Dedekind conditions. For a field base its closure in the finite extension is that extension, which is a field and is included in our convention. The next example proves that finiteness in Theorem 4.1 cannot be carried over to the inseparable case. \(\square\)

**Example 4.5, a DVR with nonfinite integral closure.** Fix a prime \(p\) and let \(k=\mathbb F_p\). Choose a series \(f\in k[[t]]\) transcendental over \(k(t)\). Such a choice exists: \(k(t)\) and its algebraic elements in \(k((t))\) form a countable set, because there are countably many polynomials and each nonzero polynomial has finitely many roots. The set of series over the finite field is uncountable, by the diagonal argument on coefficient sequences.

Inside \(k((t))\), define

\[
 K=k(t,f^p),\qquad L=k(t,f),\qquad
 A=K\cap k[[t]],\qquad B=L\cap k[[t]].
\]

The extension \(L/K\) has degree \(p\) and is purely inseparable. Indeed, the elements \(1,f,\ldots,f^{p-1}\) are linearly independent over \(k(t,f^p)\): clearing rational-function denominators in \(f^p\) would give a polynomial relation in \(f\) whose distinct exponent classes modulo \(p\) cannot cancel. Transcendence forbids it. Their span is closed under multiplication, since \(f^p\in K\), and is a finite-dimensional domain over \(K\). Multiplication by a nonzero element is injective, hence surjective, so this span is a field. It is therefore \(L\). The \(p\)-th power of every element of \(L\) belongs to \(K\).

Both \(A\) and \(B\) are DVRs with uniformizer \(t\) and residue field \(k\). To check this directly, the \(t\)-order of every nonzero element is an integer, and \(t\) lies in both subfields. An element of order zero is a unit in the intersection ring, since its inverse again has order zero. Each nonzero ideal has a least occurring order, and any element of that order generates it. This proves that all nonzero ideals are powers of \((t)\). Reduction takes the constant coefficient in \(k\), and every such coefficient occurs.

The ring \(B\) is the integral closure of \(A\) in \(L\). For \(b\in B\), its \(p\)-th power belongs to \(K\) and has nonnegative order, so \(b^p\in A\); the polynomial \(X^p-b^p\) proves integrality. Conversely an element of negative order cannot satisfy a monic equation with coefficients in \(A\), since its highest power would have strictly smaller order than every other term. Thus every element integral over \(A\) lies in \(B\).

If \(B\) were finite over \(A\), it would be free. Here is the finite torsion-free module argument for a DVR. Lift a basis modulo \(t\); the cokernel of their span satisfies \(M=tM\), so the determinant trick gives \((1+ta)M=0\), forcing it to vanish. A nonzero relation between the lifts, divided by the least power of \(t\) in its coefficients, contradicts their residue independence. The lifts are therefore a free basis. The rank of \(B\) would be \([L:K]=p\): inverting \(t\) gives \(A[1/t]=K\) and \(B[1/t]=L\). It would follow that

\[
 \dim_k(B/tB)=p.
\]

But \(B/tB=k\), of dimension one. This contradiction proves nonfiniteness. A domain is called *Japanese* when its integral closure in every finite fraction-field extension is finite as a module. The DVR \(A\) is not Japanese. This proves the phenomenon referred to by [Stacks, Tag 09E1], with an explicit field and valuation construction.

## 5. Arithmetic and geometric examples

Write \(s=\sqrt{-5}\). The ring of integers of \(\mathbb Q(s)\) is \(R=\mathbb Z[s]\), by the complete quadratic integral-basis proof in Algebraic integers and rings of integers, Theorem 1.4, with \(-5\equiv3\pmod4\). Compare [Milne, Proposition 2.11 and Remark 2.12] for the trace-and-norm test. Its prime ideals

\[
 \mathfrak p=(2,1+s),\qquad
 \mathfrak q=(3,1+s),\qquad
 \mathfrak q'=(3,1-s)
\]

have residue fields \(\mathbb F_2,\mathbb F_3,\mathbb F_3\). Direct multiplication gives \(\mathfrak p^2=(2)\) and \(\mathfrak q\mathfrak q'=(3)\), so

\[
 (6)=\mathfrak p^2\mathfrak q\mathfrak q'.
\]

There are three distinct primes and four factors counted with multiplicity. For example, \(\mathfrak p^2\) is generated by \(4,2+2s,-4+2s\); these generate \((2)\). For the product above \(3\), the generators include \(9,3(1+s),3(1-s),6\), which generate \((3)\). Moreover, \((1+s)=\mathfrak p\mathfrak q\) and \((1-s)=\mathfrak p\mathfrak q'\), as follows either by these generators or by containment and the index \(6\). Thus both element factorizations yield the same ideal factorization.

The ideal \(\mathfrak p\) is not principal: a generator \(a+bs\) would have absolute norm \(a^2+5b^2=2\), which has no integer solution. Its class is nontrivial, and its square is trivial. This proves a nontrivial class group without determining the whole group. The index calculation uses multiplication by \(a+bs\) on the ordered integer basis \(1,s\): its matrix is \(\left(\begin{smallmatrix}a&-5b\\b&a\end{smallmatrix}\right)\), with determinant \(a^2+5b^2\). The equality of lattice index and absolute determinant is proved by integer row and column reduction in Discriminants and integral bases, under *Integer subgroups and lattice indices*.

Let \(k\) have characteristic different from \(2\), and set \(C=k[x,y]/(y^2-x^3-x)\). The polynomial is irreducible because \(x^3+x=x(x^2+1)\) has order one at the irreducible polynomial \(x\), whereas a rational square has even order; a quadratic \(y^2-f\) over a field is reducible only when \(f\) is a square. The two partial derivatives cannot vanish at a point of the curve, even after extending \(k\): \(2y=0\) gives \(y=0\), and if \(x^3+x=0\), then either \(x=0\), with derivative \(1\), or \(x^2=-1\), with derivative \(-2\). The ring \(C\) is a finite integral extension of \(k[x]\), with basis \(1,y\), so it is Noetherian and has dimension one by the earlier module and integral-dimension results in the opening paragraph. At every point its component dimension is one, since it is a domain. The Jacobian row just computed has rank one, so Smooth algebras over a field and the Jacobian criterion, Corollary 2.2, proves smoothness over \(k\), and its Theorem 2.1 proves regularity of each local ring. These statements cover arbitrary ground fields. A one-dimensional regular local ring has a one-dimensional maximal-ideal cotangent space; the earlier DVR characterization then makes it a DVR. Compare [Vakil, 13.2.4/G, 13.2.7(b), 24.8.9 and 13.5.6; Stacks, Tag 00PD]. This smoothness argument works over any field of the stated characteristic. By the earlier Dedekind localization characterization, \(C\) is normal. The generic localization is its fraction field, and all nonzero-prime localizations are the DVRs just obtained. Since it is finite over \(k[x]\), it is precisely the integral closure of \(k[x]\) in its fraction field. The same ideal theory therefore applies to its finite places.

The domain \(\mathbb Z[\sqrt{-3}]\) is Noetherian and one-dimensional but not normal: \((1+\sqrt{-3})/2\) is integral and missing. The next lesson shows directly that \((2)\) does not factor into primes there. Meanwhile \(k[x,y]\) is normal and Noetherian but has the nonmaximal nonzero prime \((x)\). A descending chain above \((x)\) is

\[
 (x,y)\supsetneq(x,y^2)\supsetneq(x,y^3)\supsetneq\cdots.
\]

The ideal \(I=(x^2,y)\) cannot be a product of primes. Each factor would contain \(I\), hence contain its radical \(\mathfrak m=(x,y)\); maximality forces every factor to equal \(\mathfrak m\). But \(I\ne\mathfrak m\), since \(x\notin I\), and \(I\ne\mathfrak m^n\) for \(n\ge2\), since \(y\notin\mathfrak m^2\). This gives a direct failure of ideal factorization when axiom 2 is omitted.

The normality of \(k[x,y]\) used in this comparison also has a direct algebraic proof. A polynomial ring in one variable over a field is a PID by Euclidean division. A PID is integrally closed: if a reduced fraction \(u/v\) satisfies a monic equation, clearing denominators forces \(v\mid u^n\), so coprimality makes \(v\) a unit. Thus an element \(z\in k(x,y)\) integral over \(k[x,y]\) first belongs to \(k(x)[y]\).

For each irreducible polynomial \(q\in k[x]\), give a nonzero polynomial in \(k(x)[y]\) the minimum of the \(q\)-valuations of its coefficients. This minimum is additive under multiplication: remove the two minimum powers, then reduce modulo \(q\); two nonzero polynomials over the residue field have nonzero product. It extends to a valuation on rational functions by subtraction and satisfies the usual sum inequality, with equality for unequal values. The coefficients of a monic equation over \(k[x,y]\) have nonnegative values. If \(z\) had negative value, its highest power in that equation would be the unique term of least value, an impossibility. Hence every coefficient of \(z\), as a polynomial in \(y\), has nonnegative valuation at every irreducible \(q\). Reducing a rational coefficient to coprime numerator and denominator shows that its denominator has no irreducible factor, so it lies in \(k[x]\). Consequently \(z\in k[x,y]\). This proves normality. The Hilbert basis theorem in Noetherian and Artinian rings, Theorem 2.1, proves Noetherianity of this polynomial ring.

## 6. Exercises

1. **Easy.** Factor \((6)\) in \(\mathbb Z[\sqrt{-5}]\), and prove that the class group has a nontrivial element.
2. **Medium.** For \(\mathfrak p=(2,1+\sqrt{-5})\), compute \(\mathfrak p^{-1}\) and verify \(\mathfrak p\mathfrak p^{-1}=R\) directly.
3. **Medium.** Show that \(R/I\) has finite length when \(R\) is Noetherian, every nonzero prime is maximal, and \(I\ne0\).
4. **Medium.** Let \(M\) be a finite module over a commutative ring \(R\), and \(u\in\operatorname{End}_R(M)\). Prove that some monic \(P\in R[T]\) satisfies \(P(u)=0\), without assuming faithfulness. Then let \(x\) belong to a commutative \(R\)-algebra \(S\), and suppose \(M\) is a faithful \(R[x]\)-module finite over \(R\). Prove that \(x\) is integral over \(R\). Explain why faithfulness over \(R\) alone does not suffice in this second assertion.
5. **Hard.** Let \(\operatorname{char}k\ne2\), let \(t^2=x\), and find the integral closure of \(k[x]\) in \(k(t)\). Factor the extensions of \((x)\) and \((x-1)\).

## 7. Solutions

**1.** The computation in Section 5 gives \((6)=\mathfrak p^2\mathfrak q\mathfrak q'\). Its quotient maps verify primality. If \(\mathfrak p=(a+b\sqrt{-5})\), its index would be \(a^2+5b^2=2\), impossible. Thus \([\mathfrak p]\ne1\), while \([\mathfrak p]^2=1\).

**2.** Since \(\mathfrak p^2=(2)\), multiplication shows that \(\mathfrak p/2\) is an inverse. Every inverse is \((R:\mathfrak p)\), as established after Theorem 3.3. Hence

\[
 \mathfrak p^{-1}=R+R(1+\sqrt{-5})/2.
\]

The second generator is outside \(R\). The product is generated by \(2,1+s,(1+s)^2/2\). The last generator is \(s-2\); subtracting it from \(1+s\) gives \(3\), and \(3-2=1\). Thus the product is \(R\).

**3.** The quotient is Noetherian. A prime of the quotient comes from a prime containing \(I\), hence is maximal. The dimension-zero Artinian criterion makes the quotient Artinian. A nonzero module satisfying both chain conditions has a composition series: choose a maximal proper submodule using finite generation, then repeat; the descending chain condition forces termination. Applied to \(R/I\), this gives finite length.

**4.** With generators \(m_i\) and an endomorphism \(u\), choose a matrix \(A\) representing its action on the generators. The adjugate identity gives \(\det(T\operatorname{id}-A)|_{T=u}M=0\). For scalar multiplication by an element of a larger ring, this is a monic equation annihilating \(M\). The endomorphism conclusion \(P(u)=0\) needs no faithfulness. For the scalar conclusion, the action map \(R[x]\to\operatorname{End}_R(M)\) must be injective: faithfulness over \(R[x]\) gives \(P(x)=0\) in that ring. Faithfulness only over \(R\) does not: take \(R=k\), \(S=k[T]\), \(M=S/(T)\) and \(x=T\). The module is faithful over \(k\) and \(x\) acts as zero, but \(T\) is not integral over \(k\). Without the stronger hypothesis, \(P(x)\) need only belong to the \(R[x]\)-annihilator. See [Stacks, Tag 05BT; Vakil, Exercise 8.2.I]. In Lemma 2.2 a nonzero submodule of a field is faithful, so cancellation supplies exactly this step.

**5.** The ring \(k[t]\) is a PID, hence integrally closed, and is integral and finite over \(k[t^2]\). If an element of \(k(t)\) is integral over \(k[t^2]\), the same equation makes it integral over \(k[t]\), so it lies in \(k[t]\). Thus the closure is \(k[t]\). The ideal \((x)\) becomes \((t)^2\), and \((x-1)\) becomes \((t-1)(t+1)\). The two latter primes are distinct because \(2\ne0\) in \(k\).

## What this lesson does not prove

The finite-submodule, finite-length, dimension-zero Artinian, lying-over, incomparability and integral-dimension results have the exact earlier proofs specified in the opening paragraph. The separable closure theorem is Decomposition of primes in extensions, Theorem 5.1; the field case is handled here, and the trace inputs are Lemma 4.0 and the earlier Proposition 2.1 linked in Section 4. Lemma 4.2, Theorem 4.3, Corollary 4.4 and Example 4.5 prove the inseparable closure and nonfiniteness assertions. The two named characterizations in the linked DVR lesson prove the local route; the Jacobian and smooth-regular implications have the exact earlier proofs linked in Section 5, as do the quadratic integer basis and lattice index formula. Polynomial normality is proved directly above. For the local alternative to the global ideal-factorization proof, compare Discrete valuation rings and Dedekind domains, Theorem 3.2. Its convention excludes fields, while the present convention includes them with vacuous nonzero-prime factorization. These are different complete routes to the same ideal theorem for nonfields.

## References

- **[Noether]** Emmy Noether, [*Abstrakter Aufbau der Idealtheorie in algebraischen Zahl- und Funktionenkörpern*](https://visuallibrary.net/download/pdf/154089.pdf), Mathematische Annalen **96** (1927), 26–61, especially Sections 1–3 and 5–8; freely accessible journal scan.
- **[Milne]** J. S. Milne, *Algebraic Number Theory*, Chapters 2–3, [author's course notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- **[Stacks]** The Stacks Project, Tags [034W](https://stacks.math.columbia.edu/tag/034W), [034X](https://stacks.math.columbia.edu/tag/034X), [00PG](https://stacks.math.columbia.edu/tag/00PG), [09IG](https://stacks.math.columbia.edu/tag/09IG) and [09E1](https://stacks.math.columbia.edu/tag/09E1). AI Integrated Stacks Project is an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks Project's maintainers; its [English algebra reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html) has the corresponding labels.

- **[Vakil]** Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), public draft of 27 July 2024, Exercise 8.2.I, Sections 13.2 and 13.5, and 24.8.9.
- **Additional prerequisite tags:** [00FP](https://stacks.math.columbia.edu/tag/00FP), [00KH](https://stacks.math.columbia.edu/tag/00KH), [00KJ](https://stacks.math.columbia.edu/tag/00KJ), [00GQ](https://stacks.math.columbia.edu/tag/00GQ), [00GT](https://stacks.math.columbia.edu/tag/00GT), [00OJ](https://stacks.math.columbia.edu/tag/00OJ), [00PD](https://stacks.math.columbia.edu/tag/00PD), and [05BT](https://stacks.math.columbia.edu/tag/05BT).
