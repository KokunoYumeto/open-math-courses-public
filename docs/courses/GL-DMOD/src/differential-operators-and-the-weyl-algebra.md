# Differential operators and the Weyl algebra

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Mathematical and source-comparison corrections by GPT-6 Astra (OpenAI), Ultra, October 2026; original exposition and complete solutions retained.*

A differential equation allows multiplication by a function and differentiation, and it matters which comes first. On the affine line, differentiating a product gives

\[
\partial x-x\partial=1.
\]

We will build the algebra behind this identity, explain why its leading terms live on a cotangent bundle, and prove that its ideals behave very differently from ideals of a polynomial ring. The construction works on every smooth variety in characteristic zero, even when there are no global coordinates.

We assume elementary ring and module theory, the universal property of Kähler differentials, and the local description of a smooth variety by étale coordinates. In particular, an étale algebra has unique lifting of algebra maps across nilpotent ideals. These are the algebraic prerequisites; none of the analytic theory of differential equations is needed here. The [Algebraic Geometry Bridge](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D100) supplies geometric background. Basic references are the Stacks project, Bezrukavnikov's *Noncommutative Algebra*, and Ginzburg's *Lectures on D-modules*. The proofs below develop the algebra directly.

Except in the section explicitly devoted to positive characteristic, \(k\) is a field of characteristic zero. A variety is smooth, separated and of finite type over \(k\). We use \([P,Q]=PQ-QP\). The order filtration gives degree zero to functions and degree one to vector fields; the Bernstein filtration on a Weyl algebra gives degree one to both.

## 1. Reading a noncommutative formula

Let \(A=k[x,y]\), and write \(\partial_x,\partial_y\) for its usual derivations. Consider

\[
P=x^2\partial_x\partial_y-\partial_y.
\]

Applied to a monomial, it gives

\[
P(x^a y^b)=abx^{a+1}y^{b-1}-bx^a y^{b-1}.
\]

This calculation is about an operator on functions. In contrast, its principal symbol will be the function \(x^2\xi_x\xi_y\) on the cotangent bundle. The variables \(\xi_x,\xi_y\) describe covectors; they are not additional coordinates of the original variety. Lower derivative terms disappear from the principal symbol.

On \(k[x]\), the Euler operator \(\theta=x\partial\) satisfies

\[
\theta(x^r)=rx^r,
\qquad
\theta x^r=x^r\theta+rx^r.
\]

The first formula applies an operator to a function. The second is an equality of operators and still has a derivative term. Keeping these two meanings apart prevents many sign and order mistakes.

Every derivation \(\delta\) satisfies

\[
[\delta,a](b)=\delta(ab)-a\delta(b)=\delta(a)b.
\]

Thus commuting a derivation with multiplication produces multiplication. This observation gives a coordinate-free definition of order.

## 2. Order from repeated commutators

For a commutative \(k\)-algebra \(A\) and \(A\)-modules \(M,N\), put \(\operatorname{Diff}^{-1}_{A/k}(M,N)=0\). Define recursively

\[
\operatorname{Diff}^{m}_{A/k}(M,N)
=\{P\in\operatorname{Hom}_k(M,N):[P,a]\in
\operatorname{Diff}^{m-1}_{A/k}(M,N)\text{ for every }a\in A\}.
\]

Here \([P,a](u)=P(au)-aP(u)\). For \(m=0\), this is exactly \(\operatorname{Hom}_A(M,N)\). Membership means order **at most** \(m\). The zero operator belongs to every level. An operator has exact order \(m\) if it belongs to level \(m\) and not to level \(m-1\).

The spaces of operators are closed under addition and under multiplication by functions on either side. This follows recursively: commutation with a function commutes with either of these two scalar actions, because \(A\) is commutative. They form an increasing filtration, since the same recursion shows that an operator of order at most \(m-1\) also has order at most \(m\).

**Theorem 2.1.** If \(P:M\to N\) has order at most \(m\) and \(Q:N\to L\) has order at most \(n\), then \(QP\) has order at most \(m+n\).

**Proof.** Induct on \(m+n\). For zero total order, both maps are \(A\)-linear. In general,

\[
[QP,a]=Q[P,a]+[Q,a]P.
\]

