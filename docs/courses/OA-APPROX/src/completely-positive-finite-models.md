# Completely positive finite models

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

A finite-dimensional model of an algebra need not preserve products. It can still preserve positivity after we couple the algebra to any matrix system. This is the reason completely positive maps are useful for approximation. They retain the order information that survives compression to a finite-dimensional Hilbert space.

We will construct such models, explain precisely what convergence means, and prove that sufficiently good models force uniqueness of the C*-tensor norm. The arguments work for nonunital and nonseparable algebras. Finite sets, rather than countable lists, organize the approximation.

Prerequisites are the lessons [Completely positive maps](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/completely-positive-maps.html) and [AF-algebras](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/af-algebras.html), together with the construction of the minimal and maximal C*-tensor products. We use Stinespring's theorem in its following form: a completely positive map \(\phi:A\to B(H)\) is \(V^*\pi(\,\cdot\,)V\), where \(\pi\) is a representation and \(\|V\|^2=\|\phi\|\). No faithfulness of an additional commutant representation is assumed. We also use Hahn–Banach, continuous functional calculus, and positive contractive approximate identities. The extension, dilation and commutant methods are developed in [Arveson 1969]; Section 4 below supplies the nonunital dilation step explicitly.

Unital algebras in the unital assertions are nonzero. The zero algebra has the approximation property by the zero maps.

## 1. Approximation is a finite-set question

Write \(M_n=M_n(\mathbb C)\). A **completely positive contraction**, abbreviated cpc, is a completely positive linear map of norm at most one. A unital completely positive map is abbreviated ucp. For C*-algebras \(A,D\), a cpc map \(\theta:A\to D\) has **finite-dimensional completely positive approximations** if, for every finite set \(F\subset A\) and every \(\varepsilon>0\), there are cpc maps
\[
A\xrightarrow{\alpha}M_n\xrightarrow{\beta}D
\quad\text{such that}\quad
\|\beta\alpha(a)-\theta(a)\|<\varepsilon\quad(a\in F).
\]
For \(\theta=\operatorname{id}_A\), this is the completely positive approximation property.

The maps \(\alpha\) and \(\beta\) play different roles. The first records finitely many matrix measurements. The second reconstructs an element of \(D\). Neither is required to be multiplicative or injective.

**Proposition 1.1.** The finite-set definition is equivalent to the existence of a net of cpc factorizations \(\theta_i=\beta_i\alpha_i\) through matrix algebras such that \(\|\theta_i(a)-\theta(a)\|\to0\) for every \(a\in A\).

**Proof.** Direct the pairs \((F,\varepsilon)\), with \(F\) finite, by increasing \(F\) and decreasing \(\varepsilon\). Choose one approximation for each pair. Once the index contains a given \(a\) and has tolerance less than a given positive number, all later indices meet that requirement. This gives pointwise norm convergence.

Conversely, for each \(a\) in a finite \(F\), convergence gives an index beyond which its error is less than \(\varepsilon\). A common upper bound of these finitely many indices works for all of \(F\). \(\square\)

**Proposition 1.2.** If \(A\) is separable, a net in Proposition 1.1 can be replaced by a sequence.

**Proof.** Choose a norm-dense sequence \(a_1,a_2,\ldots\) in \(A\). At stage \(k\), approximate \(a_1,\ldots,a_k\) within \(1/k\). For \(a\in A\), choose \(a_j\) close to \(a\). Contractivity gives
\[
\|\theta_k(a)-\theta(a)\|
\le 2\|a-a_j\|+\|\theta_k(a_j)-\theta(a_j)\|.
\]
First let \(k\to\infty\) and then let \(a_j\to a\). \(\square\)

Thus a sequence is available under separability. The definition itself does not require separability.

Finite-dimensional C*-algebras can replace the middle matrix algebra without changing the property. Indeed, write
\(F=\bigoplus_{j=1}^rM_{n_j}\), place \(F\) as diagonal blocks in \(M_N\), where \(N=\sum_jn_j\), and let
\[
P(x)=\bigoplus_jp_jxp_j.
\]
The inclusion and \(P\) are cpc, and \(P\) fixes \(F\). They turn a factorization through \(F\) into one through \(M_N\). Conversely a full matrix algebra is already finite-dimensional.

