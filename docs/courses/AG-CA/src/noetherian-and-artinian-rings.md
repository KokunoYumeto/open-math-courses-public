# Noetherian and Artinian rings

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An ideal can describe infinitely many equations even when a geometric problem initially presents only a few. The Noetherian condition says that this proliferation eventually stops: every ideal, including an ideal produced by elimination or a kernel, has finitely many generators. The Artinian condition controls a different phenomenon. It prevents infinitely many successive quotients from extracting smaller pieces of a module. When both conditions hold, a module can be measured by a finite list of simple pieces.

We will connect these finiteness conditions to two questions about powers of an ideal. How does the filtration on a module meet a submodule? Can a nonzero element belong to every power? The answers are Artin–Rees and Krull intersection. Their proofs explain exactly where finite generation enters.

Rings are commutative with identity, and modules are unital. “Finite” means finitely generated. A local ring has exactly one maximal ideal; it need not be Noetherian unless we say so. We use exactness of localization and the determinant form of Nakayama from *Localization, local properties and support*. The zero ring is allowed, has empty spectrum, and has length zero as a module over itself.

## 1. Three ways to recognize a Noetherian module

A module is **Noetherian** if every ascending chain of submodules stabilizes. A ring is Noetherian if it is Noetherian as a module over itself, so the condition concerns its ideals.

**Theorem 1.1.** For an arbitrary module \(M\), the following conditions are equivalent:

1. Every ascending chain of submodules stabilizes.
2. Every nonempty family of submodules contains a maximal member under inclusion.
3. Every submodule of \(M\) is finite.

**Proof.** If a nonempty family has no maximal member, start with one member and successively choose a strictly larger member of that family. This produces a nonstabilizing ascending chain. Thus the first condition implies the second. Conversely, a maximal member of the family formed by a chain forces that chain to stabilize.

Apply the second condition to the finite submodules of a fixed submodule \(N\). Choose a maximal one, \(L\). If \(x\in N\setminus L\), the submodule \(L+Rx\) is finite and strictly larger, a contradiction. Hence \(N=L\). Finally, suppose every submodule is finite and consider a chain \(N_1\subseteq N_2\subseteq\cdots\). Its union is a submodule. Finitely many generators of the union all belong to one \(N_j\), so the union equals \(N_j\) and the chain stabilizes. \(\square\)

In particular, a Noetherian module itself is finite. The converse requires a condition on the ring: one generator over an arbitrary ring need not control the relations among its multiples.

**Proposition 1.2.** Submodules and quotients of Noetherian modules are Noetherian. In an exact sequence

\[
0\longrightarrow L\longrightarrow M\longrightarrow N\longrightarrow0,
\]

the module \(M\) is Noetherian if and only if both \(L\) and \(N\) are Noetherian. Consequently every finite module over a Noetherian ring is Noetherian.

**Proof.** Submodules inherit the condition that their submodules are finite. Submodules of a quotient correspond to submodules containing the kernel, so ascending chains lift to ascending chains upstairs. This proves the forward implication.

For the converse, let \(K\subseteq M\). Its intersection with \(L\) is finite, and its image in \(N\) is finite. Lift finitely many generators of that image to \(K\), and adjoin generators of \(K\cap L\). They generate \(K\): subtracting a combination of the lifts from any element leaves an element of the intersection. Thus every \(K\) is finite. A finite direct sum of copies of a Noetherian ring is Noetherian by repeated extensions, and any finite module is a quotient of such a sum. \(\square\)

There are already instructive examples. Every ideal of \(\mathbb Z\) is principal, so \(\mathbb Z\) is Noetherian. The ring \(k[x_1,x_2,\ldots]\), with countably many independent variables, is not: the ideals \((x_1,\ldots,x_n)\) strictly increase. Setting the first \(n\) variables to zero shows that \(x_{n+1}\) is not in the \(n\)-th ideal.

## 2. Polynomial rings and finite geometric descriptions

The following theorem allows finitely many coordinates to be added without losing control of ideals.

**Theorem 2.1 (Hilbert basis theorem).** If \(R\) is Noetherian, then \(R[t]\) is Noetherian. Every finite type \(R\)-algebra and every localization of \(R\) is therefore Noetherian.

**Proof.** Fix an ideal \(J\subseteq R[t]\). Let \(C\subseteq R\) consist of zero and the leading coefficients of nonzero elements of \(J\). It is an ideal. To add two leading coefficients, multiply the corresponding polynomials by powers of \(t\) until their degrees agree, then add. If the proposed leading coefficient cancels, the sum of the coefficients is zero, which is already in \(C\). Multiplication by \(r\in R\) has the same dichotomy: the leading coefficient is multiplied by \(r\), or becomes zero.

