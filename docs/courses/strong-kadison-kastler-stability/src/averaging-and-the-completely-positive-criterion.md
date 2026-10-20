# Averaging and the completely positive criterion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Several steps of the proof of strong Kadison–Kastler stability do not produce a homomorphism between the two algebras. They produce an averaged map instead: a unital completely positive map from one algebra into the other, close to the identity at every matrix level. This lesson proves that such a map can be replaced by a spatial isomorphism implemented by a unitary near the identity (Proposition 4.1). The proof transports the product of the second algebra back to the first and corrects it with a theorem of Ricard and Roydor on perturbations of products. The lesson also collects the averaging tools used later: limits of completely positive maps, an invariant mean on the real numbers regarded as a discrete group, Christensen's theorem on injective near inclusions, and the passage of matrix distances to tensor products.

We use: [Close operator algebras](close-operator-algebras.md) (Lemmas 1.4, 1.5 and 3.3); from the foundations course, [Theorem 1.3](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-02) (bounded sesquilinear forms are given by operators), [Corollary 9.7(a)](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10) (the unit ball of \(B(H)\) is weakly compact), the [Banach–Alaoglu theorem](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian#OA-FND-WT-03), [Corollary 11.4](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras#OA-FND-WA-18) (\(*\)-isomorphisms of von Neumann algebras are normal) and the [bicommutant theorem](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#OA-FND-BI-06); the fact that completely positive maps \(\varphi\) satisfy \(\|\varphi\|_{\rm cb}=\|\varphi(1)\|\), from [Completely positive maps](course:foundations-of-von-neumann-algebras/completely-positive-maps); Corollary 5.2 of [Injective von Neumann algebras](course:injective-factors/injective-von-neumann-algebras) (abelian algebras, type I algebras and approximately finite-dimensional algebras are injective); from [Spatial tensor products of von Neumann algebras](course:tensor-products-of-operator-algebras/spatial-tensor-products-of-von-neumann-algebras#7-tensor-products-with-b-k-commutants-and-matrix-units), Proposition 7.1 and the matrix description of \(M\bar\otimes B(K)\) behind it, and [Corollary 11.5(2)](course:tensor-products-of-operator-algebras/spatial-tensor-products-of-von-neumann-algebras#11-the-commutation-theorem-and-its-consequences) (intersections of tensor products); and the Haar probability measure of a compact group, [Theorem 8.3 of Haar measure on locally compact groups](course:harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups#OA-FND-HM-05).

## 1. Limits of completely positive maps

A linear map \(F:A\to B(K)\) on a unital C\*-algebra is *unital completely positive*, abbreviated UCP, if \(F(1)=1\) and every amplification \(F_n\) is positive. A UCP map is completely contractive, since \(\|F\|_{\rm cb}=\|F(1)\|=1\), and it preserves adjoints. We write WOT for the weak operator topology.

**Lemma 1.1** (limits of UCP maps). Let \(A\) be a unital C\*-algebra and \((F_i)\) a net of UCP maps \(A\to B(K)\). A subnet converges pointwise in WOT to a UCP map \(F:A\to B(K)\). Moreover:

1. if \(\|F_i-\Phi\|_{\rm cb}\le a\) for a fixed linear map \(\Phi:A\to B(K)\) and all \(i\), then \(\|F-\Phi\|_{\rm cb}\le a\);
2. if every \(F_i\) takes values in a von Neumann algebra \(Q\subseteq B(K)\), so does \(F\).

The limit need not be normal, even when every \(F_i\) is.

**Proof.** For \(x\in A\) let \(\Omega_x=\{y\in B(K):\|y\|\le\|x\|\}\), a WOT compact set by [Corollary 9.7(a)](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10). The net \((F_i(x))_{x\in A}\) lies in the product \(\prod_x\Omega_x\), which is compact by Tychonoff's theorem, so a subnet converges in every coordinate; call the limits \(F(x)\). Linearity and \(F(1)=1\) pass to the limit. For \(X\in M_n(A)\) positive and \(\xi\in K^n\), \(\langle F_n(X)\xi,\xi\rangle\) is a finite sum of matrix coefficients and is the limit of the nonnegative numbers \(\langle(F_i)_n(X)\xi,\xi\rangle\); so \(F\) is UCP. For (1), \((F_i)_n(X)-\Phi_n(X)\) converges in WOT to \(F_n(X)-\Phi_n(X)\), and the ball of radius \(a\|X\|\) is WOT closed. For (2), \(Q\) is WOT closed. \(\square\)

## 2. An invariant mean on the real line

We write \(\mathbb R_d\) for the additive group of real numbers with the discrete topology, and \(\ell^\infty(\mathbb R)\) for the bounded complex functions on \(\mathbb R\).

**Proposition 2.1.** There is a positive linear functional \(m\) on \(\ell^\infty(\mathbb R)\) with \(m(1)=1\) and \(m(f(\cdot+t))=m(f)\) for all \(f\) and \(t\in\mathbb R\).

**Proof.** For a finite list \(E=(e_1,\dots,e_r)\) of real numbers and \(N\ge1\) let
\[
\mu_{E,N}(f)=N^{-r}\sum_{0\le n_1,\dots,n_r<N}f\Bigl(\sum_in_ie_i\Bigr).
\]
Each \(\mu_{E,N}\) is a state of the C\*-algebra \(\ell^\infty(\mathbb R)\). For \(t=e_j\), the difference \(\mu_{E,N}(f(\cdot+e_j))-\mu_{E,N}(f)\) telescopes in the variable \(n_j\), and
\[
|\mu_{E,N}(f(\cdot+e_j))-\mu_{E,N}(f)|\le\frac{2\|f\|_\infty}N .
\]
Order the pairs \((E,N)\) by \((E,N)\le(E',N')\) when every entry of \(E\) occurs in \(E'\) and \(N\le N'\). By the Banach–Alaoglu theorem the states have a weak\* cluster point \(m\), which is again a state. Given \(f\), \(t\) and \(\varepsilon>0\), every pair beyond \(((t),N_0)\) with \(2\|f\|_\infty/N_0<\varepsilon\) satisfies the displayed bound with \(\varepsilon\) in place of the right side; passing to the cluster point gives \(|m(f(\cdot+t))-m(f)|\le\varepsilon\). \(\square\)

Fix such an \(m\). For a bounded family \((T_s)_{s\in\mathbb R}\) in \(B(K)\), the form \((\xi,\eta)\mapsto m(s\mapsto\langle T_s\xi,\eta\rangle)\) is sesquilinear and bounded by \(\sup_s\|T_s\|\,\|\xi\|\|\eta\|\), so [Theorem 1.3](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-02) gives an operator \(m_sT_s\in B(K)\) with
\[
\langle(m_sT_s)\xi,\eta\rangle=m\bigl(s\mapsto\langle T_s\xi,\eta\rangle\bigr).
\]
No measurability or continuity in \(s\) is required.

**Lemma 2.2** (operator means).

1. The map \((T_s)\mapsto m_sT_s\), from the C\*-algebra of bounded families with pointwise operations to \(B(K)\), is UCP. For fixed \(A,B\in B(K)\) and \(t\in\mathbb R\),
\[
\begin{gathered}
m_s(AT_sB)=A\,(m_sT_s)\,B,\\
m_sT_{s+t}=m_sT_s .
\end{gathered}
\]
2. If every \(T_s\) lies in a von Neumann algebra \(Q\subseteq B(K)\), then so does \(m_sT_s\).
3. If \(\|T_s-T\|\le a\) for all \(s\), then \(\|m_sT_s-T\|\le a\). The same holds for rectangular matrices of bounded families, with the mean taken entrywise.
4. Let \(s\mapsto V_s\) be a unitary representation of \(\mathbb R_d\) on \(K\), with no continuity assumed, and \(E_V(T)=m_sV_sTV_s^*\). Then \(E_V:B(K)\to B(K)\) is UCP, its range commutes with every \(V_s\), it fixes every operator commuting with all \(V_s\), and it maps into itself every von Neumann algebra \(Q\) with \(V_sQV_s^*=Q\) for all \(s\).

**Proof.** (1) Linearity and unitality are immediate. If \([T^{ij}_s]_{i,j\le n}\) is positive for every \(s\) and \(\xi\in K^n\), the function \(s\mapsto\sum_{i,j}\langle T^{ij}_s\xi_j,\xi_i\rangle\) is nonnegative, so its mean is nonnegative: the amplification is positive. The module and translation rules follow by applying \(m\) to \(\langle T_sB\xi,A^*\eta\rangle\) and to translates.

(2) For \(c\in Q'\), (1) gives \(c\,(m_sT_s)=m_s(cT_s)=m_s(T_sc)\)\(=(m_sT_s)\,c\). So \(m_sT_s\in Q''=Q\) by the bicommutant theorem.

(3) \(|\langle(m_sT_s-T)\xi,\eta\rangle|\)\(=|m(s\mapsto\langle(T_s-T)\xi,\eta\rangle)|\)\(\le a\|\xi\|\|\eta\|\), because a state satisfies \(|m(f)|\le\|f\|_\infty\). For matrices use vectors in \(K^q\) and \(K^p\).

(4) \(E_V\) is UCP by (1). For \(t\in\mathbb R\), \(V_tE_V(T)V_t^*=m_sV_{t+s}TV_{t+s}^*=E_V(T)\) by the translation rule. If \(T\) commutes with all \(V_s\), every term equals \(T\). The last assertion is (2). \(\square\)

## 3. Two perturbation theorems

The following two results are used without proof in this course; both have freely available proofs.

A von Neumann algebra is *injective* when it is injective as a C\*-algebra, as in [Injective von Neumann algebras](course:injective-factors/injective-von-neumann-algebras); [CCSSWW] calls such algebras amenable. Abelian von Neumann algebras, von Neumann algebras of type I (for instance \(B(L)\) and copies of it) and von Neumann algebras generated by an increasing family of finite-dimensional unital \(*\)-subalgebras are injective (Corollary 5.2 there).

**Theorem 3.1** (Christensen's theorem on injective near inclusions [CCSSWW, Theorem 3.3(i)]). Let \(R,Q\subseteq B(H)\) be unital von Neumann algebras with \(R\) injective. If \(R\subset_\gamma Q\) with \(\gamma<1/100\), there is a unitary \(v\in(R\cup Q)''\) such that
\[
vRv^*\subseteq Q,\qquad\|v-I\|\le150\gamma .
\]
If moreover \(Q\subset_\gamma R\) and \(\gamma<1/101\), the same conclusion holds with \(vRv^*=Q\).

The unitary lies in the von Neumann algebra generated by \(R\) and \(Q\); so every operator commuting with both \(R\) and \(Q\) commutes with \(v\). This is used repeatedly.

For a bilinear map \(b:P\times P\to P\) on a von Neumann algebra, let \(\|b\|_{\rm cb}\) be the least \(K\in[0,\infty]\) such that, for all sizes \(p,r,q\),
\[
\Bigl\|\Bigl[\textstyle\sum_{j=1}^rb(x_{ij},y_{jk})\Bigr]_{i,k}\Bigr\|\le K\|X\|\|Y\|
\]
for \(X=[x_{ij}]\in M_{p,r}(P)\) and \(Y=[y_{jk}]\in M_{r,q}(P)\). This is the completely bounded norm of the linear map that \(b\) induces on the Haagerup tensor product \(P\otimes_hP\), whose matrix norms are the infima of \(\|X\|\|Y\|\) over such factorizations. The product \(m_P(x,y)=xy\) has \(\|m_P\|_{\rm cb}=1\).

**Theorem 3.2** (Ricard–Roydor [RR, Proposition 3.2]). Let \(P\) be a von Neumann algebra and \(m:P\times P\to P\) an associative bilinear map with \(\|m-m_P\|_{\rm cb}\le1/11\). There is a completely bounded linear bijection \(L:P\to P\) with
\[
\begin{gathered}
L(m(x,y))=L(x)L(y),\\
\|L-\mathrm{id}_P\|_{\rm cb}\le10\,\|m-m_P\|_{\rm cb}.
\end{gathered}
\]
If \(m(x^*,y^*)=m(y,x)^*\) for all \(x,y\), then \(L\) can be chosen with \(L(x^*)=L(x)^*\).

Johnson and Raeburn–Taylor introduced the cohomological correction of nearby products; [RR] gives the completely bounded version with these constants.

## 4. The completely positive criterion

**Proposition 4.1** (UCP criterion). Let \(P\) be a von Neumann algebra, \(\rho:P\to B(H)\) a faithful normal representation, and \(Q\subseteq B(H)\) a unital von Neumann algebra. Suppose that \(F:P\to Q\) is UCP and
\[
\begin{aligned}
&\|F-\rho\|_{\rm cb}\le e<10^{-3},\\
&\sup_{y\in Q_1}\operatorname{dist}(y,\rho(P)_1)\le g,\qquad g+e<1 .
\end{aligned}
\]
Then there are a normal \(*\)-isomorphism \(\theta:P\to Q\) and a unitary \(u\in B(H)\) with
\[
\begin{aligned}
&\|\theta-\rho\|_{\rm cb}\le32e,\\
&u\rho(x)u^*=\theta(x)\ (x\in P),\\
&\|u-I\|\le32e .
\end{aligned}
\]
In particular \(u\rho(P)u^*=Q\). The map \(F\) is not assumed to be normal.

**Proof.** *Injectivity and surjectivity.* An injective \(*\)-homomorphism is isometric at every matrix level, so \(\|F_n(X)\|\ge\|\rho_n(X)\|-e\|X\|\)\(=(1-e)\|X\|\) for \(X\in M_n(P)\). Hence \(F\) is injective, its range \(V\) is closed, and the inverse \(F^{-1}:V\to P\) has \(\|F^{-1}\|_{\rm cb}\le(1-e)^{-1}\). Let \(y\in Q_1\) and \(\eta>0\); choose \(x\in P_1\) with \(\|y-\rho(x)\|\le g+\eta\). Then \(\|y-F(x)\|\le g+e+\eta\), so \(\operatorname{dist}(y,V)\le g+e\) for every \(y\in Q_1\). If \(V\ne Q\), pick \(z\in Q\setminus V\), \(\vartheta\in(g+e,1)\), and \(v\in V\) with \(\|z-v\|<\operatorname{dist}(z,V)/\vartheta\); then \(y=(z-v)/\|z-v\|\in Q_1\) has \(\operatorname{dist}(y,V)>\vartheta\), a contradiction. So \(F:P\to Q\) is a linear bijection.

*The transported product.* Put \(m(x,y)=F^{-1}(F(x)F(y))\) for \(x,y\in P\). It is associative, because \(F(m(m(x,y),z))\)\(=F(x)F(y)F(z)\)\(=F(m(x,m(y,z)))\). Since \(F\) preserves adjoints, \(F(m(y^*,x^*))=(F(x)F(y))^*\)\(=F(m(x,y)^*)\), so \(m(x^*,y^*)=m(y,x)^*\). For rectangular \(X\in M_{p,r}(P)\) and \(Y\in M_{r,q}(P)\), with \(F\) and \(\rho\) applied entrywise,
\[
\begin{aligned}
&F(XY)-F(X)F(Y)\\
&\quad=\bigl(F(XY)-\rho(XY)\bigr)\\
&\qquad+\bigl(\rho(X)-F(X)\bigr)\rho(Y)\\
&\qquad+F(X)\bigl(\rho(Y)-F(Y)\bigr),
\end{aligned}
\]
using \(\rho(XY)=\rho(X)\rho(Y)\). Each term has norm at most \(e\|X\|\|Y\|\), because \(F\) is completely contractive and \(\rho\) completely isometric. The matrix \([\sum_jm(x_{ij},y_{jk})]-XY\) is \(F^{-1}\) applied entrywise to \(F(X)F(Y)-F(XY)\), so
\[
q:=\|m-m_P\|_{\rm cb}\le\frac{3e}{1-e}<\frac1{11}.
\]

*Correction.* Theorem 3.2 gives an adjoint-preserving linear bijection \(L\) with \(L(m(x,y))=L(x)L(y)\) and \(\|L-\mathrm{id}\|_{\rm cb}\le\lambda:=30e/(1-e)<1\). The Neumann series gives \(\|L^{-1}-\mathrm{id}\|_{\rm cb}\le\lambda/(1-\lambda)\). Put \(\theta=F\circ L^{-1}:P\to Q\), a linear bijection preserving adjoints. For \(a=L(x)\) and \(b=L(y)\),
\[
\begin{aligned}
\theta(ab)&=\theta(L(m(x,y)))\\
&=F(m(x,y))=F(x)F(y)\\
&=\theta(a)\theta(b).
\end{aligned}
\]
So \(\theta\) is a \(*\)-isomorphism of algebras, hence unital, and it is normal by [Corollary 11.4](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras#OA-FND-WA-18). Since \(F\) is completely contractive,
\[
\begin{aligned}
&\|\theta-\rho\|_{\rm cb}\\
&\quad\le\|F(L^{-1}-\mathrm{id})\|_{\rm cb}+\|F-\rho\|_{\rm cb}\\
&\quad\le\frac{30e}{1-31e}+e\le32e,
\end{aligned}
\]
where \(30/(1-31e)<31\) for \(e<10^{-3}\).

*Implementation.* Lemma 3.3 of [Close operator algebras](close-operator-algebras.md), applied to the normal representations \(\rho\) and \(\theta\) with \(32e<2\), gives the unitary \(u\). \(\square\)

The proof shows why only the ordinary reverse gap is needed: it supplies surjectivity, while all multiplicative information comes from the completely bounded estimate for \(F\). Proposition 4.1 is used to descend from crossed products and tensor products, and to convert pointwise weak limits of conjugations into spatial isomorphisms.

## 5. Tensor products

**Lemma 5.1** (tensor gaps). Let \(A,B\subseteq B(H)\) be unital von Neumann algebras with \(d_{\rm cb}(A,B)\le\gamma\), and let \(K\) be a separable Hilbert space.

1. \(d_{\rm cb}(A\bar\otimes B(K),B\bar\otimes B(K))\le\gamma\).
2. If \(D\subseteq B(K)\) is a von Neumann algebra whose commutant \(D'\) is generated, as a von Neumann algebra, by an increasing sequence \(F_1\subseteq F_2\subseteq\cdots\) of finite-dimensional unital \(*\)-subalgebras, then \(d_{\rm cb}(A\bar\otimes D,B\bar\otimes D)\le\gamma\).

**Proof.** (1) If \(\dim K=k<\infty\), then \(M_n(A\bar\otimes B(K))=M_{nk}(A)\) and the claim is part of the hypothesis. Otherwise let \((\varepsilon_j)_{j\ge1}\) be an orthonormal basis of \(K\) and \(p_r\) the projection onto the span of \(\varepsilon_1,\dots,\varepsilon_r\). An operator on \(H\otimes K\) lies in \(A\bar\otimes B(K)\) exactly when its matrix entries relative to the basis lie in \(A\) (Proposition 7.1 of the tensor product lesson). Let \(X\in M_n(A\bar\otimes B(K))_1\) and \(P_r=(1\otimes p_r)^{(n)}\). The compression \(X_r=P_rXP_r\) is an element of \(M_{nr}(A)_1\), so there is \(Y_r\in M_{nr}(B)_1\) with \(\|X_r-Y_r\|\le\gamma+1/r\); regard \(Y_r\) as an element of \(M_n(B\bar\otimes B(K))_1\) supported by \(P_r\). As \(r\to\infty\), \(X_r\to X\) strongly. A subnet of \((Y_r)\) converges in WOT to some \(Y\), which lies in the WOT closed set \(M_n(B\bar\otimes B(K))_1\), and \(\|X-Y\|\le\gamma\) because norm balls are WOT closed. Exchange \(A\) and \(B\).

(2) Let \(X\in M_n(A\bar\otimes D)_1\) and \(\eta>0\). By (1) there is \(Y\in M_n(B\bar\otimes B(K))_1\) with \(\|X-Y\|\le\gamma+\eta\). For each \(j\) let \(\mu_j\) be the Haar probability measure of the compact group \(\mathcal U(F_j)\), put \(W_w=(1\otimes w)^{(n)}\), and
\[
Y_j=\int_{\mathcal U(F_j)}W_wYW_w^*\,d\mu_j(w).
\]
The integrand is norm continuous, because \(F_j\) is finite-dimensional, so \(Y_j\) lies in the norm closed convex hull of the conjugates \(W_wYW_w^*\). These conjugates lie in \(M_n(B\bar\otimes B(K))_1\), because \(1\otimes w\in B\bar\otimes B(K)\). The operator \(X\) commutes with every \(W_w\), since \(1\otimes D'\) commutes with \(B(H)\bar\otimes D\). Hence \(X-Y_j=\int W_w(X-Y)W_w^*\,d\mu_j(w)\) has norm at most \(\gamma+\eta\). Invariance of the Haar measure shows that \(Y_j\) commutes with \(1\otimes F_j\), hence with \(1\otimes F_i\) for \(i\le j\). A WOT cluster point \(Y_\infty\) of \((Y_j)\) lies in \(M_n(B\bar\otimes B(K))_1\), satisfies \(\|X-Y_\infty\|\le\gamma+\eta\), and commutes with \(1\otimes F_i\) for every \(i\), hence with \(1\otimes D'\). Its entries therefore lie in
\[
\bigl(B\bar\otimes B(K)\bigr)\cap\bigl(B(H)\bar\otimes D\bigr)=B\bar\otimes D,
\]
where \((1\otimes D')'=B(H)\bar\otimes D\) by Proposition 7.1 with the tensor factors exchanged, and the intersection is [Corollary 11.5(2)](course:tensor-products-of-operator-algebras/spatial-tensor-products-of-von-neumann-algebras#11-the-commutation-theorem-and-its-consequences). Since \(\eta\) was arbitrary, \(\operatorname{dist}(X,M_n(B\bar\otimes D)_1)\le\gamma\). Exchange \(A\) and \(B\). \(\square\)

## 6. Exercises

**Exercise 6.1.** Show that the mean \(m\) of Proposition 2.1 vanishes on the indicator function of every finite set. Conclude that \(m\) is not a weighted sum \(f\mapsto\sum_tc_tf(t)\) with \(c_t\ge0\) and \(\sum_tc_t=1\).

**Exercise 6.2.** Show that the reverse gap hypothesis in Proposition 4.1 cannot be dropped: give a unital von Neumann algebra \(P\subsetneq Q\) on a finite-dimensional space for which the inclusion \(F=\rho\) satisfies the other hypotheses with \(e=0\).

**Exercise 6.3.** In the proof of Proposition 4.1, show that \(m(1,x)=m(x,1)=x\) and that \(L(1)=1\).

**Exercise 6.4.** Let \(s\mapsto V_s\) be a unitary representation of \(\mathbb R_d\) and \(T\) an operator commuting with all \(V_s\) up to a uniformly small error, \(\|V_sTV_s^*-T\|\le a\) for all \(s\). Show that \(\|E_V(T)-T\|\le a\).

**Exercise 6.5.** Show that \(d(A\otimes1,B\otimes1)=d(A,B)\) for unital C\*-algebras \(A,B\subseteq B(H)\), where \(A\otimes1=\{x\otimes1:x\in A\}\subseteq B(H\otimes K)\) and \(K\ne0\).

## 7. Solutions

**Solution 6.1.** If \(S\) is finite, choose \(t_1,\dots,t_k\) with \(S+t_1,\dots,S+t_k\) pairwise disjoint. Then \(\sum_l1_{S+t_l}\le1\), and invariance gives \(k\,m(1_S)\le1\) for every \(k\), so \(m(1_S)=0\). A weighted sum would give \(c_t=m(1_{\{t\}})=0\) for every \(t\), contradicting \(\sum_tc_t=1\).

**Solution 6.2.** Take \(H=\mathbb C^2\), \(P=\mathbb C1\), \(Q=M_2(\mathbb C)\) and \(\rho=F\) the inclusion. Then \(\|F-\rho\|_{\rm cb}=0\), but \(\operatorname{dist}(y,\mathbb C1)=1\) for the self-adjoint unitary \(y=\operatorname{diag}(1,-1)\), so \(g\ge1\) and \(g+e<1\) fails. No unitary conjugates \(\mathbb C1\) onto \(M_2(\mathbb C)\).

**Solution 6.3.** \(F(1)=1\) gives \(F(m(1,x))=F(1)F(x)=F(x)\), and \(F\) is injective. Then \(L(x)=L(m(1,x))=L(1)L(x)\) for all \(x\); since \(L\) is onto, \(L(1)\) is a left unit of \(P\), hence \(L(1)=1\).

**Solution 6.4.** Apply Lemma 2.2(3) to the family \(T_s=V_sTV_s^*\).

**Solution 6.5.** The map \(x\mapsto x\otimes1\) is a \(*\)-isomorphism of \(B(H)\) onto \(B(H)\otimes1\), hence isometric, and it carries \(A_1\) and \(B_1\) onto \((A\otimes1)_1\) and \((B\otimes1)_1\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
- [CCSSWW] J. Cameron, E. Christensen, A. M. Sinclair, R. R. Smith, S. White, A. D. Wiggins, Kadison–Kastler stable factors, Duke Mathematical Journal 163 (2014), 2639–2686; Theorem 3.3 in arXiv version 3. https://arxiv.org/abs/1209.4116v3
- [RR] É. Ricard, J. Roydor, A noncommutative Amir–Cambern theorem for von Neumann algebras and nuclear C\*-algebras, Journal of Functional Analysis 267 (2014), 1121–1136; Proposition 3.2 in arXiv version 2. https://arxiv.org/abs/1108.1970v2