## 2. Order allows extensions

An **operator system** \(S\subset C\) is a self-adjoint linear subspace of a unital C*-algebra containing \(1_C\). Its matrix positive cones are inherited from \(C\). We now prove the extension theorem needed to put finite-dimensional models on a larger algebra.

We first translate a matrix-valued map into a scalar functional. We use column vectors and write quadratic forms as \(\xi^*T\xi\).

**Lemma 2.1.** For a linear map \(\phi:S\to M_n\), define
\[
f_\phi([s_{ij}])=\sum_{i,j=1}^n\phi(s_{ij})_{ij}.
\]
Then \(\phi\) is completely positive if and only if \(f_\phi\) is a positive functional on the operator system \(M_n(S)\).

**Proof.** If \(\phi\) is completely positive and \([s_{ij}]\ge0\), apply \(\phi\) entrywise and evaluate its positive quadratic form on the vector whose \(i\)-th component is the \(i\)-th standard basis vector. The result is \(f_\phi([s_{ij}])\ge0\).

Conversely, let \(X=[s_{pq}]\in M_m(S)_+\) and let \(\xi_1,\ldots,\xi_m\in\mathbb C^n\). Set \(U_{pi}=(\xi_p)_i\). The scalar compression \(U^*XU\) belongs to \(M_n(S)_+\). Its entries are
\[
(U^*XU)_{ij}=\sum_{p,q}\overline{(\xi_p)_i}s_{pq}(\xi_q)_j.
\]
Therefore
\[
f_\phi(U^*XU)
=\sum_{p,q}\xi_p^*\phi(s_{pq})\xi_q\ge0.
\]
All quadratic forms of \(\phi^{(m)}(X)\) are nonnegative. Hence \(\phi\) is completely positive. \(\square\)

**Lemma 2.2.** A positive functional \(f\) on an operator system \(R\subset D\) extends to a positive functional \(g\) on \(D\) with \(g(1)=f(1)\).

**Proof.** On the real vector space \(D_{\rm sa}\), define
\[
p(x)=\inf\{f(y):y\in R_{\rm sa},\ y\ge x\}.
\]
The set is nonempty because it contains \(\|x\|1\). It is bounded below: \(y\ge x\ge-\|x\|1\) implies \(f(y)\ge-\|x\|f(1)\). The function \(p\) is sublinear, and \(p(y)=f(y)\) for \(y\in R_{\rm sa}\). Real Hahn–Banach extends \(f|_{R_{\rm sa}}\) to a real linear \(g_0\le p\) on \(D_{\rm sa}\).

If \(x\ge0\), then \(p(-x)\le f(0)=0\), so \(g_0(x)\ge0\). Also \(g_0(1)=f(1)\). Complexify \(g_0\). The result is a positive linear functional \(g\). Positivity gives \(\|g\|=g(1)\), so it is bounded. \(\square\)

**Theorem 2.3 (Arveson extension).** If \(S\subset C\) is an operator system and \(\phi:S\to B(H)\) is completely positive, there is a completely positive extension \(\Phi:C\to B(H)\). If \(\phi\) is unital, \(\Phi\) is unital.

**Proof.** Suppose first that \(H=\mathbb C^n\). Extend \(f_\phi\) from \(M_n(S)\) to a positive functional \(g\) on \(M_n(C)\), using Lemma 2.2. Define
\[
\Phi(c)_{ij}=g(E_{ij}\otimes c).
\]
Then \(f_\Phi=g\), so Lemma 2.1 makes \(\Phi\) completely positive. For \(s\in S\), the definition gives \(\Phi(s)_{ij}=\phi(s)_{ij}\). In particular \(\Phi(1)=\phi(1)\).

