# Graded C\*-algebras, Clifford algebras and graded Hilbert modules

*Written by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Grading records which operators change parity. Two odd operators acquire a minus sign when exchanged, and this sign determines the tensor product used in KK-theory. Clifford algebras supply finite-dimensional models of this rule. Graded stabilization then places every countably generated coefficient module inside one standard graded module.

Degrees take values in \(\mathbb Z/2\); all exponents of \((-1)\) are computed modulo two. Inner products are linear in their second variable. The ordinary spatial tensor norm and the interior tensor construction are proved below in Lemmas 3.0a and 6.0a. For the foundational C\*-algebra facts, the earlier programme lesson [continuous functional calculus, homomorphisms, positive cones and quotients](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html) supplies Theorems 4.2 and 4.4 (contractivity and faithful isometry), Theorem 5.1 (functional calculus), and Proposition 8.5 (positive order). The ordinary Hilbert-module and operator foundations are proved in [Ordinary Hilbert C\*-module foundations](supporting/hilbert-c-star-modules-and-morita-equivalence/hilbert-module-foundations.html#mf-001), MF.1–MF.7: coefficient-order Cauchy–Schwarz and completion in MF.2–MF.3, bounded adjoints and the operator C\*-algebra in MF.4–MF.5, finite Gram positivity in MF.6, and rank-one bounds in MF.7. The spatial proof uses Hahn–Banach, whose earlier programme proofs are Theorems 2.1–2.2 and Corollary 6.4 of [Hahn–Banach, Baire, and the basic theorems on Banach spaces](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html). These inputs establish the elementary operator tools. The operator-range argument in Lemma 2.1 of *Ext groups, absorption and Brown–Douglas–Fillmore theory* will be used with its grading checked explicitly. Clifford generators here are self-adjoint and square to \(+1\).

## 1. Gradings and signs

A graded C\*-algebra is a pair \((A,\alpha)\), where \(\alpha\) is a \*-automorphism and \(\alpha^2=1\). The identity automorphism is allowed. Its homogeneous subspaces are
\[
\begin{aligned}
A^r&=\{a:\alpha(a)=(-1)^ra\},\\
a^r&=\tfrac12(a+(-1)^r\alpha(a)).
\end{aligned}
\tag{1.1}
\]
Thus \(A=A^0\oplus A^1\) as a Banach space, \((A^r)^*=A^r\), and \(A^rA^s\subset A^{r+s}\). A nonzero element of \(A^r\) has degree \(|a|=r\). Statements about homogeneous zero elements mean the corresponding multilinear identity in the declared degrees.

The grading is **inner** if a self-adjoint unitary \(g\in M(A)\) satisfies \(\alpha(a)=gag\). Blackadar calls this an evenly graded algebra. The multiplier \(g\) is even: its induced grading fixes it. The trivial grading is inner, implemented by \(1_{M(A)}\). An inner grading need not be trivial.

For homogeneous elements put
\[
\left[a,b\right]_{\mathrm{gr}}
=ab-(-1)^{|a||b|}ba.
\tag{1.2}
\]
This is a commutator if either entry is even, and an anticommutator if both are odd. In particular \([a,a]_{\mathrm{gr}}=2a^2\) for odd \(a\), which is positive when \(a=a^*\).

### Proposition 1.1. The graded commutator identities

For homogeneous \(x,y,z\), of respective degrees \(p,q,r\),
\[
\begin{gathered}
\left[x,y\right]_{\mathrm{gr}}=-(-1)^{pq}[y,x]_{\mathrm{gr}},\\
[x,yz]_{\mathrm{gr}}=[x,y]_{\mathrm{gr}}z\\
+(-1)^{pq}y[x,z]_{\mathrm{gr}},\\
(-1)^{pr}[[x,y]_{\mathrm{gr}},z]_{\mathrm{gr}}\\
+(-1)^{pq}[[y,z]_{\mathrm{gr}},x]_{\mathrm{gr}}\\
+(-1)^{qr}[[z,x]_{\mathrm{gr}},y]_{\mathrm{gr}}=0.
\end{gathered}
\tag{1.3}
\]

**Proof.** The first formula follows by exchanging the two terms. In the second formula the two occurrences of \(yxz\) cancel, leaving \(xyz-(-1)^{p(q+r)}yzx\). For the last formula expand its three summands:
\[
\begin{gathered}
(-1)^{pr}xyz-(-1)^{pr+pq}yxz\\
-(-1)^{qr}zxy+(-1)^{qr+pq}zyx,\\
(-1)^{pq}yzx-(-1)^{pq+qr}zyx\\
-(-1)^{pr}xyz+(-1)^{pr+qr}xzy,\\
(-1)^{qr}zxy-(-1)^{qr+pr}xzy\\
-(-1)^{pq}yzx+(-1)^{pq+pr}yxz.
\end{gathered}
\]
Every word appears twice with opposite coefficients. \(\square\)

For \(M_2(\mathbb C)\), conjugation by \(\operatorname{diag}(1,-1)\) makes diagonal matrices even and off-diagonal matrices odd. For \(\mathbb C\oplus\mathbb C\), the swap \((a,b)\mapsto(b,a)\) makes \((a,a)\) even and \((a,-a)\) odd. This second grading is not inner: every inner automorphism of a commutative algebra is trivial.

## 2. Graded modules and their operators

### Lemma 2.0. Compact module operators and their multipliers

For every Hilbert \(B\)-module \(E\), the rank-one span has an essential closed ideal \(K=\mathcal K(E)\) in \(\mathcal L(E)\), with dense action on \(E\). One has
\[
\mathcal L(E)=M(K).
\]
The module is countably generated exactly when \(K\) is \(\sigma\)-unital. On bounded families of adjointable operators, strict convergence means convergence on every vector for both the operator and its adjoint. Every bounded strict Cauchy net has an adjointable limit. Finally, a nondegenerate representation \(\rho:K\to\mathcal L(Y)\) extends uniquely to a unital representation of \(M(K)\), continuously for bounded strict convergence.

**Proof of the compact ideal.** The adjoint and composition formulas are
\[
\begin{gathered}
\theta_{x,y}^*=\theta_{y,x},\\
T\theta_{x,y}=\theta_{Tx,y},\qquad
\theta_{x,y}T=\theta_{x,T^*y}.
\end{gathered}
\]
They follow by substituting the inner-product definition. Thus the rank-one span and its closure are two-sided \*-ideals. The map \(R_x:B\to E\), \(b\mapsto xb\), has adjoint \(R_x^*z=\langle x,z\rangle\), so \(\theta_{x,x}=R_xR_x^*\) is positive. If \(a=\langle x,x\rangle\), evaluation at \(x\) gives
\[
\|\theta_{x,x}x\|^2=\|a^3\|=\|x\|^6.
\]
Together with the Cauchy–Schwarz upper bound this proves \(\|\theta_{x,x}\|=\|x\|^2\). If \(TK=0\), then \(T\theta_{x,Tx}=\theta_{Tx,Tx}=0\), so \(T=0\). An ideal disjoint from \(K\) annihilates it and is consequently zero. This proves essentiality.

The vector \(xa(a+\epsilon)^{-1}\) belongs to \(KE\), because it is \(\theta_{x,x}(x(a+\epsilon)^{-1})\). Inverses here act through the scalar unitization of the coefficient. Its squared distance from \(x\) is at most
\[
\sup_{s\geq0}\frac{s\epsilon^2}{(s+\epsilon)^2}=\epsilon/4.
\]
Thus \(KE\) has dense span. A contractive approximate identity \(e_\lambda\) of \(K\) converges to the identity on that span, then on all vectors by uniform boundedness.

**Proof of the multiplier identification.** Lesson 01 constructs the double-centralizer algebra \(M(K)\). Each \(T\in\mathcal L(E)\) gives its two actions on the ideal \(K\), and essentiality makes this homomorphism injective. Conversely, let \(m=(L,R)\) be a bounded double centralizer. Define on the dense span of \(KE\)
\[
T_m\Bigl(\sum_jk_jx_j\Bigr)=\sum_jL(k_j)x_j.
\]
This is well-defined and bounded: its right side is the vector limit of \(L(e_\lambda)\sum_jk_jx_j\), since \(L(e_\lambda)k_j=L(e_\lambda k_j)\). Its norm is at most \(\|m\|\|\sum_jk_jx_j\|\). The same construction for \(m^*\), using
\[
L(k)^*l=k^*L^{\#}(l),
\]
gives \(\langle T_m(kx),ly\rangle=\langle kx,T_{m^*}(ly)\rangle\). Density proves adjointability and \(T_m^*=T_{m^*}\). Finally \(T_mk=L(k)\), and on vectors \(lx\) one has \(kT_m(lx)=kL(l)x=R(k)lx\). Thus both multiplier actions are the prescribed ones, proving surjectivity and the identification.

**Proof of the countability assertion.** If \(x_j\) generate \(E\), rescale so \(\|x_j\|\leq1\), and put
\[
\begin{gathered}
h=\sum_{j\geq1}2^{-j}\theta_{x_j,x_j},\\
e_n=h(h+n^{-1})^{-1},\qquad r_n=1-e_n.
\end{gathered}
\]
The series converges in \(K\). Positivity and the rank-one norm formula give
\[
\begin{aligned}
\|r_nx_j\|^2
&=\|r_n\theta_{x_j,x_j}r_n\|\\
&\leq2^j\|r_nhr_n\|\leq2^j/(4n).
\end{aligned}
\]
Hence \(e_n\) converges on all generating vectors and therefore on all of \(E\). The rank-one composition formulas make \(e_n\) a two-sided approximate identity of \(K\). Conversely, approximate a sequential approximate identity of \(K\) by finite rank-one sums \(f_n\), within \(1/n\). Then \(f_nx\to x\); the countable set of first vectors in these sums generates \(E\). For a graded module take the homogeneous components of the generators and rank-one sums. The resulting \(h,e_n\) can be chosen even. The zero module satisfies the same assertions.

**Proof of the strict assertions.** If \(T_i,T_i^*\) converge on every vector and are uniformly bounded, the rank-one formulas imply convergence of \(T_ik\) and \(kT_i\) for every \(k\in K\). Approximation by rank-one sums uses the common bound. Conversely, strict convergence gives vector convergence on \(KE\), then on \(E\) by density and the common bound; apply it also to the adjoint net. A bounded strict Cauchy net therefore has vector limits \(T\) and \(S\) for its operator and adjoint. Passing to limits in the inner-product identity gives \(T^*=S\), so its limit is adjointable and is the strict limit just described. This also proves strict convergence of the bounded positive sums used later, whenever their products on the dense compact-action span are Cauchy.

**Proof of the representation extension.** Nondegeneracy means that the span of \(\rho(K)Y\) is dense. On that span set
\[
\widetilde\rho(m)\Bigl(\sum_j\rho(k_j)y_j\Bigr)
=\sum_j\rho(mk_j)y_j.
\]
This vector is the limit of \(\rho(me_\lambda)\sum_j\rho(k_j)y_j\). These operators have norm at most \(\|m\|\), so the formula is independent of the expression and extends boundedly. The construction for \(m^*\) supplies the adjoint, by the same double-centralizer inner-product calculation. Products agree on the dense span, and the unit acts as the identity; thus this is a unital \*-homomorphism. Its products with \(\rho(k)\) determine it on that span, proving uniqueness. Bounded strict convergence of the multipliers gives vector and adjoint-vector convergence on this span and then on every vector, hence strict convergence on \(\mathcal K(Y)\). No faithfulness of \(\rho\), fullness, separability or \(\sigma\)-unitality of the coefficients was needed. \(\square\)

The actual free comparisons are Blackadar's author-posted *K-Theory for Operator Algebras*, Sections 13.1–13.2, and his revised *Operator Algebras* notes, Sections II.7.2–II.7.3. References inside those works are not imported as proofs: all assertions needed here have been established above using Lesson 01 and the earlier C\*-algebra and adjointable-operator foundations.


A grading on a Hilbert \(B\)-module \(E\), over \((B,\beta)\), is a complex-linear isometric involution \(\gamma_E\) such that
\[
\begin{aligned}
\gamma_E(xb)&=\gamma_E(x)\beta(b),\\
\langle\gamma_E x,\gamma_E y\rangle
 &=\beta(\langle x,y\rangle).
\end{aligned}
\tag{2.1}
\]
Its eigenspaces \(E^0,E^1\) satisfy
\[
\begin{gathered}
E^pB^q\subset E^{p+q},\\
\langle E^p,E^q\rangle\subset B^{p+q}.
\end{gathered}
\tag{2.2}
\]
Conversely these properties for a closed direct-sum decomposition give (2.1).

The involution \(\gamma_E\) is generally semilinear over \(B\), rather than \(B\)-linear. Its eigenspaces need not be Hilbert \(B\)-submodules. For example, take \(E=B=\mathbb C\oplus\mathbb C\) with swap grading; multiplying the even vector \((1,1)\) by the odd coefficient \((1,-1)\) produces an odd vector. When \(B\) is trivially graded, \(\gamma_E\) is a self-adjoint unitary in \(\mathcal L(E)\), and its two eigenspaces are orthogonal Hilbert submodules.

### Proposition 2.1. Induced operator gradings

The map
\[
\alpha_E(T)=\gamma_E T\gamma_E
\tag{2.3}
\]
grades \(\mathcal L(E)\) and preserves \(\mathcal K(E)\). For homogeneous vectors,
\[
\begin{gathered}
|\theta_{x,y}|=|x|+|y|,\\
\theta_{x,y}(z)=x\langle y,z\rangle.
\end{gathered}
\tag{2.4}
\]
A homogeneous adjointable operator \(T\) of degree \(r\) maps \(E^p\) into \(E^{p+r}\).

**Proof.** Twice using semilinearity gives
\(\gamma_E T\gamma_E(xb)=(\gamma_E T\gamma_E x)b\), so (2.3) is \(B\)-linear. Apply \(\beta\) to the adjoint identity for \(T\), with arguments \(\gamma_E x,\gamma_E y\), to obtain
\(\langle\gamma_E T\gamma_E x,y\rangle
=\langle x,\gamma_E T^*\gamma_E y\rangle\).
Thus (2.3) preserves adjoints; composition and the involution identity are immediate. Moreover
\[
\gamma_E\theta_{x,y}\gamma_E
=\theta_{\gamma_E x,\gamma_E y}.
\]
For homogeneous \(x,y\), their two signs multiply, proving (2.4). Finite-rank spans and their norm closure are preserved. Finally
\(\gamma_ET=(-1)^rT\gamma_E\) is precisely the stated degree-shift condition. \(\square\)

A graded representation is a \*-homomorphism
\(\pi:(A,\alpha)\to(\mathcal L(E),\alpha_E)\) satisfying
\(\pi(\alpha(a))=\alpha_E(\pi(a))\). Over trivially graded \(B\), even elements act diagonally on \(E^0\oplus E^1\), and odd elements act off-diagonally. This is the convention used for an even Kasparov module.

Write \(E^{\mathrm{op}}\) for the same underlying module with grading \(-\gamma_E\). This reverses vector degrees but leaves the induced grading on \(\mathcal L(E)\) unchanged. The standard module and its balanced graded version are
\[
\begin{gathered}
H_B=\ell^2(\mathbb N)\otimes B,\\
\gamma_{H_B}((b_j))=(\beta(b_j)),\\
\widehat H_B=H_B\oplus H_B^{\mathrm{op}}.
\end{gathered}
\tag{2.5}
\]
Coordinate descriptions do not require a unit of \(B\); a symbol for a coordinate denotes a copy of \(B\), not a vector containing a nonexistent unit.

## 3. The graded tensor product

On the vector space \(A\odot B\), define, for homogeneous entries,
\[
\begin{gathered}
(a\widehat\otimes b)(a'\widehat\otimes b')\\
=(-1)^{|b||a'|}aa'\widehat\otimes bb',\\
(a\widehat\otimes b)^*\\
=(-1)^{|a||b|}a^*\widehat\otimes b^*.
\end{gathered}
\tag{3.1}
\]
The degree is \(|a|+|b|\). These formulas are extended linearly. In a triple product the total sign is
\(|b||a'|+|b||a''|+|b'||a''|\), independent of the placement of parentheses. For the involution, reversing two factors introduces exactly the signs in the second formula together with the reversed multiplication sign. Thus (3.1) is an associative \*-algebra.

### Lemma 3.0a. The ordinary spatial norm

For arbitrary C\*-algebras \(A,B\), the formula
\[
\|z\|_{\min}=\sup_{\pi,\rho}\|(\pi\odot\rho)(z)\|,
\qquad z\in A\odot B,
\]
where the supremum runs over Hilbert-space representations of the two factors, is a C\*-norm. Any pair of faithful representations gives this same norm. Tensoring homomorphisms is contractive; tensoring injective homomorphisms is isometric. The ordinary flip and rebracketing are isometric. No countability, units, or nuclearity are assumed.

**Proof.** First construct the Hilbert-space tensor product. Rewrite a finite tensor sum using an orthonormal basis \(e_j\) of the finite-dimensional span of its first entries as \(\sum_j e_j\otimes\eta_j\). The product inner product gives squared norm \(\sum_j\|\eta_j\|^2\), and hence is positive definite on the algebraic tensor product. Completing gives \(H\otimes K\). Expansion in an orthonormal basis of the second entries proves \(\|T\otimes1\|\leq\|T\|\); the corresponding expansion in the first entries proves \(\|1\otimes S\|\leq\|S\|\). Thus \(T\otimes S\) is bounded, has adjoint \(T^*\otimes S^*\), and has norm \(\|T\|\|S\|\), the reverse inequality following from unit product vectors approaching the two operator norms. The algebraic flip and rebracketing preserve these inner products and have dense range, so extend to unitaries.

We recall explicitly why faithful representations exist. In the unitization, a nonzero positive element \(c\) has a state on \(C^*(1,c)\) taking value \(\|c\|\) on \(c\), by evaluation at the maximal spectral value. Hahn–Banach extends this functional with norm one and value one at the identity. Such an extension is positive: for self-adjoint \(h\), expanding \(f(e^{ith})\) at \(t=0\) and using \(|f(e^{ith})|\leq1\) shows that \(f(h)\) is real; for \(0\leq h\leq1\), the bound \(|1-f(h)|\leq\|1-h\|\leq1\) then gives \(f(h)\geq0\). Scaling proves positivity in general. For a state \(f\), set \(\langle[x],[y]\rangle=f(x^*y)\). Nonnegativity of \(f((x+ty)^*(x+ty))\), minimized over complex \(t\), gives Cauchy–Schwarz (with a positive \(\varepsilon\) added to the denominator if \(f(y^*y)=0\)). Null vectors are therefore orthogonal to everything and the quotient is an inner-product space. Left multiplication respects the null space and is bounded because
\[
f(x^*a^*ax)\leq\|a\|^2f(x^*x),
\]
and its adjoint is left multiplication by \(a^*\). This is a representation with cyclic vector the class of \(1\). The direct sum over states separates all positive elements, hence is faithful. Restricting to the nondegenerate part of the original algebra preserves faithfulness. The functional calculus, order, and C\*-homomorphism facts in this argument have the earlier programme proofs named in the introduction.

For \(z=\sum_i a_i\otimes b_i\), every product representation has norm at most \(\sum_i\|a_i\|\|b_i\|\). The supremum is therefore finite, is submultiplicative, preserves involution, and satisfies
\[
\|z^*z\|_{\min}=\sup_{\pi,\rho}\|(\pi\odot\rho)(z)\|^2
=\|z\|_{\min}^2.
\]
It is a norm: if the factors are represented faithfully, their product representation is algebraically injective. Indeed vector functionals separate operators, and their restrictions span the dual of any finite-dimensional operator subspace. Applying product vector functionals to an image of \(z\) that is zero therefore recovers every algebraic tensor coefficient. This proves \(z=0\).

It remains to prove that one faithful pair realizes the supremum. Discard the zero representation parts, and extend representations canonically to unitizations; for an already unital algebra use its existing identity. A faithful nondegenerate representation of a nonunital algebra has a faithful extension: if \(\pi(a)+\lambda I=0\) with \(\lambda\ne0\), faithfulness would make \(-a/\lambda\) an identity of the original algebra. We can therefore prove the assertion in the unital case.

For a faithful unital representation \(\pi:A\to\mathcal B(H)\), the convex hull of its unit vector states is weak-* dense in the state space of \(A\). Otherwise real Hahn–Banach separation gives a self-adjoint \(h\in A\) and a state \(f\) with
\[
f(h)>\sup_{\|\xi\|=1}\langle\xi,\pi(h)\xi\rangle.
\]
The right side is the maximal spectral value of \(h\): faithfulness preserves spectrum and order, and a smaller upper bound would contradict the least scalar upper bound for the self-adjoint operator. Positivity gives \(f(h)\) at most that same spectral value, a contradiction. Here weak-* separation is evaluation at a self-adjoint element because a continuous real linear functional involves only finitely many evaluations.

Fix a faithful pair \(\pi,\rho\) and put \(c=\|(\pi\odot\rho)(z)\|\). For \(w\in A\odot B\), the operator inequality in this representation gives
\[
(f_\xi\otimes g_\eta)(w^*z^*zw)
\leq c^2(f_\xi\otimes g_\eta)(w^*w)
\]
for its unit vector states. This holds for finite convex combinations of each family, and then for all states \(f,g\) by weak-* approximation: the two expressions are finite sums of products of evaluations. In the product of their cyclic GNS representations, vectors of the form \(w(\xi_f\otimes\xi_g)\) are dense, and their squared norms and squared image norms are exactly these two expressions. The inequality thus bounds that product representation of \(z\) by \(c\).

Every nondegenerate representation is a direct sum of cyclic representations: choose a maximal orthogonal family of cyclic invariant subspaces; their orthogonal complement is invariant and, if nonzero, supplies another cyclic subspace. Each normalized cyclic vector defines a state and the isometric map from its GNS space onto the cyclic subspace. The product of two such sums is the sum of the product cyclic representations, first on algebraic vectors and then by completion. Hence all pairs have norm at most \(c\). The reverse bound is part of the supremum, proving independence.

Composing representations with homomorphisms proves contractivity of the tensor map. For inclusions, restrict faithful representations of the larger factors to the smaller ones and their nondegenerate parts; they remain faithful, so independence proves isometry. The Hilbert-space flip and rebracketing unitaries, applied to faithful pairs and triples, give the asserted algebra isometries. The same proof identifies \(M_n(A)\) with \(M_n(\mathbb C)\otimes_{\min}A\). Completing the algebraic tensor product now gives \(A\otimes_{\min}B\). If a factor is zero, all the assertions reduce to the zero algebra. \(\square\)

We give a concrete C\*-norm rather than leaving positivity of the graded construction implicit. Set \(D=A\otimes_{\min}B\), the ordinary spatial tensor product, and \(s=\alpha\otimes1\). For \(d\in A\odot B\), write \(d=d_0+d_1\), according to the degree of its \(B\)-factor. Define
\[
\begin{gathered}
\iota(d)=
\begin{pmatrix}
d_0&d_1\\ s(d_1)&s(d_0)
\end{pmatrix}
\\\in M_2(D).
\end{gathered}
\tag{3.2}
\]

### Lemma 3.1. A faithful C\*-completion

Formula (3.2) is an injective \*-homomorphism for (3.1). Its image has a closed completion inside \(M_2(D)\). The induced norm is the minimal graded tensor norm.

**Proof.** In multiplier notation put
\[
\lambda(a)=\operatorname{diag}(a,\alpha(a)),\qquad
u=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Then \(u\lambda(a)=\lambda(\alpha(a))u\), and
\(\iota(a\widehat\otimes b)=\lambda(a)u^{|b|}\otimes b\).
Moving \(u^{|b|}\) across \(\lambda(a')\) gives the multiplication sign in (3.1). Taking its adjoint gives the involution sign. Its top row recovers \(d_0,d_1\), so it is injective.

The parity projections \(d\mapsto d_r\) extend as contractions on \(D\), since \(1\otimes\beta\) is an isometric involution. Consequently
\[
\tfrac12\|d\|_D\leq\|\iota(d)\|\leq2\|d\|_D.
\tag{3.3}
\]
For the lower bound, use \(\|d_r\|\leq\|\iota(d)\|\); for the upper bound, each diagonal or off-diagonal matrix has norm \(\|d_r\|\). Hence the image extends to a closed linear image of \(D\). It is a C\*-subalgebra by the already checked product and adjoint rules.

To identify the spatial norm, choose faithful nondegenerate graded Hilbert-space representations \((\pi_A,H_A,\Gamma_A)\) and \((\pi_B,H_B',\Gamma_B)\). Here the primes distinguish this Hilbert space from a standard coefficient module. Such representations exist: from an ordinary faithful nondegenerate \(\pi\), use \(\pi\oplus\pi\alpha\) with the swapping grading operator. The spatial graded representation is
\[
\Pi(a\widehat\otimes b)
=\pi_A(a)\Gamma_A^{|b|}\otimes\pi_B(b).
\tag{3.4}
\]
It has precisely the signs (3.1).

Represent (3.2) faithfully on \((H_A\oplus H_A)\otimes H_B'\). Conjugation by \(\operatorname{diag}(1,\Gamma_A)\) makes the two copies of \(\lambda(a)\) equal to \(\pi_A(a)\), and turns \(u\) into
\(\begin{pmatrix}0&\Gamma_A\\\Gamma_A&0\end{pmatrix}\).
The scalar Hadamard unitary then splits this representation into (3.4) and the same formula with an additional \((-1)^{|b|}\). Conjugating the second summand by \(1\otimes\Gamma_B\) removes that additional sign. Thus its norm equals the norm of (3.4). In particular (3.4) is faithful and its norm is independent of the faithful graded representations chosen. This is the minimal spatial graded completion. \(\square\)

We denote it \(A\widehat\otimes B\). Its grading is \(\alpha\widehat\otimes\beta\), implemented in (3.4) by \(\Gamma_A\otimes\Gamma_B\).

One can instead complete in the largest norm obtained from pairs of representations whose homogeneous images supercommute. This is \(A\widehat\otimes_{\max}B\). The norm exists: (3.4) is a faithful candidate, and any such pair bounds the norm of a finite sum by the sum of the products of the factor norms. We specify the minimal norm unless a maximal subscript is present.

### Theorem 3.2. Associativity and the graded flip

Rebracketing and the signed flip give graded isomorphisms
\[
\begin{aligned}
(A\widehat\otimes B)\widehat\otimes C
 &\cong A\widehat\otimes(B\widehat\otimes C),\\
\tau(a\widehat\otimes b)
 &=(-1)^{|a||b|}b\widehat\otimes a.
\end{aligned}
\tag{3.5}
\]
The same statements hold for maximal completions.

**Proof.** Use faithful graded representations of all three factors. For homogeneous \(a,b,c\), both bracketings act, after the ordinary Hilbert-space rebracketing unitary, by
\[
\pi_A(a)\Gamma_A^{|b|+|c|}
\otimes\pi_B(b)\Gamma_B^{|c|}
\otimes\pi_C(c).
\tag{3.6}
\]
Lemma 3.1 makes both representations faithful, proving equality of the two norms. The algebraic rebracketing therefore extends to the asserted isomorphism.

For the flip, define a unitary on homogeneous vectors by
\[
U(\xi\otimes\eta)=(-1)^{|\xi||\eta|}\eta\otimes\xi.
\]
On vectors of degrees \(r,s\), conjugating (3.4) gives the operator associated to
\((-1)^{pq}b\widehat\otimes a\), where \(p=|a|,q=|b|\): the total sign is \(pq+ps\). This is the sign from its scalar prefactor and the graded action in the new order. Thus the flip preserves the faithful spatial norm. Formula (3.1) verifies its product and adjoint identities, and applying it twice gives the identity.

For maximal completions, a representation of either bracketing is a triple of representations with pairwise supercommuting homogeneous images. Indeed the first two extend uniquely to their maximal product and then supercommute with the third, and conversely restriction recovers that triple. The two universal norms consequently coincide. Exchanging the first two representations with the sign in (3.5) gives the maximal flip. \(\square\)

The sign in the involution matters. The tensor of two self-adjoint odd elements is skew-adjoint; multiplying it by \(i\) gives a self-adjoint element.

## 4. Removing an inner grading from the product

### Theorem 4.1. The inner-grading isomorphism

If \(\alpha=\operatorname{Ad}g\), with \(g\in M(A)\) a self-adjoint unitary, then
\[
\begin{gathered}
\Phi:A\widehat\otimes B\longrightarrow A\otimes_{\min}B,
\\
\Phi(a\widehat\otimes b)=ag^{|b|}\otimes b
\end{gathered}
\tag{4.1}
\]
is a \*-isomorphism. On the right the grading is \(\alpha\otimes\beta\). If \(\beta=\operatorname{Ad}h\) is also inner, it is implemented by \(g\otimes h\). Formula (4.1) also identifies the maximal graded and ordinary maximal tensor products.

**Proof.** Since \(ga'=(-1)^{|a'|}a'g\),
\[
(ag^q)(a'g^{q'})
=(-1)^{q|a'|}aa'g^{q+q'}.
\]
This verifies multiplication. The identity
\((ag^q)^*=(-1)^{|a|q}a^*g^q\)
verifies the involution. The same linear formula gives the inverse, because \(g^2=1\) and \(g\) is even.

For the norm, choose faithful nondegenerate graded representations as in Lemma 3.1, and extend \(\pi_A\) to multipliers. Put \(g_A=\pi_A(g)\) and \(c=\Gamma_Ag_A\). Both \(g_A\) and \(\Gamma_A\) implement \(\alpha\), so \(c\) commutes with \(\pi_A(A)\). They commute with each other, since \(g\) is even; hence \(c\) is a self-adjoint unitary. Let \(P_\pm=(1\pm c)/2\). The unitary
\[
W=P_+\otimes1+P_-\otimes\Gamma_B
\]
conjugates (3.4) into
\(\pi_A(a)g_A^{|b|}\otimes\pi_B(b)\).
On the negative eigenspace of \(c\), the sign from \(\Gamma_A=cg_A\) is canceled by conjugation with \(\Gamma_B\). The resulting representation is the faithful ordinary spatial representation of (4.1). Thus \(\Phi\) is isometric.

The grading assertion follows by applying \(\alpha\otimes\beta\) to the formula, using \(\alpha(g)=g\).

For the maximal assertion, take a nondegenerate supercommuting pair \(\pi,\rho\). The extended multiplier \(\pi(g)\) commutes with \(\rho(B)\): approximate \(g\) strictly by \(ge_i\), where \(e_i\) is an even approximate identity of \(A\), and use that these are even. Replacing \(\rho(b)\) by \(\pi(g)^{|b|}\rho(b)\) produces an ordinary representation of \(B\) commuting with \(\pi(A)\). Its multiplicativity and adjoint identities use the fact that \(\pi(g)\) commutes with \(\rho(B)\). Conversely an ordinary commuting pair yields a supercommuting pair by the same replacement. Degenerate representations can be restricted to the essential subspace of \(\pi(A)\); the complementary subspace contributes zero to the product. The universal norms are therefore identified. \(\square\)

This is an isomorphism of the underlying C\*-algebras with the specified grading on the ordinary product; it does not discard parity information.

For example, if \(A\) is inner graded and \(M_2\) has its diagonal grading, the product first becomes \(M_2(A)\) with grading operator \(\operatorname{diag}(g,-g)\). Write \(p_\pm=(1\pm g)/2\). The multiplier matrix
\[
\begin{gathered}
V=\begin{pmatrix}p_+&p_-\\p_-&p_+\end{pmatrix},
\\
V\operatorname{diag}(g,-g)V^*=\operatorname{diag}(1,-1),
\end{gathered}
\tag{4.2}
\]
is a self-adjoint unitary. The equality follows separately on the two eigenspaces of \(g\): it is the identity on the first and exchanges the two coordinates on the second. Thus the product is isomorphic to \(M_2(A)\) with the standard diagonal grading.

## 5. Complex Clifford algebras

For a real Euclidean space \(V\), the complex Clifford algebra \(\mathrm{Cl}(V)\) is the universal unital C\*-algebra with a real-linear map \(c:V\to\mathrm{Cl}(V)\) such that
\[
\begin{gathered}
c(v)^*=c(v),\\
c(v)c(w)\\+c(w)c(v)=2(v,w)1.
\end{gathered}
\tag{5.1}
\]
The grading sends \(c(v)\) to \(-c(v)\). For an orthonormal basis of \(\mathbb R^n\), write \(C_n=\mathrm{Cl}(\mathbb R^n)\) and \(e_j=c(v_j)\). Its generators are odd self-adjoint anticommuting unitaries. Put \(C_0=\mathbb C\) with trivial grading.

The universal construction exists because the relations have Hilbert-space representations, constructed below, and any word reduces to a scalar multiple of
\[
e_{i_1}\cdots e_{i_r},\qquad
i_1<\cdots<i_r.
\tag{5.2}
\]
There are \(2^n\) such words. Their universal representation norms are bounded by one, so the universal norm of any linear combination is bounded by the sum of the absolute coefficients.

Use the Pauli matrices
\[
\begin{aligned}
\sigma_1&=\begin{pmatrix}0&1\\1&0\end{pmatrix},\\
\sigma_2&=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\\
\sigma_3&=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\end{aligned}
\tag{5.3}
\]
They are self-adjoint unitaries, anticommute pairwise, and satisfy \(\sigma_1\sigma_2=i\sigma_3\).

### Theorem 5.1. The Clifford algebra computation

As graded C\*-algebras,
\[
\begin{gathered}
C_1\\\cong\mathbb C\oplus\mathbb C\\
\text{with swap grading},\\
C_{2k}\\\cong M_{2^k}(\mathbb C)\\
\text{with grading }\operatorname{Ad}\Gamma_k,\\
C_{2k+1}\\\cong M_{2^k}(\mathbb C)\oplus M_{2^k}(\mathbb C)\\
\text{with swap grading},
\end{gathered}
\tag{5.4}
\]
where \(\Gamma_k=\sigma_3^{\otimes k}\). For \(k\geq1\), its positive and negative eigenspaces both have dimension \(2^{k-1}\).

**Proof.** The normal forms in (5.2) bound the dimension by \(2^n\). We construct a quotient of exactly that dimension, which simultaneously proves that all normal forms are independent.

In dimension one, evaluate the generator at \(+1\) and \(-1\). The images of \(1,e_1\) form a basis of \(\mathbb C\oplus\mathbb C\), so the dimension bound makes this map an isomorphism. Negating the generator swaps the two evaluations.

For \(n=2k\), work on \(S_k=(\mathbb C^2)^{\otimes k}\), and set
\[
\begin{aligned}
c_{2j-1}&=\sigma_3^{\otimes(j-1)}\otimes\sigma_1\otimes1^{\otimes(k-j)},\\
c_{2j}&=\sigma_3^{\otimes(j-1)}\otimes\sigma_2\otimes1^{\otimes(k-j)}.
\end{aligned}
\tag{5.5}
\]
Each is a self-adjoint unitary. Two in the same slot anticommute. For two in distinct slots, the earlier non-diagonal Pauli factor meets exactly one \(\sigma_3\) in the later operator; that is the only negative interchange. Thus all Clifford relations hold. Adjacent products recover the diagonal operator in each slot:
\[
\begin{gathered}
-ic_{2j-1}c_{2j}\\=1^{\otimes(j-1)}\otimes\sigma_3\otimes1^{\otimes(k-j)}.
\end{gathered}
\tag{5.6}
\]
Multiplying by these diagonal operators in earlier slots isolates \(\sigma_1\) and \(\sigma_2\) in slot \(j\). Together with \(1,\sigma_3\), they span the full \(M_2\) there. Their slot products consequently span every tensor of matrix units, so the representation is onto \(\operatorname{End}(S_k)\). The latter has dimension \(2^{2k}\); the normal-form bound proves injectivity. Its grading is conjugation by \(\Gamma_k=\sigma_3^{\otimes k}\), since this negates every displayed generator. Among the \(2^k\) tensor-basis vectors, flipping the first factor pairs opposite grading eigenvalues, proving the equal multiplicities for \(k\geq1\).

For \(n=2k+1\), use the elements
\[
\begin{gathered}
\omega_k=(-i)^ke_1\cdots e_{2k},\\
 w=\omega_ke_{2k+1}.
\end{gathered}
\tag{5.7}
\]
Reversing \(2k\) generators introduces \((-1)^k\), exactly the factor needed for \(\omega_k^*=\omega_k\) and \(\omega_k^2=1\). It anticommutes with each of the first \(2k\) generators and commutes with the last, so \(w\) is a central odd self-adjoint unitary. Extend (5.5) in two ways by sending the last generator to \(+\Gamma_k\) and \(-\Gamma_k\). In both, (5.6) gives \(\omega_k=\Gamma_k\); hence \(w\) takes the values \(+1\) and \(-1\). The central projections \((1\pm w)/2\) isolate the two matrix summands. Each summand contains the full matrix algebra already generated by (5.5), making the combined representation onto \(M_{2^k}\oplus M_{2^k}\). Its dimension \(2^{2k+1}\) attains the normal-form bound, so it is faithful.

Negating every generator acts in these coordinates as
\[
(X,Y)\longmapsto(\Gamma_kY\Gamma_k,\Gamma_kX\Gamma_k).
\tag{5.8}
\]
Checking the first \(2k\) generators uses their anticommutation with \(\Gamma_k\); checking the last uses the exchange of its two opposite values. Conjugating the second coordinate by \(\Gamma_k\) changes this grading to pure swap. The argument includes \(k=0\), with an empty tensor product and \(\Gamma_0=1\). \(\square\)

### Corollary 5.2. Clifford tensor products

The generators from the two factors give
\[
\begin{gathered}
C_p\widehat\otimes C_q\cong C_{p+q},
\\
C_1\widehat\otimes C_1\cong(M_2,\operatorname{Ad}\sigma_3).
\end{gathered}
\tag{5.9}
\]
These identities hold for both minimal and maximal graded products. Consequently \(C_{n+2}\cong C_n\widehat\otimes C_2\).

**Proof.** The two copies of the generators in the product are odd self-adjoint unitaries. The multiplication rule (3.1) makes generators from different factors anticommute, so they define a surjective graded homomorphism from \(C_{p+q}\). The minimal product has vector-space dimension \(2^p2^q=2^{p+q}\) by Lemma 3.1; the surjection is therefore injective. For the maximal product, the algebraic product already has that dimension, and its maximal norm is faithful because it dominates the minimal norm. Its completion is the same finite-dimensional \*-algebra. Finite-dimensional C\*-algebras have their unique C\*-norm, since the norm squared of an element is the spectral radius of its square modulus. Finally the \(p=q=1\) representation sends the two generators to \(\sigma_1,\sigma_2\), giving the displayed grading. \(\square\)

The self-adjoint **chirality element** in even dimension is \(\omega_k\) in (5.7). Reversing an orientation reverses its sign. More generally an orthogonal change of orthonormal basis multiplies the top word by the determinant: distinct orthogonal vectors have zero pairwise inner products, so their Clifford product is their exterior top product under the linear normal-form identification (5.2). In (5.5), chirality is exactly \(\Gamma_k\), fixing our orientation and sign convention.

For a Euclidean vector bundle \(V\to X\), each orthogonal change of frame acts on (5.1) by a graded \*-automorphism. These actions satisfy the transition cocycle, so the fibers \(\mathrm{Cl}(V_x)\) assemble into a locally trivial graded algebra bundle \(\mathrm{Cl}(V)\). The normal forms (5.2) show that its complex rank is \(2^{\operatorname{rank}V}\). For locally compact Hausdorff \(X\), continuous sections vanishing at infinity form the graded C\*-algebra \(C_0(X,\mathrm{Cl}(V))\), with supremum norm and pointwise operations. A Hermitian graded vector bundle carrying an odd Clifford action is a graded Clifford-module bundle. A global irreducible spinor bundle is additional data; its existence does not follow merely from choosing local matrix descriptions.

## 6. Interior tensor products and graded stabilization

Let \(E\) be a graded Hilbert \(A\)-module, \(F\) a graded Hilbert \(B\)-module, and \(\phi:A\to\mathcal L(F)\) a graded \*-homomorphism. Its **interior** tensor product is the ordinary Hilbert-module tensor product with
\[
\begin{gathered}
\langle x\otimes y,x'\otimes y'\rangle\\
=\langle y,\phi(\langle x,x'\rangle)y'\rangle,\\
\gamma(x\otimes y)=\gamma_E x\otimes\gamma_F y.
\end{gathered}
\tag{6.1}
\]
There is no extra sign in the inner-product formula. The left action belongs in \(\mathcal L(F)\); an action into \(B\) alone would not describe a general correspondence.

### Lemma 6.0a. Constructing the ordinary interior product

For Hilbert modules \(E_A,F_B\) and any homomorphism \(\phi:A\to\mathcal L(F)\), the first formula in (6.1) defines a positive semidefinite form on the balanced algebraic tensor product. Its null-space quotient and completion are a Hilbert \(B\)-module. Every \(T\in\mathcal L(E)\) gives an adjointable \(T\otimes1\), with norm at most \(\|T\|\) and adjoint \(T^*\otimes1\). This assignment preserves products and adjoints. For three compatible correspondences, the map \((x\otimes y)\otimes z\mapsto x\otimes(y\otimes z)\) is a unitary. Degenerate left actions and nonunital coefficient algebras are allowed.

**Proof.** Balancing respects the form because
\(\langle xa,x'\rangle=a^*\langle x,x'\rangle\),
\(\langle x,x'a\rangle=\langle x,x'\rangle a\), and \(\phi\) preserves products and adjoints. It is conjugate symmetric and right \(B\)-linear in the second variable.

The nonunital matrix inclusion, row adjoint and finite Gram positivity used next are proved in [Ordinary Hilbert C\*-module foundations, MF.6](supporting/hilbert-c-star-modules-and-morita-equivalence/hilbert-module-foundations.html#mf-006). For \(x_1,\ldots,x_n\in E\), define \(V:A^n\to E\) by \(V(a_i)=\sum_i x_ia_i\). It is bounded by the triangle inequality and has adjoint \(V^*x=(\langle x_i,x\rangle)_i\). Its Gram matrix is
\[
G=V^*V=[\langle x_i,x_j\rangle]\in M_n(A)_+.
\]
Apply the homomorphism \(\phi_n\) to obtain a positive operator on \(F^n\). For \(u=\sum_i x_i\otimes y_i\) this gives
\[
\langle u,u\rangle
=\langle (y_i),\phi_n(G)(y_i)\rangle\geq0.
\]
The same argument applied simultaneously to two finite sums shows that their two-by-two Gram matrix is positive in \(M_2(B)\). This also proves that the form descends through every balanced relation.

For completeness, a positive block matrix \(\begin{pmatrix}a&b\\b^*&d\end{pmatrix}\) in \(M_2(B)\) satisfies
\[
b^*(a+\varepsilon1)^{-1}b\leq d,
\qquad b^*b\leq(\|a\|+\varepsilon)d.
\]
The first inequality follows by multiplying the matrix, with \(\varepsilon\) added to its first corner, on both sides by the column \((-(a+\varepsilon)^{-1}b,1)\) and its adjoint. The second uses the scalar lower bound for \((a+\varepsilon)^{-1}\). Letting \(\varepsilon\downarrow0\) proves
\(\|\langle u,v\rangle\|\leq\|\langle u,u\rangle\|^{1/2}\|\langle v,v\rangle\|^{1/2}\).
Thus the form norm is a seminorm with the triangle inequality; every null vector is orthogonal to every vector. The null vectors form a submodule, since
\(\langle ub,ub\rangle=b^*\langle u,u\rangle b\).
The quotient is a pre-Hilbert module. Its completion retains the inner product and bounded right action by these inequalities.

For \(T\in\mathcal L(E)\), positivity of
\(\|T\|^2-T^*T\) gives
\[
[\langle Tx_i,Tx_j\rangle]
\leq\|T\|^2[\langle x_i,x_j\rangle],
\]
by applying \(V^*(\|T\|^2-T^*T)V\). Apply \(\phi_n\) and evaluate at \((y_i)\). The resulting inequality proves that \(T\otimes1\) respects null vectors and has norm at most \(\|T\|\). The elementary inner-product identity gives its adjoint \(T^*\otimes1\). Products, linearity, and the identity are checked on elementary tensors and extend by density.

If \(G_C\) has left action \(\psi:B\to\mathcal L(G)\), the induced left action of \(A\) on \(F\otimes_\psi G\) is \(\phi(a)\otimes1\), which has just been constructed. Both bracketings are balanced, and the inner product between two elementary threefold tensors in either bracketing is
\[
\langle z,\psi(\langle y,\phi(\langle x,x'\rangle)y'\rangle)z'\rangle.
\]
Consequently rebracketing is well defined and isometric on the null-space quotients. Elementary tensors have dense span on both sides, so its extension is a unitary. No step used nondegeneracy or a unit. \(\square\)

### Proposition 6.1. The interior grading

Formula (6.1) defines a grading on \(E\otimes_\phi F\). For homogeneous tensors its degree is \(|x|+|y|\). The map \(T\mapsto T\otimes1\) is a graded \*-homomorphism from \(\mathcal L(E)\) to \(\mathcal L(E\otimes_\phi F)\). Rebracketing three compatible correspondences preserves grading.

**Proof.** The balanced relation is respected because
\[
\begin{gathered}
\gamma_E(xa)\otimes\gamma_Fy
\\=\gamma_Ex\otimes\phi(\alpha(a))\gamma_Fy
\\=\gamma_Ex\otimes\gamma_F(\phi(a)y).
\end{gathered}
\]
The inner product of the two graded tensors in (6.1) equals
\(\beta(\langle y,\phi(\langle x,x'\rangle)y'\rangle)\), by (2.1) and the gradedness of \(\phi\). Thus the grading is isometric, respects null vectors, and extends to the completion. It is a complex-linear involution with the required coefficient semilinearity. Lemma 6.0a supplies the adjointable map \(T\otimes1\); on elementary tensors conjugation by the grading gives
\((\gamma_ET\gamma_E)\otimes1\). Finally both ways of rebracketing have grading \(\gamma_E\otimes\gamma_F\otimes\gamma_G\), and the rebracketing unitary constructed in Lemma 6.0a therefore preserves it. \(\square\)

### Theorem 6.2. Graded stabilization

Let \(B\) be any graded C\*-algebra and \(E\) a countably generated graded Hilbert \(B\)-module. There is a degree-zero adjointable unitary
\[
E\oplus\widehat H_B\cong\widehat H_B.
\tag{6.2}
\]
No unitality or \(\sigma\)-unitality hypothesis on \(B\) is needed.

**Proof.** Split a countable generating family into its even and odd components. The resulting homogeneous family still generates: the span of the original generators times \(B\) lies in the span of the components times \(B\). Rescale its nonzero members to contractions. For a homogeneous generator \(\eta_j\) of degree \(p_j\), put
\[
X_j=H_B^{[p_j]},\qquad
R_j((b_m))=\eta_jb_1,
\tag{6.3}
\]
where the bracket means use the natural grading if \(p_j=0\) and its opposite if \(p_j=1\). This map is adjointable, with
\[
R_j^*x=(\langle\eta_j,x\rangle,0,\ldots),
\]
and has degree zero between the indicated modules. For example an input coordinate of coefficient degree \(r\) has total degree \(r+p_j\), exactly the degree of \(\eta_jb_1\). The adjoint degree check follows from
\(|\langle\eta_j,x\rangle|=p_j+|x|\).
The ranges have dense joint span by countable generation.

Repeat each map at arbitrarily late indices, retaining its source parity. Insert zero maps of both source parities as necessary so that there are infinitely many summands of each parity. Then
\[
X=\bigoplus_jX_j\cong\widehat H_B
\tag{6.4}
\]
by separate countable coordinate bijections in the two parities. Define the same operator as in the operator-range stabilization proof:
\[
\begin{gathered}
T:X\to E\oplus X,\\
T((x_j))=\\
\left(\sum_j2^{-j}R_jx_j,(4^{-j}x_j)_j\right).
\end{gathered}
\tag{6.5}
\]
It is adjointable and degree zero. Its adjoint is
\(T^*(y,(z_j))=(2^{-j}R_j^*y+4^{-j}z_j)_j\).
Every finite-support vector lies in its range by taking \(y=0\); hence that range is dense.

The range of \(T\) is dense too. Approximate \(y\in E\) by a finite sum \(\sum R_iu_i\), and realize each term in a sufficiently late copy \(j_i\) of the same graded source, with input \(2^{j_i}u_i\). The second coordinate has norm at most \(\sum_i2^{-j_i}\|u_i\|\), as small as desired. To realize a general second coordinate, first approximate it by a finite-support vector, produce it with \(x_j=4^jz_j\), and correct its first coordinate at later indices. Thus both density arguments respect the typed source summands.

The preceding lesson's operator-range lemma proves that these two dense ranges give a unitary by the rule
\[
U(|T|x)=Tx.
\tag{6.6}
\]
For clarity, its required polar step uses
\(\overline{\operatorname{ran}(T^*T)}
=\overline{\operatorname{ran}T^*}=X\),
so \(|T|\) has dense range; (6.6) preserves inner products and has dense, closed range \(E\oplus X\). This is a valid polar decomposition in the present circumstances. Since \(T\) has degree zero, \(T^*T\) and its positive square root are even. The rule (6.6) therefore intertwines the gradings on a dense subspace, and hence everywhere. It is a degree-zero unitary \(X\to E\oplus X\). Use (6.4) and invert this unitary to obtain (6.2). \(\square\)

In particular \(E\) is degree-preservingly isomorphic to \(P\widehat H_B\) for an even projection \(P\in\mathcal L(\widehat H_B)\): transport the projection onto the first summand of (6.2). Its compact operators identify with \(P\mathcal K(\widehat H_B)P\). Indeed transporting \(\theta_{x,y}\) gives the corresponding rank-one operator on the range, and cutting arbitrary rank-one operators by \(P\) produces \(\theta_{Px,Py}\).

### Proposition 6.3. Exterior tensor products

For graded Hilbert modules \(E\) over \(B\) and \(F\) over \(C\), their exterior product is a graded Hilbert \(B\widehat\otimes C\)-module with homogeneous formulas
\[
\begin{gathered}
(x\widehat\otimes y)(b\widehat\otimes c)\\
=(-1)^{|y||b|}xb\widehat\otimes yc,\\
\langle x\widehat\otimes y,x'\widehat\otimes y'\rangle\\
=(-1)^{|y|(|x|+|x'|)}
   \langle x,x'\rangle\widehat\otimes\langle y,y'\rangle.
\end{gathered}
\tag{6.7}
\]
Its grading is the sum of the vector degrees. Homogeneous adjointable operators act by
\[
(S\widehat\otimes T)(x\widehat\otimes y)
=(-1)^{|T||x|}Sx\widehat\otimes Ty,
\tag{6.8}
\]
and \((S\widehat\otimes T)^*=(-1)^{|S||T|}S^*\widehat\otimes T^*\). Moreover
\[
\mathcal K(E\widehat\otimes F)
\cong\mathcal K(E)\widehat\otimes\mathcal K(F).
\tag{6.9}
\]

**Proof.** We realize the product as a corner, which proves positivity as well as the sign formulas. Let
\(L_E=\mathcal K(E\oplus B)\), with the grading induced by \(\gamma_E\oplus\beta\). Let \(p_E,q_E\) be the even multiplier projections onto \(E,B\). For \(x\in E\), the map \(R_x:B\to E\), \(b\mapsto xb\), is compact and satisfies \(R_x^*z=\langle x,z\rangle\). To check compactness when \(B\) is nonunital, let \(e_i\) be a contractive approximate identity: \(\theta_{x,e_i}\) is the map \(b\mapsto xe_ib\), and it converges in norm to \(R_x\) since \(xe_i\to x\). The latter follows by applying the approximate identity to \(\langle x,x\rangle\). Thus the corners of \(L_E\) are \(B\), \(E\), its adjoint corner, and \(\mathcal K(E)\). Use the analogous notation for \(F\).

In \(L=L_E\widehat\otimes L_F\), put
\[
P=p_E\widehat\otimes p_F,\qquad
Q=q_E\widehat\otimes q_F.
\]
These even multiplier projections are well defined by the spatial representation (3.4) and nondegenerate multiplier extensions. The coefficient corner \(QLQ\) is \(B\widehat\otimes C\), and \(PLQ\) is a Hilbert module over it with inner product \(z^*z'\). Corner inclusions preserve the minimal tensor norm: restrict faithful graded spatial representations to the ranges of the even corner projections, and apply Lemma 3.1.

Identify \(x\widehat\otimes y\) with \(R_x\widehat\otimes R_y\) in \(PLQ\). These tensors have dense span, since compressing the dense elementary tensors of \(L\) by \(P,Q\) compresses each factor to its indicated corner. Formula (3.1) gives the right action in (6.7). For the inner product, the adjoint introduces \((-1)^{|x||y|}\), and moving \(R_y^*\) past \(R_{x'}\) introduces \((-1)^{|y||x'|}\). Their product is the displayed inner-product sign. Positivity, conjugate symmetry, boundedness of the action and completeness follow from this Hilbert corner. Its induced grading has the stated degree.

Extend \(S\in\mathcal L(E)\) and \(T\in\mathcal L(F)\) as block operators with zero on the coefficient summands. They define multiplier corners: multiplying a compact rank-one operator by such a block operator, on either side, is again compact, with the adjoint giving the second multiplier action. Their graded tensor multiplier acts on \(PLQ\); multiplication in the corner gives (6.8) and the stated adjoint. These multipliers are bounded, since the faithful spatial representations extend nondegenerately to multipliers and a homogeneous elementary tensor has norm at most \(\|S\|\|T\|\).

Finally \(\mathcal K(PLQ)\) is the norm-closed span of left multiplications by \(zz'^*\). For elementary corner tensors these products are
\[
(-1)^{|x'|(|y|+|y'|)}
\theta_{x,x'}\widehat\otimes\theta_{y,y'}.
\]
Their span is dense in the corner
\(PLP=\mathcal K(E)\widehat\otimes\mathcal K(F)\).
Left multiplication of this corner on \(PLQ\) is faithful: an element annihilating \(PLQ\) annihilates the dense span of the products \(zz'^*\), hence annihilates \(PLP\); taking its product with its own adjoint shows it is zero. A faithful C\*-representation is isometric. This proves (6.9). \(\square\)

## 7. Clifford modules and the Bott symbol

Let \(\widehat M_n\) denote the Grothendieck group of finite-dimensional unital graded \(C_n\)-representations, with isomorphisms preserving grading. Restriction along \(C_n\subset C_{n+1}\) gives a homomorphism
\[
\begin{gathered}
r_n:\widehat M_{n+1}\to\widehat M_n,\\
Q_n=\widehat M_n/r_n(\widehat M_{n+1}).
\end{gathered}
\tag{7.1}
\]
This is an algebraic quotient of representation groups, before any K-theory theorem is applied.

### Proposition 7.1. The representation quotient

For \(k\geq0\),
\[
\begin{aligned}
\widehat M_{2k}&\cong\mathbb Z^2,&
\widehat M_{2k+1}&\cong\mathbb Z,\\
Q_{2k}&\cong\mathbb Z,& Q_{2k+1}&=0.
\end{aligned}
\tag{7.2}
\]
The generator of \(Q_{2k}\) can be represented by \(S_k\) with grading \(\Gamma_k\); reversing its grading changes its class to its negative.

**Proof.** Let \(d=2^k\). If \(M_d\) acts on a finite-dimensional space, its matrix units identify that space with \(\mathbb C^d\otimes W\): take \(W=E_{11}S\) and send \(e_i\otimes\xi\) to \(E_{i1}\xi\). These images are mutually orthogonal and exhaust the space because \(\sum_iE_{ii}=1\). In these coordinates the action is \(X\otimes1\), and its commutant is \(1\otimes\operatorname{End}(W)\), as follows by commuting with all \(E_{ij}\).

For the grading \(\operatorname{Ad}\Gamma_k\), a module grading \(\gamma\) therefore has the form \(\Gamma_k\otimes J\): the product \((\Gamma_k\otimes1)\gamma\) commutes with the matrix algebra. The element \(\Gamma_k\) is even, so it commutes with \(\gamma\); hence \(J\) is a self-adjoint unitary. Its two eigenspace dimensions classify graded modules and add under direct sum. The representation monoid is \(\mathbb N^2\), and its group completion is \(\mathbb Z^2\). This also holds at \(k=0\), where the two integers are the even and odd dimensions.

For a swap-graded \(M_d\oplus M_d\), the module grading is a unitary from the first central summand to the second, intertwining their matrix actions, and its inverse in the other direction. The two multiplicity spaces consequently have equal dimension. Choosing this unitary as their identification puts the grading in swap form. Thus the monoid is \(\mathbb N\), with group completion \(\mathbb Z\).

To compute restriction to \(C_{2k}\), use the odd representation in (5.8) on \(S_k\oplus S_k\), with grading \((\xi,\eta)\mapsto(\Gamma_k\eta,\Gamma_k\xi)\). The diagonal and anti-diagonal subspaces are invariant for the first \(2k\) generators, with gradings \(\Gamma_k\) and \(-\Gamma_k\). Hence \(r_{2k}(1)=(1,1)\). Each of the two graded irreducibles for \(C_{2k+2}\) has dimension \(2^{k+1}\); restricted to \(C_{2k+1}\), that is exactly the dimension of its unique graded irreducible, so \(r_{2k+1}(1,0)=r_{2k+1}(0,1)=1\). The two quotients are therefore \(\mathbb Z^2/\mathbb Z(1,1)\cong\mathbb Z\) and \(\mathbb Z/\mathbb Z=0\). Reversing the even grading exchanges \((1,0)\) and \((0,1)\), whose quotient classes are opposite. \(\square\)

A graded module \(c:C_n\to\operatorname{End}(S)\) supplies the symbol
\[
\sigma_c(v)=c(v)|_{S^+}:S^+\to S^-.
\tag{7.3}
\]
For \(v\ne0\), its inverse is \(\|v\|^{-2}c(v)|_{S^-}\), by (5.1). Thus the two trivial bundles and (7.3) define a compactly supported K-theory class in
\[
K_0(C_0(\mathbb R^n)).
\]
Explicitly, restrict the two trivial bundles and this map to the closed unit ball \(D^n\); the boundary map on \(S^{n-1}\) is invertible. The difference-bundle theorem identifies that relative triple with \(K^0(D^n,S^{n-1})=K_0(C_0(\mathbb R^n))\). [Relative difference bundles, radial pairs and the planar normalization, Theorem RK.3](supporting/relative-k-foundations/relative-k-foundations.html#rk-difference) proves both inverse maps for every compact Hausdorff closed pair. [Theorem RK.4](supporting/relative-k-foundations/relative-k-foundations.html#rk-radial) proves the radial disc/sphere identification in both degrees, including rank-zero components. For \(n=0\) the class is \(\dim S^+-\dim S^-\).

### Lemma 7.2. Extending a module kills its symbol

If a graded \(C_n\)-module extends to a graded \(C_{n+1}\)-module, the class of (7.3) is zero. Every finite-dimensional graded \(C_{2k+1}\)-module has such an extension.

**Proof.** Let \(h=c(e_{n+1})\) be the extra odd self-adjoint unitary. For \(\|v\|\leq1\), replace (7.3) by the positive-to-negative block of
\[
c(v)+\sqrt{1-\|v\|^2}\,h;
\tag{7.4}
\]
outside the unit ball leave it equal to \(c(v)\). Since \(h\) anticommutes with \(c(v)\), the square of (7.4) is \(1\). The replacement is continuous at the unit sphere, agrees with the old symbol outside a compact set, and is invertible everywhere. It represents zero in relative K-theory, by the global-extension relation proved in [Corollary RK.4a](supporting/relative-k-foundations/relative-k-foundations.html#rk-symbol-rules). More explicitly, linearly interpolating the symbols is still fixed and invertible outside the ball, so it is an allowed relative homotopy to this everywhere invertible triple. The same argument for \(n=0\) uses \(h:S^+\to S^-\).

For odd \(n=2k+1\), use the central odd unitary \(w\) from (5.7), and let \(\gamma\) be the module grading. Put
\[
h=i\gamma c(w).
\tag{7.5}
\]
Since \(c(w)\) is odd, it anticommutes with \(\gamma\); hence \(h=h^*\) and \(h^2=1\). Since \(w\) is central and \(\gamma\) anticommutes with every \(c(e_j)\), \(h\) anticommutes with all \(c(e_j)\). It also anticommutes with \(\gamma\), so it is odd. These are precisely the relations for the extra generator. \(\square\)

Consequently (7.3) induces a well-defined homomorphism
\[
\mathrm{ABS}_n:Q_n\longrightarrow K_0(C_0(\mathbb R^n)).
\tag{7.6}
\]
For \(n=2\) the positive-to-negative block of
\(x\sigma_1+y\sigma_2\) is multiplication by \(x+iy\). Denote its class by \(\beta_2\). In dimension \(2k\), (5.5) gives the corresponding spinor symbol \(\beta_{2k}\).

The remaining **complex Atiyah–Bott–Shapiro theorem** to prove is that (7.6) is an isomorphism for every \(n\). With our orientation convention, \([S_k]\) maps to \(\beta_{2k}\). Its asserted conclusion is that the target is \(\mathbb Z\) in even dimensions, generated by this symbol, and zero in odd dimensions. The multiplicative formulation identifies
\(\bigoplus_{n\geq0}Q_n\) with \(\mathbb Z[t]\), \(\deg t=2\), and identifies \(t^k\) with \(\beta_{2k}\); products on the target use exterior products and the ordered decomposition of Euclidean space.

The representation calculation and the vanishing lemma have been proved here. The assertion that these symbols generate all compactly supported K-theory classes, and the stated compatibility of products, are the topological content of Bott periodicity. Their full proof remains an obligation in *Bott periodicity in KK: the Bott and Dirac elements*. That proof must establish that the oriented spinor symbol corresponds to the Bott element and that its product with the Dirac element is the identity, without using (7.6) as a premise. The algebraic calculation in this lesson alone is not a proof of surjectivity in (7.6).

## 8. Exercises

**8.1. Commutator signs.** Expand the graded Leibniz and Jacobi identities in (1.3). Also show that for homogeneous \(x,y\),
\[
\left[x,y\right]_{\mathrm{gr}}^*
=-(-1)^{|x||y|}[x^*,y^*]_{\mathrm{gr}}.
\]
What do these formulas say when both entries are odd and self-adjoint?

**8.2. Two odd generators.** Construct explicitly the isomorphism
\(C_1\widehat\otimes C_1\to M_2\), including the involution of the product of the two generators and its grading.

**8.3. Dimension three.** Give explicit representations of \(C_2\) and \(C_3\). Determine the central projections of \(C_3\), its grading in those coordinates, and a coordinate change making it pure swap.

**8.4. Spinors and chirality.** For an oriented Euclidean space \(V\) of dimension \(2k\), construct a graded space \(S\) of dimension \(2^k\) and prove \(\mathrm{Cl}(V)\cong\operatorname{End}(S)\). Compute the chirality element with the self-adjoint convention (5.1), and describe the effect of reversing orientation. Include the case \(k=0\).

## 9. Solutions

**Solution to 8.1.** Write \(p=|x|,q=|y|,r=|z|\). The Leibniz right side expands as
\[
xyz-(-1)^{pq}yxz
+(-1)^{pq}yxz-(-1)^{pq+pr}yzx,
\]
which is the left side. The three Jacobi expansions in the proof of Proposition 1.1 exhibit all six word cancellations, including their coefficients; no ungraded skew-symmetry was used. Finally
\[
\begin{aligned}
\left[x,y\right]_{\mathrm{gr}}^*
 &=y^*x^*-(-1)^{pq}x^*y^*\\
 &=-(-1)^{pq}
   (x^*y^*-(-1)^{pq}y^*x^*).
\end{aligned}
\]
For odd self-adjoint \(x,y\), the bracket is the self-adjoint anticommutator \(xy+yx\); for \(y=x\) it is \(2x^2\geq0\). The Jacobi and Leibniz signs remain those in (1.3), with \(p=q=1\) where appropriate.

**Solution to 8.2.** Put
\(a=\varepsilon\widehat\otimes1\) and \(b=1\widehat\otimes\varepsilon\).
They are odd self-adjoint unitaries and \(ab=-ba\). The four basis vectors \(1,a,b,ab\) map respectively to
\[
1,\quad \sigma_1,\quad\sigma_2,\quad i\sigma_3.
\]
They are linearly independent matrices, so the homomorphism is bijective. The tensor involution gives
\((ab)^*=-ab\), agreeing with \((i\sigma_3)^*=-i\sigma_3\). The even span is that of \(1,ab\), which maps to diagonal matrices; the odd span is that of \(a,b\), which maps to off-diagonal matrices. Conjugation by \(\sigma_3\) is therefore the grading. Finite-dimensionality ensures the same C\*-isomorphism for both completions.

**Solution to 8.3.** For \(C_2\), use \(e_1=\sigma_1,e_2=\sigma_2\), with grading \(\operatorname{Ad}\sigma_3\). They generate \(M_2\), and its four-dimensional basis exhausts (5.2). For \(C_3\), send
\[
\begin{gathered}
e_1\mapsto(\sigma_1,\sigma_1),\\
e_2\mapsto(\sigma_2,\sigma_2),\\
e_3\mapsto(\sigma_3,-\sigma_3).
\end{gathered}
\]
The central self-adjoint unitary \(w=-ie_1e_2e_3\) maps to \((1,-1)\), so its two spectral projections map to \((1,0)\) and \((0,1)\). Each summand contains a full \(M_2\); this gives an eight-dimensional faithful algebra, as required. The grading is
\[
\alpha(X,Y)=(\sigma_3Y\sigma_3,\sigma_3X\sigma_3).
\]
This sends each displayed generator to its negative. Under
\(\Psi(X,Y)=(X,\sigma_3Y\sigma_3)\), one has
\(\Psi\alpha\Psi^{-1}(X,Y)=(Y,X)\).

**Solution to 8.4.** Choose a positively oriented orthonormal basis and put \(S=(\mathbb C^2)^{\otimes k}\). Define its generators by (5.5). The anticommutation calculation there verifies (5.1); equations (5.6) then produce each isolated Pauli matrix, so the representation is onto \(\operatorname{End}(S)\). Its dimension equals the normal-form bound \(2^{2k}\), proving injectivity. Multiplying each adjacent pair in (5.5) gives \(i\) times the isolated \(\sigma_3\), so
\[
(-i)^kc_1\cdots c_{2k}=\sigma_3^{\otimes k}.
\]
This self-adjoint unitary anticommutes with every generator and implements the grading. A negatively oriented orthonormal basis has top exterior product of the opposite sign, so chirality reverses, exchanging \(S^+\) and \(S^-\). For \(k=0\), \(S=\mathbb C\), the empty product is \(1\), \(C_0=\mathbb C=\operatorname{End}(S)\), and the chosen grading is entirely even.

## What this lesson does not prove

Lemmas 3.0a and 6.0a prove the ordinary tensor norms and interior construction, including independence, positivity, adjointability, and rebracketing. The graded tensor norm, Clifford structure, arbitrary-coefficient graded stabilization, representation quotient, and symbol-vanishing statements have their proofs here. The dense-range polar step in (6.6) uses Lemma 2.1 of this course's earlier lesson [Ext groups, absorption and Brown–Douglas–Fillmore theory](KT-KK-02.html). The earlier Hilbert-module and C\*-algebra proofs are identified in the introduction. The relative symbol group in Section 7 is identified with operator K-theory by the earlier [Relative difference bundles, radial pairs and the planar normalization, Theorems RK.3–RK.4 and Corollary RK.4a](supporting/relative-k-foundations/relative-k-foundations.html#rk-difference).

The full Bott-periodicity and Atiyah–Bott–Shapiro isomorphism remains an explicit proof obligation in this course's *Bott periodicity in KK: the Bott and Dirac elements*. Its required generality, oriented spinor generator, and product compatibility are stated after (7.6). Neither the symbol map nor the representation quotient calculation uses that theorem. No spin-c existence or classification theorem is invoked.

## References

- B. Blackadar, *K-Theory for Operator Algebras*, second edition, 1998. [Actual freely readable author text](https://www.bruceblackadar.com/Mathematics/book6.pdf), Sections 13.5 and 14.1–14.6.1. The general interior action here has codomain \(\mathcal L(F)\), and the stabilization proof uses coefficient-module maps when there is no unit.

- B. Blackadar, *Operator Algebras: Theory of C\*-Algebras and von Neumann Algebras*, corrected author edition dated February 8, 2017. [Actual freely readable edition](https://www.bruceblackadar.com/Mathematics/Cycr.pdf), Section II.9.1. The representation-independent spatial norm has a complete proof in Lemma 3.0a.

- [Relative difference bundles, radial pairs and the planar normalization](supporting/relative-k-foundations/relative-k-foundations.html#rk-difference), Theorems RK.3–RK.4 and Corollary RK.4a, for the complete earlier programme proof of relative difference bundles, radial compact support and symbol vanishing. The free Hatcher and Blackadar sources are identified there.

- *Kasparov's KK-theory*, [Ext groups, absorption and Brown–Douglas–Fillmore theory](KT-KK-02.html), Lemma 2.1, for the earlier operator-range proof used in graded stabilization.