The first summand has order at most \(n+m-1\), by the inductive hypothesis, and so does the second. A summand whose commutator is zero can simply be omitted. The defining condition now gives the assertion. \(\square\)

Orders can drop in a product: multiplication by zero is one immediate example. Later, when the associated graded ring has no zero divisors, we will obtain exact additivity for nonzero operators. The theorem here makes no smoothness assumption and allows arbitrary modules.

Write

\[
D_{A/k}=\bigcup_{m\geq0}\operatorname{Diff}^{m}_{A/k}(A,A),
\qquad F_mD_{A/k}=\operatorname{Diff}^{m}_{A/k}(A,A).
\]

Theorem 2.1 makes this a filtered ring. It contains \(A\) as multiplication operators, but that copy of \(A\) is generally not central.

**Lemma 2.2.** To test order at most \(m\), it suffices to test commutators with algebra generators of \(A\) over \(k\).

**Proof.** Suppose the required commutators have order at most \(m-1\). The elements for which this holds form a \(k\)-subalgebra, since

\[
[P,a+b]=[P,a]+[P,b],\qquad
[P,ab]=[P,a]b+a[P,b].
\]

The closure properties just proved justify the second equality as an order bound. The subalgebra contains the generators and hence all of \(A\). \(\square\)

In order one there is already a complete answer:

\[
F_1D_{A/k}=A\oplus\operatorname{Der}_k(A,A).
\]

Indeed, if \(P\) has order at most one, then \([P,a]\) is multiplication by \(P(a)-aP(1)\). Substituting into \(P(ab)\) shows that \(\delta(a)=P(a)-aP(1)\) obeys the Leibniz rule. Conversely, a derivation plus multiplication has order at most one.

There is also a useful truncated algebra representing every level of order. Let

\[
I=\ker(A\otimes_k A\longrightarrow A),\qquad
\mathcal P^m_{A/k}=(A\otimes_k A)/I^{m+1}.
\]

We regard this as a left \(A\)-module through the first factor. It is called the module of principal parts of order \(m\).

**Lemma 2.3.** Sending \(P\) to the map \(a\otimes b\mapsto aP(b)\) gives

\[
F_mD_{A/k}\simeq\operatorname{Hom}_A(\mathcal P^m_{A/k},A).
\]

**Proof.** Every \(k\)-linear \(P\) gives a unique left \(A\)-linear map from \(A\otimes_k A\). The ideal \(I\) is generated by the differences \(1\otimes a-a\otimes1\). Applying the map to such a difference times \(1\otimes b\) gives \([P,a](b)\). Applying it to a product of \(m+1\) differences gives the corresponding iterated commutator. The recursive definition of order is equivalent to all these iterated commutators vanishing. That is precisely the condition that the map kill \(I^{m+1}\). \(\square\)

**Finiteness and its boundary.** Lemma 2.3 does not assume that \(A\) is finitely generated. If \(A\) is generated over \(k\) by \(x_1,\ldots,x_r\), however, its principal parts of each fixed order are finite as a left \(A\)-module. To prove this, put \(\delta_i=1\otimes x_i-x_i\otimes1\). The algebra \(A\otimes_k A\), viewed over its left factor, is generated by the \(\delta_i\): its right generators are \(1\otimes x_i=\delta_i+x_i\otimes1\). The quotient by all the \(\delta_i\) identifies the two factors and is \(A\), so these differences generate \(I\). Consequently the finitely many monomials

\[
\delta_1^{a_1}\cdots\delta_r^{a_r},
\qquad a_i\geq0,\quad\sum_i a_i\leq m,
\]

span \(\mathcal P^m_{A/k}\) over \(A\); monomials of larger degree lie in \(I^{m+1}\). This argument works over an arbitrary commutative base ring and requires no Noetherian hypothesis.

Finiteness fails in general. For the polynomial algebra \(A=k[x_1,x_2,\ldots]\) over a nonzero field, the change of variables \(y_i=x_i+\delta_i\) in the right factor gives