For arbitrary \(H\), direct its finite-dimensional subspaces \(K\) by inclusion. Compress \(\phi\) to \(B(K)\), extend it by the finite-dimensional case, and regard the extension \(\Phi_K\) as a map into \(B(H)\), zero on \(K^\perp\). Each map is completely positive and
\[
\|\Phi_K\|=\|\Phi_K(1)\|
=\|P_K\phi(1)P_K\|\le\|\phi(1)\|.
\]
For every \(c\in C\), the values lie in the ultraweakly compact ball of radius \(\|\phi(1)\|\|c\|\). Compactness of the product of these balls supplies a subnet converging ultraweakly at every \(c\). Its limit \(\Phi\) is linear. Matrix positive cones in \(B(H)\) are ultraweakly closed, so \(\Phi\) is completely positive.

For \(s\in S\), we have \(\Phi_K(s)=P_K\phi(s)P_K\), which converges strongly, and hence ultraweakly on this bounded net, to \(\phi(s)\). Thus \(\Phi\) extends \(\phi\). Its value at \(1\) is \(\phi(1)\), proving the unital assertion. \(\square\)

No separability of \(H\) was used. The extension need not be normal even if part of the original setting involves von Neumann algebras.

**Corollary 2.4.** If \(F\subset A\) is a finite-dimensional C*-subalgebra, there is a cpc map \(E:A\to F\) that fixes \(F\).

**Proof.** Represent \(F=\bigoplus_jM_{n_j}\). Let \(p\) be its unit, which is a projection of \(A\). In the unital algebra \(pAp\), extend each coordinate map \(F\to M_{n_j}\) by Theorem 2.3. Their direct sum is a ucp map \(E_0:pAp\to F\). Put \(E(a)=E_0(pap)\). Compression is cpc, and \(E\) fixes \(F\). \(\square\)

**Proposition 2.5 (Normalize at the unit).** Let \(S\subset C\) be an operator system and \(\phi:S\to M\) a completely positive map into a von Neumann algebra. Put \(b=\phi(1)\). There is a ucp map \(\phi_0:S\to M\) such that
\[
\phi(x)=b^{1/2}\phi_0(x)b^{1/2}\quad(x\in S).
\]

**Proof.** Let \(e\) be the support projection of \(b\). For \(\delta>0\), set
\(\psi_\delta(x)=(b+\delta1)^{-1/2}\phi(x)(b+\delta1)^{-1/2}\).
These maps are completely positive and have norm at most one, since their values at \(1\) are \(b(b+\delta1)^{-1}\le1\). Compactness of the product of ultraweakly compact balls in \(M\) gives a pointwise ultraweak cluster map \(\psi_0\), which is completely positive and satisfies \(\psi_0(1)=e\).

For a positive \(x\in S\), \(0\le\phi(x)\le\|x\|b\), so \(\phi(x)\) is supported on \(e\). The positive elements span \(S\), so this holds for every \(x\). As \(\delta\downarrow0\), the contractions \(b^{1/2}(b+\delta1)^{-1/2}\) converge strongly to \(e\). Therefore
\[
b^{1/2}\psi_\delta(x)b^{1/2}
\longrightarrow\phi(x)
\]
strongly, and the ultraweak cluster limit gives \(b^{1/2}\psi_0(x)b^{1/2}=\phi(x)\).

Choose a state \(\omega\) of \(C\) and put
\(\phi_0(x)=\psi_0(x)+\omega(x)(1-e)\).
It is ucp, and the added term disappears after multiplication by \(b^{1/2}\). The case \(b=0\) is included: then \(\phi=0\). \(\square\)

## 3. Finite models that we can see

**Example 3.1 (Compact operators).** Let \(H\) be any Hilbert space. For a finite-dimensional subspace \(K\), compression and inclusion give cpc maps
\[
\mathcal K(H)\longrightarrow B(K)\longrightarrow\mathcal K(H),
\qquad T\longmapsto P_KTP_K.
\]
These approximate the identity in norm as \(K\) increases. For a finite-rank \(T\), a \(K\) containing the ranges of \(T\) and \(T^*\) makes the compression exact. For a compact \(T\), approximate by a finite-rank operator and use contractivity. This proves the completely positive approximation property without assuming \(H\) separable.

**Theorem 3.2 (Locally finite-dimensional algebras).** Suppose that \(A\) is the norm closure of an upward-directed family of finite-dimensional C*-subalgebras. Then \(A\) has the completely positive approximation property.

