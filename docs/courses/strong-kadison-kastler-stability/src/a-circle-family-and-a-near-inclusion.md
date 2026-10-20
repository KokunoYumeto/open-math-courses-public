# A circle family and a near inclusion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

If a unitary \(u\) satisfies \(uMu^*\subseteq N\), then every contraction \(x\in M\) lies within \(2\|u-I\|\) of the element \(uxu^*\) of \(N\), so \(\gamma(M,N)\le2\|u-I\|\). Theorem 2.4 of [Close operator algebras](close-operator-algebras.md) says that the converse fails without a uniform rate: one-sided gaps can tend to \(0\) while every implementing unitary stays far from \(I\). For an injective source algebra \(M\) the converse holds with a linear bound: if \(\gamma(M,N)<\gamma<1/100\), Christensen's theorem gives a unitary \(u\) with \(uMu^*\subseteq N\) and \(\|u-I\|\le150\gamma\) (Theorem 3.1 of [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md)). This lesson and [Almost commuting matrices and small embeddings](almost-commuting-matrices-and-small-embeddings.md) prove Theorem 2.4 [OpenAI-289c].

The idea is to encode a pair of unitary matrices \(U,V\) in a pair of von Neumann algebras. The present lesson builds, for every such pair, algebras \(M\) and \(N\) with \(W^*MW\subseteq N\) for an explicit unitary \(W\), and
\[
\gamma(M,N)\le C\,\|UV-VU\|
\]
with an absolute constant \(C\) (Proposition 3.2). The next lesson shows that, for Voiculescu's almost commuting matrices, a unitary \(u\) with \(uMu^*\subseteq N\) and \(\|u-I\|\) small would produce a commuting pair of unitaries near \((U,V)\), which does not exist.

The encoding needs representations of the free group that depend on a point \(z\) of the unit circle through Fourier coefficients with uniformly summable moments, so that \(z\) can be replaced by a unitary matrix (Section 1). They come from the deformation of [A free-group deformation and close separable algebras](a-free-group-deformation-and-close-separable-algebras.md) by a twist along the homomorphism that counts generators.

We use: [Close operator algebras](close-operator-algebras.md) (Definition 1.2); [A free-group deformation and close separable algebras](a-free-group-deformation-and-close-separable-algebras.md) (Lemmas 2.1 and 4.1, and the formulas for \(T\) in the proof of Proposition 2.2); and the [double commutant theorem](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem#OA-FND-BI-06).

## 1. A circle family of representations

Let \(F\) be the free group on \(s_1,s_2,\dots\), let \(K=\ell^2(F)\) with basis \((\delta_x)\), and let \(\lambda_F,\rho_F\) be the left and right regular representations of \(F\). Let \(p_e\) be the projection onto \(\mathbb C\delta_e\) and \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). Fix \(0<t<1\) and \(r=\sqrt{1-t^2}\), and let \(\pi_t\) and the vectors \(\xi_x\) be as in Lemma 2.1 of [A free-group deformation and close separable algebras](a-free-group-deformation-and-close-separable-algebras.md), with \(F\) in place of the group called \(G\) there.

**Lemma 1.1.** Let \(g\in F\) have prefixes \(g_0=e,g_1,\dots,g_l=g\), let \(M_g\) be the span of \(f_a=\delta_{g_a}\) for \(0\le a\le l\), and let \(T_g=\pi_t(g)\lambda_F(g)^*\). Then \(T_g\) is the identity on \(M_g^\perp\), maps \(M_g\) into itself, and
\[
|\langle T_gf_b,f_a\rangle|\le t^{|a-b|}\qquad(0\le a,b\le l).
\]

**Proof.** For \(g=e\), \(T_g=I\). Otherwise the proof of Proposition 2.2 of that lesson gives \(T_g\delta_y=\delta_y\) for \(y\) not a prefix of \(g\), \(T_gf_b=r\xi_{g_b}-tf_{b+1}\) for \(b<l\), and \(T_gf_l=\xi_g\), where
\[
\xi_{g_b}=t^bf_0+r\sum_{a=1}^bt^{b-a}f_a .
\]
So the nonzero entries of column \(b\) are \(rt^b\) or \(t^l\) in row \(0\), \(r^2t^{b-a}\) or \(rt^{l-a}\) in rows \(1\le a\le b\), and \(-t\) in row \(b+1\). Since \(r\le1\), each has absolute value at most \(t^{|a-b|}\). \(\square\)