\[
\begin{aligned}
A\otimes_k A&\cong A[\delta_1,\delta_2,\ldots],\\
\mathcal P^1_{A/k}&\cong
A\oplus\bigoplus_{i\geq1}A\delta_i,\\
\delta_i\delta_j&=0\quad\text{in }\mathcal P^1_{A/k}.
\end{aligned}
\]

The direct sum is an equality of left-module descriptions: the quotient discards exactly the monomials of degree at least two in the differences. Any finite set of elements uses only finitely many of the independent \(\delta_i\), so cannot generate this module over \(A\). It cannot generate it as an \(A\)-algebra either, because products of two differences vanish. The principal-parts representation of differential operators remains valid for this algebra. \(\square\)

References for the intrinsic definitions are [Stacks, Tags 09CI, 09CJ and 0G35]. These arguments also apply over an arbitrary commutative base ring with base-linear maps.

## 3. Why étale coordinates suffice

An étale coordinate chart of dimension \(n\) is an étale map

\[
k[x_1,\ldots,x_n]\longrightarrow A.
\]

Such charts exist locally on a smooth variety. The differentials \(dx_i\) form a basis of \(\Omega^1_{A/k}\). Let \(\partial_i\) be the dual derivations, so that \(\partial_i(x_j)=\delta_{ij}\). Their brackets vanish: \([\partial_i,\partial_j]\) is a derivation killing every \(x_\ell\), and the basis of differentials says that such a derivation is zero.

The subtlety is that \(A\) need not be generated over \(k\) by the \(x_i\). We therefore cannot prove a statement about operators on \(A\) just by testing polynomials and ignoring the étale extension.

**Proposition 3.1.** On this chart, there is an isomorphism of left \(A\)-algebras

\[
\mathcal P^m_{A/k}\simeq
A[t_1,\ldots,t_n]/(t_1,\ldots,t_n)^{m+1},
\qquad 1\otimes x_i-x_i\otimes1\longleftrightarrow t_i.
\]

**Proof.** Put \(R=A[t_1,\ldots,t_n]/(t)^{m+1}\). Give \(R\) a polynomial-algebra structure by \(x_i\mapsto x_i+t_i\). Modulo \((t)\), the identity of \(A\) is a map compatible with this structure. The unique lifting property of the étale algebra gives a unique map \(\tau:A\to R\) lifting that identity and sending \(x_i\) to \(x_i+t_i\).

Consequently \(a\otimes b\mapsto a\tau(b)\) sends \(I\) into \((t)\) and induces \(\phi:\mathcal P^m_{A/k}\to R\). In the other direction, send \(a\in A\) to its first-factor image and \(t_i\) to \(1\otimes x_i-x_i\otimes1\). Since these differences belong to \(I\), this defines \(\psi:R\to\mathcal P^m_{A/k}\).

The composite \(\phi\psi\) fixes \(A\) and all \(t_i\), so is the identity. The maps \(b\mapsto\psi\tau(b)\) and \(b\mapsto1\otimes b\) from \(A\) to \(\mathcal P^m_{A/k}\) both lift the identity modulo \(I\), with polynomial coordinates sent to \(1\otimes x_i\). Unique étale lifting identifies them. Thus \(\psi\phi\) fixes both factors and is the identity too. \(\square\)

For a multi-index \(\alpha=(\alpha_1,\ldots,\alpha_n)\), write \(|\alpha|=\sum\alpha_i\), \(\alpha!=\prod\alpha_i!\), and \(\partial^\alpha=\prod\partial_i^{\alpha_i}\). In characteristic zero the étale lift just constructed is

\[
\tau(b)=\sum_{|\alpha|\leq m}
\frac{\partial^\alpha(b)}{\alpha!}t^\alpha.
\]

To verify this, the iterated Leibniz rule shows that the displayed formula is an algebra map into the truncated ring. It lifts the identity and has the required values on the \(x_i\), so étale uniqueness identifies it with \(\tau\).

**Theorem 3.2.** Every differential operator on the chart has a unique finite expression

\[
P=\sum_\alpha a_\alpha\partial^\alpha,\qquad a_\alpha\in A.
\]

It has order at most \(m\) exactly when only indices with \(|\alpha|\leq m\) occur. In particular, \(F_mD_{A/k}\) is free of rank \(\binom{n+m}{n}\).