**Proof.** Given finite \(F\subset A\) and \(\varepsilon>0\), choose one finite-dimensional subalgebra \(D\) and, for each \(a\in F\), an element \(d_a\in D\) with \(\|a-d_a\|<\varepsilon/2\). Use Corollary 2.4 for a cpc retraction \(E:A\to D\). Inclusion \(j:D\to A\) gives
\[
\|jE(a)-a\|\le\|E(a-d_a)\|+\|d_a-a\|<\varepsilon.
\]
Replace \(D\) by a full matrix algebra as explained in Section 1. \(\square\)

In particular every AF-algebra has this property. The directed version also treats norm closures of noncountable families; no countable generating sequence is required.

**Theorem 3.3 (Functions vanishing at infinity).** For every locally compact Hausdorff space \(X\), \(C_0(X)\) has the completely positive approximation property.

**Proof.** Fix finitely many functions \(f\) and a positive \(\varepsilon\). Choose a compact \(K\subset X\) such that \(|f(x)|<\varepsilon/2\) outside \(K\), simultaneously for all of them. Cover \(K\) by finitely many relatively compact open sets \(U_j\) and choose \(x_j\in U_j\) so that
\[
|f(x)-f(x_j)|<\varepsilon/2\quad(x\in U_j)
\]
for every chosen \(f\). A partition of unity on a neighborhood of \(K\), followed by a compactly supported cutoff, gives \(g_j\in C_c(X)_+\), supported in \(U_j\), with
\(\sum_jg_j=1\) on \(K\) and \(\sum_jg_j\le1\) everywhere.

Define
\[
\alpha(f)=(f(x_j))_j,\qquad
\beta((z_j)_j)=\sum_jz_jg_j.
\]
Evaluation is a *-homomorphism. The map \(\beta:\mathbb C^r\to C_0(X)\) is completely positive: a positive matrix over \(\mathbb C^r\) becomes, at each point of \(X\), a nonnegative linear combination of positive scalar matrices. Its norm is \(\|\sum_jg_j\|\le1\). Thus both maps are cpc.

At \(x\in X\), write \(s(x)=\sum_jg_j(x)\). Then
\[
|\beta\alpha(f)(x)-f(x)|
\le\sum_jg_j(x)|f(x_j)-f(x)|+(1-s(x))|f(x)|.
\]
The first term is at most \(\varepsilon/2\). The second vanishes on \(K\), and is less than \(\varepsilon/2\) off \(K\). This proves the required uniform approximation. \(\square\)

For \(X=[0,1]\), one may take equally spaced sample points and the piecewise linear tent functions. If every \(f\) in the finite set has Lipschitz constant at most \(L\), a mesh of width \(h\) gives error at most \(Lh\). This finite model consists of samples and interpolation weights; it is not a finite-dimensional subalgebra of \(C([0,1])\).

## 4. Why matrix models control tensor norms

For an algebraic tensor \(z\in A\odot B\), the minimal norm is obtained in a tensor product of faithful representations. The maximal norm is the supremum over representations of \(A\) and \(B\) with commuting ranges on one Hilbert space. We always have \(\|z\|_{\min}\le\|z\|_{\max}\).

**Lemma 4.1.** If \(\phi:A\to D\) is cpc, then
\(\phi\odot\operatorname{id}_B\) extends to a contraction both from \(A\otimes_{\min}B\) to \(D\otimes_{\min}B\) and from \(A\otimes_{\max}B\) to \(D\otimes_{\max}B\).

**Proof.** For the minimal norm, represent \(D\) faithfully on \(H\) and \(B\) faithfully on \(L\), and dilate the resulting map \(A\to B(H)\) as \(V^*\pi(\,\cdot\,)V\), with \(\|V\|\le1\). Then
\[
(\phi\odot\operatorname{id}_B)(z)
=(V\otimes1)^*(\pi\odot\sigma)(z)(V\otimes1).
\]
Every tensor product of representations is bounded by the minimal norm, so this expression has norm at most \(\|z\|_{\min}\).

