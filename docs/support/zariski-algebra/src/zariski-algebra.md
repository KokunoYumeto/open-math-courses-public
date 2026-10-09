# Algebra for Zariski's Main Theorem and field extension

*Written and self-checked by GPT-6.1 Sol (OpenAI), Codex, Ultra, October 2026. CC0-1.0.*

These algebraic results apply over arbitrary commutative rings unless a field or finite-type hypothesis is stated. A finite algebra is finite as a module over its base; an algebra of finite presentation has finitely many algebra generators and defining relations.

## Integral closure and localization

Let \(A\to B\) be a ring map, let \(T\subset A\) be multiplicatively closed, and let \(B^{\mathrm{int}}\) consist of the elements integral over the image of \(A\). Then the integral closure of \(T^{-1}A\) inside \(T^{-1}B\) is

\[
T^{-1}B^{\mathrm{int}}.
\]

The full proof is The theorem on formal functions, Appendix Z, Lemma Z.1. It clears the coefficient denominators in a monic equation and absorbs the extra annihilating denominator into the integral numerator. The argument includes zero divisors and noninjective base maps.

## Coefficients in the radical of a conductor

Suppose \(\varphi:R[X]\to S\) is finite. Put \(A=\varphi(R)\), \(x=\varphi(X)\), \(C=A[x]\), and

\[
J=\{g\in S:gS\subset C\}.
\]

Assume \(A\) is integrally closed in \(S\). For \(u\in S\) and \(p=\sum_i a_iX^i\in R[X]\),

\[
u\varphi(p)\in\sqrt J
\quad\Longrightarrow\quad
u\varphi(a_i)\in\sqrt J\quad\text{for every }i.
\]

The complete proof and its leading-coefficient lemmas are The theorem on formal functions, Appendix Z, Situation Z.4 and Lemma Z.6, using Lemmas Z.1–Z.5 in that appendix. Neither Noetherianity nor reducedness is assumed.

## Strong transcendence and quasi-finite points

For an inclusion \(R\subset S\), an element \(x\in S\) is **strongly transcendental over \(R\)** if

\[
u\sum_i a_ix^i=0
\quad\Longrightarrow\quad ua_i=0\quad\text{for every }i
\]

for all \(u\in S\) and finite lists \(a_i\in R\). If \(R\) and \(S\) are reduced and \(S\) is finite over \(R[x]\), then \(R\to S\) is quasi-finite at no prime of \(S\).

The full proof is The theorem on formal functions, Appendix Z, Lemma Z.11, with Definition Z.7 and Lemmas Z.8–Z.10. The domain case uses the polynomial-normality proof in Lemma 0.1 of the same lesson. The proof passes through one minimal prime and does not require finitely many minimal primes or a Noetherian base.

## Finite presentation across a finite algebra

Throughout, rings are commutative with identity, ring homomorphisms preserve the identity, and modules have unital actions. A module is **finite** if a finite set generates it. An \(A\)-module \(N\) is **finitely presented** if there is an exact sequence

\[
A^p\longrightarrow A^q\longrightarrow N\longrightarrow0
\]

with \(p,q\) finite nonnegative integers. A ring map \(R\to S\) is **finite** when \(S\) is finite as an \(R\)-module. It is **of finite presentation** when, as an \(R\)-algebra,

\[
S\cong R[T_1,\ldots,T_d]/(f_1,\ldots,f_c)
\]

for finite \(d,c\). These are two different requirements on a ring map.

**Theorem.** Suppose that \(R\to S\) is finite and of finite presentation. For every \(S\)-module \(M\),

\[
M\text{ is finitely presented over }R
\quad\Longleftrightarrow\quad
M\text{ is finitely presented over }S.
\]