Choose generators \(a_1,\ldots,a_s\) of \(C\), realized by polynomials \(f_1,\ldots,f_s\in J\) with degrees \(d_i\). If \(C=0\), then \(J=0\) and there is nothing to prove. Otherwise put \(d=\max_i d_i\). Whenever \(f\in J\) has degree \(n\geq d\), write its leading coefficient as \(\sum r_i a_i\). Then

\[
f-\sum_i r_i t^{n-d_i}f_i
\]

has smaller degree. Repetition leaves a polynomial of degree less than \(d\).

The polynomials of degree less than \(d\) form a finite free \(R\)-module, with the zero module understood when \(d=0\). Its submodule \(J\cap R[t]_{<d}\) is finite by Proposition 1.2. Choose module generators \(g_1,\ldots,g_u\). The reduction just performed shows that \(f_i,g_j\) generate \(J\) as an ideal. This proves the theorem for one variable; induction handles finitely many variables. A finite type algebra is a quotient of such a polynomial ring, and quotients preserve the condition.

For localization, an ideal \(K\subseteq S^{-1}R\) is the extension of its contraction \(J\subseteq R\). Indeed, if \(a/s\in K\), then \(a/1=(s/1)(a/s)\in K\); the reverse inclusion is immediate. Extending finite generators of \(J\) gives finite generators of \(K\). This argument includes localization to the zero ring. \(\square\)

The theorem gives no corresponding assertion about arbitrary subrings. Inside \(k[x,y]\), consider

\[
B=k[x,xy,xy^2,xy^3,\ldots].
\]

Every nonconstant monomial of \(B\) has positive \(x\)-degree. Consequently the component of \(x\)-degree one in the ideal \((x,xy,\ldots,xy^n)\) is spanned over \(k\) by precisely those displayed monomials: multiplying them by nonconstant elements raises the \(x\)-degree. Thus \(xy^{n+1}\) does not belong to this ideal. The ideals strictly increase, so \(B\) is not Noetherian, although its ambient ring is.

**Proposition 2.2.** If \(R\) is Noetherian, then \(\operatorname{Spec}R\) is a Noetherian topological space, \(R\) has finitely many minimal primes, its nilradical is nilpotent, and every ideal \(I\) contains a power of \(\sqrt I\).

**Proof.** A descending chain of closed sets corresponds to an ascending chain of radical ideals, using the radical–closed-set correspondence in *Spectra of rings*. It stabilizes. The finite irreducible decomposition proved there then gives finitely many minimal primes.

The nilradical has finitely many generators \(z_1,\ldots,z_r\). Choose positive integers \(e_i\) with \(z_i^{e_i}=0\). Any product of

\[
1+\sum_{i=1}^r(e_i-1)
\]

generators contains at least \(e_i\) copies of some \(z_i\), so it is zero. Thus the nilradical is nilpotent. Apply the same argument in the Noetherian quotient \(R/I\). Its nilradical is \(\sqrt I/I\), so \((\sqrt I)^N\subseteq I\) for some positive \(N\). If the relevant ideal is zero, choose \(N=1\). \(\square\)

This is a uniform conclusion. In an arbitrary ring every individual nilpotent has some vanishing power; the Noetherian hypothesis makes one exponent work for the entire nilradical. Conversely, a Noetherian spectrum does not imply a Noetherian ring: the one-point square-zero example in *Spectra of rings* still applies.

## 3. Measuring a module by simple pieces

A nonzero module \(S\) is **simple** if its only submodules are zero and itself. If \(s\neq0\), simplicity makes \(Rs=S\), so \(S\cong R/\mathfrak m\) for a maximal ideal \(\mathfrak m\): the kernel of \(R\to S\) is maximal because the quotient has no proper nonzero ideals. Conversely each \(R/\mathfrak m\) is simple.

A **composition series** of \(M\) is a finite strict chain

\[
0=M_0\subsetneq M_1\subsetneq\cdots\subsetneq M_n=M
\]

whose successive quotients are simple. A module admitting one has **finite length**. We must prove that the number \(n\), and more strongly the simple factors, do not depend on the series.

**Lemma 3.1.** If \(M\) has a composition series of \(n\) steps, every submodule and quotient has a composition series of at most \(n\) steps. A proper submodule has a series of at most \(n-1\) steps.

**Proof.** For \(B\subseteq M\), intersect the given series with \(B\). The map

\[
(B\cap M_i)/(B\cap M_{i-1})\longrightarrow M_i/M_{i-1}
\]

is injective. Its image is either zero or the whole simple factor. Remove repetitions to obtain a composition series of \(B\). If none of the \(n\) steps vanished, induction gives \(M_i\subseteq B\) for every \(i\): surjectivity of the displayed map expresses each element of \(M_i\) as an element of \(B\cap M_i\) plus an element of \(M_{i-1}\). Hence \(B=M\). This proves the strict bound for proper submodules. For a quotient, take the images of the \(M_i\). Each new quotient is a quotient of a simple factor, so is zero or simple. \(\square\)

