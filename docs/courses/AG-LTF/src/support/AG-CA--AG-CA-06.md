# The Nullstellensatz and Jacobson rings

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Prime ideals turn equations into points, but a prime need not be a closed point. The Nullstellensatz says that over a field, finite algebra generation forces closed points to have finite residue fields. It also says that closed points suffice to detect radical ideals. Jacobson rings isolate this second property and let us carry it from fields to arithmetic bases such as \(\mathbb Z\).

Rings are commutative with identity, and a field is nonzero. A finite extension of fields has finite vector-space dimension; it need not have finitely many elements. We use the Noetherian module and Hilbert basis theorems from *Noetherian and Artinian rings*, and the field criterion and integral-element tests from *Integral extensions: lying over, going up and going down*. The spectrum conventions and radical-ideal correspondence are those of *Spectra of rings*. Only the Artin–Tate theorem below assumes a Noetherian base; the Jacobson permanence theorem does not.

## 1. Why an algebra generated field is finite

The obstacle to finite algebra generation of a rational function field is the supply of new denominators. A finite extension can conceal these denominators, so we first prove a theorem that recovers finite generation of an intermediate algebra.

**Theorem 1.1 (Artin–Tate).** Let \(R\) be Noetherian, \(S\) an \(R\)-algebra of finite type, and \(T\subset S\) an \(R\)-subalgebra. If \(S\) is finite as a \(T\)-module, then \(T\) is of finite type over \(R\).

**Proof.** Choose algebra generators \(s_1,\ldots,s_n\) for \(S\) over \(R\), and module generators \(b_1,\ldots,b_e\) for \(S\) over \(T\), including \(1\) among the latter. Choose coefficients in \(T\) expressing each \(s_i\) as a linear combination of the \(b_j\), and each product \(b_i b_j\) as a linear combination of the \(b_l\). Let \(T_0\subset T\) be generated over \(R\) by this finite list of coefficients. Hilbert's basis theorem makes \(T_0\) Noetherian.

The module \(U=\sum_j T_0b_j\subset S\) contains \(1\) and every \(s_i\). The chosen product coefficients show it is closed under multiplication. It is therefore an \(R\)-subalgebra containing all the algebra generators of \(S\), so \(U=S\). Thus \(S\) is finite over \(T_0\). The submodule \(T\subset S\) is finite over the Noetherian ring \(T_0\), by the finite-module submodule theorem. Adjoining its module generators to the algebra generators of \(T_0\) gives a finite set of \(R\)-algebra generators for \(T\). \(\square\)

Including the identity in the module generators ensures that their smaller coefficient span is a unital algebra. No injectivity assumption on the structure map from \(R\) is needed.

**Lemma 1.2 (rational functions need infinitely many denominators).** If \(r\geq1\), the field \(k(X_1,\ldots,X_r)\) is not of finite type as a \(k\)-algebra.

**Proof.** Suppose finitely many fractions generate it. If \(g\) is the product of their nonzero polynomial denominators, all expressions in these generators lie in

\[
k[X_1,\ldots,X_r][1/g].
\]

There are infinitely many monic irreducibles in \(k[X_1]\). Otherwise, the product of their finite list, plus \(1\), would be a nonconstant polynomial with an irreducible factor absent from the list. This argument works over finite fields as well.

Expand \(g\) in \(X_2,\ldots,X_r\), with coefficients in \(k[X_1]\). One coefficient is nonzero, and has only finitely many irreducible factors. Choose a monic irreducible \(h(X_1)\) not dividing this coefficient, hence not dividing \(g\). The ideal \((h)\) in the multivariable polynomial ring is prime, since its quotient is the polynomial ring in \(X_2,\ldots,X_r\) over the field \(k[X_1]/(h)\). If \(1/h\) belonged to the displayed localization, we could write \(1/h=a/g^N\), giving \(g^N=ah\). Primality would force \(h\mid g\), a contradiction. But \(1/h\) belongs to the rational function field. \(\square\)

