# Krull dimension and Noether normalization

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Original text: public domain (CC0). The example in Theorem 7.1 follows Nagata's construction as presented in the Stacks Project, cited at the end.*

Dimension counts successive specializations. For an algebra of finite type over a field, it also counts independent parameters. Noether normalization connects these descriptions by finding a polynomial subalgebra over which the original algebra is finite. Choosing that subalgebra to respect ideals will let us measure both the dimension of a closed subset and its codimension.

Rings are commutative with identity, and primes are proper. The zero ring and the empty space have dimension \(-\infty\). A finite algebra is finite as a module; finite type means finitely generated as an algebra. The field \(k\) is arbitrary. We use lying over, incomparability, going down over normal domains, normality of polynomial rings, and equality of dimensions under integral inclusions from [Integral extensions: lying over, going up and going down](integral-extensions-lying-over-going-up-and-going-down.md), Theorems 3.2–3.3, 4.3 and 5.1 and Proposition 2.3. We use Zariski's lemma from [The Nullstellensatz and Jacobson rings](the-nullstellensatz-and-jacobson-rings.md), Theorem 1.3. The prime–irreducible-closed-set dictionary and finite irreducible decomposition come from [Spectra of rings](spectra-of-rings.md), Theorem 4.1, Lemma 4.2 and Theorem 4.3. Hilbert basis from [Noetherian and Artinian rings](noetherian-and-artinian-rings.md), Theorem 2.1, makes finite-type algebras Noetherian. Lemma 1.3 supplies existence and exchange of transcendence bases [Stacks, Tag 030F]. No result about depth or regular local rings is needed.

## 1. Chains, height and codimension

A strict chain \(\mathfrak p_0\subsetneq\cdots\subsetneq\mathfrak p_n\) has **length** \(n\), counting inclusions. Its one-prime version has length zero. Define \(\dim R\) as the supremum of these lengths. The **height** \(\operatorname{ht}_R\mathfrak p\) is the supremum of lengths of chains ending at \(\mathfrak p\). Localization identifies primes of \(R_{\mathfrak p}\) with primes contained in \(\mathfrak p\), preserving strict inclusions. Every chain there can be extended to its maximal ideal. Consequently

\[
\operatorname{ht}_R\mathfrak p=\dim R_{\mathfrak p}.
\tag{1}
\]

**Proposition 1.1.** For any ring, with the supremum of an empty set interpreted as \(-\infty\),

\[
\dim R=\sup_{\mathfrak m\text{ maximal}}\dim R_{\mathfrak m}
=\sup_{\mathfrak m\text{ maximal}}\operatorname{ht}_R\mathfrak m.
\tag{2}
\]

**Proof.** A chain contained in a maximal ideal is a chain of \(R\), giving the inequality from right to left. Conversely, the top prime of every finite chain is contained in a maximal ideal. Appending that maximal ideal if necessary gives a chain whose length is at least the original length. Taking suprema and using (1) proves (2), even when those lengths are unbounded. For the zero ring all three indexing sets are empty. \(\square\)

For a topological space, Krull dimension is defined by strict chains of nonempty irreducible closed subsets, again counting inclusions. An irreducible closed subset \(Y\subset X\) has codimension equal to the supremum of lengths of such chains **starting** at \(Y\) and increasing in \(X\). Codimension of a point means codimension of its closure.

**Proposition 1.2.** We have \(\dim\operatorname{Spec}R=\dim R\) and
\(\operatorname{codim}(V(\mathfrak p),\operatorname{Spec}R)=\operatorname{ht}_R\mathfrak p\).

**Proof.** Every nonempty irreducible closed subset is uniquely \(V(\mathfrak p)\), and \(V(\mathfrak q)\subsetneq V(\mathfrak p)\) means \(\mathfrak p\subsetneq\mathfrak q\). Reversing a chain gives the dimension equality. A chain starting at \(V(\mathfrak p)\) reverses to a chain ending at \(\mathfrak p\), giving the codimension equality. \(\square\)

If \(X=Z_1\cup\cdots\cup Z_s\) is a finite closed cover, then
\(\dim X=\max_i\dim Z_i\). Indeed, the largest irreducible set in any chain is contained in one \(Z_i\): an irreducible set cannot be a finite union of proper closed subsets. The whole chain then lies there. The reverse inequality follows by viewing chains in a closed subset as chains in \(X\). In particular, for a nonzero Noetherian ring with minimal primes \(\mathfrak q_i\),

\[
\dim R=\max_i\dim(R/\mathfrak q_i).
\tag{3}
\]

Nilpotents do not change the spectrum or its dimension. Heights and dimensions may nevertheless differ between components. We will prove the appropriate formula before identifying codimension with a difference of dimensions.

**Lemma 1.3 (transcendence bases).** Every field extension \(L/k\) has a maximal algebraically independent subset, \(L\) is algebraic over the field it generates, and any two such bases have the same cardinality.

