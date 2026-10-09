# Tensor products of Banach and Hilbert spaces, Jordan homomorphisms and isometries of \(C^*\)-algebras

*Written by Claude Opus 5.5 (Anthropic), September 2026, extended October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October additions (the approximation property in Section 4 and Theorem 11.8) are self-checked by the writing AI. Public domain (CC0).*

*The proof of Theorem 4.12 was written by GPT-6 Astra (OpenAI), Ultra, October 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

The algebraic tensor product of a pair of Banach spaces carries many natural norms, and different norms give different completions with different dual spaces. This lesson studies the two extreme norms and the norms between them. The *injective norm* \(\lambda\) tests a tensor against products of functionals. It turns tensors into operators of finite rank, measured in the operator norm. The *projective norm* \(\gamma\) is the largest norm for which the map \((x,y)\mapsto x\otimes y\) is contractive. It turns bounded bilinear maps into bounded linear maps, and its dual space is the space of bounded operators from one factor into the dual of the other. Between the two lie the *reasonable* cross norms, whose dual norms are again cross norms. For Hilbert spaces the injective norm, the Hilbert space norm and the projective norm give the compact, the Hilbert–Schmidt and the trace-class operators. Trace duality then identifies the dual of the compact operators with the trace class, and the dual of the trace class with the bounded operators.

The second half of the lesson is about maps between \(C^*\)-algebras that keep only part of the structure. A *Jordan homomorphism* preserves adjoints and squares of self-adjoint elements, but not products. The transpose of matrices is the basic example. It is an isometric Jordan automorphism of \(M_n(\mathbb C)\) that is not multiplicative. Its tensor product with the identity map of \(M_n(\mathbb C)\) has norm at least \(n\), so the operator norm on \(M_n(\mathbb C)\odot M_n(\mathbb C)\) is a reasonable cross norm that behaves badly under tensor products of maps, unlike \(\lambda\) and \(\gamma\). We prove that every Jordan homomorphism of a \(C^*\)-algebra into a von Neumann algebra splits, by a central projection, into a homomorphism and an antihomomorphism. We also prove Kadison's theorem: a linear isometry of a unital \(C^*\)-algebra onto a \(C^*\)-algebra is a unitary times a Jordan isomorphism; in particular, one that maps \(1\) to \(1\) is a Jordan isomorphism. Positive linear isometries of one \(C^*\)-algebra onto another, with or without units, are described in the same way.

We assume basic functional analysis (the Hahn–Banach theorem, dual spaces) and basic Hilbert space theory. We use the Hilbert tensor product and tensor products of operators from the lesson Spatial tensor products of von Neumann algebras, and the continuous functional calculus and the order of a \(C^*\)-algebra from C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients. Sections 10 and 11 also use the bidual of a \(C^*\)-algebra from [The universal enveloping von Neumann algebra of a \(C^*\)-algebra, and \(W^*\)-algebras](../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html) and the type decomposition from Projections and types of von Neumann algebras. Nothing depends on separability, and zero spaces are allowed throughout. Every fact used from other lessons is stated in full near the end, with the place where it is proved.

Cross norms, and the norms \(\lambda\) and \(\gamma\) in particular, were studied systematically by Schatten, and the injective and projective tensor products are the starting point of Grothendieck's thesis, whose main results are summarized in [Grothendieck 1952]. Jordan homomorphisms of matrix rings were split into homomorphisms and antihomomorphisms in [Jacobson–Rickart 1950]. The isometry theorem, and the splitting of Jordan isomorphisms of von Neumann algebras, are due to Kadison. The splitting for \(C^*\)-algebras is from [Størmer 1965].

## Conventions

