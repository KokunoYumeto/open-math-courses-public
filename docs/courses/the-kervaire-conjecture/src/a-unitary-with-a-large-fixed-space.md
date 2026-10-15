# A unitary with a large fixed space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of the planar boundary theorem needs a unitary matrix that mixes \(k\) copies of a word disk and fixes many vectors. This lesson proves the statement that supplies it [OpenAI-K, Lemma 3.1]: if signs \(s_1,\ldots,s_n\) add up to \(\pm1\), then every unitary \(P\) of size \(nk\) can be multiplied by a block-diagonal matrix \(\operatorname{diag}(X^{s_1},\ldots,X^{s_n})\), with one unitary \(X\) of size \(k\), so that the product fixes a \(k\)-dimensional subspace. The proof is a degree computation modulo two, in the spirit of Gerstenhaber and Rothaus [Gerstenhaber–Rothaus 1962, Theorem 1]: a map between manifolds of the same dimension has odd degree, so it is onto. To make the dimensions agree, the domain records a unitary together with a \(k\)-plane that it fixes.

- Unitary groups and graph charts (Section 1).
- The incidence manifold (Section 2).
- A homotopy to a model (Section 3).
- The unique preimage of the identity (Section 4).
- The fixed-space lemma (Section 5).

We use degree modulo two, Definition 4.1, the homotopy invariance stated after it, Lemma 4.2 and Corollary 4.3 of [Regular values and degree modulo two](course:borsuks-conjecture-in-dimension-nine/regular-values-and-degree-modulo-two), and the inverse function theorem of the core course [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) [Lebl, Theorem 8.5.1].

Throughout, matrices carry the operator norm, \(\mathrm U(m)\) is the group of unitary \(m\times m\) matrices, and \(\mathfrak u(m)\) is the real vector space of skew-Hermitian \(m\times m\) matrices, of real dimension \(m^2\). The exponential \(e^S=\sum_{n\ge0}S^n/n!\) of \(S\in\mathfrak u(m)\) is unitary, since \((e^S)^*=e^{S^*}=e^{-S}\).

## 1. Unitary groups and graph charts

**Lemma 1.1** (unitary groups). For \(\|T\|<1\) put \(\log(I+T)=\sum_{n\ge1}(-1)^{n+1}T^n/n\).

1. If \(\|S\|<\log2\), then \(\|e^S-I\|<1\) and \(\log e^S=S\). If \(\|T\|<1\), then \(e^{\log(I+T)}=I+T\).
2. If \(W\in\mathrm U(m)\) and \(\|W-I\|<1\), then \(\log W\in\mathfrak u(m)\).
3. For \(W_0\in\mathrm U(m)\), the maps \(S\mapsto W_0e^S\) on \(\{S\in\mathfrak u(m):\|S\|<\log2\}\) are homeomorphisms onto open subsets of \(\mathrm U(m)\) whose transition maps are smooth. So \(\mathrm U(m)\) is a compact smooth manifold of dimension \(m^2\). It is connected.

*Proof.* (1) The power series identities \(\log(e^x)=x\) and \(e^{\log(1+y)}=1+y\) hold for real or complex numbers with \(|x|<\log2\), \(|y|<1\), and the series converge absolutely. Substituting a matrix into absolutely convergent power series in one variable respects composition, so the same identities hold for \(S\) and \(T\); and \(\|e^S-I\|\le e^{\|S\|}-1<1\).

(2) \(W\) is normal, so \(W=V\operatorname{diag}(\lambda_j)V^*\) with \(V\) unitary and \(|\lambda_j|=1\), and \(\|W-I\|=\max_j|\lambda_j-1|<1\). Then \(\log W=V\operatorname{diag}(\log\lambda_j)V^*\), where \(\log\lambda_j\) is the sum of the scalar series. By (1), \(e^{\log\lambda_j}=\lambda_j\) has modulus one, so \(\log\lambda_j\) is purely imaginary, and \(\log W\) is skew-Hermitian.