**Theorem 3.2 (Jordan–Hölder).** Any two composition series of a finite-length module have the same multiset of simple factors up to isomorphism. Their common number of steps is its length \(\ell_R(M)\).

**Proof.** Induct on the number \(n\) of steps in one chosen series. The zero module has the unique empty series. For \(n>0\), compare the penultimate submodules \(A\) and \(B\) of two series. Both are maximal proper submodules, since their quotients in \(M\) are simple. Lemma 3.1 puts every proper submodule within the induction range.

If \(A=B\), apply induction to the two series of \(A\), then append their identical last factor \(M/A\). If \(A\neq B\), maximality gives \(A+B=M\). Put \(C=A\cap B\). The maps into the opposite quotients give isomorphisms

\[
A/C\cong M/B,\qquad B/C\cong M/A.
\]

Choose a composition series of \(C\), supplied by Lemma 3.1. Appending \(A\) gives a series of \(A\) whose last factor is \(M/B\); appending \(B\) instead gives a series of \(B\) whose last factor is \(M/A\). Induction identifies the factors of each of these with those of the respective original series below \(A\) or \(B\). Thus both original series of \(M\) have the factors of \(C\), together with \(M/A\) and \(M/B\). The multisets agree, completing the induction. \(\square\)

**Theorem 3.3.** Finite length is equivalent to being both Noetherian and Artinian, where **Artinian** means that every descending chain of submodules stabilizes. In a short exact sequence, the middle module has finite length if and only if the two end modules do, and then

\[
\ell_R(M)=\ell_R(L)+\ell_R(N).
\]

**Proof.** First suppose \(M\) has finite length. Lemma 3.1 gives finite length to its submodules and quotients. For \(A\subsetneq B\subseteq M\), concatenate a series of \(A\) with the inverse images of a series of \(B/A\). This is a composition series of \(B\), so Jordan–Hölder gives

\[
\ell_R(B)=\ell_R(A)+\ell_R(B/A)>\ell_R(A).
\]

All these integers lie between zero and \(\ell_R(M)\). An ascending or descending chain can therefore have only finitely many strict steps. This proves both chain conditions.

Conversely, suppose both conditions hold. Every nonzero submodule has a maximal proper submodule, by the maximal condition for the nonempty family of its proper submodules. Starting with \(M\), repeatedly choose one. The descending chain condition makes the process terminate at zero; it cannot terminate at a nonzero module, where another choice is available. Reversing this chain gives a composition series.

If the middle module of the displayed exact sequence has finite length, Lemma 3.1 applies to the ends. If the ends have finite length, concatenate a series of \(L\) with the inverse images of a series of \(N\). The resulting series of \(M\) has exactly the sum of their lengths, proving both the equivalence and the formula. \(\square\)

For a vector space over \(k\), the simple modules are the one-dimensional spaces. A basis gives a composition series when the dimension is finite; conversely a composition series and dimension additivity show that its dimension is the length. If a module is annihilated by \(J\), its \(R\)-submodules and \(R/J\)-submodules are identical. Thus its length can be computed over either ring.

**Proposition 3.4.** Let \(M\) have finite length and let \(S\subseteq R\) be multiplicative. The length of \(S^{-1}M\) over \(S^{-1}R\) is the number of factors \(R/\mathfrak m\) in a composition series of \(M\) for which \(S\cap\mathfrak m=\varnothing\), counted with multiplicity. In particular it is at most \(\ell_R(M)\).

**Proof.** Localize a composition series, using exactness. If \(S\) meets \(\mathfrak m\), an element of \(S\) kills \(R/\mathfrak m\), so that factor becomes zero. Otherwise all denominators have nonzero images in the field \(R/\mathfrak m\). Localization leaves this field unchanged, and it is a simple module over \(S^{-1}R\) through the surjective map to that field. Remove the zero steps from the localized series and count the surviving simple factors. \(\square\)

For example, the chain \(0\subset(p^{n-1})\subset\cdots\subset(p)\subset\mathbb Z/p^n\) has \(n\) factors \(\mathbb F_p\). The ring \(\mathbb Z/p^n\) therefore has length \(n\). In contrast, \(\mathbb Z\) is not Artinian, as \((2)\supsetneq(4)\supsetneq(8)\supsetneq\cdots\). Finite generation alone gives no finite length.

## 4. What an Artinian ring looks like

We now prove the structure theorem without assuming in advance that an Artinian ring is Noetherian. This order matters: applying the finite-module version of Nakayama to an ideal before proving its finite generation would be circular.