**Proof.** The monomials \(t^\alpha\), \(|\alpha|\leq m\), are a basis of principal parts. Under Lemma 2.3, their coefficient functionals are the operators \(\partial^\alpha/\alpha!\). They form a basis of \(F_mD\). Comparing the bases at consecutive values of \(m\) proves the order assertion. \(\square\)

Equivalently, \(D\) is generated by functions and the commuting \(\partial_i\), with relations

\[
[\partial_i,a]=\partial_i(a),\qquad
[\partial_i,\partial_j]=0.
\]

Moving functions to the left gives spanning by the displayed monomials, and their independence proves that these are all the relations on a coordinate chart.

The construction is local on the variety. Indeed, principal parts on a smaller open set are the restriction of principal parts on the chart: after a function is inverted in the first factor, its second-factor image differs from it by a nilpotent element and is also invertible. Since each \(\mathcal P^m\) is locally free of finite rank, its dual restricts as well. This gives the sheaf \(\mathcal D_X\) and its locally free order pieces \(F_m\mathcal D_X\). This argument also explains the localization property in [Stacks, Tag 0G36]. The sheaf definition is discussed in [Stacks, Tag 0G3P].

## 4. Cotangent geometry and the leading bracket

Put \(\mathcal T_X=\operatorname{Der}_k(\mathcal O_X,\mathcal O_X)\). The cotangent bundle is

\[
T^*X=\operatorname{Spec}_X\operatorname{Sym}_{\mathcal O_X}\mathcal T_X,
\qquad \pi:T^*X\to X.
\]

A tangent vector field \(v\) defines a fibre-linear function on covectors by evaluation \(\eta\mapsto\eta(v)\). This is why the symmetric algebra of the **tangent** sheaf is the algebra of functions on the **cotangent** bundle.

For \(P\in F_m\mathcal D_X\), let \(\sigma_m(P)\) be its class modulo \(F_{m-1}\). Multiplication of these classes is defined because Theorem 2.1 respects the filtration. Locally the relations imply

\[
[F_m\mathcal D_X,F_n\mathcal D_X]
\subset F_{m+n-1}\mathcal D_X.
\]

One can see this by moving derivatives past coefficients: the terms with no coefficient differentiated cancel in the commutator, and every remaining term has at least one fewer derivative. Hence the associated graded ring is commutative.

**Theorem 4.1.** There is a canonical graded isomorphism

\[
\operatorname{gr}^{F}\mathcal D_X
\simeq \operatorname{Sym}_{\mathcal O_X}\mathcal T_X
=\pi_*\mathcal O_{T^*X}.
\]

On an étale chart it sends \(\sigma_1(\partial_i)\) to \(\xi_i\), and

\[
\sigma_m\Bigl(\sum_{|\alpha|\leq m}a_\alpha\partial^\alpha\Bigr)
=\sum_{|\alpha|=m}a_\alpha\xi^\alpha.
\]

**Proof.** Functions and vector fields define an intrinsic homomorphism from the symmetric algebra to \(\operatorname{gr}^{F}\mathcal D_X\), because their symbols commute. In each chart, Theorem 3.2 identifies the monomial bases on the two sides. Thus the map is an isomorphism locally, and its intrinsic definition glues these isomorphisms. \(\square\)

For every \(P\in F_mD\), \(Q\in F_nD\), including operators of smaller actual order,

\[
\sigma_{m+n}(PQ)=\sigma_m(P)\sigma_n(Q).
\]

This is a statement in the indicated graded piece, where the symbol of an operator of lower order is zero. It follows directly from graded multiplication, or from the leading terms in the coordinate normal form.

Define a bracket on homogeneous symbols by

\[
\{\sigma_m(P),\sigma_n(Q)\}
=\sigma_{m+n-1}([P,Q]).
\]

Changing a lift by one filtration level changes the commutator by a level too, so the definition is independent of lifts. Antisymmetry, the Jacobi identity and the Leibniz rule follow from their commutator counterparts. In coordinates,

\[
\{\xi_i,x_j\}=\delta_{ij},\qquad
\{x_i,x_j\}=\{\xi_i,\xi_j\}=0,
\]

and therefore, for polynomial functions in the fibre coordinates,