**Proof.** The union of a chain of independent subsets is independent, since a polynomial relation uses finitely many elements. Zorn's lemma gives a maximal set \(B\). If \(a\in L\) were transcendental over \(k(B)\), adjoining it would preserve independence, so \(L/k(B)\) is algebraic.

For the exchange step put \(F=k(E)\), and suppose \(a\) is transcendental over \(F\) but algebraic over \(F(B)\), with \(B\) finite and independent over \(F\). Choose a minimal nonempty \(B_0\subset B\) over which \(a\) is algebraic. For \(b\in B_0\), minimality makes \(a\) transcendental over \(F(B_0\setminus\{b\})\). Clear denominators in an equation for \(a\) over \(F(B_0)\), and regard the resulting polynomial as a polynomial in \(b\). Its coefficients cannot all vanish after substituting \(a\), because that transcendence makes the coefficient evaluation injective. Thus \(b\) is algebraic over \(F(a,B_0\setminus\{b\})\), and \((B_0\setminus\{b\})\cup\{a\}\) is independent over \(F\).

We use the following elementary fact to append the remaining elements of \(B\): independence over a field persists over an algebraic extension of that field inside the ambient extension. Indeed, a polynomial relation has coefficients in a finite subextension \(L_0/F_0\). Multiplication by its nonzero polynomial on the free \(F_0[X]\)-module \(L_0[X]\) has nonzero determinant: it is injective, and remains so over \(F_0(X)\). Its adjugate shows that this determinant belongs to the ideal generated by the polynomial in \(L_0[X]\). Evaluation of the supposed relation would therefore give a nonzero polynomial relation over \(F_0\), a contradiction. Apply this fact to \(F(B_0,a)/F(B_0)\). The set \(B\setminus B_0\) remains independent over \(F(B_0,a)\), hence over \(F(a,B_0\setminus\{b\})\). Consequently replacing \(b\) by \(a\) in all of \(B\) gives an independent set over \(F\), over whose generated field \(F(B)\) is algebraic. Successive exchanges, keeping the previously inserted independent elements in \(E\), show that any independent finite set has size at most a finite algebraic spanning set. A dependent spanning set can first be reduced to a maximal independent subset.

For two arbitrary bases \(B,C\), assign to each \(b\in B\) a finite subset \(C_b\subset C\) over which it is algebraic. If \(C\) is finite, the preceding bound applied to every finite subset of \(B\) gives \(|B|\le|C|\). If \(C\) is infinite, for each finite \(E\subset C\) there are at most \(|E|\) elements of \(B\) algebraic over \(k(E)\), again by that bound. There are \(|C|\) finite subsets of an infinite set \(C\); their union therefore gives \(|B|\le|C|\). Reversing the roles proves equality, with the empty-base case included. This defines transcendence degree without restricting the size of an extension. \(\square\)

## 2. Making one equation monic

**Lemma 2.1.** For a nonconstant \(f\in k[X_1,\ldots,X_n]\), there are polynomial coordinates \(Z_1,\ldots,Z_{n-1},X_n\) in which \(f\), as a polynomial in \(X_n\), has positive degree and nonzero constant leading coefficient. Moreover,

\[
k[Z_1,\ldots,Z_{n-1},f]\ \subset\ k[X_1,\ldots,X_n]
\tag{4}
\]

is a finite inclusion of polynomial rings in \(n\) variables.

**Proof.** Choose an integer \(e\geq2\) larger than every exponent occurring in any monomial of \(f\), and put

\[
Z_i=X_i-X_n^{e^i}\quad(1\leq i<n).
\tag{5}
\]

This change has inverse \(X_i=Z_i+X_n^{e^i}\), so the displayed elements are polynomial coordinates. A monomial \(X_1^{a_1}\cdots X_n^{a_n}\) contributes a unique highest \(X_n\)-power, with exponent

\[
a_n+a_1e+a_2e^2+\cdots+a_{n-1}e^{n-1}.
\]

The base-\(e\) expansion makes these exponents distinct for the different monomials of \(f\). Every term involving a \(Z_i\) has smaller \(X_n\)-degree than that monomial's highest term. Thus exactly one monomial supplies the highest term overall, whose coefficient is its nonzero coefficient in \(k\). Since \(f\) is nonconstant, that highest degree \(D\) is positive.

Write \(f=cX_n^D+\sum_{j<D}b_j(Z)X_n^j\), where \(c\in k^\times\). The equation

\[
X_n^D+c^{-1}\sum_{j<D}b_j(Z)X_n^j-c^{-1}f=0
\tag{6}
\]

makes \(X_n\) integral over the ring in (4); its powers of degree less than \(D\) generate the whole polynomial ring over that subring. Finally, no nonzero polynomial in \(Z_1,\ldots,Z_{n-1},f\) vanishes. Regard it as a polynomial in its last argument: after substitution its term of highest last-argument degree has strictly highest \(X_n\)-degree and nonzero leading coefficient in the domain \(k[Z]\). This proves algebraic independence and the inclusion assertion. The proof uses no choice of scalars from an infinite field. \(\square\)

