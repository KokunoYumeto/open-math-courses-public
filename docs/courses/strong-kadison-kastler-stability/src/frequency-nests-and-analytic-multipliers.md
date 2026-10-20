# Frequency nests and analytic multipliers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The next lesson turns the separated modular cuts of [Rescaled Tomita graphs](rescaled-tomita-graphs.md) into exact normalizers. Its analytic engine is collected here. A *nest* is a totally ordered family of projections, and its *nest algebra* consists of the operators leaving every range invariant. Arveson's distance formula computes the distance of an operator to a nest algebra from the norms of its lower-left corners (Theorem 2.1); we prove it from Parrott's completion lemma. On \(L^2(\mathbb R,H)\), the spectral projections of the frequency define a nest, and a multiplication operator that leaves the positive-frequency subspace invariant is the boundary value of a bounded holomorphic function on the upper half-plane (Lemma 3.1). Averaging over characters then shows that a multiplication operator with a small lower-left corner is close to such an analytic multiplier (Proposition 4.2) [OpenAI-289, Section 7].

We use: [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Proposition 2.1 and Lemma 2.2, the invariant mean on \(\mathbb R_d\) and operator means); the [weak compactness of the unit ball of \(B(H)\)](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-10); the [Plancherel theorem on the real line](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies#OA-FND-LT-17); and, from [Spatial tensor products of von Neumann algebras](course:tensor-products-of-operator-algebras/spatial-tensor-products-of-von-neumann-algebras#7-tensor-products-with-b-k-commutants-and-matrix-units), Proposition 7.1 and Example 7.2 (\(L^\infty(\mathbb R)\) is its own commutant on \(L^2(\mathbb R)\)).

## 1. Parrott's completion lemma

For a contraction \(A\) put \(D_A=(1-A^*A)^{1/2}\). Polynomial approximation of the square root gives \(AD_A=D_{A^*}A\).

**Lemma 1.1** (Parrott). Let \(A:K_1\to L_1\), \(B:K_2\to L_1\) and \(C:K_1\to L_2\) be bounded operators between Hilbert spaces. There is \(X:K_2\to L_2\) with
\[
\begin{aligned}
&\left\|\begin{pmatrix}A&B\\C&X\end{pmatrix}\right\|\\
&\quad =\max\Bigl\{\bigl\|[\,A\ B\,]\bigr\|,\ \Bigl\|\begin{pmatrix}A\\C\end{pmatrix}\Bigr\|\Bigr\}.
\end{aligned}
\]

**Proof.** The left side is at least the right side for every \(X\). Let \(\mu\) be the right side; if \(\mu=0\) take \(X=0\), and otherwise scale so that \(\mu=1\). Then \(C^*C\le1-A^*A=D_A^2\), so \(\|C\xi\|\le\|D_A\xi\|\) and \(Y(D_A\xi)=C\xi\) defines a contraction on the range of \(D_A\); extend it by continuity and by \(0\) on the orthogonal complement, so that \(C=YD_A\) with \(\|Y\|\le1\). In the same way \(BB^*\le D_{A^*}^2\) gives \(B=D_{A^*}Z\) with \(\|Z\|\le1\). Put \(X=-YA^*Z\). Then
\[
\begin{aligned}
\begin{pmatrix}A&B\\C&X\end{pmatrix}
&=\begin{pmatrix}1&0\\0&Y\end{pmatrix}
\begin{pmatrix}A&D_{A^*}\\D_A&-A^*\end{pmatrix}\\
&\qquad\cdot\begin{pmatrix}1&0\\0&Z\end{pmatrix}.
\end{aligned}
\]
The middle operator \(V\) satisfies \(V^*V=1\): its entries are \(A^*A+D_A^2=1\), \(A^*D_{A^*}-D_AA^*=0\) and \(D_{A^*}^2+AA^*=1\). So all three factors are contractions. \(\square\)

## 2. Arveson's distance formula

A *nest* in \(B(K)\) is a family \(\mathcal N\) of orthogonal projections, totally ordered by \(\le\), containing \(0\) and \(1\). Its nest algebra is
\[
\begin{gathered}
\operatorname{Alg}\mathcal N=\{X\in B(K):N^\perp XN=0\\
\text{for all }N\in\mathcal N\},
\end{gathered}
\]
where \(N^\perp=1-N\); it is closed in the weak operator topology.

**Theorem 2.1** (Arveson's distance formula). For every nest \(\mathcal N\) and every \(T\in B(K)\),
\[
\operatorname{dist}(T,\operatorname{Alg}\mathcal N)=\sup_{N\in\mathcal N}\|N^\perp TN\| ,
\]
and the distance is attained.

**Proof.** For \(X\in\operatorname{Alg}\mathcal N\), \(N^\perp TN=N^\perp(T-X)N\), so the distance is at least the supremum \(m\).

*Finite nests.* Let \(0=N_0<N_1<\dots<N_k=1\) and \(E_i=N_i-N_{i-1}\). Write operators as \(k\times k\) block matrices \((x_{ij})\) with \(x_{ij}=E_ixE_j\). An operator lies in \(\operatorname{Alg}\mathcal N\) exactly when \(x_{ij}=0\) for \(i>j\), and \(N_j^\perp TN_j\) is the block \(R_j\) of \(T\) with rows \(j+1,\dots,k\) and columns \(1,\dots,j\). So we must choose the blocks of \(T-X\) with \(i\le j\) freely, keeping the given blocks \(t_{ij}\), \(i>j\), so that the norm is at most \(m=\max_j\|R_j\|\). Fill the unknown blocks diagonal by diagonal: first all \((i,i)\), then all \((i,i+1)\), and so on. When the block \((i,j)\) is filled, all blocks with rows \(i,\dots,k\) and columns \(1,\dots,j\) other than \((i,j)\) are already known, and the rectangle with rows \(i+1,\dots,k\) and columns \(1,\dots,j\), and the rectangle with rows \(i,\dots,k\) and columns \(1,\dots,j-1\), are complete. Apply Lemma 1.1 to the rectangle with rows \(i,\dots,k\) and columns \(1,\dots,j\), with the unknown block \((i,j)\) in its upper right corner. The completed rectangle has norm at most the larger of the norms of the two smaller rectangles. These are rectangles \(R_l\) of \(T\) (when \(j=i\)) or rectangles completed at the previous diagonal. By induction every completed rectangle has norm at most \(m\); the last one, rows \(1,\dots,k\) and columns \(1,\dots,k\), is the whole matrix. Empty rows or columns are omitted and have norm \(0\).

*General nests.* For each finite subfamily \(F\subseteq\mathcal N\) containing \(0\) and \(1\), the finite case gives \(X_F\in\operatorname{Alg}F\) with \(\|T-X_F\|\le\max_{N\in F}\|N^\perp TN\|\le m\). Direct the finite subfamilies by inclusion. The \(X_F\) are bounded by \(\|T\|+m\), so a subnet converges in the weak operator topology to some \(X\), with \(\|T-X\|\le m\). For \(N\in\mathcal N\), \(N^\perp X_FN=0\) as soon as \(N\in F\), so \(N^\perp XN=0\), and \(X\in\operatorname{Alg}\mathcal N\). \(\square\)

## 3. The frequency nest and analytic multipliers

Let \(H\) be a separable Hilbert space and \(\mathcal K=L^2(\mathbb R,H)=L^2(\mathbb R)\otimes H\). Use the Fourier–Plancherel transform \(\widehat f(\xi)=(2\pi)^{-1/2}\int e^{-it\xi}f(t)\,dt\) on the first factor, and let
\[
\begin{gathered}
P_a=\text{the projection onto}\\
\{f:\widehat f=0\text{ on }(-\infty,a]\},\qquad a\in\mathbb R .
\end{gathered}
\]
This is the spectral projection \(1_{(a,\infty)}(D)\) of the frequency \(D=-i\,d/dt\). Let \(C_s\) be multiplication by \(e^{ist}\). Since \(\widehat{C_sf}(\xi)=\widehat f(\xi-s)\),
\[
\begin{gathered}
C_s^*P_aC_s=P_{a-s},\\
C_sP_aC_s^*=P_{a+s} .\quad(3.1)
\end{gathered}
\]
The projections \(P_a\) decrease in \(a\); together with \(0\) and \(1\) they form the *frequency nest*.

A *bounded field* is a map \(B:\mathbb R\to B(H)\) with \(t\mapsto\langle B(t)\xi,\eta\rangle\) measurable for all \(\xi,\eta\) and \(\|B\|_\infty=\operatorname{ess\,sup}_t\|B(t)\|<\infty\); \(M_B\) denotes multiplication by \(B\) on \(\mathcal K\). It commutes with every \(C_s\). We say that \(B\) is *analytic* if \(M_B\) maps \(P_0\mathcal K\) into itself.

**Lemma 3.1** (analytic extension). Let \(B\) be an analytic bounded field. Then the formula
\[
\begin{gathered}
B(t+ir)=\int_{\mathbb R}\frac{r\,B(s)}{\pi((t-s)^2+r^2)}\,ds\\
(r>0)\quad(3.2)
\end{gathered}
\]
defines a bounded function on the upper half-plane, holomorphic in operator norm, with \(\|B(z)\|\le\|B\|_\infty\). If \(B\) and \(S\) are analytic bounded fields and \(x\in B(H)\), then \(BxS\) is an analytic bounded field and its extension is \(z\mapsto B(z)xS(z)\).

**Proof.** *The circle.* Let \(\mathbb T\) be the unit circle with normalized measure \(d\theta/2\pi\), and \(w(t)=(t-i)/(t+i)\), which maps \(\mathbb R\) onto \(\mathbb T\setminus\{1\}\) with \(d\theta/2\pi=dt/(\pi(1+t^2))\). The map
\[
(Jf)(t)=\frac{f(w(t))}{\sqrt\pi\,(t+i)}
\]
is therefore a unitary from \(L^2(\mathbb T,H)\) onto \(\mathcal K\). For \(n\ge0\), \(J(w^n\xi)=(t-i)^n(t+i)^{-n-1}\xi/\sqrt\pi\) is, by the binomial expansion of \((t-i)^n=((t+i)-2i)^n\), a combination of the functions \((t+i)^{-m}\xi\), \(1\le m\le n+1\), and
\[
\begin{gathered}
(t+i)^{-m}\\
=\frac{(-i)^m}{(m-1)!}\int_0^\infty u^{m-1}e^{-u}e^{itu}\,du ,
\end{gathered}
\]
so their Fourier transforms vanish on \((-\infty,0)\). For \(n<0\) the functions are combinations of the complex conjugates \((t-i)^{-m}\), whose transforms vanish on \((0,\infty)\). Since the \(w^n\xi_k\), for an orthonormal basis \((\xi_k)\) of \(H\), form an orthonormal basis, \(J\) maps the Hardy space \(H^2(\mathbb T,H)\), spanned by the \(w^n\xi\) with \(n\ge0\), onto \(P_0\mathcal K\).

*Fourier coefficients.* Conjugation by \(J\) turns \(M_B\) into multiplication by \(\widetilde B(w(t))=B(t)\) on \(L^2(\mathbb T,H)\). Its Fourier coefficients \(b_n=\int_{\mathbb T}\widetilde B(w)w^{-n}\,d\theta/2\pi\), defined weakly, satisfy \(\|b_n\|\le\|B\|_\infty\). Applying the invariance of \(H^2(\mathbb T,H)\) to the constant functions \(\xi\), the function \(\widetilde B\xi\) lies in \(H^2\), so \(b_n=0\) for \(n<0\). Then
\[
F(w)=\sum_{n\ge0}b_nw^n\qquad(|w|<1)
\]
converges in operator norm, locally uniformly, and is holomorphic. Since the negative coefficients vanish, \(F(w)\) is the Poisson integral \(\int P_w\widetilde B\,d\theta/2\pi\), whose kernel \(P_w(e^{i\theta})=(1-|w|^2)/|e^{i\theta}-w|^2\) is positive with integral one; testing on vectors gives \(\|F(w)\|\le\|B\|_\infty\). For \(z=t+ir\) and \(w_0=w(z)\), a direct computation gives \(1-|w_0|^2=4r/|z+i|^2\) and \(|w(s)-w_0|^2\)\(=4|s-z|^2/(|s+i|^2|z+i|^2)\), so the Poisson measure of \(w_0\) pulls back to \(r\,ds/(\pi((t-s)^2+r^2))\). Hence \(B(z)=F(w(z))\) is given by (3.2).

*Products.* \(M_{BxS}=M_B(1\otimes x)M_S\) leaves \(P_0\mathcal K\) invariant, since \(1\otimes x\) commutes with the Fourier transform in \(t\). Its circle coefficients are computed by Parseval's identity in \(L^2(\mathbb T,H)\): for \(\xi,\eta\in H\),
\[
\begin{aligned}
&\int_{\mathbb T}\langle x\widetilde S(w)\xi,\widetilde B(w)^*\eta\rangle w^{-n}\,\frac{d\theta}{2\pi}\\
&\quad =\sum_{k+l=n}\langle b_kxs_l\xi,\eta\rangle ,
\end{aligned}
\]
because \(w^{-n}x\widetilde S\xi\) has coefficients \(xs_{m+n}\xi\) and \(\widetilde B^*\eta\) has coefficients \(b_{-m}^*\eta\). These are the Taylor coefficients of \(F_B(w)\,x\,F_S(w)\), so the extension of \(BxS\) is \(B(z)xS(z)\). \(\square\)

## 4. Averaging over characters

**Lemma 4.1** (decomposable operators). An operator on \(\mathcal K\) commutes with every \(C_s\) exactly when it is \(M_F\) for a bounded field \(F\); then \(\|M_F\|=\|F\|_\infty\).

**Proof.** Let \(X\) commute with all \(C_s\). The set of \(\varphi\in L^\infty(\mathbb R)\) for which multiplication by \(\varphi\otimes1\) commutes with \(X\) is a weak\* closed subspace containing the characters. An \(L^1\) function annihilating all characters has zero Fourier transform and vanishes, so the characters span a weak\* dense subspace, and \(X\) commutes with \(L^\infty(\mathbb R)\otimes1\). For an orthonormal basis \((\xi_k)\) of \(H\), the compressions \(X_{kl}\) of \(X\) to the copies \(L^2(\mathbb R)\otimes\xi_l\to L^2(\mathbb R)\otimes\xi_k\) commute with \(L^\infty(\mathbb R)\), so they are multiplications by functions \(x_{kl}\in L^\infty\) (Example 7.2 of the tensor product lesson). For finite rational combinations \(\xi,\eta\) of the basis, the function \(a(t)=\sum_{k,l}x_{kl}(t)\xi^l\bar\eta^k\) satisfies \(|\int af\bar g\,dt|=|\langle X(f\otimes\xi),g\otimes\eta\rangle|\)\(\le\|X\|\|\xi\|\|\eta\|\|f\|_2\|g\|_2\) for all \(f,g\), so \(|a|\le\|X\|\|\xi\|\|\eta\|\) almost everywhere. Off one null set these coefficients define operators \(F(t)\) with \(\|F(t)\|\le\|X\|\), and \(X=M_F\). The converse and \(\|M_F\|\le\|F\|_\infty\) are immediate. \(\square\)

**Proposition 4.2** (approximation by analytic multipliers). For every bounded field \(F\) there is an analytic bounded field \(G\) with
\[
\|F-G\|_\infty\le\|(1-P_0)M_FP_0\| .
\]

**Proof.** By (3.1), and since \(M_F\) commutes with \(C_a\), \(C_a^*(1-P_a)M_FP_aC_a=(1-P_0)M_FP_0\); so \(\sup_a\|(1-P_a)M_FP_a\|=h:\)\(=\|(1-P_0)M_FP_0\|\). Theorem 2.1 gives \(T\) in the nest algebra of the frequency nest with \(\|M_F-T\|\le h\). With the invariant mean of Proposition 2.1 of the averaging lesson put \(E(T)=m_sC_sTC_s^*\). By (3.1), each \(C_sTC_s^*\) lies in the nest algebra, and so does the mean: for every \(a\) and vectors \(\xi,\eta\),
\[
\begin{aligned}
&\langle(1-P_a)E(T)P_a\xi,\eta\rangle\\
&\quad=m\bigl(s\mapsto\langle C_sTC_s^*P_a\xi,(1-P_a)\eta\rangle\bigr)\\
&\quad=0 .
\end{aligned}
\]
The mean commutes with every \(C_s\), so \(E(T)=M_G\) for a bounded field \(G\) by Lemma 4.1, and \(G\) is analytic. Finally \(C_sM_FC_s^*=M_F\), so by Lemma 2.2(3) of the averaging lesson \(\|M_G-M_F\|\le\|T-M_F\|\le h\), and \(\|F-G\|_\infty=\|M_F-M_G\|\). \(\square\)

For scalar fields Proposition 4.2 is Nehari's theorem: the distance from a bounded function to the bounded analytic functions is at most the norm of its Hankel operator.

## 5. Exercises

**Exercise 5.1.** Check the identity \(AD_A=D_{A^*}A\) and the three entries of \(V^*V\) in the proof of Lemma 1.1.

**Exercise 5.2.** For the nest \(\{0,N,1\}\) with one nontrivial projection, show directly that \(\operatorname{dist}(T,\operatorname{Alg}\mathcal N)=\|N^\perp TN\|\).

**Exercise 5.3.** Verify \(d\theta/2\pi=dt/(\pi(1+t^2))\) for \(e^{i\theta}=(t-i)/(t+i)\), and the formula for \((t+i)^{-m}\) as an integral.

**Exercise 5.4.** Show that the field \(B(t)=(t-i)/(t+i)\), times the identity of \(H\), is analytic and compute its extension.

**Exercise 5.5.** Let \(F(t)=(t+i)/(t-i)\), times the identity. Show that \(\|(1-P_0)M_FP_0\|=1\), and that no analytic field \(G\) has \(\|F-G\|_\infty<1\).

## 6. Solutions

**Solution 5.1.** \(A(A^*A)^n=(AA^*)^nA\), hence \(Ap(A^*A)=p(AA^*)A\) for polynomials \(p\), and by uniform approximation \(Af(A^*A)=f(AA^*)A\) for continuous \(f\) on \([0,1]\); take \(f(s)=(1-s)^{1/2}\). The entries of \(V^*V\) are \(A^*A+D_A^2\), \(A^*D_{A^*}-D_AA^*\), its adjoint, and \(D_{A^*}^2+AA^*\).

**Solution 5.2.** Here \(\operatorname{Alg}\mathcal N\) consists of the block upper triangular operators for \(K=NK\oplus N^\perp K\). Subtracting from \(T\) the operator with the same blocks except the lower left one leaves the matrix with only the block \(N^\perp TN\).

**Solution 5.3.** \(\frac{d}{dt}\frac{t-i}{t+i}=\frac{2i}{(t+i)^2}\) has modulus \(2/(1+t^2)\). For the integral, \(\int_0^\infty u^{m-1}e^{-u(1-it)}\,du\)\(=(m-1)!/(1-it)^m\) and \(1-it=-i(t+i)\).

**Solution 5.4.** \(B=w(t)\) corresponds under \(J\) to multiplication by \(w\) on the circle, which preserves \(H^2(\mathbb T,H)\). Its extension is \(B(z)=(z-i)/(z+i)\).

**Solution 5.5.** On the circle, \(F\) is \(\bar w\). The vector \(J(1)\) lies in \(P_0\mathcal K\) and \(M_FJ(1)=J(\bar w)\) is orthogonal to \(P_0\mathcal K\), so the corner has norm \(1\). An analytic \(G\) corresponds to a bounded field \(\widetilde G\) on the circle with vanishing negative coefficients. For a unit vector \(\xi\in H\), \(\widetilde G\xi\) lies in \(H^2(\mathbb T,H)\) and is orthogonal to \(\bar w\xi\), so \(\langle(\bar w-\widetilde G)\xi,\bar w\xi\rangle=1\) in \(L^2(\mathbb T,H)\), and \(\|F-G\|_\infty\ge\|(\bar w-\widetilde G)\xi\|_2\ge1\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