(3) \(\mathrm U(m)\) is closed and bounded in the space of matrices, hence compact. The map \(S\mapsto W_0e^S\) is continuous and injective on the ball of radius \(\log2\), with continuous inverse \(W\mapsto\log(W_0^{-1}W)\) on the open set of those \(W\) with \(\|W_0^{-1}W-I\|<1\) and \(\|\log(W_0^{-1}W)\|<\log2\), by (1) and (2). The images cover \(\mathrm U(m)\), and the transition maps \(S\mapsto\log(W_1^{-1}W_0e^S)\) are given by convergent power series, hence smooth. Every unitary is \(V\operatorname{diag}(e^{i\theta_j})V^*\) with \(V\) unitary, and \(t\mapsto V\operatorname{diag}(e^{it\theta_j})V^*\) joins it to \(I\); so \(\mathrm U(m)\) is connected. \(\square\)

**Grassmannians.** Let \(\operatorname{Gr}_k(\mathbb C^m)\) be the set of complex \(k\)-dimensional subspaces of \(\mathbb C^m\). We identify a subspace \(E\) with its orthogonal projection \(p_E\) and give the Grassmannian the topology of these matrices. It is compact, being the image of the compact group \(\mathrm U(m)\) under \(g\mapsto gp_{E_0}g^*\) for a fixed \(E_0\): every \(k\)-plane is \(gE_0\) for a unitary \(g\) that carries an orthonormal basis of \(E_0\), extended to one of \(\mathbb C^m\), to one of \(E\).

Fix \(E_0\in\operatorname{Gr}_k(\mathbb C^m)\), put \(r=m-k\), and write vectors of \(\mathbb C^m=E_0\oplus E_0^\perp\) as pairs \((v,y)\), and matrices in block form. For a complex \(r\times k\) matrix \(Z\), viewed as a linear map \(E_0\to E_0^\perp\), put
\[
K_Z=\begin{pmatrix}0&-Z^*\\Z&0\end{pmatrix}\in\mathfrak u(m).
\]

**Lemma 1.2** (graph charts).

1. If \(\|p_E-p_{E_0}\|<1\), then \(E\) is the graph \(\{(v,Lv):v\in E_0\}\) of exactly one linear map \(L=L(E):E_0\to E_0^\perp\), and \(L(E)\) depends smoothly on \(p_E\).
2. If \(\|Z\|<\pi/2\), then \(e^{K_Z}E_0\) is the graph of \(\Lambda(Z)=Zf(Z^*Z)\), where \(f(x)=\tan(\sqrt x)/\sqrt x=\sum_{j\ge0}c_jx^j\) for \(0\le x<\pi^2/4\), with \(f(0)=1\). The map \(\Lambda\) is smooth, and its derivative at \(0\) is the identity, so it maps a neighbourhood of \(0\) diffeomorphically onto a neighbourhood of \(0\).