Let \(q:F\to\mathbb Z\) be the homomorphism with \(q(s_j)=1\) for all \(j\), and for \(z\in\mathbb T\) let \(D_z\) be the diagonal unitary \(D_z\delta_x=z^{-q(x)}\delta_x\). Put
\[
c_0=\frac{1+t}{1-t},\qquad c_k=\frac{2t^{|k|}}{1-t}\quad(k\ne0).
\]

**Proposition 1.2** (the circle family). For \(z\in\mathbb T\) and \(g\in F\) put
\[
\pi_z(g)=z^{q(g)}D_z\pi_t(g)D_z^* .
\]

1. Each \(\pi_z\) is a unitary representation of \(F\).
2. There are operators \(A_k(g)\), for \(k\in\mathbb Z\) and \(g\in F\), not depending on \(z\), with \(A_k(g)=0\) for \(|k|>|g|\), \(\|A_k(g)\|\le c_k\), and
\[
\pi_z(g)=\sum_{k\in\mathbb Z}z^kA_k(g).
\]
3. \(\pi_z(s_j)\delta_e=tz\delta_e+r\delta_{s_j}\), and \(\pi_z(s_j)\to tz\,p_e\) in the weak operator topology as \(j\to\infty\).

**Proof.** (1) \(g\mapsto z^{q(g)}\) is a homomorphism into \(\mathbb T\), and \(g\mapsto D_z\pi_t(g)D_z^*\) is a unitary representation; their product is one.

(2) Since \(D_z\lambda_F(g)D_z^*\delta_x=z^{q(x)-q(gx)}\delta_{gx}\)\(=z^{-q(g)}\lambda_F(g)\delta_x\),
\[
\pi_z(g)=\bigl(D_zT_gD_z^*\bigr)\lambda_F(g).
\]
The diagonal unitary \(D_z\) preserves \(M_g\) and \(M_g^\perp\), so \(D_zT_gD_z^*\) is the identity on \(M_g^\perp\), and on \(M_g\) its entry in row \(a\), column \(b\) is \(z^{q(g_b)-q(g_a)}\langle T_gf_b,f_a\rangle\). Consecutive prefixes differ by one letter, so \(|q(g_b)-q(g_a)|\le|a-b|\). Let \(B_k(g)\) be the operator whose matrix on \(M_g\) keeps the entries with \(q(g_b)-q(g_a)=k\) and replaces the others by \(0\), plus the identity of \(M_g^\perp\) when \(k=0\). Then \(D_zT_gD_z^*=\sum_kz^kB_k(g)\), a finite sum, and we put \(A_k(g)=B_k(g)\lambda_F(g)\).

To bound \(\|B_k(g)\|\), recall the Schur test: if every row and every column of a matrix \((m_{ab})\) has \(\sum|m_{ab}|\le\sigma\), then its norm is at most \(\sigma\), because
\[
\begin{aligned}
&\Bigl|\sum_{a,b}m_{ab}x_b\bar y_a\Bigr|\\
&\quad \le\sum_{a,b}|m_{ab}|\,\frac{|x_b|^2+|y_a|^2}2\le\sigma
\end{aligned}
\]
for unit vectors \(x,y\). In a row \(a\) of the matrix of \(B_k(g)\) on \(M_g\), the nonzero entries lie in columns \(b\) with \(|a-b|\ge|k|\); there are at most two columns at each distance \(m\ge1\), one at distance \(0\), and the entries at distance \(m\) are at most \(t^m\) by Lemma 1.1. So the row sums, and likewise the column sums, are at most \(1+2t/(1-t)=c_0\) for \(k=0\) and \(2\sum_{m\ge|k|}t^m=c_k\) for \(k\ne0\). On \(M_g^\perp\), \(B_0(g)\) is the identity and \(c_0\ge1\). Hence \(\|A_k(g)\|=\|B_k(g)\|\le c_k\), and \(B_k(g)=0\) when \(|k|>l\).

