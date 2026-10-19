# Derivations and the Lipman–Zariski problem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

On a smooth variety of dimension \(d\), the algebraic vector fields form a locally free module of rank \(d\). The Lipman–Zariski problem asks for the converse in characteristic zero: if the vector fields on a variety form a locally free module, is the variety smooth? This course follows the construction, in a 2026 manuscript released by OpenAI, of a normal affine complex surface whose module of vector fields is free of rank two although the surface is singular. The answer to the question is therefore no.

This lesson sets up the objects. It describes the derivation module of a finitely generated algebra through the Jacobian matrix, proves that regularity makes it locally free, and computes a singular surface in positive characteristic whose derivation module is free. It shows how one two-dimensional counterexample in characteristic zero gives counterexamples in every higher dimension. It ends with the statement of the main theorem and the route the remaining lessons take.

**Prerequisites.** From the course *Commutative algebra* (AG-CA): [*Kähler differentials*](course:AG-CA/kahler-differentials) (Theorems 1.1, 2.1, 2.2, 5.1 and 6.2); [*Smooth algebras over a field and the Jacobian criterion*](course:AG-CA/smooth-algebras-over-a-field-and-the-jacobian-criterion) (Lemma 1.1, Theorem 2.1, Proposition 3.1); [*Regular local rings*](course:AG-CA/regular-local-rings) (Corollary 1.2, Proposition 3.3); [*Regular sequences, depth and Cohen–Macaulay modules*](course:AG-CA/regular-sequences-depth-and-cohen-macaulay-modules) (Corollary 6.2); [*Discrete valuation rings, normal rings and Serre's criterion*](course:AG-CA/discrete-valuation-rings-normal-rings-and-serres-criterion) (Corollary 4.5); [*Integral extensions*](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down) (Theorems 1.2 and 2.2, Proposition 2.3); [*Krull dimension and Noether normalization*](course:AG-CA/krull-dimension-and-noether-normalization) (Theorem 4.2). Derivations of affine algebras also appear in the lesson [*Locally nilpotent derivations*](course:jacobian-conjecture-and-affine-spaces/locally-nilpotent-derivations) of the course on the Jacobian conjecture.

Throughout, \(k\) is a field, and algebras are commutative \(k\)-algebras with identity.

## 1. The derivation module

**Definition 1.1.** For a \(k\)-algebra \(A\), a *derivation* is a \(k\)-linear map \(D:A\to A\) with \(D(fg)=fD(g)+gD(f)\). The derivations form an \(A\)-module \(\operatorname{Der}_k(A)\). By the universal property of the module of Kähler differentials (Theorem 1.1 of the lesson on Kähler differentials),

\[
\operatorname{Der}_k(A)\cong\operatorname{Hom}_A(\Omega_{A/k},A).
\]

For an affine variety \(X=\operatorname{Spec}A\), the sheaf associated to \(\operatorname{Der}_k(A)\) is the *tangent sheaf* \(\mathcal T_X\); its sections are the algebraic vector fields.

**Lemma 1.2 (Jacobian description).** Let \(A=k[x_1,\ldots,x_e]/(f_1,\ldots,f_s)\). The map \(D\mapsto(D(x_1),\ldots,D(x_e))\) is an isomorphism

\[
\begin{aligned}
&\operatorname{Der}_k(A)\cong\Bigl\{v\in A^e:\\
&\qquad\sum_{j=1}^e v_j\,\overline{\partial f_i/\partial x_j}=0\\
&\qquad\text{for } i=1,\ldots,s\Bigr\}.
\end{aligned}
\]

**Proof.** The Jacobian presentation (Theorem 5.1 of the lesson on Kähler differentials) is an exact sequence \(A^s\to A^e\to\Omega_{A/k}\to0\), whose first map sends the \(i\)th basis vector to \(\sum_j\overline{\partial f_i/\partial x_j}\,dx_j\). Applying \(\operatorname{Hom}_A(-,A)\), which is left exact, identifies \(\operatorname{Hom}_A(\Omega_{A/k},A)\) with the vectors \((v_j)=(\varphi(dx_j))\) killed by the transposed matrix. Under Definition 1.1, \(\varphi(dx_j)=D(x_j)\). \(\square\)

So a vector field on \(X\subset\mathbb A^e\) is a polynomial vector field \(\sum_jv_j\partial/\partial x_j\), taken modulo the ideal, that is tangent to \(X\): it kills every defining equation modulo the ideal.

**Lemma 1.3 (flat base change).** Let \(M\) be a finitely presented \(A\)-module and \(B\) a flat \(A\)-algebra. The natural map

\[
\begin{aligned}
&\operatorname{Hom}_A(M,A)\otimes_AB\\
&\qquad\longrightarrow\operatorname{Hom}_B(M\otimes_AB,\,B)
\end{aligned}
\]

is an isomorphism. In particular, for a finitely generated \(k\)-algebra \(A\) and a multiplicative set \(S\), \(\operatorname{Der}_k(S^{-1}A)\cong S^{-1}\operatorname{Der}_k(A)\).

**Proof.** Choose a presentation \(A^m\xrightarrow{\alpha}A^n\to M\to0\). Then \(\operatorname{Hom}_A(M,N)\) is the kernel of \(\alpha^{\mathsf T}:N^n\to N^m\), naturally in the \(A\)-module \(N\), and \(\operatorname{Hom}_B(M\otimes_AB,B)\) is the kernel of the same matrix on \(B^n\to B^m\). Tensoring with the flat module \(B\) preserves kernels. For the second statement, \(\Omega_{A/k}\) is finitely presented (Theorem 5.1 of the lesson on Kähler differentials, \(k[x_1,\ldots,x_e]\) being Noetherian), \(S^{-1}A\) is flat over \(A\), and \(\Omega_{S^{-1}A/k}\cong S^{-1}\Omega_{A/k}\) (Theorem 2.2 there). \(\square\)

**Proposition 1.4 (regular points).** Let \(k\) be algebraically closed, \(A\) a finitely generated \(k\)-algebra, and \(\mathfrak m\) a maximal ideal with \(A_{\mathfrak m}\) regular of dimension \(d\). Then \(\operatorname{Der}_k(A)_{\mathfrak m}\) is free of rank \(d\), and so is \(\operatorname{Der}_k(A_g)\) for some \(g\notin\mathfrak m\).

**Proof.** By Proposition 3.1 of the lesson on smooth algebras, \(A\) is smooth at \(\mathfrak m\), and by Lemma 1.1 and Theorem 2.1 there, some principal localization \(A_g\), \(g\notin\mathfrak m\), is standard smooth: \(A_g\cong k[Y_1,\ldots,Y_N]/(F_1,\ldots,F_c)\) with a \(c\times c\) minor of the Jacobian matrix invertible in \(A_g\), and \(N-c=d\). In the Jacobian presentation \(A_g^c\to A_g^N\to\Omega_{A_g/k}\to0\) the first map is then split injective, so \(\Omega_{A_g/k}\) is free of rank \(N-c=d\). Its dual \(\operatorname{Der}_k(A_g)\) is free of rank \(d\), and Lemma 1.3 gives the statement at \(\mathfrak m\). \(\square\)

The converse is the subject of this course.

**The Lipman–Zariski problem.** Let \(k\) have characteristic zero, and let \(A\) be a finitely generated \(k\)-algebra that is a domain. If \(\operatorname{Der}_k(A)\) is a locally free \(A\)-module, must \(A\) be regular?

The expectation that the answer is yes is the *Lipman–Zariski conjecture*. Freeness of \(\operatorname{Der}_k(A)\) is a condition on the dual of \(\Omega_{A/k}\). Local freeness of \(\Omega_{A/k}\) itself is equivalent to smoothness in characteristic zero (Theorem 2.1 of the lesson on smooth algebras); the dual can be free when \(\Omega_{A/k}\) is not.

## 2. A counterexample in positive characteristic

**Proposition 2.1.** Let \(k\) have characteristic \(p>0\) and

\[
A=k[x,y,z]/(xy-z^p).
\]

Then \(A\) is a normal domain of dimension \(2\), its local ring at \(\mathfrak m=(x,y,z)\) is not regular, and \(\operatorname{Der}_k(A)\) is free with basis

\[
D_1=x\,\partial_x-y\,\partial_y,\qquad D_2=\partial_z .
\]

**Proof.** *Domain and dimension.* As a polynomial in \(x\) over \(k[y,z]\), \(xy-z^p\) has degree one with coprime coefficients \(y\) and \(-z^p\), so it is irreducible, hence prime in the factorial ring \(k[x,y,z]\). Its fraction field has transcendence degree \(2\) over \(k\), so \(\dim A=2\) (Theorem 4.2 of the lesson on Krull dimension).

*Derivations.* The partial derivatives of \(f=xy-z^p\) are \(y\), \(x\) and \(-pz^{p-1}=0\). By Lemma 1.2, a derivation is a triple \((a,b,c)\in A^3\) with \(ay+bx=0\), and \(c\) is arbitrary. The element \(x\) is a nonzerodivisor in the domain \(A\), and \(A/xA\cong k[y,z]/(z^p)\) is a polynomial ring in \(y\) over \(k[z]/(z^p)\), in which \(y\) is a nonzerodivisor. From \(ay=-bx\in xA\) we get \(a\in xA\), say \(a=xh\); then \(x(hy+b)=0\) gives \(b=-hy\). So the solutions are exactly \(h(x,-y,0)+c(0,0,1)\), with \(h,c\in A\) uniquely determined because \(x\ne0\) in a domain. This proves the basis.

*Not regular.* \(f\in\mathfrak n^2\) for \(\mathfrak n=(x,y,z)\subset k[x,y,z]\), so \(\mathfrak m/\mathfrak m^2\cong\mathfrak n/\mathfrak n^2\) has dimension \(3\), while \(\dim A_{\mathfrak m}=2\) by Corollary 4.4 of the lesson on Krull dimension.

*Normal.* At a prime \(\mathfrak p\ne\mathfrak m\) of height one, some partial derivative \(y\) or \(x\) is a unit in \(A_{\mathfrak p}\), because \(x,y\in\mathfrak p\) would force \(z^p\in\mathfrak p\) and \(\mathfrak p\supseteq\mathfrak m\). So the Jacobian matrix has rank one there, \(A\) is smooth and \(A_{\mathfrak p}\) is regular (Corollary 2.2 and Theorem 2.1 of the lesson on smooth algebras). Thus \(A\) satisfies \((R_1)\). Every local ring of \(A\) is the quotient of a regular local ring by a nonzero element, hence Cohen–Macaulay (Corollary 6.2 of the lesson on Cohen–Macaulay modules). By Corollary 4.5 of the lesson on Serre's criterion, \(A\) is normal. \(\square\)

The vector fields \(D_1\) and \(D_2\) commute. In characteristic zero this cannot happen at a singular point: a theorem of Jörder, quoted in the introduction of [OpenAI-048], shows that a normal complex space whose tangent sheaf has a local basis of commuting vector fields is smooth. The counterexample of this course therefore has a basis \(w_1,w_2\) with \([w_1,w_2]\ne0\).

## 3. From surfaces to every dimension

**Lemma 3.1.** Let \(A\) be a finitely generated \(k\)-algebra and \(B=A[t_1,\ldots,t_n]\). Then

\[
\operatorname{Der}_k(B)\cong\bigl(\operatorname{Der}_k(A)\otimes_AB\bigr)\oplus B^n .
\]

In particular, if \(\operatorname{Der}_k(A)\) is free of rank \(r\), then \(\operatorname{Der}_k(B)\) is free of rank \(r+n\).

**Proof.** A \(k\)-derivation \(D\) of \(B\) into a \(B\)-module \(M\) restricts to a \(k\)-derivation of \(A\) into \(M\) and has values \(D(t_i)\in M\). Conversely, a derivation \(A\to M\) and arbitrary values \(m_i\in M\) define a unique derivation of \(B\), by the product rule on monomials. So \(\Omega_{B/k}\cong(\Omega_{A/k}\otimes_AB)\oplus\bigoplus_iB\,dt_i\). Dualize, and apply Lemma 1.3 to the free, hence flat, \(A\)-module \(B\). \(\square\)

**Lemma 3.2.** If \(A\) is a normal Noetherian domain, so is \(A[t]\).

**Proof.** Let \(K\) be the fraction field of \(A\). The ring \(K[t]\) is factorial, hence normal (Proposition 2.3 of the lesson on integral extensions), so an element \(g\) of \(K(t)\) integral over \(A[t]\) lies in \(K[t]\). Suppose \(g^m+a_1g^{m-1}+\cdots+a_m=0\) with \(a_i\in A[t]\). Choose \(N\) larger than the degrees of \(g\) and of all \(a_i\), and put \(g_1=t^N-g\), a monic polynomial of degree \(N\). Substituting \(g=t^N-g_1\) and multiplying by \((-1)^m\) gives a monic equation \(g_1^m+b_1g_1^{m-1}+\cdots+b_m=0\) over \(A[t]\) with

\[
\begin{gathered}
b_m=(-1)^mc,\\
c=t^{Nm}+a_1t^{N(m-1)}+\cdots+a_m .
\end{gathered}
\]

Each \(a_it^{N(m-i)}\) has degree less than \(Nm\), so \(c\in A[t]\) is monic. The equation reads \(c=(-1)^{m+1}g_1\,c'\) with \(c'=g_1^{m-1}+b_1g_1^{m-2}+\cdots+b_{m-1}\), a factorization of the monic \(c\) in \(K[t]\) whose factor \(g_1\) is monic; the cofactor is then monic as well. In a splitting field, the roots of \(c\) are integral over \(A\), and the coefficients of \(g_1\) are polynomials in some of these roots. By Theorem 1.2 of the lesson on integral extensions they are integral over \(A\), and they lie in \(K\), so they lie in \(A\). Hence \(g_1\in A[t]\) and \(g=t^N-g_1\in A[t]\). \(\square\)

**Lemma 3.3 (regularity descends along flat local maps).** Let \(R\to S\) be a flat local homomorphism of Noetherian local rings. If \(S\) is regular, so is \(R\).

**Proof.** Let \(\kappa\) and \(\lambda\) be the residue fields. If \(F\to\kappa\) is a free resolution over \(R\), flatness makes \(F\otimes_RS\) a free resolution of \(S/\mathfrak m_RS\) over \(S\), and \((F\otimes_RS)\otimes_S\lambda=F\otimes_R\lambda\). Hence

\[
\begin{aligned}
\operatorname{Tor}_i^S(S/\mathfrak m_RS,\lambda)&\cong\operatorname{Tor}_i^R(\kappa,\lambda)\\
&\cong\operatorname{Tor}_i^R(\kappa,\kappa)\otimes_\kappa\lambda,
\end{aligned}
\]

the second isomorphism because \(\lambda\) is a direct sum of copies of \(\kappa\). If \(S\) is regular, every finite \(S\)-module has projective dimension at most \(\dim S\) (Theorem 2.2 of the lesson on regular local rings), so these groups vanish for \(i>\dim S\). Then \(\operatorname{Tor}_i^R(\kappa,\kappa)=0\) for \(i>\dim S\), so \(\operatorname{pd}_R\kappa<\infty\) by Theorem 2.2 of [*Projective dimension and the Auslander–Buchsbaum formula*](course:AG-CA/projective-dimension-and-the-auslander-buchsbaum-formula), and \(R\) is regular by Serre's characterization. \(\square\)

**Proposition 3.4.** Let \(A\) be a finitely generated normal domain of dimension \(2\) over a field \(k\), with \(\operatorname{Der}_k(A)\cong A^2\), a maximal ideal \(\mathfrak m\) with \(A/\mathfrak m=k\) and \(A_{\mathfrak m}\) not regular, and \(A_{\mathfrak p}\) regular for every prime \(\mathfrak p\ne\mathfrak m\). For \(n\ge0\), the ring \(B=A[t_1,\ldots,t_n]\) is a finitely generated normal domain of dimension \(n+2\) with \(\operatorname{Der}_k(B)\cong B^{n+2}\), and its non-regular primes are exactly those containing \(\mathfrak mB\); they form a closed set of codimension two.

**Proof.** Normality follows from Lemma 3.2 by induction, the derivation module from Lemma 3.1, and the dimension from Theorem 4.2 of the lesson on Krull dimension, since the transcendence degree grows by \(n\). Let \(\mathfrak q\) be a prime of \(B\). If \(\mathfrak q\not\supseteq\mathfrak mB\), then \(\mathfrak p=\mathfrak q\cap A\ne\mathfrak m\), the ring \(A_{\mathfrak p}[t_1,\ldots,t_n]\) is regular (Proposition 3.3 of the lesson on regular local rings), and \(B_{\mathfrak q}\) is a localization of it, hence regular. If \(\mathfrak q\supseteq\mathfrak mB\), then \(\mathfrak q\cap A=\mathfrak m\), and \(A_{\mathfrak m}\to B_{\mathfrak q}\) is a flat local homomorphism, because \(B\) is free over \(A\). If \(B_{\mathfrak q}\) were regular, Lemma 3.3 would make \(A_{\mathfrak m}\) regular. Finally \(V(\mathfrak mB)\cong\operatorname{Spec}k[t_1,\ldots,t_n]\) has dimension \(n\), codimension two in \(\operatorname{Spec}B\). \(\square\)

## 4. The theorem and the route

**Theorem 4.1 (OpenAI, 2026).** There are a finitely generated normal integral \(\mathbb C\)-algebra \(A\) of dimension two and a maximal ideal \(\mathfrak m\) such that \(\operatorname{Der}_{\mathbb C}(A)\cong A^2\) and \(A_{\mathfrak m}\) is not regular. One can choose \(\operatorname{Spec}A\) smooth away from \(\mathfrak m\).

With Proposition 3.4 this gives normal varieties of every dimension \(n\ge2\) whose tangent sheaf is free and whose singular locus has codimension two. The introduction of [OpenAI-048] lists the earlier results proving the conjecture under additional hypotheses: hypersurfaces and complete intersections, graded algebras, isolated singularities in dimension at least three, log canonical singularities, and surface singularities of small geometric genus. The surface constructed here lies outside each of them.

The construction has three stages.

1. *A curve with residue data.* A smooth projective curve \(C\) of genus \(21\) is built on \(\mathbb P^1\times\mathbb P^1\), with a line bundle \(L\) such that \(L^{\otimes4}\cong K_C\) and \(\deg L=10\), six marked points, and global meromorphic sections whose residues satisfy two prescribed identities. A trace form for a degree-four map \(C\to\mathbb P^1\) translates quadratic-space data from an auxiliary elliptic curve into those identities. Lessons: [*An elliptic curve on the quadric*](an-elliptic-curve-on-the-quadric.md), [*A curve of genus 21 with a fourth root of its canonical bundle*](a-curve-of-genus-21-with-a-fourth-root-of-its-canonical-bundle.md), [*Traces, residues and vector bundles on the projective line*](traces-residues-and-vector-bundles-on-the-projective-line.md), [*The trace form and the residue data*](the-trace-form-and-the-residue-data.md).
2. *Vector fields on a neighbourhood.* Starting from the total space of \(L^{-1}\), the gluing of a neighbourhood of the zero section is modified by finitely many flows, so that two vector fields with prescribed finite jets exist and their determinant vanishes to order exactly five along \(C\). Cohomology vanishing on \(C\) and the theorem on formal functions lift the jets to actual fields, and Grauert's criterion contracts \(C\) (self-intersection \(-10\)) to a normal surface singularity with a free tangent sheaf. Lessons: [*Gluing vector fields: the first two orders*](gluing-vector-fields-the-first-two-orders.md), [*Gluing vector fields: higher orders and the determinant*](gluing-vector-fields-higher-orders-and-the-determinant.md), [*Analytic realization and contraction*](analytic-realization-and-contraction.md).
3. *Algebraization.* The analytic germ is replaced by an affine algebraic surface with the same completed local ring, through a finite-determinacy lemma for equations together with their relations and Artin's approximation theorem; freeness of the derivation module descends by faithful flatness. Lesson: [*Algebraization*](algebraization.md).

Seven classical theorems are used without proof in the programme: Grauert's contraction theorem, Grauert's direct image theorem and the analytic theorem on formal functions, Theorem B on Stein spaces, the extension of holomorphic functions across a point of a normal surface, Artin's approximation theorem, and the excellence of convergent power series rings. They are stated exactly where they are used, as N1–N5 in the lesson on analytic realization and as A1, A2 in the lesson on algebraization; everything else is proved in the course or in the lessons it cites.

## 5. Exercises

**5.1** (easy). Show that \(\operatorname{Der}_k(A_g)\cong\operatorname{Der}_k(A)_g\) for a finitely generated \(k\)-algebra \(A\) and \(g\in A\), directly from Lemma 1.2.

**5.2** (medium). Let \(A=k[x,y]/(xy)\). Show that \(\operatorname{Der}_k(A)\) is generated by \(x\partial_x\) and \(y\partial_y\) and is not free.

**5.3** (medium). Let \(A\) be a finitely generated domain over a field \(k\) of characteristic zero. Show that if \(\operatorname{Der}_k(A)\) is free, its rank is \(\dim A\).

**5.4** (hard). Let \(k\) have characteristic zero and \(A=k[x,y,z]/(xy-z^2)\), graded by degree. Show that the derivations of degree zero form a vector space of dimension four, that there are no nonzero derivations of negative degree, and deduce that \(\operatorname{Der}_k(A)\) is not free.

**5.5** (medium). Let \(k\) have characteristic two and \(A=k[x,y]/(y^2-x^3)\). Show that \(A\) is a domain that is not normal, and that \(\operatorname{Der}_k(A)\) is free of rank one. So in positive characteristic a free derivation module does not even force normality.

## 6. Solutions

**5.1.** Write \(A=k[x_1,\ldots,x_e]/I\) and \(A_g=k[x_1,\ldots,x_e,w]/(I,wg-1)\). By Lemma 1.2 a derivation of \(A_g\) is a vector \((v_1,\ldots,v_e,v_w)\) over \(A_g\) killing the derivatives of the generators of \(I\) and of \(wg-1\); the last condition determines \(v_w=-w^2\sum_jv_j\partial g/\partial x_j\). So \(\operatorname{Der}_k(A_g)\) is the set of \(v\in A_g^e\) satisfying the equations for \(I\), which is the localization at \(g\) of the corresponding module over \(A\), because localization is exact.

**5.2.** By Lemma 1.2 a derivation is a pair \((a,b)\) with \(ay+bx=0\). Every element of \(A\) is uniquely \(c+u(x)+w(y)\) with \(c\in k\), \(u\in xk[x]\), \(w\in yk[y]\). Writing \(a\) and \(b\) this way, \(ay+bx\) is the sum of \(a_0y+w_a(y)y\) and \(b_0x+u_b(x)x\), and both parts vanish only if \(a_0=0\), \(w_a=0\), \(b_0=0\), \(u_b=0\). So \(a\in xA\) and \(b\in yA\), and the derivations are \(\{h\,x\partial_x+h'\,y\partial_y\}\). If the module were free, its rank would be one, since at the prime \((y)\) the localization is \(k(x)\cdot x\partial_x\). A generator \(D\) would satisfy \(x\partial_x=aD\) and \(y\partial_y=bD\); as \(y\cdot x\partial_x=0\) and \(D\) generates a free module, \(ya=0\), so \(a\in xA\), and likewise \(b\in yA\). Writing \(D=c\,x\partial_x+e\,y\partial_y\) gives \((1-ca-eb)D=0\), so \(1=ca+eb\in(x,y)\), a contradiction.

**5.3.** Let \(K\) be the fraction field. By Lemma 1.3, \(\operatorname{Der}_k(A)\otimes_AK\cong\operatorname{Der}_k(K)\), the dual of \(\Omega_{K/k}\). In characteristic zero \(K/k\) is separably generated, and \(\Omega_{K/k}\) has dimension equal to the transcendence degree (Theorem 6.2 of the lesson on Kähler differentials), which is \(\dim A\) (Theorem 4.2 of the lesson on Krull dimension).

**5.4.** A derivation of degree zero sends \(x,y,z\) to linear forms, \(D(x_i)=\sum_jM_{ij}x_j\), and must send \(f=xy-z^2\) into \((f)\); in degree two this means \(D(f)=\lambda f\) for a scalar \(\lambda\). These are the matrices preserving the quadratic form \(f\) up to a scalar, a Lie algebra of dimension \(\dim\mathfrak{so}_3+1=4\); explicitly \(x\partial_x+y\partial_y+z\partial_z\), \(x\partial_x-y\partial_y\), \(2z\partial_x+y\partial_z\), \(2z\partial_y+x\partial_z\) are a basis. A derivation of negative degree sends \(x,y,z\) to constants \((c_1,c_2,c_3)\), and \(D(f)=c_1y+c_2x-2c_3z\) must vanish in \(A_1\), so all \(c_i=0\). Hence the graded module \(\operatorname{Der}_k(A)\) begins in degree zero, and \(\operatorname{Der}_k(A)/\mathfrak m\operatorname{Der}_k(A)\), with \(\mathfrak m=(x,y,z)\), has dimension at least four. If \(\operatorname{Der}_k(A)\) were free, it would be free of rank \(\dim A=2\) (Exercise 5.3), and its localization at \(\mathfrak m\) would need only two generators, contradicting Nakayama's lemma.

**5.5.** The polynomial \(y^2-x^3\) is irreducible: as a polynomial in \(y\) of degree two it would otherwise have a root in \(k[x]\), whose square would be \(x^3\). So \(A\) is a domain. The element \(u=y/x\) of its fraction field satisfies \(u^2=x\in A\), so it is integral over \(A\); it is not in \(A\), since otherwise \(y=xu\in xA\), while \(A/xA\cong k[y]/(y^2)\) and \(y\ne0\) there. So \(A\) is not normal. In characteristic two, \(\partial(y^2-x^3)/\partial x=-3x^2=x^2\) and \(\partial(y^2-x^3)/\partial y=2y=0\). By Lemma 1.2 a derivation is a pair \((a,b)\) with \(ax^2=0\), that is \(a=0\), and \(b\) arbitrary. So \(\operatorname{Der}_k(A)=A\,\partial_y\), free of rank one.

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Introduction: the problem, the positive results, and the outline followed in this course.