**Lemma 4.1.** In an Artinian ring every prime is maximal, there are finitely many maximal ideals, and the Jacobson radical is nilpotent.

**Proof.** A quotient by a prime is an Artinian domain. For a nonzero element \(a\) in that domain, the chain \((a)\supseteq(a^2)\supseteq\cdots\) stabilizes. An equality \((a^n)=(a^{n+1})\) gives \(a^n=a^{n+1}b\); cancellation gives \(ab=1\). Thus the domain is a field.

If there were infinitely many distinct maximal ideals \(\mathfrak m_1,\mathfrak m_2,\ldots\), their finite intersections would form a strictly descending chain. To see strictness at step \(n+1\), choose \(a_i\in\mathfrak m_i\setminus\mathfrak m_{n+1}\) for \(i\leq n\). Their product lies in the first \(n\) ideals and not in the prime \(\mathfrak m_{n+1}\). This contradicts the descending chain condition.

Put \(J=\operatorname{Jac}(R)\). Its powers stabilize: choose \(n\geq1\) with \(J^n=J^{n+1}\). Set \(E=J^n\); then \(E^2=E\). Suppose \(E\neq0\). Among ideals \(K\) with \(EK\neq0\), choose a minimal one using the descending chain condition. There is \(a\in K\) with \(E(a)\neq0\), since ideal products consist of finite sums of products. Minimality gives \(K=(a)\).

Since \(E^2K=EK\neq0\), some \(x\in E\) satisfies \(E(xK)\neq0\). Minimality again gives \(xK=K\). Thus \(a=xra\) for some \(r\in R\). But \(x\in J\), so \(1-xr\) is a unit by the Jacobson-radical unit test from the preceding lesson. The equality \((1-xr)a=0\) forces \(a=0\), a contradiction. Consequently \(E=0\) and \(J\) is nilpotent. This argument did not assume that \(J\) or \(E\) was finite. \(\square\)

**Theorem 4.2.** For a ring \(R\), the following are equivalent:

1. \(R\) is Artinian.
2. \(R\) is Noetherian and every prime ideal is maximal.
3. \(R\) has finite length as an \(R\)-module.

Such a ring has finitely many maximal ideals \(\mathfrak m_1,\ldots,\mathfrak m_s\), and the natural map

\[
R\longrightarrow\prod_{i=1}^s R_{\mathfrak m_i}
\]

is an isomorphism. Each factor is Artinian local. For the zero ring the product is empty.

**Proof.** Suppose first that \(R\) is Artinian and nonzero. Lemma 4.1 gives finitely many maximal ideals and \(J^N=0\). Distinct maximal ideals are comaximal, so the Chinese remainder theorem identifies

\[
R/J\cong\prod_{i=1}^s R/\mathfrak m_i.
\]

For completeness, comaximal ideals \(A,B\) satisfy \(A\cap B=AB\): writing \(1=a+b\) expresses any \(z\in A\cap B\) as \(za+zb\in AB\). The map to \(R/A\times R/B\) is surjective because \(ub+va\) realizes the residues of \(u,v\). Induction gives the finite version used here.

Each \(J^i/J^{i+1}\) is an Artinian module over \(R/J\). The coordinate idempotents of the finite product split it into finitely many vector spaces over the residue fields. Each such vector space is Artinian and hence finite-dimensional. Indeed, an infinite-dimensional space has a basis containing distinct \(v_1,v_2,\ldots\); the spans of the basis with \(v_1,\ldots,v_n\) removed form a strictly descending chain. Thus each layer has finite length. The filtration by the finitely many powers of \(J\), and Theorem 3.3, give finite length to \(R\).

Finite length implies both chain conditions by Theorem 3.3, and an Artinian ring has only maximal primes by Lemma 4.1. This proves that the third condition implies the second and first. Conversely, suppose \(R\) is Noetherian and all primes are maximal. Every prime contains a minimal prime; since that minimal prime is already maximal, they agree. Proposition 2.2 makes their set finite and makes their intersection \(J=\sqrt{(0)}\) nilpotent. Again \(R/J\) is a finite product of fields. Now each \(J^i/J^{i+1}\) is finite, so its coordinate vector spaces are finite-dimensional. The same filtration proves finite length. This proves all equivalences.

To identify the product factors explicitly, the ideals \(\mathfrak m_i^N\) are pairwise comaximal. If \(a+b=1\), with \(a\in\mathfrak m_i\) and \(b\in\mathfrak m_j\), expand \((a+b)^{2N-1}\); each term lies in one of these two \(N\)-th powers. Therefore

\[
\bigcap_i\mathfrak m_i^N
=\prod_i\mathfrak m_i^N
=\left(\prod_i\mathfrak m_i\right)^N
=J^N=0,
\qquad
R\cong\prod_i R/\mathfrak m_i^N.
\]