(3) The operator \(T_{s_j}\) is the identity off the span of \(\delta_e\) and \(\delta_{s_j}\), and \(T_{s_j}\delta_{s_j}=\xi_{s_j}=t\delta_e+r\delta_{s_j}\). So
\[
\begin{aligned}
\pi_z(s_j)\delta_e&=D_zT_{s_j}D_z^*\delta_{s_j}\\
&=z\,D_z(t\delta_e+r\delta_{s_j})\\
&=tz\delta_e+r\delta_{s_j}.
\end{aligned}
\]
For \(x\ne e\) and all \(j\) with \(s_j\ne x^{-1}\), \(s_jx\notin\{e,s_j\}\), so \(\pi_z(s_j)\delta_x=\delta_{s_jx}\). For fixed \(x,y\in F\), \(\langle\pi_z(s_j)\delta_x,\delta_y\rangle\) therefore tends to \(tz\) if \(x=y=e\) and to \(0\) otherwise, which are the matrix entries of \(tz\,p_e\). The operators \(\pi_z(s_j)\) are unitaries, so convergence of the matrix entries implies weak operator convergence. \(\square\)

The constants enter through the two sums
\[
\begin{gathered}
S_0=\sum_kc_k=\frac{1+t}{1-t}+\frac{4t}{(1-t)^2},\\
S_1=\sum_k|k|\,c_k=\frac{4t}{(1-t)^3}.
\end{gathered}
\]
For \(t=1/2\): \(c_0=3\), \(c_k=2^{2-|k|}\) for \(k\ne0\), \(S_0=11\) and \(S_1=16\).

## 2. Substituting unitary matrices for the circle parameter

Let \(d\ge1\) and let \(U,V\) be unitaries on \(\mathbb C^d\). On \(L=K\otimes K\otimes\mathbb C^d\) define, for \(g\in F\),
\[
\begin{gathered}
a(g)=\sum_kA_k(g)\otimes I\otimes U^k,\\
b(g)=\sum_kI\otimes A_k(g)\otimes V^k .
\end{gathered}
\]
Both sums are finite.

**Lemma 2.1.** \(a\) and \(b\) are unitary representations of \(F\) on \(L\), and as \(j\to\infty\), in the weak operator topology,
\[
\begin{gathered}
a(s_j)\to t\,p_e\otimes I\otimes U,\\
b(s_j)\to t\,I\otimes p_e\otimes V .
\end{gathered}
\]

**Proof.** Write \(U=\sum_zzP_z\), a finite sum over the eigenvalues \(z\in\mathbb T\) of \(U\), with spectral projections \(P_z\). Then \(U^k=\sum_zz^kP_z\), and Proposition 1.2(2) gives
\[
a(g)=\sum_z\pi_z(g)\otimes I\otimes P_z .
\]
The \(P_z\) are pairwise orthogonal with sum \(I\), so \(a\) is a unitary representation because each \(\pi_z\) is one. By Proposition 1.2(3), \(\pi_z(s_j)\otimes I\otimes P_z\to tz\,p_e\otimes I\otimes P_z\) weakly: the matrix entries between elementary tensors converge, and the operators are bounded. Summing over \(z\) gives the limit \(t\,p_e\otimes I\otimes U\). The same argument with the eigenvalues of \(V\) applies to \(b\). \(\square\)

The ranges of \(a\) and \(b\) need not commute (Exercise 4.4); this is the point of the construction. Their failure to commute is controlled by the following elementary estimate.

**Lemma 2.2.** For unitaries \(U,V\) and integers \(m,n\),
\[
\begin{aligned}
&\|U^mV^n-V^nU^m\|\\
&\quad \le|m|\,|n|\,\|UV-VU\| .
\end{aligned}
\]

**Proof.** Write \([X,Y]=XY-YX\) and \(\nu=\|[U,V]\|\). Since \([U^{-1},V]=-U^{-1}[U,V]U^{-1}\), \(\|[U^{\pm1},V]\|=\nu\). For \(m\ge1\), \([U^m,V]=\sum_{i=0}^{m-1}U^i[U,V]U^{m-1-i}\), so \(\|[U^m,V]\|\le m\nu\), and the same holds with \(U^{-1}\) in place of \(U\). Hence \(\|[U^m,V]\|\le|m|\nu\) for every integer \(m\). Applying this to the unitaries \(V\) and \(U^m\) gives \(\|[U^m,V^n]\|\le|n|\,\|[U^m,V]\|\le|m||n|\nu\). \(\square\)