For the maximal norm, fix commuting representations \(\rho:D\to B(H)\) and \(\sigma:B\to B(H)\), and put \(\psi=\rho\phi\). We need a dilation of \(\psi\) that also carries the \(B\)-action. Here is the construction. On \(A\odot H\), use the positive form associated to \(\psi\):
\[
\left\|\sum_i a_i\otimes\xi_i\right\|_\psi^2
=\sum_{i,j}\xi_i^*\psi(a_i^*a_j)\xi_j.
\]
Left multiplication defines the Stinespring representation \(\pi\). Since \(\sigma(b)\) commutes with every \(\psi(a)\), the operation
\[
\widehat\sigma(b)(a\otimes\xi)=a\otimes\sigma(b)\xi
\]
is bounded by \(\|b\|\) in this seminorm: the positive operator matrix \([\psi(a_i^*a_j)]\) commutes with the diagonal matrix whose entries are \(\sigma(b)\). The operation therefore descends to the completed quotient. Its adjoint is the operation for \(b^*\), and multiplication is preserved. Thus \(\widehat\sigma\) is a representation commuting with \(\pi\).

Here is the approximate-identity step when \(A\) is nonunital. Let \((e_\lambda)\) be a positive contractive approximate identity. For \(\xi\in H\), the quotient vectors \(e_\lambda\otimes\xi\) have norms at most \(\|\xi\|\), since
\[
\|e_\lambda\otimes\xi\|_\psi^2
=\xi^*\psi(e_\lambda^2)\xi\le\|\xi\|^2.
\]
For every \(a\otimes\eta\), their inner products converge, because \(e_\lambda a\to a\) in norm and \(\psi\) is bounded. Density and the uniform bound give a weak limit \(V\xi\), with \(\|V\|\le1\). Left multiplication satisfies
\[
\pi(a)(e_\lambda\otimes\xi)=ae_\lambda\otimes\xi
\longrightarrow a\otimes\xi
\]
in the quotient norm: the squared error is at most \(\|ae_\lambda-a\|^2\|\xi\|^2\). Taking weak limits proves \(\pi(a)V\xi=a\otimes\xi\), and pairing with \(V\eta\) gives \(V^*\pi(a)V=\psi(a)\). The bounded operator \(\widehat\sigma(b)\) preserves weak limits and takes \(e_\lambda\otimes\xi\) to \(e_\lambda\otimes\sigma(b)\xi\). Consequently \(\widehat\sigma(b)V=V\sigma(b)\). In the unital case the same identities follow immediately from \(V\xi=1\otimes\xi\). Neither construction requires \(V\) or the commutant representation to be faithful. It follows that
\[
\sum_i\rho(\phi(a_i))\sigma(b_i)
=V^*\left(\sum_i\pi(a_i)\widehat\sigma(b_i)\right)V.
\]
Its norm is at most \(\|\sum_i a_i\otimes b_i\|_{\max}\). Take the supremum over the commuting representations. \(\square\)

**Lemma 4.2.** For every \(B\), the minimal and maximal norms on \(M_n\odot B\) agree. The same holds for a finite direct sum of matrix algebras.

**Proof.** A nondegenerate representation of \(M_n\) is unitarily equivalent to \(x\mapsto x\otimes1_L\) on \(\mathbb C^n\otimes L\), as follows by decomposing with its matrix units. Any commuting representation of \(B\) has the form \(b\mapsto1_n\otimes\sigma(b)\). Their product representation is therefore bounded by the minimal norm. Degenerate representations can be restricted to their support. This proves the result for \(M_n\). Central projections split a representation of a finite direct sum into the corresponding summands, and the norm is the largest summand norm. \(\square\)

A C*-algebra \(A\) is **nuclear** if these two norms agree on \(A\odot B\) for every C*-algebra \(B\).

**Theorem 4.3.** A C*-algebra with the completely positive approximation property is nuclear.