There is no Noetherian hypothesis. The result is [Stacks Project, Tag 0564](https://stacks.math.columbia.edu/tag/0564).

Finite presentation concerns both a generating set and its relations. On passing from \(S\) to \(R\), we will express the relations using finitely many \(R\)-module generators of \(S\). The essential preliminary point is that the algebra presentation of \(S\), together with its module finiteness, supplies a finite **module** presentation of \(S\).

### Controlling kernels and adding relations

**Lemma 1.** Let \(A\) be any ring.

1. If \(N\) is finitely presented, every surjection \(A^r\to N\) with finite \(r\) has finite kernel.
2. If \(D\to N\) is surjective, \(D\) is finite and \(N\) is finitely presented, its kernel is finite.
3. If \(E\) is finitely presented and \(U\subseteq E\) is finite, then \(E/U\) is finitely presented.
4. A finite direct sum of finitely presented modules is finitely presented.

**Proof.** For the first assertion, take a surjection \(p:A^q\to N\) whose kernel \(L\) has generators \(\ell_1,\ldots,\ell_b\), and let \(v:A^r\to N\) be the chosen surjection. Lift the images of the standard bases to obtain maps

\[
\alpha:A^q\to A^r,\qquad \beta:A^r\to A^q,
\qquad v\alpha=p,\qquad p\beta=v.
\]

Both \(\alpha(\ell_i)\) and \((1-\alpha\beta)e_j\) lie in \(\ker v\). If \(z\in\ker v\), then \(\beta z\in L\), and

\[
z=\alpha(\beta z)+(1-\alpha\beta)z.
\]

The first summand belongs to the span of the \(\alpha(\ell_i)\); the second belongs to the span of the finitely many \((1-\alpha\beta)e_j\). This proves the assertion for any chosen finite free surjection, rather than only for the presentation used to define \(N\).

For the second assertion, choose a finite free module \(F\) surjecting onto \(D\). The composite \(F\to N\) has finite kernel by the first assertion. Its image in \(D\) is exactly \(\ker(D\to N)\): a lift to \(F\) of an element in that kernel already maps to zero in \(N\). Images of a finite generating set therefore generate the required kernel.

For the third assertion, choose \(A^q\to E\) with finite kernel \(L\), choose generators \(u_1,\ldots,u_b\) of \(U\), and choose lifts \(\widetilde u_i\in A^q\). The kernel of \(A^q\to E/U\) is

\[
L+A\widetilde u_1+\cdots+A\widetilde u_b.
\]

Indeed, subtracting a lifted expression for the image in \(U\) leaves an element of \(L\). This gives finitely many relations for \(E/U\). Finally, taking a direct sum of finitely many presentation sequences proves the fourth assertion. \(\square\)

The kernel and quotient assertions are the parts of [Stacks Project, Tag 0519](https://stacks.math.columbia.edu/tag/0519) needed here. Their proofs show why an arbitrary submodule of a finite module need not be assumed finite.

### Turning the algebra presentation into a module presentation

**Lemma 2.** If \(R\to S\) is finite and of finite presentation, then \(S\) is finitely presented as an \(R\)-module.

**Proof.** The zero ring cases cause no difficulty: if \(R=0\), then \(S=0\), and if \(S=0\), it is already the zero \(R\)-module. Hence assume both rings are nonzero.

We first produce polynomial equations with leading coefficient \(1\). Choose \(R\)-module generators \(w_1,\ldots,w_h\) of \(S\), adding \(w_1=1\) if necessary. Thus \(h\geq1\). For \(s\in S\), express multiplication by \(s\) on these generators as

\[
sw_j=\sum_{k=1}^h a_{jk}w_k,\qquad a_{jk}\in R.
\]

With \(A=(a_{jk})\) and \(w\) the column of generators, this says \((sI-A)w=0\) over \(S\). Multiplication by the adjugate gives

\[
\det(sI-A)w=0.
\]

The adjugate identity holds over a commutative ring by the cofactor expansion of the determinant: diagonal entries of the product are the determinant, and off-diagonal entries are determinants with a repeated row or column. In particular no inverse or division is involved. Since \(w_1=1\), the monic polynomial

\[
p_s(X)=\det(XI-A)\in R[X]
\]

satisfies \(p_s(s)=0\). This is the finite-module integrality argument underlying [Stacks Project, Tag 052I](https://stacks.math.columbia.edu/tag/052I).

Now use a finite algebra presentation

\[
P=R[T_1,\ldots,T_d],\qquad
S=P/I,\qquad I=(f_1,\ldots,f_c).
\]

For the image \(s_i\) of \(T_i\), choose the monic polynomial just constructed, and call it \(p_i\), of degree \(e_i\geq1\). Because \(p_i(s_i)=0\), all the \(p_i(T_i)\) belong to \(I\). Consequently there is a surjection

\[
B=P/(p_1(T_1),\ldots,p_d(T_d))\longrightarrow S.
\]

The \(R\)-module \(B\) is finite free. Here are the normal-form details. For any nonzero commutative coefficient ring \(C\) and monic polynomial \(p\in C[X]\) of degree \(e\geq1\), repeatedly subtracting a suitable multiple of \(p\) removes the highest term of a polynomial of degree at least \(e\). This terminates with a polynomial of degree less than \(e\). The remainder is unique: if \(q\neq0\), the leading coefficient of \(qp\) equals that of \(q\), so \(qp\) has degree \(\deg q+e\) and cannot be a nonzero polynomial of smaller degree. Therefore

\[
C[X]/(p)\cong C\oplus CX\oplus\cdots\oplus CX^{e-1}
\]

as a \(C\)-module. Apply this successively to \(T_1,\ldots,T_d\). At each step the next \(p_i\) remains monic over the preceding quotient, so uniqueness and spanning are both preserved. It follows that \(B\) has the \(R\)-basis

\[
\mathcal B=\{T_1^{a_1}\cdots T_d^{a_d}:0\leq a_i<e_i\}.
\]

When \(d=0\), this set consists of the empty product \(1\) and \(B=R\). In all cases its cardinality is the finite integer \(D=\prod_i e_i\), with empty product \(D=1\).

The kernel \(J\) of \(B\to S\) is the ideal generated by the images \(\overline f_1,\ldots,\overline f_c\). As an \(R\)-module it is generated by the finite set

\[
\{b\overline f_j:b\in\mathcal B,\ 1\leq j\leq c\}.
\]

To check this, write each coefficient in an ideal expression \(\sum_j b_j\overline f_j\) in the basis \(\mathcal B\); the resulting coefficients lie in \(R\). Thus \(S=B/J\) is a quotient of a finite free \(R\)-module by a finite \(R\)-submodule, and Lemma 1 gives its finite presentation. More explicitly, the coordinate vectors of these \(Dc\) elements in \(\mathcal B\) give a presentation

\[
R^{Dc}\longrightarrow R^D\longrightarrow S\longrightarrow0.
\]

The first map need not be injective; a finite presentation imposes no such requirement. \(\square\)

### Encoding an action by finitely many relations

**Lemma 3.** For a ring map \(R\to S\) of finite type, an \(S\)-module that is finitely presented over \(R\) is finitely presented over \(S\).

**Proof.** Take \(R\)-module generators \(m_1,\ldots,m_q\) and a finite presentation of \(M\) on those generators. Let \(u_1,\ldots,u_d\) generate \(S\) as an \(R\)-algebra. The \(S\)-module

\[
E=S\otimes_R M
\]

has a finite presentation on \(1\otimes m_1,\ldots,1\otimes m_q\) with the same finite list of relations, now allowing coefficients in \(S\). To verify this without a flatness assumption, write the original presentation matrix as \(C:R^p\to R^q\), and let \(Q=S^q/\operatorname{im}(C_S)\). The rule

\[
\left(s,\sum_j r_jm_j\right)\longmapsto
\text{the class of }(sr_1,\ldots,sr_q)\text{ in }Q
\]

is well defined: changing the chosen vector \((r_j)\) changes it by a vector in \(\operatorname{im}C\), which maps into \(\operatorname{im}(C_S)\). It is an \(R\)-balanced bilinear map, hence gives \(E\to Q\). In the other direction, \((s_j)\mapsto\sum_j s_j\otimes m_j\) kills \(\operatorname{im}(C_S)\) and gives \(Q\to E\). The two maps are inverse, proving the claimed presentation.

The action defines a surjective \(S\)-linear map

\[
\mu:E\longrightarrow M,\qquad s\otimes m\longmapsto sm.
\]

Let \(H\) be the \(S\)-submodule generated by

\[
u_i\otimes m_j-1\otimes u_i m_j,
\qquad 1\leq i\leq d,\quad 1\leq j\leq q.
\]

Each generator maps to zero under \(\mu\). These are all the relations needed to recover the given action. Indeed, expressing \(m\) in the \(R\)-generators \(m_j\) shows

\[
u_i\otimes m\equiv1\otimes u_i m\pmod H
\]

for every \(m\in M\). Multiplying this congruence by an arbitrary element of \(S\) allows one factor \(u_i\) at a time to move from the first tensor factor to its action on the second. Induction on the number of factors proves

\[
u_{i_1}\cdots u_{i_k}\otimes m
\equiv1\otimes(u_{i_1}\cdots u_{i_k}m)\pmod H.
\]

Every element of \(S\) is an \(R\)-linear combination of such monomials, including the empty monomial. Hence every \(z\in E\) satisfies \(z\equiv1\otimes\mu(z)\pmod H\). In particular \(\ker\mu=H\). Lemma 1 applied over \(S\) shows that \(M\cong E/H\) is finitely presented. The same argument covers \(d=0\) or \(q=0\), when the displayed list of action relations is empty. \(\square\)

This is the assertion of [Stacks Project, Tag 0561](https://stacks.math.columbia.edu/tag/0561).

### Proof of the theorem

If \(M\) is finitely presented over \(R\), then it is finitely presented over \(S\) by Lemma 3: a finite ring map is of finite type, because any finite \(R\)-module generating set of \(S\) also generates its \(R\)-algebra.

For the converse, take a finite \(S\)-module presentation

\[
S^b\longrightarrow S^q\longrightarrow M\longrightarrow0
\]

and let \(K\) be the image of the first map. Choose \(R\)-module generators \(t_1,\ldots,t_a\) of \(S\). The vectors \(t_i e_j\) generate \(S^b\) over \(R\), so their images generate \(K\) over \(R\). Lemma 2 makes \(S\), and then Lemma 1 makes \(S^q\), finitely presented over \(R\). Finally, \(M=S^q/K\) is finitely presented over \(R\) by the quotient assertion of Lemma 1. \(\square\)

Empty generating and relation lists are allowed throughout. Thus the proof includes \(M=0\), presentations with \(q=0\), an algebra presentation with no variables, and presentations with no relations. Its finiteness assertions come from the displayed generating sets, so they remain valid over rings with infinitely generated ideals.

### Why both conditions on the algebra matter

Let \(k\) be a field and \(R=k[X_1,X_2,\ldots]\). The ideal \(I=(X_1,X_2,\ldots)\) is not finitely generated. For if a finite list generated it, all polynomials on that list would involve variables from some finite set \(X_1,\ldots,X_N\), and would have zero constant term. The ideal they generate would then lie in \((X_1,\ldots,X_N)\); setting those variables equal to zero shows that \(X_{N+1}\) cannot lie there. Now \(S=R/I=k\) is a finite \(R\)-algebra and \(M=S\) is free of rank one over \(S\). It is not finitely presented over \(R\), because Lemma 1 would make the kernel \(I\) of \(R\to M\) finite. The module finiteness condition on the algebra alone therefore does not suffice.

Conversely, \(k\to k[T]\) is a ring map of finite presentation, and \(k[T]\) is free of rank one over itself. As a \(k\)-module it is not finite: any finite list of polynomials has bounded degree, while \(T^n\) occurs for every \(n\). Thus the ring presentation condition alone does not suffice either.


## Dimension near a point after extension of the ground field

**Theorem.** Let \(k\) be a field, let \(S\) be a finite-type \(k\)-algebra, and let \(K/k\) be any field extension. Put
\[
X=\operatorname{Spec}S,\qquad S_K=K\otimes_k S,\qquad X_K=\operatorname{Spec}S_K.
\]
If \(\mathfrak q_K\in\operatorname{Spec}S_K\) contracts to \(\mathfrak q\in\operatorname{Spec}S\), write \(x_K\) and \(x\) for their points. Then
\[
\boxed{\dim_{x_K}X_K=\dim_xX.}
\]
Here \(\dim_xX\) is the infimum of \(\dim U\) over open neighborhoods \(U\) of \(x\). For an affine scheme of finite type over a field, it is the largest dimension of an irreducible component containing \(x\). The local-ring dimension \(\dim S_{\mathfrak q}\) is a different quantity. For example, the generic point of an affine line has pointwise dimension one and local-ring dimension zero.

The assertion permits nilpotents, components of different dimensions, nonclosed points, and extensions of infinite transcendence degree. No separability hypothesis is imposed. The existence of \(\mathfrak q\) already excludes the zero ring.

We give a proof using irreducible components, then a second proof using a polynomial presentation. Both arguments preserve the chosen point upstairs throughout.

### Algebra used below

Three earlier CC0 lessons provide complete proofs of the following facts:

* AG-CA-03, Theorem 2.1 and Proposition 2.2: finite-type algebras over a field and their localizations are Noetherian; a Noetherian spectrum has finitely many irreducible components, corresponding to its minimal primes.
* AG-CA-05, Theorem 5.1: an integral inclusion preserves Krull dimension. Its proof contracts prime chains using incomparability and lifts prime chains using lying over and going up, all proved in that lesson's Section 3. Finite algebras are integral by Theorems 1.1–1.2 in Section 1.
* AG-CA-09, Corollary 3.2 and Theorem 4.2: a finite-type domain \(D/k\) is finite over an embedded polynomial algebra \(k[t_1,\ldots,t_d]\), with
  \(d=\dim D=\operatorname{trdeg}_k\operatorname{Frac}D\). The polynomial algebra in \(d\) variables has dimension \(d\).

The facts about scalar extension and the chosen point are proved next.

**Lemma A (flatness and primes below a selected prime).** The map \(S\to K\otimes_k S\) is faithfully flat. More generally, if \(A\to B\) is flat, \(Q\in\operatorname{Spec}B\) contracts to \(q\), and \(p\subset q\) is prime, there is a prime \(P\subset Q\) contracting to \(p\).

**Proof.** For an \(S\)-module \(M\), the map
\[
(K\otimes_k S)\otimes_S M\longrightarrow K\otimes_k M,
\qquad (a\otimes s)\otimes m\longmapsto a\otimes sm
\]
is an isomorphism; its inverse sends \(a\otimes m\) to \((a\otimes1)\otimes m\). Every exact sequence of \(k\)-vector spaces splits after choosing bases, so tensoring with \(K\) preserves exactness. Also \(K\otimes_k M\neq0\) whenever \(M\neq0\): choosing a \(k\)-basis of \(M\) identifies the tensor product with a direct sum of copies of the nonzero field \(K\). This proves faithful flatness.

For the general assertion, set \(R=A_q\) and \(T=B_Q\). The induced map \(R\to T\) is flat and local. To check flatness explicitly, an exact sequence of \(R\)-modules is an exact sequence of \(A\)-modules; tensoring first with \(B\) and then localizing at \(B\setminus Q\) preserves exactness. Localization is exact because a fraction is zero precisely when a further denominator annihilates its numerator.

This local flat map is faithfully flat. Indeed, every proper ideal \(I\subset R\) lies in the maximal ideal \(qR\), and \(IT\) lies in the proper maximal ideal \(QT\). Given a nonzero \(R\)-module \(N\), choose \(0\neq n\in N\). The cyclic submodule \(Rn\cong R/I\) has proper annihilator \(I\). Flatness embeds its tensor product \(T/IT\neq0\) in \(T\otimes_R N\), proving the claim.

Consequently \(T\otimes_R\kappa(pR)\) is nonzero. It has a prime ideal: a maximal proper ideal exists by Zorn's lemma. The fibre algebra is
\[
(R\setminus pR)^{-1}(T/pT).
\]
A prime of this algebra pulls back to a prime of \(T\) whose contraction to \(R\) is \(pR\). Contracting further to \(B\) gives \(P\subset Q\), with contraction \(p\) in \(A\). This proves the required prime lifting. \(\square\)

**Lemma B (components of an extended domain).** Suppose \(D\) is a finite-type \(k\)-domain of dimension \(d\). Every minimal prime \(P\) of \(C=K\otimes_k D\) satisfies
\[
\dim(C/P)=d.
\]

**Proof.** Choose a normalization \(R=k[t_1,\ldots,t_d]\subset D\) as in the earlier lesson, and let \(F=\operatorname{Frac}R\). Since \(D\) is a domain, its map to \(F\otimes_R D\) is injective. This is a finite-dimensional \(F\)-vector space, so a choice of basis gives an \(R\)-linear injection
\[
D\hookrightarrow F^m
\]
for some finite \(m\). Tensoring this injection over \(k\) with \(K\) gives an injection of \(R_K=K[t_1,\ldots,t_d]\)-modules
\[
C\hookrightarrow (K\otimes_k F)^m.
\]
Writing \(T=R\setminus\{0\}\), the algebra \(K\otimes_k F\) is \(T^{-1}R_K\). Each member of \(T\) remains a nonzero polynomial after extending coefficients, so this localization is a domain. Every nonzero element of \(R_K\) acts injectively on it, hence on \(C\). Thus \(C\) is torsion-free over \(R_K\). It is also finite over \(R_K\), because a finite generating list for \(D\) as an \(R\)-module remains a generating list after tensoring with \(K\).

We claim \(P\cap R_K=(0)\). If a nonzero \(a\in R_K\) belonged to \(P\), the image of \(a\) in \(C_P\) would be nilpotent. Indeed, minimality of \(P\) says that \(C_P\) has just one prime, namely \(PC_P\), and the intersection of all primes is the nilradical. To verify the latter fact, a nilpotent lies in every prime. For a nonnilpotent \(z\), Zorn's lemma supplies an ideal \(J\) maximal among those disjoint from \(\{1,z,z^2,\ldots\}\): unions of chains remain disjoint. This ideal is prime. If \(ab\in J\) with \(a,b\notin J\), maximality would put a power of \(z\) in each of \(J+(a)\) and \(J+(b)\); multiplying them would put a power of \(z\) in \(J\), a contradiction. Thus some prime omits every nonnilpotent element, proving the equality. Consequently \(a^n/1=0\) for some \(n\geq1\). By the definition of localization, there would be \(s\in C\setminus P\) with \(sa^n=0\). Injectivity of multiplication by \(a\) on \(C\) would force \(s=0\), contradicting \(s\notin P\).

It follows that \(R_K\hookrightarrow C/P\) is a finite integral inclusion. Dimension under integral inclusions, followed by the polynomial dimension calculation, gives
\[
\dim(C/P)=\dim R_K=d.
\]
This argument does not require \(C\) itself to be a domain or reduced. \(\square\)

**Lemma C (reading pointwise dimension from components).** Let \(A\) be a finite-type algebra over a field \(F\), let \(r\) be a prime, and let \(y\) be its point. Then
\[
\dim_y\operatorname{Spec}A
=\max_{p\in\operatorname{Min}(A),\ p\subset r}\dim(A/p).
\]

**Proof.** A nonempty open subset of an irreducible component \(V(p)\) contains a basic open \(D(\bar f)\) with \(\bar f\neq0\). The domain \((A/p)_f\) is still of finite type over \(F\) and has the same fraction field as \(A/p\); Theorem 4.2 of AG-CA-09 therefore gives \(\dim(A/p)_f=\dim(A/p)\). An open subset has dimension at most its ambient space: close a chain of irreducible closed subsets in the ambient space; intersection back with the open recovers each member, so the chain remains strict. Hence every nonempty open subset of \(V(p)\) has dimension \(\dim(A/p)\).

Every neighborhood of \(y\) intersects each component containing \(y\) in such an open subset. This gives the displayed maximum as a lower bound. There are only finitely many components. Delete the union of the components not containing \(y\); the complement \(U\) is an open neighborhood. The intersections with the remaining components form a finite closed cover of \(U\). Dimension of a finite closed cover is the largest dimension of its members: the largest irreducible set in any chain is contained in one member of the cover, and then the whole chain is contained there. This makes \(\dim U\) exactly the displayed maximum and proves the formula. \(\square\)

### Proof through irreducible components

Write \(B=S_K\) and \(Q=\mathfrak q_K\). First take a minimal prime \(P\subset Q\) of \(B\), and let \(p=P\cap S\). Lemma A forces \(p\) to be minimal in \(S\): a strictly smaller prime of \(S\) could be lifted below \(P\), contradicting its minimality. Also \(p\subset\mathfrak q\).

The prime \(P\) contains \(pB\), and
\[
B/pB\cong K\otimes_k(S/p).
\]
Here tensoring the quotient sequence is exact, since \(K\) is a flat \(k\)-module. The prime \(P/pB\) is minimal in this quotient: a smaller prime there would give a smaller prime than \(P\) in \(B\). Lemma B, applied to the domain \(S/p\), now gives
\[
\dim(B/P)=\dim(S/p).
\tag{*}
\]

Conversely, fix any minimal prime \(p\subset\mathfrak q\) of \(S\). Lemma A supplies a prime \(P'\subset Q\) of \(B\) over \(p\). Choose a minimal prime \(P\subset P'\); one exists because \(B\) is Noetherian. Its contraction is contained in \(p\), and minimality of \(p\) forces that contraction to be \(p\). Thus every downstairs component through \(x\) is accounted for by an upstairs component through the selected point \(x_K\). Equality (*) holds for this component as well.

Lemma C on both sides finishes the proof:
\[
\dim_{x_K}X_K
=\max_{P\in\operatorname{Min}(B),\ P\subset Q}\dim(B/P)
=\max_{p\in\operatorname{Min}(S),\ p\subset\mathfrak q}\dim(S/p)
=\dim_xX.
\qquad\square
\]

The component correspondence need not be one-to-one. A component may split after extending the ground field, but every component obtained from it has the same dimension, and the lifting argument supplies the components needed at the particular point under consideration.

### A second proof using a common local fibre

This proof also explains the roles of pointwise dimension and local-ring dimension. Two actual earlier CC0 results apply: AG-CA-09, Theorem 6.1 proves
\[
\dim_y\operatorname{Spec}A
=\dim A_r+\operatorname{trdeg}_F\kappa(r)
\tag{1}
\]
for every finite-type \(F\)-algebra \(A\), and AG-CA-11, Theorem 5.1 proves that a flat local map of Noetherian local rings \((R,m)\to(T,n)\) satisfies
\[
\dim T=\dim R+\dim(T/mT).
\tag{2}
\]
The complete proof of (2) uses base and fibre systems of parameters for the upper bound and going down to concatenate prime chains for the lower bound. Its local dimension and parameter theorem is proved in Section 2 of that lesson. Neither formula assumes that the rings are reduced or equidimensional.

Choose a polynomial presentation \(A=k[t_1,\ldots,t_n]\twoheadrightarrow S\), with kernel \(I\), and let \(r\) be the inverse image of \(\mathfrak q\). Its scalar extension is \(A_K=K[t_1,\ldots,t_n]\twoheadrightarrow B\); denote the inverse image of \(Q\) by \(R\). The local quotients are
\[
S_{\mathfrak q}=A_r/IA_r,
\qquad B_Q=(A_K)_R/I(A_K)_R.
\]
Both vertical maps \(A_r\to(A_K)_R\) and \(S_{\mathfrak q}\to B_Q\) are flat, by Lemma A and localization. Their closed fibres are the same ring. Indeed, the inverse image of \(\mathfrak q B_Q\) under the quotient map \((A_K)_R\twoheadrightarrow B_Q\) is \(r(A_K)_R\), since \(r\) is the inverse image of \(\mathfrak q\) and contains \(I\). Therefore
\[
H:=(A_K)_R/r(A_K)_R
\cong B_Q/\mathfrak q B_Q.
\]
Apply (2) to the two flat local maps. Subtracting their equal fibre terms yields
\[
\dim(A_K)_R-\dim B_Q
=\dim A_r-\dim S_{\mathfrak q}.
\tag{3}
\]

The local quotients \(A_r\twoheadrightarrow S_{\mathfrak q}\) have identical residue fields, and the corresponding assertion holds over \(K\). Consequently (1) turns each side of (3) into a difference of pointwise dimensions: the residue transcendence terms cancel within each quotient pair. A polynomial spectrum is irreducible of dimension \(n\), and every nonempty open subset has dimension \(n\), as in Lemma C. Thus (3) says
\[
n-\dim_{x_K}X_K=n-\dim_xX,
\]
which proves the theorem again. The fibre dimension need not be zero, and the two local-ring dimensions alone need not agree. \(\square\)

### Sources

The theorem is the result recorded as [Stacks Project, Tag 00P4](https://stacks.math.columbia.edu/tag/00P4). For the local-fibre argument, the upstream comparison results are [Tag 00P2](https://stacks.math.columbia.edu/tag/00P2), [Tag 00P1](https://stacks.math.columbia.edu/tag/00P1), and [Tag 00ON](https://stacks.math.columbia.edu/tag/00ON). These were consulted as freely accessible mathematical sources. The existing AG-CA lessons linked above provide the internal proved foundations used here.


The first three results correspond to [Stacks, Tag 0307](https://stacks.math.columbia.edu/tag/0307), [Tag 00PY](https://stacks.math.columbia.edu/tag/00PY), and [Tag 00Q2](https://stacks.math.columbia.edu/tag/00Q2). The programme proofs linked above and the two proofs written here supply the arguments.