## 3. The two algebras and the near inclusion

Let \(G=F\times F\), \(S=\ell^2(G)\) with basis \((\delta_x)_{x\in G}\), and let \(\lambda,\rho\) be the left and right regular representations of \(G\) on \(S\). On \(H=S\otimes L\), every operator \(T\) has blocks \(T_{x,y}\in B(L)\), defined by \(\langle T_{x,y}v,w\rangle=\langle T(\delta_y\otimes v),\delta_x\otimes w\rangle\). For \(x=(x_1,x_2)\in G\) put
\[
f(x)=a(x_1)\,b(x_2),
\]
a unitary of \(L\), and let \(W\) be the block diagonal unitary of \(H\) with \(W(\delta_x\otimes v)=\delta_x\otimes f(x)v\). Define
\[
\begin{gathered}
M=W\bigl(\lambda(G)''\otimes I_L\bigr)W^*,\\
N=\bigl(\rho(G)\otimes I_L\bigr)',
\end{gathered}
\]
where \(\lambda(G)''\otimes I_L\) denotes the set of operators \(X\otimes I_L\) with \(X\in\lambda(G)''\).

**Lemma 3.1.** \(M\) and \(N\) are von Neumann algebras on \(H\) containing \(I_H\), and \(W^*MW\subseteq N\). An operator \(T\) on \(H\) lies in \(N\) exactly when \(T_{xq,yq}=T_{x,y}\) for all \(x,y,q\in G\).