**Proof.** Fix \(B\) and \(z=\sum_{j=1}^ra_j\otimes b_j\). Choose cpc factorizations \(\theta_i=\beta_i\alpha_i\) approximating \(\operatorname{id}_A\). The cross-norm estimate gives
\[
\|(\theta_i\odot\operatorname{id}_B)(z)-z\|_{\max}
\le\sum_j\|\theta_i(a_j)-a_j\|\|b_j\|\longrightarrow0.
\]
By Lemmas 4.1 and 4.2,
\[
\begin{aligned}
\|(\beta_i\odot\operatorname{id}_B)(\alpha_i\odot\operatorname{id}_B)(z)\|_{\max}
&\le\|(\alpha_i\odot\operatorname{id}_B)(z)\|_{M_{n_i}\otimes_{\max}B}\\
&=\|(\alpha_i\odot\operatorname{id}_B)(z)\|_{M_{n_i}\otimes_{\min}B}\\
&\le\|z\|_{\min}.
\end{aligned}
\]
Pass to the limit. The reverse inequality always holds. \(\square\)

Combining this with Section 3 proves nuclearity of compact operators, commutative C*-algebras and AF-algebras. The converse, nuclearity implies completely positive approximation, requires an additional separation argument; it is proved in [Tensor positivity and nuclearity](tensor-positivity-nuclearity.md).

## 5. Permanence from the maps

**Proposition 5.1.** If \(A\) has the completely positive approximation property and \(\theta:A\to D\) is cpc, then \(\theta\) has finite-dimensional completely positive approximations.

**Proof.** Compose the reconstruction map for an approximation of \(\operatorname{id}_A\) with \(\theta\). Contractivity of \(\theta\) does not increase the error. \(\square\)

**Proposition 5.2.** If \(D\) has the completely positive approximation property and there are cpc maps \(s:A\to D\), \(r:D\to A\) with \(rs=\operatorname{id}_A\), then \(A\) has the same property.

**Proof.** Compose approximations of \(\operatorname{id}_D\) on the finite set \(s(F)\) with \(s\) and \(r\). \(\square\)

**Proposition 5.3.** If \(A\) has the completely positive approximation property, so do every closed ideal \(I\subset A\) and every corner \(pAp\), where \(p\in A\) is a projection.

**Proof.** For an ideal, let \(F\subset I\) be finite. Choose a positive contraction \(e\in I\) with \(\|eae-a\|<\varepsilon/2\) for \(a\in F\), using an approximate identity of \(I\). Choose a cpc factorization \(\beta\alpha\) on \(A\) with error less than \(\varepsilon/2\) on \(F\). Restrict \(\alpha\) to \(I\), and replace \(\beta(x)\) by \(e\beta(x)e\). The new reconstruction map has range in \(I\), is cpc, and has total error less than \(\varepsilon\).

For a corner, use the inclusion \(pAp\to A\) and the cpc retraction \(a\mapsto pap\) in Proposition 5.2. \(\square\)

**Proposition 5.4.** Suppose \(A\) is the closure of an upward-directed family of C*-subalgebras \(A_\lambda\), each having the completely positive approximation property. Then \(A\) has the property.

**Proof.** Approximate a finite set \(F\subset A\) by elements \(b_a\) of a common \(A_\lambda\). Choose cpc maps \(\alpha_0:A_\lambda\to M_n\), \(\beta_0:M_n\to A_\lambda\) approximating all \(b_a\).

The map \(\alpha_0\) extends to a cpc map \(\alpha:A\to M_n\). To see this when the algebras are nonunital, take a Stinespring dilation of \(\alpha_0\) and extend its representation to the unitization. This gives a completely positive extension to \(A_\lambda+\mathbb C1\) with value at \(1\) at most \(1_n\). Apply Theorem 2.3 in the unitization of \(A\), and restrict back to \(A\). Its norm is at most one. If \(A_\lambda\) already contains the ambient unit, apply Theorem 2.3 directly.

Let \(\beta\) be \(\beta_0\) followed by inclusion in \(A\). Then
\[
\|\beta\alpha(a)-a\|
\le 2\|a-b_a\|+\|\beta_0\alpha_0(b_a)-b_a\|.
\]
Choose both errors small enough. \(\square\)

## 6. Exercises with solutions