\[
\{p,q\}=\sum_i
\left(\frac{\partial p}{\partial\xi_i}\partial_iq
-\partial_i p\frac{\partial q}{\partial\xi_i}\right).
\]

This fixes the sign of the cotangent Poisson bracket used here. With \(p=x^2\xi_x\xi_y\) and \(q=x\), the bracket is \(x^2\xi_y\). Directly, the operator from Section 1 satisfies \([P,x]=x^2\partial_y\), with exactly that principal symbol.

Changing coordinates can alter lower-order terms of an operator. Its principal symbol remains the same cotangent function. For example, on \(\mathbb G_m\) use \(z=x^{-1}\). Then \(\partial_x=-z^2\partial_z\), so

\[
\partial_x^2=z^4\partial_z^2+2z^3\partial_z.
\]

The quadratic symbols agree under the induced covector-coordinate change. The second term shows why a total expression in derivatives is not itself coordinate invariant.

## 5. Polynomial operators: two filtrations, one ring

On \(\mathbb A^n\), Theorem 3.2 identifies \(D_{k[x]/k}\) with the Weyl algebra

\[
A_n(k)=k\langle x_1,\ldots,x_n,\partial_1,\ldots,\partial_n\rangle/
\bigl([x_i,x_j], [\partial_i,\partial_j],
[\partial_i,x_j]-\delta_{ij}\bigr).
\]

Its \(k\)-basis is \(x^\alpha\partial^\beta\). The order filtration counts only \(|\beta|\), while the Bernstein filtration is

\[
B_rA_n=\operatorname{span}_k\{x^\alpha\partial^\beta:
|\alpha|+|\beta|\leq r\}.
\]

The defining commutator replaces two letters by a scalar, so multiplication respects this filtration and

\[
\operatorname{gr}^{B}A_n\simeq
k[x_1,\ldots,x_n,\xi_1,\ldots,\xi_n],
\quad \deg x_i=\deg\xi_i=1.
\]

In the order grading, \(x_i\) has degree zero instead. The underlying polynomial rings are isomorphic; their gradings and the dimensions of their filtration pieces differ. For example,

\[
\dim_k B_rA_n=\binom{r+2n}{2n},
\]

whereas \(F_0A_n=k[x_1,\ldots,x_n]\) already has infinite \(k\)-dimension when \(n>0\).

**Theorem 5.1.** Let \(R\) be a ring with an exhaustive increasing multiplicative filtration \(F_mR\), \(m\geq0\), with \(1\in F_0R\) and \(F_{-1}R=0\). If \(\operatorname{gr}^{F}R\) is left Noetherian, then \(R\) is left Noetherian. The corresponding right-handed assertion also holds. In particular, commutative Noetherian associated graded implies both.

**Proof.** Give a left ideal \(J\subset R\) the intersection filtration. Its associated graded embeds as a homogeneous left ideal of \(\operatorname{gr}^{F}R\), so it has finitely many homogeneous generators \(\bar q_1,\ldots,\bar q_s\). Lift them to \(q_i\in J\), of degrees \(d_i\).

For \(u\in J\) of degree \(m\), express its symbol as \(\sum_i\bar a_i\bar q_i\), choosing homogeneous coefficients of degree \(m-d_i\) and omitting negative degrees. Lift the coefficients to \(a_i\in R\). Then \(u-\sum_i a_iq_i\) has degree at most \(m-1\). Repeating terminates at degree below zero and proves that the \(q_i\) generate \(J\). Every left ideal is therefore finitely generated. Apply the argument to the opposite ring for right ideals. \(\square\)

The lower bound and exhaustiveness in this theorem matter: they guarantee that degree reduction terminates and reaches every element of the ring. No topology or completion is required for this nonnegative filtration. Compare Ginzburg, Proposition 1.1.6(i), in the freely accessible lecture notes linked below. The proof here supplies the filtered statement directly.

Consequently \(A_n\) is left and right Noetherian. More generally, for smooth affine \(X=\operatorname{Spec}A\), the order grading of \(D_{A/k}\) is \(\operatorname{Sym}_A\operatorname{Der}_k(A,A)\). The derivation module is finitely generated projective, so this symmetric algebra is a finitely generated commutative algebra over the Noetherian ring \(A\). Thus \(D_{A/k}\) is left and right Noetherian as well. To identify the affine associated graded with global sections, use exactness of global sections for quasi-coherent sheaves on an affine scheme in each finite filtration level; this avoids assuming global coordinates.