**Theorem 1.3 (Zariski's lemma).** If a field \(L\) is of finite type as a \(k\)-algebra, then \(L/k\) is a finite field extension.

**Proof.** Write \(L=k[a_1,\ldots,a_n]\). Reorder a maximal algebraically independent subset of these generators as \(a_1,\ldots,a_r\). Every remaining generator is algebraic over \(F=k(a_1,\ldots,a_r)\). Indeed, adjoining it to the chosen subset gives a polynomial relation, whose nonzero coefficients in \(k[a_1,\ldots,a_r]\) remain nonzero in \(F\). Since \(L\) is a field, it contains \(F\), and

\[
L=F[a_{r+1},\ldots,a_n].
\]

The finite list of algebraic generators makes \(L\) finite over \(F\), either by multiplying the finite power spans or by Theorem 1.2 of the integral-extensions lesson. Apply Artin–Tate to \(k\subset F\subset L\): it makes \(F\) a finite-type \(k\)-algebra. If \(r>0\), algebraic independence identifies \(F\) with the rational function field of Lemma 1.2, giving a contradiction. Therefore \(r=0\), and \(L\) is generated by finitely many elements algebraic over \(k\), so is finite over \(k\). \(\square\)

This proof supplies Zariski's lemma before dimension theory. Noether normalization will give another route in *Krull dimension and Noether normalization*.

## 2. Closed points detect radical equations

**Theorem 2.1 (weak Nullstellensatz).** For any maximal ideal \(\mathfrak m\) of a finite-type \(k\)-algebra \(A\), the residue field \(\kappa(\mathfrak m)=A/\mathfrak m\) is finite over \(k\). If \(k\) is algebraically closed, the maximal ideals of \(k[X_1,\ldots,X_n]\) are exactly

\[
\mathfrak m_a=(X_1-a_1,\ldots,X_n-a_n),
\qquad a=(a_1,\ldots,a_n)\in k^n.
\]

**Proof.** The quotient \(A/\mathfrak m\) is a field and a finite-type \(k\)-algebra, so Theorem 1.3 applies. When \(k\) is algebraically closed, every element of a finite extension has a minimal polynomial of degree one, and the extension equals \(k\). In the polynomial case the images of the variables are then elements \(a_i\in k\). The ideal \(\mathfrak m_a\) lies in \(\mathfrak m\), and its quotient is \(k\), by evaluation at \(a\). It is maximal, so equals \(\mathfrak m\). Conversely this same quotient proves that every \(\mathfrak m_a\) is maximal. \(\square\)

For an ideal \(I\subset k[X_1,\ldots,X_n]\), let \(Z_k(I)\subset k^n\) be its common zero set. For \(Y\subset k^n\), write \(I_k(Y)\) for the ideal of polynomials vanishing on \(Y\). These concern \(k\)-valued points, while \(V_A(I)\) denotes a closed subset of the full prime spectrum.

**Theorem 2.2 (strong Nullstellensatz).** For any finite-type \(k\)-algebra \(A\) and ideal \(I\subset A\),

\[
\sqrt I=\bigcap_{\substack{\mathfrak m\text{ maximal in }A\\I\subset\mathfrak m}}\mathfrak m.
\tag{1}
\]

If \(k\) is algebraically closed and \(A=k[X_1,\ldots,X_n]\), then

\[
I_k(Z_k(I))=\sqrt I.
\tag{2}
\]

**Proof.** Every maximal ideal containing \(I\) contains \(\sqrt I\). To prove the reverse inclusion in (1), take \(f\notin\sqrt I\). The algebra \(B=(A/I)[1/\bar f]\) is nonzero: if \(1=0\) in it, the localization equality criterion would put some power of \(f\) in \(I\). It is of finite type over \(k\), since adjoining the inverse adds only one algebra generator. Choose a maximal ideal \(\mathfrak n\subset B\). Theorem 2.1 makes \(L=B/\mathfrak n\) finite over \(k\).

Let \(\mathfrak m\) be the kernel of \(A\to L\). The domain \(A/\mathfrak m\subset L\) contains \(k\), and every one of its elements is algebraic, hence integral, over \(k\). The integral field criterion makes \(A/\mathfrak m\) a field, so \(\mathfrak m\) is maximal. It contains \(I\), and avoids \(f\), since the image of \(f\) is a unit in \(B\) and remains nonzero in \(L\). This separates every element outside \(\sqrt I\) from the intersection, proving (1).

For (2), Theorem 2.1 identifies the maximal ideals containing \(I\) with points \(a\in Z_k(I)\). A polynomial belongs to \(\mathfrak m_a\) exactly when it vanishes at \(a\), so their intersection is \(I_k(Z_k(I))\). Now apply (1). Empty intersections are interpreted as the whole ring, including the case \(I=A\). \(\square\)

The geometric form also has a useful certificate, called the **Rabinowitsch trick**. If \(k\) is algebraically closed and \(f\) vanishes on \(Z_k(I)\), then

\[
1\in I\,k[X_1,\ldots,X_n,T]+(1-Tf).
\tag{3}
\]

Indeed, a maximal ideal containing this ideal, if it were proper, would correspond to a point \((a,b)\in k^{n+1}\) with \(a\in Z_k(I)\) and \(1-bf(a)=0\). But \(f(a)=0\), giving a contradiction. Thus (3) yields a polynomial identity

\[
1=\sum_{j=1}^s H_j(X,T)g_j(X)+H(X,T)(1-Tf(X)),
\qquad g_j\in I.
\]

If \(f\ne0\), substitute \(T=1/f\) in the localization of the polynomial domain and clear denominators to obtain \(f^N\in I\) for some \(N\). If \(f=0\), membership in \(\sqrt I\) is immediate. This proves (2) by a second route and turns pointwise vanishing into an explicit ideal-membership certificate. The full identity and the denominator step are worked out in Solution 7.5.

## 3. The Jacobson property

A ring \(R\) is **Jacobson** if every prime \(\mathfrak p\) is the intersection of the maximal ideals containing \(\mathfrak p\). This is different from the **Jacobson radical**, which is just the intersection of all maximal ideals of a ring; the property requires the analogous equality over every prime.

**Proposition 3.1 (three descriptions).** The following are equivalent:

1. \(R\) is Jacobson.
2. Every radical ideal is the intersection of the maximal ideals containing it.
3. The closed points are dense in every closed subset of \(\operatorname{Spec}R\).

Every quotient of a Jacobson ring is Jacobson.

**Proof.** Condition (2) implies (1), since a prime is radical. Conversely, take a radical ideal \(I\) and \(f\notin I\). The intersection-of-primes theorem supplies \(\mathfrak p\supset I\) with \(f\notin\mathfrak p\). Condition (1) gives a maximal ideal \(\mathfrak m\supset\mathfrak p\) avoiding \(f\). Thus \(f\) is absent from the intersection in (2), proving equality.

The closed points of \(V(I)\) are the maximal ideals containing \(I\). If their intersection is \(J\), their closure is \(V(J)\): these are exactly the equations shared by those points. The ideal \(J\) is radical. Consequently density in \(V(I)\) is equivalent to \(J=\sqrt I\), by the radical-ideal correspondence of Proposition 2.2 of *Spectra of rings*. This proves (2) equivalent to (3). Finally, primes and maximal ideals of \(R/K\) correspond to the respective ideals of \(R\) containing \(K\); passing the defining intersection equality to the quotient proves the last assertion. \(\square\)

**Proposition 3.2 (basic examples).** Fields and principal ideal domains with infinitely many maximal ideals are Jacobson. In particular \(\mathbb Z\) is Jacobson. A local ring of positive dimension is not Jacobson, even without a Noetherian hypothesis.

**Proof.** In a field the only prime is zero and is maximal. In a principal ideal domain every nonzero prime is maximal, since its generator is irreducible and Bezout's identity makes the quotient a field. It remains to express zero as the intersection of maximal ideals. A nonzero element has only finitely many irreducible factors, so belongs to only finitely many maximal ideals. If there are infinitely many maximal ideals, one avoids that element. Their intersection is therefore zero. The integer primes are infinite by Euclid's argument, giving the assertion for \(\mathbb Z\).

In a local ring \((R,\mathfrak m)\), the intersection of the maximal ideals containing any prime is just \(\mathfrak m\). Hence such a ring is Jacobson exactly when every prime equals \(\mathfrak m\). Positive dimension supplies a prime strictly below \(\mathfrak m\), so the property fails. \(\square\)

In particular, density of closed points in the whole spectrum is insufficient unless it also holds in every closed subset. The definition places this demand on every prime quotient, including quotients representing individual irreducible closed sets.

## 4. Finite type over a Jacobson base

The next lemma is the algebraic step that replaces the base by a field on a suitable open subset.

**Lemma 4.1 (a finite-type field over a domain).** Suppose \(A\subset L\), where \(L\) is a field of finite type over \(A\). There is a nonzero \(f\in A\) such that \(A_f\) is a field and \(L/A_f\) is finite. If \(A\) is Jacobson, \(A\) itself is a field and \(L/A\) is finite.

**Proof.** The subring \(A\) is a domain; let \(K=\operatorname{Frac}(A)\). Writing \(L=A[b_1,\ldots,b_r]\), we also have \(L=K[b_1,\ldots,b_r]\), because \(L\) contains \(K\). Zariski's lemma makes \(L/K\) finite. Choose monic equations for the \(b_i\) over \(K\), and let \(f\ne0\) be the product of their coefficient denominators in \(A\). Every \(b_i\) is integral over \(A_f\), and \(L=A_f[b_1,\ldots,b_r]\), since \(L\) is already a field. Thus \(L\) is finite and integral over \(A_f\). The integral field criterion makes \(A_f\) a field, and finiteness gives the first assertion.

If \(A\) is Jacobson, the intersection of its maximal ideals is zero, since zero is prime. Some maximal ideal \(\mathfrak m\) avoids the nonzero \(f\). Its extension to the field \(A_f\) is a prime, hence zero, whose contraction is zero by the domain property. Prime correspondence gives \(\mathfrak m=0\), so \(A\) is a field. Then \(A_f=A\), and the first assertion gives finiteness. \(\square\)

**Theorem 4.2 (general Nullstellensatz and Jacobson permanence).** If \(R\) is Jacobson and \(R\to S\) is of finite type, then \(S\) is Jacobson. Every maximal ideal \(\mathfrak n\subset S\) contracts to a maximal ideal \(\mathfrak m\subset R\), and

\[
\kappa(\mathfrak n)/\kappa(\mathfrak m)
\quad\text{is a finite field extension}.
\]

**Proof.** First take a maximal \(\mathfrak n\) and its contraction \(\mathfrak p\). The quotient \(A=R/\mathfrak p\) is a Jacobson domain by Proposition 3.1 and embeds in the field \(L=S/\mathfrak n\), which is of finite type over \(A\). Lemma 4.1 makes \(A\) a field and \(L/A\) finite. Thus \(\mathfrak p\) is maximal and the stated residue extension is finite.

To prove \(S\) Jacobson, fix a prime \(\mathfrak q\subset S\) and \(s\notin\mathfrak q\). The nonzero algebra \(B=(S/\mathfrak q)[1/\bar s]\) is of finite type over \(R\). Choose a maximal ideal \(M\subset B\). The part just proved makes its contraction \(\mathfrak m\subset R\) maximal and \(L=B/M\) finite over \(k=R/\mathfrak m\). Let \(N\) be the kernel of \(S\to L\). It contains \(\mathfrak q\) and avoids \(s\), whose image is invertible. Moreover

\[
k\subset S/N\subset L.
\]

Every element of the intermediate domain is algebraic over \(k\), hence integral. The integral field criterion makes \(S/N\) a field. Therefore \(N\) is a maximal ideal containing \(\mathfrak q\) and avoiding \(s\). Every element outside \(\mathfrak q\) can be separated this way, so \(\mathfrak q\) is the intersection of the maximal ideals containing it. \(\square\)

In particular, inverting one element preserves the Jacobson property: \(R_f\) is of finite type over \(R\). Its maximal ideals correspond to maximal ideals of \(R\) avoiding \(f\), since contraction is maximal and localization preserves the quotient field. Arbitrary localizations need not have this property, as the next examples show.

## 5. Equations, residue fields and arithmetic points

**Lemma 5.1 (the fundamental theorem of algebra).** Every nonconstant complex polynomial has a complex root.

**Proof.** We use only the usual real-analysis facts that a continuous function attains its minimum on a compact disk and that complex numbers have polar form. For a polynomial \(f\) of positive degree, its leading term implies \(|f(z)|\to\infty\) as \(|z|\to\infty\): outside a sufficiently large disk the leading term is larger than the sum of the absolute values of all lower terms. Thus \(|f|\) attains a global minimum, at \(z_0\). If \(f(z_0)\ne0\), write
\[
\frac{f(z_0+w)}{f(z_0)}=1+aw^r+w^{r+1}g(w),
\qquad a\ne0,
\]
where \(r\ge1\) is the least nonzero positive-degree coefficient. Choose a unit complex number \(u\) with \(au^r=-|a|\), using its polar angle divided by \(r\). For \(w=tu\), \(t>0\) small, \(g\) is bounded by some \(C\) on the unit disk, and
\[
\left|\frac{f(z_0+tu)}{f(z_0)}\right|
\le1-|a|t^r+Ct^{r+1}<1
\]
as soon as \(|a|t^r<1\) and \(Ct<|a|\). This contradicts minimality. Hence \(f(z_0)=0\). Dividing by the corresponding linear factor and inducting on degree shows that every complex polynomial splits into linear factors. \(\square\)

**The real line and the complex plane.** The maximal ideals of \(\mathbb R[X]\) are generated by monic irreducible polynomials. They are precisely

\[
(X-a),\qquad a\in\mathbb R,
\quad\text{and}\quad
(X^2-2aX+a^2+b^2),\qquad a\in\mathbb R,\ b>0.
\]

Here we use the algebraic closedness of \(\mathbb C\), the fundamental theorem of algebra. To obtain the list, a nonconstant real polynomial has a complex root. A real root gives a linear factor. A nonreal root \(a+bi\) occurs with its conjugate, and division by their product gives a real quadratic factor: polynomial division by this real monic quadratic has real remainder of degree at most one, and vanishing at both distinct roots forces that remainder to be zero. The displayed quadratic has no real root because it is \((X-a)^2+b^2\), so is irreducible. These observations leave only degrees one and two for a real irreducible. The quadratic quotient is \(\mathbb C\), by evaluation at \(a+bi\); the image contains \(i=(a+bi-a)/b\). Thus the real affine line has closed points with residue fields \(\mathbb R\) and \(\mathbb C\). Real-valued points alone miss the second kind: \(X^2+1\) has no real zero, but generates a proper radical ideal. The strong geometric Nullstellensatz requires an algebraically closed field.

In \(\mathbb C[X,Y]\), Theorem 2.1 instead gives every maximal ideal as \((X-a,Y-b)\), with \((a,b)\in\mathbb C^2\). The prime \((Y)\) is the generic point of the horizontal line, while its closed points are \((X-a,Y)\). Their intersection is \((Y)\), as follows either from Theorem 2.2 or by evaluating the restriction of a polynomial at every \(a\in\mathbb C\). A nonzero one-variable polynomial cannot vanish at infinitely many distinct values, by successive division by its linear factors.

**Localization can leave only one closed point.** For an integer prime \(p\), the ring \(\mathbb Z_{(p)}\) has primes \((0)\) and \((p)\), by prime correspondence. The sole maximal ideal \((p)\) has nonzero intersection with itself, whereas the zero prime must be the intersection of the maximal ideals containing it for the ring to be Jacobson. Thus this localization of the Jacobson ring \(\mathbb Z\) is not Jacobson. It inverts all integers outside \((p)\), rather than just one chosen element.

Similarly, \(k[[X]]\) is a local domain whose nonzero series is \(X^n u\), where \(u\) has nonzero constant term. Such a series \(u\) is a unit: its inverse coefficients are obtained recursively from the equation \(uv=1\). Every nonzero prime therefore contains \(X\), and \((X)\) is maximal with quotient \(k\). Its only primes are \((0)\) and \((X)\), so it has dimension one and is not Jacobson. Both examples show that a useful local ring need not share the Jacobson property of a global polynomial ring.

**Closed points over the integers.** Every maximal ideal of \(\mathbb Z[X]\) has the form

\[
(p,G(X)),
\tag{4}
\]

where \(p\) is an integer prime and the reduction \(g\in\mathbb F_p[X]\) of \(G\) is monic irreducible of positive degree. Indeed, Theorem 4.2 contracts a maximal ideal to \((p)\subset\mathbb Z\). Its image in \(\mathbb F_p[X]\) is maximal, hence generated by a monic irreducible \(g\). Lifting \(g\) proves (4). Conversely, the quotient by (4) is the field \(\mathbb F_p[X]/(g)\), so the ideal is maximal. If \(\deg g=d\), this field has \(p^d\) elements, since the classes of \(1,X,\ldots,X^{d-1}\) form an \(\mathbb F_p\)-basis. For example, \((2,X^2+X+1)\) has residue field with four elements, while \((2,X)\) has residue field with two. These closed points include polynomial information as well as the characteristic of the residue field; no maximal ideal lies over the zero prime of \(\mathbb Z\).

**The parabola meets its tangent with a nilpotent direction.** In \(k[X,Y]\), over any field, put

\[
I=(Y-X^2,Y)=(Y,X^2).
\]

The equality follows by subtracting the two original generators. The quotient is \(k[X]/(X^2)\). In it, the class of \(X\) is nonzero and has square zero: nonmembership of \(X\) in \((X^2)\) follows from degrees. Hence

\[
\sqrt I=(X,Y),
\qquad k[X,Y]/\sqrt I\simeq k.
\tag{5}
\]

One can verify the radical equality by noting that every prime containing \(X^2\) contains \(X\), or directly by describing nilpotents in the quotient. The common zero set consists of the origin. It records the radical (5); the original quotient also records the nonzero nilpotent \(X\). This is how the ideal distinguishes a tangent intersection from its underlying set of points. In this example the equality \(I_k(Z_k(I))=(X,Y)\) holds even when \(k\) is not algebraically closed, because the only zero is explicitly the origin. It does not imply the general geometric theorem over that field.

## 6. An optional uncountable-field extension

Finite generation in Zariski's lemma cannot usually be replaced by countable generation. Over an uncountable base, however, a useful part of its conclusion survives.

**Theorem 6.1.** Let \(k\) be uncountable and let a field \(L\) be generated by at most countably many elements as a \(k\)-algebra. Then \(L/k\) is algebraic. If \(k\) is also algebraically closed, \(L=k\).

**Proof.** Monomials of finite degree in a countable list of generators form a countable family: their finite index lists and exponent lists form a countable union of countable sets. They span \(L\) as a \(k\)-vector space. Enumerate this spanning family, and let \(V_n\) be the span of its first \(n\) members. A linearly independent family has at most \(n\) members in \(V_n\). Since every vector is in some \(V_n\), every linearly independent family in \(L\) is at most countable.

Suppose \(t\in L\) is transcendental over \(k\). The elements

\[
\frac{1}{t-a},\qquad a\in k,
\]

are linearly independent over \(k\). For a finite relation with distinct \(a_1,\ldots,a_e\), multiply by \(\prod_j(t-a_j)\) to obtain

\[
\sum_{i=1}^e c_i\prod_{j\ne i}(t-a_j)=0.
\]

Transcendence makes the corresponding polynomial in an indeterminate zero. Evaluating at \(a_i\) gives \(c_i\prod_{j\ne i}(a_i-a_j)=0\), so every \(c_i=0\). This is an uncountable independent family, contradicting the preceding paragraph. Thus every element of \(L\) is algebraic over \(k\). For algebraically closed \(k\), each of their minimal polynomials has degree one, and \(L=k\). \(\square\)

This theorem asserts algebraicity, without a finite-degree conclusion. For a countable field \(k\), the rational function field \(k(t)\) is a counterexample to algebraicity under countable algebra generation: adjoining \(t\) and the inverses of all nonzero polynomials in \(k[t]\) generates the whole field. There are countably many such polynomials, but \(t\) remains transcendental.

## 7. Exercises

**Exercise 7.1 (easy: denominators over the integers).** Prove that \(\mathbb Q\) is not of finite type as a \(\mathbb Z\)-algebra. Make the obstruction explicit for any proposed finite list of rational generators.

**Exercise 7.2 (easy: the radical of a tangent intersection).** In \(k[X,Y]\), compute the radical of \(I=(Y-X^2,Y)\). Determine the common zeros, the quotient ring, and a nonzero nilpotent in that quotient. Explain which information is lost on replacing \(I\) by its radical.

**Exercise 7.3 (medium: a field over the integers).** Let a field \(L\) be of finite type as a \(\mathbb Z\)-algebra. Prove that \(L\) is a finite set. Distinguish this assertion from finiteness of a field extension, and determine the possible characteristics.

**Exercise 7.4 (medium: a local obstruction).** Prove that a Noetherian local ring of positive dimension is not Jacobson. Determine whether the Noetherian hypothesis is needed. Give two explicit rings to which the conclusion applies.

**Exercise 7.5 (medium: the Rabinowitsch certificate).** Let \(k\) be algebraically closed, \(I\subset k[X_1,\ldots,X_n]\), and let \(f\) vanish on \(Z_k(I)\). Prove that the ideal

\[
I\,k[X_1,\ldots,X_n,T]+(1-Tf)
\]

is the whole polynomial ring. Write an identity expressing \(1\) in that ideal and use substitution and denominator clearing to prove \(f^N\in I\) for some positive integer \(N\). Include \(f=0\).

**Exercise 7.6 (hard: detecting and mapping closed points).** For a finite-type \(k\)-algebra \(A\), prove that \(\mathfrak p\in\operatorname{Spec}A\) is closed if and only if \(\kappa(\mathfrak p)/k\) is finite. For a homomorphism \(A\to B\) of finite-type \(k\)-algebras, prove that the induced map \(\operatorname{Spec}B\to\operatorname{Spec}A\) sends closed points to closed points. Does this require either algebra to be finite as a module over the other?

## 8. Solutions

**Solution 7.1.** For generators \(q_i=a_i/b_i\), with \(b_i\ne0\), put \(d=\prod_i b_i\); for an empty list take \(d=1\). Every polynomial expression in the \(q_i\) with integer coefficients belongs to \(\mathbb Z[1/d]\). There is a prime \(p\) not dividing \(d\), by the infinitude of integer primes. If \(1/p=c/d^n\), then \(d^n=pc\), forcing \(p\mid d\), a contradiction. Thus the proposed algebra omits \(1/p\), and cannot equal \(\mathbb Q\). If \(d\) is a unit, the argument still applies with any prime. Inverting every nonzero integer gives the field, but no finite list of denominators does so.

**Solution 7.2.** Subtraction of \(Y-X^2\) from \(Y\) gives \(X^2\); conversely \(Y-X^2\) belongs to \((Y,X^2)\). Hence \(I=(Y,X^2)\) and the quotient is \(k[X]/(X^2)\). Its elements have unique representatives \(a+bX\). If such an element is nilpotent, its constant term \(a\) is nilpotent in the field \(k\), so \(a=0\). Conversely every \(bX\) has square zero. The nilradical of the quotient is therefore generated by the nonzero class of \(X\), and its inverse image is \(\sqrt I=(X,Y)\). The equation \(Y=0\) followed by \(X^2=0\) forces every field-valued zero to be the origin. Its vanishing ideal is \((X,Y)\), as the constant term test shows. Replacing \(I\) by its radical gives the field \(k\) and removes the nilpotent direction. The original quotient has basis \(1,X\) as a \(k\)-vector space; the radical quotient has basis \(1\).

**Solution 7.3.** The ring \(\mathbb Z\) is Jacobson by Proposition 3.2. Apply Theorem 4.2 to \(\mathbb Z\to L\) and the maximal ideal \((0)\subset L\). Its contraction to \(\mathbb Z\) must be a maximal ideal \((p)\), and \(L/\mathbb F_p\) is a finite extension. Write its degree as \(d\geq1\). A vector-space basis identifies its underlying set with \(\mathbb F_p^d\), so it has exactly \(p^d\) elements. Thus characteristic zero cannot occur. Every finite field is of finite type as a \(\mathbb Z\)-algebra, since a finite basis over its prime field supplies finitely many algebra generators. A finite extension of an infinite field still has infinitely many elements; here finiteness as a set follows from the finite prime field together with the finite extension degree.

**Solution 7.4.** Let \((R,\mathfrak m)\) be local. All its primes are contained in \(\mathfrak m\), since every proper ideal lies in a maximal ideal and there is only one. Positive dimension provides a strict chain of primes, so in particular there is a prime \(\mathfrak p\subsetneq\mathfrak m\). The intersection of maximal ideals containing \(\mathfrak p\) is \(\mathfrak m\), which is not \(\mathfrak p\). This violates the Jacobson definition. Neither the existence of the chain nor the intersection argument uses Noetherianity. Section 5 supplies \(\mathbb Z_{(p)}\) and \(k[[X]]\), each with exactly the two primes zero and its nonzero maximal ideal. They are also Noetherian: the first is a localization of \(\mathbb Z\); in the second, any nonzero ideal has an element of least order \(n\), which is \(X^n\) times a unit, and all other elements are divisible by \(X^n\). That ideal is \((X^n)\), so every ideal is finitely generated.

**Solution 7.5.** Set \(P=k[X_1,\ldots,X_n]\) and \(J=I P[T]+(1-Tf)\). If \(J\) were proper, a maximal ideal containing it would, by the weak Nullstellensatz in \(n+1\) variables, be the evaluation ideal at some \((a,b)\in k^{n+1}\). Every element of \(I\) would vanish at \(a\), so \(a\in Z_k(I)\), and then \(f(a)=0\). But \(1-Tf\) would evaluate to \(1-bf(a)=1\), contradicting its membership in that maximal ideal. Thus \(J=P[T]\). Ideal membership uses a finite sum, even if we have not chosen generators for \(I\), so there are \(g_1,\ldots,g_s\in I\) and \(H_j,H\in P[T]\) with

\[
1=\sum_{j=1}^s H_j(X,T)g_j(X)+H(X,T)(1-Tf(X)).
\]

For \(f\ne0\), the substitution map \(P[T]\to P[1/f]\), sending \(T\) to \(1/f\), gives \(1=\sum_j H_j(X,1/f)g_j\). Choose a positive integer \(N\) at least as large as every \(T\)-degree of a nonzero \(H_j\). Multiplication by \(f^N\) gives

\[
f^N=\sum_{j=1}^s \bigl(f^N H_j(X,1/f)\bigr)g_j,
\]

and each coefficient in parentheses is in \(P\). The equality initially holds in the localization; since \(P\) is a domain and \(f\ne0\), its localization map is injective, so the equality holds in \(P\) itself. The right side lies in \(I\), proving \(f^N\in I\). If \(f=0\), the generator \(1-Tf\) is already \(1\), and \(f^1=0\in I\), so both conclusions are immediate. This proof covers the empty zero set as well as a nonempty one.

**Solution 7.6.** A prime is closed in the spectrum exactly when it is maximal, by the specialization relation. If \(\mathfrak p\) is maximal, the weak Nullstellensatz makes \(A/\mathfrak p=\kappa(\mathfrak p)\) finite over \(k\). Conversely, suppose the field \(\kappa(\mathfrak p)=\operatorname{Frac}(A/\mathfrak p)\) is finite over \(k\). Every element of its subdomain \(A/\mathfrak p\) is algebraic over \(k\), so this domain is integral over the field \(k\). The integral field criterion says that it is a field. Thus \(\mathfrak p\) is maximal and is closed.

Now take a closed point \(\mathfrak n\) of \(\operatorname{Spec}B\), and let \(\mathfrak p\) be its contraction to \(A\). The map embeds \(A/\mathfrak p\) in \(B/\mathfrak n\), a finite extension of \(k\). The same integral-field argument makes \(A/\mathfrak p\) a field, so \(\mathfrak p\) is closed. No module finiteness of \(B\) over \(A\) is required. For example, the inclusion \(k\subset k[T]\) has this closed-point property although \(k[T]\) has infinitely many linearly independent powers of \(T\) over \(k\) and is not a finite \(k\)-module. The direction of the spectral map is from the target ring's spectrum to the source ring's spectrum.

## Proof dependencies

Lemma 5.1 proves the fundamental theorem of algebra used in the real and complex examples, from compactness and polar form in elementary real analysis. The Stacks Fields chapter gives a different algebraic route at [Tag 09I5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-C-algebraically-closed). Artin–Tate, Zariski's lemma, both Nullstellensatz forms, the Jacobson characterizations and permanence theorem, and the uncountable-field result have full proofs here.

## References

- The Stacks project authors, *The Stacks project*, Commutative Algebra: [Tag 00IS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Artin-Tate) for Artin–Tate; [Tag 00FV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-nullstellensatz) for the Nullstellensatz; [Tag 00FY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-field-finite-type-over-domain) for the finite-type field lemma; [Tag 00FU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-uncountable-nullstellensatz) for the optional uncountable-field variant.
- The same work, Jacobson rings: [Tag 00G0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-ring-jacobson) for the definition, [Tag 00G3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-jacobson) for the topological characterization, [Tag 00G4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-pid-jacobson) for the integer and one-dimensional examples, and [Tag 00G9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Jacobson-mod-ideal) for quotients. Finite-type permanence and maximal-ideal contraction are in [Tag 00GB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-Jacobson-permanence); the algebraic residue-field criterion is in [Tag 00GA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-residue-extension-closed). The links use the AI Integrated Stacks Project English reader described in the course introduction.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Section 3.2, especially 3.2.4 on real and complex points and 3.2.5–6 on the Nullstellensatz. These passages give the point dictionary and theorem statements, with proof routes elsewhere in the book. [Author’s public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).
- Timothy J. Ford, *Commutative Algebra*, version of 23 September 2026, Chapter 5, Section 2: the Artin–Tate lemma for a tower of rings, Zariski’s lemma and both forms of Hilbert’s Nullstellensatz. [Author’s version](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf).