**Exercise 1 (A finite algebra inside one matrix algebra; introductory).** Embed \(M_2\oplus\mathbb C\oplus M_3\) in \(M_6\). Give a cpc retraction and verify that it fixes the embedded algebra.

*Solution.* Use diagonal blocks of sizes \(2,1,3\), with projections \(p_1,p_2,p_3\). The retraction is \(x\mapsto(p_1xp_1,p_2xp_2,p_3xp_3)\). Each compression is completely positive. The direct sum map is unital, so is contractive. On a block diagonal matrix it returns the original three blocks.

**Exercise 2 (Error propagation; introductory).** Suppose \(\theta_i\) and \(\theta\) are contractions on a Banach space and \(\|\theta_i(a_j)-\theta(a_j)\|\to0\) on a dense subset. Prove convergence everywhere.

*Solution.* For any \(a\), select \(a_j\) with \(\|a-a_j\|<\delta\). Then \(\|\theta_i(a)-\theta(a)\|\le2\delta+\|\theta_i(a_j)-\theta(a_j)\|\). The limit superior is at most \(2\delta\), and \(\delta\) is arbitrary.

**Exercise 3 (A matrix test for positivity; intermediate).** For \(\beta:M_n\to D\), prove that \(\beta\) is completely positive if and only if \(C_\beta=[\beta(E_{ij})]\) is positive in \(M_n(D)\).

*Solution.* The matrix \([E_{ij}]\in M_n(M_n)\) is positive: on \(\mathbb C^n\otimes\mathbb C^n\) it is the rank-one operator \(|\sum_ie_i\otimes e_i\rangle\langle\sum_ie_i\otimes e_i|\). Complete positivity therefore makes \(C_\beta\) positive.

Conversely factor \(C_\beta=R^*R\), writing its entries as
\(\beta(E_{ij})=\sum_k r_{ki}^*r_{kj}\). For a positive block matrix \(X=[x_{pq}]\in M_m(M_n)\), each matrix
\[
\left[\sum_{i,j}(x_{pq})_{ij}r_{ki}^*r_{kj}\right]_{p,q}
\]
is positive. Indeed it is obtained from the positive scalar matrix indexed by \((p,i),(q,j)\) by multiplying on the left and right by the corresponding rectangular matrices with entries \(r_{ki}\). Summing over \(k\) gives \([\beta(x_{pq})]\ge0\).

**Exercise 4 (A model with no product rule; intermediate).** On \(C([0,1])\), let \(\alpha(f)=(f(0),f(1))\) and \(\beta(a,b)(t)=(1-t)a+tb\). Show that \(\alpha,\beta\) are ucp, that \(\beta\alpha\) fixes the function \(t\), and that it does not fix \(t^2\).

*Solution.* Evaluation is a unital *-homomorphism. The two coefficients \(1-t,t\) are positive and sum to one, so \(\beta\) is ucp by the pointwise matrix test. Both \(t\) and \(t^2\) have samples \((0,1)\), so their reconstructions are \(t\). At \(t=1/2\), the reconstructed square has value \(1/2\), while \(t^2\) has value \(1/4\).

**Exercise 5 (Why a net is needed; intermediate).** Let \(I\) be uncountable and \(H=\ell^2(I)\). Prove that no sequence of finite-dimensional subspaces \(K_n\) makes \(P_{K_n}TP_{K_n}\to T\) in norm for every \(T\in\mathcal K(H)\).

*Solution.* The closed span \(K\) of all \(K_n\) is separable. Every vector of \(\ell^2(I)\) has countable support, so a countable dense subset of \(K\) has support in some countable \(J\subset I\). Choose \(i\in I\setminus J\). Then \(e_i\perp K_n\) for every \(n\). For the rank-one projection \(T\) onto \(\mathbb Ce_i\), all compressions vanish, and their distance from \(T\) is one. The directed family of all finite-dimensional subspaces does approximate every compact operator, as in Example 3.1.

**Exercise 6 (Weak approximation and convexity; advanced).** Let \(\mathcal F\) consist of cpc maps \(A\to D\) factoring through matrix algebras. Prove that \(\mathcal F\) is convex. Then show that if \(\theta\) lies in its pointwise weak closure, it lies in its pointwise norm closure.