**Proof.** \(N\) is the commutant of a self-adjoint set, so it is a von Neumann algebra. An operator commuting with all \(I_S\otimes Y\), \(Y\in B(L)\), has the form \(X\otimes I_L\): with matrix units of \(L\) relative to an orthonormal basis, this is the block argument in the proof of Lemma 4.1(1) of [A free-group deformation and close separable algebras](a-free-group-deformation-and-close-separable-algebras.md). It then commutes with \(\lambda(G)'\otimes I_L\) exactly when \(X\in\lambda(G)''\). So \(\lambda(G)''\otimes I_L\) is the commutant of \((\lambda(G)'\otimes I_L)\cup(I_S\otimes B(L))\), a von Neumann algebra, and so is its unitary conjugate \(M\). Since \(\rho(G)\subseteq\lambda(G)'\), every \(X\in\lambda(G)''\) commutes with \(\rho(G)\); so \(W^*MW=\lambda(G)''\otimes I_L\subseteq N\). Finally, \((\rho(q)\otimes I_L)(\delta_y\otimes v)=\delta_{yq^{-1}}\otimes v\), so \(T\) commutes with \(\rho(q)\otimes I_L\) exactly when \(T_{xq^{-1},yq^{-1}}=T_{x,y}\) for all \(x,y\). \(\square\)

So \(M\) is spatially embedded in \(N\) by \(W^*\). The next proposition shows that \(M\) is also nearly included in \(N\) when \(U\) and \(V\) nearly commute.

**Proposition 3.2.** Let \(\nu=\|UV-VU\|\) and \(C=2S_0^2S_1^2\). For every \(X\in\lambda(G)''\) there is \(Y\in N\) with
\[
\bigl\|W(X\otimes I_L)W^*-Y\bigr\|\le C\nu\|X\| .
\]
For \(X=\lambda(g)\), \(g\in G\), one can take \(Y=\lambda(g)\otimes f(g)\). In particular \(\gamma(M,N)\le C\nu\), and \(C=61952\) for \(t=1/2\).

**Proof.** Write \(X_{x,y}=\langle X\delta_y,\delta_x\rangle\). Since \(X\) commutes with \(\rho(G)\), \(X_{xq,yq}=X_{x,y}\) for all \(x,y,q\). The operator \(Z=W(X\otimes I_L)W^*\) has blocks
\[
Z_{x,y}=X_{x,y}\,f(x)f(y)^* .
\]
*Expansion.* Identify \(H\) with \((S\otimes K\otimes K)\otimes\mathbb C^d\). For \(k,m\in\mathbb Z\) let \(\Delta_{k,m}\) be the block diagonal operator on \(S\otimes K\otimes K\) whose block at \(x\) is \(A_k(x_1)\otimes A_m(x_2)\); then \(\|\Delta_{k,m}\|\le c_kc_m\). Put
\[
B_{kmph}=\Delta_{k,m}(X\otimes I_K\otimes I_K)\Delta_{h,p}^*,
\]
so \(\|B_{kmph}\|\le c_kc_mc_pc_h\|X\|\), and the block of \(B_{kmph}\) at \((x,y)\) is
\[
\begin{gathered}
(A_k(x_1)\otimes A_m(x_2))\,X_{x,y}\\
\cdot(A_h(y_1)\otimes A_p(y_2))^* .
\end{gathered}
\]
Expanding \(f(x)=a(x_1)b(x_2)\) and \(f(y)^*=b(y_2)^*a(y_1)^*\),
\[
Z=\sum_{k,m,p,h}B_{kmph}\otimes U^kV^{m-p}U^{-h}.
\]
The series converges absolutely in norm, since \(\sum c_kc_mc_pc_h=S_0^4\). Both sides have the same blocks, because each block of the right side is a finite sum equal to \(Z_{x,y}\); so they are equal.

*The reordered operator.* Define
\[
Y=\sum_{k,m,p,h}B_{kmph}\otimes U^{k-h}V^{m-p},
\]
again absolutely convergent. Collecting terms, its blocks are
\[
\begin{aligned}
Y_{x,y}&=X_{x,y}\,a(x_1)a(y_1)^*\,b(x_2)b(y_2)^*\\
&=X_{x,y}\,f(xy^{-1}),
\end{aligned}
\]
using that \(a\) and \(b\) are representations. Since \((xq)(yq)^{-1}=xy^{-1}\) and \(X_{xq,yq}=X_{x,y}\), Lemma 3.1 gives \(Y\in N\).

*The estimate.* By Lemma 2.2,
\[
\begin{aligned}
&\|U^kV^{m-p}U^{-h}-U^{k-h}V^{m-p}\|\\
&\quad =\|[V^{m-p},U^{-h}]\|\\
&\quad \le|m-p|\,|h|\,\nu .
\end{aligned}
\]
Hence \(\|Z-Y\|\le\nu\|X\|\sum c_kc_mc_pc_h|m-p||h|\). Since \(|m-p|\le|m|+|p|\), the sum is at most \(S_0S_1\cdot2S_0S_1=C\).

For \(X=\lambda(g)\), \(X_{x,y}=1\) if \(x=gy\) and \(0\) otherwise, so \(Y_{x,y}=f(g)\) if \(x=gy\) and \(0\) otherwise; that is, \(Y=\lambda(g)\otimes f(g)\). Finally, every contraction of \(M\) is \(W(X\otimes I_L)W^*\) with \(X\in\lambda(G)''\) and \(\|X\|\le1\), so its distance to \(N\) is at most \(C\nu\). For \(t=1/2\), \(C=2\cdot11^2\cdot16^2=61952\). \(\square\)

If \(U\) and \(V\) commute, then \(f\) is a representation of \(G\), each \(W(\lambda(g)\otimes I_L)W^*=\lambda(g)\otimes f(g)\) lies in \(N\), and \(M\subseteq N\) (Exercise 4.2). Proposition 3.2 is a quantitative form of this, valid on the whole unit ball of \(M\) and not only on the group unitaries.

## 4. Exercises

**Exercise 4.1.** Show that \(\langle\pi_z(g)\delta_e,\delta_e\rangle=z^{q(g)}t^{|g|}\) for \(g\in F\) and \(z\in\mathbb T\).

**Exercise 4.2.** Suppose \(UV=VU\). Show that \(f\) is a unitary representation of \(G\), that \(W(\lambda(g)\otimes I_L)W^*=\lambda(g)\otimes f(g)\), and that \(M\subseteq N\).

**Exercise 4.3.** Show that \(\|\pi_z(s_j)-tz\,p_e\|\ge1\) for every \(j\), so the limit in Proposition 1.2(3) is not a norm limit.

**Exercise 4.4.** For \(v,w\in\mathbb C^d\), show that
\[
\begin{aligned}
&\bigl\langle[a(s_1),b(s_1)]\,\delta_e\otimes\delta_e\otimes v,\ \delta_e\otimes\delta_e\otimes w\bigr\rangle\\
&\quad =t^2\langle(UV-VU)v,w\rangle .
\end{aligned}
\]
Deduce \(\|a(s_1)b(s_1)-b(s_1)a(s_1)\|\)\(\ge t^2\|UV-VU\|\).

**Exercise 4.5.** Show that \(\lambda(G)''\) commutes with \(\rho(G)\) directly from \(\rho(G)\subseteq\lambda(G)'\), and that \(\lambda(g)\otimes f(g)\in N\) for every \(g\in G\) even when \(U\) and \(V\) do not commute.

## 5. Solutions

**Solution 4.1.** \(D_z^*\delta_e=\delta_e\) because \(q(e)=0\), so \(\pi_z(g)\delta_e=z^{q(g)}D_z\xi_g\). Since \(D_z^*\delta_e=\delta_e\), \(\langle D_z\xi_g,\delta_e\rangle=\langle\xi_g,\delta_e\rangle=t^{|g|}\) by Lemma 2.1(1) of [A free-group deformation and close separable algebras](a-free-group-deformation-and-close-separable-algebras.md).

**Solution 4.2.** If \(UV=VU\), then every \(a(g)\) commutes with every \(b(h)\), since \(A_k(g)\otimes I\) and \(I\otimes A_m(h)\) commute and \(U^k\) commutes with \(V^m\). So \(f(xy)=a(x_1y_1)b(x_2y_2)\)\(=a(x_1)b(x_2)a(y_1)b(y_2)\)\(=f(x)f(y)\). For \(g\in G\), \(W(\lambda(g)\otimes I)W^*(\delta_x\otimes v)\)\(=\delta_{gx}\otimes f(gx)f(x)^*v\)\(=\delta_{gx}\otimes f(g)v\). The operator \(\lambda(g)\otimes f(g)\) commutes with \(\rho(G)\otimes I_L\), so it lies in \(N\). By the double commutant theorem, \(\lambda(G)''\) is the weak operator closure of the span of \(\lambda(G)\); the map \(X\mapsto W(X\otimes I_L)W^*\) is weakly continuous and \(N\) is weakly closed, so \(M\subseteq N\).

**Solution 4.3.** For \(x\ne e\), \(p_e\delta_x=0\), so \((\pi_z(s_j)-tz\,p_e)\delta_x=\pi_z(s_j)\delta_x\) is a unit vector.

**Solution 4.4.** From the proof of Lemma 2.1 and Proposition 1.2(3), \(a(s_1)(\delta_e\otimes\eta\otimes v)\)\(=t\,\delta_e\otimes\eta\otimes Uv+r\,\delta_{s_1}\otimes\eta\otimes v\) for every \(\eta\in K\), and similarly for \(b(s_1)\) in the second factor. Applying \(b(s_1)\) and then \(a(s_1)\) to \(\delta_e\otimes\delta_e\otimes v\), the component along \(\delta_e\otimes\delta_e\otimes\mathbb C^d\) is \(t^2\,\delta_e\otimes\delta_e\otimes UVv\); in the other order it is \(t^2\,\delta_e\otimes\delta_e\otimes VUv\). Taking the inner product with \(\delta_e\otimes\delta_e\otimes w\) gives the identity, and the norm bound follows by taking the supremum over unit vectors \(v,w\).

**Solution 4.5.** Every \(\rho(q)\) commutes with \(\lambda(G)\), so \(\rho(q)\in\lambda(G)'\), and every element of \(\lambda(G)''=(\lambda(G)')'\) commutes with \(\rho(q)\). The operator \(\lambda(g)\otimes f(g)\) has blocks \(f(g)\) at the pairs \((gy,y)\) and \(0\) elsewhere; these are invariant under \((x,y)\mapsto(xq,yq)\), so it lies in \(N\) by Lemma 3.1. What fails without commutation is the identity \(W(\lambda(g)\otimes I_L)W^*=\lambda(g)\otimes f(g)\).

## References

- [OpenAI-289c] OpenAI, Near inclusions of von Neumann algebras without small spatial embeddings, preprint, 5 October 2026, Sections 2 and 3. https://github.com/openai/math/tree/main/preprints/Near-Inclusions-of-von-Neumann-Algebras-Without-Small-Spatial-Embeddings-October-5-2026