## 3. Normalization that respects ideals

The following stronger form will prove ordinary normalization and the height formula together.

**Theorem 3.1 (normalization adapted to ideals).** Let \(P=k[X_1,\ldots,X_n]\), and let
\(I_0\subset\cdots\subset I_s\subsetneq P\) be a finite chain of ideals. There is a polynomial subring \(C=k[U_1,\ldots,U_n]\subset P\) such that \(P\) is finite over \(C\) and, for integers \(0\leq h_0\leq\cdots\leq h_s\leq n\),

\[
I_j\cap C=(U_1,\ldots,U_{h_j}).
\tag{7}
\]

The ideals need not be prime or radical.

**Proof.** Induct on \(n\). For \(n=0\), every proper ideal of \(k\) is zero. If all the ideals are zero, take \(C=P\). Otherwise let \(I_a\) be the first nonzero ideal and choose \(0\ne f\in I_a\). It is nonconstant, since every ideal in the chain is proper. Lemma 2.1 makes \(P\) finite over the polynomial ring
\(C_0=k[Z_1,\ldots,Z_{n-1},f]\).

For \(j\geq a\), the contraction \(I_j\cap C_0\) contains \(f\). Its image \(J_j\) in \(C_0/(f)=k[Z_1,\ldots,Z_{n-1}]\) is proper: otherwise the contraction would contain one. Apply induction to this chain of \(J_j\). Obtain algebraically independent \(V_1,\ldots,V_{n-1}\) in \(k[Z]\), a finite inclusion \(k[V]\subset k[Z]\), and
\(J_j\cap k[V]=(V_1,\ldots,V_{r_j})\).

Set \(C=k[V_1,\ldots,V_{n-1},f]\). These \(n\) elements are algebraically independent because \(f\) is transcendental over \(k[Z]\) and the \(V_i\) are independent there. The inclusion \(C\subset C_0\) is finite: a finite generating list for \(k[Z]\) over \(k[V]\) also generates after adjoining the independent variable \(f\). Finiteness composes, so \(P\) is finite over \(C\).

Because \(f\in I_j\), membership of a polynomial in \(V,f\) in \(I_j\) is equivalent to membership of its constant term in \(f\) in \(J_j\). Therefore
\(I_j\cap C=(f,V_1,\ldots,V_{r_j})\) for \(j\geq a\). The earlier ideals are zero and contract to zero. Order the parameters as \(U_1=f,U_2=V_1,\ldots,U_n=V_{n-1}\). This gives (7), with \(h_j=0\) before \(a\) and \(h_j=1+r_j\) thereafter. \(\square\)

**Corollary 3.2 (Noether normalization).** Every nonzero finite-type \(k\)-algebra \(S\) contains a polynomial ring \(A=k[y_1,\ldots,y_d]\) over which it is finite. Given any finite chain of proper ideals of \(S\), this normalization can be chosen so that their contractions to \(A\) are ideals generated by initial lists of its variables.

**Proof.** Present \(S=P/I\) and apply Theorem 3.1 to \(I\) together with the inverse images of the chosen ideals. If \(I\cap C=(U_1,\ldots,U_h)\), the induced map

\[
C/(I\cap C)=k[U_{h+1},\ldots,U_n]\longrightarrow S
\]

is injective by the definition of contraction. Images of a finite \(C\)-module generating list for \(P\) generate \(S\) over this quotient. Taking \(y_i=\overline{U}_{h+i}\) proves both assertions. In particular, their number may be zero, giving a finite algebra over \(k\). \(\square\)

Geometrically this gives a finite surjection \(\operatorname{Spec}S\to\mathbb A_k^d\), by lying over. It does not say that \(S\) is normal, or that the extension is flat. The term “normalization” here refers to the choice of parameters.

## 4. Parameters measure dimension and height

For a finite-type domain \(B\), write \(d(B)=\operatorname{trdeg}_k\operatorname{Frac}(B)\). A maximal algebraically independent subcollection of algebra generators is a transcendence basis of its fraction field. Indeed, each remaining generator is algebraic over the field generated by that subcollection. Exchange of bases makes this number independent of the choice.

**Lemma 4.1 (a strict specialization loses a parameter).** For \(0\ne\mathfrak p\in\operatorname{Spec}B\),
\(d(B)\geq d(B/\mathfrak p)+1\).

**Proof.** Choose algebraically independent \(\bar b_1,\ldots,\bar b_r\) in \(B/\mathfrak p\) that form a transcendence basis of its fraction field; choose lifts \(b_i\) and \(0\ne a\in\mathfrak p\). Suppose a nonzero polynomial relation among \(a,b_1,\ldots,b_r\) exists. Write it as \(\sum_j a^j g_j(b)=0\), and let \(j_0\) be the least index with nonzero polynomial \(g_{j_0}\). Divide by \(a^{j_0}\) in the domain, and reduce modulo \(\mathfrak p\). This gives \(g_{j_0}(\bar b)=0\), contradicting independence. Thus the lifts together with \(a\) are algebraically independent. \(\square\)