**Theorem 5.2.** For \(n\geq1\), the characteristic-zero Weyl algebra \(A_n\) is simple and has no nonzero finite-dimensional unital modules.

**Proof of simplicity.** Let \(J\) be a nonzero two-sided ideal. Choose a nonzero element \(P\in J\) of smallest Bernstein degree. Each commutator \([\partial_i,P]\) and \([P,x_i]\) belongs to \(J\) and has smaller Bernstein degree unless it is zero. Minimality makes all these commutators zero.

In normal form,

\[
[\partial_i,x^\alpha\partial^\beta]
=\alpha_i x^{\alpha-e_i}\partial^\beta,
\qquad
[x^\alpha\partial^\beta,x_i]
=\beta_i x^\alpha\partial^{\beta-e_i}.
\]

Normal-form independence and characteristic zero first force all positive \(x_i\)-exponents to vanish, then all positive \(\partial_i\)-exponents. Thus \(P\) is a nonzero scalar. Its inverse gives \(1\in J\), hence \(J=A_n\). \(\square\)

**Proof concerning finite dimension.** On a finite-dimensional unital module \(V\), take traces of \([\partial_1,x_1]=1\). A commutator of endomorphisms has trace zero, while the identity has trace \(\dim_k V\). In characteristic zero this forces \(\dim_k V=0\). \(\square\)

This does not say that \(A_n\) has no proper left ideals: for instance, \(A_1\partial\) is proper, with quotient \(k[x]\). Simplicity concerns two-sided ideals. When \(n=0\), \(A_0=k\) is still simple but certainly has finite-dimensional modules; the restriction \(n\geq1\) in the second assertion is essential.

Also, \(A_n\) has no zero divisors: the Bernstein symbol of a product of two nonzero elements is the product of two nonzero polynomials. This proves the product is nonzero. The same reasoning proves exact additivity of order on a connected smooth affine variety, since its cotangent coordinate ring is a domain.

On \(\mathbb G_m\), the normal form is

\[
D_{k[x,x^{-1}]/k}
=\bigoplus_{j\geq0}k[x,x^{-1}]\partial^j
=\bigoplus_{j\geq0}k[x,x^{-1}]\theta^j.
\]

For the second equality, \(\theta^j=x^j\partial^j\) plus lower-order terms, with invertible leading coefficient \(x^j\). Thus the change of basis is triangular and invertible in every finite order. In this form \(\theta x^r=x^r(\theta+r)\) for every \(r\in\mathbb Z\).

## 6. What changes in positive characteristic

Now let \(k\) have characteristic \(p>0\), and work on \(k[x]\). Define the Hasse operators by

\[
H_r(x^q)=\binom qr x^{q-r},
\]

with the binomial coefficient reduced in \(k\) and the value zero if \(q<r\). Pascal's identity gives

\[
[H_r,x]=H_{r-1},\qquad H_0=1.
\]

Lemma 2.2 and induction show that \(H_r\) has order at most \(r\). Repeating the commutator \(r\) times gives \(H_0\ne0\), so the order is exactly \(r\). For \(r<p\), one has \(H_r=\partial^r/r!\). But

\[
\partial^p=0\text{ on }k[x],\qquad H_p(x^p)=1.
\]

Every derivation is \(a(x)\partial\), and it commutes with multiplication by \(x^p\). Functions commute with \(x^p\) as well, so the ring generated by functions and derivations commutes with \(x^p\). The operator \(H_p\) does not: its commutator with \(x^p\), applied to \(1\), is \(1\). Therefore Grothendieck's differential-operator ring is strictly larger than the ring generated by functions and derivations.

There is also a finite-dimensional representation of the abstract characteristic-\(p\) Weyl algebra: multiplication by \(x\) and differentiation on

\[
V=k[x]/(x^p).
\]

