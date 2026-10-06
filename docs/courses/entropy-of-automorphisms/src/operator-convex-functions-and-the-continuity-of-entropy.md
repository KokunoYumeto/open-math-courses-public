# Operator convex functions and the continuity of entropy

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

## Introduction

The entropy lessons of this course rest on two analytic tools. The first is the operator concavity of
\(\eta(t)=-t\log t\), together with Jensen's inequality for unital positive maps: \(\eta(\Phi(a))\ge\Phi(\eta(a))\).
The lesson "Entropy of finite-dimensional subalgebras" applies it to conditional expectations. The second is the
continuity of the von Neumann entropy \(S(\rho)=\operatorname{Tr}\eta(\rho)\) in the trace norm, which the lesson
"Entropy of lattice translations in quantum spin chains" uses in its sharp form, the Fannes–Audenaert inequality
\[
|S(\rho)-S(\sigma)|\le T\log(d-1)+\mathrm h(T),\qquad T=\tfrac12\|\rho-\sigma\|_1,\quad
\mathrm h(T)=\eta(T)+\eta(1-T),
\]
for density matrices \(\rho,\sigma\) on \(\mathbb C^d\).

This lesson proves both in full generality. Sections 1–3 develop operator convex functions: the inverse and the
square (Proposition 1.3), the functions \(t\log t\) and \(\log t\) (Theorem 2.2), and the theorem of Hansen and Pedersen
that operator convexity is equivalent to Jensen's operator inequality for isometries, for unital columns of operators
and for unital positive maps between C\*-algebras (Theorem 3.1). Section 4 proves the elementary inequalities for
Shannon entropy that the course uses. Section 5 proves the sharp continuity bound for Shannon entropy by a coupling
argument (Theorem 5.2). Section 6 proves the eigenvalue inequalities of Courant–Fischer, Ky Fan and Mirsky, and Section
7 deduces the Fannes–Audenaert inequality for every value of \(T\) and every dimension, with equality cases (Theorem 7.1).

Logarithms are natural. We put \(\eta(t)=-t\log t\) for \(t>0\), \(\eta(0)=0\), and
\(\mathrm h(t)=\eta(t)+\eta(1-t)\) for \(t\in[0,1]\). Both are continuous and concave, since
\(\eta''(t)=-1/t<0\) on \((0,\infty)\).

## Results used from other lessons

**(R1) Continuous functional calculus.** For a self-adjoint element \(x\) of a unital C\*-algebra \(A\) and a
continuous real function \(f\) on \(\sigma(x)\), \(f\mapsto f(x)\) is an isometric \(*\)-homomorphism of
\(C(\sigma(x))\) into \(A\), with \(f(x)=x\) for \(f(t)=t\), \(\sigma(f(x))=f(\sigma(x))\), and
\(\|f(x)\|=\sup_{\sigma(x)}|f|\). A \(*\)-homomorphism \(\pi\) satisfies \(\pi(f(x))=f(\pi(x))\); in particular
\(f(W^*xW)=W^*f(x)W\) for unitaries \(W\), and \(f(x_1\oplus x_2)=f(x_1)\oplus f(x_2)\). The spectrum of \(x\) is the
same in \(A\) and in every C\*-subalgebra containing \(x\) and the unit. A self-adjoint \(x\) satisfies
\(\alpha\le x\le\beta\) exactly when \(\sigma(x)\subseteq[\alpha,\beta]\); the positive elements form a closed convex
cone, and \(y\le z\) implies \(c^*yc\le c^*zc\). These are [C\*-algebras: continuous functional calculus, Theorem 5.1
and Corollary 5.4](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-07), [Theorem
3.2](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-06) (spectral permanence),
and [Theorem 8.2 and Proposition 8.5](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-15)
there.