Apply this lemma successively to the domains \(B/\mathfrak p_i\) along a chain. It follows that every chain in \(B\) has length at most \(d(B)\), and a chain from \(\mathfrak p\) to \(\mathfrak q\) has length at most \(d(B/\mathfrak p)-d(B/\mathfrak q)\).

**Theorem 4.2 (dimension and transcendence degree).** A polynomial ring in \(d\) variables over \(k\) has dimension \(d\). For every finite-type domain \(S\),

\[
\dim S=\operatorname{trdeg}_k\operatorname{Frac}(S).
\tag{8}
\]

**Proof.** The lemma bounds polynomial-ring chains by \(d\). The coordinate chain
\((0)\subsetneq(y_1)\subsetneq\cdots\subsetneq(y_1,\ldots,y_d)\)
has length \(d\), since all its quotients are polynomial domains. Now normalize \(S\) over \(A=k[y_1,\ldots,y_r]\). The finite integral inclusion gives \(\dim S=\dim A=r\), by the integral-extension lesson. Its fraction field is finite algebraic over \(k(y_1,\ldots,y_r)\). To check this directly, localize the finite module at all nonzero elements of \(A\): it becomes a finite-dimensional domain over that field, hence a field, containing \(S\) and therefore equal to \(\operatorname{Frac}(S)\). Thus the transcendence degree is \(r\). \(\square\)

For an arbitrary nonzero finite-type algebra, normalization and equality of dimensions under integral inclusions still give \(\dim S=d\), where \(d\) is the number of normalization parameters. Formula (3) gives another description: the largest transcendence degree of a component's function field.

**Theorem 4.3 (height formula).** If \(S\) is a finite-type \(k\)-domain and \(\mathfrak p\) is prime, then

\[
\operatorname{ht}_S\mathfrak p+\dim(S/\mathfrak p)=\dim S.
\tag{9}
\]

**Proof.** Choose the normalization in Corollary 3.2 adapted to \(\mathfrak p\). Write
\(A=k[y_1,\ldots,y_d]\subset S\) and \(\mathfrak p\cap A=(y_1,\ldots,y_t)=\mathfrak r\). The latter prime has height \(t\): the first \(t\) coordinate ideals give the lower bound, and Lemma 4.1 bounds any chain ending there by
\(d(A)-d(A/\mathfrak r)=t\).

Contraction of a chain ending at \(\mathfrak p\) preserves all its strict inclusions by incomparability. Therefore \(\operatorname{ht}_S\mathfrak p\leq\operatorname{ht}_A\mathfrak r\). Conversely \(A\) is normal, so going down lifts any chain ending at \(\mathfrak r\) to a chain ending at the specified prime \(\mathfrak p\). Distinct contractions ensure that the lifted inclusions are strict. Hence \(\operatorname{ht}_S\mathfrak p=t\).

The quotient inclusion \(A/\mathfrak r\subset S/\mathfrak p\) is finite and integral, so \(\dim(S/\mathfrak p)=d-t\). Also \(\dim S=d\) by Theorem 4.2. Adding proves (9). \(\square\)

**Corollary 4.4.** Every maximal ideal \(\mathfrak m\) of such a domain has
\(\dim S_{\mathfrak m}=\operatorname{ht}_S\mathfrak m=\dim S\).

**Proof.** The field \(S/\mathfrak m\) is finite over \(k\) by Zariski's lemma, and therefore has transcendence degree and dimension zero. Apply (9) and (1). \(\square\)

## 5. Saturated chains and catenarity

A chain between specified primes is **saturated** if no prime can be inserted between adjacent members. A ring is **catenary** if, between any two comparable primes, saturated chains have a common finite length and every chain can be extended to one.

**Theorem 5.1.** Every finite-type \(k\)-algebra is catenary. Between \(\mathfrak p\subset\mathfrak q\), the common length is

\[
\operatorname{trdeg}_k\kappa(\mathfrak p)
-\operatorname{trdeg}_k\kappa(\mathfrak q).
\tag{10}
\]

Every maximal chain in a finite-type \(k\)-domain has length \(\dim S\).

**Proof.** Work in the domain \(S/\mathfrak p\); primes in the interval correspond exactly to primes between zero and \(\mathfrak q/\mathfrak p\). If \(\mathfrak a\subsetneq\mathfrak b\) are adjacent primes in a saturated chain, the prime \(\mathfrak b/\mathfrak a\) in the domain \(S/\mathfrak a\) has height one. There is its length-one chain from zero, and a longer chain would supply an intermediate prime. The height formula in that domain gives

\[
\dim(S/\mathfrak a)-\dim(S/\mathfrak b)=1.
\]

Sum these differences along the chain, and use (8) and
\(\kappa(\mathfrak a)=\operatorname{Frac}(S/\mathfrak a)\). This proves (10). Any starting chain can be extended by inserting primes whenever possible: Lemma 4.1 bounds all lengths in this interval, so the insertion process must terminate. This also prevents infinite chains in the interval.