The only prime of \(R/\mathfrak m_i^N\) is \(\mathfrak m_i/\mathfrak m_i^N\), since a prime containing the power contains \(\mathfrak m_i\). Thus this quotient is local and Artinian. Under the product decomposition, localization at \(\mathfrak m_i\) keeps the \(i\)-th factor: the \(i\)-th coordinate idempotent becomes one, the others become zero, and elements outside the unique maximal ideal of the remaining factor are already units. The projection is consequently the localization map, establishing the asserted natural isomorphism. The zero ring satisfies all three conditions directly. \(\square\)

An Artinian spectrum is therefore a finite discrete set. The residue field at each point need not equal the local ring. Nilpotent directions remain, and their successive layers are measured by length. For \(k[x,y]/(x^2,xy,y^3)\), for instance, the residue field is \(k\), while the classes of \(1,x,y,y^2\) give four independent layers in total. A composition series will make this precise in the exercises.

## 5. Intersecting a filtration with a submodule

Fix a Noetherian ring \(R\), an ideal \(I\), a finite module \(M\), and a submodule \(N\subseteq M\). The powers \(I^nM\) induce the filtration \(I^nM\cap N\) on \(N\). It need not be the same as \(I^nN\). For example, in \(R=k[t]\), take \(I=(t)\), \(M=R\), and \(N=(t^3)\). Then

\[
I^nM\cap N=(t^{\max(n,3)}),\qquad I^nN=(t^{n+3}).
\]

These are different, but the first filtration becomes predictable after degree three. Artin–Rees says that some finite degree works for every such inclusion.

**Theorem 5.1 (Artin–Rees).** Under the hypotheses just stated, there is an integer \(c\geq0\) such that for every \(n\geq c\),

\[
I^nM\cap N=I^{n-c}(I^cM\cap N).
\]

**Proof.** Introduce an indeterminate \(t\) which records the filtration degree. The **Rees algebra** and **Rees module** are

\[
\mathcal R=\bigoplus_{n\geq0} I^nt^n\subseteq R[t],
\qquad
\mathcal M=\bigoplus_{n\geq0} I^nM\,t^n\subseteq M[t].
\]

Here \(I^0=R\). Since \(I\) is finite, with generators \(a_1,\ldots,a_r\), the algebra \(\mathcal R\) is generated over \(R\) by \(a_1t,\ldots,a_rt\). Hilbert's theorem makes it Noetherian. Generators of \(M\), placed in degree zero, generate \(\mathcal M\) over \(\mathcal R\), so this module is Noetherian by Proposition 1.2.

The graded submodule

\[
\mathcal N=\bigoplus_{n\geq0}(I^nM\cap N)t^n
\]

is consequently finite. It has finitely many homogeneous generators: replace any finite generating set by all of its homogeneous components, which still belong to this graded submodule. Let their degrees be \(d_1,\ldots,d_v\), and put \(c=\max d_i\), choosing \(c=0\) if \(\mathcal N=0\).

For \(n\geq c\), the component of degree \(n\) is generated by products of these generators with elements of \(I^{n-d_i}\). If \(z_i\in I^{d_i}M\cap N\) is the coefficient of a degree-\(d_i\) generator, then

\[
I^{n-d_i}z_i
=I^{n-c}I^{c-d_i}z_i
\subseteq I^{n-c}(I^cM\cap N).
\]

This gives one inclusion. The other follows directly: multiplying \(I^cM\cap N\) by \(I^{n-c}\) lands both in \(I^nM\) and in \(N\). \(\square\)

The proof packages all degrees into one module, then uses finite generation once. The integer \(c\) depends on the inclusion and ideal; it is not a universal number for the ring. No freeness of \(M\), principal-ideal hypothesis, or local hypothesis was used.

One useful comparison follows immediately. For \(n\geq c\),

\[
I^nN\subseteq I^nM\cap N\subseteq I^{n-c}N.
\]

Thus the powers on \(N\) and the induced powers from \(M\) differ by a bounded shift. This is the mechanism that will later make completion preserve exact sequences of finite modules.

## 6. What can survive every power?

**Theorem 6.1 (Krull intersection).** Let \(R\) be Noetherian, \(I\subseteq R\) an ideal, and \(M\) finite. Put \(K=\bigcap_{n\geq0}I^nM\). Then \(IK=K\), and one element \(1+a\), with \(a\in I\), annihilates all of \(K\). More precisely,

\[
\bigcap_{n\geq0}I^nM
=\{x\in M:(1+a)x=0\text{ for some }a\in I\}.
\]

In particular:

