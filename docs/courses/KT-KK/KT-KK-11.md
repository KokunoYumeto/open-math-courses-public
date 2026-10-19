# Unbounded Kasparov modules and spectral triples

*Written by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An elliptic differential operator carries geometric information that its bounded transform largely forgets. The unbounded picture retains its domain, principal symbol and commutators, while still giving a class in KK-theory. We prove the passage to bounded cycles and the converse existence theorem. We then derive the connection and positivity estimates used to recognize unbounded products.

The regular-operator calculus and its arbitrary-correspondence tensor extension are proved in local Lemma 0.0. Lemmas 0.1–0.2 give the localization and compact-support facts used in the analytic sum and essential-connection proofs. [Lesson 05, Lemma 2.0](KT-KK-05.html#lemma-2-0-compact-module-operators-and-their-multipliers) proves the compact ideal, multiplier identification and countable-generation criterion. The bounded product existence, uniqueness, normalization and essential-replacement multiplication connections are the earlier Lesson 09 [Theorem 3.1](KT-KK-09.html#3-existence-from-the-technical-theorem), [Theorems 4.1–4.2](KT-KK-09.html#4-uniqueness-and-descent-to-homotopy-classes), [Lemma 2.1](KT-KK-09.html#2-the-product-axioms-and-normalization) and [Proposition 5.1, including equation (5.1a)](KT-KK-09.html#5-essential-representations-and-homomorphisms); its current product theorem allows arbitrary final coefficient algebras. All additional unbounded estimates used here are proved below.

## 0. Regular calculus, localization and compact supports

**Lemma 0.0 (resolvents, continuous calculus and tensor extension).** Let \(E\) be a Hilbert \(B\)-module, and let \(D=D^*\) be a closed densely defined operator for which \(1+D^2\) has dense range. Then \(D\pm i\) are bijective from \(\operatorname{Dom}D\) to \(E\), with mutually adjoint inverse resolvents of norm at most one. There is a nondegenerate continuous functional calculus \(C_0(\mathbb R)\to\mathcal L(E)\); it extends to bounded continuous functions, and
\[
\|(D-z)^{-1}\|\leq |\operatorname{Im}z|^{-1}
\quad(\operatorname{Im}z\ne0).
\]
If \(Y\) is any \(B\)-\(C\) correspondence, the closure of \(D\otimes1\) on \(\operatorname{Dom}D\odot_B Y\) is self-adjoint regular on \(E\otimes_B Y\), and its bounded continuous functional calculus is \(f(D)\otimes1\). No separability or essentiality of the left action on \(Y\) is assumed.

**Proof: resolvents.** Symmetry cancels the mixed terms in
\[
\langle(D\pm i)x,(D\pm i)x\rangle
=\langle Dx,Dx\rangle+\langle x,x\rangle.
\]
Thus these operators are bounded below by one. Their ranges are closed: a convergent sequence of images makes the preimages Cauchy, and closedness of \(D\) then gives a preimage of the limit. The range of each contains the dense range of \(1+D^2\), since on \(\operatorname{Dom}D^2\) this is the product \((D+i)(D-i)\) in either order. Their ranges are therefore all of \(E\). Write \(R_\pm=(D\pm i)^{-1}\). For \(a,b\in E\), symmetry gives
\[
\langle R_+a,b\rangle
=\langle R_+a,(D-i)R_-b\rangle
=\langle a,R_-b\rangle.
\]
Hence \(R_+^*=R_-\). The identities \(DR_\pm=1\mp iR_\pm\), first on their ranges, give
\[
R_+-R_-=-2iR_+R_-=-2iR_-R_+.
\]
In particular they commute. Put \(U=1-2iR_+\). The preceding identities give \(UU^*=U^*U=1\), and \(1-U=2iR_+\) has dense range \(\operatorname{Dom}D\).

**Proof: functional calculus.** We first prove the continuous calculus of a unitary locally. For a Laurent polynomial \(p(z)=\sum_{j=-m}^m a_jz^j\), put \(M=\sup_{|z|=1}|p(z)|\). Given \(\xi\in E\) and \(N>2m\), the continuous \(E\)-valued polynomial
\[
w_N(z)=N^{-1/2}\sum_{k=0}^{N-1}z^kU^{-k}\xi
\]
has
\(\int_{\mathbb T}\langle w_N,w_N\rangle\,d\theta/(2\pi)=\langle\xi,\xi\rangle\).
For \(m\leq l\leq N-1-m\), the coefficient of \(z^l\) in \(p(z)w_N(z)\) is \(N^{-1/2}U^{-l}p(U)\xi\). Integrating the inner product cancels distinct monomials, and every omitted coefficient contributes a positive element. Since pointwise \(|p(z)|^2\leq M^2\), this gives the positive-order inequality
\[
\frac{N-2m}{N}\langle p(U)\xi,p(U)\xi\rangle
\leq \int_{\mathbb T}\langle p w_N,p w_N\rangle\,\frac{d\theta}{2\pi}
\leq M^2\langle\xi,\xi\rangle.
\]
Take norms and then \(N\to\infty\). Thus \(\|p(U)\|\leq\|p\|_\infty\), for every Laurent polynomial, on a Hilbert module as well as a Hilbert space.

Laurent polynomials are uniformly dense in \(C(\mathbb T)\). Indeed the kernels
\(K_N(\theta)=N^{-1}|\sum_{k=0}^{N-1}e^{ik\theta}|^2\)
are positive with normalized integral one. The geometric-series formula bounds their integral outside any fixed neighborhood of zero by a constant times \(N^{-1}\). Uniform continuity then makes convolution with \(K_N\) converge uniformly to a continuous circle function; each convolution is a Laurent polynomial. The polynomial norm bound therefore extends evaluation at \(U\) to a unital contractive *-homomorphism \(C(\mathbb T)\to\mathcal L(E)\). Multiplication and adjoints pass through uniform polynomial approximation. No earlier normal-calculus or spectral-representation assertion is needed for this construction. The map
\[
u(t)=(t-i)/(t+i)
\]
identifies \(\mathbb R\) with the circle minus \(1\). For \(f\in C_0(\mathbb R)\), its transported function extends by zero at \(1\); evaluate it at \(U\) to define \(f(D)\). This is a contractive *-homomorphism. It is nondegenerate because the function \(1-u(t)=2i/(t+i)\) has operator value \(1-U\), whose range is dense.

For completeness, its extension to \(C_b(\mathbb R)\) is also constructive. Let \(e_n\in C_c(\mathbb R)\) be positive cutoffs tending uniformly to one on compact sets, with \(0\leq e_n\leq1\). For bounded continuous \(h\), the uniformly bounded operators \((he_n)(D)\) converge on every vector \(f(D)\xi\), because \(he_nf\to hf\) uniformly. Such vectors have dense span, so the operators converge on every vector to a bounded operator \(h(D)\). The same argument for \(\overline h\) gives its adjoint. Products and adjoints pass to these uniformly bounded vector limits, proving the extended *-homomorphism. Its value does not depend on the chosen cutoffs, by the same dense-span argument.

The identity \(D=i(1+U)(1-U)^{-1}\) holds on the dense domain \(\operatorname{ran}(1-U)\). For nonreal \(z\), the bounded scalar function \((t+i)/(t-z)\) therefore shows that the value of \((t-z)^{-1}\) has range in \(\operatorname{Dom}D\) and is a two-sided inverse of \(D-z\). Its norm is bounded by the scalar supremum \(|\operatorname{Im}z|^{-1}\). Polynomial identities on \(U\) and their uniform limits show that this calculus agrees with the two original resolvents and with the usual products of their functions. In particular the value of \((1+t^2)^{-1}\) is \((1+D^2)^{-1}=R_+R_-\).

We also need the converse Cayley construction. If \(V\) is unitary and \(1-V\) has dense range, then it is injective: its kernel equals the kernel of \(1-V^*\), which is orthogonal to that dense range. On \(\operatorname{ran}(1-V)\) define
\[
S((1-V)x)=i(1+V)x.
\]
Expanding both inner products and using \(V^*V=1\) proves symmetry. The operators \(S+i\) and \(S-i\) have bounded, everywhere-defined, mutually adjoint inverses
\[
Q_+=(1-V)/(2i),\qquad Q_-=(V^*-1)/(2i).
\]
These formulas prove that \(S\) is closed, since the inverse of an injective bounded operator is closed on its range. If \(y\in\operatorname{Dom}S^*\), choose \(x\in\operatorname{Dom}S\) with \((S-i)x=(S^*-i)y\). Then \(y-x\in\ker(S^*-i)\), which is orthogonal to the surjective range of \(S+i\). Hence \(y=x\), proving \(S=S^*\). The commuting product \(Q_+Q_-\) has range in \(\operatorname{Dom}S^2\) and is the inverse of \(1+S^2\), by the two resolvent identities. Thus \(S\) is regular. This proves the converse without a graph-complement theorem.

**Proof: tensor extension.** [Lemma 6.0a of Lesson 05](KT-KK-05.html#lemma-6-0a-constructing-the-ordinary-interior-product) supplies the unital *-homomorphism \(T\mapsto T\otimes1\) on adjointable operators. Thus \(V=U\otimes1\) is unitary. The range of \(1-V\) is dense: the algebraic tensors with first vector in \(\operatorname{Dom}D\) are dense, and every such vector is in that range. Apply the converse Cayley construction to \(V\), obtaining a self-adjoint regular \(S\). The formulas for \(Q_\pm\) show that \(S(x\otimes y)=Dx\otimes y\) on the algebraic domain. This domain is a graph core: its image under \(S+i\) contains all elementary tensors and is dense, while \(S+i\), with its bounded inverse and \(S Q_+=1-iQ_+\), identifies its graph norm with an equivalent complete norm on \(E\otimes_B Y\). Consequently \(S\) is precisely the closure of the algebraic tensor operator. Continuous circle calculus commutes with \(T\mapsto T\otimes1\). The bounded-function extension does too, since uniformly bounded vector convergence on \(E\) gives vector convergence on elementary tensors and hence on their dense span. This proves the claimed calculus identity. If \(D\) is odd, its grading sends \(U\) to \(U^*\), and the same formulas give \(f(D)\mapsto f(-D)\) and oddness of the tensor extension. \(\square\)

The free [Kaad–Lesch author preprint, Section 2.3 and Proposition 4.1](https://www.math.uni-bonn.de/people/lesch/dl/pap/2011-KaaLes-ArXiv-v2.pdf) supplies the regular-operator formulation used here. Its references are not imported as proof premises: the resolvent, Cayley, functional-calculus and tensor assertions needed below have just been proved.


**Lemma 0.1 (the symmetric local-global criterion).** Let \(R\) be a closed densely defined symmetric operator on a Hilbert \(B\)-module \(E\). For each state \(\omega\) of \(B\), complete the quotient of \(E\) for the scalar semi-inner product
\(\omega(\langle x,y\rangle)\), and denote the resulting Hilbert space by \(E_\omega\) and its canonical map by \(j_\omega\). The rule
\(j_\omega x\mapsto j_\omega Rx\), on \(j_\omega(\operatorname{Dom}R)\), is well defined, symmetric and closable; write \(R_\omega\) for its closure. Then \(R\) is self-adjoint regular if and only if every \(R_\omega\) is self-adjoint. There is no countability, unitality or fullness hypothesis.

**Proof of localization.** The domain image is dense because the scalar seminorm is at most the module norm. If \(j_\omega x=0\) for a domain vector, then for every other domain vector \(y\), symmetry gives
\[
\langle j_\omega Rx,j_\omega y\rangle
=\langle j_\omega x,j_\omega Ry\rangle=0.
\]
Density makes \(j_\omega Rx=0\), proving that the rule is well defined. The same equality proves symmetry. Every densely defined symmetric Hilbert-space operator is closable: if domain vectors tend to zero and their images tend to \(z\), testing against its dense domain gives \(z=0\). This proves the assertions preceding the equivalence.

**Proof of separation.** We need an explicit separation statement for a closed Hilbert submodule \(L\subsetneq E\). Choose \(x\notin L\), and put \(d=\operatorname{dist}(x,L)>0\). In the real Banach space \(B_{\mathrm{sa}}\) consider
\[
\mathcal C=\{\langle x-y,x-y\rangle+b:y\in L,\ b\in B_+\}.
\]
This set is convex. In fact, for \(0\leq t\leq1\), the convex combination of the two squared-distance elements for \(y,z\) is the squared-distance element for \(ty+(1-t)z\), plus
\(t(1-t)\langle y-z,y-z\rangle\). It is also stable under addition of \(B_+\). Every member has norm at least \(d^2\), by monotonicity of the norm on positive elements; this lower bound persists on its closure. The earlier [*Hahn–Banach, Baire and the basic theorems on Banach spaces*, Corollary 6.4(2)](../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-06), therefore supplies a nonzero bounded real linear functional \(f\) and \(\epsilon>0\) with \(f(c)\geq\epsilon\) for all \(c\in\mathcal C\). Since \(\mathcal C+B_+\subset\mathcal C\), scaling any positive element shows \(f(b)\geq0\) for \(b\in B_+\). Its complex-linear extension is positive. Normalize it to a state \(\omega\). Then
\[
\|j_\omega x-j_\omega y\|^2
=\omega(\langle x-y,x-y\rangle)
\geq\epsilon/\|f\|\qquad(y\in L).
\]
Thus the closure of \(j_\omega(L)\) is a proper Hilbert subspace. This proves the needed separation without a Jordan decomposition or an orthogonal complement for \(L\) in the module.

**Proof of the criterion.** Symmetry gives, on the domain,
\[
\langle(R\pm i)x,(R\pm i)x\rangle
=\langle Rx,Rx\rangle+\langle x,x\rangle.
\]
Hence \(R\pm i\) are injective and have closed range: convergence of their images makes their preimages and their \(R\)-images Cauchy, and closedness of \(R\) gives the limit in the domain. If either range were proper, apply the separation just proved to this closed submodule. For its separating state,
\[
j_\omega(\operatorname{ran}(R\pm i))
=\operatorname{ran}(R_{\omega,0}\pm i).
\]
The closure of the right side is \(\operatorname{ran}(R_\omega\pm i)\) when \(R_\omega\) is self-adjoint: its initial domain is a graph core, so its graph approximation approximates each image, and the latter range is the whole Hilbert space. This contradicts separation. Consequently both \(R\pm i\) are surjective.

Their inverse maps are bounded and mutually adjoint by the symmetry inner-product identity. If \(y\in\operatorname{Dom}R^*\), choose \(x\in\operatorname{Dom}R\) with \((R-i)x=(R^*-i)y\). Then \(y-x\) is in \(\ker(R^*-i)\), orthogonal to the surjective range of \(R+i\), and is zero. Thus \(R=R^*\). The two inverse resolvents commute by their resolvent identity, and their product is an inverse for \(1+R^2\), with range in \(\operatorname{Dom}R^2\). This proves regularity.

Conversely, for self-adjoint regular \(R\), Lemma 0.0 gives its two inverse resolvents. Each adjointable module operator descends boundedly to \(E_\omega\): apply \(\omega\) to
\(\langle Tx,Tx\rangle\leq\|T\|^2\langle x,x\rangle\). Its adjoint descends too. The descended inverse resolvents show that the ranges of \(R_\omega\pm i\) contain the dense image of \(j_\omega(E)\). A closed symmetric Hilbert-space operator has closed ranges for these two operators by the displayed estimate, so they are surjective. The adjoint-domain argument just given, now in the Hilbert space, proves self-adjointness. \(\square\)

The freely readable [Kaad–Lesch author preprint, Theorems 3.1 and 4.2](https://www.math.uni-bonn.de/people/lesch/dl/pap/2011-KaaLes-ArXiv-v2.pdf), printed pp. 8–13, is the comparison source. The precise symmetric criterion required in this lesson, including its separating-state proof, has been established locally above.

**Lemma 0.2 (compact maps and a noncomplemented support).** If \(T:E\to Y\) is adjointable and \(T^*T\in\mathcal K(E)\), then \(T\in\mathcal K(E,Y)\). If \(X\subset E\) is a closed Hilbert submodule, finite rank-one sums with their two vectors in \(X\) have the same norm on \(X\) and on \(E\). They therefore define an isometric inclusion \(\mathcal K(X)\to\mathcal K(E)\). A compact operator on \(E\) whose range and adjoint range lie in \(X\) belongs to this included algebra. None of these assertions requires an adjointable projection onto \(X\).

**Proof.** For the first assertion let \(a=T^*T\), and use \(f_\delta(t)=t/(t+\delta)\). Functional calculus puts \(f_\delta(a)\) in \(\mathcal K(E)\), and
\[
\|T-Tf_\delta(a)\|^2
=\|(1-f_\delta(a))a(1-f_\delta(a))\|
\leq\delta/4.
\]
Composition of an adjointable map with rank-one operators is rank one, so \(Tf_\delta(a)\) is compact with target \(Y\). Its norm limit is \(T\).

For finite columns \(C,D:B^r\to X\) with those same columns viewed in \(E\), both Gram matrices are unchanged. The operator \(CD^*\) has squared norm
\[
\|(C^*C)^{1/2}(D^*D)(C^*C)^{1/2}\|,
\]
because \((CD^*)^*(CD^*)=D(C^*C)D^*\), and \(ZZ^*\) and \(Z^*Z\) have the same norm for \(Z=D(C^*C)^{1/2}\). This proves the isometric inclusion by completion; rank-one products and adjoints prove it is a *-homomorphism.

Finally let \(k\in\mathcal K(E)\) have both ranges in \(X\). Regarded as a map \(E\to X\), it is adjointable, with adjoint \(k^*|_X\). Its squared modulus is still \(k^*k\), so the first assertion makes it compact with target \(X\). A contractive approximate identity \(u_\lambda\) of \(\mathcal K(X)\), included in \(\mathcal K(E)\), converges on every vector in \(X\), by [Lesson 05, Lemma 2.0](KT-KK-05.html#lemma-2-0-compact-module-operators-and-their-multipliers). Finite rank approximation of this compact map shows \(u_\lambda k\to k\) in norm. Apply the same argument to \(k^*\) to obtain \(ku_\lambda\to k\). The sandwiches \(u_\lambda k u_\lambda\) lie in \(\mathcal K(X)\): on finite rank sums this follows from the rank-one composition rule, and norm limits give it for the approximate-identity elements. They converge to \(k\), proving the assertion. \(\square\)


## 1. Domains, grading and local compactness

Let \(A,B\) be graded C\*-algebras. An **unbounded Kasparov module** is a countably generated graded Hilbert \(B\)-module \(E\), a graded representation \(\phi:A\to\mathcal L(E)\), and an odd self-adjoint regular operator \(D\), such that
\[
(1+D^2)^{-1}\phi(a)\in\mathcal K(E)\qquad(a\in A).
\tag{1.1}
\]
There must also be a dense graded \(*\)-subalgebra \(\mathcal A\subset A\) whose elements preserve \(\operatorname{Dom}D\), with bounded adjointable graded commutators
\[
c_a=D\phi(a)-(-1)^{|a|}\phi(a)D,\qquad a\in\mathcal A
\tag{1.2}
\]
homogeneous. Requiring domain preservation makes (1.2) an actual equality on the whole domain. Products and adjoints preserve these conditions, by the Leibniz rule and the adjoint identity on the domain. The representation need not be essential.

Condition (1.1) is **local compactness of the resolvent**. It becomes globally compact resolvent when \(A\) is unital and \(\phi(1)=1\). These are different requirements for nonunital algebras.

**Lemma 1.1 (all vanishing functions are locally compact).** Condition (1.1) implies
\[
f(D)\phi(a),\quad \phi(a)f(D)\in\mathcal K(E)
\qquad(f\in C_0(\mathbb R),\ a\in A).
\tag{1.3}
\]

**Proof.** Write \(q(t)=(1+t^2)^{-1}\). Choose continuous cutoffs \(e_n\) of the positive variable \(q\), zero near zero and equal to one on larger compact subintervals of \((0,1]\). The quotient \(e_n(q)/q\) is bounded and continuous after its zero extension. Thus \(e_n(q(D))\phi(a)\) is a bounded operator times \(q(D)\phi(a)\), and is compact.

The functions \(f(t)e_n(q(t))\) converge uniformly to \(f\): on a large compact interval the cutoffs are eventually one, and outside it \(f\) is uniformly small. Therefore \(f(D)\phi(a)\) is a norm limit of compact operators. Taking adjoints, with \(a^*\) and \(\overline f\), proves the other assertion. \(\square\)

For example, on \(E=C_0(\mathbb R)\) with its usual coefficient inner product, multiplication by \(x\) is self-adjoint regular. Its inverse resolvents are multiplication by \((x\pm i\rho)^{-1}\), with dense ranges. Since \(\mathcal K(E)=C_0(\mathbb R)\), its resolvent is compact as a module operator. This means multiplication by a function vanishing at infinity, rather than finite rank as a Hilbert-space operator.

## 2. The bounded transform

Put
\[
F_D=D(1+D^2)^{-1/2}.
\tag{2.1}
\]
Regular functional calculus gives a self-adjoint odd contraction with
\[
F_D^2-1=-(1+D^2)^{-1}.
\tag{2.2}
\]
The substantive point is compactness of its source commutators.

**Lemma 2.1 (the resolvent commutator estimate).** For homogeneous \(a\in\mathcal A\), set \(\epsilon=(-1)^{|a|}\), \(c=c_a\), and \(R_z=(D-z)^{-1}\), with \(z=\pm i\rho\), \(\rho>0\). Then
\[
R_z\phi(a)-\epsilon\phi(a)R_{\epsilon z}
=-\epsilon R_zcR_{\epsilon z}.
\tag{2.3}
\]
Consequently, for \(Q_\rho=D(D^2+\rho^2)^{-1}\),
\[
\|[Q_\rho,\phi(a)]_{\mathrm{gr}}\|
\leq \|c\|\rho^{-2}.
\tag{2.4}
\]
Its products on either side by \(\phi(b)\) are compact for all \(b\in A\).

**Proof.** Domain preservation and (1.2) give
\((D-z)\phi(a)=\epsilon\phi(a)(D-\epsilon z)+c\)
on \(\operatorname{Dom}D\). Multiply by the two inverse resolvents and rearrange to obtain (2.3). Since
\[
Q_\rho=\tfrac12(R_{i\rho}+R_{-i\rho}),
\]
the graded commutator is the sum of the two right sides of (2.3), with the same factor \(1/2\). Each inverse resolvent has norm at most \(\rho^{-1}\), proving (2.4).

Lemma 1.1 makes \(R_{\epsilon z}\phi(b)\) compact, so the right-localized products are compact. The adjoint identity applied to \(a^*\) proves the left-localized products. Every composition used here is of bounded adjointable operators. \(\square\)

**Theorem 2.2 (Baaj–Julg bounded transform).** The triple \((E,\phi,F_D)\) is a Kasparov module.

**Proof.** Self-adjointness, parity and the square defect were checked in (2.1)–(2.2). For the commutator use the scalar integral, interpreted on vectors through regular functional calculus,
\[
F_D\xi=\frac2\pi\int_0^\infty
D(1+D^2+t^2)^{-1}\xi\,dt.
\tag{2.5}
\]
To justify this interpretation, integrate first to a finite endpoint. The resulting bounded continuous functions converge pointwise to \(x/\sqrt{1+x^2}\), are bounded in absolute value by one, and converge uniformly on compact subsets of \(\mathbb R\). Apply them first to vectors \(f(D)\eta\), \(f\in C_0(\mathbb R)\), then use their dense span and the uniform bound. Thus the partial integrals converge strongly on the module. The integral in (2.5) generally does not converge in operator norm.

After taking a commutator the situation improves: Lemma 2.1 bounds the integrand by
\(\|c_a\|/(1+t^2)\). Its norm integral is finite. Strong convergence identifies the norm-convergent commutator integral with \([F_D,\phi(a)]_{\mathrm{gr}}\). For every \(b\in A\), Lemma 2.1 also makes each localized integrand compact. Therefore
\[
[F_D,\phi(a)]_{\mathrm{gr}}\phi(b),\quad
\phi(b)[F_D,\phi(a)]_{\mathrm{gr}}\in\mathcal K(E).
\tag{2.6}
\]

We still need the unlocalized commutator. For homogeneous \(a,b\in\mathcal A\), the Leibniz identity gives
\[
\begin{aligned}
\left[F_D,\phi(ab)\right]_{\mathrm{gr}}
&=[F_D,\phi(a)]_{\mathrm{gr}}\phi(b)\\
&\quad+(-1)^{|a|}\phi(a)[F_D,\phi(b)]_{\mathrm{gr}}.
\end{aligned}
\tag{2.7}
\]
Both terms are compact by (2.6). The linear span of products from the dense algebra \(\mathcal A\) is dense in \(A\): approximate an algebra approximate identity and any element by elements of \(\mathcal A\), then multiply. Finally \(\|[F_D,\phi(a)]_{\mathrm{gr}}\|\leq2\|a\|\) on each parity subspace. Norm closure of the compact operators proves the required compact commutator for all \(a\in A\). This proves all cycle axioms. \(\square\)

The factorization step (2.7) is particularly useful when the resolvent is compact only after source multiplication. It avoids treating (1.1) as a claim about a globally compact operator.

## 3. Making a bounded cycle unbounded

We now prove the converse existence theorem. Its construction uses a slowly growing inverse compact operator, with growth chosen to preserve a dense algebra of source elements.

**Lemma 3.1 (a controlled inverse).** Suppose \(F\) is an odd self-adjoint unitary on a countably generated \(E\), and \([F,\phi(a)]_{\mathrm{gr}}\) is compact. If \(A\) is separable, there is an even positive compact operator \(l\), of dense range and commuting with \(F\), such that for a dense graded \(*\)-algebra \(\mathcal A\),
\[
\begin{gathered}
\phi(a)\operatorname{Ran}l\subset\operatorname{Ran}l,\\
[l^{-1},\phi(a)],\qquad
[F,\phi(a)]_{\mathrm{gr}}l^{-1}
\end{gathered}
\tag{3.1}
\]
extend to bounded adjointable operators.

**Proof.** [Lesson 05, Lemma 2.0](KT-KK-05.html#lemma-2-0-compact-module-operators-and-their-multipliers) supplies an even strictly positive \(h_0\in\mathcal K(E)\) from a countable homogeneous generating family. Put
\(h=h_0+Fh_0F\). It is even, positive, strictly positive and commutes with \(F\), since \(F^2=1\). For the strict positivity, \(h\geq h_0\) and \(e_\delta=h(h+\delta)^{-1}\) give \(0\leq(1-e_\delta)h_0(1-e_\delta)\leq\delta/4\); hence \((1-e_\delta)h_0^{1/2}\to0\) in norm. Density of \(h_0^{1/2}E\) proves vector convergence of \(e_\delta\) to one, and rank-one approximation makes it an approximate identity of \(\mathcal K(E)\). Take a countable homogeneous family \(a_j\), closed under adjoints, with dense linear span in \(A\); include its identity in that family when \(A\) is unital. Write \(k_j=[F,\phi(a_j)]_{\mathrm{gr}}\).

The increasing quasicentral [construction of Lemmas 1.1–1.2 in *Kasparov's technical theorem*](KT-KK-08.html#1-approximate-identities-with-commutator-control) gives positive contractions \(u_n\in C^*(h)\), supported away from zero in \(\sigma(h)\), with \(u_{n+1}u_n=u_n\), forming an approximate identity of \(\mathcal K(E)\), and with
\[
\|[u_n,\phi(a_j)]\|,\quad
\|k_j(1-u_n)\|\leq2^{-n}\qquad(j\leq n).
\tag{3.2}
\]
The compact ideal is derived by every \(\phi(a_j)\), so those are legitimate commutator tests. All these cutoffs are even and commute with \(F\).

On \(\sigma(h)\setminus\{0\}\) form the continuous function
\[
r=1+\sum_{n=1}^\infty(1-u_n),\qquad l=r^{-1}.
\tag{3.3}
\]
The sum is locally finite. Indeed, wherever a cutoff \(u_N\) is positive, the nesting makes \(u_n=1\) for every \(n>N\); every compact spectral subset away from zero is covered by finitely many such neighborhoods. Also \(r\to\infty\) as the spectral variable tends to zero, because each finite collection of cutoffs vanishes near zero. Thus \(l\) extends continuously by zero at zero and belongs to \(C^*(h)\). It is strictly positive there. Its functional-calculus approximate identity also approximates \(h\), hence all of \(\mathcal K(E)\), so \(\operatorname{Ran}l\) is dense in \(E\). The initial \(1\) ensures \(r\geq1\) everywhere.

Let \(R=l^{-1}\) on \(\operatorname{Ran}l\) and
\(R_N=1+\sum_{n=1}^N(1-u_n)\).
The operators \(lR_N\) are contractions converging strongly to \(1\). Check this first on \(u_mE\), where the series is finite, and then use density. Therefore \(R_N\xi\to R\xi\) for \(\xi\in\operatorname{Dom}R=\operatorname{Ran}l\).

For each fixed \(j\), the commutators \([R_N,\phi(a_j)]\) converge in norm to an adjointable operator \(C_j\), by (3.2). Hence, for \(\xi\in\operatorname{Dom}R\),
\[
R_N\phi(a_j)\xi\longrightarrow
\phi(a_j)R\xi+C_j\xi.
\]
Multiplying this convergent sequence by \(l\), and using \(lR_N\to1\), proves that \(\phi(a_j)\xi\) is in \(\operatorname{Ran}l\), and identifies its inverse image as the displayed limit. This proves domain preservation and \([R,\phi(a_j)]=C_j\); it does not rely on boundedness of a sequence implying membership in an unbounded domain.

Similarly
\[
k_jR_N=k_j+\sum_{n=1}^Nk_j(1-u_n)
\]
converges in norm to an adjointable operator, again by (3.2). On \(\operatorname{Dom}R\) its limit is \(k_jR\). Here are the product and adjoint checks. If \(R=l^{-1}\), \(\epsilon_a=(-1)^{|a|}\), and \(k_a=[F,\phi(a)]_{\rm gr}\), then on its invariant domain
\[
[R,\phi(ab)]=[R,\phi(a)]\phi(b)+\phi(a)[R,\phi(b)],\qquad
k_{ab}R=(k_aR)\phi(b)-k_a[R,\phi(b)]+\epsilon_a\phi(a)(k_bR).
\]
Thus both required extensions remain bounded adjointable under products and sums. Adjoints preserve domain invariance because the generating family was closed under adjoints, and \(k_{a^*}=-\epsilon_a k_a^*\) gives the adjoint relation. The \(*\)-algebra generated by the family without formally adjoining an identity is the required dense graded algebra. In the unital case the identity was included among the controlled generators. In fact the constructed extensions for the original generators are compact, since their partial-sum commutators and products are compact and converge in norm. \(\square\)

**Theorem 3.2 (existence of unbounded representatives).** For separable graded \(A\), every class of \(KK(A,B)\) is represented by the bounded transform of an unbounded Kasparov module. The coefficient algebra \(B\) need not be separable or \(\sigma\)-unital.

**Proof.** [Theorem 3.2 of *Kasparov modules and the groups \(KK(A,B)\)*](KT-KK-06.html#theorem-3-2-odd-self-adjoint-normalization) supplies an operator-homotopic representative with exact odd self-adjoint unitary \(F\), on a countably generated module. Its doubled zero-representation summand is part of that construction, so no unsupported exact-square perturbation is needed.

Choose \(l\) by Lemma 3.1 and define
\[
D=Fl^{-1},\qquad\operatorname{Dom}D=\operatorname{Ran}l.
\tag{3.4}
\]
This domain is dense, graded, and invariant under \(F\). The operator is closed and symmetric: \(l^{-1}\) is the inverse of a bounded positive injective operator of dense range, and \(F\) commutes with \(l\).
For completeness its inverse resolvents are explicitly
\[
(D\pm i)^{-1}=l(F\pm il)^{-1}
=l(F\mp il)(1+l^2)^{-1}.
\tag{3.5}
\]
Their products with \(D\pm i\) on the dense domain are identity, and their ranges are exactly \(\operatorname{Ran}l\). Symmetry and surjectivity of both \(D\pm i\) imply self-adjointness: for a vector in \(\operatorname{Dom}D^*\), subtract the domain vector with the same image under \(D^*\pm i\); the remainder is orthogonal to the surjective range of \(D\mp i\), hence zero. The product of the two resolvents gives the inverse of \(1+D^2\), with range \(\operatorname{Dom}D^2\), proving regularity.

Now
\[
(1+D^2)^{-1}=l^2(1+l^2)^{-1}\in\mathcal K(E).
\]
For homogeneous \(a\in\mathcal A\), Lemma 3.1 gives the domain identity
\[
[D,\phi(a)]_{\mathrm{gr}}
=F[l^{-1},\phi(a)]
 +[F,\phi(a)]_{\mathrm{gr}}l^{-1},
\tag{3.6}
\]
whose right side is bounded adjointable. Thus this is an unbounded module, even with globally compact resolvent.

Its bounded transform is
\[
F_D=F(1+l^2)^{-1/2}.
\tag{3.7}
\]
The continuous function \((1+x^2)^{-1/2}-1\) vanishes at \(x=0\), so \(F_D-F\) is compact. The compact perturbation rule identifies their classes. This proves the theorem. \(\square\)

This is an existence theorem for a representative. It does not assert that an arbitrary equivalence between two unbounded operators is a bounded perturbation or a path on their original domains.

## 4. Spectral triples and the circle

A **spectral triple** is the Hilbert-space case: a dense \(*\)-algebra \(\mathcal A\) represented on a separable Hilbert space, a self-adjoint \(D\) with bounded commutators on \(\mathcal A\), and locally compact resolvent. An even triple has a grading commuting with the representation and anticommuting with \(D\). An odd triple has no grading. Theorem 2.2 gives its even Fredholm module; in the odd case tensor with the right Clifford generator as in the odd cycle construction.

The regularity of an unbounded Hilbert-module operator means the graph/resolvent property used above. The **smooth regularity** of a spectral triple usually asks for iterated bounded commutators with \(|D|\). These are different uses of the word regular.

**Proposition 4.1 (the circle triple).** On \(H=L^2(\mathbb R/2\pi\mathbb Z)\), with multiplication representation,
\[
De_n=ne_n,\qquad
\operatorname{Dom}D=
\left\{\sum_nx_ne_n:\sum_n(1+n^2)|x_n|^2<\infty\right\}
\tag{4.1}
\]
defines an odd unbounded module for \(C(\mathbb T)\), with smooth algebra \(C^\infty(\mathbb T)\).

**Proof.** [Lesson 03, Lemma 5.0](KT-KK-03.html#lemma-5-0-the-fourier-basis-used-in-the-examples) proves the Fourier-basis completeness and uniform trigonometric density used here. The real diagonal operator on the displayed domain is self-adjoint: its adjoint domain is obtained by testing against each Fourier basis vector and requiring the same square-summable sequence \(nx_n\). Its inverse resolvents have diagonal entries \((n\pm i)^{-1}\), giving regularity. The resolvent \((1+D^2)^{-1}\) has diagonal entries tending to zero and is the norm limit of its finite Fourier truncations.

For smooth \(g\), multiplication preserves the first Sobolev domain: the product rule, first for trigonometric polynomials and then by smooth approximation, bounds its graph norm by a constant times \(\|g\|_\infty+\|g'\|_\infty\). On that domain
\[
[D,M_g]=-iM_{g'}.
\]
This is bounded. Smooth functions are uniformly dense in \(C(\mathbb T)\), proving every unbounded-module condition. \(\square\)

Its bounded transform has Fourier eigenvalues \(n/\sqrt{1+n^2}\). It differs compactly from \(r=2P-1\), where \(P\) selects \(n\geq0\), because the diagonal difference tends to zero in both directions. Its compression pairing with the positive coordinate unitary is therefore the unilateral-shift index \(-1\).

We use the usual \((1,0)\) pseudodifferential calculus. In a bundle chart, a symbol of order \(m\) is a smooth matrix function satisfying
\[
\|\partial_x^\alpha\partial_\xi^\beta a(x,\xi)\|
\le C_{\alpha\beta}\langle\xi\rangle^{m-|\beta|},
\qquad \langle\xi\rangle=(1+|\xi|^2)^{1/2},
\tag{4.3}
\]
on every compact coordinate set. Quantization has phase \(e^{i(x-y)\cdot\xi}\). Classical symbols, with homogeneous principal part, are included. Ellipticity means that the full symbol is invertible for sufficiently large \(|\xi|\), uniformly on compact coordinate sets, with inverse bounded by \(C\langle\xi\rangle^{-m}\). For classical symbols this is equivalent to invertibility of the homogeneous principal symbol off the zero section. The following arguments also apply to nonclassical symbols satisfying these estimates and this ellipticity condition.

The finite-chart construction, smooth density, bounded smooth multiplication, and finite-rank approximation of \(H^1\hookrightarrow L^2\) are proved in [*Fredholm modules and analytic K-homology*, Lemma 4.1a](KT-KK-03.html#lemma-4-1a-finite-chart-sobolev-density-and-compactness). We use that lemma for the Sobolev space and compact inclusion, and supply the pseudodifferential assertions here. Gerd Grubb's lecture notes *Distributions and Operators*, [Chapter 7](https://web.math.ku.dk/~grubb/dist7n.pdf), Sections 7.1–7.4, and [Chapter 8](https://web.math.ku.dk/~grubb/dist8n.pdf), Sections 8.1–8.2, treat the same symbol calculus and elliptic construction.

**Lemma 4.2a (symbol estimates and composition).** Let \(M\) be closed, with finite-rank Hermitian bundles and a smooth positive density. Operators in \(\Psi^m\) act boundedly \(H^{s+m}\to H^s\) for every real \(s\). In particular \(\Psi^0\) acts boundedly on \(L^2\). In compatible coordinates,
\[
a\# b-\sum_{|\alpha|<N}
\frac{1}{\alpha!}\,\partial_\xi^\alpha a\,D_x^\alpha b
\in S^{m+n-N}_{1,0},
\qquad D_x=\frac1i\partial_x,
\tag{4.4}
\]
when \(a\in S^m_{1,0}\), \(b\in S^n_{1,0}\). The formal adjoint has order \(m\), with principal symbol the fibre adjoint of the principal symbol. Smooth kernels form a two-sided ideal in this calculus. For a smooth scalar \(g\),
\[
[P,M_g]\in\Psi^{m-1}.
\tag{4.5}
\]

**Proof: Fourier normalization and the local bound.** We use the unitary normalization
\(\widehat u(\xi)=(2\pi)^{-d/2}\int e^{-ix\cdot\xi}u(x)\,dx\)
in a chart of dimension \(d\). Its inversion and norm identity can be seen directly on Schwartz functions. Inserting \(e^{-\varepsilon|\xi|^2}\) into the pairing of two Fourier transforms and applying Fubini gives the pairing with convolution by
\[
G_\varepsilon(x)=(4\pi\varepsilon)^{-d/2}
e^{-|x|^2/(4\varepsilon)}.
\]
The one-variable Gaussian Fourier formula follows by differentiating its integral in the frequency variable and integrating by parts: the integral satisfies \(J'(t)=-tJ(t)/(2\varepsilon)\). Its value at zero is \(\sqrt{\pi/\varepsilon}\), obtained by squaring the integral and using polar coordinates. Taking products proves the displayed formula in dimension \(d\). The kernels \(G_\varepsilon\) have integral one and mass tending to zero outside every fixed ball. Splitting the convolution at that ball proves convergence to the original Schwartz function in \(L^2\), and pointwise for the inversion formula. Integration by parts makes Fourier transforms of Schwartz functions rapidly decreasing, so dominated convergence removes the Gaussian from the Fourier pairing. This proves Parseval and inversion on that space. The smooth-density construction of Lemma 4.1a, applied on increasing cubes, gives its density in \(L^2(\mathbb R^d)\); inversion then extends the transform to a unitary. Define \(H^s(\mathbb R^d)\) by the Fourier norm \(\|\langle\xi\rangle^s\widehat u\|_2\).

For a left symbol compactly supported in \(x\), integration by parts in \(x\) gives, for any prescribed \(L\),
\[
\|\widehat a(\eta-\xi,\xi)\|
\le C_L\langle\eta-\xi\rangle^{-L}\langle\xi\rangle^m.
\]
Here \(C_L\) uses finitely many \(x\)-derivative seminorms in (4.3). The Fourier kernel for the map \(H^{s+m}\to H^s\) is therefore bounded by
\[
C_L\langle\eta-\xi\rangle^{-L}
\frac{\langle\eta\rangle^s}{\langle\xi\rangle^s}
\le C_{L,s}\langle\eta-\xi\rangle^{-L+|s|}.
\tag{4.6}
\]
We used the elementary inequality
\(\langle v+w\rangle^r\le 2^{|r|/2}\langle v\rangle^r\langle w\rangle^{|r|}\),
valid for every real \(r\); for negative \(r\) apply the positive inequality to \(v=(v+w)-w\) and invert. Choosing \(L>d+|s|\) makes both kernel integrals bounded. If these bounds are \(A,B\), Cauchy–Schwarz with measure \(\|K(\eta,\xi)\|\,d\xi\), followed by Fubini, gives \(\|Ku\|_2^2\le AB\|u\|_2^2\). Thus (4.6) proves the local Sobolev assertion with a finite seminorm bound.

**Proof: the complete remainder estimate.** We first allow a compactly supported amplitude \(A(x,y,\xi)\) satisfying (4.3), with derivatives in both \(x,y\). Its left symbol is
\[
c(x,\xi)=(2\pi)^{-d}\operatorname{Os}\!\int
e^{-iz\cdot\eta}A(x,x+z,\xi+\eta)\,dz\,d\eta.
\tag{4.7}
\]
The notation \(\operatorname{Os}\) means the limit with smooth frequency regularizers. Integrating by parts with \((1-\Delta_z)^L\) introduces \(\langle\eta\rangle^{-2L}\); the \(z\)-support stays in a fixed compact set when \(x\) stays in one. The preceding weight inequality makes the resulting integral absolutely convergent for sufficiently large \(L\), after any fixed number of derivatives. This defines (4.7), independently of the regularizer, and gives \(c\in S^m_{1,0}\). Fourier inversion, first with regularizers, proves \(\operatorname{Op}(A)=\operatorname{Op}(c)\).

Taylor-expand the amplitude in the frequency increment \(\eta\), rather than changing its compact \(z\)-support. After \(N\) terms the remainder is a sum, over \(|\alpha|=N\), of
\[
\frac{N\eta^\alpha}{\alpha!}\int_0^1(1-t)^{N-1}
\partial_\xi^\alpha A(x,x+z,\xi+t\eta)\,dt.
\]
Transfer \(\eta^\alpha\) onto the amplitude by integration by parts in \(z\). Its coefficient becomes \((1/i)^{|\alpha|}\partial_y^\alpha\partial_\xi^\alpha A\), of order \(m-N\). Further integrations with \((1-\Delta_z)^L\) make the integrand bounded by
\[
C\langle\eta\rangle^{-2L}
\langle\xi+t\eta\rangle^{m-N}
\le C'\langle\xi\rangle^{m-N}
\langle\eta\rangle^{-2L+|m-N|},
\tag{4.8}
\]
uniformly for \(0\le t\le1\). Thus the integral is bounded in order \(m-N\). After \(\partial_x^\gamma\partial_\xi^\beta\), exactly the same argument gives order \(m-N-|\beta|\): total \(x\)-derivatives act on the two base variables, while each additional frequency derivative lowers the symbol order. Increase \(L\) for the finitely many derivatives being estimated. Every constant involves finitely many amplitude seminorms. The integrable majorants also justify removal of regularizers and differentiation under the integral. Fourier inversion evaluates each Taylor term at \(z=0\), giving
\[
c-\sum_{|\alpha|<N}\frac{1}{\alpha!}
D_y^\alpha\partial_\xi^\alpha A(x,y,\xi)\big|_{y=x}
\in S^{m-N}_{1,0}.
\tag{4.9}
\]

For composition the exact formula, derived by composing the two Fourier kernels, is
\[
(a\#b)(x,\xi)=(2\pi)^{-d}\operatorname{Os}\!\int
e^{-iz\cdot\eta}a(x,\xi+\eta)b(x+z,\xi)\,dz\,d\eta.
\tag{4.10}
\]
Local output cutoffs make the second factor compactly supported in \(z\). Taylor expansion of the first factor in \(\eta\) gives the terms of (4.4). Its remainder has \(N\) frequency derivatives of \(a\), and transferring \(\eta^\alpha\) differentiates only \(b\) in \(z\). After additional \(z\)-integrations its absolute value is bounded by
\[
C\langle\xi\rangle^{m+n-N}
\langle\eta\rangle^{-2L+|m-N|}.
\]
For each extra frequency derivative distribute it between the factors; their orders add to \(m+n-N-|\beta|\). This proves every seminorm estimate in (4.4), not just its leading term. Input cutoffs are covered by (4.9) or by composition with their multiplication symbols.

**Proof: coordinate changes, adjoints and global spaces.** Away from \(x=y\), repeated integration by parts in \(\xi\) lowers the symbol order until the kernel and any prescribed derivatives have absolutely convergent integrals. Hence those pieces are smooth. Near the diagonal a change of coordinates \(\kappa\) has
\[
\kappa(x)-\kappa(y)=B(x,y)(x-y),\qquad
B(x,y)=\int_0^1D\kappa(y+t(x-y))\,dt.
\]
On a sufficiently small compact neighbourhood of the diagonal, \(B\) is invertible with bounded derivatives of its inverse. The substitution \(\eta=B(x,y)^T\xi\) restores the original phase. The resulting amplitude still has order \(m\): a base derivative introducing a factor \(\eta\) also introduces a frequency derivative of the original symbol, which lowers its order by one. Jacobians, density factors and bundle transition matrices have bounded derivatives there. Formula (4.9) reduces this amplitude to a left symbol. On the diagonal its leading term transforms by the cotangent coordinate map and the bundle maps. This proves the invariance of order and ellipticity. Choose local frames and multiply by the positive square root of the density to make the \(L^2\) coordinate map unitary; this treats arbitrary densities and requires no orientation.

The reversed conjugate-transpose kernel of a localized operator has amplitude \(a(y,\xi)^*\). Formula (4.9) shows that its left symbol is
\[
a^{\dagger}\sim\sum_\alpha\frac{1}{\alpha!}
D_x^\alpha\partial_\xi^\alpha(a(x,\xi)^*),
\tag{4.11}
\]
with remainder of order \(m-N\) after \(N\) terms. In these unitary density coordinates this is the formal \(L^2\) adjoint. Its leading term is \(a^*\), so its principal symbol is the fibre adjoint and its order is \(m\).

For completeness, the real-order global Sobolev comparison uses only the same chart bounds and elementary interpolation. A compactly supported coordinate pullback and frame change is bounded on nonnegative integer Sobolev spaces by the chain rule and change of variables. Its transpose has the same form, with a smooth Jacobian factor, so duality gives every negative integer order. The Fourier weighted spaces interpolate between consecutive integer orders. To verify this assertion, set \(r(z)=(1-z)r_0+zr_1\), \(\Lambda=\langle D\rangle\), and for vectors with compact Fourier support apply the three-lines estimate to
\(\langle\Lambda^{r(z)}T\Lambda^{-r(z)}f,h\rangle\).
First put bounded frequency projections on both sides of \(T\). This scalar function is then holomorphic and bounded on the closed strip. On each boundary line the imaginary powers are unitary, so the bounds are the two endpoint operator bounds times \(\|f\|_2\|h\|_2\). The three-lines estimate follows by applying the maximum-modulus principle on a rectangle to the normalized function times \(M_0^{z-1}M_1^{-z}e^{\varepsilon z^2}\), then increasing the rectangle's height and letting \(\varepsilon\downarrow0\). If an endpoint bound is zero, first replace it by a positive bound and then take its limit. The maximum-modulus and analytic-continuation inputs are proved in [*Cauchy's theorem for cycles and its consequences*, Theorems 3.2, 3.6–3.7](../foundations-of-von-neumann-algebras/cauchy-s-theorem-for-cycles-and-its-consequences.html#oa-fnd-ct-03): the disk mean-value identity forces any interior modulus maximum to be locally constant, and the identity theorem propagates this to the rectangle. For a compact-frequency input, Fatou's inequality for the output Fourier norm removes its increasing frequency projections; density then removes the input projections. This gives the intermediate operator bound \(M_0^{1-\theta}M_1^\theta\), and proves boundedness of each compact coordinate change for every real order.

Choose finitely many smooth real cutoffs \(\chi_j\), supported inside bundle charts, with \(\sum_j\chi_j^2=1\), and define the global \(H^s\) norm by the sum of the squared Fourier norms of their coordinate pieces. The coordinate-change bounds compare any two choices on a finite refinement of their overlaps. Localization \(u\mapsto(\chi_ju)_j\) and reconstruction \((v_j)_j\mapsto\sum_j\chi_jv_j\) are bounded, and their composite on sections is the identity. Local Fourier approximation, followed by a cutoff inside the chart, proves smooth density for these spaces. For \(s=1\) this is exactly the weak-derivative space of Lemma 4.1a; for negative orders it agrees with the corresponding dual distribution space. A finite chart sum now gives the asserted global \(H^{s+m}\to H^s\) bound.

A symbol in every negative order has a smooth kernel, since any kernel derivative is absolutely integrable in frequency after taking a sufficiently negative order. Conversely a compact smooth coordinate kernel has a rapidly decreasing left symbol, by Fourier integration by parts. Such a kernel maps every Sobolev order to every other one. To pass from those bounds to smoothness, if \(s>k+d/2\), Cauchy–Schwarz gives
\[
\int |\xi|^k|\widehat u(\xi)|\,d\xi
\le \left(\int\langle\xi\rangle^{-2(s-k)}\,d\xi\right)^{1/2}
\|u\|_{H^s}.
\]
Fourier inversion and dominated differentiation therefore give continuous derivatives through order \(k\), with this bound; local cutoffs give the same assertion on \(M\). Composing a smooth kernel with a pseudodifferential operator now gives a smooth kernel on either side: apply its Sobolev bounds, or those of its formal adjoint, to the smooth kernel sections and their parameter derivatives, then use this estimate. This proves the smooth ideal assertion and continuous preservation of smooth sections. Finally the leading term in (4.4) for \([P,M_g]\) is \(a g-g a=0\), because \(g\) is scalar; the remainder for \(N=1\) has order \(m-1\). On separated chart pieces both kernels are smooth. This proves (4.5) globally. \(\square\)

**Lemma 4.2b (elliptic parametrices and exact domains).** An elliptic \(P\in\Psi^m(V^0,V^1)\), \(m>0\), on a closed manifold has a two-sided parametrix \(Q\in\Psi^{-m}(V^1,V^0)\):
\[
PQ=1-R_1,\qquad QP=1-R_0,
\tag{4.12}
\]
with smooth kernels \(R_0,R_1\). Its smooth-domain graph closure has domain exactly \(H^m(V^0)\), which also equals
\[
\{u\in L^2(V^0):Pu\in L^2(V^1)
\text{ in distributions}\}.
\tag{4.13}
\]
Its graph norm is equivalent to the \(H^m\) norm. Its Hilbert-space adjoint is the closure of the formal adjoint, with domain \(H^m(V^1)\).

**Proof: inverse symbols and their summation.** On a zero-dimensional component all spaces are finite dimensional and all kernels are smooth; take \(Q=0\). On a positive-dimensional component, in each relatively compact chart ellipticity gives \(p^{-1}\) for large frequency. Differentiating \(p^{-1}p=1\) gives, for example,
\(\partial(p^{-1})=-p^{-1}(\partial p)p^{-1}\).
Induction with the product rule proves all the symbol bounds of order \(-m\): each frequency derivative lowers the combined order by one, and base derivatives preserve it. For a classical elliptic symbol, compactness of the unit cosphere first bounds the inverse of \(p_m\); since \(p-p_m\) has order \(m-1\), a finite-dimensional Neumann series makes \(p\) invertible for sufficiently large frequency and gives the same inverse bounds. Thus the stated ellipticity condition includes that classical case.

Cut the inverse off at bounded frequency to obtain \(q_0\in S^{-m}\). The composition estimate gives
\(r=1-p\#q_0\in S^{-1}\), on the smaller coordinate set under consideration. Use buffered coordinate cutoffs and localized symbol classes modulo \(S^{-\infty}\); all estimates are on one fixed compact set. The correction terms
\[
q_j=q_0\#r^{\#j}\in S^{-m-j},\qquad j\ge0,
\]
have the property
\[
p\#\sum_{j<N}q_j=1-r^{\#N}\pmod{S^{-\infty}}.
\tag{4.14}
\]
Composition is associative modulo smoothing because actual kernels compose associatively. Recovery from exponentials, as in (4.7), shows that two complete local symbols for the same near-diagonal kernel differ by \(S^{-\infty}\): the difference is a compact smooth kernel, whose Fourier transform is rapidly decreasing. Thus geometric cancellation gives the finite order assertion (4.14).

We give the summation, without presuming convergence of a geometric series of operators. Fix a smooth \(\chi\), zero near zero and one outside a larger ball. Choose increasing radii \(R_j\to\infty\) so that, for the first \(j\) derivative seminorms, \(\chi(\xi/R_j)q_j\) has seminorm at most \(2^{-j}\) when measured in order \(-m-j/2\). This is possible because \(q_j\) has the stronger order \(-m-j\); on the cutoff's support its extra weight is at most a constant times \(R_j^{-j/2}\). Derivatives of the cutoff have the same weighted gain. The series
\[
q=q_0+\sum_{j\ge1}\chi(\xi/R_j)q_j
\tag{4.15}
\]
converges in every seminorm of order \(-m\). For any fixed \(N\), the tail with \(j\ge2N\) converges in order \(-m-N\); the finitely many remaining terms with \(j\ge N\) already have that order. The difference between any term and its cutoff has bounded frequency support and is smoothing. Consequently
\(q-\sum_{j<N}q_j\in S^{-m-N}\).
Equations (4.4) and (4.14) give \(p\#q-1\in S^{-N}\) for every \(N\), so its kernel is smooth. A fixed cutoff near the diagonal makes the local quantization properly supported; changing that cutoff changes only a smooth off-diagonal kernel.

**Proof: gluing the inverse.** Take a finite partition of unity \(\psi_j\) with supports compactly inside bundle charts. Choose \(\zeta_j=1\) near \(\operatorname{supp}\psi_j\) and \(\theta_j=1\) near \(\operatorname{supp}\zeta_j\), all supported in the same chart. Let \(Q_j\) be the local right parametrices just constructed on these buffered sets, and set
\(Q_R=\sum_j\zeta_jQ_j\psi_j\), carried back to the bundles on \(M\).
The local calculation gives \(P Q_j=1\) modulo a smooth kernel. Inserting \(\zeta_j\) does not change this on inputs supported in \(\operatorname{supp}\psi_j\), modulo a smooth kernel: \((1-\zeta_j)Q_j\psi_j\) has separated coordinate supports and is smooth. The output outside \(\theta_j\) is also a separated-support smooth kernel. The smooth ideal assertion in Lemma 4.2a therefore gives
\(P Q_R=\sum_j\psi_j\) modulo a smooth kernel, hence \(P Q_R=1-R_1\).
All sums are finite, with fixed supports; no sum of growing operator supports is involved.

Apply the same right-inverse construction to the elliptic formal adjoint \(P^{\dagger}\), and take its formal adjoint. This gives \(Q_L\in\Psi^{-m}\) with \(Q_LP=1-R'_0\). The exact identity
\[
Q_L-Q_R=Q_LR_1-R'_0Q_R
\]
makes their difference smooth. Therefore \(Q_RP-1\) is smooth too. Taking \(Q=Q_R\) proves (4.12) for arbitrary bundles. The identities extend to distributions by transposition: all the operators and their formal adjoints preserve smooth sections continuously, and the kernels have compact support in \(M\times M\).

**Proof: the closed and adjoint domains.** The Sobolev bounds give
\(P:H^m\to L^2\), \(Q:L^2\to H^m\), and \(R_0:L^2\to H^m\).
For \(u\in L^2\) with \(Pu=f\in L^2\) distributionally, (4.12) gives the actual distribution identity
\[
u=Qf+R_0u\in H^m,
\qquad
\|u\|_{H^m}\le C(\|f\|_2+\|u\|_2).
\tag{4.16}
\]
Conversely an \(H^m\) section has \(Pu\in L^2\). This proves (4.13). The reverse graph bound follows from boundedness of \(P:H^m\to L^2\).

The smooth-domain operator is closable: if \(u_k\to0\) and \(Pu_k\to f\) in \(L^2\), then for every smooth test \(v\),
\(\langle f,v\rangle=\lim_k\langle u_k,P^{\dagger}v\rangle=0\),
and smooth density gives \(f=0\). Smooth \(H^m\) approximation and its bounded \(P\)-image put all of \(H^m\) in the graph closure. Conversely a graph-Cauchy sequence is \(H^m\)-Cauchy by (4.16), so its \(L^2\) limit belongs to \(H^m\). This proves the minimal-domain assertion and closedness.

Testing the Hilbert adjoint identity on every smooth section says exactly that \(P^{\dagger}v\) is an \(L^2\) distribution. The formal adjoint has symbol \(p^*+S^{m-1}\) by (4.11); the inverse bound for \(p^*\) and a Neumann series make it elliptic. Applying the already proved maximal-domain assertion to it puts \(v\) in \(H^m(V^1)\). Conversely approximation of an \(H^m\) vector passes the formal adjoint identity to the graph closure. Thus the adjoint of the closure is precisely the closed \(P^{\dagger}\) on \(H^m(V^1)\). \(\square\)

**Proposition 4.2 (closed-manifold elliptic examples).** Let \(P:C^\infty(M,V^0)\to C^\infty(M,V^1)\) be an elliptic pseudodifferential operator of order one on a closed manifold. Its closed realization gives the even unbounded module
\[
\left(L^2(V^0)\oplus L^2(V^1),\,M_g,\,
\begin{pmatrix}0&P^*\\P&0\end{pmatrix}\right)
\tag{4.2}
\]
over \(C(M)\), with smooth source \(C^\infty(M)\). Its domain is exactly \(H^1(V^0)\oplus H^1(V^1)\). In particular this applies to the spin\(^c\) Dirac operator.

**Proof.** Write \(P\) for its graph closure and \(P^{\dagger}\) for its smooth formal adjoint. Lemma 4.2b proves
\(\operatorname{Dom}P=H^1(V^0)\),
\(\operatorname{Dom}P^*=H^1(V^1)\),
and identifies \(P^*\) with the closure of \(P^{\dagger}\).
On smooth sections the doubled operator \(D\) in (4.2) is formally self-adjoint. Its leading matrix has off-diagonal blocks \(p^*,p\), and its inverse is bounded in order \(-1\) when \(p\) is elliptic. The remaining symbol has order zero, so another Neumann series proves ellipticity of \(D\), including the nonclassical case. Lemma 4.2b applied to this doubled operator proves that its smooth-domain closure has the displayed \(H^1\) domain and equals its Hilbert adjoint. This closure is the operator matrix in (4.2), since smooth approximation converges in the graph norms of both blocks. Thus \(D\) is self-adjoint on that exact domain.

For \(u\) in that domain,
\(\|(D\pm i)u\|_2^2=\|Du\|_2^2+\|u\|_2^2\).
The range of \(D\pm i\) is closed by this identity and closedness of \(D\); its orthogonal complement is \(\ker(D\mp i)=0\), by self-adjointness and the same identity. Therefore both inverse resolvents exist with norm at most one. The estimate (4.16) makes them bounded \(L^2\to H^1\). Composing with the compact inclusion of Lemma 4.1a proves they are compact on \(L^2\). Their product is \((1+D^2)^{-1}\), so the required resolvent square is compact as well. The two inverse resolvents also show that \(1+D^2\) is onto, hence regular in the Hilbert-module sense of Lemma 0.0. The Hilbert space is separable: the finite-chart Fourier approximation in Lemma 4.1a gives a countable dense family, and hence it is countably generated as a \(\mathbb C\)-module.

Smooth scalar multiplication preserves the \(H^1\) domain by Lemma 4.1a. Lemma 4.2a gives \([P,M_g]\) and \([P^{\dagger},M_g]\) of order zero, bounded on \(L^2\); their two blocks give the bounded commutator \([D,M_g]\). The identity first holds on smooth sections and then on the entire domain by graph approximation. The grading \(\Gamma=\operatorname{diag}(1,-1)\) preserves the domain, commutes with scalar multiplication and anticommutes with \(D\). Smooth functions are uniformly dense in \(C(M)\), again by Lemma 4.1a. This verifies every unbounded-module condition, and Theorem 2.2 gives its even bounded cycle. For a spin\(^c\) Dirac operator, \([D,M_g]\) is Clifford multiplication by \(dg\), as follows directly from its connection product rule. \(\square\)

## 5. Recognizing unbounded products

Let \((E_1,\phi_1,D_1)\) and \((E_2,\phi_2,D_2)\) be unbounded modules. Put \(E=E_1\widehat\otimes_{\phi_2}E_2\), and \(S=D_1\widehat\otimes1\). Local Lemma 0.0 defines this self-adjoint regular tensor extension and proves its functional calculus identity for arbitrary correspondences. Suppose \(D\) is another odd self-adjoint regular operator making an unbounded module on \(E\), with the tensor source representation.

**Lemma 5.1 (an unbounded connection becomes a bounded one).** Suppose a homogeneous subspace \(\mathcal X\) dense in \(E_1^0=\overline{\phi_1(A)E_1}\) has the domain inclusions for the creation operator \(T_x\) and its adjoint, and
\[
DT_x-(-1)^{|x|}T_xD_2,\qquad
T_x^*D-(-1)^{|x|}D_2T_x^*
\tag{5.1}
\]
extend boundedly and adjointably. Then \(F_D\) satisfies the \(F_{D_2}\)-connection conditions for every \(x\in E_1^0\). If \(\mathcal X\) is dense in the whole first module, this is a full connection. No essentiality assumption on the first source representation is needed.

**Proof.** On \(E\oplus E_2\), treat the creation and adjoint as the two off-diagonal blocks of a homogeneous operator \(X_x\). The domain assumptions and (5.1) give its bounded graded commutator with \(D\oplus D_2\). The proof of Lemma 2.1 applies verbatim to this represented bounded operator, without requiring it to be a source element. Its bounded-transform commutator, after right multiplication by any operator \(b\) with \((1+(D\oplus D_2)^2)^{-1/2}b\) compact, is compact, by the same norm-integrable resolvent products.

Take homogeneous \(d\) in the second smooth source and use the right multiplier \(\operatorname{diag}(0,\phi_2(d))\). Its localized square-root resolvent is compact by Lemma 1.1. The top-right block of the preceding estimate makes
\[
\bigl(F_DT_x-(-1)^{|x|}T_xF_{D_2}\bigr)\phi_2(d)
\]
compact. Since \(T_{xd}=T_x\phi_2(d)\), moving \(F_{D_2}\) across \(\phi_2(d)\) adds its compact source commutator. Thus the connection error for \(xd\) is compact. Taking adjoints gives its other creation condition. The linear span of \(\mathcal X\mathcal B\) is dense in \(E_1^0\): the right coefficient action on this Hilbert submodule is nondegenerate, and the second smooth algebra \(\mathcal B\) is dense in that coefficient algebra. Norm continuity of \(x\mapsto T_x\) extends both conditions to every vector of that submodule. The same argument gives all of \(E_1\) when \(\mathcal X\) is dense there. \(\square\)

**Lemma 5.2 (alignment above minus two, with essential connections).** In the bounded product problem, let \(A\) be separable and the intermediate algebra \(B\) be \(\sigma\)-unital, let \(G\) be a self-adjoint contraction cycle, and suppose its \(F_2\)-connection conditions hold for all \(x\in\overline{\phi_1(A)E_1}\). If \(F_1\) is normalized and, for one \(0\leq\kappa<2\),
\[
\phi(a)[F_1\widehat\otimes1,G]_{\mathrm{gr}}\phi(a)^*
\geq-\kappa\phi(aa^*)\pmod{\mathcal K(E)}
\tag{5.2}
\]
for all \(a\), then \(G\) represents the product class.

**Proof.** First suppose the connection holds on the whole first module. Use the [technical-theorem partition in the uniqueness proof, Lesson 09 Theorem 4.1](KT-KK-09.html#4-uniqueness-and-descent-to-homotopy-classes), with \(G\) as its connection, and obtain the product
\(H=M^{1/2}(F_1\widehat\otimes1)+N^{1/2}G\), using its self-adjoint sandwich correction. The comparison sandwich of \([G,H]_{\mathrm{gr}}\) is
\[
\phi(a)M^{1/2}[G,F_1\widehat\otimes1]_{\mathrm{gr}}\phi(a)^*
 +2\phi(a)N^{1/2}\phi(a)^*.
\]
Compact commutation of the cutoffs and (5.2) bound it below by
\(-\kappa\phi(aa^*)\). In the [localized defect quotient of the cycle lesson](KT-KK-06.html#proposition-3-3-the-positive-comparison-criterion), \(G,H\) are self-adjoint unitaries with anticommutator at least \(-\kappa\). To see the lower-bound assertion there, apply its negative-part argument to the even pseudolocal operator \([G,H]_{\mathrm{gr}}+\kappa\): every source sandwich is positive, so its negative part is locally compact.

For \(L_t=(1-t)G+tH\), that quotient gives
\[
L_t^2\geq (1-t)^2+t^2-\kappa t(1-t)
\geq(2-\kappa)/4.
\]
Normalize \(L_t\) by continuous functional calculus, using
\((\max(L_t^2,\delta))^{-1/2}\), \(0<\delta<(2-\kappa)/4\). The resulting norm-continuous odd operators are self-adjoint unitaries in the defect quotient, hence cycles. Their endpoints differ locally compactly from \(G,H\) if an endpoint normalization was needed. This supplies an operator homotopy. Thus \(G\) has the product class in this case.

Here is the essential-source reduction, including the compact errors that a compression argument must retain. Write \(E_1^0=\overline{\phi_1(A)E_1}\), and \(E^0=\overline{\phi(A)E}\). The natural tensor identification
\[
E_1^0\widehat\otimes_B E_2\cong E^0
\]
is isometric and onto, by the balancing rule and the definition of the two closures. The essential-replacement construction in [Proposition 5.1 of *Connections and the existence of the Kasparov product*](KT-KK-09.html#5-essential-representations-and-homomorphisms), applied with intermediate algebra \(A\), supplies cycles \(F_1^0\) on \(E_1^0\) and \(G^0\) on \(E^0\), in the same homotopy classes as the original cycles. For homogeneous \(a\in A\) the adjointable multiplication maps
\[
A_a^1:E_1\to E_1^0,\qquad A_a:E\to E^0
\]
have adjoints given by multiplication by \(a^*\) followed by inclusion. Their connection errors are compact:
\[
\begin{gathered}
F_1^0A_a^1-(-1)^{|a|}A_a^1F_1\in\mathcal K(E_1,E_1^0),\\
G^0A_a-(-1)^{|a|}A_aG\in\mathcal K(E,E^0).
\end{gathered}
\tag{5.6}
\]
Normalize the replacement cycles; locally compact changes preserve (5.6).

The operator \(G^0\) is a full \(F_2\)-connection on \(E_1^0\). For \(x\in E_1\), the creation map for \(ax\) is \(A_aT_x\). Its connection error is the sum of the compact error from (5.6), composed with \(T_x\), and
\[
(-1)^{|a|}A_a\bigl(GT_x-(-1)^{|x|}T_xF_2\bigr).
\]
After inclusion into \(E\), the latter is compact, by the assumed connection for \(ax\) and the compact source commutator \([G,\phi(a)]_{\rm gr}\). It is compact with target \(E^0\) too: its adjointable \(R^*R\) is the same compact operator before and after isometric inclusion, and the \(R^*R\) compactness test proves the assertion. Adjointing gives the other creation condition. Density of the vectors \(ax\) proves the full connection.

For the positivity calculation we need one further consequence of the weak connection. If \(k\in\mathcal K(E_1)\), then
\[
\phi(a)[G,k\widehat\otimes1]_{\rm gr}\phi(b)\in\mathcal K(E)
\qquad(a,b\in A).
\tag{5.7}
\]
Indeed \(\phi_1(a)k\phi_1(b)\) is a norm limit of rank-one operators whose two vectors lie in \(E_1^0\). Their tensor images are \(T_xT_y^*\); moving \(G\) past each creation map and its adjoint makes their graded commutators compact, with the two \(F_2\) terms cancelling. Expand the commutator of \(\phi(a)(k\widehat\otimes1)\phi(b)\); its other terms contain the compact source commutators of \(G\). This proves (5.7).

Take an even \(c\in A\). By (5.6) the odd first-module operator
\[
R_c=(A_c^1)^*F_1^0A_c^1-\phi_1(c)^*F_1\phi_1(c)
\]
is compact. Put \(S^0=F_1^0\widehat\otimes1\). Moving \(G^0\) across \(A_c\) with (5.6), then sandwiching by \(\phi(d)\), gives
\[
\begin{aligned}
&\phi(d)^*A_c^*[S^0,G^0]_{\rm gr}A_c\phi(d)\\
&\quad\equiv
\phi(cd)^*[F_1\widehat\otimes1,G]_{\rm gr}\phi(cd)
\pmod{\mathcal K(E)} .
\end{aligned}
\tag{5.8}
\]
The omitted term is the sandwich of \([R_c\widehat\otimes1,G]_{\rm gr}\), compact by (5.7); the other omitted terms are the compact commutators of \(G\) with \(c\). Thus (5.2) transfers to \(G^0,S^0\).

For precision, positivity and compactness in this last transfer also hold on the essential submodule. The left side of (5.8), including the lower-bound correction, has both its range and its adjoint range in \(E^0\), and its restriction is the corresponding source sandwich on \(E^0\). Its negative part has the same range property. Local Lemma 0.2 proves that a compact operator on \(E\) whose range and adjoint range lie in \(E^0\) restricts compactly to that submodule, even without an adjointable projection. Its finite-column Gram-matrix norm identifies the two compact norms, and its compact-map argument justifies the approximate-identity sandwiches. This identifies the compact negative part on the submodule. Positive even approximate identities \(c\) give \(cd\to d\), so (5.2) holds for every source element on \(E^0\).

The full-connection case already proved applies to \(F_1^0,G^0,F_2\). Essential replacement and homotopy invariance of the product identify the original classes, proving the lemma in its stated generality. \(\square\)

**Lemma 5.3 (positivity after bounded transformation).** Let \(D,S\) be odd self-adjoint regular operators with \(\operatorname{Dom}D\subset\operatorname{Dom}S\). If
\[
2\operatorname{Re}\langle D\xi,S\xi\rangle
\geq-c\langle\xi,\xi\rangle\qquad(\xi\in\operatorname{Dom}D)
\tag{5.3}
\]
for \(c\geq0\), then \([F_D,F_S]_{\mathrm{gr}}\geq-c\).
Replacing \(S\) by \(\alpha S\) replaces this lower bound by \(-\alpha c\).

**Proof.** Write \(\lambda=1+u^2\), \(\mu=1+v^2\), and
\[
\begin{gathered}
r_D=(D^2+\lambda)^{-1},\quad h_D=Dr_D,\quad k_D=\sqrt\lambda\,r_D,\\
r_S=(S^2+\mu)^{-1},\quad h_S=Sr_S,\quad k_S=\sqrt\mu\,r_S.
\end{gathered}
\]
For \(\eta\in\operatorname{Dom}S\), the form \(Q(\xi)=2\operatorname{Re}\langle D\xi,S\xi\rangle\) satisfies
\[
Q(h_D\eta)+Q(k_D\eta)=2\operatorname{Re}\langle S\eta,h_D\eta\rangle.
\tag{5.4}
\]
Indeed \(Dh_D=1-\lambda r_D\) and \(Dk_D=\sqrt\lambda h_D\). Expanding the left side leaves the right side and the difference
\[
2\lambda\operatorname{Re}
\bigl(\langle h_D\eta,Sr_D\eta\rangle
-\langle r_D\eta,Sh_D\eta\rangle\bigr),
\]
which is zero by symmetry of \(S\). The domain inclusion legitimizes both terms. Apply (5.4) to \(h_S\psi\) and \(k_S\psi\), expand \(Sh_S=1-\mu r_S\), and cancel the remaining two terms by self-adjointness of \(h_D\). This gives
\[
\sum_{w\in\{h_Dh_S,k_Dh_S,h_Dk_S,k_Dk_S\}}Q(w\psi)
=2\operatorname{Re}\langle\psi,h_Dh_S\psi\rangle.
\tag{5.5}
\]

Integrate over \(u,v\geq0\), with coefficient \(4/\pi^2\), first on finite rectangles. Lemma (2.5) makes the right side converge to the quadratic form of \([F_D,F_S]_{\mathrm{gr}}\). On the left, (5.3) bounds every summand below by \(-c\langle w\psi,w\psi\rangle\). The integrated sum of these latter positive forms is at most \(\langle\psi,\psi\rangle\). To verify this, first use
\[
h_D^2+k_D^2=r_D,\qquad
\frac2\pi\int_0^\infty r_D\,du=(1+D^2)^{-1/2}\leq1.
\]
The two remaining \(S\)-sandwiches are therefore bounded by \(h_S^2+k_S^2=r_S\); their integral is likewise at most \(1\). These positive-form estimates also justify passage to the increasing rectangles without an absolute-integrability assertion for the original unsplit product. The lower bound follows for every \(\psi\), hence as an operator inequality. Scaling \(S\) scales the form bound (5.3), proving the final assertion. \(\square\)

**Theorem 5.4 (Kucerovsky's criterion).** Let \(A\) be separable and the intermediate algebra be \(\sigma\)-unital. Suppose (5.1) holds for a homogeneous subspace \(\mathcal X\subset\operatorname{Dom}D_1\) dense in \(\overline{\phi_1(A)E_1}\), suppose \(\operatorname{Dom}D\subset\operatorname{Dom}(D_1\widehat\otimes1)\), and suppose (5.3) holds with \(S=D_1\widehat\otimes1\). Then the bounded-transform class of \(D\) is the Kasparov product of the classes of \(D_1,D_2\). The first representation may be nonessential.

**Proof.** Theorem 2.2 supplies all three cycles. Lemma 5.1 supplies their essential-source connection condition. Choose \(\alpha>0\) with \(\alpha c<2\). Lemma 5.3 gives the alignment bound for \(F_D\) and \(F_{\alpha D_1}\widehat\otimes1\); functional calculus commutes with the tensor representation. Lemma 5.2 identifies the product.

The cycles of \(\alpha D_1\) and \(D_1\) have the same class. For \(t\in[\min(1,\alpha),\max(1,\alpha)]\), the functions \(tx/\sqrt{1+t^2x^2}\) vary uniformly in \(x\), continuously in \(t\). Their transforms are therefore a norm-continuous operator path. Each is a cycle by Theorem 2.2, since multiplication of \(D_1\) by a positive scalar preserves every domain and commutator condition and its locally compact functional calculus. The homotopy and product invariance finish the proof. \(\square\)

The positivity requirement is sufficient, rather than necessary. It is a bound on a quadratic form on the specified domain, not merely a symbolic anticommutator of differential expressions.

## 6. Connections and tensor sums

The expression \(1\widehat\otimes D_2\) usually fails to descend to the balanced tensor product. Acting on \(xb\widehat\otimes y\) and on \(x\widehat\otimes\phi_2(b)y\) produces a difference containing \([D_2,\phi_2(b)]_{\mathrm{gr}}\). A connection supplies exactly that correction.

For clarity first let the coefficient algebra and its dense smooth algebra be ungraded. Write \(\Omega^1(\mathcal B)\) for universal one-forms, with
\[
db=1\otimes b-b\otimes1,\qquad
\Omega^1(\mathcal B)=\ker(\mathcal B^+\otimes\mathcal B^+\to\mathcal B^+)
\]
on the relevant algebraic subspace. Their representation by \(D_2\) is
\(b_0\,db_1\mapsto\phi_2(b_0)[D_2,\phi_2(b_1)]\).
A connection on a dense right module \(\mathcal E_1\) satisfies
\[
\nabla(xb)=(\nabla x)b+x\otimes db.
\tag{6.1}
\]
After representing its one-forms, define on a suitable algebraic domain
\[
(1\widehat\otimes_\nabla D_2)(x\widehat\otimes y)
=(-1)^{|x|}x\widehat\otimes D_2y+(\nabla_{D_2}x)y.
\tag{6.2}
\]
Here \(\nabla_{D_2}x\) has degree \(|x|+1\). The represented Leibniz rule is
\[
\nabla_{D_2}(xb)
=(\nabla_{D_2}x)\phi_2(b)
 +(-1)^{|x|}T_x[D_2,\phi_2(b)].
\]
Inserting this rule in (6.2) proves that the two balanced tensors have the same image. The graded version puts the Koszul signs in this Leibniz rule and in the multiplication map; the creation-domain formulation (5.1) covers both versions.

The Hermitian condition says that
\[
(-1)^{|x|}[D_2,\phi_2(\langle x,x'\rangle)]
=T_x^*\nabla_{D_2}x'
-(\nabla_{D_2}x)^*T_{x'}
\tag{6.3}
\]
with the corresponding graded signs when the coefficient has odd elements. This is exactly the symmetry identity obtained by taking inner products of (6.2) on two elementary tensors. Symmetry by itself does not prove self-adjointness or regularity.

**Proposition 6.1 (a finite projective connection).** Let \(B\) be unital and trivially graded, let \(\phi_2\) be unital, and let \((E_2,\phi_2,D_2)\) be an unbounded module. Let \(p=p^*=p^2\in M_N(\mathcal B)\), an even projection on a graded free module, with its represented commutator with \(D_2^{\oplus N}\) bounded. Put \(E_1=pB^N\), with an even compact left action of a separable source and a dense smooth source algebra acting by matrices in \(pM_N(\mathcal B)p\). The closure on \(pE_2^N\) of
\[
D_p=pD_2^{\oplus N}p
\tag{6.4}
\]
is self-adjoint regular. For smooth source matrices it is an unbounded module whose class is the product of \((E_1,\phi_1,0)\) with the class of \(D_2\). The same is true after addition of a bounded odd self-adjoint connection endomorphism.

**Proof.** Write \(q=1-p\), \(\mathcal D=D_2^{\oplus N}\), with the grading signs on free coordinates. Bounded commutation makes \(p\operatorname{Dom}\mathcal D\subset\operatorname{Dom}\mathcal D\). The off-diagonal expression
\[
K=p\mathcal Dq+q\mathcal Dp
\]
extends to a bounded odd self-adjoint operator, because its entries are signed blocks of \([\mathcal D,p]\). Thus
\(\mathcal R=\mathcal D-K=p\mathcal Dp+q\mathcal Dq\)
on \(\operatorname{Dom}\mathcal D\).

A bounded self-adjoint perturbation of a self-adjoint regular operator remains so. Here is the needed argument: for \(\rho>\|K\|\), factor
\[
\mathcal R\pm i\rho
=\bigl(1-K(\mathcal D\pm i\rho)^{-1}\bigr)
(\mathcal D\pm i\rho).
\]
The first factor has its norm-convergent Neumann inverse. Both resolvents of \(\mathcal R\) are therefore adjointable with dense ranges; the symmetry and inverse-resolvent argument of Theorem 3.2 proves self-adjointness and regularity. The projection \(p\) commutes with these resolvents, so their restrictions give the inverse resolvents of \(D_p\) on \(pE_2^N\).

Because \(\phi_2(1)=1\), the original resolvents are globally compact. The displayed Neumann formula therefore makes \((\mathcal R\pm i\rho)^{-1}\) compact for \(\rho>\|K\|\). After self-adjoint regularity has been established, Lemma 0.0 gives the resolvents at every nonreal parameter. The resolvent identity
\[
(\mathcal R\pm i)^{-1}
=(\mathcal R\pm i\rho)^{-1}
\bigl(1\pm i(\rho-1)(\mathcal R\pm i)^{-1}\bigr)
\]
transfers compactness to \(\pm i\). Restriction to \(pE_2^N\) preserves compactness. Smooth represented matrix elements preserve the domain and have bounded commutators, by the product rule. These facts verify the unbounded-cycle conditions for the stated smooth left action.

For a smooth \(x\in pB^N\), its creation operator is the represented column, and
\[
D_pT_x-T_xD_2=p[\mathcal D,T_x],
\]
with the coordinate grading signs understood. The right side is a finite column of bounded represented derivatives. Taking adjoints proves the other condition. The first unbounded operator is zero on \(pB^N\), so its domain is all of that module, its localized resolvent is compact by the compact left action, and its positivity form is zero. Theorem 5.4 proves the product assertion.

A bounded odd self-adjoint endomorphism \(C\) of the final module preserves self-adjoint regularity by the same perturbation argument, preserves compact resolvent by the resolvent identity, and adds the bounded creation error \(CT_x\). Its source commutators are bounded. The same criterion, still with zero first operator, proves the final assertion. \(\square\)

Thus a Hermitian connection on a finite projective module gives its Grassmann operator (6.4) plus its represented bounded one-form matrix. For a vector bundle on a closed manifold this is the familiar twisted Dirac operator. The tensor identification and creation calculation agree with the [full twisting product, Lesson 09 Theorem 9.2](KT-KK-09.html#9-bundles-and-twisted-dirac-operators).

**Lemma 6.2 (a controlled tensor sum).** Let \(S,T\) be odd self-adjoint regular operators on a Hilbert module. Suppose, for every sufficiently large \(\rho>0\), all products
\[
(S\pm i\rho)^{-1}(T\pm i\rho)^{-1}
\]
and their adjoints have the same range \(W\), including the mixed choices of signs. Suppose \(ST+TS\), initially on \(W\), extends to a bounded adjointable self-adjoint \(K\). These are the resolvent-range and bounded-anticommutator conditions for an almost anticommuting pair. Then \(D=S+T\) is self-adjoint regular on
\(\operatorname{Dom}S\cap\operatorname{Dom}T\).
If a source representation has bounded commutators with \(S,T\) on a dense smooth algebra, and
\[
\phi(a)f(S)(T\pm i)^{-1}\in\mathcal K(E)
\qquad(f\in C_0(\mathbb R)),
\tag{6.6}
\]
with either choice of signs, then \(D\) has locally compact resolvent.

**Proof.** First spell out the domain consequences of the range assumption. An \(S\)-resolvent maps \(\operatorname{Dom}T\) into \(W\), because that domain is the range of a \(T\)-resolvent; reversing the factors gives the analogous assertion. A vector in \(W\) has both \(S\xi\in\operatorname{Dom}T\) and \(T\xi\in\operatorname{Dom}S\). For example, writing it as \((S-z)^{-1}\eta\), with \(\eta\in\operatorname{Dom}T\), gives \(S\xi=\eta+z\xi\in\operatorname{Dom}T\). Thus \(ST+TS=K\) on this genuine product domain. Multiplying this equality by the inverse resolvents gives, on \(\operatorname{Dom}T\),
\[
T(S-z)^{-1}
=-(S+z)^{-1}T+(S+z)^{-1}K(S-z)^{-1}.
\tag{6.10}
\]
All terms on the right are bounded for the \(T\)-graph norm. This also verifies domain preservation by the resolvent, rather than treating its formal commutator as sufficient.

Let \(P_n=n^2(S^2+n^2)^{-1}\), \(Q_n=n^2(T^2+n^2)^{-1}\), with \(n\) sufficiently large. Applying (6.10) twice gives the ordinary commutator
\[
[T,P_n]=-n^2(S^2+n^2)^{-1}
(KS-SK)(S^2+n^2)^{-1},
\]
as a bounded extension, of norm at most \(\|K\|/n\). The symmetric estimate holds for \([S,Q_n]\). Both \(P_nQ_n\) and its adjoint have range in \(W\). They converge strongly to \(1\), and their commutators with either \(S\) or \(T\) tend to zero in norm. Hence, for every vector in the joint domain,
\[
P_nQ_n\xi\longrightarrow\xi,\quad
SP_nQ_n\xi\longrightarrow S\xi,\quad
TP_nQ_n\xi\longrightarrow T\xi.
\]
This proves that \(W\) is a core for the joint graph norm. It is stronger than a separate-core assertion for the two operators.

On \(W\) expand the square, and then pass to this joint graph limit, to obtain on the whole intersection
\[
\langle D\xi,D\xi\rangle
=\langle S\xi,S\xi\rangle+\langle T\xi,T\xi\rangle
 +\langle\xi,K\xi\rangle.
\tag{6.7}
\]
It makes the graph norm of \(D\) equivalent to the joint graph norm. Thus \(D\) is closed and symmetric on the intersection.

The cutoffs above have commutators with \(D\) of norm at most \(2\|K\|/n\).

This proves self-adjointness directly. For \(\xi\in\operatorname{Dom}D^*\), adjointing the commutator identity on the common domain gives
\[
D(P_nQ_n)\xi
=(P_nQ_n)D^*\xi+[D,P_nQ_n]\xi.
\]
The left side is defined because the cutoff has range in the domain. Its two coordinates converge to \(\xi,D^*\xi\); closedness implies \(\xi\in\operatorname{Dom}D\).

To obtain regularity apply the symmetric local-global criterion proved here in Lemma 0.1. The Hilbert-space localizations of \(S,T\) are self-adjoint by its converse, or directly by the tensor-extension and resolvent proof of Lemma 0.0; the GNS representation identifies the state localization with that interior tensor product. For this identification, \(x\widehat\otimes\xi_\omega\mapsto j_\omega x\) preserves inner products and has dense range, and elementary \(x\widehat\otimes\pi_\omega(b)\xi_\omega\) reduce by balancing to \(xb\widehat\otimes\xi_\omega\). The localized \(S,T\) are self-adjoint, and (6.10) extends to their graph domains: approximate a graph-domain vector by algebraic localized vectors and use its bounded graph-norm right side and closedness. Thus their cutoff products again have range in the joint domain, the same commutator estimates hold, and the products form a joint core by the preceding three limits.

For fixed \(n\), the map \(P_nQ_n\) into this joint graph space is bounded: \(SP_n\) and \(TQ_n\) are bounded, and the remaining term is the bounded commutator. Approximate an arbitrary localized vector by algebraic localized vectors, then apply this map. Its images lie in the graph of the algebraic localization of \(D\). Conversely that graph lies in the joint graph space. Taking the joint-core limit and using (6.7) proves that the localization of \(D\) is exactly the closed localized sum on the joint domain. The Hilbert-space adjoint-domain argument above makes this operator self-adjoint. The local-global criterion now proves regularity of \(D\).

For compactness, (6.6) and continuous functional calculus imply
\[
\phi(a)f(S)g(T)\in\mathcal K(E)
\qquad(f,g\in C_0(\mathbb R)).
\tag{6.8}
\]
Indeed products of signed \(T\)-inverse resolvents uniformly generate \(C_0(\mathbb R)\). Keep \(f(S)\) fixed and approximate \(g(T)\) by finite linear combinations of these products. In each nonconstant product its first inverse resolvent supplies compactness by (6.6); the other factors are bounded. Norm closure proves (6.8). Requiring every \(f\) in (6.6) keeps this argument from presuming that a bounded source commutator is itself another source element.

Choose compactly supported spectral contractions \(f_n,g_n\), equal to one on \([-n,n]\), whose tails satisfy
\[
\|(1-f_n(S))(1+S^2)^{-1/2}\|,\quad
\|(1-g_n(T))(1+T^2)^{-1/2}\|\longrightarrow0.
\]
The joint graph estimate (6.7) bounds both
\((1+S^2)^{1/2}(D+i)^{-1}\) and
\((1+T^2)^{1/2}(D+i)^{-1}\).
It follows that
\(\phi(a)f_n(S)g_n(T)(D+i)^{-1}\)
converges in norm to \(\phi(a)(D+i)^{-1}\): first estimate the \(S\)-tail, then the \(T\)-tail, keeping the other cutoff a contraction. Every approximant is compact by (6.8). Adjointing gives the other localization. Thus the inverse resolvents of \(D\) are locally compact. \(\square\)

**Proposition 6.3 (the analytic connection construction).** Let \((E_1,\phi_1,D_1)\), \((E_2,\phi_2,D_2)\) be unbounded modules for \((A,B)\), \((B,C)\), where \(A\) is separable, \(B\) is \(\sigma\)-unital and \(C\) is any graded \(C^*\)-algebra. Suppose an even adjointable projection \(p\) identifies \(E_1=pH_B\), and the represented projection \(P=p\widehat\otimes1\) has a bounded commutator with the signed diagonal \(\mathcal D=D_2^{(\infty)}\). Let a Hermitian connection give
\[
T=P\mathcal DP+C
\quad\hbox{on }P(H\widehat\otimes E_2),
\tag{6.9}
\]
with bounded odd self-adjoint \(C\). Suppose \(S=D_1\widehat\otimes1\) and \(T\) satisfy the domain and bounded anticommutator assumptions of Lemma 6.2, and the smooth source preserves their domains with bounded commutators. Suppose the smooth creation errors in (6.2) are bounded on a dense domain. Then \(D=S+T\) is an unbounded product module.

**Proof.** The infinite diagonal \(\mathcal D\) is self-adjoint regular, with the coordinatewise inverse resolvents. The bounded off-diagonal commutator with \(P\) makes
\[
\mathcal D-P\mathcal D(1-P)-(1-P)\mathcal DP
\]
a bounded self-adjoint perturbation of \(\mathcal D\). It commutes with \(P\). The proof of Proposition 6.1, which used no finite-dimensional property in its regularity argument, therefore proves regularity and self-adjointness of (6.9).

For a compact \(k\in\mathcal K(H_B)\) and \(\rho>0\), the operator
\[
(k\widehat\otimes1)(\mathcal D\pm i\rho)^{-1}
\]
is compact on \(H\widehat\otimes E_2\). Approximate \(k\) by finite matrices over \(B\). Each matrix entry then has the form \(\phi_2(b)(D_2\pm i\rho)^{-1}\), compact by Lemma 1.1; finite matrix approximation proves the assertion.

Extend \(C\) by zero on \((1-P)(H\widehat\otimes E_2)\), and write \(\mathcal R=\mathcal D+Q\) for the preceding block-diagonal perturbation, so \(Q\) is bounded self-adjoint. For \(\rho>\|Q\|\),
\[
(\mathcal R\pm i\rho)^{-1}
=(\mathcal D\pm i\rho)^{-1}
\bigl(1+Q(\mathcal D\pm i\rho)^{-1}\bigr)^{-1}.
\]
The second factor has its norm-convergent Neumann inverse. Multiplying by \(k\widehat\otimes1\) gives compactness at this parameter. For \(k\in\mathcal K(E_1)\) extended by zero to \(H_B\), compression by \(P\) therefore gives
\((k\widehat\otimes1)(T\pm i\rho)^{-1}\in\mathcal K(E)\).
Self-adjoint regularity and the resolvent identity
\[
(T\pm i)^{-1}
=(T\pm i\rho)^{-1}
\bigl(1\pm i(\rho-1)(T\pm i)^{-1}\bigr)
\]
give the same localized compactness at \(\pm i\). This argument uses a Neumann inverse only at \(\rho>\|Q\|\).

For every \(f\in C_0(\mathbb R)\), local compactness of the first module makes \(\phi_1(a)f(D_1)\) compact on \(E_1\). Extend it by zero into \(\mathcal K(H_B)\) and use the preceding paragraph. Thus
\[
\phi(a)f(S)(T\pm i)^{-1}\in\mathcal K(E).
\]
This proves exactly the functional-calculus form (6.8) needed in Lemma 6.2, as well as (6.6). The lemma now proves self-adjoint regularity and local compactness of the tensor sum.

Its source commutators are the sum of the assumed bounded commutators. Its creation errors are the bounded connection errors plus \(T_{D_1x}\), bounded for \(x\) in the specified smooth \(D_1\)-domain. Finally
\[
2\operatorname{Re}\langle S\xi,D\xi\rangle
=2\langle S\xi,S\xi\rangle+\langle\xi,K\xi\rangle
\geq-\|K\|\langle\xi,\xi\rangle.
\]
All hypotheses of Theorem 5.4 are therefore met. This proves the unbounded product identification. \(\square\)

### 6.4. Mesland's general smooth product

Mesland's product theorem applies to countably generated smooth operator modules. We state it with the smooth data that its analytic conclusion requires. The conventions in this paragraph are those of *Spectral triples and KK-theory: a survey*, Sections 7–13; the corresponding constructions and proofs are in *Unbounded bivariant K-theory and correspondences in noncommutative geometry*, Sections 3–6.

An operator space \(X\) has the matrix norms inherited from a concrete inclusion in a \(C^*\)-algebra. A map \(u:X\to Y\) is completely bounded when \(\sup_n\|u_n:M_n(X)\to M_n(Y)\|<\infty\). The matrix Haagerup norm is
\[
\|z\|_{h,n}
=\inf\left\{\|v\|_{M_{n,r}(X)}\|w\|_{M_{r,n}(Y)}:
 z_{ij}=\sum_{\ell=1}^r v_{i\ell}\otimes w_{\ell j}\right\}.
\]
Its completion is denoted \(X\otimes_hY\). For operator modules, \(X\otimes_{h,\mathcal B}Y\) is its quotient by the closed span of \(xb\otimes y-x\otimes by\). The multiplication and module actions are required to be completely bounded in these norms. The involution on an involutive operator algebra is completely bounded into the conjugate opposite operator space; thus its matrix formulation includes transposition.

A \(C^k\)-structure on \(A\) is fixed by a defining spectral triple and its Sobolev operator algebras
\(\mathcal A_k\subset\cdots\subset\mathcal A_1\subset\mathcal A_0=A\).
Here \(\mathfrak G(D)\subset E\oplus E\) is the graph of \(D\); its next operator sends \((x,Dx)\) to \((Dx,D^2x)\), and iteration gives the graph scale. The first matrix representation is
\[
\pi_1(a)=
\begin{pmatrix}a&0\\ [D,a]_{\mathrm{gr}}&(-1)^{|a|}a\end{pmatrix}.
\]
Compression to the graph and its complementary graph gives \(\theta_1\); repeat this construction on successive graphs to define \(\pi_j,\theta_j\). At each step both \(a\) and \(a^*\) must preserve the relevant domain and have the required bounded graph commutator. The norm of \(\bigoplus_{i=0}^j\pi_i(a)\), and its matrix amplifications, gives the \(j\)-th operator-algebra topology. The top algebra is dense in \(A\). In the nonunital case use the positive countable approximate identity bounded in that topology, as in Definition 4.2.6 of the full paper.

A countably generated graded Hilbert \(B\)-module is \(C^k\) when it has a homogeneous frame \((x_\ell)\) such that the finite sums \(\sum_\ell\theta_{x_\ell,x_\ell}\) form an approximate identity for \(\mathcal K_B(E)\), and the finite Gram matrices \((\langle x_\ell,x_m\rangle)\) have uniformly bounded \(j\)-th matrix norm for \(j\leq k\). The frame coefficient maps give its operator-module scales \(E^j\), with \(E^0=E\). A \(C^k\)-bimodule has completely bounded left actions \(\mathcal A_j\to\operatorname{End}^*_{\mathcal B_j}(E^j)\). These are smooth module topologies; their norms are not defined solely by the \(B\)-valued inner product.

Write \(\operatorname{Sob}^j_i(D)\) for the operator algebra obtained by applying the preceding graph construction \(i\) times to an operator on the level-\(j\) module. In the survey convention a \(C^k\)-cycle has a \(C^k\)-bimodule and an odd self-adjoint regular operator on its \(C^{k-1}\) scale, extending to the lower scales, whose underlying Hilbert-module operator is an unbounded KK-cycle. It is **transverse** when
\[
\mathcal A_n\longrightarrow\operatorname{Sob}^j_i(D)
\quad\text{is completely bounded for }i+j=n\leq k.
\]
The relevant graph domains and adjoints are part of these requirements. They control the represented source on every indicated graph scale, rather than only on the Hilbert-module completion.

Use the unitization in universal one-forms when needed. In degree zero,
\(\Omega^1_h(\mathcal B_j)=\ker(\mathcal B_j^+\otimes_h\mathcal B_j^+\to\mathcal B_j^+)\) and \(db=1\otimes b-b\otimes1\); the graded version uses the graded multiplication and Koszul signs. A smooth universal connection is a completely bounded even map
\[
\nabla:E^k\longrightarrow E^k\otimes_{h,\mathcal B_k}\Omega^1_h(\mathcal B_k)
\]
satisfying the Leibniz rule. It is Hermitian when its two form-valued inner-product pairings satisfy
\(\langle x,\nabla y\rangle-\langle\nabla x,y\rangle=d\langle x,y\rangle\).
It is a **transverse \(C^k\)-connection** when its induced graph connections \(\theta_i(\nabla)\) have completely bounded commutators with the graph operator on \(\mathfrak G(D_i)^j\), for \(i+j\leq k\). Equivalently, for \(n\geq1\) and \(n+j\leq k\), both relative commutators
\[
(\operatorname{ad}D)^n(\nabla)(D\pm i)^{-n+1},
\qquad
(D\otimes1\pm i)^{-n+1}(\operatorname{ad}D)^n(\nabla)
\]
extend completely boundedly from \(E^j\) to \(E^j\otimes_{h,\mathcal B_j}\Omega^1_h(\mathcal B_j)\), with their domain-preserving graph interpretations. A geometric correspondence consists of this cycle and connection.

**Theorem 6.4 (Mesland's product, stated).** Fix separable graded \(C^k\)-algebras \(A,B,C\), \(k\geq2\), and geometric correspondences \((E_1,D_1,\nabla)\), \((E_2,D_2,\nabla')\) for \((A,B)\), \((B,C)\), with the transverse structures and Hermitian connections just specified. On \(E_1\widehat\otimes_B E_2\), the represented operator \(1\widehat\otimes_\nabla D_2\) is the self-adjoint regular closure of (6.2), initially on smooth tensors with \(x\in E_1^k\) and \(y\in\operatorname{Dom}(D_2|_{E_2^{k-1}})\). The sum is self-adjoint regular on
\[
\operatorname{Dom}(D_1\widehat\otimes1)
\cap\operatorname{Dom}(1\widehat\otimes_\nabla D_2).
\]
The product connection is obtained by representing the first connection through the derivation \(b\mapsto[\nabla',b]\) and adding the second connection on elementary tensors. Then
\[
(E_1,D_1,\nabla)\circ(E_2,D_2,\nabla')
=\bigl(E_1\widehat\otimes_B E_2,\,
D_1\widehat\otimes1+1\widehat\otimes_\nabla D_2,\,
1\widehat\otimes_\nabla\nabla'\bigr)
\tag{6.5}
\]
is again a transverse \(C^k\)-cycle with connection. Its bounded-transform class is
\[
[D_1\widehat\otimes1+1\widehat\otimes_\nabla D_2]
=[D_1]\widehat\otimes_B[D_2]\quad\text{in }KK(A,C).
\]
The smooth tensor scales use the balanced Haagerup completions; at level zero their Hilbert-module realization is the interior tensor product. Composition is associative under the canonical tensor identifications, intertwining the operators, connections and graph scales. For correspondences implementing the specified unitary factorizations of spectral triples, this gives a category and a bounded-transform functor to KK-theory.

For identifying a KK-product alone, the transverse \(C^1\)-cycle and connection hypotheses suffice. The assertion that the product connection retains the full \(C^k\)-structure above uses the survey's \(k\geq2\) hypothesis. No finite projectivity or finite-dimensional source is required. This is [Mesland's survey, Theorem 13.36 and Remark 13.37](https://arxiv.org/pdf/1304.3802v1), with Definitions 10.24, 10.30, 11.32 and 12.34–12.35. The full paper gives the induced graph operator in Theorem 5.4.1, the sum and graph-scale construction in Theorems 6.2.5 and 6.2.7 and Lemma 6.2.6, and the compactness and KK identification in [Theorems 6.3.3–6.3.4](https://arxiv.org/pdf/0904.4383v5).

The hypotheses of Proposition 6.3 are explicit conditions on the Hilbert-module projection, represented connection, resolvent ranges and bounded anticommutator. Its local proof, and the torus product below, use those conditions directly. Theorem 6.4 supplies the general smooth correspondence statement.

## 7. Exercises

**7.1. Circle domains.** Prove that \(-i\,d/d\theta\) defines the odd circle module, including self-adjointness, compact resolvent, smooth domain preservation and the sign of its coordinate pairing.

**7.2. Compact bounded-transform commutators.** Prove compactness of \([F_D,\phi(a)]_{\mathrm{gr}}\) from the resolvent integral when the source is nonunital. Identify the step that upgrades localized compactness.

**7.3. Spectral triples.** Show that an even or odd spectral triple defines a Fredholm module. Explain why summability and smooth regularity are additional conditions.

**7.4. Two circles.** Construct an even unbounded cycle on the torus from two circle Dirac operators. Prove its domain, compactness and commutator assertions, verify the product conditions in Kucerovsky's criterion, and compare its Clifford orientation with the earlier bounded product.

## 8. Solutions

**Solution to 7.1.** The Fourier calculation gives precisely domain (4.1). Testing the adjoint on each Fourier vector shows that an adjoint-domain vector has square-summable coefficients \(nx_n\), hence belongs to that domain; the operator is self-adjoint. Its inverse resolvents are the bounded diagonal operators \((n\pm i)^{-1}\), and the resolvent square has eigenvalues \((1+n^2)^{-1}\), uniformly approximable by finite Fourier truncations. For smooth \(g\), the Sobolev product rule makes \(M_g\) bounded for the graph norm, preserving the domain; its commutator is \(-iM_{g'}\). These facts prove the unbounded-module assertions. Its bounded transform differs compactly from \(2P-1\), with \(P\) the nonnegative-mode projection. Compressing the positive coordinate gives the unilateral shift, whose kernel is zero and cokernel one dimensional. The pairing is \(-1\).

**Solution to 7.2.** For \(c=[D,\phi(a)]_{\mathrm{gr}}\), formula (2.3) expresses the commutator of \(D(D^2+1+t^2)^{-1}\) as two products of inverse resolvents and \(c\). Its norm is bounded by \(\|c\|/(1+t^2)\); multiplication on the right by \(\phi(b)\) puts a compact localized inverse resolvent at its right end. Norm integration proves \([F_D,\phi(a)]_{\mathrm{gr}}\phi(b)\) compact. Adjointing proves the other side. Applying the graded Leibniz identity to \(ab\) now gives a sum of two compact operators, as in (2.7). Products from the dense smooth algebra span a dense subspace of \(A\), and the bounded-transform commutator is norm-continuous in the source. This proves global compactness without imposing a unit or globally compact resolvent. The factorization of the source element is the required upgrade.

**Solution to 7.3.** In the even case take the original Hilbert-space grading, representation and operator \(F_D\). Theorem 2.2 proves the compact square defect, self-adjointness and compact source commutators. In the odd case the same calculations give an ungraded Fredholm module; tensor its operator with the right odd Clifford generator to obtain its odd KK-cycle. A Fredholm cycle requires only these compactness conditions. Summability instead controls membership of the resolvent in Schatten ideals, and smooth regularity controls repeated commutators with \(|D|\). Neither follows from the cycle axioms: a diagonal positive operator with eigenvalues \(\log(n+1)\), for example, has compact resolvent but its inverse powers need not have any finite Schatten exponent. With scalar representation it still defines an unbounded module.

**Solution to 7.4.** Use the [ordered right Clifford model, Lesson 09 Proposition 8.1](KT-KK-09.html#8-the-two-circle-classes), with generators \(-\sigma_2,\sigma_1\) and grading \(\Gamma=\sigma_3\). On
\(H=\ell^2(\mathbb Z^2)\otimes\mathbb C^2\), let
\[
D_{\mathbb T^2}e_{n,m}
=(n\sigma_1-m\sigma_2)e_{n,m},
\tag{8.1}
\]
with domain the vectors satisfying
\[
\sum_{n,m}(1+n^2+m^2)\|\xi_{n,m}\|^2<\infty.
\tag{8.2}
\]
The two coefficient matrices anticommute and square to one, so each matrix in (8.1) is self-adjoint and has square \((n^2+m^2)1\). The adjoint-domain Fourier test proves self-adjointness on (8.2). Its bounded inverse resolvents prove regularity, and its resolvent square is the diagonal \((1+n^2+m^2)^{-1}\), compact by finite lattice truncation. The grading anticommutes with \(D_{\mathbb T^2}\).

Multiplication by a smooth torus function preserves (8.2), by the two-variable Sobolev product rule. The commutator is multiplication by
\(-i\sigma_1\partial_xg+i\sigma_2\partial_yg\), a bounded matrix function. The tensor source acts evenly. Thus this is an even unbounded module.

For the product first use on the \(C(\mathbb T)\)-module
\(\ell^2(\mathbb Z)\widehat\otimes C(\mathbb T)\widehat\otimes C_1\)
the unbounded first operator \(n\varepsilon\). Its source commutators with coordinate Laurent monomials are bounded finite shifts, its localized resolvent is compact on the standard module, and smooth functions preserve its domain by the same Fourier derivative estimate. The right-dilated second circle operator is \(-m\sigma_2\), with the representation of its original Clifford generator by \(\sigma_1\), exactly as in the bounded product construction.

For the dense elementary creation vectors, the maps are \(J_nM_g\sigma_1^r\), with \(g\) smooth. Computing (5.1) leaves the bounded fixed term \(n\sigma_1\), the bounded derivative \([m,M_g]\), and the sign
\(\sigma_2\sigma_1^r=(-1)^r\sigma_1^r\sigma_2\). Creation of a fixed smooth vector preserves the indicated domains; the adjoint does too, by its Fourier and multiplication formula. The torus domain is contained in the first \(n\sigma_1\) domain, and its positivity form is
\[
\langle n\sigma_1\xi,D_{\mathbb T^2}\xi\rangle
+\langle D_{\mathbb T^2}\xi,n\sigma_1\xi\rangle
=2\sum_{n,m}n^2\|\xi_{n,m}\|^2\geq0.
\]
Theorem 5.4 therefore identifies the product. Its bounded transform is exactly
\((n\sigma_1-m\sigma_2)/\sqrt{1+n^2+m^2}\), the [earlier circle-by-circle bounded product, Lesson 09 Proposition 8.1](KT-KK-09.html#8-the-two-circle-classes). The zero mode has one vector of each parity and every other matrix is invertible. Its scalar index is zero.

## What this lesson proves and uses

The bounded-transform and unbounded-representative theorems are proved in Sections 2–3. The regular calculus, localization, elliptic domains and product-recognition estimates used in the examples and exercises have local proofs. The compact ideal, tensor and countability facts used here have the earlier Lesson 05 providers specified at the start; bounded product existence and its essential-source connection convention are the earlier Lesson 09 results specified there. Propositions 6.1 and 6.3 and the torus solution apply the locally proved criterion of Theorem 5.4.

## What this lesson does not prove

The general smooth operator-module framework and Theorem 6.4 are stated with their source hypotheses. This includes the Haagerup realization and smooth stabilization (*Unbounded bivariant K-theory and correspondences in noncommutative geometry*, Theorem 3.2.6 and Theorem 4.4.3), induced graph identifications (Theorem 5.4.1), preservation of the transverse graph scales (Theorems 6.2.5 and 6.2.7 and Lemma 6.2.6), and the general smooth compactness and KK-product results (Theorems 6.3.3–6.3.4). The survey states the correspondence product in Theorem 13.36 and its \(C^1\) KK specialization in Remark 13.37. These external smooth-scale results are not premises of the local proofs or exercises.

## References and source credit

- Jens Kaad, [*On the Unbounded Picture of KK-Theory*, actual arXiv version 1901.05161v3](https://arxiv.org/pdf/1901.05161v3), 22 August 2020, Section 3, printed pp. 4–5, is the free comparison for the bounded transform and inverse-compact construction. The posted version has [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); this source notice is retained. The source attributes its surjectivity theorem externally; its statement is not imported as a proof. The controlled inverse, its domain invariance, both inverse resolvents and bounded-transform comparison are proved in Section 3 above.
- Koen van den Dungen, [*Localisations of half-closed modules and the unbounded Kasparov product*, actual free arXiv version 2006.10616v2](https://arxiv.org/pdf/2006.10616v2), Sections 2.4 and 3.1, printed pp. 11–16, is the comparison source for the creation-operator estimates and integrated positivity. No separate open adaptation licence is asserted. Section 5 gives the full proof used here, including the nonessential-source multiplication connections and compact-support checks.
- Jens Kaad and Matthias Lesch, [*A Local Global Principle for Regular Operators in Hilbert C*-Modules*, actual author-hosted version 2](https://www.math.uni-bonn.de/people/lesch/dl/pap/2011-KaaLes-ArXiv-v2.pdf), Sections 2.3–2.4, Theorems 3.1 and 4.2, and Section 7, is the free comparison for resolvents, localization and controlled sums. The author file retains its source copyright; no separate open reuse licence is asserted. The precise regular calculus and symmetric localization criterion needed here are proved in Lemmas 0.0–0.1, rather than supplied by the preprint's references.
- Bruce Blackadar, [*K-Theory for Operator Algebras*, actual free corrected author edition](https://www.bruceblackadar.com/Mathematics/book6.pdf), Sections 12.4/14.6 and 18.3–18.5, supplies the free comparison for quasicentral choices and bounded product calculus. The [author's usage terms](https://www.bruceblackadar.com/mathpubs.html) retain copyright and allow use under Creative Commons rules with attribution; no particular licence version is named or inferred. The exact proofs used here are the [earlier local Lesson 08 quasicentral construction](KT-KK-08.html#1-approximate-identities-with-commutator-control), Lesson 09 product and multiplication-connection results, and the local arguments above.

- Gerd Grubb, *Distributions and Operators*, lecture notes, revised 2008, [author's lecture-note page](https://web.math.ku.dk/~grubb/distribution.htm), [Chapter 7](https://web.math.ku.dk/~grubb/dist7n.pdf), Theorems 7.5, 7.13 and 7.18 and Corollaries 7.19–7.20, and [Chapter 8](https://web.math.ku.dk/~grubb/dist8n.pdf), Theorems 8.1 and 8.5–8.7: the symbol and elliptic calculus. Lemmas 4.2a–4.2b prove the estimates, complete remainder bounds, symbol summation, bundle parametrix and exact domains used in Proposition 4.2.

- Bram Mesland, [*Spectral triples and KK-theory: a survey*, actual free arXiv version 1304.3802v1](https://arxiv.org/pdf/1304.3802v1), Sections 7–13, printed pp. 204–211, especially Definitions 11.32 and 12.34–12.35, Theorem 12.33, Theorem 13.36 and Remark 13.37. This is the source of the smooth correspondence statement and its graph-scale hypotheses.
- Bram Mesland, [*Unbounded bivariant K-theory and correspondences in noncommutative geometry*, actual free arXiv version 0904.4383v5](https://arxiv.org/pdf/0904.4383v5), Definitions 4.2.6, 4.3.1, 4.6.2 and 5.3.3, Theorem 4.4.3, Theorem 5.4.1, Theorems 6.2.5, 6.2.7 and 6.3.3–6.3.4, and Lemma 6.2.6. The survey's order convention is used in Theorem 6.4; the full paper supplies the operator-module construction. Both preprints are posted under [arXiv's non-exclusive distribution licence](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html); their source notices are retained. The statement and explanation here are independently written.

The CC0 notice at the start concerns this lesson's independently written exposition and proofs. It does not alter any source's copyright or licence. No source expression is copied or adapted as a substitute for a programme proof.