For a chain maximal under insertion and endpoint extension in a domain, the first prime is zero and the last is maximal; otherwise either endpoint could be extended. Its bottom quotient has dimension \(\dim S\), its top quotient has dimension zero by Zariski's lemma, and its steps each lose one dimension. Its length is therefore \(\dim S\). \(\square\)

In particular, for a finite-type domain and \(\mathfrak p\subset\mathfrak q\),
\(\operatorname{ht}_{S/\mathfrak p}(\mathfrak q/\mathfrak p)
=\operatorname{ht}_S\mathfrak q-\operatorname{ht}_S\mathfrak p\).
Indeed (9) computes both sides as the difference of the two quotient dimensions. Catenarity controls intervals even when different components of the entire algebra have different dimensions.

## 6. Dimension at a point

For \(x\in X\), define \(\dim_xX\) to be the minimum of \(\dim U\) over open neighborhoods \(U\) of \(x\). For our finite-dimensional spaces this minimum exists. This quantity measures dimensions of components near the point. The dimension of its local ring instead measures chains of generalizations ending there.

**Theorem 6.1.** For any finite-type \(k\)-algebra \(S\), any prime \(\mathfrak p\), and its point \(x\),

\[
\dim_x\operatorname{Spec}S
=\dim S_{\mathfrak p}+\operatorname{trdeg}_k\kappa(\mathfrak p).
\tag{11}
\]

**Proof.** Let the finitely many components through \(x\) be
\(V(\mathfrak q_i)\), for minimal primes \(\mathfrak q_i\subset\mathfrak p\), and put \(d_i=\dim(S/\mathfrak q_i)\). Every neighborhood \(U\) of \(x\) meets each such component in a nonempty open subset. That subset has dimension \(d_i\). To verify this, it contains a basic open \(D(\bar f)\) of the component with \(\bar f\ne0\); its algebra \((S/\mathfrak q_i)_f\) is a finite-type domain with the same fraction field, so (8) gives dimension \(d_i\). Open subsets cannot have larger dimension than the ambient space: closing a chain of irreducible closed subsets in the ambient space preserves strict inclusions, because intersecting the closures back with the open recovers the chain. Thus \(\dim U\geq\max_i d_i\).

Remove the union of all components not containing \(x\). Its complement is an open neighborhood of \(x\). Its finite closed cover by the intersections with the remaining components has dimension \(\max_i d_i\), by the finite-cover argument in Section 1. Hence \(\dim_x X=\max_i d_i\).

The minimal primes of \(S_{\mathfrak p}\) are exactly the \(\mathfrak q_iS_{\mathfrak p}\). The localization version of (3), followed by (1), gives

\[
\dim S_{\mathfrak p}
=\max_i\operatorname{ht}_{S/\mathfrak q_i}(\mathfrak p/\mathfrak q_i).
\]

Apply (9) in each domain \(S/\mathfrak q_i\). Its quotient by \(\mathfrak p/\mathfrak q_i\) is \(S/\mathfrak p\), whose dimension is
\(e=\operatorname{trdeg}_k\kappa(\mathfrak p)\), independently of \(i\). Thus the last maximum is \(\max_i(d_i-e)=\dim_xX-e\), proving (11). \(\square\)

At a closed point the residue transcendence degree is zero, so the two dimensions agree. At the generic point of a component of dimension \(d\), the local ring has dimension zero while the pointwise dimension is \(d\). If all components have dimension \(d\), the proof also gives \(\operatorname{ht}\mathfrak p+\dim(S/\mathfrak p)=d\). Equidimensionality is a hypothesis that makes this global difference formula possible.

## 7. Computations and limits of the formulas

**An arithmetic surface.** The prime ideals of \(\mathbb Z\) give \(\dim\mathbb Z=1\). For \(\mathbb Z[X]\), primes with contraction zero correspond to primes of \(\mathbb Q[X]\); primes over \((p)\) correspond to primes of \(\mathbb F_p[X]\). Each fibre has chains of length at most one. A chain of length three would therefore have to pass from a nonzero horizontal prime to \((p)\) and then to a larger prime over \((p)\). That middle inclusion is impossible. Any nonzero element of a horizontal prime can be divided by its integer content inside that prime, since its contraction is zero; the resulting primitive polynomial cannot belong to \((p)\). No other contraction pattern permits three steps. The chain
\((0)\subsetneq(p)\subsetneq(p,X)\) has length two, so \(\dim\mathbb Z[X]=2\).

Over \(R=\mathbb Z_{(p)}\), the domain \(R[X]\) has maximal ideals of different heights. The ideal \((p,X)\) has height two by that same chain and localization of the preceding bound. The ideal \((pX-1)\) is maximal because its quotient is \(R[1/p]=\mathbb Q\). Its contraction to \(R\) is zero, so all primes below it lie in the \(\mathbb Q[X]\) fibre, where it is a nonzero height-one prime. Thus the equality of every maximal height with the dimension needs the finite-type-over-a-field hypothesis.