- If \(I\subseteq\operatorname{Jac}(R)\), then \(K=0\).
- If \(R\) is a domain, \(I\) is proper, and \(M\) is torsion-free, then \(K=0\). This includes \(M=R\).

**Proof.** The submodule \(K\) is finite because \(M\) is Noetherian. Apply Artin–Rees to \(K\subseteq M\). Since \(K\subseteq I^nM\) for every \(n\), its formula at \(n=c+1\) reads

\[
K=I^{c+1}M\cap K=I(I^cM\cap K)=IK.
\]

The determinant form of Nakayama, which does not require \(I\) to lie in a radical, supplies an annihilator \(1+a\) of \(K\), with \(a\in I\). Explicitly, choose generators of \(K\), write each as an \(I\)-linear combination of them, and form the coefficient matrix \(A\). The adjugate of \(1-A\) shows that \(\det(1-A)\) annihilates each generator. Its determinant has the form \(1+a\), since all nonconstant determinant terms belong to \(I\). If \(K=0\), choose \(a=0\).

This proves containment in the set on the right. Conversely, if \((1+a)x=0\) for some \(a\in I\), then \(x=-ax\), hence \(x=(-a)^nx\in I^nM\) for every \(n\). This also proves that, although the right side allows an element-dependent \(a\), a single choice annihilates the entire intersection.

If \(I\subseteq\operatorname{Jac}(R)\), every \(1+a\) is a unit, so it kills only zero. If \(R\) is a domain and \(I\) is proper, \(1+a\neq0\), since otherwise \(-1\in I\). Torsion-freeness then again forces each killed element to be zero. \(\square\)

For a Noetherian local ring \((R,\mathfrak m)\) and a finite module,

\[
\bigcap_{n\geq0}\mathfrak m^nM=0.
\]

This assertion says that distinct elements can eventually be distinguished modulo a sufficiently high power of the maximal ideal. It does not say that every compatible sequence modulo those powers already comes from an element of \(M\); that is the separate issue of completeness.

The torsion-free hypothesis in the domain conclusion cannot be deleted. Over \(R=\mathbb Z\), the ideal \(I=(2)\) is proper, but for \(M=\mathbb Z/3\), multiplication by two is invertible. Thus \(I^nM=M\) for every \(n\), and the intersection is nonzero. The annihilator formula remains correct: \(1+2=3\) kills \(M\). A proper ideal in a domain suffices for the intersection of its powers *inside the ring*; it does not suffice for arbitrary finite modules.

### A smooth function invisible to every finite order

Let \(G\) be the ring of germs at zero of smooth real functions in one variable. It is local: a germ with nonzero value at zero has a smooth reciprocal near zero, while a germ with value zero cannot be a unit. Its maximal ideal is \(\mathfrak m=(x)\). Indeed, for a representative with \(f(0)=0\),

\[
f(x)=x\int_0^1 f'(sx)\,ds,
\]

and the integral is smooth in \(x\).

Define \(h(0)=0\) and \(h(x)=\exp(-1/x^2)\) for \(x\neq0\). For every nonnegative integer \(n\), the function \(h(x)/x^n\), extended by zero at zero, is smooth. Its derivatives away from zero are sums of powers of \(1/x\) times \(\exp(-1/x^2)\); all approach zero because \(u^d e^{-u^2}\to0\) as \(u\to\infty\), for every fixed \(d\). Applying this to each derivative proves smoothness and vanishing of all derivatives of the extension. Hence the nonzero germ \(h\) belongs to every \((x^n)=\mathfrak m^n\).

The germ is nonzero because its representative is positive at every sufficiently small nonzero point. Thus \(\bigcap\mathfrak m^n\neq0\), although \(G\) is local and \(\mathfrak m\) is principal. By Theorem 6.1, \(G\) cannot be Noetherian. The example identifies the failure: finite-order data need not determine a smooth germ, whereas the Noetherian local theorem forces separation by ideal powers.

## 7. Exercises

**Exercise 7.1 (first steps).** Let \(M\) be a Noetherian module and \(u:M\to M\) a surjective endomorphism. Prove injectivity using stabilization of the kernels of its iterates. Compare this argument with the finite-module determinant proof in the preceding lesson.

**Exercise 7.2 (first steps).** Give composition series for \(\mathbb Z/360\) and \(A=k[x,y]/(x^2,xy,y^3)\). Identify every factor and compute the lengths, over \(\mathbb Z\) and over \(A\) respectively.

**Exercise 7.3 (structural).** Prove that \(R[[t]]\) is Noetherian whenever \(R\) is Noetherian. Use the lowest nonzero coefficients of elements of an ideal to form a homogeneous ideal in \(R[T]\). Explain why your final expression is a finite sum of multiples of fixed generators; merely taking a limit of elements of the ideal would not suffice.