Differentiation preserves the ideal because \(\partial(x^p)=0\), and the relation \([\partial,x]=1\) remains valid. The module has dimension \(p\). Its identity has trace \(p=0\) in \(k\), so the characteristic-zero obstruction disappears. This representation of the abstract algebra is not faithful: \(x^p\) and \(\partial^p\) act by zero.

## 7. Exercises and complete solutions

The difficulty labels indicate the length of the argument, not additional background.

**Exercise 7.1 (easy).** On \(k[x]\), expand \([\partial^2,x^2]\) in normal form. Then compute \([\partial^3,x^2]\) and check the leading-symbol bracket in each case.

**Solution.** First \(\partial x^2=x^2\partial+2x\), whence

\[
\partial^2x^2=x^2\partial^2+4x\partial+2.
\]

Thus \([\partial^2,x^2]=4x\partial+2\). Differentiating that normal-form expression once more gives

\[
\partial^3x^2=x^2\partial^3+6x\partial^2+6\partial,
\]

so the second commutator is \(6x\partial^2+6\partial\). The leading symbols are respectively \(4x\xi\) and \(6x\xi^2\), agreeing with \(\{\xi^2,x^2\}\) and \(\{\xi^3,x^2\}\).

**Exercise 7.2 (easy).** Show that \(x\mapsto x\), \(\partial\mapsto-\partial\), with reversal of products, defines an involutive anti-automorphism \(t\) of \(A_1\). Compute \(t(x^2\partial^2+x\partial)\).

**Solution.** On the free associative algebra, reverse every word and replace each \(\partial\) by \(-\partial\). The relation \(\partial x-x\partial-1\) is carried to \(-x\partial+\partial x-1\), the same relation, so the map descends. Applying it twice fixes the generators and every product, making it an involution. Finally,

\[
t(x^2\partial^2+x\partial)=\partial^2x^2-\partial x
=x^2\partial^2+3x\partial+1.
\]

**Exercise 7.3 (medium).** Prove the multiplicative symbol identity for
\(P=\sum a_\alpha\partial^\alpha\) and
\(Q=\sum b_\beta\partial^\beta\) of orders at most \(m,n\), using the complete product formula.

**Solution.** Repeated Leibniz gives

\[
PQ=\sum_{\alpha,\beta}\sum_{\gamma\leq\alpha}
\binom\alpha\gamma a_\alpha\partial^\gamma(b_\beta)
\partial^{\alpha-\gamma+\beta}.
\]

The terms of derivative degree \(m+n\) require \(|\alpha|=m\), \(|\beta|=n\), and \(\gamma=0\). Their sum has symbol \((\sum_{|\alpha|=m}a_\alpha\xi^\alpha)(\sum_{|\beta|=n}b_\beta\xi^\beta)\). All other terms have smaller degree. This proves the identity even if that product is zero.

**Exercise 7.4 (medium).** Give the characteristic-zero trace obstruction for a nonzero finite-dimensional \(A_1\)-module, and construct explicitly the characteristic-\(p\) module of dimension \(p\).

**Solution.** If \(X,D\) are the actions, \(DX-XD=I\) gives \(0=\operatorname{tr}(DX-XD)=\dim V\). In characteristic zero a positive integer is nonzero in \(k\), a contradiction. In characteristic \(p\), take basis \(v_0,\ldots,v_{p-1}\), put \(Xv_j=v_{j+1}\) for \(j<p-1\) and \(Xv_{p-1}=0\), and put \(Dv_j=jv_{j-1}\), with \(Dv_0=0\). For \(j<p-1\) the commutator is \(((j+1)-j)v_j=v_j\). For \(j=p-1\) it is \(-(p-1)v_{p-1}=v_{p-1}\). These formulas realize \(k[x]/(x^p)\).

**Exercise 7.5 (medium).** Give \(x^2\partial^2+x\partial\) its order and Bernstein degree. Compute both leading symbols and explain why they differ.

**Solution.** Its order is two and its order symbol is \(x^2\xi^2\), with \(x\) of degree zero. Its Bernstein degree is four; its Bernstein symbol is again the polynomial \(x^2\xi^2\), now of total degree four. The polynomials happen to agree, but they lie in different graded pieces. For \(x^{10}+\partial\), the distinction is visible in the polynomials themselves: the order symbol is \(\xi\), whereas the Bernstein symbol is \(x^{10}\).