*Proof.* (1) Write \(p_0=p_{E_0}\) and \(T=p_0p_Ep_0\) on \(E_0\). For \(v\in E_0\), \(\|Tv-v\|=\|p_0(p_E-p_0)v\|<\|v\|\) if \(v\ne0\), so \(T\) is invertible on \(E_0\), with inverse depending smoothly on \(p_E\) (Neumann series). For \(v\in E_0\) the vector \(u=p_ET^{-1}v\) lies in \(E\) and \(p_0u=TT^{-1}v=v\), so \(u=(v,Lv)\) with \(L=(I-p_0)p_ET^{-1}\). The graph of \(L\) is a \(k\)-dimensional subspace of \(E\), so it is \(E\). If \(E\) were also the graph of \(L'\), then \((v,Lv)-(v,L'v)\in E\) would lie in \(E_0^\perp\); but no nonzero \(u\in E\) has \(p_0u=0\), since then \(\|u\|=\|(p_E-p_0)u\|<\|u\|\). So \(L'=L\).

(2) From \(K_Z^2=\operatorname{diag}(-Z^*Z,-ZZ^*)\), the even and odd terms of the exponential series give
\[
\begin{gathered}
e^{K_Z}\begin{pmatrix}v\\0\end{pmatrix}=\begin{pmatrix}c(Z^*Z)v\\Zs(Z^*Z)v\end{pmatrix},\\
c(x)=\sum_{j\ge0}\frac{(-x)^j}{(2j)!},\\
s(x)=\sum_{j\ge0}\frac{(-x)^j}{(2j+1)!},
\end{gathered}
\]
so that \(c(x)=\cos\sqrt x\) and \(s(x)=\sin\sqrt x/\sqrt x\) for \(x\ge0\). The eigenvalues of \(Z^*Z\) are squares of numbers in \([0,\|Z\|]\subseteq[0,\pi/2)\), so \(c(Z^*Z)\) is invertible, and \(e^{K_Z}E_0\) is the graph of \(Zs(Z^*Z)c(Z^*Z)^{-1}=Zf(Z^*Z)\). The series \(\sum_jc_jZ(Z^*Z)^j\) converges for \(\|Z\|<\pi/2\), so \(\Lambda\) is smooth; \(\Lambda(Z)=Z+O(\|Z\|^3)\), so its derivative at \(0\) is the identity, and the inverse function theorem applies. \(\square\)

## 2. The incidence manifold

**Lemma 2.1** (the incidence manifold). Let \(1\le k\le m\) and \(r=m-k\). The set
\[
\begin{gathered}
\mathcal R=\{(W,E)\in\mathrm U(m)\times\operatorname{Gr}_k(\mathbb C^m):\\
W|_E=\mathrm{id}_E\}
\end{gathered}
\]
is a compact smooth manifold of dimension \(m^2-k^2=2kr+r^2\). Charts are obtained as follows. For \((W_1,E_1)\in\mathcal R\) there are \(g\in\mathrm U(m)\) with \(gE_0=E_1\), and \(Y_1\in\mathrm U(r)\) with \(g^{-1}W_1g=I_k\oplus Y_1\); then
\[
\begin{gathered}
\chi(Z,B)=\Bigl(g\,e^{K_Z}\bigl(I_k\oplus Y_1e^B\bigr)e^{-K_Z}g^{-1},\\
g\,e^{K_Z}E_0\Bigr),
\end{gathered}
\]
for complex \(r\times k\) matrices \(Z\) and \(B\in\mathfrak u(r)\), both small, maps a neighbourhood of \(0\) homeomorphically onto a neighbourhood of \((W_1,E_1)\) in \(\mathcal R\).

*Proof.* \(\mathcal R\) is defined by the closed condition \((W-I)p_E=0\) in a compact space, so it is compact. Given \((W_1,E_1)\), choose \(g\) as in the description of the Grassmannian. Then \(g^{-1}W_1g\) fixes \(E_0\) pointwise; a unitary that preserves \(E_0\) preserves \(E_0^\perp\), so \(g^{-1}W_1g=I_k\oplus Y_1\) with \(Y_1\in\mathrm U(r)\).

The point \(\chi(Z,B)\) lies in \(\mathcal R\): its unitary fixes \(ge^{K_Z}E_0\) pointwise. Conversely, we construct a continuous inverse. Let \((W,E)\in\mathcal R\) be close to \((W_1,E_1)\). Then \(g^{-1}E\) is close to \(E_0\), so it is the graph of \(L(g^{-1}E)\) (Lemma 1.2(1)), and there is exactly one small \(Z\) with \(\Lambda(Z)=L(g^{-1}E)\), that is \(e^{K_Z}E_0=g^{-1}E\) (Lemma 1.2(2)); it depends continuously, indeed smoothly, on \(p_E\). The unitary \(e^{-K_Z}g^{-1}Wge^{K_Z}\) fixes \(E_0\) pointwise, so it is \(I_k\oplus Y\) with \(Y\in\mathrm U(r)\) close to \(Y_1\), and \(B=\log(Y_1^{-1}Y)\) (Lemma 1.1). The map \((W,E)\mapsto(Z,B)\) so defined is continuous, indeed given by smooth formulas in the entries of \(W\) and \(p_E\), and sends \((W_1,E_1)\) to \((0,0)\). It inverts \(\chi\) on both sides near these points: for small \((Z,B)\), the construction applied to \(\chi(Z,B)\) returns \(Z\), by the uniqueness in Lemma 1.2(2), and then \(Y=Y_1e^B\) and \(B\), by Lemma 1.1(1); and every \((W,E)\in\mathcal R\) close to \((W_1,E_1)\) equals \(\chi\) of its small parameters. So \(\chi\) maps a neighbourhood of \(0\) homeomorphically onto a neighbourhood of \((W_1,E_1)\) in \(\mathcal R\). A chart composed with the inverse of another is smooth, because \(\chi\) is smooth as a map into pairs of matrices \((W,p_E)\), with \(p_E=ge^{K_Z}p_{E_0}e^{-K_Z}g^{-1}\), and the inverse of a chart is given by smooth formulas in \((W,p_E)\). The parameters \(Z\) and \(B\) have \(2kr\) and \(r^2\) real coordinates. If \(r=0\), \(\mathcal R\) is the single point \((I,\mathbb C^m)\), of dimension \(0=m^2-k^2\). \(\square\)

## 3. A homotopy to a model

Fix signs \(s_1,\ldots,s_n\in\{1,-1\}\) with \(\varepsilon=\sum_is_i\in\{1,-1\}\), an integer \(k\ge1\), and \(m=nk\). Split \(\mathbb C^m=E_1\oplus\cdots\oplus E_n\) into coordinate blocks of dimension \(k\), and for \(X\in\mathrm U(k)\) and \(P\in\mathrm U(m)\) put
\[
F(X)=\operatorname{diag}(X^{s_1},\ldots,X^{s_n})\,P .
\]
Since \(\varepsilon\ne0\), some index \(i_0\) has \(s_{i_0}=\varepsilon\). Put \(E_0=E_{i_0}\), \(r=m-k\), and
\[
\begin{gathered}
F_0(X)=X^{\varepsilon}\oplus(-I_r)\\
\text{on }E_0\oplus E_0^\perp .
\end{gathered}
\]

**Lemma 3.1.** There is a continuous map \(\Phi:[0,1]\times\mathrm U(k)\to\mathrm U(m)\) with \(\Phi(0,\cdot)=F\) and \(\Phi(1,\cdot)=F_0\).

*Proof.* We concatenate three homotopies; each is continuous in both variables.

*Remove \(P\).* Write \(P=V\operatorname{diag}(e^{i\theta_j})V^*\) with \(V\) unitary and real \(\theta_j\), and replace \(P\) by \(V\operatorname{diag}(e^{i(1-u)\theta_j})V^*\), \(0\le u\le1\).

*Cancel pairs.* The numbers \(n_\pm\) of signs \(\pm1\) satisfy \(n_+-n_-=\varepsilon\), so the indices other than \(i_0\) split into pairs \(\{i,j\}\) with \(s_i=1\) and \(s_j=-1\). On \(E_i\oplus E_j\) put
\[
\begin{gathered}
R_u=\begin{pmatrix}\cos(\pi u/2)I_k&-\sin(\pi u/2)I_k\\ \sin(\pi u/2)I_k&\cos(\pi u/2)I_k\end{pmatrix},\\
H_u(X)=\operatorname{diag}(X,I_k)\,R_u\\
\cdot\operatorname{diag}(I_k,X^{-1})\,R_u^{-1}.
\end{gathered}
\]
Then \(H_0(X)=\operatorname{diag}(X,X^{-1})\), and since \(R_1\operatorname{diag}(I_k,X^{-1})R_1^{-1}=\operatorname{diag}(X^{-1},I_k)\), \(H_1(X)=I\). Apply \(H_u\) on all pairs at once, keeping \(X^\varepsilon\) on \(E_0\).

*Move the identity to \(-I\).* On \(E_0^\perp\) replace \(I\) by \(e^{i\pi u}I\), \(0\le u\le1\). \(\square\)

## 4. The unique preimage of the identity

Let \(\mathcal M=\mathrm U(k)\times\mathcal R\), with \(\mathcal R\) as in Lemma 2.1; it is a compact smooth manifold of dimension \(k^2+(m^2-k^2)=m^2\), the dimension of \(\mathrm U(m)\). For a map \(\Psi:\mathrm U(k)\to\mathrm U(m)\) define
\[
\begin{gathered}
G_\Psi:\mathcal M\longrightarrow\mathrm U(m),\\
G_\Psi(X,W,E)=\Psi(X)\,W^{-1} .
\end{gathered}
\]
A point with \(G_\Psi(X,W,E)=I\) has \(\Psi(X)=W\), so \(\Psi(X)\) fixes the \(k\)-plane \(E\) pointwise.

**Lemma 4.1.** Let \(W_0=I_k\oplus(-I_r)\).

1. The only point of \(\mathcal M\) mapped to \(I\) by \(G_{F_0}\) is \((I_k,W_0,E_0)\).
2. In the chart \((A,Z,B)\mapsto(X,W,E)\) of \(\mathcal M\) at this point given by \(X=e^A\), \(W=e^{K_Z}(I_k\oplus(-e^B))e^{-K_Z}\) and \(E=e^{K_Z}E_0\), with \(A\in\mathfrak u(k)\) (Lemma 1.1 and Lemma 2.1 with \(g=I\), \(Y_1=-I_r\)), and the chart \(\log\) of \(\mathrm U(m)\) at \(I\), the map \(G_{F_0}\) is smooth near \(0\), and its derivative at \(0\) is
\[
(A,Z,B)\longmapsto\begin{pmatrix}\varepsilon A&2Z^*\\-2Z&-B\end{pmatrix},
\]
a linear isomorphism of \(\mathfrak u(k)\times M_{r\times k}(\mathbb C)\times\mathfrak u(r)\) onto \(\mathfrak u(m)\).

*Proof.* (1) If \(G_{F_0}(X,W,E)=I\), then \(W=F_0(X)=X^\varepsilon\oplus(-I_r)\). Every fixed vector of this matrix lies in \(E_0\), and \(W\) fixes the \(k\)-dimensional space \(E\) pointwise, so \(E=E_0\) and \(X^\varepsilon=I_k\). Since \(\varepsilon=\pm1\), \(X=I_k\) and \(W=W_0\). Conversely this point is mapped to \(I\).

(2) The chart is the product of the chart of Lemma 1.1 at \(I_k\) and the chart of Lemma 2.1, and \(G_{F_0}\) is a composite of products, inverses, exponentials and \(\log\) near \(I\), so it is smooth. Differentiate along \(t\mapsto(tA,tZ,tB)\) at \(t=0\). The derivative of \(F_0(e^{tA})=e^{t\varepsilon A}\oplus(-I_r)\) is \(\dot F=\operatorname{diag}(\varepsilon A,0)\). The derivative of \(W(t)=e^{tK_Z}(I_k\oplus(-e^{tB}))e^{-tK_Z}\) is
\[
\begin{aligned}
\dot W&=K_ZW_0-W_0K_Z+\operatorname{diag}(0,-B)\\
&=\begin{pmatrix}0&2Z^*\\2Z&-B\end{pmatrix}.
\end{aligned}
\]
At \(t=0\), \(F_0=W_0=W_0^{-1}\), so the derivative of \(F_0W^{-1}\) is \(\dot FW_0^{-1}-F_0W_0^{-1}\dot WW_0^{-1}=\dot FW_0-\dot WW_0\), which is the displayed matrix; the derivative of \(\log\) at \(I\) is the identity. The linear map is injective, and both spaces have real dimension \(k^2+2kr+r^2=m^2\). If \(r=0\), the map is \(A\mapsto\varepsilon A\). \(\square\)

## 5. The fixed-space lemma

**Lemma 5.1** (a unitary with a large fixed space; [OpenAI-K, Lemma 3.1]). Let \(s_1,\ldots,s_n\in\{1,-1\}\) with \(\sum_is_i\in\{1,-1\}\), let \(k\ge1\) and \(m=nk\). For every \(P\in\mathrm U(m)\) there is \(X\in\mathrm U(k)\) such that
\[
F(X)=\operatorname{diag}(X^{s_1},\ldots,X^{s_n})\,P
\]
fixes pointwise a complex subspace of dimension at least \(k\).

*Proof.* \(\mathcal M\) is a closed smooth manifold of dimension \(m^2\) (Lemma 2.1), and \(\mathrm U(m)\) is a connected closed smooth manifold of the same dimension (Lemma 1.1). By Lemma 4.1 above and Lemma 4.2 of the degree lesson, \(\deg_2G_{F_0}=1\): the fibre over \(I\) is one point, at which \(G_{F_0}\) is differentiable in charts with invertible derivative. The homotopy \(\Phi\) of Lemma 3.1 gives the homotopy \((u,X,W,E)\mapsto\Phi(u,X)W^{-1}\) from \(G_F\) to \(G_{F_0}\), so \(\deg_2G_F=1\) by homotopy invariance. By Corollary 4.3 of the degree lesson, \(G_F\) is onto; a point with \(G_F(X,W,E)=I\) gives \(F(X)=W\), which fixes the \(k\)-plane \(E\) pointwise. \(\square\)

The conclusion holds for an arbitrary fixed \(P\); no continuity in \(P\) is claimed. The hypothesis \(\sum_is_i=\pm1\) enters in two places: it lets all blocks but one cancel in pairs, and it makes \(X^\varepsilon=I\) force \(X=I\), so that the preimage is a single point. For \(|\sum_is_i|\ge2\) the solutions of \(X^\varepsilon=I\) form a set of positive dimension, and the companion manuscript on nonsingular systems replaces the count of a single preimage by a computation in cohomology [OpenAI-H, Section 2]; the lesson [Simultaneous fixed spaces](course:nonsingular-systems-over-groups/simultaneous-fixed-spaces) proves that version, for several unitary variables. Without any condition the statement fails (Exercise 6.2).

## 6. Exercises

**6.1** (easy). Prove Lemma 5.1 directly when \(n=1\).

**6.2** (medium). Let \(n=2\), \(s=(1,-1)\), \(k=1\) and \(P=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\). Show that \(\operatorname{diag}(x,x^{-1})P\) has no eigenvalue \(1\) for any \(x\in\mathrm U(1)\).

**6.3** (easy). Let \(m=2\), \(k=1\). Describe \(\mathcal R\) and check that its dimension is \(3\).

**6.4** (easy). Prove Lemma 5.1 directly when \(P\) is block-diagonal, \(P=\operatorname{diag}(P_1,\ldots,P_n)\) with \(P_i\in\mathrm U(k)\).

**6.5** (medium). For \(k=r=1\) and \(Z=z\in\mathbb C\), compute \(e^{K_z}\) and check Lemma 1.2(2).

## 7. Solutions

**6.1.** Then \(s_1=\varepsilon\) and \(F(X)=X^\varepsilon P\). For \(X=P^{-\varepsilon}\), \(X^\varepsilon=P^{-\varepsilon^2}=P^{-1}\), so \(F(X)=I\), which fixes all of \(\mathbb C^k\).

**6.2.** \(F(x)=\begin{pmatrix}0&x\\-x^{-1}&0\end{pmatrix}\) has trace \(0\) and determinant \(1\), so its characteristic polynomial is \(\lambda^2+1\), with roots \(\pm i\).

**6.3.** A point is a pair of a unitary \(W\) and a line \(E\) that it fixes; \(W\) acts on \(E^\perp\) by a number of modulus one. So \(\mathcal R\) is the set of pairs (line in \(\mathbb C^2\), number of modulus one), the product \(\mathbb{CP}^1\times\mathrm U(1)\), of dimension \(2+1=3=4-1\).

**6.4.** Then \(F(X)=\operatorname{diag}(X^{s_1}P_1,\ldots,X^{s_n}P_n)\). Let \(s_{i_0}=\varepsilon\) and \(X=P_{i_0}^{-\varepsilon}\); the block \(X^{\varepsilon}P_{i_0}=I_k\), so \(F(X)\) fixes \(E_{i_0}\) pointwise.

**6.5.** \(K_z^2=-|z|^2I_2\), so \(e^{K_z}=\begin{pmatrix}\cos|z|&-\bar z\,\frac{\sin|z|}{|z|}\\ z\,\frac{\sin|z|}{|z|}&\cos|z|\end{pmatrix}\) (with \(\frac{\sin|z|}{|z|}=1\) at \(z=0\)). It maps \((1,0)\) to \((\cos|z|,\ z\sin|z|/|z|)\), which spans the graph of multiplication by \(z\tan|z|/|z|=zf(|z|^2)\).

## References

- [OpenAI-K] OpenAI, *The Kervaire theorem for groups*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026
- [OpenAI-H] OpenAI, *Nonsingular systems of equations over arbitrary groups*, OpenAI Math Release preprint, 5 October 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026
- [Gerstenhaber–Rothaus 1962] M. Gerstenhaber and O. S. Rothaus, *The solution of sets of equations in groups*, Proc. Nat. Acad. Sci. U.S.A. 48 (1962), 1531–1533, Theorem 1; free on PubMed Central. https://pmc.ncbi.nlm.nih.gov/articles/PMC220992/
- [Lebl] J. Lebl, *Basic Analysis II*, version 6.3, Theorem 8.5.1 (inverse function theorem); core course Real Analysis II. https://www.jirka.org/ra/html/sec_svinvfuncthm.html#thm_inverse