**Exercise 7.4 (arithmetic).** For a positive integer \(n\), use Theorem 4.2 to recover

\[
\mathbb Z/n\cong\prod_{p^e\parallel n}\mathbb Z/p^e.
\]

Identify its localizations, and compute its length. Include \(n=1\).

**Exercise 7.5 (structural).** In a Noetherian local ring \((R,\mathfrak m)\), prove that \(\mathfrak m=\mathfrak m^2\) forces \(\mathfrak m=0\), and that \(R\) is a field if and only if \(\mathfrak m/\mathfrak m^2=0\). Explain which finiteness hypothesis your proof uses.

**Exercise 7.6 (synthesis).** Let \(R=k\times k\) and \(I=k\times0\). Compute \(\bigcap_{n\geq0}I^n\). Find one \(a\in I\) such that \(1+a\) kills every element of this intersection, and determine why the zero-intersection conclusion for ideals in the Jacobson radical does not apply.

## 8. Solutions

**Solution 7.1.** The submodules \(\ker u^j\) ascend. Choose \(r\) with \(\ker u^r=\ker u^{r+1}\). If \(x\in\ker u\), surjectivity of \(u^r\) supplies \(y\) with \(u^ry=x\). Then \(u^{r+1}y=0\), so \(y\in\ker u^{r+1}=\ker u^r\), giving \(x=0\). The previous determinant argument proves the same conclusion for a finite module over any commutative ring. The present argument instead uses the ascending chain condition directly. Its hypotheses imply finite generation by Theorem 1.1, so it is consistent with that stronger result.

**Solution 7.2.** In \(\mathbb Z/360\), use the ideals generated by the following divisors, in this order:

\[
(360)=0\subset(180)\subset(90)\subset(45)\subset(15)\subset(5)\subset(1).
\]