**Exercise 7.6 (hard).** Prove that \(H_p\) is not generated by functions and derivations on \(k[x]\) in characteristic \(p\). Explain why replacing it by \(\partial^p/p!\) is impossible.

**Solution.** For a derivation \(\delta\), \(\delta(x^p)=p x^{p-1}\delta(x)=0\), so \([\delta,x^p]=0\). Multiplications also commute with \(x^p\); sums and products of commuting operators still do. But \([H_p,x^p](1)=H_p(x^p)-x^pH_p(1)=1\). Thus \(H_p\) is outside the generated ring. The scalar \(p!\) is zero in \(k\), while \(\partial^p\) is the zero operator, so the proposed division defines no operator and cannot recover \(H_p\).

**Exercise 7.7 (hard).** Let \(A\) be an étale algebra over \(k[x_1,\ldots,x_n]\) in characteristic zero. Show that an operator of order at most \(m\) that kills every coordinate monomial \(x^\beta\) with \(|\beta|\leq m\) is zero. Identify where the étale condition enters.

**Solution.** By Theorem 3.2 write \(P=\sum_{|\alpha|\leq m}a_\alpha\partial^\alpha\). Evaluating on \(1\) gives \(a_0=0\). Induct on \(r\leq m\), assuming all coefficients of degree less than \(r\) vanish. For \(|\beta|=r\), a derivative with larger total degree kills \(x^\beta\); one with the same total degree contributes only when \(\alpha=\beta\), and then contributes \(\beta!\). Thus \(0=P(x^\beta)=\beta!a_\beta\), so \(a_\beta=0\). Characteristic zero allows division by \(\beta!\). The étale condition entered in proving the normal form on all of \(A\) via principal parts, before the test on monomials; testing monomials alone would not justify that normal form on an arbitrary extension algebra.

## What this lesson does not prove

The geometric prerequisites used are the existence of étale coordinate charts on a smooth variety, the unique nilpotent lifting property of étale maps, and exactness of global sections for quasi-coherent sheaves on affine schemes. The universal property of Kähler differentials is also assumed. These are algebraic geometry results, not assertions about differential-operator modules. In particular, [Stacks, Tags 00UQ and 00UR] identify an étale map of finite presentation with the unique lifting property for square-zero ideals; applying that property successively to the powers of a nilpotent ideal gives the version used in Proposition 3.1. [Stacks, Tag 00TA] gives local standard smooth presentations, and [Stacks, Tag 00T7] identifies their free differentials. For the affine sheaf arguments, [Stacks, Tag 01IA] identifies quasi-coherent sheaves with modules and [Stacks, Tag 01XB] gives vanishing of higher cohomology.

This lesson proves the operator, symbol, Noetherianity, simplicity and finite-dimensional representation statements it uses. It does not assert the corresponding simplicity theorem for every global ring of differential operators, nor a positive-characteristic analogue of the characteristic-zero normal form.

## References

- The Stacks project, *Commutative Algebra*, Tags 09CI, 09CJ, 09CM, 0G35 and 0G36; *Sheaves of Modules*, Tag 0G3P. The [AI Integrated Stacks Project English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-differential-operators) preserves these tags and labels. AI Integrated Stacks Project is an edition with AI-proposed corrections and AI-written additions; it is not reviewed by the maintainers of the [official Stacks project](https://stacks.math.columbia.edu/).
- Roman Bezrukavnikov, *Noncommutative Algebra*, MIT 18.706, spring 2023, Sections 24.6 and 25.2. [Open course materials](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/).
- Victor Ginzburg, with Vladimir Baranovsky and Sam Evens, *Lectures on D-modules*, 1998, Section 1.1, especially Proposition 1.1.6. [University-hosted notes](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf).
- M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §10.1, and V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), for the ring of holomorphic differential operators and its order filtration. The algebraic arguments here do not require the analytic results.
- Alexander Beilinson and Vladimir Drinfeld, *Quantization of Hitchin's integrable system and Hecke eigensheaves*, Sections 1.1.3–1.1.4, for the relationship with differential operators on smooth stacks.