- Banach spaces are complex. \(E^*\) is the dual of \(E\), with \(\|f\|=\sup\{|f(x)|:\|x\|\le1\}\), and \(j_E:E\to E^{**}\) is the canonical isometry, \(j_E(x)(f)=f(x)\). An *operator* is a bounded linear map. \(B(E,F)\) is the Banach space of operators \(E\to F\) with the operator norm, \(B(E)=B(E,E)\), and a *contraction* is an operator of norm at most one.
- \(E\odot F\) is the algebraic tensor product, spanned by the elementary tensors \(x\otimes y\). Every bilinear map \(b\) on \(E\times F\) defines a unique linear map on \(E\odot F\) with \(x\otimes y\mapsto b(x,y)\). We use this universal property without comment to define linear maps on \(E\odot F\).
- Hilbert spaces are complex, and inner products are linear in the first variable. \(H\otimes K\) is the Hilbert tensor product: the completion of \(H\odot K\) for the inner product \(\langle\xi\otimes\eta,\xi'\otimes\eta'\rangle=\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle\).
- \(C^*\)-algebras need not have a unit. \(A_h\) is the set of self-adjoint elements of \(A\), and \(C^*(S)\) is the \(C^*\)-subalgebra generated by a subset \(S\). For operators on a Hilbert space, \(S'\) is the commutant and \(S''\) the bicommutant. We write \([x,y]=xy-yx\) and \(x\circ y=xy+yx\).

## 1. Tensors as operators of finite rank

**Lemma 1.1.** Let \(E\) and \(F\) be normed spaces, and \(u\in E\odot F\).

1. \(u=\sum_{i=1}^nx_i\otimes y_i\) for some \(x_i\in E\) and linearly independent \(y_1,\ldots,y_n\in F\), with \(n=0\) when \(u=0\).
2. If \(y_1,\ldots,y_n\) are linearly independent and \(\sum_ix_i\otimes y_i=0\), then every \(x_i\) is \(0\).
3. For \(f\in E^*\) and \(g\in F^*\), the number \(\langle u,f\otimes g\rangle=\sum_if(x_i)g(y_i)\) does not depend on the representation \(u=\sum_ix_i\otimes y_i\). Moreover \(u=0\) if and only if \(\langle u,f\otimes g\rangle=0\) for all \(f\in E^*\) and \(g\in F^*\).

**Proof.** (1) Start with any representation of \(u\). Choose a basis of the span of its second factors, expand each second factor in this basis, and collect terms by bilinearity.

(2) Since the \(y_i\) are linearly independent, there are linear functionals \(g_1,\ldots,g_n\) on their span with \(g_j(y_i)=\delta_{ij}\). They are bounded, because the span is finite-dimensional, and the Hahn–Banach theorem extends them to elements of \(F^*\). The linear map \(E\odot F\to E\) given by \(x\otimes y\mapsto g_j(y)x\) sends \(\sum_ix_i\otimes y_i\) to \(x_j\). So \(x_j=0\).

(3) The number is the value at \(u\) of the linear functional defined by the bilinear form \((x,y)\mapsto f(x)g(y)\), so it depends only on \(u\). If it vanishes for all \(f\) and \(g\), write \(u\) as in (1) and take \(g=g_j\) from (2). Then \(f(x_j)=0\) for every \(f\in E^*\), so \(x_j=0\) by the Hahn–Banach theorem, and \(u=0\). \(\square\)

Extending (3) linearly in the second variable, \(\langle u,v\rangle=\sum_{i,k}f_k(x_i)g_k(y_i)\) for \(v=\sum_kf_k\otimes g_k\in E^*\odot F^*\) is a well-defined bilinear pairing of \(E\odot F\) with \(E^*\odot F^*\). By (3), \(E^*\odot F^*\) separates the points of \(E\odot F\). The pairing also separates the points of \(E^*\odot F^*\): if \(\langle x\otimes y,v\rangle=0\) for all \(x,y\), write \(v=\sum_kf_k\otimes g_k\) with linearly independent \(g_k\). For each \(x\) the functional \(\sum_kf_k(x)g_k\) is then zero, so every \(f_k(x)=0\), and \(v=0\).

**Proposition 1.2** (tensors as operators). Let \(E\) and \(F\) be normed spaces. For \(u=\sum_ix_i\otimes y_i\in E\odot F\) define
\[
T_u:E^*\to F,\qquad T_u(f)=\sum_if(x_i)\,y_i .
\tag{1.1}
\]

1. \(T_u\) is a well-defined operator of finite rank, \(\|T_u\|\le\sum_i\|x_i\|\|y_i\|\), and \(g(T_uf)=\langle u,f\otimes g\rangle\) for \(f\in E^*\), \(g\in F^*\). The map \(u\mapsto T_u\) is linear and injective.
2. Put \(u^{\mathrm t}=\sum_iy_i\otimes x_i\in F\odot E\). The adjoint \(T_u^*:F^*\to E^{**}\) takes its values in \(j_E(E)\), and \(T_u^*=j_E\circ T_{u^{\mathrm t}}\).

**Proof.** (1) The operator \(f\mapsto f(x)y\) depends bilinearly on \((x,y)\), and this gives the linear map \(u\mapsto T_u\). The norm bound is the triangle inequality, and the range lies in the span of the \(y_i\). If \(T_u=0\), then \(\langle u,f\otimes g\rangle=g(T_uf)=0\) for all \(f,g\), so \(u=0\) by Lemma 1.1(3).

(2) For \(g\in F^*\) and \(f\in E^*\),
\((T_u^*g)(f)=g(T_uf)=\sum_if(x_i)g(y_i)=f\big(\sum_ig(y_i)x_i\big)=j_E(T_{u^{\mathrm t}}g)(f)\). \(\square\)

So \(E\odot F\) is a space of operators of finite rank from \(E^*\) to \(F\). Through \(u\mapsto u^{\mathrm t}\) it is also a space of operators of finite rank from \(F^*\) to \(E\), and the adjoint of each of the two operators of \(u\) is the other one followed by \(j_E\) or \(j_F\).

## 2. Cross norms: the injective and the projective norm

From now on \(E\), \(F\), \(G\) are Banach spaces.

**Definition 2.1.** A norm \(\beta\) on \(E\odot F\) is a *cross norm* if \(\beta(x\otimes y)=\|x\|\|y\|\) for all \(x\in E\) and \(y\in F\). We write \(E\otimes_\beta F\) for the normed space \((E\odot F,\beta)\) and \(E\hat\otimes_\beta F\) for its completion.

**Definition 2.2.** For \(u\in E\odot F\) put
\[
\lambda(u)=\sup\big\{|\langle u,f\otimes g\rangle|:\ f\in E^*,\ g\in F^*,\ \|f\|\le1,\ \|g\|\le1\big\},
\tag{2.1}
\]
\[
\gamma(u)=\inf\Big\{\sum_{i=1}^n\|x_i\|\|y_i\|:\ u=\sum_{i=1}^nx_i\otimes y_i\Big\}.
\tag{2.2}
\]
They are the *injective* and the *projective* norm. They are also written \(\varepsilon\) and \(\pi\).

**Theorem 2.3.**

1. \(\lambda(u)=\|T_u\|\) for every \(u\in E\odot F\). So \(\lambda\) is a norm, and \(u\mapsto T_u\) extends to an isometry of \(E\hat\otimes_\lambda F\) onto the norm closure of \(\{T_u:u\in E\odot F\}\) in \(B(E^*,F)\).
2. \(\lambda\le\gamma\), and both are cross norms.
3. If \(\beta\) is a seminorm on \(E\odot F\) with \(\beta(x\otimes y)\le\|x\|\|y\|\) for all \(x,y\), then \(\beta\le\gamma\). In particular \(\gamma\) is the largest cross norm.
4. \(|\langle u,v\rangle|\le\lambda(u)\,\gamma(v)\) for \(u\in E\odot F\) and \(v\in E^*\odot F^*\). Here \(\gamma(v)\) is the projective norm of \(v\), formed with the norms of \(E^*\) and \(F^*\).

**Proof.** (1) By Proposition 1.2(1) and the Hahn–Banach theorem in the form \(\|y\|=\sup_{\|g\|\le1}|g(y)|\),
\[
\lambda(u)=\sup_{\|f\|\le1}\ \sup_{\|g\|\le1}|g(T_uf)|=\sup_{\|f\|\le1}\|T_uf\|=\|T_u\| .
\]
The operator norm is a norm on \(B(E^*,F)\), and \(u\mapsto T_u\) is linear and injective, so \(\lambda\) is a norm. Since \(B(E^*,F)\) is complete, the isometry extends to the completion, with the closure of its range as image.

(2) For every representation of \(u\) and all \(\|f\|,\|g\|\le1\), \(|\sum_if(x_i)g(y_i)|\le\sum_i\|x_i\|\|y_i\|\). Hence \(\lambda\le\gamma\). The function \(\gamma\) is a seminorm: scaling the \(x_i\) of a representation of \(u\) gives \(\gamma(cu)\le|c|\gamma(u)\), with equality for \(c\ne0\) by applying this to \(c^{-1}\); and joining representations of \(u\) and \(u'\) gives \(\gamma(u+u')\le\gamma(u)+\gamma(u')\). As \(\lambda\le\gamma\) and \(\lambda\) is a norm, so is \(\gamma\). Finally, \(\lambda(x\otimes y)=\sup_{f,g}|f(x)||g(y)|=\|x\|\|y\|\) by the Hahn–Banach theorem, and \(\lambda(x\otimes y)\le\gamma(x\otimes y)\le\|x\|\|y\|\).

(3) For every representation, \(\beta(u)\le\sum_i\beta(x_i\otimes y_i)\le\sum_i\|x_i\|\|y_i\|\).

(4) By (2.1) and homogeneity, \(|\langle u,f\otimes g\rangle|\le\lambda(u)\|f\|\|g\|\). Summing over a representation \(v=\sum_kf_k\otimes g_k\) and taking the infimum gives the claim. \(\square\)

The word *injective* refers to Exercise 1: \(\lambda\) does not change when \(E\) and \(F\) are replaced by larger spaces that contain them isometrically.

**Proposition 2.4** (tensor products of operators). Let \(S\in B(E_1,E_2)\) and \(T\in B(F_1,F_2)\), and let \(S\otimes T:E_1\odot F_1\to E_2\odot F_2\) be the linear map with \(x\otimes y\mapsto Sx\otimes Ty\). For \(\beta=\lambda\) and for \(\beta=\gamma\),
\[
\beta\big((S\otimes T)u\big)\le\|S\|\|T\|\,\beta(u)\qquad(u\in E_1\odot F_1).
\tag{2.3}
\]
So \(S\otimes T\) extends to an operator \(E_1\hat\otimes_\beta F_1\to E_2\hat\otimes_\beta F_2\), of norm exactly \(\|S\|\|T\|\) when \(E_1\ne0\ne F_1\). The flip \(u\mapsto u^{\mathrm t}\) is an isometry of \(E\otimes_\beta F\) onto \(F\otimes_\beta E\) for both norms.

**Proof.** For \(\gamma\): if \(u=\sum_ix_i\otimes y_i\), then \((S\otimes T)u=\sum_iSx_i\otimes Ty_i\), and \(\gamma((S\otimes T)u)\le\sum_i\|Sx_i\|\|Ty_i\|\le\|S\|\|T\|\sum_i\|x_i\|\|y_i\|\); take the infimum. For \(\lambda\): for \(f\in E_2^*\) and \(g\in F_2^*\), \(\langle(S\otimes T)u,f\otimes g\rangle=\sum_if(Sx_i)g(Ty_i)=\langle u,S^*f\otimes T^*g\rangle\). By Theorem 2.3(4) with the elementary tensor \(S^*f\otimes T^*g\), this is at most \(\lambda(u)\|S^*f\|\|T^*g\|\le\|S\|\|T\|\lambda(u)\) when \(\|f\|,\|g\|\le1\). Both norms are cross norms, so testing (2.3) on elementary tensors gives the norm \(\|S\|\|T\|\). The flip statement holds because (2.1) and (2.2) are symmetric in the two factors. \(\square\)

**Example 2.5** (small cases). 1. If \(E=\mathbb C\), then \(c\otimes y\mapsto cy\) identifies \(E\odot F\) with \(F\), and \(\lambda\) and \(\gamma\) both become the norm of \(F\).

2. Let \(E=\ell^1_n\), that is \(\mathbb C^n\) with \(\|x\|_1=\sum_i|x_i|\) and standard basis \(e_1,\ldots,e_n\). By Lemma 1.1, applied with the two factors exchanged, every \(u\in E\odot F\) is \(\sum_ie_i\otimes y_i\) for unique \(y_i\in F\). Then
\[
\gamma(u)=\sum_i\|y_i\|,\qquad \lambda(u)=\sup\Big\{\sum_i|g(y_i)|:\ g\in F^*,\ \|g\|\le1\Big\}.
\tag{2.4}
\]
Indeed, \(\gamma(u)\le\sum_i\|e_i\|\|y_i\|\). Conversely, choose \(g_i\in F^*\) with \(\|g_i\|\le1\) and \(g_i(y_i)=\|y_i\|\). The bilinear form \(b(x,y)=\sum_ix_ig_i(y)\) satisfies \(|b(x,y)|\le\|x\|_1\|y\|\), so the functional it defines on \(E\odot F\) is bounded by \(\gamma\), by the argument of Theorem 2.3(3). Its value at \(u\) is \(\sum_i\|y_i\|\). For \(\lambda\), a functional of norm at most one on \(\ell^1_n\) is \(x\mapsto\sum_ic_ix_i\) with all \(|c_i|\le1\), and the best choice of the \(c_i\) turns \(|\sum_ic_ig(y_i)|\) into \(\sum_i|g(y_i)|\).

3. Take \(F=\ell^2_n\), \(\mathbb C^n\) with the Euclidean norm, and \(y_i=e_i\). Then \(\gamma(u)=n\), while \(\lambda(u)=\sup\{\sum_i|g_i|:\sum_i|g_i|^2\le1\}=\sqrt n\) by the Cauchy–Schwarz inequality. So \(\lambda\ne\gamma\) as soon as \(n\ge2\), and their ratio can be as large as we like.

4. For a compact Hausdorff space \(X\), \(C(X)\hat\otimes_\lambda F\) is the space of continuous functions \(X\to F\) with the supremum norm. For a positive Radon measure \(\mu\) on a locally compact space, \(L^1(\mu)\hat\otimes_\gamma F\) is the space of integrable functions with values in \(F\). Both are proved in [Vector-valued functions, tensor products with \(L^p\), and preduals](../measurable-fields-and-direct-integrals/vector-valued-functions-tensor-products-with-lp-and-preduals.html).

## 3. Dual norms and reasonable cross norms

**Definition 3.1.** Let \(\beta\) be a norm on \(E\odot F\). For \(v\in E^*\odot F^*\) put
\[
\beta^*(v)=\sup\{|\langle u,v\rangle|:\ u\in E\odot F,\ \beta(u)\le1\}\in[0,\infty] .
\tag{3.1}
\]
So \(\beta^*(v)<\infty\) exactly when \(u\mapsto\langle u,v\rangle\) is bounded on \(E\otimes_\beta F\), and then \(\beta^*(v)\) is the norm of this functional.

The next lemma computes the injective norm of \(E^*\odot F^*\). By definition it is a supremum over the unit balls of \(E^{**}\) and \(F^{**}\), but the unit balls of \(E\) and \(F\) are enough.

**Lemma 3.2.** For every \(v\in E^*\odot F^*\),
\[
\lambda(v)=\sup\{|\langle x\otimes y,v\rangle|:\ x\in E,\ y\in F,\ \|x\|\le1,\ \|y\|\le1\}.
\tag{3.2}
\]

**Proof.** Write \(v=\sum_kf_k\otimes g_k\). For \(\varphi\in E^{**}\) and \(\psi\in F^{**}\), \(\langle v,\varphi\otimes\psi\rangle=\psi\big(\sum_k\varphi(f_k)g_k\big)\). For fixed \(\varphi\), the Hahn–Banach theorem in the Banach space \(F^*\) says that the supremum over \(\|\psi\|\le1\) is the norm of \(\sum_k\varphi(f_k)g_k\) in \(F^*\). By the definition of that norm, it equals
\[
\sup_{\|y\|\le1}\Big|\sum_k\varphi(f_k)g_k(y)\Big|=\sup_{\|y\|\le1}\Big|\varphi\Big(\sum_kg_k(y)f_k\Big)\Big| .
\]
Now exchange the two suprema. For fixed \(y\), the supremum over \(\|\varphi\|\le1\) is the norm of \(\sum_kg_k(y)f_k\) in \(E^*\), which is \(\sup_{\|x\|\le1}|\sum_kf_k(x)g_k(y)|\). Altogether \(\lambda(v)=\sup_{x,y}|\sum_kf_k(x)g_k(y)|\), which is (3.2). \(\square\)

**Theorem 3.3** (reasonable cross norms). Let \(\beta\) be a cross norm on \(E\odot F\). The following are equivalent.

1. \(\lambda\le\beta\).
2. \(\beta^*(f\otimes g)\le\|f\|\|g\|\) for all \(f\in E^*\) and \(g\in F^*\).
3. \(\beta^*\) is finite on \(E^*\odot F^*\), and it is a cross norm there.

When they hold, \(\lambda\le\beta\le\gamma\) on \(E\odot F\), and \(\lambda\le\beta^*\le\gamma\) on \(E^*\odot F^*\).

We call \(\beta\) *reasonable* when these conditions hold, and \(\beta^*\) is then its *dual cross norm*. The norms \(\lambda\) and \(\gamma\) are reasonable, and \(\lambda\) is the smallest reasonable cross norm.

**Proof.** (1)⇒(3). By Theorem 2.3(4), \(|\langle u,v\rangle|\le\lambda(u)\gamma(v)\le\beta(u)\gamma(v)\), so \(\beta^*(v)\le\gamma(v)<\infty\). As a supremum of seminorms, \(\beta^*\) is a seminorm. It is a norm because \(E\odot F\) separates the points of \(E^*\odot F^*\) (Section 1). In particular \(\beta^*(f\otimes g)\le\gamma(f\otimes g)=\|f\|\|g\|\). Conversely, \(\beta(x\otimes y)=\|x\|\|y\|\le1\) when \(\|x\|,\|y\|\le1\), so \(\beta^*(f\otimes g)\ge\sup_{x,y}|f(x)||g(y)|=\|f\|\|g\|\).

(3)⇒(2) is clear. (2)⇒(1): \(\lambda(u)=\sup_{f,g}|\langle u,f\otimes g\rangle|\le\sup_{f,g}\beta(u)\,\beta^*(f\otimes g)\le\beta(u)\), the suprema over the unit balls.

For the last statement, \(\beta\le\gamma\) by Theorem 2.3(3), and \(\beta^*\le\gamma\) was shown above. By Lemma 3.2, \(\lambda(v)\) is a supremum of \(|\langle x\otimes y,v\rangle|\) over elementary tensors with \(\beta(x\otimes y)\le1\), so \(\lambda(v)\le\beta^*(v)\). \(\square\)

A cross norm need not be reasonable. The next example shows that cross norms can even be far smaller than \(\lambda\).

**Example 3.4** (a cross norm that is not reasonable). Let \(E=F=\mathbb C^2\) with the Euclidean norm, and identify \(E\odot F\) with the \(2\times2\) matrices \(M_2(\mathbb C)\) through \(x\otimes y\mapsto xy^{\mathrm T}\), the matrix with entries \(x_ky_l\). A functional on \(\mathbb C^2\) of norm at most one is \(x\mapsto a^{\mathrm T}x\) with \(\|a\|\le1\), and \(\langle w,f\otimes g\rangle=a^{\mathrm T}wb\) for \(f=a^{\mathrm T}(\cdot)\) and \(g=b^{\mathrm T}(\cdot)\). So \(\lambda(w)\) is the operator norm \(\|w\|\) of the matrix \(w\). Let \(\iota\) be the identity matrix, so \(\lambda(\iota)=1\).

Fix \(s>1\). Let \(C_s\) be the convex hull of the set of all \(xy^{\mathrm T}\) with \(\|x\|\|y\|\le1\) together with all \(\zeta s\iota\), \(|\zeta|=1\). It is compact, convex and balanced. It contains the open unit ball of \(\gamma\): if \(\gamma(w)<1\), then \(w=\sum_ix_iy_i^{\mathrm T}\) with \(t=\sum_i\|x_i\|\|y_i\|<1\), which is a convex combination of the matrices \(t\,x_iy_i^{\mathrm T}/(\|x_i\|\|y_i\|)\) (omitting zero terms) and \(0\). So the Minkowski functional \(\beta_s(w)=\inf\{r>0:w\in rC_s\}\) is a norm, and \(\beta_s(\iota)\le1/s<\lambda(\iota)\).

We show that \(\beta_s\) is a cross norm. Clearly \(\beta_s(xy^{\mathrm T})\le1\) for unit vectors \(x,y\). For the other inequality we find a functional \(\phi\) with \(|\phi|\le1\) on \(C_s\) and \(\phi(xy^{\mathrm T})=1\); then \(\beta_s(xy^{\mathrm T})\ge1\), since \(|\phi(w)|\le\beta_s(w)\) for every \(w\). For a matrix \(\Phi\) put \(\phi_\Phi(w)=\sum_{k,l}\Phi_{kl}w_{kl}\). Then \(\phi_\Phi(x'y'^{\mathrm T})=x'^{\mathrm T}\Phi y'\), which has modulus at most \(\|\Phi\|\|x'\|\|y'\|\), and \(\phi_\Phi(\iota)=\operatorname{tr}\Phi\). So we need \(\Phi\) with \(\|\Phi\|\le1\), \(x^{\mathrm T}\Phi y=1\) and \(\operatorname{tr}\Phi=0\). Let \(a=\bar x\) (entrywise conjugate) and \(b=y\), and choose unit vectors \(a'\perp a\) and \(b'\perp b\). For \(|t|\le1\) put \(\Phi=ab^*+t\,a'b'^*\). It maps the orthonormal basis \(b,b'\) to the orthogonal vectors \(a,ta'\), so \(\|\Phi\|\le1\), and \(x^{\mathrm T}\Phi y=x^{\mathrm T}\bar x=1\). Also \(\operatorname{tr}\Phi=\langle a,b\rangle+t\langle a',b'\rangle\). The matrix of inner products of the orthonormal bases \((a,a')\) and \((b,b')\) is unitary, and a \(2\times2\) unitary matrix has diagonal entries of equal modulus. So \(|\langle a,b\rangle|=|\langle a',b'\rangle|\). If \(\langle a',b'\rangle\ne0\), take \(t=-\langle a,b\rangle/\langle a',b'\rangle\), which has modulus one; otherwise \(\langle a,b\rangle=0\) and \(t=0\) works. In both cases \(\operatorname{tr}\Phi=0\), so \(\phi_\Phi\) vanishes at every \(\zeta s\iota\) and is bounded by one on \(C_s\).

So \(\beta_s(xy^{\mathrm T})=1\) for unit vectors, and by homogeneity \(\beta_s(xy^{\mathrm T})=\|x\|\|y\|\) for all \(x,y\): \(\beta_s\) is a cross norm with \(\beta_s(\iota)\le1/s\). By Theorem 3.3 it is not reasonable, and its dual function \(\beta_s^*\) is not a cross norm. Since \(s\) is arbitrary, no inequality \(c\lambda\le\beta\) with \(c>0\) holds for all cross norms \(\beta\) on \(E\odot F\), and \(E\odot F\) has no smallest cross norm.

## 4. Duality for the projective norm

**Theorem 4.1** (the dual of the projective tensor product).

1. Let \(\beta\) be a norm on \(E\odot F\) with \(\beta(x\otimes y)\le\|x\|\|y\|\), and let \(\varphi\) be a bounded linear functional on \(E\otimes_\beta F\). The formulas
\[
A_\varphi(x)(y)=\varphi(x\otimes y)=B_\varphi(y)(x)
\tag{4.1}
\]
define operators \(A_\varphi\in B(E,F^*)\) and \(B_\varphi\in B(F,E^*)\) with \(\|A_\varphi\|=\|B_\varphi\|=\sup\{|\varphi(x\otimes y)|:\|x\|,\|y\|\le1\}\le\|\varphi\|\). Each is the restriction of the adjoint of the other: \(B_\varphi=A_\varphi^*\circ j_F\) and \(A_\varphi=B_\varphi^*\circ j_E\).
2. For \(\beta=\gamma\), the map \(\varphi\mapsto A_\varphi\) is an isometric linear bijection of \((E\hat\otimes_\gamma F)^*\) onto \(B(E,F^*)\), and \(\varphi\mapsto B_\varphi\) is one onto \(B(F,E^*)\). The inverse sends \(A\in B(E,F^*)\) to the functional with \(\sum_ix_i\otimes y_i\mapsto\sum_iA(x_i)(y_i)\).

In other words, the dual of \(E\hat\otimes_\gamma F\) is the space of bounded bilinear forms on \(E\times F\), with the norm \(\sup\{|b(x,y)|:\|x\|,\|y\|\le1\}\).

**Proof.** (1) \(A_\varphi(x)\) is a linear functional on \(F\), and \(|\varphi(x\otimes y)|\le\|\varphi\|\beta(x\otimes y)\le\|\varphi\|\|x\|\|y\|\). Both operator norms equal the supremum of \(|\varphi(x\otimes y)|\) over the two unit balls. For the adjoints, \((A_\varphi^*j_F(y))(x)=j_F(y)(A_\varphi x)=\varphi(x\otimes y)=B_\varphi(y)(x)\), and symmetrically.

(2) Let \(A\in B(E,F^*)\). The bilinear form \((x,y)\mapsto A(x)(y)\) defines a linear functional \(\varphi_A\) on \(E\odot F\), and \(|\varphi_A(u)|\le\sum_i\|A\|\|x_i\|\|y_i\|\) for every representation of \(u\). So \(|\varphi_A(u)|\le\|A\|\gamma(u)\), and \(\varphi_A\) extends to the completion with \(\|\varphi_A\|\le\|A\|\). By construction \(A_{\varphi_A}=A\). For \(\varphi\in(E\hat\otimes_\gamma F)^*\), the functionals \(\varphi\) and \(\varphi_{A_\varphi}\) agree on elementary tensors, whose span is dense, so they are equal. Finally \(\|A_\varphi\|\le\|\varphi\|=\|\varphi_{A_\varphi}\|\le\|A_\varphi\|\) by (1). The statement for \(B_\varphi\) is the same with the factors exchanged. \(\square\)

The same duality is used in [Vector-valued functions, tensor products with \(L^p\), and preduals](../measurable-fields-and-direct-integrals/vector-valued-functions-tensor-products-with-lp-and-preduals.html) to find the dual of an \(L^1\) space of vector-valued functions.

**Corollary 4.2** (the universal property). Let \(\Phi:E\times F\to G\) be a bounded bilinear map, with \(\|\Phi\|=\sup\{\|\Phi(x,y)\|:\|x\|,\|y\|\le1\}\). There is exactly one operator \(\hat\Phi:E\hat\otimes_\gamma F\to G\) with \(\hat\Phi(x\otimes y)=\Phi(x,y)\), and \(\|\hat\Phi\|=\|\Phi\|\).

**Proof.** The linear map \(\hat\Phi\) on \(E\odot F\) defined by \(\Phi\) satisfies \(\|\hat\Phi(u)\|\le\sum_i\|\Phi(x_i,y_i)\|\le\|\Phi\|\sum_i\|x_i\|\|y_i\|\) for every representation. So \(\|\hat\Phi(u)\|\le\|\Phi\|\gamma(u)\), and \(\hat\Phi\) extends by continuity. Since \(\gamma(x\otimes y)=\|x\|\|y\|\), the values on elementary tensors give \(\|\hat\Phi\|\ge\|\Phi\|\). Two operators that agree on the elementary tensors agree on their dense span, hence everywhere. \(\square\)

The universal property characterizes the projective tensor product. We prove this with an inequality in (a) and, in (b), only the existence of a factorization of norm at most \(\|\Phi\|\); equality then follows in both.

**Proposition 4.3.** Let \(i:E\times F\to G\) be a bilinear map with the following properties.

- (a) \(\|i(x,y)\|\le\|x\|\|y\|\) for all \(x,y\).
- (b) For every Banach space \(G'\) and every bounded bilinear map \(\Phi:E\times F\to G'\) there is an operator \(\Phi_0:G\to G'\) with \(\Phi_0\circ i=\Phi\) and \(\|\Phi_0\|\le\|\Phi\|\).
- (c) The vectors \(i(x,y)\) span a dense subspace of \(G\).

Then the operator \(\hat\imath:E\hat\otimes_\gamma F\to G\) of Corollary 4.2 is an isometry of \(E\hat\otimes_\gamma F\) onto \(G\). Consequently \(\|i(x,y)\|=\|x\|\|y\|\), and the operator \(\Phi_0\) in (b) is unique and has norm \(\|\Phi\|\). Conversely, \(E\hat\otimes_\gamma F\) with the map \((x,y)\mapsto x\otimes y\) has these properties.

**Proof.** By (a) and Corollary 4.2, \(\|\hat\imath\|\le1\). Apply (b) with \(G'=E\hat\otimes_\gamma F\) and \(\Phi(x,y)=x\otimes y\), which has norm at most one. This gives \(\Phi_0:G\to E\hat\otimes_\gamma F\) with \(\|\Phi_0\|\le1\) and \(\Phi_0(i(x,y))=x\otimes y\). Then \(\Phi_0\circ\hat\imath\) is the identity on elementary tensors, hence on \(E\hat\otimes_\gamma F\). And \(\hat\imath\circ\Phi_0\) is the identity on the vectors \(i(x,y)\), hence on \(G\) by (c). So \(\hat\imath\) is bijective, and \(\hat\imath\) and its inverse \(\Phi_0\) are contractions, which makes \(\hat\imath\) isometric. In particular \(\|i(x,y)\|=\gamma(x\otimes y)=\|x\|\|y\|\). In (b), \(\Phi_0\) is determined on the dense span of the \(i(x,y)\), so \(\Phi_0=\hat\Phi\circ\hat\imath^{-1}\), which has norm \(\|\hat\Phi\|=\|\Phi\|\). The converse is Corollary 4.2 together with Theorem 2.3(2). \(\square\)

**Remark 4.4** (the hypotheses are needed). Without (c) the conclusion fails. Take \(G=(E\hat\otimes_\gamma F)\oplus\mathbb C\) with the norm \(\max(\gamma(w),|c|)\) and \(i(x,y)=(x\otimes y,0)\). Then (a) holds, and (b) holds with \(\Phi_0(w,c)=\hat\Phi(w)\), but \(\hat\imath\) is not onto. A bound as in (a) is needed as well. Take \(G=E\hat\otimes_\gamma F\) with \(E\ne0\ne F\) and \(i(x,y)=2\,x\otimes y\). Then (b) holds with \(\Phi_0=\frac12\hat\Phi\) and (c) holds, but \(\hat\imath=2\cdot\mathrm{id}\) is not isometric. If one asks for \(\|\Phi_0\|=\|\Phi\|\) in (b), the example fails (b), and the bound in (a) follows from (b) and (c): apply (b) to \(\Phi=i\) (when \(i\) is bounded) and note that \(\Phi_0\) must then be the identity of \(G\).

**Theorem 4.5** (the dual norm of \(\gamma\) is \(\lambda\)). For every \(v\in E^*\odot F^*\), \(\gamma^*(v)=\lambda(v)\). For every reasonable cross norm \(\beta\) on \(E\odot F\),
\[
\lambda(v)=\gamma^*(v)\le\beta^*(v)\le\lambda^*(v)\le\gamma(v)\qquad(v\in E^*\odot F^*).
\tag{4.2}
\]

**Proof.** The functional \(u\mapsto\langle u,v\rangle\) on \(E\otimes_\gamma F\) has norm \(\gamma^*(v)\). By Theorem 4.1, this norm is \(\sup\{|\langle x\otimes y,v\rangle|:\|x\|,\|y\|\le1\}\), which is \(\lambda(v)\) by Lemma 3.2. If \(\lambda\le\beta\le\gamma\), the unit balls satisfy the reverse inclusions, so \(\gamma^*\le\beta^*\le\lambda^*\). Finally \(\lambda^*\le\gamma\) by Theorem 3.3 applied to \(\beta=\lambda\). \(\square\)

So the dual of the projective norm is always the injective norm of the duals. The dual of the injective norm is not always the projective norm.

**Proposition 4.6** (the dual norm of \(\lambda\)).

1. \(\lambda^*\le\gamma\) on \(E^*\odot F^*\).
2. If \(E\) and \(F\) are finite-dimensional, then \(\lambda^*=\gamma\).
3. Let \(E\) be a Banach space whose dual \(E^*\) fails the approximation property, and let \(F=E^*\). Then \(\lambda^*\) and \(\gamma\) are not equivalent norms on \(E^*\odot F^*=E^*\odot E^{**}\). Such spaces \(E\) exist.

**Proof.** (1) is part of (4.2).

(2) In finite dimensions both \(E\odot F\) and \(E^*\odot F^*\) have dimension \(\dim E\cdot\dim F\). The pairing separates points on both sides, so every linear functional on \(E\odot F\) is \(u\mapsto\langle u,v\rangle\) for exactly one \(v\in E^*\odot F^*\). Apply Theorem 4.5 to the pair \(E^*,F^*\) in place of \(E,F\). Since \(j_E\) and \(j_F\) are bijective here, it says that for \(u\in E\odot F\),
\[
\sup\{|\langle u,v\rangle|:\ \gamma(v)\le1\}=\lambda(u),
\]
because by Lemma 3.2, applied to the pair \(E^*,F^*\), the injective norm of \(E^{**}\odot F^{**}=E\odot F\) can be computed on the unit balls of \(E^*\) and \(F^*\), and so it is the norm \(\lambda\) of \(E\odot F\). Thus \((E\odot F,\lambda)\) is isometric to the dual of \((E^*\odot F^*,\gamma)\) through the pairing. By the Hahn–Banach theorem, the norm \(\gamma(v)\) is the supremum of \(|\langle u,v\rangle|\) over the unit ball of this dual, that is over \(\lambda(u)\le1\). This is \(\lambda^*(v)\).

(3) By Corollary 4.11(1) below, since \(X=E^*\) fails the approximation property, there are sequences \((\varphi_n)\) in \(X^*=E^{**}\) and \((h_n)\) in \(X=E^*\) with \(\sum_n\|\varphi_n\|\|h_n\|<\infty\) and \(\sum_n\varphi_n(h)h_n=0\) for every \(h\in E^*\), such that \(\sum_n\varphi_n\otimes h_n\ne0\) in \(E^{**}\hat\otimes_\gamma E^*\). By Proposition 2.4 the flip is isometric, so \(v=\sum_nh_n\otimes\varphi_n\) is a nonzero element of \(E^*\hat\otimes_\gamma E^{**}\). The map \(J\) sending \(v'\in E^*\odot E^{**}\) to the functional \(u\mapsto\langle u,v'\rangle\) on \(E\otimes_\lambda E^*\) has \(\|Jv'\|=\lambda^*(v')\le\gamma(v')\), so it extends to \(E^*\hat\otimes_\gamma E^{**}\). By continuity, for \(x\in E\) and \(h\in E^*\),
\[
(Jv)(x\otimes h)=\sum_nh_n(x)\varphi_n(h)=\Big(\sum_n\varphi_n(h)h_n\Big)(x)=0 .
\]
So \(Jv=0\). Choose \(v_m\in E^*\odot E^{**}\) with \(\gamma(v_m-v)\to0\). Then \(\lambda^*(v_m)=\|Jv_m\|\to\|Jv\|=0\), while \(\gamma(v_m)\to\gamma(v)>0\). So no inequality \(\gamma\le c\lambda^*\) holds. Such spaces \(E\) exist: if \(X\) is a Banach space without the approximation property, then \(X^*\) fails it too, by Corollary 4.11(2), so \(E=X\) will do; A closed subspace of \(c_0\) without the approximation property is constructed in [Theorem 4.12](#4-12-a-closed-sequence-subspace-without-finite-rank-approximation). The first counterexample is due to Enflo [Enflo 1973]; the construction below follows Davie's method as presented in [Dacunha–Castelle 1974]. \(\square\)

The proof of (3) also shows that the natural map of \(E^*\hat\otimes_\gamma F^*\) into \((E\hat\otimes_\lambda F)^*\) need not be injective. It is injective when \(E^*\) or \(F^*\) has the approximation property (Corollary 4.11(3) below).

### The approximation property

A Banach space \(X\) has the *approximation property* if for every compact set \(K\subseteq X\) and every
\(\varepsilon>0\) there is an operator \(S\) of finite rank on \(X\) with \(\|Sx-x\|\le\varepsilon\) for all \(x\in K\).
Hilbert spaces have it: for an orthogonal projection \(P\) onto a large finite-dimensional subspace, \(\|Px-x\|\) is
small uniformly on a compact set. This subsection proves Grothendieck's criterion for it, which Proposition 4.6(3)
uses.

**Lemma 4.7** (series in the projective tensor product). Every \(w\in E\hat\otimes_\gamma F\) is the
\(\gamma\)-convergent sum \(w=\sum_nx_n\otimes y_n\) of a sequence with \(\sum_n\|x_n\|\|y_n\|<\infty\). For every
\(\varepsilon>0\) the sequence can be chosen with \(\sum_n\|x_n\|\|y_n\|\le\gamma(w)+\varepsilon\).

**Proof.** Choose \(w_k\in E\odot F\) with \(\gamma(w-w_k)\le\varepsilon4^{-k}\). Then
\(\gamma(w_{k+1}-w_k)\le\varepsilon4^{-k}\cdot2\), and by the definition of \(\gamma\), \(w_1\) and each \(w_{k+1}-w_k\)
have finite representations \(\sum_ix_i\otimes y_i\) with \(\sum_i\|x_i\|\|y_i\|\) at most \(\gamma(w_1)+\varepsilon/2\)
and at most \(3\varepsilon4^{-k}\) respectively. Listing all these terms gives a sequence with
\(\sum_n\|x_n\|\|y_n\|\le\gamma(w_1)+\varepsilon/2+\varepsilon\sum_k3\cdot4^{-k}\le\gamma(w)+\tfrac74\varepsilon\), whose
partial sums along the blocks are the \(w_k\). The full partial sums differ from the \(w_k\) by at most the tail of the
convergent series \(\sum\|x_n\|\|y_n\|\), so the series converges to \(w\). Replace \(\varepsilon\) by
\(\frac47\varepsilon\). \(\square\)

**Lemma 4.8** (compact sets are small). For every compact \(K\subseteq X\) there is a sequence \((z_n)\) in \(X\) with
\(\|z_n\|\to0\) such that every \(x\in K\) is \(\sum_nc_nz_n\) for numbers \(c_n\ge0\) with \(\sum_nc_n\le1\).

**Proof.** Let \(B\) be the closed unit ball. Choose a finite set \(F_1\subseteq K_1=K\) with \(K_1\subseteq F_1+4^{-1}B\),
and put \(K_2=\{x-f:x\in K_1,\ f\in F_1,\ \|x-f\|\le4^{-1}\}\), a compact set. Inductively choose a finite
\(F_k\subseteq K_k\) with \(K_k\subseteq F_k+4^{-k}B\) and put
\(K_{k+1}=\{x-f:x\in K_k,\ f\in F_k,\ \|x-f\|\le4^{-k}\}\). For \(x\in K\) choose \(f_1\in F_1\) with
\(x-f_1\in K_2\), then \(f_2\in F_2\) with \(x-f_1-f_2\in K_3\), and so on; then
\(\|x-\sum_{k\le m}f_k\|\le4^{-m}\), so \(x=\sum_kf_k\) with \(f_k\in F_k\). For \(k\ge2\), \(F_k\subseteq K_k\) consists
of vectors of norm at most \(4^{1-k}\). Let \((z_n)\) list the vectors \(2^kf\), \(f\in F_k\), \(k\ge1\), in order of
\(k\); for \(k\ge2\) they have norm at most \(4\cdot2^{-k}\), so \(\|z_n\|\to0\). Then
\(x=\sum_k2^{-k}(2^kf_k)\) is of the required form, with \(\sum_k2^{-k}=1\). \(\square\)

Let \(\tau_c\) be the topology on \(B(X)\) of uniform convergence on compact sets, given by the seminorms
\(p_K(T)=\sup_{x\in K}\|Tx\|\), \(K\subseteq X\) compact.

**Lemma 4.9** (functionals continuous for \(\tau_c\)). Let \(\ell\) be a linear functional on \(B(X)\) with
\(|\ell(T)|\le C\,p_K(T)\) for a compact \(K\) and a constant \(C\). There are \(\psi_n\in X^*\) and \(z_n\in X\) with
\(\sum_n\|\psi_n\|\|z_n\|<\infty\) and \(\ell(T)=\sum_n\psi_n(Tz_n)\) for all \(T\in B(X)\).

**Proof.** Take \((z_n)\) for \(K\) from Lemma 4.8. For \(x=\sum_nc_nz_n\in K\), \(\|Tx\|\le\sum_nc_n\|Tz_n\|\le
\sup_n\|Tz_n\|\), so \(|\ell(T)|\le C\sup_n\|Tz_n\|\). Let \(c_0(X)\) be the Banach space of sequences in \(X\) that tend
to \(0\), with the supremum norm. The map \(\Phi:T\mapsto(Tz_n)_n\) sends \(B(X)\) into \(c_0(X)\), and
\(\lambda(\Phi T)=\ell(T)\) is a well-defined linear functional on \(\Phi(B(X))\) of norm at most \(C\). By the
Hahn–Banach theorem (Hahn–Banach, Baire and the basic theorems on Banach spaces, Section 2) it extends to
\(\Lambda\in c_0(X)^*\). Put \(\psi_n(y)=\Lambda(y\delta_n)\), where \(y\delta_n\) has \(y\) in place \(n\) and \(0\)
elsewhere. Given \(N\) and \(\delta>0\), choose unit vectors \(y_n\) with \(\psi_n(y_n)\ge\|\psi_n\|-\delta\); the
sequence \((y_1,\dots,y_N,0,\dots)\) has norm at most \(1\), so \(\sum_{n\le N}(\|\psi_n\|-\delta)\le\|\Lambda\|\). Hence
\(\sum_n\|\psi_n\|\le\|\Lambda\|\). A sequence \((y_n)\in c_0(X)\) is the norm limit of its truncations, so
\(\Lambda((y_n))=\sum_n\psi_n(y_n)\). With \(y_n=Tz_n\) this gives the formula, and
\(\sum_n\|\psi_n\|\|z_n\|\le\|\Lambda\|\sup_n\|z_n\|\). \(\square\)

**Theorem 4.10** (Grothendieck's criterion). For a Banach space \(X\) the following are equivalent.

1. \(X\) has the approximation property.
2. If \(\varphi_n\in X^*\) and \(x_n\in X\) satisfy \(\sum_n\|\varphi_n\|\|x_n\|<\infty\) and
   \(\sum_n\varphi_n(x)x_n=0\) for every \(x\in X\), then \(\sum_n\varphi_n(x_n)=0\).
3. The operator \(X^*\hat\otimes_\gamma X\to B(X)\) that extends \(\varphi\otimes x\mapsto\varphi(\cdot)x\) is
   injective.

**Proof.** The operator in (3) exists by Corollary 4.2, applied to the bilinear map \((\varphi,x)\mapsto\varphi(\cdot)x\)
of norm one, and it sends \(\sum_n\varphi_n\otimes x_n\) to \(x\mapsto\sum_n\varphi_n(x)x_n\). Likewise the *trace*
\(\operatorname{tr}(\varphi\otimes x)=\varphi(x)\) extends to a functional on \(X^*\hat\otimes_\gamma X\) of norm at most
one.

(1)\(\Rightarrow\)(3). Let \(u\) have image \(0\). By Lemma 4.7, \(u=\sum_n\varphi_n\otimes x_n\) with
\(\sum_n\|\varphi_n\|\|x_n\|<\infty\); dropping zero terms, choose \(\rho_n\to\infty\) with
\(\sum_n\rho_n\|\varphi_n\|\|x_n\|<\infty\) and put \(x_n'=x_n/(\rho_n\|x_n\|)\) and
\(\varphi_n'=\rho_n\|x_n\|\varphi_n\). Then \(u=\sum_n\varphi_n'\otimes x_n'\), \(\sum_n\|\varphi_n'\|<\infty\), and
\(K=\{0\}\cup\{x_n'\}\) is compact because \(\|x_n'\|=1/\rho_n\to0\). For \(\psi\in X^*\) and \(x\in X\),
\(\sum_n\psi(x_n')\varphi_n'(x)=\psi\bigl(\sum_n\varphi_n'(x)x_n'\bigr)=0\), so \(\sum_n\psi(x_n')\varphi_n'=0\). Hence, for
a finite-rank operator \(S=\sum_j\psi_j(\cdot)y_j\),
\[
\sum_n\varphi_n'\otimes Sx_n'=\sum_j\Bigl(\sum_n\psi_j(x_n')\varphi_n'\Bigr)\otimes y_j=0 .
\]
So \(\gamma(u)=\gamma\bigl(\sum_n\varphi_n'\otimes(x_n'-Sx_n')\bigr)\le\sum_n\|\varphi_n'\|\,\sup_{x\in K}\|x-Sx\|\), which
is as small as we like by (1). So \(u=0\).

(3)\(\Rightarrow\)(2). Under the hypothesis of (2), \(u=\sum_n\varphi_n\otimes x_n\) has image \(0\), so \(u=0\) and
\(\sum_n\varphi_n(x_n)=\operatorname{tr}(u)=0\).

(2)\(\Rightarrow\)(1). Suppose \(X\) fails the approximation property: for some compact \(K\) and \(\varepsilon>0\),
\(p_K(1-S)>\varepsilon\) for every finite-rank \(S\). On the span of the finite-rank operators and \(1\), put
\(\ell(S+t1)=t\). For \(t\ne0\), \(p_K(S+t1)=|t|\,p_K(1-(-S/t))>|t|\varepsilon\), so \(|\ell|\le\varepsilon^{-1}p_K\)
there. The Hahn–Banach theorem with the seminorm \(\varepsilon^{-1}p_K\) extends \(\ell\) to \(B(X)\) with the same
bound, and Lemma 4.9 writes \(\ell(T)=\sum_n\psi_n(Tz_n)\) with \(\sum_n\|\psi_n\|\|z_n\|<\infty\). For
\(S=\psi(\cdot)y\), \(0=\ell(S)=\psi\bigl(\sum_n\psi_n(y)z_n\bigr)\) for all \(\psi\), so \(\sum_n\psi_n(y)z_n=0\) for every
\(y\); but \(\sum_n\psi_n(z_n)=\ell(1)=1\). So (2) fails. \(\square\)

**Corollary 4.11.**

1. If \(X\) fails the approximation property, there are \(\varphi_n\in X^*\) and \(x_n\in X\) with
   \(\sum_n\|\varphi_n\|\|x_n\|<\infty\) and \(\sum_n\varphi_n(x)x_n=0\) for every \(x\in X\), such that
   \(\sum_n\varphi_n\otimes x_n\ne0\) in \(X^*\hat\otimes_\gamma X\).
2. If \(X^*\) has the approximation property, so has \(X\).
3. If \(E^*\) or \(F^*\) has the approximation property, then the operator of \(E^*\hat\otimes_\gamma F^*\) into
   \((E\hat\otimes_\lambda F)^*\) that extends \(\langle\cdot,v\rangle\), \(v\in E^*\odot F^*\), is injective.

**Proof.** (1) Theorem 4.10 gives sequences as stated with \(\sum_n\varphi_n(x_n)\ne0\); the trace of
\(\sum_n\varphi_n\otimes x_n\) is this number, so the element is not \(0\).

(2) Suppose \(X\) fails the approximation property, and take \(\psi_n\in X^*\), \(z_n\in X\) as in the proof of
(2)\(\Rightarrow\)(1). Put \(\Phi_n=j_X(z_n)\in X^{**}\). Then \(\sum_n\|\Phi_n\|\|\psi_n\|<\infty\), and for \(f\in X^*\)
and \(y\in X\), \(\bigl(\sum_n\Phi_n(f)\psi_n\bigr)(y)=f\bigl(\sum_n\psi_n(y)z_n\bigr)=0\); so
\(\sum_n\Phi_n(f)\psi_n=0\) for every \(f\in X^*\), while \(\sum_n\Phi_n(\psi_n)=\sum_n\psi_n(z_n)=1\). By Theorem 4.10,
applied to \(X^*\), the space \(X^*\) fails the approximation property.

(3) Let \(F^*\) have the approximation property, and let \(v\in E^*\hat\otimes_\gamma F^*\) define the zero functional on
\(E\hat\otimes_\lambda F\). By Lemma 4.7 and the rescaling in the proof of Theorem 4.10, \(v=\sum_ne_n\otimes f_n\) with
\(\sum_n\|e_n\|<\infty\) and \(\|f_n\|\to0\). For \(x\in E\) and \(y\in F\), \(\sum_ne_n(x)f_n(y)=0\), so
\(\sum_ne_n(x)f_n=0\) in \(F^*\). For a finite-rank operator \(S=\sum_j\Psi_j(\cdot)g_j\) on \(F^*\), with
\(\Psi_j\in F^{**}\), \(\bigl(\sum_n\Psi_j(f_n)e_n\bigr)(x)=\Psi_j\bigl(\sum_ne_n(x)f_n\bigr)=0\), so
\(\sum_ne_n\otimes Sf_n=\sum_j\bigl(\sum_n\Psi_j(f_n)e_n\bigr)\otimes g_j=0\), and
\(\gamma(v)\le\sum_n\|e_n\|\sup_m\|f_m-Sf_m\|\), which is small for suitable \(S\) because \(\{0\}\cup\{f_n\}\) is
compact. So \(v=0\). If \(E^*\) has the approximation property, apply this to the flipped element of
\(F^*\hat\otimes_\gamma E^*\) (Proposition 2.4). \(\square\)

*Reference:* Theorem 4.10 and Corollary 4.11 are due to Grothendieck.


### 4.12. A closed sequence subspace without finite-rank approximation

**Theorem 4.12.** There is a closed complex linear subspace of the sequence space
\(c_0\) without the approximation property. There is also a real example.

Here the approximation property means: for every compact \(K\subset X\) and
every \(\eta>0\), there is a bounded finite-rank linear map \(R:X\to X\) such
that \(\sup_{x\in K}\|Rx-x\|<\eta\). The proof below produces one compact set
on which that error cannot be less than \(1/3\).

*Proof.* The construction follows Davie's method in the exposition [Dacunha–Castelle 1974]. The probabilistic estimates, coefficient maps and compact-set obstruction are proved below.

#### The certificate we will construct

We will construct a Banach space \(X\), a compact subset \(K\), and a bounded
linear functional \(b:B(X)\to\mathbb C\) with

\[
b(I_X)=1,\qquad b(R)=0\quad\text{for every finite-rank }R,
\qquad |b(T)|\le3\sup_{x\in K}\|Tx\|.                 \tag{4.12.1}
\]

These identities immediately rule out the approximation property: apply the
last inequality to \(T=I_X-R\). In particular, the compact set must control
the *whole* functional, not just a series of differences of functionals.

#### A finite probability estimate

All probabilities in this proof are on finite product spaces. If a real random
variable \(Y\) lies in \([-1,1]\) and has mean zero, convexity gives

\[
e^{tY}\le\frac{1+Y}{2}e^t+\frac{1-Y}{2}e^{-t},\qquad
\mathbb E e^{tY}\le\cosh t\le e^{t^2/2}.
\]

The final inequality follows termwise from \((2k)!\ge2^k k!\) in the power
series. Consequently, for independent such variables \(Y_1,\dots,Y_m\) and
real coefficients \(a_j\) of absolute value at most one,
\(\mathbb E\exp(t\sum a_jY_j)\le\exp(mt^2/2)\).
For a nonnegative random variable \(Z\), summing over the event \(Z\ge s\)
gives \(\mathbb P(Z\ge s)\le\mathbb EZ/s\). Apply this to the exponential
and take \(t=v/m\) to obtain each one-sided tail bound
\(\exp(-v^2/(2m))\). Apply both tails to the real and imaginary parts. For
complex coefficients \(|c_j|\le1\), this proves

\[
\mathbb P\left(\left|\sum_{j=1}^m c_jY_j\right|>u\right)
\le4\exp\left(-\frac{u^2}{4m}\right).                \tag{4.12.2}
\]

Indeed, a complex number of modulus greater than \(u\) has a real or imaginary
part of absolute value greater than \(u/\sqrt2\). The probability of a union
is at most the sum of the probabilities because its indicator is at most the
sum of the event indicators. These are the only probabilistic tools used below.

#### Finite Fourier data and the closed sequence subspace

For every integer \(n\ge0\), put \(m_n=2^n\), \(N_n=3m_n\), and let
\(G_n=\mathbb Z/N_n\mathbb Z\). Regard the groups as disjoint sets and put
\(G=\coprod_{n\ge0}G_n\). Its characters are
\(\chi_r(g)=\exp(2\pi i rg/N_n)\), \(0\le r<N_n\).
The finite geometric-series formula gives

\[
\frac1{N_n}\sum_{g\in G_n}\overline{\chi_r(g)}\chi_s(g)
=\begin{cases}1&r=s,\\0&r\ne s.\end{cases}           \tag{4.12.3}
\]

Partition these characters into sets \(S_n,T_n\) with respectively \(m_n\)
and \(2m_n\) elements, so that

\[
\left|2\sum_{\chi\in S_n}\chi(g)-\sum_{\chi\in T_n}\chi(g)\right|
\le d_n:=12\sqrt{N_n\log(8N_n)}\quad(g\in G_n).       \tag{4.12.4}
\]

Here is an existence proof with the cardinalities enforced. Independently put
each character into a preliminary set with probability \(1/3\). Write its
indicator as \(B_r\), and take \(Y_r=B_r-1/3\). By (4.12.2), with
\(u=\sqrt{4N_n\log(8N_n)}\), the probability that
\(|\sum_rY_r\chi_r(g)|\le u\) fails for any of the \(N_n\) choices of
\(g\) is at most \(1/2\). Choose a successful outcome. At the identity of
the group the same bound says that its cardinality differs from \(N_n/3\)
by at most \(u\). Add or remove exactly that many characters to obtain
cardinality \(m_n\). Each change changes the character sum by a number of
modulus one. Thus the final centered sum has modulus at most \(2u\);
multiplying it by three gives (4.12.4), since \(6u=d_n\).

List \(S_n=(\sigma_{n,j})_{j=1}^{m_n}\) and
\(T_n=(\tau_{n,j})_{j=1}^{2m_n}\). For each \(n\ge1\), choose signs
\(\epsilon_{n,j}\in\{-1,1\}\) such that

\[
\left|\sum_{j=1}^{m_n}\epsilon_{n,j}
\tau_{n-1,j}(g)\overline{\sigma_{n,j}(h)}\right|
\le v_n:=2\sqrt{m_n\log(8P_n)},
\quad g\in G_{n-1},\ h\in G_n,                       \tag{4.12.5}
\]

where \(P_n=N_{n-1}N_n\). To see existence, choose independent signs with
equal probabilities. Apply (4.12.2) to each pair \((g,h)\), then sum the failure
probabilities. Their sum is at most \(4P_n/(8P_n)=1/2\).
Complex conjugation gives the corresponding reversed-conjugation bound; a
second, incompatible selection of signs is not necessary.

These are finite nonempty choices for each \(n\); one can fix an ordering of
all partitions and sign strings and select the first successful one.

Define \(u_{n,j}:G\to\mathbb C\), for \(n\ge1\), by

\[
u_{n,j}(h)=
\begin{cases}
\tau_{n-1,j}(h),&h\in G_{n-1},\\
\epsilon_{n,j}\sigma_{n,j}(h),&h\in G_n,\\
0,&\text{otherwise}.
\end{cases}                                                        \tag{4.12.6}
\]

Let \(X\) be their closed linear span in the supremum norm. Every generator
has finite support and norm one, so \(X\subset c_0(G)\): a uniform limit of
finite-support functions tends to zero outside finite sets. The space
\(c_0(G)\) is complete, since a uniformly Cauchy sequence has a uniform
coordinatewise limit and this limit still vanishes outside finite sets.
Therefore \(X\) is Banach. Enumerating the countable set \(G\) identifies
\(c_0(G)\) isometrically with the usual \(c_0\).

The following two formulas define the same bounded functional
\(f_{n,j}:X\to\mathbb C\):

\[
f_{n,j}(x)=\frac{\epsilon_{n,j}}{N_n}
\sum_{g\in G_n}\overline{\sigma_{n,j}(g)}x(g)
=\frac1{N_{n-1}}\sum_{g\in G_{n-1}}
\overline{\tau_{n-1,j}(g)}x(g).                         \tag{4.12.7}
\]

Both have norm at most one. On a generator \(u_{k,l}\), equation (4.12.3) shows
that both are \(1\) if \((k,l)=(n,j)\), and zero otherwise: at either
overlapping block the other family belongs to the disjoint set of characters.
Equality on the dense generator span proves equality on all of \(X\).
In particular \(f_{n,j}(u_{k,l})=\delta_{nk}\delta_{jl}\).

#### Trace differences with summable norm bounds

For \(T\in B(X)\), define

\[
b_n(T)=\frac1{m_n}\sum_{j=1}^{m_n}f_{n,j}(Tu_{n,j}).   \tag{4.12.8}
\]

These are linear functionals with \(\|b_n\|\le1\) and \(b_n(I_X)=1\).
For \(g\in G_n\), put

\[
w_{n,g}=\frac1{m_{n+1}}\sum_{j=1}^{m_{n+1}}
\overline{\tau_{n,j}(g)}u_{n+1,j}
-\frac1{m_n}\sum_{j=1}^{m_n}\epsilon_{n,j}
\overline{\sigma_{n,j}(g)}u_{n,j}\in X.                 \tag{4.12.9}
\]

Use the first formula of (4.12.7) for \(b_n\) and the second for \(b_{n+1}\).
All sums are finite, and the denominators then give the exact identity

\[
b_{n+1}(T)-b_n(T)=\frac1{N_n}\sum_{g\in G_n}(Tw_{n,g})(g). \tag{4.12.10}
\]

For clarity, the three nonzero blocks of \(w_{n,g}\), evaluated at \(h\), are

\[
\begin{array}{ll}
h\in G_{n-1}:&-m_n^{-1}\sum_j\epsilon_{n,j}
\overline{\sigma_{n,j}(g)}\tau_{n-1,j}(h),\\[2pt]
h\in G_n:&(2m_n)^{-1}\left(\sum_j\tau_{n,j}(h-g)
-2\sum_j\sigma_{n,j}(h-g)\right),\\[2pt]
h\in G_{n+1}:&m_{n+1}^{-1}\sum_j\epsilon_{n+1,j}
\overline{\tau_{n,j}(g)}\sigma_{n+1,j}(h).
\end{array}                                                       \tag{4.12.11}
\]

Thus (4.12.4) and (4.12.5) imply

\[
\|w_{n,g}\|\le\delta_n:=
\max\left\{\frac{v_n}{m_n},\frac{d_n}{2m_n},
\frac{v_{n+1}}{m_{n+1}}\right\}.                       \tag{4.12.12}
\]

Explicitly \(\log(8N_n)=\log24+n\log2\) and
\(\log(8P_n)=\log36+2n\log2\). Hence \(\delta_n\) is bounded by a fixed
constant times \(\sqrt{n+1}\,2^{-n/2}\). This tends to zero even after
multiplication by \(n^2\), and its sum converges: the successive-term ratio
of each polynomial-times-geometric bound tends to \(1/\sqrt2<1\), so its
tail is bounded by a geometric series with ratio strictly less than one.

By (4.12.10), \(|b_{n+1}(T)-b_n(T)|\le\delta_n\|T\|\). Consequently
\(b(T):=\lim_{n\to\infty}b_n(T)\) exists for every \(T\), is linear,
has norm at most one, and satisfies \(b(I_X)=1\).

It annihilates every finite-rank operator. First, if the range of \(R\) lies
in the span of generators with indices at most \(q\), then (4.12.7) gives
\(b_n(R)=0\) whenever \(n>q\), hence \(b(R)=0\). Every bounded finite-rank
operator is \(Rx=\sum_{i=1}^r\phi_i(x)y_i\), where \(\phi_i\in X^*\):
choose a basis of its finite-dimensional range and compose its continuous
coordinate functionals with \(R\). Those coordinate functionals are bounded
because on the Euclidean coefficient unit sphere the norm of the basis
combination has a positive minimum (continuity, compactness and independence).
Approximating each \(y_i\) by generator combinations produces such operators
\(R_k\) with
\(\|R-R_k\|\le\sum_i\|\phi_i\|\|y_i-y_{i,k}\|\to0\).
Continuity of \(b\) gives \(b(R)=0\).

#### The compact witness includes the initial trace

Set

\[
K=\{0,u_{1,1},u_{1,2}\}\ \cup\
\{n^2w_{n,g}:n\ge1,\ g\in G_n\}.                     \tag{4.12.13}
\]

For any neighborhood of zero, all sufficiently high blocks lie in it because
\(n^2\delta_n\to0\). Each remaining block is finite. An open cover of
\(K\) has a member containing zero, hence contains the entire tail; finitely
many further members cover the finitely many remaining points. Thus \(K\)
is compact, without any assumption that bounded subsets of \(X\) are compact.

Write \(p_K(T)=\sup_{x\in K}\|Tx\|\). Equation (4.12.8) for \(n=1\) gives
\(|b_1(T)|\le p_K(T)\). Equation (4.12.10) gives
\(|b_{n+1}(T)-b_n(T)|\le n^{-2}p_K(T)\). Telescoping now controls the whole
limit, including its initial term:

\[
|b(T)|\le\left(1+\sum_{n=1}^{\infty}\frac1{n^2}\right)p_K(T)
\le3p_K(T),                                         \tag{4.12.14}
\]

where \(\sum_{n\ge1}n^{-2}\le1+\int_1^\infty t^{-2}\,dt=2\).
This proves every part of (4.12.1), and therefore the complex result.

For the real statement, if the underlying real space of \(X\) had the
approximation property, approximate on \(K\cup iK\) by a real finite-rank
operator \(R\). Then
\(R_{\mathbb C}x=(Rx-iR(ix))/2\) is complex linear, has finite complex
rank, and its error on \(K\) is no greater than the maximum error of \(R\)
on \(K\cup iK\). This contradicts the complex result. Finally, the real
linear map sending each complex coordinate to its real and imaginary parts
embeds this underlying real space as a closed subspace of real \(c_0\).
Its supremum norm and the original norm differ by factors between one and
\(\sqrt2\). A bounded linear isomorphism transports finite-rank operators
and compact sets, with error multiplied by at most its two operator norms,
so the approximation property is invariant under this change. This proves
the real result as well.

**Consequence for the tensor norms.** For the complex space \(X\) just constructed, Corollary 4.11(2) implies that \(X^*\) also fails the approximation property. Taking \(E=X\) in Proposition 4.6(3) therefore gives its asserted examples.

## 5. The Hilbert cross norm and singular values

Let \(H\) and \(K\) be Hilbert spaces. The *conjugate space* \(\overline H\) consists of symbols \(\bar\xi\), \(\xi\in H\), with \(\bar\xi+\bar\eta=\overline{\xi+\eta}\), \(c\,\bar\xi=\overline{\bar c\,\xi}\) and \(\langle\bar\xi,\bar\eta\rangle=\langle\eta,\xi\rangle\). It is a Hilbert space, and \(\xi\mapsto\bar\xi\) is a conjugate-linear isometry of \(H\) onto \(\overline H\). By the Riesz theorem, \(\zeta\mapsto(\bar\xi\mapsto\langle\zeta,\xi\rangle)\) is a linear isometry of \(H\) onto \(\overline H^{\,*}\). We use this identification throughout.

For \(\xi\in H\) and \(\eta\in K\), \(\theta_{\eta,\xi}\in B(H,K)\) is the operator \(\zeta\mapsto\langle\zeta,\xi\rangle\eta\). It is linear in \(\eta\) and in \(\bar\xi\), and \(\theta_{\eta,\xi}^*=\theta_{\xi,\eta}\), \(A\theta_{\eta,\xi}B=\theta_{A\eta,B^*\xi}\), \(\|\theta_{\eta,\xi}\|=\|\eta\|\|\xi\|\). With \(E=\overline H\), \(E^*=H\) and \(F=K\), the operator (1.1) of \(\bar\xi\otimes\eta\) is exactly \(\theta_{\eta,\xi}\). So Proposition 1.2 identifies \(\overline H\odot K\) with the space \(\mathcal F(H,K)\) of operators \(H\to K\) of finite rank. The map is onto, because an operator \(T\) of finite rank equals \(\sum_k\theta_{f_k,T^*f_k}\) for an orthonormal basis \(f_1,\ldots,f_m\) of its range. From now on we identify \(u\in\overline H\odot K\) with the operator \(T_u\), and we write \(\lambda(T)\) and \(\gamma(T)\) for \(T\in\mathcal F(H,K)\). By Theorem 2.3(1), \(\lambda(T)=\|T\|\).

The space \(\overline H\odot K\) also carries the inner product of the Hilbert tensor product, \(\langle\bar\xi\otimes\eta,\bar\xi'\otimes\eta'\rangle=\langle\xi',\xi\rangle\langle\eta,\eta'\rangle\). We write \(\sigma\) for its norm and call it the *Hilbert cross norm*. It is a cross norm, and the completion is the Hilbert space \(\overline H\otimes K\). The Hilbert cross norm is the only cross norm that comes from an inner product, provided the scalars are complex.

**Theorem 5.1** (uniqueness of the Hilbert cross norm). Let \(H\) and \(K\) be complex Hilbert spaces, and let \(\langle\cdot,\cdot\rangle'\) be an inner product on \(H\odot K\) with \(\langle x\otimes y,x\otimes y\rangle'=\|x\|^2\|y\|^2\) for all \(x\in H\) and \(y\in K\). Then \(\langle\cdot,\cdot\rangle'\) is the inner product of the Hilbert tensor product. No completeness or continuity of \(\langle\cdot,\cdot\rangle'\) is assumed.

**Proof.** Let \(D(\zeta,\zeta')=\langle\zeta,\zeta'\rangle'-\langle\zeta,\zeta'\rangle\). It is sesquilinear, and \(D(x\otimes y,x\otimes y)=0\) for all \(x,y\). A sesquilinear form \(s\) on a complex vector space satisfies the polarization identity \(s(a,b)=\frac14\sum_{k=0}^3i^k\,s(a+i^kb,\,a+i^kb)\), so it vanishes when its quadratic form vanishes. For fixed \(y\), apply this to \((x,x')\mapsto D(x\otimes y,x'\otimes y)\): so \(D(x\otimes y,x'\otimes y)=0\) for all \(x,x',y\). For fixed \(x,x'\), apply it to \((y,y')\mapsto D(x\otimes y,x'\otimes y')\), whose quadratic form we just showed to vanish. So \(D\) vanishes on all pairs of elementary tensors, and by sesquilinearity \(D=0\). \(\square\)

**Example 5.2** (real scalars). Theorem 5.1 fails over the real numbers. Let \(H=K=\mathbb R^2\), let \(J\) be the rotation \(J(a,b)=(-b,a)\), and let \(Q=J\otimes J\) on \(\mathbb R^2\otimes\mathbb R^2\). Since \(J^{\mathrm T}=-J\), \(Q\) is symmetric, and \(Q^2=J^2\otimes J^2=1\), so \(\|Q\|=1\). For \(0<|t|<1\), \(\langle\zeta,\zeta'\rangle_t=\langle(1+tQ)\zeta,\zeta'\rangle\) is an inner product different from the Hilbert tensor product one, because \(Q\ne0\). But \(\langle Jx,x\rangle=0\) for every real \(x\), so \(\langle x\otimes y,x\otimes y\rangle_t=\|x\|^2\|y\|^2+t\langle Jx,x\rangle\langle Jy,y\rangle=\|x\|^2\|y\|^2\). Each \(\langle\cdot,\cdot\rangle_t\) gives a cross norm. The complex proof breaks at the second polarization step. Over the real field, a bilinear form with vanishing quadratic form need only be antisymmetric, not zero. Here \(D(x\otimes y,x'\otimes y')=t\langle Jx,x'\rangle\langle Jy,y'\rangle\): it vanishes when \(x=x'\) or \(y=y'\), but for fixed \(x,x'\) with \(\langle Jx,x'\rangle\ne0\) it is a nonzero antisymmetric form in \((y,y')\).

**Lemma 5.3** (the trace of a finite-rank operator). There is a unique linear functional \(\operatorname{Tr}\) on \(\mathcal F(H)=\mathcal F(H,H)\) with \(\operatorname{Tr}\theta_{\eta,\xi}=\langle\eta,\xi\rangle\). For every orthonormal basis \((e_i)\) of \(H\) and \(T\in\mathcal F(H)\), \(\operatorname{Tr}T=\sum_i\langle Te_i,e_i\rangle\), the series converging absolutely. For \(T\in\mathcal F(H,K)\) and \(B\in B(K,H)\), \(\operatorname{Tr}(BT)=\operatorname{Tr}(TB)\). Finally \(|\operatorname{Tr}T|\le\gamma(T)\).

**Proof.** The form \((\bar\xi,\eta)\mapsto\langle\eta,\xi\rangle\) is bilinear on \(\overline H\times H\), which defines \(\operatorname{Tr}\). For \(T=\theta_{\eta,\xi}\), \(\sum_i\langle Te_i,e_i\rangle=\sum_i\langle e_i,\xi\rangle\langle\eta,e_i\rangle=\langle\eta,\xi\rangle\) by Parseval's identity, and the series converges absolutely by the Cauchy–Schwarz inequality in \(\ell^2\). Linearity gives the formula for every \(T\). For \(T=\theta_{\eta,\xi}\) with \(\xi\in H\), \(\eta\in K\): \(BT=\theta_{B\eta,\xi}\) and \(TB=\theta_{\eta,B^*\xi}\), whose traces are \(\langle B\eta,\xi\rangle=\langle\eta,B^*\xi\rangle\). Finally \(|\operatorname{Tr}\theta_{\eta,\xi}|\le\|\eta\|\|\xi\|\), so \(|\operatorname{Tr}T|\le\sum_i\|\xi_i\|\|\eta_i\|\) for every representation \(T=\sum_i\theta_{\eta_i,\xi_i}\). \(\square\)

In operator language the inner product of the Hilbert cross norm is \(\langle S,T\rangle_\sigma=\operatorname{Tr}(T^*S)\): both sides equal \(\langle\xi',\xi\rangle\langle\eta,\eta'\rangle\) for \(S=\theta_{\eta,\xi}\) and \(T=\theta_{\eta',\xi'}\).

**Lemma 5.4** (singular value decomposition). Let \(T\in\mathcal F(H,K)\) have rank \(r\). There are orthonormal vectors \(a_1,\ldots,a_r\in H\) and \(b_1,\ldots,b_r\in K\) and numbers \(s_1\ge\cdots\ge s_r>0\) with
\[
T=\sum_{k=1}^rs_k\,\theta_{b_k,a_k},\qquad\text{that is}\qquad T\zeta=\sum_ks_k\langle\zeta,a_k\rangle b_k .
\tag{5.1}
\]
The numbers \(s_k^2\), with multiplicity, are the nonzero eigenvalues of \(T^*T\). We call \(s_1,\ldots,s_r\) the *singular values* of \(T\).

**Proof.** \(T^*\) has finite rank, so \(V=T^*(K)\) is finite-dimensional, and \(V^\perp=\ker T\). The self-adjoint operator \(T^*T\) maps \(V\) into \(V\) and vanishes on \(V^\perp\). Let \(P\) be its restriction to \(V\). An operator on a finite-dimensional space is invertible when it is injective, so the spectrum of \(P\) is its finite set of eigenvalues, which are real and at least \(0\) because \(\langle P\zeta,\zeta\rangle=\|T\zeta\|^2\). For each point \(t\) of the spectrum, the function equal to \(1\) at \(t\) and \(0\) at the other points is continuous on the spectrum. The continuous functional calculus turns these functions into mutually orthogonal projections \(p_t\) with \(\sum_tp_t=1_V\) and \(P=\sum_ttp_t\). Choose an orthonormal basis of each range \(p_tV\), list the basis vectors with \(t>0\) as \(a_1,\ldots,a_r\) in decreasing order of \(t\), and put \(s_k=\sqrt t\) and \(b_k=Ta_k/s_k\). Then \(\langle b_k,b_l\rangle=\langle T^*Ta_k,a_l\rangle/(s_ks_l)=\delta_{kl}\). The remaining basis vectors of \(V\), and all of \(V^\perp\), are killed by \(T\) (for \(t=0\), \(\|Ta\|^2=\langle Pa,a\rangle=0\)). Expanding \(\zeta\) in the orthonormal basis of \(V\) plus its component in \(V^\perp\) gives (5.1). From (5.1), \(T^*T=\sum_ks_k^2\theta_{a_k,a_k}\), so the \(s_k^2\) are its nonzero eigenvalues, and \(r\) is the rank of \(T\). \(\square\)

**Theorem 5.5** (the three norms on finite-rank operators). Let \(T\in\mathcal F(H,K)\) have singular values \(s_1\ge\cdots\ge s_r>0\). Then
\[
\lambda(T)=\|T\|=s_1,\qquad \sigma(T)=\Big(\sum_ks_k^2\Big)^{1/2}=\Big(\sum_i\|Te_i\|^2\Big)^{1/2},\qquad \gamma(T)=\sum_ks_k,
\tag{5.2}
\]
for every orthonormal basis \((e_i)\) of \(H\) (with \(s_1=0\) and empty sums if \(T=0\)). Moreover \(\gamma(T)=\sup\{|\operatorname{Tr}(RT)|:\ R\in B(K,H),\ \|R\|\le1\}\), and the supremum is attained at an operator \(R\) of finite rank. In particular \(\lambda\le\sigma\le\gamma\), and \(\sigma\) is a reasonable cross norm.

**Proof.** Use (5.1). For \(\lambda\): \(\|T\zeta\|^2=\sum_ks_k^2|\langle\zeta,a_k\rangle|^2\le s_1^2\|\zeta\|^2\), with equality at \(\zeta=a_1\). For \(\sigma\): the elements \(\bar a_k\otimes b_k\) are orthonormal in \(\overline H\odot K\), and \(T=\sum_ks_k\,\bar a_k\otimes b_k\), so \(\sigma(T)^2=\sum_ks_k^2\). Also \(\sum_i\|Te_i\|^2=\sum_i\sum_ks_k^2|\langle e_i,a_k\rangle|^2=\sum_ks_k^2\|a_k\|^2\) by Parseval's identity.

For \(\gamma\): by the Hahn–Banach theorem, \(\gamma(T)\) is the supremum of \(|\varphi(T)|\) over the functionals \(\varphi\) of norm at most one on \(\overline H\otimes_\gamma K\). By Theorem 4.1(2), with \(\overline H^{\,*}=H\), these are the functionals \(\varphi(\bar\xi\otimes\eta)=\langle R\eta,\xi\rangle\) with \(R\in B(K,H)\) and \(\|R\|=\|\varphi\|\le1\). Since \(\langle R\eta,\xi\rangle=\operatorname{Tr}(R\theta_{\eta,\xi})\), this functional is \(T\mapsto\operatorname{Tr}(RT)\). This proves the formula for \(\gamma(T)\) as a supremum. The representation (5.1) gives \(\gamma(T)\le\sum_ks_k\). For \(R_0=\sum_k\theta_{a_k,b_k}\), which maps each \(b_k\) to \(a_k\) and kills the orthogonal complement of the \(b_k\), we have \(\|R_0\|\le1\) and
\[
\operatorname{Tr}(R_0T)=\sum_{k,l}s_l\operatorname{Tr}(\theta_{a_k,b_k}\theta_{b_l,a_l})=\sum_{k,l}s_l\langle b_l,b_k\rangle\operatorname{Tr}\theta_{a_k,a_l}=\sum_ks_k .
\]
So \(\gamma(T)=\sum_ks_k\). The inequalities \(s_1\le(\sum s_k^2)^{1/2}\le\sum s_k\) give \(\lambda\le\sigma\le\gamma\), and Theorem 3.3 shows that \(\sigma\) is reasonable. \(\square\)

For the identity \(\iota_n\) of \(\mathbb C^n\), all \(n\) singular values equal \(1\), so \(\lambda(\iota_n)=1\), \(\sigma(\iota_n)=\sqrt n\) and \(\gamma(\iota_n)=n\). The three norms are different as soon as \(n\ge2\).

## 6. Compact, Hilbert–Schmidt and trace-class operators

**Definition 6.1.** An operator \(T\in B(H,K)\) is *compact* if the image of the unit ball of \(H\) is totally bounded. \(\mathcal K(H,K)\) is the set of compact operators.

**Lemma 6.2.** \(\mathcal K(H,K)\) is the closure of \(\mathcal F(H,K)\) in the operator norm. More precisely, if \(T\) is compact and \(Q\) runs through the net of orthogonal projections of finite rank on \(K\), ordered by inclusion of ranges, then \(\|T-QT\|\to0\).

**Proof.** An operator of finite rank maps the unit ball onto a bounded subset of a finite-dimensional space, which is totally bounded. If \(\|T-T_n\|\to0\) with \(T_n\) compact, and \(\varepsilon>0\), choose \(n\) with \(\|T-T_n\|<\varepsilon/3\) and cover the image of the unit ball under \(T_n\) by finitely many balls of radius \(\varepsilon/3\). The balls with the same centres and radius \(\varepsilon\) cover its image under \(T\). So the compact operators form a closed set containing \(\mathcal F(H,K)\). Conversely, let \(T\) be compact and \(\varepsilon>0\). Cover the image of the unit ball by balls of radius \(\varepsilon\) around \(y_1,\ldots,y_m\), and let \(Q_0\) be the projection onto the span of the \(y_j\). If \(Q\ge Q_0\) and \(\|\zeta\|\le1\), pick \(j\) with \(\|T\zeta-y_j\|<\varepsilon\). As \((1-Q)y_j=0\), \(\|(1-Q)T\zeta\|=\|(1-Q)(T\zeta-y_j)\|<\varepsilon\). \(\square\)

**Theorem 6.3** (the three completions).

1. The identification \(\bar\xi\otimes\eta\mapsto\theta_{\eta,\xi}\) extends to an isometry of \(\overline H\hat\otimes_\lambda K\) onto \(\mathcal K(H,K)\) with the operator norm.
2. It extends to a unitary map of the Hilbert space \(\overline H\otimes K\) onto the space \(\mathcal S_2(H,K)\) of *Hilbert–Schmidt operators*: the operators \(T\in B(H,K)\) with \(\sum_i\|Te_i\|^2<\infty\) for an orthonormal basis \((e_i)\) of \(H\), normed by \(\|T\|_2=(\sum_i\|Te_i\|^2)^{1/2}\). This sum does not depend on the basis, \(\|T^*\|_2=\|T\|_2\), \(\|T\|\le\|T\|_2\), and \(\mathcal S_2(H,K)\subseteq\mathcal K(H,K)\).
3. For a positive operator \(P\in B(H)\) put \(\operatorname{Tr}P=\sum_i\langle Pe_i,e_i\rangle\in[0,\infty]\). This does not depend on the orthonormal basis, and \(T\in B(H,K)\) is a Hilbert–Schmidt operator if and only if \(\operatorname{Tr}(T^*T)<\infty\), equivalently \(\operatorname{Tr}(TT^*)<\infty\). Then \(\|T\|_2^2=\operatorname{Tr}(T^*T)=\operatorname{Tr}(TT^*)\).
4. The continuous extension \(\overline H\hat\otimes_\gamma K\to B(H,K)\) of the identification is injective. Its image \(\mathcal S_1(H,K)\) is the space of *trace-class operators*, normed by \(\|T\|_1=\gamma(u)\) for the \(u\) that maps to \(T\). Then \(\|T\|\le\|T\|_2\le\|T\|_1\). If \(\sum_n\|\xi_n\|\|\eta_n\|<\infty\), the series \(\sum_n\theta_{\eta_n,\xi_n}\) converges in norm to an element of \(\mathcal S_1(H,K)\) with \(\|\cdot\|_1\) at most \(\sum_n\|\xi_n\|\|\eta_n\|\).
5. If \(S\in\mathcal S_2(H,K)\) and \(U\in\mathcal S_2(K,L)\), then \(US\in\mathcal S_1(H,L)\) and \(\|US\|_1\le\|U\|_2\|S\|_2\). If \(T\in\mathcal S_1(H,K)\), \(A\in B(K,L)\) and \(B\in B(G,H)\) for Hilbert spaces \(G,L\), then \(\|ATB\|_1\le\|A\|\|T\|_1\|B\|\).
6. The trace extends continuously to \(\mathcal S_1(H)\), with \(|\operatorname{Tr}T|\le\|T\|_1\) and \(\operatorname{Tr}T=\sum_i\langle Te_i,e_i\rangle\), absolutely convergent, for every orthonormal basis. For \(T\in\mathcal S_1(H,K)\) and \(R\in B(K,H)\), \(\operatorname{Tr}(RT)=\operatorname{Tr}(TR)\).

**Proof.** (1) By Theorem 2.3(1), the completion for \(\lambda\) is isometric to the norm closure of \(\mathcal F(H,K)\), which is \(\mathcal K(H,K)\) by Lemma 6.2.

(2) Since \(\lambda\le\sigma\), the identification extends to a contraction \(\Phi_\sigma\) from \(\overline H\otimes K\) to \(B(H,K)\). Let \((e_i)\) and \((f_j)\) be orthonormal bases of \(H\) and \(K\). Then \((\bar e_i)\) is an orthonormal basis of \(\overline H\), and the \(\bar e_i\otimes f_j\) form an orthonormal basis of \(\overline H\otimes K\) (see the lesson on spatial tensor products). Write \(u=\sum_{i,j}c_{ij}\,\bar e_i\otimes f_j\) with \(\sum|c_{ij}|^2=\sigma(u)^2\). As \(\theta_{f_j,e_i}e_k=\delta_{ik}f_j\), the finite partial sums of \(u\) map \(e_k\) to partial sums of \(\sum_jc_{kj}f_j\), and continuity gives \(\Phi_\sigma(u)e_k=\sum_jc_{kj}f_j\). Hence \(\sum_k\|\Phi_\sigma(u)e_k\|^2=\sigma(u)^2\), so \(\Phi_\sigma\) is isometric. Conversely, if \(\sum_i\|Te_i\|^2<\infty\), put \(c_{ij}=\langle Te_i,f_j\rangle\). These are square-summable, and the corresponding \(u\) has \(\Phi_\sigma(u)e_k=Te_k\) for all \(k\), so \(\Phi_\sigma(u)=T\). This identifies the range with \(\mathcal S_2(H,K)\) and \(\sigma\) with \(\|\cdot\|_2\). Independence of the basis: by Parseval's identity twice, and because a double series of nonnegative terms may be summed in either order,
\[
\sum_i\|Te_i\|^2=\sum_i\sum_j|\langle Te_i,f_j\rangle|^2=\sum_j\sum_i|\langle e_i,T^*f_j\rangle|^2=\sum_j\|T^*f_j\|^2 .
\]
The left side does not depend on \((f_j)\) and the right side does not depend on \((e_i)\), so neither depends on any basis, and \(\|T\|_2=\|T^*\|_2\). For a unit vector \(\zeta\), choose a basis containing \(\zeta\): then \(\|T\zeta\|\le\|T\|_2\). Finally, if \(P_F\) is the projection onto the span of finitely many basis vectors \(e_i\), \(i\in F\), then \(\|T-TP_F\|\le\|T(1-P_F)\|_2=(\sum_{i\notin F}\|Te_i\|^2)^{1/2}\), which tends to \(0\). So \(T\) is a norm limit of operators of finite rank, and it is compact by Lemma 6.2.

(3) For positive \(P\), \(\langle Pe_i,e_i\rangle=\|P^{1/2}e_i\|^2\), where \(P^{1/2}\) is the positive square root. So \(\operatorname{Tr}P=\|P^{1/2}\|_2^2\) (possibly \(\infty\)), which does not depend on the basis by (2). With \(P=T^*T\) we get \(\operatorname{Tr}(T^*T)=\sum_i\|Te_i\|^2=\|T\|_2^2\), and with \(P=TT^*\) and \(\|T^*\|_2=\|T\|_2\) the last claim follows.

(4) Since \(\lambda\le\gamma\), the identification extends to a contraction \(\Phi_\gamma\) on \(\overline H\hat\otimes_\gamma K\). For projections \(P\) on \(H\) and \(Q\) on \(K\) of finite rank, let \(\bar P\) be the operator \(\bar\xi\mapsto\overline{P\xi}\) on \(\overline H\), a contraction. By Proposition 2.4, \(\bar P\otimes Q\) extends to a contraction of \(\overline H\hat\otimes_\gamma K\). Its range lies in the finite-dimensional, hence closed, subspace \(\overline{PH}\odot QK\) of \(\overline H\odot K\). On elementary tensors \(\theta_{Q\eta,P\xi}=Q\theta_{\eta,\xi}P\), so by continuity \(\Phi_\gamma((\bar P\otimes Q)u)=Q\,\Phi_\gamma(u)\,P\) for all \(u\). Now suppose \(\Phi_\gamma(u)=0\). Then the element \((\bar P\otimes Q)u\) of \(\overline H\odot K\) corresponds to the zero operator, so it is \(0\) by Proposition 1.2. On the other hand \((\bar P\otimes Q)u\to u\) as \(P\) and \(Q\) increase: if \(u_0\in\overline H\odot K\) has \(\gamma(u-u_0)<\varepsilon\), then \((\bar P\otimes Q)u_0=u_0\) as soon as the ranges of \(P\) and \(Q\) contain the vectors of a representation of \(u_0\), and then \(\gamma((\bar P\otimes Q)u-u)\le\gamma((\bar P\otimes Q)(u-u_0))+\gamma(u_0-u)<2\varepsilon\). Hence \(u=0\), and \(\Phi_\gamma\) is injective. The identity map of \(\overline H\odot K\) is a contraction from \(\gamma\) to \(\sigma\), so it extends to a contraction \(\iota:\overline H\hat\otimes_\gamma K\to\overline H\otimes K\) with \(\Phi_\sigma\circ\iota=\Phi_\gamma\). This gives \(\|T\|_2\le\|T\|_1\), and \(\|T\|\le\|T\|_2\) is in (2). For the series, the partial sums of \(\sum_n\bar\xi_n\otimes\eta_n\) form a Cauchy sequence for \(\gamma\), and its limit maps to the norm limit of the partial sums of \(\sum_n\theta_{\eta_n,\xi_n}\), because \(\Phi_\gamma\) is continuous.

(5) Let \((g_j)\) be an orthonormal basis of \(K\). For \(\zeta\in H\), \(US\zeta=\sum_j\langle S\zeta,g_j\rangle Ug_j=\sum_j\theta_{Ug_j,S^*g_j}\zeta\). By the Cauchy–Schwarz inequality, \(\sum_j\|S^*g_j\|\|Ug_j\|\le\|S^*\|_2\|U\|_2=\|S\|_2\|U\|_2\). By (4), the series \(\sum_j\theta_{Ug_j,S^*g_j}\) converges in norm to an element of \(\mathcal S_1(H,L)\) of trace-class norm at most \(\|U\|_2\|S\|_2\). A norm limit is also a strong limit, and the partial sums converge strongly to \(US\). So this element is \(US\). For the second claim, \(ATB\) corresponds to \((\overline{B^*}\otimes A)u\), where \(\overline{B^*}:\overline H\to\overline G\) is \(\bar\xi\mapsto\overline{B^*\xi}\), because \(A\theta_{\eta,\xi}B=\theta_{A\eta,B^*\xi}\). Apply Proposition 2.4.

(6) By Lemma 5.3, \(\operatorname{Tr}\) is bounded by \(\gamma\) on \(\mathcal F(H)\), so it extends continuously to \(\mathcal S_1(H)\). Write \(T\in\mathcal S_1(H)\) as the image of a limit of partial sums, \(T=\sum_n\theta_{\eta_n,\xi_n}\) with \(\sum_n\|\xi_n\|\|\eta_n\|<\infty\): take \(u_m\in\overline H\odot H\) with \(\gamma(u-u_m)<2^{-m}\) and join representations of \(u_1\) and of the differences \(u_{m+1}-u_m\), each with total cost at most \(\gamma(u_{m+1}-u_m)+2^{-m}\). Then \(\operatorname{Tr}T=\sum_n\langle\eta_n,\xi_n\rangle\) by continuity. For an orthonormal basis \((e_i)\), \(\sum_i\sum_n|\langle e_i,\xi_n\rangle||\langle\eta_n,e_i\rangle|\le\sum_n\|\xi_n\|\|\eta_n\|\), so the double series converges absolutely and may be summed in either order. Summing over \(i\) first gives \(\sum_n\langle\eta_n,\xi_n\rangle\) by Parseval's identity, and summing over \(n\) first gives \(\sum_i\langle Te_i,e_i\rangle\). Finally, \(T\mapsto\operatorname{Tr}(RT)\) and \(T\mapsto\operatorname{Tr}(TR)\) are continuous on \(\mathcal S_1(H,K)\) by (5), and they agree on \(\mathcal F(H,K)\) by Lemma 5.3. \(\square\)

Every trace-class operator is thus a norm-convergent sum \(\sum_n\theta_{\eta_n,\xi_n}\) with \(\sum_n\|\xi_n\|\|\eta_n\|<\infty\). Running the construction in the proof of (6) with a representation of \(u_1\) of cost at most \(\gamma(u)+\varepsilon\) and with the tolerances \(\varepsilon2^{-m}\) shows that \(\|T\|_1\) is the infimum of \(\sum_n\|\xi_n\|\|\eta_n\|\) over such representations. The inclusions \(\mathcal S_1\subseteq\mathcal S_2\subseteq\mathcal K\subseteq B\) are strict when \(H\) and \(K\) are infinite-dimensional. Exercise 2 shows this for \(H=K=\ell^2(\mathbb N)\). The same argument works in general, with orthonormal sequences \((\delta_k)\) in \(H\) and \((\delta'_k)\) in \(K\), the operators \(\sum_kc_k\theta_{\delta'_k,\delta_k}\) in place of \(D_c\), and a partial isometry in place of the unitary \(W\).

## 7. Trace duality

**Lemma 7.1** (polar decomposition). Let \(R\in B(K,H)\) and \(|R|=(R^*R)^{1/2}\in B(K)\), the positive square root. There is \(V\in B(K,H)\) with \(\|V\|\le1\), \(R=V|R|\) and \(V^*R=|R|\).

**Proof.** \(\||R|\kappa\|^2=\langle R^*R\kappa,\kappa\rangle=\|R\kappa\|^2\). So \(|R|\kappa\mapsto R\kappa\) is a well-defined isometry on the range of \(|R|\). It extends to an isometry on the closure \(M\) of that range. Put \(V=0\) on \(M^\perp\). Then \(\|V\|\le1\) and \(V|R|=R\). For \(\kappa\in K\) and \(x=m+m'\) with \(m\in M\), \(m'\in M^\perp\), write \(m=\lim_n|R|\kappa_n\). Then \(\langle V^*R\kappa,x\rangle=\langle V|R|\kappa,Vm\rangle=\lim_n\langle V|R|\kappa,V|R|\kappa_n\rangle=\lim_n\langle|R|\kappa,|R|\kappa_n\rangle=\langle|R|\kappa,x\rangle\), since \(|R|\kappa\perp m'\). So \(V^*R=|R|\). \(\square\)

**Theorem 7.2** (trace duality).

1. The map \(R\mapsto\psi_R\), \(\psi_R(T)=\operatorname{Tr}(RT)\) for \(T\in\mathcal K(H,K)\), is an isometric linear bijection of \(\mathcal S_1(K,H)\) onto \(\mathcal K(H,K)^*\). In tensor language: \((\overline H\hat\otimes_\lambda K)^*=H\hat\otimes_\gamma\overline K\) through the canonical pairing \(\langle\bar\xi\otimes\eta,\zeta\otimes\bar\omega\rangle=\langle\zeta,\xi\rangle\langle\eta,\omega\rangle\).
2. The map \(R\mapsto(T\mapsto\operatorname{Tr}(RT))\) is an isometric linear bijection of \(B(K,H)\) onto \(\mathcal S_1(H,K)^*\).
3. The map \(R\mapsto(T\mapsto\operatorname{Tr}(RT))\) is an isometric linear bijection of \(\mathcal S_2(K,H)\) onto \(\mathcal S_2(H,K)^*\). So the Hilbert cross norm is its own dual: \(\sigma^*=\sigma\).
4. For \(H=K\): the dual of \(\mathcal K(H)\) is \(\mathcal S_1(H)\), and the dual of \(\mathcal S_1(H)\) is \(B(H)\). So the bidual of \(\mathcal K(H)\) is \(B(H)\), and the canonical embedding of \(\mathcal K(H)\) into its bidual is the inclusion \(\mathcal K(H)\subseteq B(H)\).

**Proof.** (1) *Isometry.* Let \(R\in\mathcal F(K,H)\). By Theorem 5.5, applied to \(R\) with the roles of \(H\) and \(K\) exchanged, and by \(\operatorname{Tr}(TR)=\operatorname{Tr}(RT)\), the norm \(\|R\|_1=\gamma(R)\) is the supremum of \(|\operatorname{Tr}(RT)|\) over \(T\in B(H,K)\) with \(\|T\|\le1\), attained at an operator of finite rank. So \(\|\psi_R\|=\|R\|_1\), where \(\psi_R\) is regarded as a functional on \(\mathcal K(H,K)\). Both sides are continuous in \(R\) for \(\|\cdot\|_1\), because \(|\operatorname{Tr}(RT)|\le\|R\|_1\|T\|\) by Theorem 6.3(5)–(6). As \(\mathcal F(K,H)\) is dense in \(\mathcal S_1(K,H)\), the map \(R\mapsto\psi_R\) is isometric on all of \(\mathcal S_1(K,H)\).

*Surjectivity.* Let \(\psi\in\mathcal K(H,K)^*\). The form \((\eta,\xi)\mapsto\psi(\theta_{\eta,\xi})\) on \(K\times H\) is linear in \(\eta\), conjugate-linear in \(\xi\), and bounded by \(\|\psi\|\|\eta\|\|\xi\|\). By the Riesz theorem, applied for each fixed \(\eta\), there is \(R\in B(K,H)\) with \(\psi(\theta_{\eta,\xi})=\langle R\eta,\xi\rangle=\operatorname{Tr}(R\theta_{\eta,\xi})\) and \(\|R\|\le\|\psi\|\). So \(\psi(T)=\operatorname{Tr}(RT)\) for \(T\) of finite rank. We show that \(R\) is of trace class with \(\|R\|_1\le\|\psi\|\). Take \(V\) from Lemma 7.1. For a finite orthonormal family \(g_1,\ldots,g_m\) in \(K\),
\[
\sum_k\langle|R|g_k,g_k\rangle=\sum_k\langle V^*Rg_k,g_k\rangle=\sum_k\langle Rg_k,Vg_k\rangle=\psi\Big(\sum_k\theta_{g_k,Vg_k}\Big).
\]
The operator \(T_0=\sum_k\theta_{g_k,Vg_k}\) sends \(\zeta\) to \(\sum_k\langle V^*\zeta,g_k\rangle g_k\), the projection of \(V^*\zeta\) onto the span of the \(g_k\), so \(\|T_0\|\le1\). Hence \(\sum_k\langle|R|g_k,g_k\rangle\le\|\psi\|\), and taking finite subfamilies of an orthonormal basis gives \(\operatorname{Tr}|R|\le\|\psi\|\). Put \(S=|R|^{1/2}\). By Theorem 6.3(3), \(S\in\mathcal S_2(K)\) with \(\|S\|_2^2=\operatorname{Tr}|R|\). Also \(VS\in\mathcal S_2(K,H)\) with \(\|VS\|_2\le\|S\|_2\), since \(\|VSg\|\le\|Sg\|\). Now \(R=V|R|=(VS)S\), so by Theorem 6.3(5), \(R\in\mathcal S_1(K,H)\) with \(\|R\|_1\le\|S\|_2^2\le\|\psi\|\). The functionals \(\psi\) and \(\psi_R\) are continuous and agree on the dense subspace \(\mathcal F(H,K)\), so \(\psi=\psi_R\).

*Tensor form.* Under the identifications of Section 5, \(\zeta\otimes\bar\omega\in H\odot\overline K\) corresponds to \(\theta_{\zeta,\omega}\in\mathcal F(K,H)\), and \(\operatorname{Tr}(\theta_{\zeta,\omega}\theta_{\eta,\xi})=\langle\eta,\omega\rangle\operatorname{Tr}\theta_{\zeta,\xi}=\langle\eta,\omega\rangle\langle\zeta,\xi\rangle\). This is the canonical pairing of \(E\odot F\) with \(E^*\odot F^*\) for \(E=\overline H\) and \(F=K\).

(2) This is Theorem 4.1(2) for \(E=\overline H\), \(F=K\) and \(\overline H^{\,*}=H\): the functional of \(R\in B(K,H)\) takes the value \(\langle R\eta,\xi\rangle=\operatorname{Tr}(R\theta_{\eta,\xi})\) at \(\bar\xi\otimes\eta\), hence \(\operatorname{Tr}(RT)\) at every \(T\in\mathcal S_1(H,K)\) by continuity.

(3) \(\mathcal S_2(H,K)\) is a Hilbert space with \(\langle S,T\rangle=\operatorname{Tr}(T^*S)\), the inner product of \(\overline H\otimes K\) (Section 5 and continuity). So \(\operatorname{Tr}(RT)=\langle T,R^*\rangle\), and \(R\mapsto R^*\) is a conjugate-linear isometry of \(\mathcal S_2(K,H)\) onto \(\mathcal S_2(H,K)\) by Theorem 6.3(2). The Riesz theorem finishes the proof.

(4) Combine (1) and (2) with \(H=K\). For \(T\in\mathcal K(H)\), the canonical image of \(T\) in the bidual is the functional \(R\mapsto\psi_R(T)=\operatorname{Tr}(RT)\) on \(\mathcal S_1(H)\). Since \(\operatorname{Tr}(RT)=\operatorname{Tr}(TR)\) by Theorem 6.3(6), this is the functional that (2) assigns to \(T\in B(H)\). \(\square\)

## 8. Jordan homomorphisms

**Definition 8.1.** Let \(A\) and \(B\) be \(C^*\)-algebras. A linear map \(\pi:A\to B\) is a *Jordan \(*\)-homomorphism* if \(\pi(x^*)=\pi(x)^*\) for all \(x\) and \(\pi(h^2)=\pi(h)^2\) for all \(h\in A_h\). A bijective Jordan \(*\)-homomorphism is a *Jordan \(*\)-isomorphism*. A *\(*\)-antihomomorphism* is a linear map with \(\pi(x^*)=\pi(x)^*\) and \(\pi(xy)=\pi(y)\pi(x)\).

The inverse of a Jordan \(*\)-isomorphism is again one. For \(y\in B\), \(\pi(\pi^{-1}(y)^*)=y^*\), so \(\pi^{-1}(y^*)=\pi^{-1}(y)^*\). In particular \(h=\pi^{-1}(k)\) is self-adjoint for \(k\in B_h\), and \(\pi(h^2)=k^2\) gives \(\pi^{-1}(k^2)=\pi^{-1}(k)^2\).

**Lemma 8.2** (basic identities). Let \(\pi:A\to B\) be a Jordan \(*\)-homomorphism and \(x,y,z\in A\).

1. \(\pi(x\circ y)=\pi(x)\circ\pi(y)\) and \(\pi(x^2)=\pi(x)^2\).
2. \(\pi(xyx)=\pi(x)\pi(y)\pi(x)\) and \(\pi(xyz+zyx)=\pi(x)\pi(y)\pi(z)+\pi(z)\pi(y)\pi(x)\).
3. \(\pi([[x,y],z])=[[\pi(x),\pi(y)],\pi(z)]\) and \(\pi([x,y]^2)=[\pi(x),\pi(y)]^2\).
4. \(\pi\) is positive, \(\|\pi(h)\|\le\|h\|\) for \(h\in A_h\), and \(\|\pi(x)\|\le2\|x\|\) for all \(x\). If \(A\) has a unit, \(\pi(1)\) is a projection and \(\pi(x)=\pi(1)\pi(x)\pi(1)\).
5. \(\pi\) maps projections to projections, and mutually orthogonal projections to mutually orthogonal projections.

**Proof.** (1) For \(h,k\in A_h\), \(h\circ k=(h+k)^2-h^2-k^2\), so \(\pi(h\circ k)=\pi(h)\circ\pi(k)\). Both sides of the first identity are bilinear in \((x,y)\), and every element is \(h+ik\) with \(h,k\in A_h\). Then \(2\pi(x^2)=\pi(x\circ x)=2\pi(x)^2\).

(2) Expanding gives \(x\circ(x\circ y)-x^2\circ y=2xyx\), and (1) turns the left side into the same expression in \(\pi(x),\pi(y)\). Replacing \(x\) by \(x+z\) and subtracting the identities for \(x\) and for \(z\) gives the second formula.

(3) \([[x,y],z]=(xyz+zyx)-(yxz+zxy)\) and \([x,y]^2=x\circ(yxy)-xy^2x-yx^2y\). Apply (1) and (2) to each term.

(4) A positive \(a\) is the square of the self-adjoint \(a^{1/2}\), so \(\pi(a)=\pi(a^{1/2})^2\ge0\). Suppose first that \(A\) has a unit. Then \(\pi(1)=\pi(1^2)=\pi(1)^2\) is a self-adjoint idempotent, a projection, and (2) with \(x=1\) gives \(\pi(y)=\pi(1)\pi(y)\pi(1)\). For \(h\in A_h\), \(\|h\|1\pm h\ge0\), so \(-\|h\|\pi(1)\le\pi(h)\le\|h\|\pi(1)\), and \(\|\pi(h)\|\le\|h\|\) because \(\pi(1)\le1\) (in the unitization of \(B\) if \(B\) has no unit). If \(A\) has no unit, extend \(\pi\) to the unitization by \(\tilde\pi(a+c1)=\pi(a)+c1\). This is a Jordan \(*\)-homomorphism: for \(h\in A_h\) and real \(t\), \(\tilde\pi((h+t)^2)=\pi(h)^2+2t\pi(h)+t^2=\tilde\pi(h+t)^2\). Apply the unital case, using that the norm of \(A\) is the restriction of the norm of its unitization. Finally \(x=h+ik\) with \(\|h\|,\|k\|\le\|x\|\).

(5) If \(p\) is a projection, \(\pi(p)^2=\pi(p^2)=\pi(p)=\pi(p)^*\). If \(p\) and \(q\) are orthogonal projections, then \(p+q\) is a projection, so \(P=\pi(p)\) and \(Q=\pi(q)\) are projections with \(P+Q\) a projection. Then \((P+Q)^2=P+Q\) gives \(PQ+QP=0\). Multiplying by \(P\) on the left and on the right gives \(PQ=-PQP=QP\), so \(2PQ=0\). \(\square\)

**Example 8.3.** 1. Every \(*\)-homomorphism and every \(*\)-antihomomorphism is a Jordan \(*\)-homomorphism, and so is a direct sum \(x\mapsto\pi_1(x)\oplus\pi_2(x)\) of Jordan \(*\)-homomorphisms.

2. The transpose \(t(x)=x^{\mathrm t}\) on \(M_n(\mathbb C)\) is a \(*\)-antiautomorphism, hence a Jordan \(*\)-automorphism. It is isometric: \(x^{\mathrm t}=\overline{x^*}\), where the bar conjugates every entry, and \(\bar x=CxC\) for the conjugate-linear isometry \(C\) of \(\mathbb C^n\) that conjugates coordinates, so \(\|\bar x\|=\|x\|\). For \(n\ge2\) it is not multiplicative: \((E_{12}E_{21})^{\mathrm t}=E_{11}\), while \(E_{12}^{\mathrm t}E_{21}^{\mathrm t}=E_{21}E_{12}=E_{22}\), where \(E_{kl}\) are the matrix units of \(M_n(\mathbb C)\).

3. For \(n\ge2\), \(\pi(x)=x\oplus x^{\mathrm t}\) from \(M_n(\mathbb C)\) into \(M_n(\mathbb C)\oplus M_n(\mathbb C)\) is a Jordan \(*\)-homomorphism that is neither multiplicative nor antimultiplicative: \(\pi(E_{12}E_{21})=E_{11}\oplus E_{11}\), while \(\pi(E_{12})\pi(E_{21})=E_{11}\oplus E_{22}\) and \(\pi(E_{21})\pi(E_{12})=E_{22}\oplus E_{11}\). Exercise 3 splits it for \(n=2\).

**Example 8.4** (the transpose tensored with the identity). Identify \(M_n(\mathbb C)\odot M_n(\mathbb C)\) with \(B(\mathbb C^n\otimes\mathbb C^n)\), where \(a\otimes b\) acts as in the lesson on spatial tensor products. The operator norm is a cross norm there. It lies between \(\lambda\) and \(\gamma\), formed with the operator norm of \(M_n(\mathbb C)\): it is at most \(\gamma\) by Theorem 2.3(3), and at least \(\lambda\) because a product functional \(f\otimes g\) has norm \(\|f\|\|g\|\) on \(B(\mathbb C^n\otimes\mathbb C^n)\) (every functional on \(M_n(\mathbb C)\) is normal, and product functionals of normal functionals have this norm by the lesson on spatial tensor products). So it is a reasonable cross norm. Now let \(F=\sum_{k,l}E_{kl}\otimes E_{lk}\), the unitary that exchanges the two factors, \(F(\xi\otimes\eta)=\eta\otimes\xi\), and let \(\omega=\sum_ke_k\otimes e_k\). Then
\[
(t\otimes\mathrm{id})(F)=\sum_{k,l}E_{lk}\otimes E_{lk}=\theta_{\omega,\omega},
\tag{8.1}
\]
since both sides send \(e_k\otimes e_l\) to \(\delta_{kl}\,\omega\). So \(\|F\|=1\) while \(\|(t\otimes\mathrm{id})(F)\|=\|\omega\|^2=n\). Thus \(\|t\otimes\mathrm{id}\|\ge n\), although \(\|t\|=\|\mathrm{id}\|=1\). For \(\lambda\) and \(\gamma\) this cannot happen, by Proposition 2.4. Also, \((t\otimes\mathrm{id})(\theta_{\omega,\omega})=F\) by (8.1), because \(t\) is its own inverse. For \(n\ge2\), \(\theta_{\omega,\omega}\ge0\) but \(F\) has the eigenvalue \(-1\) at \(e_1\otimes e_2-e_2\otimes e_1\). So \(t\) is positive, but \(t\otimes\mathrm{id}\) is not; in the language of Completely positive maps, \(t\) is not completely positive.

**Proposition 8.5** (commuting elements). Let \(\pi:A\to B\) be a Jordan \(*\)-homomorphism. If \(x,y\in A\) commute, then \(\pi(xy)=\pi(x)\pi(y)=\pi(y)\pi(x)\).

**Proof.** Let \(B_0=C^*(\pi(A))\), and \(c=[\pi(x),\pi(y)]\in B_0\). By Lemma 8.2(3), \([c,\pi(z)]=\pi([[x,y],z])=0\) for every \(z\in A\). So \(c\) commutes with \(\pi(A)\), hence with the \(*\)-algebra it generates, hence with \(B_0\). As \(B_0\) is closed under adjoints, \(c^*\in B_0\), so \(c\) commutes with \(c^*\): \(c\) is normal. Also \(c^2=\pi([x,y]^2)=\pi(0)=0\) by Lemma 8.2(3). For a normal element the norm is the spectral radius, so \(\|c\|^2=\|c^2\|=0\), and \(c=0\). Then \(\pi(xy)=\frac12\pi(x\circ y)=\frac12(\pi(x)\pi(y)+\pi(y)\pi(x))=\pi(x)\pi(y)\). \(\square\)


**Corollary 8.6.** Let \(\pi:A\to B\) be a Jordan \(*\)-homomorphism. If a projection \(p\in A\) commutes with \(x\), then \(\pi(xp)=\pi(x)\pi(p)=\pi(p)\pi(x)\). If \(z\) is a central projection of \(A\), then \(\pi(z)\) is a projection commuting with \(\pi(A)\), and \(\pi(xz)=\pi(x)\pi(z)\) for all \(x\in A\).

**Proof.** Proposition 8.5 and Lemma 8.2(5). \(\square\)

**Remark 8.7** (square identities are not enough). Proposition 8.5 does not follow from the identities of Lemma 8.2 alone: its proof also uses the involution and the norm of \(B\). For linear maps between algebras that preserve squares, it fails. Let \(R\) be the commutative algebra with basis \(1,s,t,st\) and \(s^2=t^2=0\), and let \(\Lambda\) be the exterior algebra of \(\mathbb C^2\), with basis \(1,\epsilon_1,\epsilon_2,\epsilon_1\epsilon_2\), \(\epsilon_k^2=0\) and \(\epsilon_1\epsilon_2=-\epsilon_2\epsilon_1\). The linear map \(\phi\) with \(\phi(1)=1\), \(\phi(s)=\epsilon_1\), \(\phi(t)=\epsilon_2\), \(\phi(st)=0\) satisfies \(\phi(r^2)=\phi(r)^2\) for every \(r\): both sides equal \(c_0^2+2c_0c_1\epsilon_1+2c_0c_2\epsilon_2\) for \(r=c_0+c_1s+c_2t+c_3st\). But \(s\) and \(t\) commute while \(\phi(s)\phi(t)=\epsilon_1\epsilon_2\ne0=\phi(st)\). Here \([\phi(s),\phi(t)]=2\epsilon_1\epsilon_2\) is central and has square zero, as in the proof above, but nothing forces it to vanish. No splitting as in Section 10 exists for \(\phi\) either. The only idempotents of \(\Lambda\) are \(0\) and \(1\), and \(\phi(st)=0\) differs from both \(\phi(s)\phi(t)=\epsilon_1\epsilon_2\) and \(\phi(t)\phi(s)=-\epsilon_1\epsilon_2\).

## 9. Matrix units split a Jordan homomorphism

Let \(A\) be a unital \(C^*\)-algebra. A family \((u_{ij})_{i,j=1}^n\) in \(A\) with \(u_{ij}^*=u_{ji}\), \(u_{ij}u_{kl}=\delta_{jk}u_{il}\) and \(\sum_iu_{ii}=1\) is called a *system of \(n\times n\) matrix units* of \(A\).

**Theorem 9.1.** Let \(A\) be a unital \(C^*\)-algebra with a system \((u_{ij})\) of \(n\times n\) matrix units, \(n\ge2\), and let \(L=\{a\in A:\ au_{ij}=u_{ij}a\text{ for all }i,j\}\). Let \(\pi:A\to B\) be a Jordan \(*\)-homomorphism into a \(C^*\)-algebra \(B\). Put \(P_i=\pi(u_{ii})\) and \(U_{ij}=\pi(u_{ij})\), and for \(i\ne j\)
\[
v_{ij}=P_iU_{ij}P_j,\qquad w_{ij}=P_iU_{ji}P_j .
\tag{9.1}
\]

1. Every \(x\in A\) is \(\sum_{i,j}x_{ij}u_{ij}\) for exactly one family \((x_{ij})\) in \(L\), namely \(x_{ij}=\sum_ku_{ki}xu_{jk}\). Moreover \(\pi(x)=\sum_{i,j}\pi(x_{ij})U_{ij}\), and each \(\pi(a)\), \(a\in L\), commutes with every \(U_{ij}\).
2. \(P_1,\ldots,P_n\) are mutually orthogonal projections with sum \(\pi(1)\). For \(i\ne j\): \(U_{ij}=v_{ij}+w_{ji}\); \(v_{ij}=P_iU_{ij}=U_{ij}P_j\); \(w_{ij}=P_iU_{ji}=U_{ji}P_j\); and \(v_{ij}^*=v_{ji}\), \(w_{ij}^*=w_{ji}\).
3. For distinct \(i,j,k\): \(v_{ij}v_{jk}=v_{ik}\) and \(w_{ij}w_{jk}=w_{ik}\).
4. \(v_{ii}:=v_{ij}v_{ji}\) and \(w_{ii}:=w_{ij}w_{ji}\) are the same for every \(j\ne i\). They are projections, and \(v_{ii}+w_{ii}=P_i\).
5. \((v_{ij})\) and \((w_{ij})\) are systems of \(n\times n\) matrix units with sums \(e=\sum_iv_{ii}\) and \(f=\sum_iw_{ii}\). The projections \(e\) and \(f\) are orthogonal, \(e+f=\pi(1)\), both lie in \(C^*(\pi(A))\), and both commute with \(\pi(A)\).
6. \(\pi(x)e=\sum_{i,j}\pi(x_{ij})v_{ij}\) and \(\pi(x)f=\sum_{i,j}\pi(x_{ij})w_{ji}\). The map \(x\mapsto\pi(x)e\) is a \(*\)-homomorphism and \(x\mapsto\pi(x)f\) is a \(*\)-antihomomorphism of \(A\) into \(B\), and \(\pi(x)=\pi(x)e+\pi(x)f\).

**Proof.** (1) Each \(x_{ij}\) lies in \(L\): \(x_{ij}u_{ab}=\sum_ku_{ki}xu_{jk}u_{ab}=u_{ai}xu_{jb}\), and \(u_{ab}x_{ij}=\sum_ku_{ab}u_{ki}xu_{jk}=u_{ai}xu_{jb}\). Next, \(\sum_{i,j}x_{ij}u_{ij}=\sum_{i,j,k}u_{ki}xu_{jk}u_{ij}=\sum_{i,j}u_{ii}xu_{jj}=x\). If \(\sum_{i,j}y_{ij}u_{ij}=0\) with \(y_{ij}\in L\), then for all \(a,b\), \(0=\sum_ku_{ka}\big(\sum_{i,j}y_{ij}u_{ij}\big)u_{bk}=\sum_ky_{ab}u_{kk}=y_{ab}\). Since \(x_{ij}\) commutes with \(u_{ij}\), Proposition 8.5 gives \(\pi(x_{ij}u_{ij})=\pi(x_{ij})U_{ij}\), and it shows that \(\pi(a)\) commutes with \(U_{ij}\) for \(a\in L\).

(2) The \(u_{ii}\) are mutually orthogonal projections with sum \(1\), so Lemma 8.2(5) gives the first claim. For \(i\ne j\), \(u_{ij}=u_{ii}u_{ij}u_{jj}+u_{jj}u_{ij}u_{ii}\), because the second term is \(0\). Lemma 8.2(2) gives \(U_{ij}=P_iU_{ij}P_j+P_jU_{ij}P_i=v_{ij}+w_{ji}\). Multiplying this identity by \(P_i\) on the left, or by \(P_j\) on the right, and using \(P_iP_j=0\), gives \(P_iU_{ij}=v_{ij}=U_{ij}P_j\). The same identity for the pair \((j,i)\), \(U_{ji}=v_{ji}+w_{ij}\), gives \(P_iU_{ji}=w_{ij}=U_{ji}P_j\). Finally \(U_{ij}^*=\pi(u_{ji})=U_{ji}\), so \(v_{ij}^*=P_jU_{ji}P_i=v_{ji}\) and \(w_{ij}^*=P_jU_{ij}P_i=w_{ji}\).

By (2), \(U_{ab}=P_aU_{ab}P_b+P_bU_{ab}P_a\) for \(a\ne b\), so
\[
P_mU_{ab}=0=U_{ab}P_m\qquad(m\notin\{a,b\}).
\tag{9.2}
\]
We now derive four relations from Lemma 8.2(1), using (2) and (9.2) to rewrite products.

- (R1) For \(i\ne j\): \(v_{ij}w_{ji}=0=w_{ji}v_{ij}\). Indeed \(u_{ij}^2=0\), so \(0=U_{ij}^2=(v_{ij}+w_{ji})^2\). Here \(v_{ij}^2=P_iU_{ij}P_jP_iU_{ij}P_j=0\) and likewise \(w_{ji}^2=0\), so \(v_{ij}w_{ji}+w_{ji}v_{ij}=0\). The first term lies in \(P_iBP_i\) and the second in \(P_jBP_j\), so each is \(0\).
- (R2) For distinct \(i,j,k\): \(v_{ij}v_{jk}=v_{ik}\) and \(w_{ij}w_{jk}=w_{ik}\). Indeed \(u_{ij}\circ u_{jk}=u_{ik}\), so \(U_{ik}=U_{ij}U_{jk}+U_{jk}U_{ij}\). Multiply by \(P_i\) on the left and \(P_k\) on the right. Since \(P_iU_{jk}=0\) by (9.2), what remains is \(v_{ik}=(P_iU_{ij})(U_{jk}P_k)=v_{ij}v_{jk}\). Multiply instead by \(P_k\) on the left and \(P_i\) on the right. Since \(P_kU_{ij}=0\), what remains is \(w_{ki}=(P_kU_{jk})(U_{ij}P_i)=w_{kj}w_{ji}\), which is the second claim with the indices renamed.
- (R3) For \(i\ne j\): \(P_i=v_{ij}v_{ji}+w_{ij}w_{ji}\). Indeed \(u_{ij}\circ u_{ji}=u_{ii}+u_{jj}\), so \(U_{ij}U_{ji}+U_{ji}U_{ij}=P_i+P_j\). Multiply by \(P_i\) on both sides; by (2) the two products become \((P_iU_{ij})(U_{ji}P_i)=v_{ij}v_{ji}\) and \((P_iU_{ji})(U_{ij}P_i)=w_{ij}w_{ji}\).
- (R4) For distinct \(i,j,k\): \(w_{kj}v_{ji}=0\) and \(v_{kj}w_{ji}=0\). Indeed \(u_{jk}\circ u_{ji}=0\), so \(U_{jk}U_{ji}+U_{ji}U_{jk}=0\). Multiply by \(P_k\) on the left and \(P_i\) on the right. As \(P_kU_{ji}=0\), what remains is \((P_kU_{jk})(U_{ji}P_i)=w_{kj}v_{ji}=0\). In the same way \(u_{kj}\circ u_{ij}=0\), and \(P_kU_{ij}=0\) leaves \((P_kU_{kj})(U_{ij}P_i)=v_{kj}w_{ji}=0\).

(3) This is (R2).

(4) Fix \(i\ne j\) and put \(q=v_{ij}v_{ji}=v_{ij}v_{ij}^*\) and \(r=w_{ij}w_{ji}=w_{ij}w_{ij}^*\). Both are positive, and \(q=P_iqP_i\). By (R3), \(q+r=P_i\). By (R1) for the pair \((j,i)\), \(v_{ji}w_{ij}=0\), so \(qr=v_{ij}(v_{ji}w_{ij})w_{ji}=0\). Hence \(q=q(q+r)=q^2\): \(q\) is a projection, and so is \(r=P_i-q\). Now let \(n\ge3\) and \(k\notin\{i,j\}\). By (R3) for the pair \((j,k)\) and by (R4),
\[
v_{ji}=P_jv_{ji}=v_{jk}v_{kj}v_{ji}+w_{jk}(w_{kj}v_{ji})=v_{jk}v_{kj}v_{ji},
\]
and with (R2), \(v_{ik}v_{ki}=v_{ij}(v_{jk}v_{kj}v_{ji})=v_{ij}v_{ji}\). In the same way \(w_{ji}=v_{jk}(v_{kj}w_{ji})+w_{jk}w_{kj}w_{ji}=w_{jk}w_{kj}w_{ji}\), and \(w_{ik}w_{ki}=w_{ij}(w_{jk}w_{kj}w_{ji})=w_{ij}w_{ji}\). So \(v_{ii}\) and \(w_{ii}\) do not depend on \(j\).

(5) We check \(v_{ij}v_{kl}=\delta_{jk}v_{il}\) for all indices. If \(j\ne k\), then \(v_{ij}=v_{ij}P_j\) and \(v_{kl}=P_kv_{kl}\) (also on the diagonal, as \(v_{ii}\le P_i\)), and \(P_jP_k=0\). Let \(j=k\). For distinct \(i,j,l\) this is (R2), and for \(l=i\ne j\) it is the definition of \(v_{ii}\). For \(i=j\ne l\), use \(v_{ii}=v_{il}v_{li}\) from (4), then (R3) and (R1):
\[
v_{ii}v_{il}=(P_i-w_{il}w_{li})v_{il}=v_{il}-w_{il}(w_{li}v_{il})=v_{il}.
\]
For \(j=l\ne i\), \(v_{ij}v_{jj}=(v_{ij}v_{ji})v_{ij}=v_{ii}v_{ij}=v_{ij}\). For \(i=j=l\), \(v_{ii}^2=v_{ii}\). With \(v_{ij}^*=v_{ji}\), this shows that the \(v_{ij}\) are \(n\times n\) matrix units with sum \(e\). The same computation, with (R1) in the form \(v_{li}w_{il}=0\), shows that the \(w_{ij}\) are \(n\times n\) matrix units with sum \(f\). By (4), \(e+f=\sum_iP_i=\pi(1)\). Also \(v_{ii}w_{jj}=0\) for all \(i,j\) (for \(i\ne j\) because \(P_iP_j=0\), for \(i=j\) by (4)), so \(ef=0\). Both \(e\) and \(f\) are sums of products of the \(P_i\) and \(U_{ij}\), so they lie in \(C^*(\pi(A))\).

It remains to show that \(e\) and \(f\) commute with \(\pi(A)\). Clearly \(eP_i=v_{ii}=P_ie\). For \(i\ne j\), by (R1),
\[
eU_{ij}=v_{ii}v_{ij}+v_{jj}w_{ji}=v_{ij}+v_{ji}(v_{ij}w_{ji})=v_{ij},\qquad
U_{ij}e=v_{ij}v_{jj}+w_{ji}v_{ii}=v_{ij}+(w_{ji}v_{ij})v_{ji}=v_{ij}.
\]
So \(e\) commutes with every \(P_i\) and \(U_{ij}\). By Lemma 8.2(4), \(\pi(1)\) commutes with \(\pi(A)\), so \(f=\pi(1)-e\) also commutes with them, and \(fU_{ij}=U_{ij}f=U_{ij}-v_{ij}=w_{ji}\). For \(a\in L\), \(\pi(a)\) commutes with every \(U_{ij}\) by (1), hence with \(e\) and \(f\). By (1) again, \(\pi(x)=\sum_{i,j}\pi(x_{ij})U_{ij}\) commutes with \(e\) and \(f\).

(6) The formulas for \(\pi(x)e\) and \(\pi(x)f\) follow from (1), \(eU_{ij}=v_{ij}\), \(fU_{ij}=w_{ji}\) (\(i\ne j\)), \(eP_i=v_{ii}\) and \(fP_i=w_{ii}\). Let \(a,b\in L\). Since \(b\) commutes with \(u_{12}\) and \(a\) with \(u_{21}\), \((au_{12})\circ(bu_{21})=ab\,u_{11}+ba\,u_{22}\). By Lemma 8.2(1), Proposition 8.5 and (1),
\[
\pi(ab)P_1+\pi(ba)P_2=\pi(a)U_{12}\pi(b)U_{21}+\pi(b)U_{21}\pi(a)U_{12}=\pi(a)\pi(b)U_{12}U_{21}+\pi(b)\pi(a)U_{21}U_{12}.
\tag{9.3}
\]
Now \(U_{12}U_{21}e=U_{12}v_{21}=U_{12}e\,v_{21}=v_{12}v_{21}=v_{11}\), and likewise \(U_{21}U_{12}e=v_{22}\), \(P_1e=v_{11}\) and \(P_2e=v_{22}\). Multiplying (9.3) on the right by \(e\) and then by \(v_{11}\) gives \(\pi(ab)v_{11}=\pi(a)\pi(b)v_{11}\). In the same way \(U_{12}U_{21}f=U_{12}w_{12}=w_{21}w_{12}=w_{22}\) and \(U_{21}U_{12}f=w_{11}\), and multiplying (9.3) on the right by \(f\) and then by \(w_{11}\) gives \(\pi(ab)w_{11}=\pi(b)\pi(a)w_{11}\). The elements \(\pi(a)\), \(\pi(b)\), \(\pi(ab)\) commute with all \(v_{ij}\) and \(w_{ij}\), and \(v_{ii}=v_{i1}v_{11}v_{1i}\), \(w_{ii}=w_{i1}w_{11}w_{1i}\). Summing over \(i\),
\[
\pi(ab)e=\pi(a)\pi(b)e,\qquad\pi(ab)f=\pi(b)\pi(a)f\qquad(a,b\in L).
\tag{9.4}
\]
Now let \(x=\sum x_{ij}u_{ij}\) and \(y=\sum y_{kl}u_{kl}\) as in (1). The coefficients commute with the matrix units, so \(xy=\sum_{i,l}\big(\sum_jx_{ij}y_{jl}\big)u_{il}\). By (9.4) and the relations of the matrix units,
\[
\pi(xy)e=\sum_{i,j,l}\pi(x_{ij})\pi(y_{jl})v_{il}=\Big(\sum_{i,j}\pi(x_{ij})v_{ij}\Big)\Big(\sum_{k,l}\pi(y_{kl})v_{kl}\Big)=\pi(x)e\,\pi(y)e,
\]
\[
\pi(xy)f=\sum_{i,j,l}\pi(y_{jl})\pi(x_{ij})w_{li}=\Big(\sum_{k,l}\pi(y_{kl})w_{lk}\Big)\Big(\sum_{i,j}\pi(x_{ij})w_{ji}\Big)=\pi(y)f\,\pi(x)f .
\]
Finally \(\pi(x^*)e=\pi(x)^*e=(\pi(x)e)^*\), because \(e\) commutes with \(\pi(x)\), and the same holds for \(f\). And \(\pi(x)=\pi(x)\pi(1)=\pi(x)e+\pi(x)f\). \(\square\)

The projections \(e\) and \(f\) need not lie in \(\pi(A)\) itself. For \(\pi(x)=x\oplus x^{\mathrm t}\) on \(M_2(\mathbb C)\), \(e=1\oplus0\) (Exercise 3).

*Remark.* For a Jordan homomorphism \(\pi\) of a von Neumann algebra \(M\) into another, \(e\) and \(f\) need not be central projections in \(\pi(M)\): in that example \(e=1\oplus0\) is not of the form \(x\oplus x^{\mathrm t}\). So we prove that \(e\) and \(f\) lie in \(C^*(\pi(A))\) and commute with \(\pi(A)\).

## 10. The decomposition theorem

Up to a commutative summand, a von Neumann algebra is covered by systems of matrix units.

**Lemma 10.1.** Let \(M\) be a von Neumann algebra. There are mutually orthogonal central projections \(z_1,z_2,z_3,\ldots\) and \(z_\infty\), with sum \(1\), such that \(Mz_1\) is commutative, \(Mz_n\) contains a system of \(n\times n\) matrix units with sum \(z_n\) for each finite \(n\ge2\), and \(Mz_\infty\) contains a system of \(2\times2\) matrix units with sum \(z_\infty\). Some of these projections may be \(0\).

**Proof.** We use the facts on types stated in the background section. Let \(z_{\rm I}\) be the central projection of the type I part. For each nonzero cardinal \(\alpha\) let \(z_\alpha\) be the largest \(\alpha\)-homogeneous central projection of \(Mz_{\rm I}\): \(z_\alpha=\sum_{i\in I_\alpha}e_i\) with mutually orthogonal abelian projections \(e_i\) of central support \(z_\alpha\) and \(|I_\alpha|=\alpha\). These \(z_\alpha\) are mutually orthogonal with sum \(z_{\rm I}\), and the \(e_i\) with \(i\in I_\alpha\) are mutually equivalent. For \(\alpha=1\), \(z_1\) is itself abelian, so \(Mz_1=z_1Mz_1\) is commutative. For finite \(\alpha=n\ge2\), the \(n\) equivalent projections with sum \(z_n\) are the diagonal of a system of \(n\times n\) matrix units of \(Mz_n\). For infinite \(\alpha\), split \(I_\alpha\) into two disjoint sets of cardinality \(\alpha\), and let \(a_\alpha\) be the sum of the \(e_i\) over the first set. A bijection between the two sets pairs equivalent projections, so \(a_\alpha\sim z_\alpha-a_\alpha\) by additivity of equivalence. The summand \(M(1-z_{\rm I})\) has no nonzero abelian projection, so \(1-z_{\rm I}=b+b'\) with orthogonal equivalent projections \(b,b'\). Put \(z_\infty=\sum_{\alpha\ \text{infinite}}z_\alpha+(1-z_{\rm I})\) and \(a=\sum_\alpha a_\alpha+b\). By additivity, \(a\sim z_\infty-a\). If \(v\in M\) has \(v^*v=a\) and \(vv^*=z_\infty-a\), then \(a\), \(z_\infty-a\), \(v\) and \(v^*\) form a system of \(2\times2\) matrix units of \(Mz_\infty\). By construction \(z_1+\sum_{2\le n<\infty}z_n+z_\infty=1\). \(\square\)

**Theorem 10.2** (normal Jordan homomorphisms split). Let \(M\) be a von Neumann algebra, \(N\subseteq B(H)\) a von Neumann algebra and \(\pi:M\to N\) a Jordan \(*\)-homomorphism that is \(\sigma\)-weakly continuous. There is a projection \(e\) in the centre of \(\pi(M)''\) such that \(x\mapsto\pi(x)e\) is a \(*\)-homomorphism and \(x\mapsto\pi(x)(1-e)\) is a \(*\)-antihomomorphism.

**Proof.** Take \(z_1,z_2,\ldots,z_\infty\) from Lemma 10.1, and put \(Q_k=\pi(z_k)\). By Corollary 8.6, the \(Q_k\) are mutually orthogonal projections that commute with \(\pi(M)\), and \(\pi(x)Q_k=\pi(xz_k)\). The finite partial sums of \(\sum_kz_k\) increase to \(1\) strongly, hence \(\sigma\)-weakly, and \(\pi\) is \(\sigma\)-weakly continuous. The partial sums of \(\sum_kQ_k\) increase strongly to their supremum, which is also their \(\sigma\)-weak limit. So \(\sum_kQ_k=\pi(1)\).

For each \(k\), the restriction of \(\pi\) to the unital \(C^*\)-algebra \(Mz_k\) is a Jordan \(*\)-homomorphism with \(z_k\mapsto Q_k\). If \(k=1\), \(Mz_1\) is commutative, so this restriction is a \(*\)-homomorphism by Proposition 8.5; put \(e_1=Q_1\) and \(f_1=0\). If \(k\ge2\), Theorem 9.1, applied with the matrix units of Lemma 10.1, gives orthogonal projections \(e_k,f_k\in C^*(\pi(Mz_k))\) with \(e_k+f_k=Q_k\) that commute with \(\pi(Mz_k)\), such that \(\pi(ab)e_k=\pi(a)\pi(b)e_k\) and \(\pi(ab)f_k=\pi(b)\pi(a)f_k\) for \(a,b\in Mz_k\).

Each \(e_k\) commutes with all of \(\pi(M)\): for \(x\in M\), \(\pi(x)e_k=\pi(x)Q_ke_k=\pi(xz_k)e_k=e_k\pi(xz_k)=e_kQ_k\pi(x)=e_k\pi(x)\). Let \(e=\sum_ke_k\) and \(f=\sum_kf_k\), strong sums of mutually orthogonal projections. Then \(e\) commutes with \(\pi(M)\). It lies in \(\pi(M)''\), because every \(e_k\) does and \(\pi(M)''\) is strongly closed. As \(\pi(M)'=(\pi(M)'')'\), \(e\) is in the centre of \(\pi(M)''\). For \(x,y\in M\), since \(z_k\) is central and \(Q_k\) commutes with \(\pi(y)\),
\[
\pi(xy)e=\sum_k\pi(xz_k\,yz_k)e_k=\sum_k\pi(xz_k)\pi(yz_k)e_k=\sum_k\pi(x)\pi(y)Q_ke_k=\pi(x)\pi(y)e .
\]
In the same way \(\pi(xy)f=\pi(y)\pi(x)f\). Finally \(e+f=\sum_kQ_k=\pi(1)\) and \(\pi(x)=\pi(x)\pi(1)\), so \(\pi(x)(1-e)=\pi(x)f\). Since \(e\) commutes with \(\pi(M)\), both maps preserve adjoints. \(\square\)

**Theorem 10.3** (Jordan homomorphisms split). Let \(A\) be a \(C^*\)-algebra, \(N\subseteq B(H)\) a von Neumann algebra and \(\pi:A\to N\) a Jordan \(*\)-homomorphism. There is a projection \(e\) in the centre of \(\pi(A)''\) such that \(x\mapsto\pi(x)e\) is a \(*\)-homomorphism and \(x\mapsto\pi(x)(1-e)\) is a \(*\)-antihomomorphism. In particular this holds for every Jordan \(*\)-homomorphism from one von Neumann algebra into another, whether or not it is normal.

*Reference:* [Størmer 1965]; for Jordan isomorphisms of von Neumann algebras, Kadison.

**Proof.** By Lemma 8.2(4), \(\pi\) is bounded. Regard \(A^{**}\) as a von Neumann algebra, as in the background section, so that its \(\sigma\)-weak topology is the weak\(^*\) topology \(\sigma(A^{**},A^*)\). For \(\psi\) in the predual \(N_*\), \(\psi\circ\pi\in A^*\), and \(\psi\mapsto\psi\circ\pi\) is a bounded map \(\pi_*:N_*\to A^*\). Its adjoint \(\bar\pi=(\pi_*)^*:A^{**}\to(N_*)^*=N\) is \(\sigma\)-weakly continuous, and \(\bar\pi(j_A(a))=\pi(a)\), since \(\psi(\bar\pi(j_A(a)))=j_A(a)(\psi\circ\pi)=\psi(\pi(a))\) for every \(\psi\in N_*\).

The map \(\bar\pi\) is a Jordan \(*\)-homomorphism. For fixed \(a\in A\), the maps \(X\mapsto\bar\pi(j_A(a)\circ X)\) and \(X\mapsto\pi(a)\circ\bar\pi(X)\) are \(\sigma\)-weakly continuous, because multiplication is separately \(\sigma\)-weakly continuous in \(A^{**}\) and in \(N\). They agree on the dense set \(j_A(A)\) by Lemma 8.2(1), so they agree on \(A^{**}\). Next, for fixed \(X\in A^{**}\), the maps \(Y\mapsto\bar\pi(Y\circ X)\) and \(Y\mapsto\bar\pi(Y)\circ\bar\pi(X)\) are \(\sigma\)-weakly continuous and agree on \(j_A(A)\), so \(\bar\pi(Y\circ X)=\bar\pi(Y)\circ\bar\pi(X)\) for all \(X,Y\). In the same way \(\bar\pi(X^*)=\bar\pi(X)^*\), since both involutions are \(\sigma\)-weakly continuous. Taking \(Y=X\) self-adjoint gives \(\bar\pi(X^2)=\bar\pi(X)^2\).

By Theorem 10.2 there is a projection \(e\) in the centre of \(\bar\pi(A^{**})''\) such that \(X\mapsto\bar\pi(X)e\) is a \(*\)-homomorphism and \(X\mapsto\bar\pi(X)(1-e)\) a \(*\)-antihomomorphism. By continuity and density, \(\pi(A)\subseteq\bar\pi(A^{**})\), and \(\bar\pi(A^{**})\) lies in the \(\sigma\)-weak closure of \(\pi(A)\), which lies in \(\pi(A)''\). Taking bicommutants, \(\bar\pi(A^{**})''=\pi(A)''\). Restricting to \(j_A(A)\) gives the claim. \(\square\)

**Corollary 10.4.**

1. Every Jordan \(*\)-homomorphism \(\pi:A\to B\) of \(C^*\)-algebras is contractive: \(\|\pi(x)\|\le\|x\|\).
2. Let \(\pi\) be a Jordan \(*\)-isomorphism of a von Neumann algebra \(M\) onto a von Neumann algebra \(N\). There is a central projection \(p\) of \(M\) such that \(\pi(p)\) is central in \(N\), \(\pi\) restricts to a \(*\)-isomorphism of \(Mp\) onto \(N\pi(p)\), and \(\pi\) restricts to a \(*\)-anti-isomorphism of \(M(1-p)\) onto \(N(1-\pi(p))\).
3. If in (2) \(M\) is a factor, then \(\pi\) is a \(*\)-isomorphism or a \(*\)-anti-isomorphism, and \(N\) is a factor.

**Proof.** (1) Represent \(B\) faithfully on a Hilbert space \(H\) (background) and apply Theorem 10.3 with \(N=B(H)\). Since \(e\) commutes with \(\pi(x)\), \(\|\pi(x)\|=\max(\|\pi(x)e\|,\|\pi(x)(1-e)\|)\). The map \(x\mapsto\pi(x)e\) is a \(*\)-homomorphism, hence contractive. The map \(x\mapsto\pi(x)(1-e)\) is a \(*\)-homomorphism into the opposite algebra of \(B(H)\), the same Banach space with the product reversed, which is again a \(C^*\)-algebra; so it is contractive too.

(2) By Theorem 10.3, with \(\pi(M)''=N\), there is a central projection \(e\) of \(N\) such that \(x\mapsto\pi(x)e\) is a \(*\)-homomorphism and \(x\mapsto\pi(x)(1-e)\) a \(*\)-antihomomorphism. The inverse \(\pi^{-1}\) is a Jordan \(*\)-isomorphism, so \(p=\pi^{-1}(e)\) is a projection (Lemma 8.2(5)). For \(x\in M\), \(\pi(x)\) commutes with \(e\), so \(x=\pi^{-1}(\pi(x))\) commutes with \(p\) by Proposition 8.5 for \(\pi^{-1}\). Hence \(p\) is central, and \(\pi(xp)=\pi(x)\pi(p)=\pi(x)e\) by Corollary 8.6. So \(\pi\) maps \(Mp\) onto \(\pi(M)e=Ne\), and on \(Mp\) it is the \(*\)-homomorphism \(x\mapsto\pi(x)e\); it is injective because \(\pi\) is. The same argument with \(1-p\) gives the anti-isomorphism.

(3) If \(M\) is a factor, then \(p=0\) or \(p=1\). A \(*\)-isomorphism or \(*\)-anti-isomorphism maps the centre onto the centre, so \(N\) is a factor. \(\square\)

## 11. Isometries of \(C^*\)-algebras

A *state* of a unital \(C^*\)-algebra \(A\) is a positive linear functional \(\omega\) with \(\omega(1)=1\). A state has norm one. Indeed, \(\omega\) is real on self-adjoint elements, since each is a difference of two positive ones, and \(-\|h\|\le h\le\|h\|\) gives \(|\omega(h)|\le\|h\|\) for \(h\in A_h\). For \(x\in A\), choose \(|c|=1\) with \(c\,\omega(x)\ge0\) and put \(h=\frac12(cx+(cx)^*)\). Then \(\omega((cx)^*)=\overline{\omega(cx)}\), so \(|\omega(x)|=\omega(h)\le\|h\|\le\|x\|\).

**Lemma 11.1** (states). Let \(A\) be a unital \(C^*\)-algebra.

1. A linear functional \(\omega\) with \(\|\omega\|=\omega(1)=1\) is a state.
2. For \(h\in A_h\) and \(t\) in the spectrum of \(h\) there is a state \(\omega\) with \(\omega(h)=t\). Hence \(\|h\|=\sup_\omega|\omega(h)|\) over the states, and \(h\ge0\) if and only if \(\omega(h)\ge0\) for every state.
3. If \(\omega(b)\) is real for every state \(\omega\), then \(b\) is self-adjoint. If \(\omega(b)\ge0\) for every state, then \(b\ge0\).

**Proof.** (1) This is the positivity test of Projections and types of von Neumann algebras (Lemma 17.1 there, with the element \(1\)).

(2) The continuous functional calculus identifies \(C^*(1,h)\) with the continuous functions on the spectrum of \(h\), and evaluation at \(t\) is a linear functional on it of norm \(1\) with value \(1\) at \(1\). By the Hahn–Banach theorem it extends to \(\omega\) on \(A\) with \(\|\omega\|=1=\omega(1)\), and \(\omega\) is a state by (1). The norm of \(h\) is the largest \(|t|\) with \(t\) in the spectrum, and \(h\ge0\) exactly when the spectrum lies in \([0,\infty)\). Conversely, \(|\omega(h)|\le\|h\|\) for every state, since states have norm one, and \(\omega(h)\ge0\) for every state when \(h\ge0\).

(3) Write \(b=b_1+ib_2\) with \(b_1,b_2\in A_h\). Then \(\omega(b)=\omega(b_1)+i\omega(b_2)\) with \(\omega(b_1),\omega(b_2)\) real. If \(\omega(b)\) is real for all states, then \(\omega(b_2)=0\) for all states, and \(b_2=0\) by (2). The second claim then follows from (2). \(\square\)

**Lemma 11.2** (extreme points). Let \(A\) be a unital \(C^*\)-algebra.

1. The extreme points of \(S_+=\{x\in A:0\le x\le1\}\) are exactly the projections of \(A\).
2. \(1\) is an extreme point of the unit ball of \(A\).
3. If \(u\ge0\) is an extreme point of the unit ball of \(A\), then \(u=1\).

**Proof.** (1) Let \(p\) be a projection and \(p=\frac12(a+b)\) with \(a,b\in S_+\). Then \((1-p)a(1-p)+(1-p)b(1-p)=2(1-p)p(1-p)=0\), and both terms are positive, so \((1-p)a(1-p)=0\). This says \(\|a^{1/2}(1-p)\|^2=0\), so \(a(1-p)=0\) and \(a=ap=pa\). In the same way \(p(1-a)p+p(1-b)p=2p(1-p)p=0\) gives \((1-a)p=0\), so \(a=ap=p\), and then \(b=p\). Conversely, let \(x\in S_+\) not be a projection, and put \(y=x-x^2\). By the functional calculus, \(y\ge0\), \(y\ne0\), and \(x+y=1-(1-x)^2\) and \(x-y=x^2\) lie in \(S_+\). Since \(x=\frac12\big((x+y)+(x-y)\big)\), \(x\) is not extreme.

(2) Let \(1=\frac12(a+b)\) with \(\|a\|,\|b\|\le1\). For each state \(\omega\), \(1=\frac12(\omega(a)+\omega(b))\) with \(|\omega(a)|,|\omega(b)|\le1\). As \(1\) is an extreme point of the closed unit disc, \(\omega(a)=1\). So \(\omega(a-1)=0\) for every state. By Lemma 11.1(3), \(a-1\) is self-adjoint, and by Lemma 11.1(2) its norm is \(0\). So \(a=1\), and then \(b=1\).

(3) As \(u\in S_+\), which lies in the unit ball, \(u\) is an extreme point of \(S_+\), so it is a projection \(p\) by (1). Now \(p=\frac12\big(1+(2p-1)\big)\), and \(2p-1\) is a self-adjoint unitary, so it lies in the unit ball. Extremality gives \(2p-1=1\), that is \(p=1\). \(\square\)

**Lemma 11.3** (unital contractions are positive). Let \(A\) and \(B\) be unital \(C^*\)-algebras and \(\varphi:A\to B\) linear with \(\varphi(1)=1\) and \(\|\varphi\|\le1\). Then \(\varphi\) is positive and \(\varphi(x^*)=\varphi(x)^*\).

**Proof.** For a state \(\omega\) of \(B\), \(\omega\circ\varphi\) has norm at most one and value \(1\) at \(1\), so it is a state of \(A\) by Lemma 11.1(1). If \(a\ge0\), then \(\omega(\varphi(a))\ge0\) for every state \(\omega\) of \(B\), and \(\varphi(a)\ge0\) by Lemma 11.1(3). Every self-adjoint element is a difference of positive ones, so \(\varphi\) maps \(A_h\) into \(B_h\), and \(\varphi(x^*)=\varphi(x)^*\) follows by writing \(x=h+ik\). \(\square\)

**Proposition 11.4.** Let \(M\) and \(N\) be von Neumann algebras and \(\Phi\) a linear isometry of \(M\) onto \(N\) with \(\Phi(1)=1\). Then \(\Phi\) is a Jordan \(*\)-isomorphism.

**Proof.** \(\Phi^{-1}\) is also a linear isometry that maps \(1\) to \(1\). By Lemma 11.3, \(\Phi\) and \(\Phi^{-1}\) are positive and preserve adjoints. So \(\Phi\) maps \(S_+(M)\) onto \(S_+(N)\): if \(0\le x\le1\), then \(\Phi(x)\ge0\) and \(1-\Phi(x)=\Phi(1-x)\ge0\), and \(\Phi^{-1}\) gives the converse. An affine bijection of one convex set onto another maps extreme points onto extreme points, so by Lemma 11.2(1), \(\Phi\) maps projections onto projections. If \(p\) and \(q\) are orthogonal projections, then \(p+q\) is a projection, so \(\Phi(p)\), \(\Phi(q)\) and their sum are projections, and \(\Phi(p)\Phi(q)=0\) as in the proof of Lemma 8.2(5). For a finite sum \(h=\sum_kt_kp_k\) with real \(t_k\) and mutually orthogonal projections \(p_k\),
\[
\Phi(h^2)=\sum_kt_k^2\Phi(p_k)=\Big(\sum_kt_k\Phi(p_k)\Big)^2=\Phi(h)^2 .
\]
Every self-adjoint element of \(M\) is a norm limit of such sums (background), and \(\Phi\) is norm continuous. So \(\Phi(h^2)=\Phi(h)^2\) for all \(h\in M_h\). \(\square\)

**Theorem 11.5** (Kadison's theorem, unital case). Let \(A\) and \(B\) be unital \(C^*\)-algebras and \(\pi\) a linear isometry of \(A\) onto \(B\) with \(\pi(1)=1\).

1. \(\pi\) is a Jordan \(*\)-isomorphism.
2. There is a central projection \(z\) of the von Neumann algebra \(B^{**}\) such that \(x\mapsto\pi(x)z\) is a \(*\)-homomorphism and \(x\mapsto\pi(x)(1-z)\) is a \(*\)-antihomomorphism of \(A\) into \(B^{**}\). Here \(B\) is regarded as a subalgebra of \(B^{**}\) through \(j_B\).

In general \(z\) cannot be chosen in \(B\) (Example 11.7(4)).

*Reference:* due to Kadison.

**Proof.** (1) The second adjoint \(\pi^{**}:A^{**}\to B^{**}\) is \(\sigma\)-weakly continuous, extends \(\pi\), and has norm one. The second adjoint of \(\pi^{-1}\) is its inverse, of norm one as well. So \(\pi^{**}\) is a linear isometry of \(A^{**}\) onto \(B^{**}\). The unit of \(A^{**}\) is \(j_A(1)\): for \(X\in A^{**}\), \(j_A(1)X\) and \(X\) are \(\sigma\)-weakly continuous in \(X\) and agree on the dense set \(j_A(A)\). Hence \(\pi^{**}(1)=j_B(\pi(1))=1\). By Proposition 11.4, \(\pi^{**}\) is a Jordan \(*\)-isomorphism, and so is its restriction \(\pi\).

(2) \(\pi^{**}\) is a \(\sigma\)-weakly continuous Jordan \(*\)-isomorphism of \(A^{**}\) onto \(B^{**}\). Theorem 10.2 gives a projection \(z\) in the centre of \(\pi^{**}(A^{**})''=B^{**}\) with the stated properties for \(\pi^{**}\). Restrict to \(A\). \(\square\)

**Theorem 11.6** (positive isometries). Let \(A\) and \(B\) be \(C^*\)-algebras, with or without units, and \(\pi\) a positive linear isometry of \(A\) onto \(B\). Then \(\pi\) is a Jordan \(*\)-isomorphism.

**Proof.** As in the proof of Theorem 11.5, \(\pi^{**}\) is a linear isometry of \(A^{**}\) onto \(B^{**}\). It is positive. Indeed, an element \(X\) of \(A^{**}\) is positive exactly when \(X(f)\ge0\) for every positive \(f\in A^*\) (background). For \(X\ge0\) and positive \(g\in B^*\), \((\pi^{**}X)(g)=X(g\circ\pi)\ge0\), because \(g\circ\pi\) is positive. So \(u=\pi^{**}(1)\ge0\). An isometry of \(A^{**}\) onto \(B^{**}\) maps the unit ball onto the unit ball, affinely and bijectively, so it maps extreme points onto extreme points. By Lemma 11.2(2), \(1\) is an extreme point of the unit ball of \(A^{**}\). So \(u\) is a positive extreme point of the unit ball of \(B^{**}\), and \(u=1\) by Lemma 11.2(3). By Proposition 11.4, \(\pi^{**}\) is a Jordan \(*\)-isomorphism, and so is its restriction \(\pi\). \(\square\)

**Example 11.7** (the hypotheses are needed).

1. *Onto.* The map \(\pi(a,b)=(a,\,b,\,\frac12(a+b))\) from \(\mathbb C^2\) to \(\mathbb C^3\), with the maximum norms, is a positive linear isometry with \(\pi(1)=1\). It is not a Jordan homomorphism: \(\pi\big((1,0)^2\big)=(1,0,\frac12)\), but \(\pi(1,0)^2=(1,0,\frac14)\).
2. *Unit or positivity.* If \(u\ne1\) is a unitary of a unital \(C^*\)-algebra \(B\), then \(x\mapsto ux\) is a linear isometry of \(B\) onto \(B\). It is not a Jordan \(*\)-homomorphism, because it sends \(1\) to \(u\), which is not a projection (Lemma 8.2(4)).
3. *Jordan but not multiplicative.* The map \(x\oplus y\mapsto x\oplus y^{\mathrm t}\) of \(M_n(\mathbb C)\oplus M_n(\mathbb C)\) onto itself, \(n\ge2\), is a unital positive isometry. It is neither multiplicative nor antimultiplicative, and \(z=1\oplus0\).
4. *The bidual is needed in Theorem 11.5(2).* Let \(B\) be the \(C^*\)-algebra of bounded sequences \((x_k)\) in \(M_2(\mathbb C)\) that converge to a scalar multiple of \(1\), and \(\pi((x_k))=(x_1,x_2^{\mathrm t},x_3,x_4^{\mathrm t},\ldots)\), the transpose in the even places. Then \(\pi\) is a unital linear isometry of \(B\) onto \(B\). Suppose \(z=(z_k)\in B\) were a projection commuting with \(B\) such that \(x\mapsto\pi(x)z\) is multiplicative and \(x\mapsto\pi(x)(1-z)\) antimultiplicative. \(B\) contains the sequences with a single nonzero term, so each \(z_k\) commutes with \(M_2(\mathbb C)\), and \(z_k\in\{0,1\}\). At an odd place the coordinate of \(\pi(x)\) is \(x_k\); if \(z_k=0\), the identity map of \(M_2(\mathbb C)\) would be antimultiplicative, which it is not. So \(z_k=1\) for odd \(k\). At an even place the coordinate is \(x_k^{\mathrm t}\), and \(z_k=1\) would make the transpose multiplicative; so \(z_k=0\). Then \((z_k)\) does not converge, and \(z\notin B\).

**Theorem 11.8** (Kadison's theorem). Let \(A\) be a unital \(C^*\)-algebra, \(B\) a \(C^*\)-algebra and \(T\) a linear isometry of \(A\) onto \(B\).

1. \(B\) has a unit, \(u=T(1)\) is a unitary of \(B\), and \(J(x)=u^*T(x)\) is a Jordan \(*\)-isomorphism of \(A\) onto \(B\). So \(T(x)=uJ(x)\) for all \(x\in A\).
2. Conversely, for every unital \(C^*\)-algebra \(B\), every unitary \(u\in B\) and every Jordan \(*\)-isomorphism \(J\) of \(A\) onto \(B\), the map \(x\mapsto uJ(x)\) is a linear isometry of \(A\) onto \(B\).

*Reference:* due to Kadison. The proof of (1) below shows first that the functionals that take the value \(1\) at \(u\) on the unit sphere of \(B^*\) separate the points of \(B\), and then that this forces \(u\) to be unitary.

**Proof.** (1) *Step 1: the functionals at \(u\).* Let \(\mathcal D\) be the set of \(f\in B^*\) with \(\|f\|=1=f(u)\). For a state \(\omega\) of \(A\), the functional \(f=\omega\circ T^{-1}\) has \(\|f\|=\|\omega\|=1\), because \(T^{-1}\) maps the unit ball of \(B\) onto that of \(A\), and \(f(u)=\omega(1)=1\); so \(f\in\mathcal D\). Let \(y\in B\) with \(f(y)=0\) for every \(f\in\mathcal D\). Then \(\omega(T^{-1}y)=0\) for every state \(\omega\) of \(A\). Writing \(T^{-1}y=h+ik\) with \(h,k\in A_h\), the real numbers \(\omega(h)\) and \(\omega(k)\) vanish for every state, so \(h=k=0\) by Lemma 11.1(2), and \(y=0\). Thus \(\mathcal D\) separates the points of \(B\).

*Step 2: the form of the functionals at \(u\).* Let \(f\in\mathcal D\). By the polar decomposition of bounded functionals (background (g)) there are a partial isometry \(v\in B^{**}\) and a positive functional \(\omega\) with \(\|\omega\|=\|f\|=1\) and \(f(x)=\omega(xv)\) for \(x\in B^{**}\). Let \((\pi,K,\xi)\) be the GNS representation of \(\omega\), regarded as a positive functional on the unital \(C^*\)-algebra \(B^{**}\) (background (h)), so that \(\omega(y)=\langle\pi(y)\xi,\xi\rangle\), \(\pi(1)=1\) and \(\|\xi\|^2=\omega(1)=1\). With \(\eta=\pi(v)\xi\), we have \(\|\eta\|\le1\) and \(f(x)=\langle\pi(x)\eta,\xi\rangle\) for \(x\in B^{**}\). Now
\[
1=f(u)=\langle\pi(u)\eta,\xi\rangle\le\|\pi(u)\eta\|\,\|\xi\|\le1,
\]
so \(\|\pi(u)\eta\|=1\) and \(\|\pi(u)\eta-\xi\|^2=1+1-2\operatorname{Re}\langle\pi(u)\eta,\xi\rangle=0\), that is \(\pi(u)\eta=\xi\). Hence
\[
f(x)=\langle\pi(x)\eta,\pi(u)\eta\rangle=\langle\pi(u^*x)\eta,\eta\rangle\qquad(x\in B^{**}),
\tag{11.1}
\]
and \(\langle\pi(u^*u)\eta,\eta\rangle=\|\pi(u)\eta\|^2=1\ge\|\eta\|^2\). Since \(0\le\pi(u^*u)\le1\), this gives \(\|\eta\|=1\) and \(\|(1-\pi(u^*u))^{1/2}\eta\|^2=\|\eta\|^2-\langle\pi(u^*u)\eta,\eta\rangle=0\), so \(\pi(u^*u)\eta=\eta\).

*Step 3: \(u\) is a unitary.* Let \(y\in B\). The element \(y-yu^*u\) lies in \(B\), and by (11.1) and \(\pi(u^*u)\eta=\eta\),
\[
f(y-yu^*u)=\langle\pi(u^*y)\eta,\eta\rangle-\langle\pi(u^*y)\pi(u^*u)\eta,\eta\rangle=0
\]
for every \(f\in\mathcal D\). By Step 1, \(y=yu^*u\). Taking adjoints, \(y=u^*uy\) as well. So \(u^*u\) is a unit for \(B\). Now \(u^*uu^*=u^*\), and for \(y\in B\), (11.1) gives \(f(y-uu^*y)=\langle\pi(u^*y-u^*uu^*y)\eta,\eta\rangle=0\) for every \(f\in\mathcal D\). So \(y=uu^*y\) for every \(y\), and \(y=1\) gives \(uu^*=1\). Hence \(u\) is a unitary.

*Step 4.* Left multiplication by the unitary \(u^*\) is a linear isometry of \(B\) onto \(B\): \(\|u^*y\|^2=\|y^*uu^*y\|=\|y\|^2\). So \(J=u^*T\) is a linear isometry of \(A\) onto \(B\) with \(J(1)=u^*u=1\), and it is a Jordan \(*\)-isomorphism by Theorem 11.5(1).

(2) \(J\) and its inverse are Jordan \(*\)-homomorphisms, so both are contractive by Corollary 10.4(1); hence \(J\) is isometric. Left multiplication by \(u\) is isometric, as in Step 4. \(\square\)

By (1), the unit of \(B\) and the unitary \(u\) are determined by \(T\); the map \(J\) need not be multiplicative or antimultiplicative (Example 11.7(3)).

## Exercises

**Exercise 1** (the injective norm is injective). Let \(E_0\subseteq E\) and \(F_0\subseteq F\) be closed subspaces. Show that for \(u\in E_0\odot F_0\), the injective norm computed in \(E_0\odot F_0\) equals the injective norm computed in \(E\odot F\).

*Solution.* A functional in the unit ball of \(E^*\) restricts to one in the unit ball of \(E_0^*\). Conversely, by the Hahn–Banach theorem every functional in the unit ball of \(E_0^*\) is such a restriction. The same holds for \(F\). The number \(\langle u,f\otimes g\rangle\) depends only on the restrictions of \(f\) and \(g\) to \(E_0\) and \(F_0\). So the two suprema in (2.1) run over the same set of numbers.

**Exercise 2** (the three completions differ). Let \(H=\ell^2(\mathbb N)\) with orthonormal basis \((\delta_k)\). For a bounded sequence \(c=(c_k)\) let \(D_c\) be the diagonal operator \(D_c\delta_k=c_k\delta_k\).

(a) Show that \(D_c\) is compact if and only if \(c_k\to0\), Hilbert–Schmidt if and only if \(\sum_k|c_k|^2<\infty\), and of trace class if and only if \(\sum_k|c_k|<\infty\), and that then \(\|D_c\|_1=\sum_k|c_k|\).

(b) Deduce that \(\mathcal S_1(H)\subsetneq\mathcal S_2(H)\subsetneq\mathcal K(H)\subsetneq B(H)\), and that no two of the norms \(\lambda\), \(\sigma\), \(\gamma\) on \(\overline H\odot H\) are equivalent.

*Solution.* (a) If \(c_k\to0\), let \(c^{(m)}\) keep the first \(m\) terms of \(c\) and replace the others by \(0\). Then \(D_{c^{(m)}}\) has finite rank and \(\|D_c-D_{c^{(m)}}\|=\sup_{k>m}|c_k|\to0\), so \(D_c\) is compact by Lemma 6.2. If \(c_k\not\to0\), there are \(\varepsilon>0\) and infinitely many \(k\) with \(|c_k|\ge\varepsilon\). For two such indices, \(\|c_k\delta_k-c_l\delta_l\|\ge\sqrt2\,\varepsilon\), so the image of the unit ball is not totally bounded. The Hilbert–Schmidt criterion is Theorem 6.3(2): \(\sum_k\|D_c\delta_k\|^2=\sum_k|c_k|^2\). If \(\sum_k|c_k|<\infty\), then \(D_c=\sum_kc_k\theta_{\delta_k,\delta_k}\) with \(\sum_k|c_k|\|\delta_k\|^2<\infty\), so \(D_c\in\mathcal S_1(H)\) with \(\|D_c\|_1\le\sum_k|c_k|\) by Theorem 6.3(4). Conversely, let \(D_c\in\mathcal S_1(H)\), and let \(W\) be the diagonal unitary with entries \(\overline{c_k}/|c_k|\) (and \(1\) where \(c_k=0\)). Then \(WD_c=D_{|c|}\) is of trace class with \(\|WD_c\|_1\le\|D_c\|_1\) by Theorem 6.3(5), and by Theorem 6.3(6), \(\sum_k|c_k|=\operatorname{Tr}(WD_c)\le\|WD_c\|_1\le\|D_c\|_1\).

(b) The sequences \(c_k=1/k\), \(c_k=1/\sqrt k\) and \(c_k=1\) give operators in \(\mathcal S_2\setminus\mathcal S_1\), in \(\mathcal K\setminus\mathcal S_2\) and in \(B\setminus\mathcal K\). The operator \(D_{c^{(m)}}\) has finite rank, and its singular values are the \(|c_k|\ne0\) with \(k\le m\) (write \(D_{c^{(m)}}=\sum_{k\le m}|c_k|\,\theta_{(c_k/|c_k|)\delta_k,\delta_k}\), omitting zero terms). By Theorem 5.5, for \(c_k=1/\sqrt k\) we get \(\lambda(D_{c^{(m)}})=1\) and \(\sigma(D_{c^{(m)}})^2=\sum_{k\le m}1/k\to\infty\); for \(c_k=1/k\) we get \(\sigma(D_{c^{(m)}})^2\le\sum_k1/k^2\) and \(\gamma(D_{c^{(m)}})=\sum_{k\le m}1/k\to\infty\). So there are no constants with \(\sigma\le C\lambda\) or \(\gamma\le C\sigma\), and, since \(\lambda\le\sigma\le\gamma\), no two of the norms are equivalent.

**Exercise 3** (a Jordan homomorphism with two pieces). Let \(\pi(x)=x\oplus x^{\mathrm t}\) from \(M_2(\mathbb C)\) into \(M_2(\mathbb C)\oplus M_2(\mathbb C)\), and use the matrix units \(E_{kl}\). Compute \(v_{12}\), \(w_{12}\), \(e\) and \(f\) of Theorem 9.1, and show that \(e\notin\pi(M_2(\mathbb C))\).

*Solution.* \(P_1=E_{11}\oplus E_{11}\), \(P_2=E_{22}\oplus E_{22}\), \(U_{12}=E_{12}\oplus E_{21}\) and \(U_{21}=E_{21}\oplus E_{12}\). Hence \(v_{12}=P_1U_{12}P_2=E_{12}\oplus0\) and \(w_{12}=P_1U_{21}P_2=0\oplus E_{12}\). Then \(v_{11}=v_{12}v_{12}^*=E_{11}\oplus0\) and \(w_{11}=w_{12}w_{12}^*=0\oplus E_{11}\), and similarly \(v_{22}=E_{22}\oplus0\), \(w_{22}=0\oplus E_{22}\). So \(e=1\oplus0\) and \(f=0\oplus1\). Indeed \(\pi(x)e=x\oplus0\) is multiplicative and \(\pi(x)f=0\oplus x^{\mathrm t}\) is antimultiplicative. If \(1\oplus0=x\oplus x^{\mathrm t}\), then \(x=1\) and \(x^{\mathrm t}=0\), which is impossible.

**Exercise 4** (unital isometries of a matrix algebra). Show that every linear isometry \(\Phi\) of \(M_n(\mathbb C)\) onto itself with \(\Phi(1)=1\) has the form \(x\mapsto uxu^*\) or \(x\mapsto ux^{\mathrm t}u^*\) for a unitary \(u\).

*Solution.* By Theorem 11.5, \(\Phi\) is a Jordan \(*\)-isomorphism. Since \(M_n(\mathbb C)\) is a factor, Corollary 10.4(3) shows that \(\Phi\) is a \(*\)-automorphism or a \(*\)-antiautomorphism. A \(*\)-automorphism of \(M_n(\mathbb C)=B(\mathbb C^n)\) is \(x\mapsto uxu^*\) for a unitary \(u\), because isomorphisms between algebras \(B(H)\) are spatial ([The universal enveloping von Neumann algebra of a \(C^*\)-algebra, and \(W^*\)-algebras](../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html), Lemma 6.4). If \(\Phi\) is a \(*\)-antiautomorphism, then \(x\mapsto\Phi(x)^{\mathrm t}\) is multiplicative, preserves adjoints and is bijective, so it is \(x\mapsto vxv^*\) for a unitary \(v\). Hence \(\Phi(x)=(vxv^*)^{\mathrm t}=\bar v\,x^{\mathrm t}\,v^{\mathrm t}\), and \(u=\bar v\) is a unitary with \(u^*=v^{\mathrm t}\).

**Exercise 5** (many real inner products). Let \(H\) and \(K\) be real Hilbert spaces of dimension at least two. Show that \(H\odot K\) carries infinitely many inner products with \(\|x\otimes y\|=\|x\|\|y\|\) for all \(x,y\).

*Solution.* Choose orthonormal \(a_1,a_2\in H\) and \(b_1,b_2\in K\). Let \(J_H\) send \(a_1\mapsto a_2\) and \(a_2\mapsto-a_1\) and vanish on the orthogonal complement of \(a_1,a_2\); define \(J_K\) in the same way. Both are antisymmetric, so \(\langle J_Hx,x\rangle=0\) and \(\langle J_Ky,y\rangle=0\). The operator \(Q=J_H\otimes J_K\) on \(H\otimes K\) is symmetric, since \(J_H^{\mathrm T}\otimes J_K^{\mathrm T}=(-J_H)\otimes(-J_K)=Q\), and \(\|Q\|\le1\). For \(|t|<1\), \(\langle\zeta,\zeta'\rangle_t=\langle(1+tQ)\zeta,\zeta'\rangle\) is an inner product, since \(1+tQ\ge1-|t|>0\). It satisfies \(\langle x\otimes y,x\otimes y\rangle_t=\|x\|^2\|y\|^2+t\langle J_Hx,x\rangle\langle J_Ky,y\rangle=\|x\|^2\|y\|^2\). Different values of \(t\) give different inner products, because \(\langle Q(a_1\otimes b_1),a_2\otimes b_2\rangle=1\).

## Where this leads

- A positive map stays positive after tensoring with the identity map of \(M_n(\mathbb C)\), for every \(n\), exactly when it is completely positive; these maps are studied in Completely positive maps. Example 8.4 shows that the transpose is not completely positive.
- By Theorem 7.2, \(B(H)\) is the dual of the trace class. This is the starting point of normal functionals and weights on von Neumann algebras; the same predual is built from Hilbert tensors in the lesson *Concrete preduals from Hilbert tensors* of the course *Modular Theory & Weights*.
- A linear order isomorphism of one unital \(C^*\)-algebra onto another that maps \(1\) to \(1\) is a Jordan \(*\)-isomorphism. Also, for unital \(C^*\)-algebras \(A\) and \(B\), every weak\(^*\) continuous affine bijection of the state space of \(A\) onto the state space of \(B\) has the form \(\rho\mapsto\rho\circ\psi\) for a Jordan \(*\)-isomorphism \(\psi\) of \(B\) onto \(A\) (Kadison).

## Results used from other lessons

(a) *The Hahn–Banach theorem.* Every bounded linear functional on a subspace of a normed space extends to the whole space with the same norm. Consequently \(\|x\|=\max\{|f(x)|:\|f\|\le1\}\) for every vector \(x\). Proved in Hahn–Banach, Baire and the basic
theorems on Banach spaces, Section 2.

(b) *Facts on \(C^*\)-algebras*, proved in C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients. The continuous functional calculus for normal elements, with and without a unit. The norm of a normal element is its spectral radius. A self-adjoint element \(h\) is positive exactly when its spectrum lies in \([0,\infty)\), and then it has a unique positive square root; every self-adjoint element is a difference of two positive ones; \(-\|h\|\le h\le\|h\|\); and \(-c\le b\le c\) for a self-adjoint \(b\) implies \(\|b\|\le c\). A \(C^*\)-algebra is a closed ideal in its unitization, with the same norm and the same positive elements. Every \(*\)-homomorphism between \(C^*\)-algebras is contractive.

(c) *Spectral projections.* Let \(h\) be a self-adjoint element of a von Neumann algebra \(M\subseteq B(H)\). There is a projection-valued measure \(E\) on the Borel subsets of the spectrum of \(h\) with \(h=\int\lambda\,dE(\lambda)\), and every \(E(\omega)\) commutes with each operator that commutes with \(h\); so \(E(\omega)\in M\). If the spectrum is divided into disjoint Borel sets \(\omega_1,\ldots,\omega_m\) of diameter less than \(\varepsilon\), and \(\lambda_k\in\omega_k\), then the \(E(\omega_k)\) are mutually orthogonal projections and \(\|h-\sum_k\lambda_kE(\omega_k)\|\le\varepsilon\). Proved in The spectral theorem for bounded self-adjoint
operators, Theorems 3.1 and 4.4: the commutation is Theorem 3.1(5), so \(E(\omega)\in M''=M\), and the
estimate is Theorem 3.1(3) applied to the function \(\lambda-\sum_k\lambda_k1_{\omega_k}(\lambda)\), of supremum at most
\(\varepsilon\) on the spectrum.

(d) *Biduals of \(C^*\)-algebras*, from [The universal enveloping von Neumann algebra of a \(C^*\)-algebra, and \(W^*\)-algebras](../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html). For a \(C^*\)-algebra \(A\), the bidual \(A^{**}\) carries a product and an involution extending those of \(A\) through \(j_A\), and with them it is isometrically isomorphic to a von Neumann algebra, by a map that carries \(\sigma(A^{**},A^*)\) to the \(\sigma\)-weak topology. Multiplication is separately \(\sigma\)-weakly continuous, the involution is \(\sigma\)-weakly continuous, and \(j_A(A)\) is \(\sigma\)-weakly dense. An element \(X\) of \(A^{**}\) is positive exactly when \(X(f)\ge0\) for every positive \(f\in A^*\). For an operator \(T\) between Banach spaces, the second adjoint \(T^{**}\) is continuous for the weak\(^*\) topologies, satisfies \(T^{**}\circ j=j\circ T\), has norm \(\|T\|\), and \((ST)^{**}=S^{**}T^{**}\). A von Neumann algebra \(N\) is the dual of its predual \(N_*\), the space of its \(\sigma\)-weakly continuous functionals. Every \(C^*\)-algebra has a faithful representation on a Hilbert space.

(e) *Projections and types*, from Projections and types of von Neumann algebras. Let \(M\) be a von Neumann algebra. There is a central projection \(z_{\rm I}\) such that \(M(1-z_{\rm I})\) has no nonzero abelian projection and \(Mz_{\rm I}\) is of type I. For each nonzero cardinal \(\alpha\), \(Mz_{\rm I}\) has a largest central projection \(z_\alpha\) that is the sum of \(\alpha\) mutually orthogonal abelian projections with central support \(z_\alpha\); these \(z_\alpha\) are mutually orthogonal with sum \(z_{\rm I}\). Abelian projections with the same central support are equivalent. If \((e_i)\) and \((f_i)\) are families of mutually orthogonal projections with \(e_i\sim f_i\) for each \(i\), then \(\sum_ie_i\sim\sum_if_i\). Mutually orthogonal, mutually equivalent projections \(e_1,\ldots,e_n\) with sum \(1\) are the diagonal of a system of \(n\times n\) matrix units. If an algebra has no nonzero abelian projections, then each of its projections is the sum of two orthogonal equivalent projections. Finally, a bounded linear functional \(\omega\) on a unital \(C^*\)-algebra with \(\omega(1)=\|\omega\|\) is positive.

(f) *Banach spaces without the approximation property.* [Theorem 4.12](#4-12-a-closed-sequence-subspace-without-finite-rank-approximation) proves that a closed subspace of \(c_0\) fails the approximation property, over the complex or real scalars. Its complex example, together with Corollary 4.11(2), supplies the existence assertion in Proposition 4.6(3). The construction follows Davie's method in [Dacunha–Castelle 1974]; Enflo's original counterexample is [Enflo 1973].

(g) *Polar decomposition of bounded functionals.* For a \(C^*\)-algebra \(B\) and \(f\in B^*\), regarded as a normal functional on \(B^{**}\), there are a partial isometry \(v\in B^{**}\) and a positive functional \(\omega\) with \(\|\omega\|=\|f\|\) and \(f(x)=\omega(xv)\) for all \(x\in B^{**}\). Proved in Polar decomposition and absolute value of functionals, Theorem 2.7 (with the module action \((v\omega)(x)=\omega(xv)\) of its conventions).

(h) *The GNS construction.* Every positive functional \(\omega\) on a unital \(C^*\)-algebra \(C\) is \(\omega(y)=\langle\pi(y)\xi,\xi\rangle\) for a representation \(\pi\) of \(C\) with \(\pi(1)=1\) and a vector \(\xi\) with \(\|\xi\|^2=\omega(1)=\|\omega\|\). Proved in Representations and positive functionals, Section 5.

## References



- [Jacobson–Rickart 1950] N. Jacobson and C. E. Rickart, *Jordan homomorphisms of rings*, Trans. Amer. Math. Soc. 69 (1950), 479–502. Free at https://www.ams.org/journals/tran/1950-069-00/S0002-9947-1950-0038335-X/S0002-9947-1950-0038335-X.pdf
- [Størmer 1965] E. Størmer, *On the Jordan structure of \(C^*\)-algebras*, Trans. Amer. Math. Soc. 120 (1965), 438–447. Free at https://www.ams.org/journals/tran/1965-120-03/S0002-9947-1965-0185463-5/S0002-9947-1965-0185463-5.pdf
- [Enflo 1973] P. Enflo, *A counterexample to the approximation problem in Banach spaces*, Acta Math. 130 (1973), 309–317. Free at https://projecteuclid.org/journals/acta-mathematica/volume-130/issue-none/A-counterexample-to-the-approximation-problem-in-Banach-spaces/10.1007/BF02392270.pdf
- [Grothendieck 1952] A. Grothendieck, *Résumé des résultats essentiels dans la théorie des produits tensoriels topologiques et des espaces nucléaires*, Ann. Inst. Fourier 4 (1952), 73–112. Free at https://www.numdam.org/item/10.5802/aif.46.pdf
- [Dacunha–Castelle 1974] D. Dacunha-Castelle, *Contre-exemple à la propriété d'approximation uniforme dans les espaces de Banach*, Séminaire Bourbaki, exposé 433 (June 1973), volume 15 (1974), 286–293. [NUMDAM exposition](https://www.numdam.org/item/SB_1972-1973__15__286_0/).