If \(d'\mid d\mid360\), then \((d')/(d)\) in this chain is a cyclic group of order \(d/d'\): multiplication by \(d'\) identifies it with \(\mathbb Z/(d/d')\). The six factors are therefore \(\mathbb F_2,\mathbb F_2,\mathbb F_2,\mathbb F_3,\mathbb F_3,\mathbb F_5\), all simple \(\mathbb Z\)-modules. The length is six.

In \(A\), the monomials not divisible by \(x^2,xy,y^3\) are \(1,x,y,y^2\). They form a basis: the ideal generated by the three prohibited monomials is precisely the span of their monomial multiples, so no relation among these four remaining monomials lies in it. The ideal \(\mathfrak m=(x,y)\) is nilpotent and \(A/\mathfrak m=k\); an element with nonzero constant coefficient is a unit by a finite geometric series in its nilpotent part. Thus \(A\) is local. The chain

\[
0\subset(y^2)\subset(y)\subset(x,y)\subset A
\]

has successive one-dimensional \(k\)-vector spaces, each annihilated by \(\mathfrak m\). Each factor is the simple \(A\)-module \(k\). The length over \(A\) is four, agreeing with the vector-space dimension here because every simple factor is this residue field.

**Solution 7.3.** Set \(B=R[[t]]\), and let \(J\subseteq B\) be an ideal. For each \(d\geq0\), let \(E_d\subseteq R\) consist of the coefficients of \(t^d\) in elements of \(J\cap t^dB\). These are ideals, and multiplication by \(t\) shows \(E_d\subseteq E_{d+1}\). Consequently

\[
H=\bigoplus_{d\geq0}E_dT^d\subseteq R[T]
\]

is a homogeneous ideal. Hilbert's theorem gives finite homogeneous generators \(a_iT^{d_i}\), \(1\leq i\leq s\): start with finite generators of \(H\) and take their homogeneous components. For each choose \(f_i\in J\cap t^{d_i}B\) with coefficient \(a_i\) in degree \(d_i\). Zero generators may be discarded. If \(H=0\), all coefficients of every nonzero element of \(J\) would have to vanish at its first nonzero degree, so \(J=0\).

We claim \(J=(f_1,\ldots,f_s)\). Take \(f\in J\). Cancel its coefficients in increasing degree. If a residual \(g\in J\cap t^dB\) has coefficient \(a\) in degree \(d\), the homogeneous generation of \(H\) gives

\[
aT^d=\sum_{d_i\leq d}r_iT^{d-d_i}a_iT^{d_i},\qquad r_i\in R.
\]

Subtract \(\sum r_it^{d-d_i}f_i\). The result still lies in \(J\) and now belongs to \(t^{d+1}B\). If the coefficient was already zero, no subtraction is needed. Repeating degree by degree constructs, for each fixed \(i\), a series \(q_i\in R[[t]]\) from the coefficients added to that generator. At degree \(d\), the increment to \(q_i\) has degree \(d-d_i\); these degrees tend to infinity. Thus each coefficient of \(q_i\) is well defined. For any fixed degree \(m\), the cancellation process eventually makes the residual zero through degree \(m\). It follows coefficient by coefficient that

\[
f=\sum_{i=1}^s q_i f_i.
\]

This is a finite sum in the ideal generated by the \(f_i\). We have proved finite generation without assuming beforehand that arbitrary ideals are closed under limits. Repeating the one-variable result also proves that \(R[[t_1,\ldots,t_r]]\) is Noetherian for finite \(r\), since iterated formal series in finitely many variables are the same coefficient arrays.

**Solution 7.4.** For \(n>1\), the finite ring \(A=\mathbb Z/n\) is Artinian: it has only finitely many subsets and hence finitely many ideals. Its maximal ideals are \((p)\) for the primes dividing \(n\), by the correspondence with maximal ideals of \(\mathbb Z\) containing \((n)\). Let \(p^e\parallel n\) and write \(n=p^e m\), \(p\nmid m\). The natural map \(A\to\mathbb Z/p^e\) sends every element outside \((p)\) to a unit, so it induces a map from \(A_{(p)}\). In that localization \(m\) is a unit and \(p^em=0\), whence \(p^e=0\). There is therefore a map \(\mathbb Z/p^e\to A_{(p)}\). The composites fix the integer classes; uniqueness of localization makes them inverse. Thus \(A_{(p)}\cong\mathbb Z/p^e\). Theorem 4.2 gives the claimed product through these natural reduction maps.

Each local factor has length \(e\), by its filtration by powers of \(p\). The coordinate idempotents decompose the product as a direct sum of modules, so additivity gives \(\ell_A(A)=\sum e\). The same length is obtained over \(\mathbb Z\), because restriction along the surjection \(\mathbb Z\to A\) does not change submodules. If \(n=1\), the ring is zero, the product over the empty prime set is the zero ring, and the length is zero.

**Solution 7.5.** Since \(R\) is Noetherian, its ideal \(\mathfrak m\) is finite. The equality \(\mathfrak m=\mathfrak m^2\) says that \(\mathfrak m\mathfrak m=\mathfrak m\). Nakayama applies to the module \(\mathfrak m\) and the ideal \(\mathfrak m\subseteq\operatorname{Jac}(R)\), and gives \(\mathfrak m=0\). Conversely, \(\mathfrak m/\mathfrak m^2=0\) is exactly that equality. A local ring with maximal ideal zero is a field: any nonzero element is outside the maximal ideal and hence a unit. A field has maximal ideal zero and therefore zero quotient \(\mathfrak m/\mathfrak m^2\). The proof needs finite generation of \(\mathfrak m\); Noetherianness guarantees it. It does not require a completeness hypothesis.

**Solution 7.6.** The ideal \(I\) satisfies \(I^2=I\), since it is generated by the idempotent \((1,0)\). Hence every positive power is \(I\), and the intersection, including the zeroth power \(R\), is \(I\neq0\). Take \(a=(-1,0)\). Then \(1+a=(0,1)\), which kills \(I\). The maximal ideals are \(k\times0\) and \(0\times k\), so their intersection, the Jacobson radical, is zero. Thus \(I\) is not contained in it. The annihilator formula predicts the nonzero intersection exactly; it does not require \(1+a\) to be a unit.

## What this lesson does not prove

Every finiteness, length, Artinian structure, Artin–Rees, and Krull-intersection assertion used in this lesson has been proved here, including the formal-power-series assertion in Solution 7.3. We import the preceding lesson's exactness of localization, local unit test, and Nakayama theorem. We have compared ideal-power filtrations but have not yet constructed completion or proved its exactness; those belong to *Completion and formal neighborhoods*.

## References

- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Sections 3.6, 6.5, and 13.9. [Author's public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).
- Timothy J. Ford, *Commutative Algebra*, version of 23 September 2026, Chapter 4, Sections 1 and 4 on chain conditions, composition series and commutative noetherian and artinian rings; Chapter 5, Section 2.1 on the Hilbert Basis Theorem; Chapter 6, Sections 2.2 and 3.2 on the Artin–Rees and Krull Intersection Theorems. Section 3.2 states the domain conclusion and the finitely generated module conclusion separately. [Author's version](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf).
- The Stacks project authors, *The Stacks project*, Commutative Algebra: [Tag 00FN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-permanence), [Tag 0306](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-power-series), [Tag 00IV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-length-additive), [Tag 00IZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-length-localize), [Tag 00J8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-artinian-radical-nilpotent), [Tag 00KJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-dimension-zero-ring), [Tag 00IN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Artin-Rees), and [Tag 00IQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-intersection-powers-ideal-module).
