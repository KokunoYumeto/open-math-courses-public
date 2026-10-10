# Analytic germs, local parametrization and the Nullstellensatz

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The zero set of finitely many holomorphic functions can be singular, but near any point it has a very concrete shape. After a generic linear change of coordinates, an irreducible germ of such a set is a branched covering of a polydisc: away from the zero set of one holomorphic function, the discriminant, it is a smooth manifold that covers the polydisc with a fixed finite number of sheets. This lesson proves this local parametrization theorem and its algebraic counterpart, the analytic Nullstellensatz: a germ vanishing on the zero set of an ideal has a power in the ideal. It also defines the dimension of a germ and identifies it with the Krull dimension of its local ring.

We use [Holomorphic functions of several variables](holomorphic-functions-of-several-variables.md), notably the Riemann extension theorem and the connectedness of complements of hypersurfaces, and [The local ring of holomorphic germs](the-local-ring-of-holomorphic-germs.md), notably Weierstrass division, unique factorization and the finiteness theorem. From commutative algebra: the radical of an ideal is the intersection of the primes containing it [Spectra of rings, Proposition 2.2](course:AG-CA/spectra-of-rings#2-equations-neighborhoods-and-specialization); factorial domains are normal [Integral extensions, Proposition 2.3](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down#2-integral-closure-survives-localization); an integral extension has the same Krull dimension as its base [Integral extensions, Theorem 5.1](course:AG-CA/integral-extensions-lying-over-going-up-and-going-down#5-chains-and-dimension); and the primitive element theorem for finite extensions of fields of characteristic zero, which have as many embeddings into an algebraic closure as their degree [Stacks, Tags 030N and 09HJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-primitive-element).

Basic references are [Demailly], [Lebl SCV] and [Cartan 1950].

## 1. Germs of analytic sets and their ideals

Two subsets of \(\mathbf C^n\) have the same **germ** at \(x\) if they agree on some neighbourhood of \(x\); the germ of \(A\) is written \((A,x)\). An **analytic germ** is the germ of an analytic subset of a neighbourhood of \(x\). We work at \(x=0\) and write \(\mathcal O_n\) for the ring of germs of holomorphic functions.

For an ideal \(J=(g_1,\ldots,g_k)\subset\mathcal O_n\), the germ \(V(J)\) of the common zero set of representatives \(g_1,\ldots,g_k\) does not depend on the generators: other generators are combinations of these and conversely, near \(0\). For an analytic germ \(A\), let \(I(A)\subset\mathcal O_n\) be the ideal of germs vanishing on \(A\). Directly from the definitions,

\[
J\subset I(V(J)),\qquad V(I(A))=A,
\tag{1.1}
\]

the second because \(A\) is the zero set of finitely many germs in \(I(A)\), so \(V(I(A))\subset A\), while every germ of \(I(A)\) vanishes on \(A\). An analytic germ is **irreducible** if it is not the union of two analytic germs different from it.

**Proposition 1.1.** An analytic germ \(A\) is irreducible if and only if \(I(A)\) is a prime ideal.

**Proof.** Let \(A\) be irreducible and \(fg\in I(A)\). Then \(A=(A\cap V(f))\cup(A\cap V(g))\), so one of these equals \(A\), say the first, and \(f\in I(A)\). Conversely, if \(A=A_1\cup A_2\) with \(A_i\neq A\), then by (1.1) there are \(f\in I(A_1)\setminus I(A)\) and \(g\in I(A_2)\setminus I(A)\), and \(fg\in I(A)\). \(\square\)

**Proposition 1.2.** Every decreasing sequence of analytic germs is eventually constant. Every analytic germ is a finite union \(A=A_1\cup\cdots\cup A_N\) of irreducible analytic germs with \(A_i\not\subset A_j\) for \(i\neq j\), and these **irreducible components** are unique up to order.

**Proof.** The ideals \(I(A_k)\) of a decreasing sequence increase, so they stabilize because \(\mathcal O_n\) is Noetherian, and \(A_k=V(I(A_k))\) stabilizes. If some analytic germ had no finite decomposition into irreducible germs, splitting it repeatedly would produce a strictly decreasing infinite sequence. Uniqueness: if \(A=\bigcup A_i=\bigcup B_l\) are two irredundant decompositions, each \(A_i=\bigcup_l(A_i\cap B_l)\) is irreducible, so \(A_i\subset B_l\) for some \(l\); symmetrically \(B_l\subset A_j\), and irredundancy forces \(i=j\) and \(A_i=B_l\). \(\square\)

## 2. Coordinates adapted to a prime ideal

**Lemma 2.1.** Every root \(w\in\mathbf C\) of \(w^d+a_1w^{d-1}+\cdots+a_d=0\) satisfies \(|w|\leq2\max_j|a_j|^{1/j}\).

**Proof.** If \(|w|>2|a_j|^{1/j}\) for all \(j\), dividing the equation by \(w^d\) gives \(1=|\sum_ja_jw^{-j}|<\sum_j2^{-j}<1\). \(\square\)

**Proposition 2.2.** Let \(J\subset\mathcal O_n\) be a proper ideal. There are an integer \(d\), \(0\leq d\leq n\), and linear coordinates \(z=(z',z'')\), \(z'=(z_1,\ldots,z_d)\), \(z''=(z_{d+1},\ldots,z_n)\), such that \(J\cap\mathcal O_d=0\) and, for every \(k=d+1,\ldots,n\), the ideal \(J\) contains a Weierstrass polynomial

\[
P_k=z_k^{s_k}+\sum_{j=1}^{s_k}a_{j,k}(z_1,\ldots,z_{k-1})\,z_k^{s_k-j},\qquad a_{j,k}\ \text{vanishing to order at least } j \text{ at } 0.
\tag{2.1}
\]

The coordinate basis can be chosen arbitrarily close to any given basis.

**Proof.** Induction on \(n\). If \(J=0\), take \(d=n\). Otherwise choose \(0\neq g\in J\), of order \(s\) at \(0\) with lowest homogeneous part \(g_s\), and a vector \(e_n\) close to the given last basis vector with \(g_s(e_n)\neq0\); this excludes only a closed set with empty interior. In coordinates \((\tilde z,z_n)\) for the basis \((e_1^0,\ldots,e_{n-1}^0,e_n)\), [The local ring of holomorphic germs, Proposition 2.2](the-local-ring-of-holomorphic-germs.md#2-weierstrass-polynomials) writes \(g\) as a unit times a Weierstrass polynomial \(P_n\in J\) of degree \(s\) with coefficient orders as in (2.1). The ideal \(J_{n-1}=J\cap\mathbf C\{\tilde z\}\) is proper. Apply the induction hypothesis to it, changing only the coordinates \(\tilde z\), by a basis of the span of \(e_1^0,\ldots,e_{n-1}^0\). A linear change of \(\tilde z\) keeps \(P_n\) a Weierstrass polynomial in \(z_n\) with coefficients in \(\mathcal O_{n-1}\), of the same orders. \(\square\)

We call such coordinates **adapted** to \(J\). The ring \(\mathcal O_n/J\) is then a finite \(\mathcal O_d\)-module and \(\mathcal O_d\to\mathcal O_n/J\) is injective, by [The local ring of holomorphic germs, Corollary 4.2](the-local-ring-of-holomorphic-germs.md#4-finiteness).

**Corollary 2.3 (cone condition).** In coordinates adapted to \(J\), there are \(C>0\) and \(\rho>0\) such that every \(z\in V(J)\) with \(|z|<\rho\) satisfies \(|z''|\leq C|z'|\); here \(|\cdot|\) is the maximum of the absolute values of the coordinates. Consequently, if \(\Delta'\subset\mathbf C^d\) and \(\Delta''\subset\mathbf C^{n-d}\) are polydiscs of radii \(r',r''\) with \(r''<\rho\) and \(Cr'<r''\), the projection \(\pi:V(J)\cap(\Delta'\times\Delta'')\to\Delta'\) is proper.

**Proof.** On \(V(J)\) all \(P_k\) vanish. By Lemma 2.1 and (2.1), \(|z_k|\leq2\max_j|a_{j,k}(z_1,\ldots,z_{k-1})|^{1/j}\leq C_k\max_{i<k}|z_i|\) near \(0\), since \(|a_{j,k}|\leq c\,|(z_1,\ldots,z_{k-1})|^j\). Induction on \(k\) gives \(|z''|\leq C|z'|\). Then \(V(J)\cap(\Delta'\times\Delta'')\) lies in \(\Delta'\times\{|z''|\leq Cr'\}\), with \(\{|z''|\leq Cr'\}\) compact in \(\Delta''\); the preimage of a compact \(K'\subset\Delta'\) is a closed subset of the compact set \(K'\times\{|z''|\leq Cr'\}\). \(\square\)

## 3. The finite extension and a primitive element

From now on \(J\) is a prime ideal, \(A=V(J)\), and the coordinates are adapted to \(J\). The ring \(\mathcal O_n/J\) is a domain containing \(\mathcal O_d\), finite over it. Write \(\tilde f\) for the class of \(f\). Let \(K\) and \(L\) be the fields of fractions of \(\mathcal O_d\) and \(\mathcal O_n/J\). Then \(L=K(\tilde z_{d+1},\ldots,\tilde z_n)\) is a finite extension; let \(q=[L:K]\), and let \(\sigma_1,\ldots,\sigma_q\) be the distinct \(K\)-embeddings of \(L\) into an algebraic closure \(\overline K\).

**Lemma 3.1.** For \(c=(c_{d+1},\ldots,c_n)\in\mathbf C^{n-d}\) outside a finite union of proper linear subspaces, the linear form \(u(z'')=\sum_kc_kz_k\) is a **primitive element**: \(L=K(\tilde u)\).

**Proof.** \(\tilde u\) generates \(L\) exactly when its \(q\) conjugates \(\sigma_i(\tilde u)\) are distinct. For \(i\neq j\), some \(\sigma_i(\tilde z_k)\neq\sigma_j(\tilde z_k)\), since the \(\tilde z_k\) generate \(L\). So \(\{c:\ \sigma_i(\tilde u)=\sigma_j(\tilde u)\}=\{c:\ \sum_kc_k(\sigma_i\tilde z_k-\sigma_j\tilde z_k)=0\}\) is a linear subspace of \(\mathbf C^{n-d}\), proper because it misses the corresponding basis vector. \(\square\)

**Lemma 3.2.** Let \(g\in L\) be integral over \(\mathcal O_d\). Its minimal polynomial over \(K\) has coefficients in \(\mathcal O_d\). If \(g=\tilde f\) with \(f\in\mathfrak m_n\), this minimal polynomial is a Weierstrass polynomial.

**Proof.** The conjugates \(\sigma_i(g)\) satisfy the same monic equations over \(\mathcal O_d\) as \(g\), so they are integral over \(\mathcal O_d\); the coefficients of the minimal polynomial are, up to sign, elementary symmetric functions of some of these conjugates, hence integral over \(\mathcal O_d\) and in \(K\). Since \(\mathcal O_d\) is factorial, it is normal, and the coefficients lie in \(\mathcal O_d\). For the second claim let \(W\in\mathcal O_d[T]\) be the minimal polynomial, of degree \(r\). The germ \(W(z',f(z))\) lies in \(J\), and every element of the proper ideal \(J\) vanishes at \(0\); since \(f(0)=0\), this gives \(W(0,0)=0\). So the monic polynomial \(W(0,T)\) of degree \(r\) has the form \(T^mv(T)\) with \(v(0)\neq0\) and \(1\leq m\leq r\). By Weierstrass preparation in the variables \((z',T)\), \(W=UW'\) with \(W'\) a Weierstrass polynomial of degree \(m\) in \(T\) and \(U\) a unit; by [The local ring of holomorphic germs, Lemma 2.3](the-local-ring-of-holomorphic-germs.md#2-weierstrass-polynomials), \(W=W'Q\) with \(Q\in\mathcal O_d[T]\) monic and \(Q(0,0)\neq0\). In the domain \(\mathcal O_n/J\), \(W'(\tilde f)Q(\tilde f)=0\), and \(Q(\tilde f)\) is the class of the germ \(Q(z',f(z))\), a unit because its value at \(0\) is \(Q(0,0)\neq0\). So \(W'(\tilde f)=0\), and minimality gives \(m=r\), \(W=W'\). \(\square\)

Fix a primitive linear form \(u\) as in Lemma 3.1. Let \(W_u\in\mathcal O_d[T]\) be the minimal polynomial of \(\tilde u\), a Weierstrass polynomial of degree \(q\), and \(W_k\) that of \(\tilde z_k\), a Weierstrass polynomial of degree at most \(q\). Let \(\delta\in\mathcal O_d\) be the discriminant of \(W_u\): the product \(\prod_{i<j}(\sigma_i\tilde u-\sigma_j\tilde u)^2\), a symmetric expression in the roots, hence a polynomial in the coefficients of \(W_u\). It is nonzero because the conjugates are distinct. For \(z'\) near \(0\), the number \(\delta(z')\) is the discriminant of the numerical polynomial \(W_u(z',T)\), which is nonzero exactly when \(W_u(z',\cdot)\) has \(q\) distinct roots.

**Lemma 3.3.** If \(g\in L\) is integral over \(\mathcal O_d\), then \(\delta g\in\mathcal O_d[\tilde u]\). In particular there are \(B_k\in\mathcal O_d[T]\) of degree at most \(q-1\) with

\[
\delta(z')\,z_k\equiv B_k(z',u(z''))\pmod J\qquad(k=d+1,\ldots,n).
\tag{3.1}
\]

**Proof.** Write \(g=\sum_{j<q}b_j\tilde u^j\) with \(b_j\in K\). Applying the \(\sigma_i\) gives a linear system \(\sigma_i(g)=\sum_jb_j\sigma_i(\tilde u)^j\) with Vandermonde matrix \(V\), \((\det V)^2=\pm\delta\). By Cramer's rule, \(\delta b_j=\pm\det V\cdot\det V_j\), where \(V_j\) is \(V\) with one column replaced by \((\sigma_i(g))_i\); this is a polynomial in the integral elements \(\sigma_i(g),\sigma_i(\tilde u)\), hence integral over \(\mathcal O_d\), and it lies in \(K\). By normality \(\delta b_j\in\mathcal O_d\). \(\square\)

**Lemma 3.4.** Let \(G\subset\mathcal O_n\) be the ideal generated by \(W_u(z',u(z''))\) and \(\delta(z')z_k-B_k(z',u(z''))\), \(k=d+1,\ldots,n\), and let \(m=\max\{q,(n-d)(q-1)\}\). Then \(G\subset J\) and \(\delta^mJ\subset G\). More precisely, every \(f\in\mathcal O_n\) satisfies \(\delta^mf\equiv R(z',u(z''))\) modulo \(G\) for some \(R\in\mathcal O_d[T]\) of degree less than \(q\), and \(R=0\) when \(f\in J\).

**Proof.** \(G\subset J\) by the definitions of \(W_u\) and \(B_k\). Since \(\deg W_k\leq q\), each monomial \(\delta^qz_k^j\), \(j\leq q\), is congruent to \(\delta^{q-j}B_k(z',u)^j\) modulo \(\delta z_k-B_k(z',u)\) (factor \((\delta z_k)^j-B_k^j\)). Hence \(\delta^qW_k(z',z_k)\equiv\delta^qW_k\bigl(z',B_k(z',u)/\delta\bigr)\) modulo \(G\), where the right side is a polynomial in \(u\) over \(\mathcal O_d\) that vanishes at \(\tilde u\) in \(L\) (because \(B_k(z',\tilde u)/\delta=\tilde z_k\)), hence is a multiple of the minimal polynomial \(W_u\). So \(\delta^qW_k(z',z_k)\in G\).

Now let \(f\in\mathcal O_n\). Dividing successively by the Weierstrass polynomials \(W_n,W_{n-1},\ldots,W_{d+1}\) in the variables \(z_n,z_{n-1},\ldots,z_{d+1}\), as in the proof of the finiteness theorem, gives \(f=R_0+\sum_kW_kq_k\) with \(R_0\in\mathcal O_d[z'']\) of degree less than \(q\) in each \(z_k\), hence of total degree at most \((n-d)(q-1)\leq m\). As \(m\geq q\), \(\delta^mf\equiv\delta^mR_0\) modulo \(G\). Substituting \(\delta z_k\equiv B_k(z',u)\) in each monomial of degree at most \(m\) gives \(\delta^mR_0\equiv H(z',u)\) modulo \(G\) with \(H\in\mathcal O_d[T]\), and dividing \(H\) by the monic \(W_u\) gives the remainder \(R\). If \(f\in J\), then \(R(z',\tilde u)=0\) in \(L\) with \(\deg R<q=\deg W_u\), so \(R=0\). \(\square\)

## 4. The local parametrization theorem

**Theorem 4.1 (local parametrization).** Let \(J\subset\mathcal O_n\) be prime, \(A=V(J)\), with coordinates adapted to \(J\), primitive linear form \(u\), degree \(q=[L:K]\) and discriminant \(\delta\). For polydiscs \(\Delta'\subset\mathbf C^d\), \(\Delta''\subset\mathbf C^{n-d}\) of sufficiently small radii \(r',r''\) with \(r'\) small compared with \(r''\), put \(\Delta=\Delta'\times\Delta''\) and \(S=\{z'\in\Delta':\ \delta(z')=0\}\). Then:

1. \(A_S=A\cap((\Delta'\setminus S)\times\Delta'')\) is a complex submanifold of dimension \(d\), and \(\pi:A_S\to\Delta'\setminus S\) is a covering map with exactly \(q\) sheets;
2. \(A_S\) is connected and dense in \(A\cap\Delta\);
3. the fibres of \(\pi:A\cap\Delta\to\Delta'\) over points of \(S\) have at most \(q\) points;
4. \(A\cap\Delta\) lies in the cone \(|z''|\leq C|z'|\), and \(\pi:A\cap\Delta\to\Delta'\) is proper.

**Proof of 1 and 4.** After a linear change of the coordinates \(z''\) we may assume \(u=z_{d+1}\); then \(W_u=W_{d+1}\) and \(B_{d+1}=\delta T\). Choose the radii so small that: the germs \(W_u,\delta,B_k\) and generators of \(J\) and \(G\) have representatives on \(\Delta\), with \(A\cap\Delta\) the zero set of the generators of \(J\); the relations \(G\subset J\) and \(\delta^mJ\subset G\) of Lemma 3.4, and the polynomial identities from its proof, hold for these representatives on \(\Delta\); Corollary 2.3 applies; and for every \(z'\in\Delta'\) all roots of all the polynomials \(W_k(z',\cdot)\) have absolute value less than \(r''\) (possible by Lemma 2.1, the coefficients being small near \(0\)). Then

\[
A\cap\Delta\ \subset\ V(G)\cap\Delta\ \subset\ (A\cap\Delta)\cup(S\times\Delta''),
\tag{4.1}
\]

the second inclusion because \(V(G)\subset V(\delta^mJ)=V(\delta)\cup V(J)\). So \(A_S\) consists of the points \(z\in\Delta\) with

\[
\delta(z')\neq0,\qquad W_u(z',z_{d+1})=0,\qquad z_k=B_k(z',z_{d+1})/\delta(z')\quad(k\geq d+2).
\tag{4.2}
\]

Where \(\delta(z')\neq0\) the roots of \(W_u(z',\cdot)\) are simple, so \(\partial W_u/\partial T\neq0\) at the points of \(A_S\), and by the implicit function theorem \(z_{d+1}\), and with it every \(z_k\), is locally a holomorphic function of \(z'\) on \(A_S\). Hence \(A_S\) is a \(d\)-dimensional submanifold and \(\pi|_{A_S}\) is a local homeomorphism, with fibres of at most \(q\) points.

The map \(\pi:A_S\to\Delta'\setminus S\) is proper, being the restriction of the proper map of Corollary 2.3 over an open set. A proper local homeomorphism \(p:X\to Y\) with finite fibres between Hausdorff, locally compact spaces is a covering: given \(y\) with fibre \(\{x_1,\ldots,x_s\}\), choose disjoint open \(U_i\ni x_i\) mapped homeomorphically onto open \(V_i\ni y\); there is an open \(V\ni y\) inside \(\bigcap V_i\) with \(p^{-1}(V)\subset\bigcup U_i\), since otherwise points \(x\notin\bigcup U_i\) with \(p(x)\to y\) would accumulate, by properness, at a point of the fibre; then \(p^{-1}(V)\) is the disjoint union of the sets \(U_i\cap p^{-1}(V)\), each mapped homeomorphically onto \(V\). The base \(\Delta'\setminus S\) is connected [Holomorphic functions of several variables, Corollary 4.3](holomorphic-functions-of-several-variables.md#4-the-riemann-extension-theorem), so the number of sheets is constant.

It equals \(q\). Let \(z'\in\Delta'\setminus S\) and let \(w\) be one of the \(q\) distinct roots of \(W_u(z',\cdot)\). Put \(z_{d+1}=w\) and \(z_k=B_k(z',w)/\delta(z')\) for \(k\geq d+2\). The proof of Lemma 3.4 gives polynomial identities \(\delta^qW_k\bigl(z',B_k(z',T)/\delta\bigr)=W_u(z',T)\,Q_k(z',T)\) in \(\mathcal O_d[T]\), and we include them among the relations required to hold on \(\Delta'\). Setting \(T=w\) gives \(\delta(z')^qW_k(z',z_k)=0\), hence \(W_k(z',z_k)=0\) and \(|z_k|<r''\) by the choice of radii. So the point lies in \(\Delta\), satisfies the generators of \(G\), and therefore lies in \(V(G)\cap((\Delta'\setminus S)\times\Delta'')=A_S\) by (4.1). Distinct roots give distinct points, so each fibre has exactly \(q\) points. Part 4 is Corollary 2.3. \(\square\)

**Lemma 4.2.** For a prime ideal \(J\), \(I(V(J))=J\).

**Proof.** Let \(f\in I(V(J))\). By Lemma 3.2, \(\tilde f\) has a minimal polynomial \(T^r+b_1T^{r-1}+\cdots+b_r\) with \(b_i\in\mathcal O_d\), so \(f^r+b_1f^{r-1}+\cdots+b_r\in J\). Evaluating at the points of \(A_S\), where \(f\) and all elements of \(J\) vanish (after shrinking \(\Delta\)), gives \(b_r(z')=0\) for all \(z'\in\Delta'\setminus S\), because every such \(z'\) has points of \(A_S\) above it by Theorem 4.1(1). So \(b_r=0\) on the dense set \(\Delta'\setminus S\), hence \(b_r=0\). An irreducible polynomial with zero constant term is \(T\) itself, so \(r=1\) and \(\tilde f=0\), that is \(f\in J\). The reverse inclusion is (1.1). \(\square\)

**Proof of 2 and 3.** Let \(A_{S,1},\ldots,A_{S,N}\) be the connected components of \(A_S\). Each is a covering of the connected base \(\Delta'\setminus S\) with \(q_j\geq1\) sheets, and \(\sum q_j=q\). For a linear form \(\lambda\) on \(\mathbf C^{n-d}\) and \(z'\in\Delta'\setminus S\), put

\[
P_{\lambda,j}(z',T)=\prod_{(z',z'')\in A_{S,j}}\bigl(T-\lambda(z'')\bigr).
\tag{4.3}
\]

Locally over \(\Delta'\setminus S\), \(A_{S,j}\) is the union of \(q_j\) graphs of holomorphic maps, so the coefficients of \(P_{\lambda,j}\) are holomorphic on \(\Delta'\setminus S\); they are bounded by the cone condition. By the Riemann extension theorem [Holomorphic functions of several variables, Theorem 4.2](holomorphic-functions-of-several-variables.md#4-the-riemann-extension-theorem) they extend holomorphically to \(\Delta'\), so \(P_{\lambda,j}\in\mathcal O(\Delta')[T]\) is monic of degree \(q_j\), and \(P_{\lambda,j}(z',\lambda(z''))\) vanishes on \(A_{S,j}\).

The function \(F(z)=\delta(z')\prod_jP_{\lambda,j}(z',\lambda(z''))\) vanishes on \(A_S\cup(S\times\Delta'')\supset A\cap\Delta\), so \(F\in I(A)=J\) by Lemma 4.2. As \(\delta\neq0\) lies in \(\mathcal O_d\) and \(J\cap\mathcal O_d=0\), \(\delta\notin J\); since \(J\) is prime, \(P_{\lambda,j}(z',\lambda(z''))\in J\) for some \(j=j(\lambda)\).

*Connectedness.* Choose a sequence \(z'_\nu\to0\) in \(\Delta'\setminus S\), possible because \(S\) has empty interior, and a linear form \(\lambda\) that separates the \(q\) points of every fibre \(\pi^{-1}(z'_\nu)\). This excludes countably many proper linear subspaces of the space of linear forms, so such \(\lambda\) exist (a countable union of proper subspaces has empty interior, by the Baire category theorem). If \(N\geq2\), pick \(i\neq j(\lambda)\). The germ \(P_{\lambda,j(\lambda)}(z',\lambda(z''))\in J\) vanishes on \(A\) near \(0\), in particular at the points of \(A_{S,i}\) above \(z'_\nu\) for large \(\nu\), which tend to \(0\) by the cone condition. At such a point \((z'_\nu,z'')\), \(\lambda(z'')\) would be a root of \(P_{\lambda,j(\lambda)}(z'_\nu,\cdot)\), that is equal to \(\lambda(w'')\) for a point \((z'_\nu,w'')\in A_{S,j(\lambda)}\), contradicting the choice of \(\lambda\). So \(N=1\), \(A_S\) is connected, and \(P_\lambda:=P_{\lambda,1}\) has degree \(q\) and \(P_\lambda(z',\lambda(z''))\in J\) for every \(\lambda\).

*Fibres over \(S\).* \(P_\lambda(z',\lambda(z''))\) vanishes on the closure \(\overline{A_S}\) in \(\Delta\). If a fibre of \(\overline{A_S}\) over \(z'\in S\) had \(q+1\) points, a linear form \(\lambda\) separating them would give \(q+1\) distinct roots of the polynomial \(P_\lambda(z',\cdot)\) of degree \(q\). So these fibres have at most \(q\) points.

*Density.* Suppose that for polydiscs \(\Delta\) of arbitrarily small radii \(A_S\) is not dense in \(A\cap\Delta\). Then there are points \(z_\nu=(z'_\nu,z''_\nu)\in A\), \(z_\nu\to0\), with \(z'_\nu\in S\) and \(z''_\nu\notin F_\nu\), where \(F_\nu\) is the finite set of \(z''\) with \((z'_\nu,z'')\in\overline{A_S}\). The roots of \(P_\lambda(z'_\nu,\cdot)\) are exactly the values \(\lambda(F_\nu)\): they are limits of roots of \(P_\lambda(z',\cdot)\) as \(z'\to z'_\nu\) through \(\Delta'\setminus S\), since roots of monic polynomials depend continuously on the coefficients, and those roots are values of \(\lambda\) at points of \(A_S\). Choose \(\lambda\) with \(\lambda(z''_\nu)\notin\lambda(F_\nu)\) for all \(\nu\), again outside countably many proper subspaces. Then \(P_\lambda(z'_\nu,\lambda(z''_\nu))\neq0\) for all \(\nu\), although \(P_\lambda(z',\lambda(z''))\in J\) vanishes on \(A\) near \(0\). This contradiction shows that \(A_S\) is dense in \(A\cap\Delta\) once \(\Delta\) is small enough; fibres of \(A\cap\Delta\) over \(S\) are then fibres of \(\overline{A_S}\), proving 3. \(\square\)

## 5. The Nullstellensatz and dimension

**Theorem 5.1 (analytic Nullstellensatz).** For every ideal \(J\subset\mathcal O_n\), \(I(V(J))=\sqrt J\).

**Proof.** If \(f^k\in J\), then \(f\) vanishes on \(V(J)\); so \(\sqrt J\subset I(V(J))\). Conversely, for every prime \(\mathfrak p\supset J\) we have \(V(\mathfrak p)\subset V(J)\), hence \(I(V(J))\subset I(V(\mathfrak p))=\mathfrak p\) by Lemma 4.2. Therefore \(I(V(J))\) lies in the intersection of all primes containing \(J\), which is \(\sqrt J\). \(\square\)

**Corollary 5.2.** The maps \(J\mapsto V(J)\) and \(A\mapsto I(A)\) are inverse inclusion-reversing bijections between radical ideals of \(\mathcal O_n\) and analytic germs at \(0\); prime ideals correspond to irreducible germs.

A point \(x\) of an analytic set \(A\) is **regular** if \(A\) is a complex submanifold near \(x\), and **singular** otherwise. The regular points form an open subset \(A_{\mathrm{reg}}\) of \(A\).

**Definition 5.3.** The **dimension** \(\dim(A,0)\) of an irreducible analytic germ is the integer \(d\) of coordinates adapted to \(I(A)\). The dimension of an analytic germ is the maximum of the dimensions of its irreducible components.

**Theorem 5.4.** Let \(A\) be an irreducible analytic germ. Then \(\dim(A,0)\) equals the Krull dimension of the local ring \(\mathcal O_n/I(A)\), and it equals the dimension of the manifold \(A_{\mathrm{reg}}\) at every regular point of a sufficiently small representative. In particular it does not depend on the choice of adapted coordinates. Regular points are dense in small representatives of \(A\).

**Proof.** \(\mathcal O_d\subset\mathcal O_n/I(A)\) is a finite, hence integral, extension, so both rings have the same Krull dimension, and \(\dim\mathcal O_d=d\) by [The local ring of holomorphic germs, Proposition 1.1](the-local-ring-of-holomorphic-germs.md#1-the-ring-of-germs). In a representative \(A\cap\Delta\) as in Theorem 4.1, \(A_S\subset A_{\mathrm{reg}}\) is a dense \(d\)-dimensional manifold, open in \(A\cap\Delta\). Every connected component of \(A_{\mathrm{reg}}\cap\Delta\) is open in \(A\cap\Delta\), so it meets \(A_S\) and has dimension \(d\). \(\square\)

**Proposition 5.5.** Let \(B\subset A\) be analytic germs with \(A\) irreducible and \(B\neq A\). Then \(\dim B<\dim A\), and every small representative of \(B\) has empty interior in the corresponding representative of \(A\).

**Proof.** It suffices to treat an irreducible \(B\). Then \(\mathfrak p=I(B)/I(A)\) is a nonzero prime of the Noetherian local domain \(R=\mathcal O_n/I(A)\), and \(\mathcal O_n/I(B)=R/\mathfrak p\). Concatenating a chain of primes of \(R/\mathfrak p\) with the chain \(0\subsetneq\mathfrak p\) gives \(\dim R/\mathfrak p+1\leq\dim R\), so \(\dim B<\dim A\) by Theorem 5.4. For the second statement, suppose \(B\cap\Delta\) contains a nonempty open subset of \(A\cap\Delta\), with \(\Delta\) as in Theorem 4.1. Since \(A_S\) is dense and open in \(A\cap\Delta\), \(B\cap A_S\) is an analytic subset of the connected manifold \(A_S\) with interior points. In a connected manifold, the interior of an analytic subset is closed as well as open: near a limit of interior points, the local equations vanish on an open set accumulating at that point and hence, by the identity theorem, on a whole connected neighbourhood. So \(B\supset A_S\), and \(B\cap\Delta\supset\overline{A_S}=A\cap\Delta\), contradicting \(B\neq A\). \(\square\)

## 6. Exercises

**Exercise 6.1.** Let \(A=\{z\in\mathbf C^2:\ z_2^2=z_1^3\}\). Find adapted coordinates, the degree \(q\), a primitive element, the discriminant locus, and verify Theorem 4.1. Show that the germ \((A,0)\) is irreducible.

*Solution.* \(P_2=z_2^2-z_1^3\) is a Weierstrass polynomial in \(z_2\) with \(a_{2,2}=-z_1^3\) of order \(3\geq2\); \(J=(P_2)\) is prime because \(P_2\) has no root in \(\mathcal O_1\) (a root \(g\) would satisfy \(g^2=z_1^3\), impossible for orders: \(2\operatorname{ord}g=3\)), so it is irreducible in \(\mathcal O_1[z_2]\), hence in \(\mathcal O_2\), and \(\mathcal O_2\) is factorial. Here \(d=1\), \(q=2\), \(u=z_2\), \(W_u=T^2-z_1^3\), \(\delta=4z_1^3\), \(S=\{0\}\). Over \(z_1\neq0\) the fibre is \(\{\pm z_1^{3/2}\}\), two points, and going once around \(z_1=0\) exchanges them, so \(A_S\) is a connected double covering of the punctured disc. The fibre over \(0\) is one point. Irreducibility is Proposition 1.1, as \(J\) is prime and \(I(A)=J\) by Lemma 4.2.

**Exercise 6.2.** Let \(A=\{z_1z_2=0\}\subset\mathbf C^2\). Find its irreducible components and dimensions, and show that \(0\) is a singular point.

*Solution.* \(A=\{z_1=0\}\cup\{z_2=0\}\), two lines, each irreducible of dimension \(1\) since its ideal \((z_i)\) is prime. A germ of complex submanifold is irreducible: in coordinates in which it is \(\{z_{k+1}=\cdots=z_n=0\}\), its ideal is \((z_{k+1},\ldots,z_n)\), with quotient \(\mathcal O_k\), a domain. By Theorem 5.1, \(I(A)=\sqrt{(z_1z_2)}=(z_1z_2)\), which is not prime. So \((A,0)\) is not irreducible, and \(0\) is a singular point.

**Exercise 6.3.** Use Theorem 5.1 to show: if \(f\in\mathcal O_n\) vanishes wherever \(g_1,\ldots,g_k\in\mathcal O_n\) all vanish (near \(0\)), then \(f^N=\sum h_ig_i\) for some \(N\) and some \(h_i\in\mathcal O_n\).

*Solution.* By hypothesis \(f\in I(V(J))\) for \(J=(g_1,\ldots,g_k)\), which equals \(\sqrt J\); so \(f^N\in J\).

**Exercise 6.4.** Show that the real analogue of Lemma 4.2 fails: for the prime ideal \(J=(x^2+y^2)\) of the ring of real convergent power series in \(x,y\), the vanishing ideal of its real zero set is strictly larger than \(J\).

*Solution.* The real zero set of \(x^2+y^2\) is the origin, whose vanishing ideal is \((x,y)\), and \(x\notin(x^2+y^2)\) by comparing orders. (\(J\) is prime because \(x^2+y^2\) is irreducible over the real power series ring: a factorization would give a factorization of its quadratic part into real linear forms.) The proofs above use complex roots at every step.

## References

- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Lebl SCV] J. Lebl, *Tasty Bits of Several Complex Variables*, version 4.4 (2026). <https://www.jirka.org/scv/>
- [Cartan 1950] H. Cartan, Idéaux et modules de fonctions analytiques de variables complexes, *Bulletin de la Société Mathématique de France* 78 (1950), 29–64. <https://www.numdam.org/item/BSMF_1950__78__29_0/>
- [Stacks] The Stacks project, cited by tag; each tag links to the same result in the AI Integrated Stacks Project. <https://stacks.math.columbia.edu/>