**A plane with a line attached.** Put \(S=k[x,y,z]/(xz,yz)\). A prime containing both products either contains \(z\) or contains \(x,y\). These two incomparable prime ideals are therefore exactly the minimal primes. Their quotients are \(k[x,y]\) and \(k[z]\), so the components have dimensions two and one and \(\dim S=2\). Both generic primes have height zero. At the generic point of the line, (11) reads \(1=0+1\). At the origin, both components occur, and it reads \(2=2+0\). At the rational point \((x,y,z-1)\), only the line occurs and it reads \(1=1+0\).

**A finite projection of a hyperbola.** In \(S=k[x,y]/(xy-1)=k[x,x^{-1}]\), put \(s=x+y\). Then
\(x^2-sx+1=0\) and \(y=s-x\), so \(1,x\) generate \(S\) over \(k[s]\). This map is injective: for any nonzero polynomial \(g\) of degree \(r\), the Laurent polynomial \(g(x+x^{-1})\) has nonzero coefficient of \(x^r\), contributed only by its leading term. This normalization works in every characteristic. Projection to \(x\) alone is not finite, as shown by the integral field criterion after localizing at \((x)\).

**Theorem 7.1 (Nagata's infinite-dimensional example).** There is a Noetherian domain with maximal ideals of unbounded finite height.

**Construction and proof.** Let \(P=k[x_1,x_2,\ldots]\). Partition the variables into finite blocks \(E_i=\{x_{2^{i-1}},\ldots,x_{2^i-1}\}\), and let \(\mathfrak p_i=(E_i)\). Each is prime, because its quotient is a polynomial domain on the remaining variables. Set
\[
S=P\setminus\bigcup_{i\ge1}\mathfrak p_i,
\qquad A=S^{-1}P.
\tag{12a}
\]
The set \(S\) is multiplicative, as the complement of a union of primes. A nonzero polynomial belongs to only finitely many \(\mathfrak p_i\): for every block absent from its finite variable set, its image in the quotient is the same nonzero polynomial.

We first prove that every prime disjoint from \(S\) is contained in some \(\mathfrak p_i\). The zero prime is. For a nonzero such prime \(\mathfrak q\), choose \(0\ne f\in\mathfrak q\). Let \(F=\{i:f\in\mathfrak p_i\}\), finite. If \(F\) were empty, \(f\in S\) would already be a contradiction. Suppose \(\mathfrak q\) is not contained in any \(\mathfrak p_i\) for \(i\in F\). Finite prime avoidance gives \(g\in\mathfrak q\) outside all those primes. Choose a variable \(x\) in a block \(E_j\) absent from both \(f\) and \(g\), with \(j\notin F\), and put \(h=f+xg\in\mathfrak q\). For \(i\in F\), its image is \(xg\ne0\) modulo \(\mathfrak p_i\). For \(i=j\), its image is \(f\ne0\). For every other \(i\notin F\), its image has nonzero constant coefficient \(f\) as a polynomial in the surviving independent variable \(x\); it cannot vanish. Thus \(h\in S\), again a contradiction. This proves the claim. The finite prime-avoidance argument used here is the one in *Associated primes and primary decomposition*, Solution 8.5; equivalently its elementary ideal proof can be used before the rest of that lesson.

The maximal ideals of \(A\) are consequently exactly \(\mathfrak m_i=\mathfrak p_iA\). Each \(\mathfrak p_i\) is disjoint from \(S\), and no two of them contain each other; the preceding claim rules out a larger disjoint prime. Moreover
\[
A_{\mathfrak m_i}=P_{\mathfrak p_i}
\cong K_i[E_i]_{(E_i)},
\tag{12b}
\]
where \(K_i\) is the rational-function field in all variables outside \(E_i\). Indeed every nonzero polynomial in the outside variables becomes invertible, and the remaining elements inverted are precisely those outside the block maximal ideal. This finite-variable local polynomial ring is Noetherian of dimension \(|E_i|=2^{i-1}\), by the polynomial dimension calculation above. The block size, rather than \(2^i\), is the height in this indexing.

Finally let \(I\subset A\) be a nonzero ideal, and choose \(0\ne a\in I\). It belongs to only finitely many maximal ideals, by the same finite-variable observation applied to its numerator. At each of these finitely many ideals the localized ideal \(I_{\mathfrak m_i}\) has finitely many generators. Choose their numerators from \(I\), and let \(I_0\) be generated by all these choices and \(a\). At the other maximal ideals \(a\) is a unit, so \((I_0)_{\mathfrak m}=I_{\mathfrak m}=A_{\mathfrak m}\). At the selected ideals equality holds by construction. Local detection applied to \(I/I_0\) gives \(I=I_0\). The zero ideal is finitely generated as well. Thus \(A\) is Noetherian, while (12b) gives unbounded heights and hence infinite dimension. This proves the warning in its full form. \(\square\)

## 8. Exercises

**Exercise 8.1 (easy: components).** Compute the minimal primes, components and dimension of \(k[x,y,z]/(xy,xz)\).

**Exercise 8.2 (easy: finite parameters).** Give and verify Noether normalizations of \(k[x,y]/(xy-1)\) and \(k[x,y,z]/(xy-z^2)\), over an arbitrary field.

**Exercise 8.3 (medium: products).** Prove
\(\dim(S\otimes_kT)=\dim S+\dim T\) for finite-type \(k\)-algebras. Explain this through the function fields of components, without assuming that the tensor product of two domains is a domain. Use \(-\infty+d=-\infty\), including \(d=-\infty\), for the zero-ring cases.

**Exercise 8.4 (medium: dimension zero).** Prove that a finite-type \(k\)-algebra is Artinian if and only if it is finite-dimensional over \(k\).

**Exercise 8.5 (hard: a failed global height formula).** In \(S=k[x,y,z]/(xz,yz)\), find a prime for which \(\operatorname{ht}\mathfrak p+\dim(S/\mathfrak p)\ne\dim S\). Then prove the equality for every finite-type \(k\)-domain by choosing a normalization adapted to the prime.

**Exercise 8.6 (hard: three dimensions at a point).** For that same plane-and-line algebra, compute \(\dim_xX\), \(\dim S_{\mathfrak p}\), and \(\operatorname{trdeg}_k\kappa(\mathfrak p)\) at the two generic points, the origin, and \((x,y,z-1)\). Explain why a constant global dimension cannot replace \(\dim_xX\) in (11).

## 9. Solutions

**Solution 8.1.** A prime containing \(xy,xz\) either contains \(x\), or contains both \(y,z\). The primes \((x)\) and \((y,z)\) are incomparable, so are precisely the minimal primes over the defining ideal. They give a plane with coordinate algebra \(k[y,z]\) and a line with coordinate algebra \(k[x]\). Their dimensions are two and one by Theorem 4.2; the finite closed-cover formula gives total dimension two. The generic points have height zero because they are minimal.

**Solution 8.2.** For the hyperbola, use \(s=x+y\). The monic equation, expression \(y=s-x\), and Laurent highest-power calculation in Section 7 prove finiteness and injectivity of \(k[s]\to S\). For the quadric, use \(k[x,y]\to k[x,y,z]/(z^2-xy)\). Monic division in \(z\) gives a unique representative \(a(x,y)+b(x,y)z\). Uniqueness follows because a nonzero multiple of the monic polynomial \(z^2-xy\) has \(z\)-degree at least two. Thus the map is injective and the target is free over \(k[x,y]\) with basis \(1,z\), hence finite. These arguments work also in characteristic two. The normalization has two parameters, so this algebra has dimension two.

**Solution 8.3.** First let \(U,V\) be finite-type domains of dimensions \(d,e\), and choose normalizations \(A=k[a_1,\ldots,a_d]\subset U\), \(B=k[b_1,\ldots,b_e]\subset V\). Tensoring injections of vector spaces preserves injections, so
\(D=A\otimes_kB\subset H=U\otimes_kV\) is an inclusion. Products of finite module generators make \(H\) finite over the polynomial ring \(D\) in \(d+e\) variables. Equality of dimensions under integral inclusions already yields \(\dim H=d+e\).

Here is the component interpretation. Let \(F=\operatorname{Frac}A\), \(G=\operatorname{Frac}B\). Torsion-freeness of the domains embeds \(U\) into its finite-dimensional localization \(U\otimes_AF\), and a choice of vector-space basis identifies that localization with \(F^r\). Likewise \(V\hookrightarrow G^s\). Tensor over \(k\) to embed \(H\) into \((F\otimes_kG)^{rs}\). The ring \(F\otimes_kG\) is the localization of \(D\) by the nonzero elements of \(A\) and of \(B\); it is a domain, since \(D\) is a polynomial domain. Therefore \(H\) is torsion-free over \(D\).

The Noetherian ring \(H\) has every minimal prime associated to itself, by [Associated primes and primary decomposition](associated-primes-and-primary-decomposition.md), Theorem 3.2. A nonzero element of \(D\) acts injectively on \(H\), so cannot lie in such a prime: an associated prime is an annihilator of a nonzero element. Thus each minimal \(\mathfrak r\) of \(H\) contracts to zero in \(D\). The finite inclusion \(D\subset H/\mathfrak r\) makes its fraction field algebraic over \(\operatorname{Frac}D\). Each component consequently has function-field transcendence degree \(d+e\), as claimed. A tensor product may still have several components; for instance \(\mathbb C\otimes_{\mathbb R}\mathbb C\simeq\mathbb C\times\mathbb C\).

For general nonzero \(S,T\), let \(\mathfrak p_i,\mathfrak q_j\) be their finite sets of minimal primes. Every prime of \(S\otimes T\) contracts to primes containing some \(\mathfrak p_i\) and \(\mathfrak q_j\). Thus the closed subsets with algebras
\((S/\mathfrak p_i)\otimes_k(T/\mathfrak q_j)\) form a finite cover of its spectrum. The domain calculation and (3) give

\[
\dim(S\otimes_kT)
=\max_{i,j}\bigl(\dim(S/\mathfrak p_i)+\dim(T/\mathfrak q_j)\bigr)
=\dim S+\dim T.
\]

If either algebra is zero, its tensor product is zero and the stipulated convention gives the same equality.

**Solution 8.4.** A finite-dimensional algebra is Artinian because any strict descending chain of ideals strictly decreases vector-space dimension. Conversely, suppose \(S\ne0\) is Artinian. Its primes are maximal by [Noetherian and Artinian rings](noetherian-and-artinian-rings.md), Theorem 4.2, so \(\dim S=0\). Normalize it over a polynomial ring in \(d\) variables. The finite integral inclusion gives \(0=\dim S=d\); hence this polynomial ring is just \(k\), and the finite module assertion says precisely that \(S\) is finite-dimensional over \(k\). The zero algebra satisfies both conditions.

**Solution 8.5.** Take the minimal prime \(\mathfrak p=(x,y)\) in the plane-and-line algebra. Its height is zero, and its quotient \(k[z]\) has dimension one, whereas \(\dim S=2\). This violates the proposed equality. For a finite-type domain, choose \(A=k[y_1,\ldots,y_d]\subset S\) finite with contraction \(\mathfrak r=(y_1,\ldots,y_t)\). Its coordinate chain and the transcendence-degree drop bound give \(\operatorname{ht}_A\mathfrak r=t\). Incomparability contracts chains ending at \(\mathfrak p\) strictly; going down over the normal domain \(A\) lifts chains ending at \(\mathfrak r\) to that specified \(\mathfrak p\). Thus \(\operatorname{ht}_S\mathfrak p=t\). The finite quotient inclusion gives \(\dim(S/\mathfrak p)=\dim(A/\mathfrak r)=d-t\), and the original inclusion gives \(\dim S=d\). Their sum proves the formula with all its hypotheses.

**Solution 8.6.** At \((z)\), only the plane component contains the point; its function field is \(k(x,y)\). At \((x,y)\), only the line component contains the point; its function field is \(k(z)\). Both primes are minimal, so both local dimensions are zero. At the origin \((x,y,z)\), both components occur, the pointwise dimension is their maximum two, and the residue field is \(k\). At \((x,y,z-1)\), the plane does not occur because \(z\) is not in that prime; the pointwise dimension is one and the residue field is \(k\). Theorem 6.1 now gives the following values, with explicit height-two chain \((z)\subsetneq(z,x)\subsetneq(z,x,y)\) at the origin and height-one chain \((x,y)\subsetneq(x,y,z-1)\) at the other closed point.

| Prime | Pointwise dimension | Local-ring dimension | Residue transcendence degree |
|---|---:|---:|---:|
| \((z)\) | 2 | 0 | 2 |
| \((x,y)\) | 1 | 0 | 1 |
| \((x,y,z)\) | 2 | 2 | 0 |
| \((x,y,z-1)\) | 1 | 1 | 0 |

The global dimension is two everywhere as a single invariant of the algebra. Substituting it on the left of (11) would give a false equation at both listed points lying only on the line.

## Proof dependencies

Nagata's example is constructed and verified in Theorem 7.1. The field-basis argument in Section 1 supplies the transcendence-basis facts. Integral extensions, the spectrum dictionary, Zariski's lemma, Artinian primes and associated primes are used at their indicated internal locators. General Noetherian local dimension theory follows in *Dimension theory of Noetherian local rings*.

## References

- The Stacks project authors, *The Stacks project*, Commutative Algebra: dimension and height [Tag 00KE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-Krull), [Tag 00KF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-height), [Tag 00KG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-height); monic substitution and normalization [Tag 051N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-helper-polynomial), [Tag 00OX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-one-relation), [Tag 00OY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noether-normalization), [Tag 051P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-refined-Noether-normalization).
- The same work, dimension formulas [Tag 00P0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-prime-polynomial-ring), [Tag 00P1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-dimension-at-a-point-finite-type-field); topological definitions [Section 0054](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topology.html#topology-section-krull-dimension), [Tag 02I3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topology.html#topology-definition-codimension); transcendence bases [Tag 030F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-transcendence-degree); Nagata warning [Section 02JC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/examples.html#examples-section-Noetherian-infinite-dimension). The links use the AI Integrated Stacks Project English reader described in the course introduction.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Sections 12.1–12.2, especially 12.2.4–5, 12.2.7 and 12.2.9–11. [Author's public draft](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).

## Sources

The infinite-dimensional Noetherian example in Theorem 7.1 is Nagata's construction, following its presentation by the Stacks Project authors in the examples chapter ([source at the pinned AI Integrated Stacks Project revision](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/examples.tex#L1161)). The argument above supplies the prime-containment and finite-generation verifications and uses the actual block size in its local dimension calculation.

## Licence

The text of this lesson is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). The Stacks Project, cited above for the arguments this lesson follows, is distributed by its authors under the GNU FDL 1.2 or later.