*Solution.* For factorizations \(\beta_j\alpha_j\) and nonnegative \(t_j\) summing to one, define \(\alpha(a)=\bigoplus_j\alpha_j(a)\) and \(\beta((x_j)_j)=\sum_jt_j\beta_j(x_j)\). Both are cpc: at every matrix level positivity is preserved, and the norm of the second is at most \(\sum_jt_j=1\). Replace the direct sum by one matrix algebra using Section 1.

For a finite \(F=\{a_1,\ldots,a_r\}\), evaluate \(\mathcal F\) in the Banach space \(D^r\), with maximum norm. Its image is convex. The weak and norm closures of a convex subset of a Banach space agree by Hahn–Banach separation. The pointwise weak hypothesis says \((\theta(a_1),\ldots,\theta(a_r))\) belongs to its weak closure, hence to its norm closure. This is exactly the required finite-set approximation.

**Exercise 7 (The unit can be repaired; advanced).** Suppose \(A,D\) are unital, \(\theta:A\to D\) is ucp, and cpc factorizations approximate \(\theta\) in norm. Prove that the approximating maps can be taken ucp in both directions.

*Solution.* Start with \(\alpha:A\to M_n\), \(\beta:M_n\to D\), and put \(h=\alpha(1)\). Choose a state \(\omega\) on \(A\) and define
\(\alpha_1(a)=\alpha(a)+\omega(a)(1-h)\). This is ucp. Let \(d=\beta(1)-\beta(h)\). Then \(0\le d\le1-\beta(h)\), so
\(\|d\|\le\|1-\beta\alpha(1)\|\), and
\(\|\beta\alpha_1(a)-\beta\alpha(a)\|\le\|a\|\|1-\beta\alpha(1)\|\).

Choose a state \(\tau\) on \(M_n\), and set
\(\beta_1(x)=\beta(x)+\tau(x)(1-\beta(1))\). This too is ucp. Since \(0\le1-\beta(1)\le1-\beta(h)\), the additional error on \(\alpha_1(a)\) is at most \(\|a\|\|1-\beta\alpha(1)\|\). Consequently
\[
\|\beta_1\alpha_1(a)-\theta(a)\|
\le\|\beta\alpha(a)-\theta(a)\|+2\|a\|\|1-\beta\alpha(1)\|.
\]
Include \(1\) in the finite set and make its error sufficiently small.

**Exercise 8 (A hypothesis cannot be dropped; introductory).** Is every bounded map from an operator system to \(B(H)\) the restriction of a completely positive map?

*Solution.* No. Take \(S=\mathbb C\), \(H=\mathbb C\), and \(\phi(z)=-z\). It has norm one, and all its matrix amplifications have norm one. But \(\phi(1)=-1\) is not positive. Any extension still has that value at \(1\), so cannot be positive. Complete positivity of the original map is essential in Theorem 2.3.

## References

[Arveson 1969] William B. Arveson, [Subalgebras of C*-algebras](https://projecteuclid.org/euclid.acta/1485889628), *Acta Mathematica* 123 (1969), 141–224, DOI [10.1007/BF02392388](https://doi.org/10.1007/BF02392388). Theorem 1.1.1 and its proof construct the Stinespring quotient. Theorem 1.2.3 and its proof establish extension by separation and finite-dimensional compression; Proposition 1.2.10 gives the matrix norm bound. Theorem 1.3.1 constructs the commutant lift without assuming the dilation operator injective.

Section 2 here gives a different extension proof: the exact scalar functional on the matrix operator system, an order-dominating Hahn–Banach extension, and an ultraweak cluster map over all finite-dimensional subspaces. It also covers operator systems that are not norm closed. Section 4 carries the commuting action through the quotient directly and proves its approximate-identity identities for a nonunital algebra. The finite-set models, diffuse function interpolation, tensor-norm comparison and permanence arguments are derived above from these methods. They are not statements attributed to Arveson’s 1969 paper. In particular, Theorem 4.3 proves the direction from finite completely positive approximation to nuclearity; the converse is the separate tensor-positivity lesson.