**(R2) Hermitian matrices.** A self-adjoint operator \(A\) on \(\mathbb C^d\) has an orthonormal basis of
eigenvectors; we write \(\lambda_1(A)\ge\dots\ge\lambda_d(A)\) for its eigenvalues, repeated by multiplicity. This is
the finite-dimensional case of [The spectral theorem for bounded self-adjoint operators, Section
4](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators#OA-FND-ST-04): the spectral measure is carried by the
finitely many eigenvalues, and its values there are the projections onto the eigenspaces.

**(R3) Positive maps on abelian algebras.** A positive linear map from an abelian C\*-algebra into a C\*-algebra is
completely positive: [Completely positive maps, Theorem 5.4(2)](course:foundations-of-von-neumann-algebras/completely-positive-maps#OA-FND-CM-08).

**(R4) Stinespring's theorem.** If \(\varphi:A\to B(H)\) is completely positive and \(A\) is unital, then
\(\varphi=V^*\pi(\cdot)V\) for a representation \(\pi\) of \(A\) on a Hilbert space \(K\) and \(V\in B(H,K)\) with
\(V^*V=\varphi(1)\): [Completely positive maps, Theorem 6.1](course:foundations-of-von-neumann-algebras/completely-positive-maps#OA-FND-CM-05).

**(R5) Faithful representations.** Every C\*-algebra has a faithful representation on a Hilbert space:
[Representations and positive functionals, Section
7](course:foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark#OA-FND-GN-07) (the Gelfand–Naimark
theorem).

## 1. Operator convex functions

**Definition 1.1.** Let \(I\subseteq\mathbb R\) be an interval and \(f:I\to\mathbb R\) continuous. Then \(f\) is
*operator convex* on \(I\) if
\[
f(\lambda a+(1-\lambda)b)\le\lambda f(a)+(1-\lambda)f(b)
\tag{1.1}
\]
for every Hilbert space \(H\), all self-adjoint \(a,b\in B(H)\) with spectra in \(I\), and all \(\lambda\in[0,1]\).
It is *operator concave* if \(-f\) is operator convex.

Here \(f(a)\) is the continuous functional calculus (R1). The left side of (1.1) is defined: if
\(\sigma(a),\sigma(b)\subseteq[\alpha,\beta]\subseteq I\), then \(\alpha\le a,b\le\beta\), so
\(\alpha\le\lambda a+(1-\lambda)b\le\beta\) (R1). For \(H=\mathbb C\), (1.1) is ordinary convexity, so an operator
convex function is convex. Positive combinations of operator convex functions are operator convex. If \(f_m\) are
operator convex on \(I\) and \(f_m\to f\) uniformly on each compact subinterval of \(I\), then \(f\) is operator convex:
for \(x\) with \(\sigma(x)\subseteq[\alpha,\beta]\subseteq I\), \(\|f_m(x)-f(x)\|\le\sup_{[\alpha,\beta]}|f_m-f|\to0\)
(R1), and the positive cone is closed.

**Lemma 1.2** (Schur complement). Let \(c,d,x\in B(H)\) with \(c\) positive and invertible and \(d\) self-adjoint. If
the operator \(\begin{pmatrix}c&x\\x^*&d\end{pmatrix}\) on \(H\oplus H\) is positive, then \(d\ge x^*c^{-1}x\).

**Proof.** For \(\zeta\in H\) put \(\xi=-c^{-1}x\zeta\). Then
\[
0\le\langle c\xi,\xi\rangle+2\operatorname{Re}\langle x\zeta,\xi\rangle+\langle d\zeta,\zeta\rangle
=\langle c^{-1}x\zeta,x\zeta\rangle-2\langle c^{-1}x\zeta,x\zeta\rangle+\langle d\zeta,\zeta\rangle
=\langle(d-x^*c^{-1}x)\zeta,\zeta\rangle .\qquad\square
\]

**Proposition 1.3.** (1) The function \(t\mapsto t^{-1}\) is operator convex on \((0,\infty)\).
(2) For \(s>0\), \(t\mapsto(t+s)^{-1}\) is operator convex on \((-s,\infty)\).
(3) The function \(t\mapsto t^2\) is operator convex on \(\mathbb R\).

**Proof.** (1) Let \(a\in B(H)\) be positive and invertible. For \(\xi,\zeta\in H\),
\[
\Bigl\langle\begin{pmatrix}a&1\\1&a^{-1}\end{pmatrix}\begin{pmatrix}\xi\\\zeta\end{pmatrix},
\begin{pmatrix}\xi\\\zeta\end{pmatrix}\Bigr\rangle=\|a^{1/2}\xi+a^{-1/2}\zeta\|^2\ge0 .
\]
Let \(b\) be another positive invertible operator and \(\lambda\in[0,1]\). Adding \(\lambda\) times the matrix for
\(a\) and \(1-\lambda\) times that for \(b\) gives a positive operator
\(\begin{pmatrix}c&1\\1&d\end{pmatrix}\) with \(c=\lambda a+(1-\lambda)b\) and
\(d=\lambda a^{-1}+(1-\lambda)b^{-1}\). If \(a,b\ge\varepsilon>0\), then \(c\ge\varepsilon\), so \(c\) is invertible.
Lemma 1.2 gives \(d\ge c^{-1}\), which is (1.1).

(2) If \(\sigma(a),\sigma(b)\subseteq(-s,\infty)\), then \(a+s\) and \(b+s\) are positive and invertible, and
\(\lambda(a+s)+(1-\lambda)(b+s)=\lambda a+(1-\lambda)b+s\). Apply (1).

(3) \(\lambda a^2+(1-\lambda)b^2-(\lambda a+(1-\lambda)b)^2=\lambda(1-\lambda)(a-b)^2\ge0\). \(\square\)

Not every convex function is operator convex: \(t\mapsto t^3\) is not operator convex on \([0,\infty)\) (Exercise 8.1).

## 2. The functions \(t\log t\) and \(\log t\)

For \(s>0\) put
\[
g_s(t)=\frac t{1+s}-\frac t{t+s}=\frac t{1+s}-1+\frac s{t+s}\quad(t\ge0),\qquad
k_s(t)=\frac1{1+s}-\frac1{t+s}\quad(t>0).
\]

**Lemma 2.1.** Let \(0<r\le R\). As \(\varepsilon\to0\) and \(N\to\infty\),
\(\int_\varepsilon^Ng_s(t)\,ds\to t\log t\) uniformly for \(t\in[0,R]\) (with \(0\log0=0\)), and
\(\int_\varepsilon^Nk_s(t)\,ds\to\log t\) uniformly for \(t\in[r,R]\).

**Proof.** For \(t>0\), an antiderivative of \(k_s(t)\) in \(s\) is \(\log(1+s)-\log(t+s)\), which tends to \(0\) as
\(s\to\infty\) and equals \(-\log t\) at \(s=0\). So \(\int_0^\infty k_s(t)\,ds=\log t\), and
\(\int_0^\infty g_s(t)\,ds=t\int_0^\infty k_s(t)\,ds=t\log t\), because \(g_s(t)=tk_s(t)\). At \(t=0\) every
\(g_s(0)=0\). For uniformity write \(g_s(t)=\frac t{t+s}\cdot\frac{t-1}{1+s}\). For \(t\in[0,R]\),
\(|g_s(t)|\le R+1\) for all \(s>0\), and \(|g_s(t)|\le R(R+1)s^{-2}\) for \(s\ge1\). Hence
\(|\int_0^\varepsilon g_s(t)\,ds|\le(R+1)\varepsilon\) and \(|\int_N^\infty g_s(t)\,ds|\le R(R+1)/N\). Likewise
\(k_s(t)=\frac{t-1}{(1+s)(t+s)}\) satisfies \(|k_s(t)|\le(R+1)/r\) and, for \(s\ge1\), \(|k_s(t)|\le(R+1)s^{-2}\), for
\(t\in[r,R]\). \(\square\)

**Theorem 2.2.** (1) The function \(t\mapsto t\log t\), with value \(0\) at \(0\), is operator convex on \([0,\infty)\).
Equivalently, \(\eta\) is operator concave on \([0,\infty)\): for positive \(a,b\) and \(\lambda\in[0,1]\),
\(\eta(\lambda a+(1-\lambda)b)\ge\lambda\eta(a)+(1-\lambda)\eta(b)\).
(2) The function \(\log\) is operator concave on \((0,\infty)\).

**Proof.** (1) Fix \(R>0\) and \(0<\varepsilon<N\). The function \((s,t)\mapsto g_s(t)\) is continuous on the compact
set \([\varepsilon,N]\times[0,R]\), hence uniformly continuous. So the Riemann sums
\(\sum_k(s_k-s_{k-1})g_{s_k}(t)\) of a sequence of partitions of \([\varepsilon,N]\) with mesh tending to \(0\)
converge to \(\int_\varepsilon^Ng_s(t)\,ds\) uniformly in \(t\in[0,R]\). Each \(g_s\) is a linear function plus
\(s(t+s)^{-1}\), so it is operator convex on \([0,\infty)\) by Proposition 1.3(2); hence every Riemann sum is operator
convex there. By the closure property after Definition 1.1, applied on \([0,R]\) for every \(R\), first
\(t\mapsto\int_\varepsilon^Ng_s(t)\,ds\) and then, by Lemma 2.1, \(t\mapsto t\log t\) are operator convex on
\([0,\infty)\).

(2) The same argument applies to \(k_s=(1+s)^{-1}-(t+s)^{-1}\), which is operator concave on \((0,\infty)\) by
Proposition 1.3(2), on the intervals \([r,R]\) with \(0<r\le R\), using the second half of Lemma 2.1. Every pair of
positive invertible operators has spectra in such an interval. \(\square\)

## 3. Jensen's operator inequality

**Theorem 3.1** (Jensen's operator inequality). Let \(f\) be a continuous function on an interval \(I\). The
following are equivalent.

(a) \(f\) is operator convex on \(I\).

(b) \(f(V^*XV)\le V^*f(X)V\) for all Hilbert spaces \(H,K\), every isometry \(V\in B(H,K)\) and every self-adjoint
\(X\in B(K)\) with \(\sigma(X)\subseteq I\).

(c) \(f\bigl(\sum_{i=1}^na_i^*x_ia_i\bigr)\le\sum_{i=1}^na_i^*f(x_i)a_i\) for every Hilbert space \(H\), every
\(n\ge1\), all \(a_1,\dots,a_n\in B(H)\) with \(\sum_ia_i^*a_i=1\) and all self-adjoint \(x_1,\dots,x_n\in B(H)\) with
spectra in \(I\).

(d) \(f(\Phi(x))\le\Phi(f(x))\) for every unital positive linear map \(\Phi:A\to B\) between unital C\*-algebras and
every self-adjoint \(x\in A\) with \(\sigma(x)\subseteq I\).

If \(0\in I\), then \(f\) is operator convex with \(f(0)\le0\) exactly when

(e) \(f(C^*XC)\le C^*f(X)C\) for all Hilbert spaces \(H,K\), every contraction \(C\in B(H,K)\) and every self-adjoint
\(X\in B(K)\) with \(\sigma(X)\subseteq I\).

For operator concave \(f\) all these inequalities hold reversed, and (e) holds reversed when \(f(0)\ge0\).

In (b)–(e) the left sides are defined. If \(\alpha\le X\le\beta\), then \(\alpha=\alpha V^*V\le V^*XV\le\beta\), and
likewise in (c); in (d), \(\alpha\le x\le\beta\) gives \(\alpha\le\Phi(x)\le\beta\) because \(\Phi\) is positive and
unital. In (e), \(C^*XC\) lies between \(\min(\alpha,0)\) and \(\max(\beta,0)\), since \(0\le C^*C\le1\).

**Proof.** (a)\(\Rightarrow\)(b). Put \(P=1_K-VV^*\), a projection with \(PV=0\). On \(K\oplus H\) let
\[
U=\begin{pmatrix}P&V\\V^*&0\end{pmatrix},\qquad D=\begin{pmatrix}1_K&0\\0&-1_H\end{pmatrix},\qquad
T=\begin{pmatrix}X&0\\0&c\,1_H\end{pmatrix},
\]
with a fixed \(c\in I\). Then \(U^*=U\) and \(U^2=\begin{pmatrix}P+VV^*&PV\\V^*P&V^*V\end{pmatrix}=1\), so \(U\) and
\(DU\) are unitaries. A direct computation gives
\[
UTU=\begin{pmatrix}PXP+cVV^*&PXV\\V^*XP&V^*XV\end{pmatrix},
\]
and \(D(UTU)D\) is the same matrix with the off-diagonal entries negated. Their average is
\(S=(PXP+cVV^*)\oplus V^*XV\). The operators \(UTU\) and \(D(UTU)D\) are unitarily equivalent to \(T\), so their
spectra lie in \(\sigma(T)\subseteq I\). By (1.1) with \(\lambda=\frac12\) and (R1),
\[
f(PXP+cVV^*)\oplus f(V^*XV)=f(S)\le\tfrac12\bigl(Uf(T)U+DUf(T)UD\bigr).
\]
Since \(f(T)=f(X)\oplus f(c)1_H\), the computation above with \(f(X)\) and \(f(c)\) in place of \(X\) and \(c\) shows
that the second diagonal entry of the right side is \(V^*f(X)V\). Compressing to the summand \(H\), which preserves
order (R1), gives \(f(V^*XV)\le V^*f(X)V\).

(b)\(\Rightarrow\)(c). The map \(V:H\to H^n\), \(V\xi=(a_1\xi,\dots,a_n\xi)\), is an isometry, since
\(V^*V=\sum_ia_i^*a_i=1\). With \(X=x_1\oplus\dots\oplus x_n\), \(V^*XV=\sum_ia_i^*x_ia_i\) and
\(V^*f(X)V=\sum_ia_i^*f(x_i)a_i\).

(c)\(\Rightarrow\)(a). Take \(n=2\), \(a_1=\lambda^{1/2}1\), \(a_2=(1-\lambda)^{1/2}1\), \(x_1=a\), \(x_2=b\).

(b)\(\Rightarrow\)(d). Let \(C_x\) be the C\*-subalgebra of \(A\) generated by \(1\) and \(x\). It is abelian, so the
restriction of \(\Phi\) to \(C_x\) is completely positive (R3). Represent \(B\) faithfully on a Hilbert space \(H\)
(R5); spectra and order in \(B\) are those in \(B(H)\) (R1). By (R4), \(\Phi(y)=V^*\pi(y)V\) for \(y\in C_x\), with a
representation \(\pi\) of \(C_x\) on \(K\) and \(V^*V=\Phi(1)=1\). The element \(\pi(x)\) is self-adjoint with
\(\sigma(\pi(x))\subseteq\sigma(x)\subseteq I\), and \(f(x)\in C_x\) with \(\pi(f(x))=f(\pi(x))\) (R1). By (b),
\[
f(\Phi(x))=f(V^*\pi(x)V)\le V^*f(\pi(x))V=V^*\pi(f(x))V=\Phi(f(x)).
\]

(d)\(\Rightarrow\)(a). Take \(A=B(H)\oplus B(H)\), \(B=B(H)\), \(\Phi(y\oplus z)=\lambda y+(1-\lambda)z\) and
\(x=a\oplus b\); then \(f(x)=f(a)\oplus f(b)\).

(e). Let \(f\) be operator convex with \(f(0)\le0\), let \(C\) be a contraction and \(X\) as in (e). The map
\(V:H\to K\oplus H\), \(V\xi=(C\xi,(1-C^*C)^{1/2}\xi)\), is an isometry. Put \(X'=X\oplus0_H\), whose spectrum lies in
\(\sigma(X)\cup\{0\}\subseteq I\). Then \(V^*X'V=C^*XC\) and
\[
V^*f(X')V=C^*f(X)C+f(0)(1-C^*C)\le C^*f(X)C .
\]
By (b), \(f(C^*XC)\le V^*f(X')V\le C^*f(X)C\). Conversely, if (e) holds, then \(C=0\) gives \(f(0)\le0\), and since
isometries are contractions, (b) and hence (a) hold. The statements for operator concave \(f\) follow by applying the
above to \(-f\). \(\square\)

*Reference:* the equivalence of (a), (b) and (c), and the contractive form (e), are [Hansen–Pedersen 2003, Theorem 2.1
and Corollary 2.3]; their proof of (a)\(\Rightarrow\)(c) averages over roots of unity, while the proof above uses one
self-adjoint unitary. Form (e) goes back to Hansen and Pedersen, and (d) for unital positive maps to [Davis 1957]
and [Choi 1974].

**Corollary 3.2.** Let \(\Phi:A\to B\) be a unital positive linear map between unital C\*-algebras. For every positive
\(a\in A\), \(\eta(\Phi(a))\ge\Phi(\eta(a))\), and \(\log\Phi(a)\ge\Phi(\log a)\) when \(a\) is invertible. For every
contraction \(C\) and positive \(X\), \(\eta(C^*XC)\ge C^*\eta(X)C\).

**Proof.** Theorem 2.2 and Theorem 3.1(d) for \(\eta\) on \([0,\infty)\) and for \(\log\) on \((0,\infty)\); the last
statement is Theorem 3.1(e) for the operator concave \(\eta\), with \(\eta(0)=0\). \(\square\)

## 4. Shannon entropy

Let \((\Omega,P)\) be a finite probability space. For a random variable \(U\) on \(\Omega\) with finitely many values,
put \(H(U)=\sum_u\eta(P(U=u))\); for a probability vector \(p=(p_1,\dots,p_m)\), \(H(p)=\sum_i\eta(p_i)\). A pair
\((U,V)\) is a random variable with values in pairs, and \(H(U\mid V)=H(U,V)-H(V)\). When \(P(V=v)>0\),
\(H(U\mid V=v)\) is the entropy of the conditional distribution \(u\mapsto P(U=u\mid V=v)\).

**Proposition 4.1** (Shannon's inequalities). Let \(U,V,W,U_1,\dots,U_n\) be random variables with finitely many
values on \((\Omega,P)\).

1. \(0\le H(U)\le\log m\) if \(U\) takes \(m\) values with positive probability.
2. \(H(U\mid V)=\sum_{v}P(V=v)\,H(U\mid V=v)\ge0\), the sum over the \(v\) with \(P(V=v)>0\). In particular
   \(H(U)\le H(U,V)\).
3. \(H(U,V)\le H(U)+H(V)\); equivalently \(H(U\mid V)\le H(U)\).
4. \(H(U\mid V,W)\le H(U\mid V)\).
5. \(H(U_1,\dots,U_n\mid V)\le\sum_jH(U_j\mid V)\).
6. For probability vectors \(p_1,p_2\) and \(\lambda\in[0,1]\),
   \(\lambda H(p_1)+(1-\lambda)H(p_2)\le H(\lambda p_1+(1-\lambda)p_2)\le\lambda H(p_1)+(1-\lambda)H(p_2)+\mathrm h(\lambda)\).
7. (Grouping.) If \(r\) is a probability vector on \(\{1,\dots,m\}\), \(j\le m\) and \(e=1-r_j>0\), then
   \(H(r)=\mathrm h(e)+e\,H(r')\), where \(r'=(r_i/e)_{i\ne j}\).

**Proof.** Write \(\pi_{uv}=P(U=u,V=v)\), \(p_u=P(U=u)\) and \(q_v=P(V=v)\). Terms with zero probability contribute
nothing below, since \(\eta(0)=0\).

(1) \(\eta\ge0\) on \([0,1]\). By concavity of \(\eta\), \(\frac1m\sum_i\eta(p_i)\le\eta(\frac1m)\) for the \(m\)
positive probabilities, and \(m\eta(\frac1m)=\log m\).

(2) For \(q_v>0\) put \(r_u=\pi_{uv}/q_v\). Then \(\sum_u\eta(\pi_{uv})=\sum_u\eta(q_vr_u)=\eta(q_v)+q_vH(r)\), because
\(\sum_ur_u=1\). Summing over \(v\) gives \(H(U,V)=H(V)+\sum_vq_vH(U\mid V=v)\). Exchanging the roles of \(U\) and \(V\)
gives \(H(U,V)\ge H(U)\).

(3) Using \(\log x\ge1-1/x\) for \(x>0\),
\[
H(U)+H(V)-H(U,V)=\sum_{\pi_{uv}>0}\pi_{uv}\log\frac{\pi_{uv}}{p_uq_v}\ge\sum_{\pi_{uv}>0}\bigl(\pi_{uv}-p_uq_v\bigr)\ge0 .
\]

(4) By (2) for the pair \((U,W)\) given \(V\), then (3) for the conditional distributions given \(V=v\), then (2) again,
\[
H(U,W\mid V)=\sum_vq_vH(U,W\mid V=v)\le\sum_vq_v\bigl(H(U\mid V=v)+H(W\mid V=v)\bigr)=H(U\mid V)+H(W\mid V).
\]
By the definitions this reads \(H(U,V,W)-H(V)\le H(U,V)-H(V)+H(V,W)-H(V)\), that is,
\(H(U,V,W)-H(V,W)\le H(U,V)-H(V)\).

(5) Directly from the definitions, \(H(U_1,\dots,U_n\mid V)=H(U_1\mid V)+H(U_2,\dots,U_n\mid V,U_1)\), and
\(H(U_2,\dots,U_n\mid V,U_1)\le H(U_2,\dots,U_n\mid V)\) by (4). Induction on \(n\).

(6) The left inequality is concavity of \(\eta\) in each coordinate. For the right one, let \(Z\) take the value \(1\)
with probability \(\lambda\) and \(2\) with probability \(1-\lambda\), and let \(X\) have conditional distribution
\(p_z\) given \(Z=z\); on the finite set of pairs \((x,z)\) this defines a probability, and \(X\) has distribution
\(\lambda p_1+(1-\lambda)p_2\). By (2), \(H(X)\le H(X,Z)=H(Z)+H(X\mid Z)=\mathrm h(\lambda)+\lambda H(p_1)+(1-\lambda)H(p_2)\).

(7) \(\sum_{i\ne j}\eta(er'_i)=\eta(e)+eH(r')\) because \(\sum_{i\ne j}r'_i=1\), and \(\eta(r_j)=\eta(1-e)\). \(\square\)

## 5. The sharp continuity bound for Shannon entropy

For probability vectors \(p,q\) on \(\{1,\dots,d\}\) put \(t(p,q)=\frac12\sum_i|p_i-q_i|\in[0,1]\).

**Lemma 5.1** (Maximal coupling). There is a matrix \((\pi_{ij})\) with nonnegative entries, row sums \(p_i\), column
sums \(q_j\), and \(\sum_i\pi_{ii}=1-t(p,q)\).

**Proof.** Put \(m_i=\min(p_i,q_i)\), \(a_i=p_i-m_i\ge0\) and \(b_j=q_j-m_j\ge0\). Then
\(\sum_ia_i=\sum_jb_j=1-\sum_im_i=t\), where \(t=t(p,q)\), because \(|p_i-q_i|=a_i+b_i\) and \(\sum_i(a_i+b_i)=2t\).
For every \(i\), \(a_ib_i=0\). If \(t=0\), take \(\pi_{ij}=m_i\delta_{ij}\). Otherwise put
\(\pi_{ij}=m_i\delta_{ij}+a_ib_j/t\). Its row sums are \(m_i+a_i=p_i\), its column sums \(m_j+b_j=q_j\), and its diagonal
is \(\pi_{ii}=m_i\), so \(\sum_i\pi_{ii}=1-t\). \(\square\)

**Theorem 5.2.** Let \(d\ge2\), and let \(p,q\) be probability vectors on \(\{1,\dots,d\}\) with \(t=t(p,q)\). Then
\[
|H(p)-H(q)|\le t\log(d-1)+\mathrm h(t).
\tag{5.1}
\]
For each \(t\in[0,1]\), equality holds for \(q=(1,0,\dots,0)\) and \(p=(1-t,\frac t{d-1},\dots,\frac t{d-1})\).

**Proof.** By symmetry it suffices to bound \(H(p)-H(q)\). Take \(\pi\) from Lemma 5.1 and view it as the distribution
of a pair \((X,Y)\) on \(\{1,\dots,d\}^2\), so that \(X\) has distribution \(p\), \(Y\) has distribution \(q\), and
\(P(X\ne Y)=t\). By Proposition 4.1(2), \(H(p)=H(X)\le H(X,Y)=H(q)+\sum_jq_jH(X\mid Y=j)\), the sum over \(q_j>0\).
For such \(j\), the conditional distribution \(r^{(j)}\) of \(X\) given \(Y=j\) has \(r^{(j)}_j=\pi_{jj}/q_j\); put
\(e_j=1-r^{(j)}_j\). By grouping (Proposition 4.1(7)) and Proposition 4.1(1) on \(d-1\) points,
\(H(r^{(j)})\le\mathrm h(e_j)+e_j\log(d-1)\); this also holds when \(e_j=0\), since then \(H(r^{(j)})=0\). By concavity of
\(\mathrm h\),
\[
\sum_jq_jH(X\mid Y=j)\le\mathrm h\Bigl(\sum_jq_je_j\Bigr)+\log(d-1)\sum_jq_je_j ,
\]
and \(\sum_jq_je_j=\sum_j(q_j-\pi_{jj})=t\). This proves (5.1). In the example, \(t(p,q)=t\), \(H(q)=0\), and
\(H(p)=\eta(1-t)+(d-1)\eta\bigl(\frac t{d-1}\bigr)=\eta(1-t)+\eta(t)+t\log(d-1)\). \(\square\)

The inequality \(H(X\mid Y)\le\mathrm h(P(X\ne Y))+P(X\ne Y)\log(d-1)\) proved here is Fano's inequality.

## 6. Eigenvalue inequalities

In this section \(A,B,W\) are self-adjoint operators on \(\mathbb C^d\), with eigenvalues ordered as in (R2), and
\(\|C\|_1=\operatorname{Tr}|C|\).

**Lemma 6.1** (Courant–Fischer). \(\lambda_i(A)=\max_V\min\{\langle Ax,x\rangle:x\in V,\ \|x\|=1\}\), the maximum over
the subspaces \(V\) of dimension \(i\). Consequently, \(A\le B\) implies \(\lambda_i(A)\le\lambda_i(B)\) for every \(i\).

**Proof.** Let \(f_1,\dots,f_d\) be orthonormal eigenvectors with \(Af_l=\lambda_l(A)f_l\). On
\(V=\operatorname{span}(f_1,\dots,f_i)\) every unit vector has \(\langle Ax,x\rangle\ge\lambda_i(A)\). Conversely, every
subspace \(V\) of dimension \(i\) meets \(\operatorname{span}(f_i,\dots,f_d)\), which has dimension \(d-i+1\), in a
unit vector \(x\), and \(\langle Ax,x\rangle\le\lambda_i(A)\). If \(A\le B\), then \(\langle Ax,x\rangle\le\langle
Bx,x\rangle\) for every \(x\), and the formula gives \(\lambda_i(A)\le\lambda_i(B)\). \(\square\)

**Lemma 6.2** (Ky Fan). (1) For orthonormal vectors \(e_1,\dots,e_k\),
\(\sum_{i\le k}\langle Ae_i,e_i\rangle\le\sum_{i\le k}\lambda_i(A)\).
(2) \(\operatorname{Tr}(AW)\le\sum_{i=1}^d\lambda_i(A)\lambda_i(W)\).

**Proof.** (1) With \(f_l\) as above, \(\sum_{i\le k}\langle Ae_i,e_i\rangle=\sum_l\lambda_l(A)c_l\), where
\(c_l=\sum_{i\le k}|\langle e_i,f_l\rangle|^2\). By Bessel's inequality \(0\le c_l\le1\), and
\(\sum_lc_l=\sum_{i\le k}\|e_i\|^2=k\). Hence
\[
\sum_l\lambda_l(A)c_l-\sum_{l\le k}\lambda_l(A)=\sum_{l\le k}\lambda_l(A)(c_l-1)+\sum_{l>k}\lambda_l(A)c_l
\le\lambda_k(A)\Bigl(\sum_{l\le k}(c_l-1)+\sum_{l>k}c_l\Bigr)=0 .
\]
(2) Let \(g_1,\dots,g_d\) be orthonormal eigenvectors of \(W\) with \(Wg_j=w_jg_j\), \(w_j=\lambda_j(W)\). Put
\(s_k=\sum_{j\le k}\langle Ag_j,g_j\rangle\) and \(\Lambda_k=\sum_{j\le k}\lambda_j(A)\), so \(s_k\le\Lambda_k\) by (1)
and \(s_d=\operatorname{Tr}A=\Lambda_d\). Summation by parts and \(w_k-w_{k+1}\ge0\) give
\[
\operatorname{Tr}(AW)=\sum_jw_j\langle Ag_j,g_j\rangle=\sum_{k<d}(w_k-w_{k+1})s_k+w_ds_d
\le\sum_{k<d}(w_k-w_{k+1})\Lambda_k+w_d\Lambda_d=\sum_jw_j\lambda_j(A).\qquad\square
\]

**Proposition 6.3** (Mirsky's inequalities for the trace norm).
\[
\sum_{i=1}^d|\lambda_i(A)-\lambda_i(B)|\le\|A-B\|_1\le\sum_{i=1}^d|\lambda_i(A)-\lambda_{d+1-i}(B)| .
\tag{6.1}
\]

**Proof.** Write \(A-B=C_+-C_-\) with \(C_\pm\ge0\) and \(C_+C_-=0\) (R1), so \(\|A-B\|_1=\operatorname{Tr}C_++\operatorname{Tr}C_-\).
The operator \(E=A+C_-=B+C_+\) satisfies \(E\ge A\) and \(E\ge B\), so \(\lambda_i(E)\ge\lambda_i(A),\lambda_i(B)\) by
Lemma 6.1. For numbers \(x,y\le z\), \(|x-y|\le(z-x)+(z-y)\). Hence
\[
\sum_i|\lambda_i(A)-\lambda_i(B)|\le\sum_i\bigl(2\lambda_i(E)-\lambda_i(A)-\lambda_i(B)\bigr)
=\operatorname{Tr}(E-A)+\operatorname{Tr}(E-B)=\operatorname{Tr}C_-+\operatorname{Tr}C_+ .
\]
For the second inequality let \(W=1_{(0,\infty)}(A-B)-1_{(-\infty,0]}(A-B)\), a self-adjoint operator with eigenvalues
\(\pm1\) and \(\operatorname{Tr}((A-B)W)=\|A-B\|_1\). By Lemma 6.2(2) for \(A,W\) and for \(B,-W\), and
\(\lambda_i(-W)=-\lambda_{d+1-i}(W)\),
\[
\|A-B\|_1=\operatorname{Tr}(AW)+\operatorname{Tr}(B(-W))\le\sum_i\lambda_i(A)\lambda_i(W)-\sum_i\lambda_i(B)\lambda_{d+1-i}(W)
=\sum_j\lambda_j(W)\bigl(\lambda_j(A)-\lambda_{d+1-j}(B)\bigr),
\]
and \(|\lambda_j(W)|\le1\). \(\square\)

*Reference:* both inequalities hold for every unitarily invariant norm; the left one is due to Mirsky. Lemma 6.2(1) is [Ky Fan 1949].

## 7. The Fannes–Audenaert inequality

A *density matrix* on \(\mathbb C^d\) is a positive operator \(\rho\) with \(\operatorname{Tr}\rho=1\); its entropy is
\(S(\rho)=\operatorname{Tr}\eta(\rho)=H(\lambda(\rho))\), where \(\lambda(\rho)=(\lambda_1(\rho),\dots,\lambda_d(\rho))\).

**Theorem 7.1** (Fannes–Audenaert inequality). Let \(d\ge2\), let \(\rho,\sigma\) be density matrices on
\(\mathbb C^d\), and let \(T=\frac12\|\rho-\sigma\|_1\). Then \(T\in[0,1]\) and
\[
|S(\rho)-S(\sigma)|\le T\log(d-1)+\mathrm h(T).
\tag{7.1}
\]
For each \(T\in[0,1]\), equality holds for \(\sigma=\operatorname{diag}(1,0,\dots,0)\) and
\(\rho=\operatorname{diag}(1-T,\frac T{d-1},\dots,\frac T{d-1})\).

**Proof.** Let \(p=\lambda(\rho)\), \(q=\lambda(\sigma)\), and let \(q'\) be \(q\) in increasing order,
\(q'_i=\lambda_{d+1-i}(\sigma)\). These are probability vectors, \(H(q')=H(q)=S(\sigma)\) and \(H(p)=S(\rho)\). By
Proposition 6.3,
\[
T_0:=t(p,q)\le T\le t(p,q')=:T_1\le\tfrac12\Bigl(\sum_ip_i+\sum_iq'_i\Bigr)=1 .
\]
Put \(F(t)=t\log(d-1)+\mathrm h(t)\), a concave function on \([0,1]\). Theorem 5.2 applied to \((p,q)\) and to
\((p,q')\) gives \(|S(\rho)-S(\sigma)|\le F(T_0)\) and \(|S(\rho)-S(\sigma)|\le F(T_1)\). Since \(T\in[T_0,T_1]\), concavity
gives \(F(T)\ge\min(F(T_0),F(T_1))\), which proves (7.1). The equality case is the one of Theorem 5.2, since the two
matrices are diagonal. \(\square\)

*Reference:* (7.1) is [Audenaert 2007], who reduces it to the commuting case through Mirsky's inequalities in the same
way and then proves the classical case by an optimization; the coupling proof of Theorem 5.2 replaces that
optimization. Fannes' original bound [Fannes 1973] was \(|S(\rho)-S(\sigma)|\le2T\log d+\eta(2T)\) for
\(2T\le1/e\).

The bound \(F(T)\) increases on \([0,1-\frac1d]\), where it reaches its maximum \(F(1-\frac1d)=\log d\), and decreases
afterwards. So (7.1) also gives the uniform estimate \(|S(\rho)-S(\sigma)|\le F(\min(T,1-\frac1d))\), which is
nondecreasing in \(T\), and \(|S(\rho)-S(\sigma)|\to0\) as \(T\to0\), uniformly in the dimension-\(d\) states.

## 8. Exercises

**Exercise 8.1.** Show that \(t\mapsto t^3\) is not operator convex on \([0,\infty)\): take
\(a=\begin{pmatrix}1&1\\1&1\end{pmatrix}\) and \(b=\begin{pmatrix}3&1\\1&1\end{pmatrix}\) and \(\lambda=\frac12\).

*Solution.* Both matrices are positive: \(a\) has eigenvalues \(0,2\), and \(b\) has trace \(4\) and determinant \(2\).
Here \(a^3=\begin{pmatrix}4&4\\4&4\end{pmatrix}\), \(b^2=\begin{pmatrix}10&4\\4&2\end{pmatrix}\) and
\(b^3=\begin{pmatrix}34&14\\14&6\end{pmatrix}\), so \(\frac12(a^3+b^3)=\begin{pmatrix}19&9\\9&5\end{pmatrix}\). With
\(c=\frac12(a+b)=\begin{pmatrix}2&1\\1&1\end{pmatrix}\), \(c^2=\begin{pmatrix}5&3\\3&2\end{pmatrix}\) and
\(c^3=\begin{pmatrix}13&8\\8&5\end{pmatrix}\). The difference \(\frac12(a^3+b^3)-c^3=\begin{pmatrix}6&1\\1&0\end{pmatrix}\)
has determinant \(-1\), so it has a negative eigenvalue, and (1.1) fails.

**Exercise 8.2.** Let \(d=2\). Show that (7.1) reads \(|S(\rho)-S(\sigma)|\le\mathrm h(T)\), and that for qubit states
\(|S(\rho)-S(\sigma)|\le\log2\) with equality only if one state is pure and the other is \(\frac12\).

*Solution.* \(\log(d-1)=0\). Every density matrix on \(\mathbb C^2\) has \(0\le S\le\log2\) by Proposition 4.1(1), with
\(S=0\) exactly for pure states (eigenvalues \(1,0\)) and \(S=\log2\) exactly for \(\frac12\) (eigenvalues
\(\frac12,\frac12\), by strict concavity of \(\eta\)). So the difference is at most \(\log2\), and equality forces one
state pure and the other \(\frac12\). For such a pair \(T=\frac12\), and \(\mathrm h(\frac12)=\log2\), so (7.1) is an
equality.

**Exercise 8.3.** Let \(\Phi:A\to B\) be a unital positive map between unital C\*-algebras and \(\varphi\) a state of
\(B\). Show that \(\varphi(\eta(\Phi(a)))\ge(\varphi\circ\Phi)(\eta(a))\) for positive \(a\), and that for a density
matrix \(\rho\) on \(\mathbb C^d\) and a unital positive trace-preserving map \(\Phi\) of \(M_d(\mathbb C)\),
\(S(\Phi(\rho))\ge S(\rho)\).

*Solution.* By Corollary 3.2, \(\eta(\Phi(a))-\Phi(\eta(a))\ge0\), and a state is positive. For the second statement
take \(\varphi=\operatorname{Tr}\) (a positive functional) and \(a=\rho\): \(\operatorname{Tr}\eta(\Phi(\rho))\ge
\operatorname{Tr}\Phi(\eta(\rho))=\operatorname{Tr}\eta(\rho)\), and \(\Phi(\rho)\) is again a density matrix.

## References



- [Audenaert 2007] K. M. R. Audenaert, A sharp continuity estimate for the von Neumann entropy, *Journal of Physics A:
  Mathematical and Theoretical* 40 (2007), 8127–8136. Free version: https://arxiv.org/abs/quant-ph/0610146
- [Choi 1974] M.-D. Choi, A Schwarz inequality for positive linear maps on C\*-algebras, *Illinois Journal of
  Mathematics* 18 (1974), 565–574. https://doi.org/10.1215/ijm/1256051007
- [Davis 1957] C. Davis, A Schwarz inequality for convex operator functions, *Proceedings of the American
  Mathematical Society* 8 (1957), 42–44. https://doi.org/10.1090/S0002-9939-1957-0084120-4. Free at https://www.ams.org/journals/proc/1957-008-01/S0002-9939-1957-0084120-4/
- [Fannes 1973] M. Fannes, A continuity property of the entropy density for spin lattice systems, *Communications in
  Mathematical Physics* 31 (1973), 291–294. https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-4
- [Hansen–Pedersen 2003] F. Hansen and G. K. Pedersen, Jensen's operator inequality, *Bulletin of the London
  Mathematical Society* 35 (2003), 553–564. Free version: https://arxiv.org/abs/math/0204049
- [Ky Fan 1949] K. Fan, On a theorem of Weyl concerning eigenvalues of linear transformations I, *Proceedings of the
  National Academy of Sciences of the USA* 35 (1949), 652–655. https://doi.org/10.1073/pnas.35.11.652
