# Disjoint pair resamplings

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the operator inequality \(H^2\succeq H\), and with it the mixing theorem of [The switch chain](the-switch-chain.md). We keep the notation of that lesson: \(V=\{1,\dots,n\}\) with \(n\ge4\), a graphical vector \(d\), the uniform measure on \(\Omega_d\) and its inner product, the pair fibers, and \(h_a=I-E_a\), \(H=\sum_ah_a\). When \(H^2\) is expanded, the products \(h_ah_b\) of intersecting pairs are controlled by the triple estimate of [A variance inequality for three rows](a-variance-inequality-for-three-rows.md). The products of *disjoint* pairs \(a,b\) remain. In Caputo's binary collision processes the operators of disjoint pairs commute [Caputo], and a product of two commuting orthogonal projections is again an orthogonal projection, hence positive semidefinite. Here they need not commute: both resamplings can change the four vertex pairs between \(a\) and \(b\), a dependence already observed by Carstens, Berger and Strona [CBS]. A single term \(\langle h_af,h_bf\rangle\) can be negative (Exercise 4.1). OpenAI's argument [OpenAI-SW, Sections 5–7] shows that the sum of all these terms is nonnegative. Proposition 1.1 bounds one interaction from below by a switch term minus two errors, each the square of a projection onto a function of the form "both vertices of \(b\) go to the same endpoint of \(a\)". Lemma 2.1, an inequality on the slices of the Boolean cube, shows that the switch terms pay for the errors. Theorem 3.3 then gives \(H^2\succeq H\).

## 1. One interaction

For disjoint pairs \(a=\{i,j\}\) and \(b=\{k,l\}\), the four vertex pairs between \(a\) and \(b\) form the *cross matrix*
\[
\begin{pmatrix}[ik]&[il]\\ {[jk]}&[jl]\end{pmatrix},
\]
where \([xy]\) is \(1\) if \(xy\) is an edge and \(0\) otherwise. Let \(T_{a,b}\) be the map of \(\Omega_d\) that toggles these four pairs when every row and column of the cross matrix has sum one, and does nothing otherwise. It preserves all degrees and is an involution, so it acts on functions as a self-adjoint orthogonal operator, and
\[
g_{a,b}=\tfrac12\bigl(I-T_{a,b}\bigr)=g_{b,a}
\]
is an orthogonal projection. When \(T_{a,b}\) acts, it is a switch.

Fix the order \((i,j)\) of the endpoints of \(a\). In an \(a\)-fiber \(\mathcal F\) in which both \(k\) and \(l\) are singletons, let \(x_k\) and \(x_l\) indicate that \(k\), respectively \(l\), is adjacent to \(i\), and put
\[
z^{\mathcal F}_{kl}=\mathbf 1_{\{x_k=x_l\}}-\mathbb P\bigl(x_k=x_l\mid\mathcal F\bigr),
\]
a function on \(\mathcal F\). On such a fiber let \(R_{a,b}\) be the orthogonal projection onto the multiples of \(z^{\mathcal F}_{kl}\) (zero if \(z^{\mathcal F}_{kl}=0\)); on the other \(a\)-fibers let \(R_{a,b}=0\). Since the fibers partition \(\Omega_d\), this defines an orthogonal projection \(R_{a,b}\) on all functions. It does not depend on the order of \(i,j\), but \(R_{a,b}\) and \(R_{b,a}\) are different operators.

**Proposition 1.1** (OpenAI). For disjoint pairs \(a,b\) and every function \(f\) on \(\Omega_d\),
\[
2\langle h_af,h_bf\rangle\ge2\|g_{a,b}f\|^2-\|R_{a,b}f\|^2-\|R_{b,a}f\|^2 .\tag{1.1}
\]

**Proof.** Let \(O=V\setminus(a\cup b)\).

*Cells.* Call two graphs equivalent if they have the same edges inside \(O\), agree on the edges \(ij\) and \(kl\), and every \(w\in O\) has the same number of neighbours in \(a\) and the same number of neighbours in \(b\) in both. A resampling at \(a\) changes only vertex pairs between \(a\) and its singletons and keeps all the recorded data (a vertex \(w\in O\) keeps its edges to \(b\)); the same holds for \(b\). So every \(a\)-fiber and every \(b\)-fiber lies in one equivalence class, a *cell*, and all operators in (1.1) map functions supported on a cell to functions supported on it. It suffices to prove (1.1) on each cell, with its uniform measure.

*Coordinates on a cell.* Let \(A_0\subseteq O\) be the vertices with exactly one neighbour in \(a\), and \(B_0\subseteq O\) those with exactly one neighbour in \(b\) (the two sets may overlap). A graph of the cell is described by its cross matrix \(M\), the set \(U\subseteq A_0\) of vertices of \(A_0\) adjacent to \(i\), and the set \(W\subseteq B_0\) of vertices of \(B_0\) adjacent to \(k\); every other vertex pair is fixed by the cell. The sum \(s\) of the entries of \(M\) is fixed, since \(d_i+d_j=2[ij]+\sum_{w\in O}|N(w)\cap a|+s\). Let
\[
r=[ik]+[il],\qquad c=[ik]+[jk]
\]
be the first row sum and the first column sum of \(M\). The degree conditions at \(i\) and \(k\) read
\[
|U|=q_0-r,\qquad |W|=q_1-c\tag{1.2}
\]
for integers \(q_0,q_1\) fixed by the cell; the degrees of \(j\) and \(l\) then follow from the fixed totals \(d_i+d_j\) and \(d_k+d_l\), and the degrees of the vertices in \(O\) are fixed by the cell. So the cell is in bijection with the triples \((M,U,W)\) where \(M\) is a \(0/1\) matrix with entry sum \(s\), and \(U\subseteq A_0\), \(W\subseteq B_0\) satisfy (1.2); an overlap of \(A_0\) and \(B_0\) imposes no constraint, because the two assignments concern different edges. All these triples have the same probability.

*The two conditional expectations.* Inside the cell, the \(a\)-fiber of a graph is determined by \(X=(c,W)\): \(c\) and \(s-c\) are the numbers of neighbours of \(k\) and \(l\) in \(a\), and \(W\) gives the remaining edges with no endpoint in \(a\). Conversely the \(a\)-fiber determines \(X\). Likewise the \(b\)-fiber is determined by \(Y=(r,U)\). Hence, on the cell,
\[
E_a=\mathbb E[\,\cdot\mid X],\qquad E_b=\mathbb E[\,\cdot\mid Y].\tag{1.3}
\]
Let \(\mathcal A\) and \(\mathcal B\) be the spaces of functions of \(X\) and of \(Y\) (both contain the constants), and \(\mathcal J=(\mathcal A+\mathcal B)^\perp\). The map \(T_{a,b}\) changes neither \(X\) nor \(Y\), so \(g_{a,b}\) kills \(\mathcal A\) and \(\mathcal B\), and being self-adjoint, it has range in \(\mathcal J\):
\[
\|g_{a,b}f\|\le\|\operatorname{proj}_{\mathcal J}f\|.\tag{1.4}
\]

*When \(X\) and \(Y\) are independent.* Then \(E_aE_b=E_bE_a\) is the projection onto the constants, the spaces \(\mathcal A\ominus\mathbb R\) and \(\mathcal B\ominus\mathbb R\) are orthogonal, and \(h_ah_b=I-E_a-E_b+E_aE_b\) is the orthogonal projection onto \(\mathcal J\). Hence \(2\langle h_af,h_bf\rangle=2\|\operatorname{proj}_{\mathcal J}f\|^2\ge2\|g_{a,b}f\|^2\) by (1.4), which is stronger than (1.1). This happens in the following cases.

- \(s=0\) or \(s=4\): \(M\) is fixed, \(U\) and \(W\) are independent uniform subsets of fixed sizes.
- \(s=1\) or \(s=3\): \(M\) is determined by \((r,c)\), which locates its single one or its single zero, so the probability of \((M,U,W)\) is a product of a function of \((r,U)\) and a function of \((c,W)\).
- \(s=2\), when one of the events \(D_r=\{r\neq1\}\), \(D_c=\{c\neq1\}\) or the *center* \(\{r=c=1\}\) has probability zero; see below.

For \(s=2\) the six matrices with two ones are arranged by \((r,c)\) as follows:
\[
\begin{array}{c|ccc}
 & c=0 & c=1 & c=2\\ \hline
r=0 & - & \begin{pmatrix}0&0\\1&1\end{pmatrix} & -\\
r=1 & \begin{pmatrix}0&1\\0&1\end{pmatrix} & \begin{pmatrix}1&0\\0&1\end{pmatrix},\ \begin{pmatrix}0&1\\1&0\end{pmatrix} & \begin{pmatrix}1&0\\1&0\end{pmatrix}\\
r=2 & - & \begin{pmatrix}1&1\\0&0\end{pmatrix} & -
\end{array}
\]
Let \(m_{rc}\) be the number of matrices at \((r,c)\): \(m_{11}=2\), \(m_{01}=m_{10}=m_{12}=m_{21}=1\), and \(m_{rc}=0\) at the corners. The probability of \((M,U,W)\) is proportional to \(\mathbf 1[|U|=q_0-r]\,\mathbf 1[|W|=q_1-c]\), and summing over the matrices at \((r,c)\),
\[
\mathbb P(r,U,c,W)\ \text{is proportional to}\ m_{rc}\,\mathbf 1\bigl[|U|=q_0-r\bigr]\,\mathbf 1\bigl[|W|=q_1-c\bigr].\tag{1.5}
\]
The events \(D_r\) and \(D_c\) are disjoint, since the corners are empty. If both have positive probability, the center has positive probability too: \(D_r\) requires \(c=1\) and a subset \(W\) of size \(q_1-1\), \(D_c\) requires \(r=1\) and a subset \(U\) of size \(q_0-1\), and these \(U,W\) together with either central matrix form a triple of the cell. If \(D_c\) has probability zero, then \(c=1\) always, \(m_{rc}\) in (1.5) depends on \(r\) only, and (1.5) is a product of a function of \((r,U)\) and a function of \(W\); the case \(\mathbb P(D_r)=0\) is symmetric. If the center has probability zero, one of \(D_r,D_c\) has probability zero by what was just shown. In all these cases \(X\) and \(Y\) are independent.

*The remaining case.* Let \(s=2\) and let \(D_r\), \(D_c\) and the center all have positive probability. Put \(p_r=\mathbb P(D_r)\), \(p_c=\mathbb P(D_c)\), so that \(p_r,p_c>0\) and \(p_r+p_c<1\), and let
\[
u=\frac{\mathbf 1_{D_c}-p_c}{\sqrt{p_c(1-p_c)}}\in\mathcal A,\qquad v=\frac{\mathbf 1_{D_r}-p_r}{\sqrt{p_r(1-p_r)}}\in\mathcal B,
\]
unit vectors with mean zero. Since \(D_r\cap D_c=\varnothing\),
\[
\langle u,v\rangle=-\rho,\qquad \rho=\sqrt{\frac{p_rp_c}{(1-p_r)(1-p_c)}}\in(0,1).
\]
By (1.5), given \(X=(c,W)\), the law of \(Y\) depends on \(c\) only through whether \(c=1\): if \(c\neq1\), then \(r=1\) and \(U\) is a uniform subset of size \(q_0-1\), the same for \(c=0\) and \(c=2\); if \(c=1\), the law of \((r,U)\) is proportional to \(m_{r1}\mathbf 1[|U|=q_0-r]\). Symmetrically, the law of \(X\) given \(Y\) depends only on whether \(r=1\). Consequently \(E_a\mathcal B\subseteq\operatorname{span}(1,u)\) and \(E_b\mathcal A\subseteq\operatorname{span}(1,v)\). Moreover \(\mathbb E[\mathbf 1_{D_r}\mid X]=\frac{p_r}{1-p_c}\mathbf 1_{\{c=1\}}\), because \(D_r\subseteq\{c=1\}\) and the law of \(Y\) is the same on all of \(\{c=1\}\); a short computation gives
\[
E_av=-\rho\,u,\qquad E_bu=-\rho\,v .
\]
Let \(\mathcal A'\) be the functions in \(\mathcal A\) orthogonal to \(1\) and \(u\), and \(\mathcal B'\) those in \(\mathcal B\) orthogonal to \(1\) and \(v\). For \(\alpha\in\mathcal A'\) and \(\beta\in\mathcal B\), \(\langle\alpha,\beta\rangle=\langle\alpha,E_a\beta\rangle=0\), since \(E_a\beta\in\operatorname{span}(1,u)\); so \(\mathcal A'\perp\mathcal B\), and likewise \(\mathcal B'\perp\mathcal A\). The space of functions on the cell is therefore the orthogonal sum
\[
\operatorname{span}(1)\oplus\mathcal A'\oplus\mathcal B'\oplus\operatorname{span}(u,v)\oplus\mathcal J ,
\]
and each summand is invariant under \(E_a\) and \(E_b\): both act as the identity on \(\operatorname{span}(1)\); on \(\mathcal A'\), \(E_a\) is the identity and \(E_b\) is zero; on \(\mathcal B'\) the reverse; both vanish on \(\mathcal J\); and on the plane \(E_au=u\), \(E_av=-\rho u\), \(E_bv=v\), \(E_bu=-\rho v\). The summands \(\operatorname{span}(1)\), \(\mathcal A'\), \(\mathcal B'\) contribute nothing to \(\langle h_af,h_bf\rangle\), and \(\mathcal J\) contributes \(\|\operatorname{proj}_{\mathcal J}f\|^2\). On the plane write the component of \(f\) as \(xu+yv\); then
\[
h_a(xu+yv)=y(v+\rho u),\qquad h_b(xu+yv)=x(u+\rho v),
\]
and the vectors \(v+\rho u\) and \(u+\rho v\) have squared norm \(1-\rho^2\) and inner product \(\rho(1-\rho^2)\). Since \(2|xy|\rho\le x^2+y^2\),
\[
2xy\rho(1-\rho^2)\ge-(x^2+y^2)(1-\rho^2)=-\|y(v+\rho u)\|^2-\|x(u+\rho v)\|^2 .
\]
Altogether
\[
2\langle h_af,h_bf\rangle\ge2\|\operatorname{proj}_{\mathcal J}f\|^2-\|y(v+\rho u)\|^2-\|x(u+\rho v)\|^2 .\tag{1.6}
\]

*The error terms.* The vector \(y(v+\rho u)\) is the orthogonal projection of \(f\) onto the line spanned by \(v+\rho u\): this vector lies in the plane, is orthogonal to \(u\), and has inner product \(1-\rho^2\) with \(v\). Moreover \(v+\rho u=v-E_av\). On an \(a\)-fiber of the cell with \(c\neq1\), the function \(v\) is constant, so \(v-E_av=0\) there. On an \(a\)-fiber with \(c=1\), the vertices \(k\) and \(l\) each have exactly one neighbour in \(a\), so they are singletons, and \(r\neq1\) exactly when \(x_k=x_l\); there
\[
v-E_av=\frac{\mathbf 1_{\{x_k=x_l\}}-\mathbb P(x_k=x_l\mid X)}{\sqrt{p_r(1-p_r)}},
\]
a multiple of \(z^{\mathcal F}_{kl}\). So the line spanned by \(v+\rho u\) lies in the range of \(R_{a,b}\). If \(\Pi\) is the projection onto a line inside the range of a projection \(R\), then \(\Pi=\Pi R\) and \(\|\Pi f\|\le\|Rf\|\). Hence \(\|y(v+\rho u)\|^2\le\|R_{a,b}f\|^2\), and in the same way \(\|x(u+\rho v)\|^2\le\|R_{b,a}f\|^2\). With (1.6) and (1.4) this proves (1.1) on the cell. \(\square\)

## 2. Equality indicators on a slice

Let \(N\ge0\) and \(0\le q\le N\), and let \(\mathcal X_{N,q}\) be the set of \(x\in\{0,1\}^N\) with \(q\) ones, with the uniform measure. Let \(\tau_{ij}\) exchange the coordinates \(i\) and \(j\), acting on functions by \((\tau_{ij}f)(x)=f(\tau_{ij}x)\), and put
\[
G=\frac12\sum_{i<j}(I-\tau_{ij}).
\]
For \(i<j\) let \(Q_{ij}\) be the orthogonal projection onto the multiples of \(z_{ij}=\mathbf 1_{\{x_i=x_j\}}-\mathbb P(x_i=x_j)\) (zero if \(z_{ij}=0\)), and \(S=\sum_{i<j}Q_{ij}\).

**Lemma 2.1** (OpenAI). \(S\preceq G\).

The functions \(z_{ij}\) are quadratic in the coordinates, so they live in the first two levels of the decomposition of functions on the slice into eigenspaces of \(G\) [Filmus]; the proof computes the two relevant eigenvalues directly.

**Proof.** Each \(\frac12(I-\tau_{ij})\) is an orthogonal projection, so \(G\succeq0\). If every \(z_{ij}\) vanishes, then \(S=0\); this covers \(N\le2\) and \(q\in\{0,N\}\). Let \(N\ge3\), \(1\le q\le N-1\) and \(r=N-q\). Then
\[
p=\mathbb P(x_i=x_j)=\frac{q(q-1)+r(r-1)}{N(N-1)},\qquad 1-p=\frac{2qr}{N(N-1)},\qquad\|z_{ij}\|^2=p(1-p)>0 .
\]
Let \(m=\binom N2\), index \(\mathbb R^m\) by the pairs \(i<j\), write \(c_{ji}=c_{ij}\), and define \(B\colon\mathbb R^m\to L^2(\mathcal X_{N,q})\) by \(Bc=\sum_{i<j}c_{ij}z_{ij}/\sqrt{p(1-p)}\). Then \(S=BB^*\). Let \(K=B^*B\), the Gram matrix of the normalized \(z_{ij}\), and decompose \(\mathbb R^m\) orthogonally as
\[
\mathcal C_0=\{c\text{ constant}\},\quad \mathcal C_1=\Bigl\{c_{ij}=u_i+u_j:\ \sum_iu_i=0\Bigr\},\quad \mathcal C_2=\Bigl\{c:\ \sum_{j\neq i}c_{ij}=0\text{ for every }i\Bigr\}.
\]
Indeed, the map \(u\mapsto(u_i+u_j)_{i<j}\) is injective for \(N\ge3\) (if \(u_i+u_j=0\) for all pairs, then \(u_i=-u_j=u_k=-u_i\) on every triangle), its image is \(\mathcal C_0\oplus\mathcal C_1\) (constant \(u\) gives \(\mathcal C_0\), and \(\sum_{i<j}(u_i+u_j)=(N-1)\sum_iu_i\)), and the orthogonal complement of its image is \(\mathcal C_2\). The dimensions are \(1\), \(N-1\) and \(m-N\).

*\(K\) acts by scalars.* The number of pairs \(i<j\) with \(x_i=x_j\) is \(\binom q2+\binom r2\) on the whole slice, so \(\sum_{i<j}z_{ij}=0\) and \(B\) kills \(\mathcal C_0\). The measure is invariant under permutations of the coordinates, so the entry of \(K\) at two pairs depends only on the size of their intersection: \(K=I+\kappa_1A_1+\kappa_0A_0\), where \((A_1c)_{ij}\) sums \(c\) over the pairs meeting \(\{i,j\}\) in one point and \((A_0c)_{ij}\) over the pairs disjoint from it. For \(c\in\mathcal C_1\) the row sums are \(\sum_{l\neq i}c_{il}=(N-2)u_i\) and the total is \(0\), so \((A_1c)_{ij}=(N-2)(u_i+u_j)-2c_{ij}=(N-4)c_{ij}\) and \((A_0c)_{ij}=0-c_{ij}-(N-4)c_{ij}=-(N-3)c_{ij}\). For \(c\in\mathcal C_2\) the row sums and the total vanish, so \((A_1c)_{ij}=-2c_{ij}\) and \((A_0c)_{ij}=c_{ij}\). Hence \(K\) acts on \(\mathcal C_1\) by a scalar \(\mu_1\) and on \(\mathcal C_2\) by a scalar \(\mu_2\), both nonnegative because \(K\succeq0\).

*The value of \(\mu_1\).* The number of coordinates \(j\neq i\) with \(x_j=x_i\) is \(q-1\) if \(x_i=1\) and \(r-1\) if \(x_i=0\), that is, \((r-1)+(2q-N)x_i\). For \(u\) with \(\sum_iu_i=0\),
\[
\sum_{i<j}(u_i+u_j)z_{ij}=\sum_iu_i\sum_{j\neq i}\mathbf 1_{\{x_i=x_j\}}-p(N-1)\sum_iu_i=(2q-N)\sum_iu_ix_i .\tag{2.1}
\]
For a uniform \(q\)-subset, \(\operatorname{Var}x_i=qr/N^2\) and \(\operatorname{Cov}(x_i,x_j)=-qr/(N^2(N-1))\), so \(\sum_iu_ix_i\) has mean zero and
\[
\Bigl\|\sum_iu_ix_i\Bigr\|^2=\frac{qr}{N(N-1)}\sum_iu_i^2,\qquad \sum_{i<j}(u_i+u_j)^2=(N-2)\sum_iu_i^2 .
\]
Comparing \(\|Bc\|^2=\mu_1\|c\|^2\) for \(c_{ij}=u_i+u_j\) and using \(1-p=2qr/(N(N-1))\),
\[
\mu_1=\frac{(2q-N)^2}{2(N-2)p}.
\]
We claim \(\mu_1\le N/2\). Indeed, with \(q^2+r^2=N^2-2qr\),
\[
N(N-2)p-(2q-N)^2=\frac{(N-2)(N^2-N-2qr)}{N-1}-(N^2-4qr)=\frac{2N}{N-1}\bigl(qr-(N-1)\bigr),
\]
and \(qr-(N-1)=(q-1)(r-1)\ge0\).

*A bound on \(\mu_2\).* The diagonal entries of \(K\) are \(1\), so \(\operatorname{tr}K=m=(N-1)\mu_1+(m-N)\mu_2\). For \(N\ge4\) this gives \(\mu_2\le\frac m{m-N}=\frac{N-1}{N-3}\le N-1\). (For \(N=3\), \(\mathcal C_2=\{0\}\).)

*The eigenvalues of \(G\).* Directly from the definition,
\[
Gx_i=\frac12\sum_{l\neq i}(x_i-x_l)=\frac{Nx_i-q}2 ,
\]
and, since only exchanges of exactly one of \(i,j\) with a third coordinate change \(x_ix_j\),
\[
G(x_ix_j)=(N-2)x_ix_j-\tfrac12(x_i+x_j)\sum_{l\neq i,j}x_l=(N-1)x_ix_j-\frac{q-1}2(x_i+x_j),
\]
using \(x_i^2=x_i\) and \(\sum_lx_l=q\). By (2.1), \(B\mathcal C_1\) consists of multiples of functions \(\sum_iu_ix_i\) with \(\sum_iu_i=0\), on which \(G\) acts by \(N/2\). For \(c\in\mathcal C_2\), write \(z_{ij}=1-p-x_i-x_j+2x_ix_j\); the constant and linear terms cancel because the row sums of \(c\) vanish, so \(Bc\) is a multiple of \(\sum_{i<j}c_{ij}x_ix_j\), on which \(G\) acts by \(N-1\) for the same reason.

*Comparison.* The subspaces \(\mathcal U_1=B\mathcal C_1\) and \(\mathcal U_2=B\mathcal C_2\) are orthogonal, since \(\langle Bc,Bc'\rangle=\langle c,Kc'\rangle\), and \(S=BB^*\) acts on \(\mathcal U_t\) by \(\mu_t\): \(SBc=BKc=\mu_tBc\) for \(c\in\mathcal C_t\). The range of \(B\) is \(\mathcal U_1+\mathcal U_2\), so \(S=0\) on its orthogonal complement, which is invariant under \(G\) because \(\mathcal U_1\) and \(\mathcal U_2\) are. On \(\mathcal U_1\), \(S=\mu_1\le N/2=G\); on \(\mathcal U_2\), \(S=\mu_2\le N-1=G\); on the complement, \(S=0\preceq G\). Since \(S\) and \(G\) both preserve these three orthogonal subspaces, \(S\preceq G\). \(\square\)

**Corollary 2.2** (OpenAI). For every pair \(a\) and every function \(f\) on \(\Omega_d\),
\[
\sum_{b\cap a=\varnothing}\|R_{a,b}f\|^2\le\sum_{b\cap a=\varnothing}\|g_{a,b}f\|^2 .
\]

**Proof.** Fix an \(a\)-fiber, identified with a slice \(\mathcal X_{N,q}\) of its \(N\) singletons by recording which of them are adjacent to \(i\) (Lemma 4.1 of [The switch chain](the-switch-chain.md)). If both vertices of \(b=\{k,l\}\) are singletons, the cross matrix has column sums one, and \(T_{a,b}\) exchanges the assignments of \(k\) and \(l\) when they differ and does nothing when they agree; so on the fiber \(T_{a,b}=\tau_{kl}\), \(g_{a,b}=\frac12(I-\tau_{kl})\) and \(R_{a,b}=Q_{kl}\). If \(k\) or \(l\) is not a singleton, a column sum of the cross matrix is \(0\) or \(2\), and \(g_{a,b}\) and \(R_{a,b}\) both vanish on the fiber. Since \(\|Qf\|^2=\langle f,Qf\rangle\) for a projection \(Q\), on the fiber the two sides are \(\langle f,Sf\rangle\) and \(\langle f,Gf\rangle\), and Lemma 2.1 compares them. All operators preserve the fibers, so averaging over the fibers proves the corollary. \(\square\)

## 3. The operator inequality

**Corollary 3.1** (OpenAI). The operator
\[
D=\sum_{(a,b):\ a\cap b=\varnothing}h_ah_b ,
\]
summed over ordered pairs of disjoint vertex pairs, is self-adjoint and positive semidefinite.

**Proof.** Both orders of every disjoint pair occur, and \((h_ah_b)^*=h_bh_a\), so \(D\) is self-adjoint. By Proposition 1.1, with the sum over unordered pairs \(\{a,b\}\) of disjoint vertex pairs,
\[
\langle f,Df\rangle=\sum_{\{a,b\}}2\langle h_af,h_bf\rangle\ge\sum_{\{a,b\}}\bigl(2\|g_{a,b}f\|^2-\|R_{a,b}f\|^2-\|R_{b,a}f\|^2\bigr)=\sum_a\Bigl(\sum_{b\cap a=\varnothing}\|g_{a,b}f\|^2-\sum_{b\cap a=\varnothing}\|R_{a,b}f\|^2\Bigr),
\]
where the last step gives each pair \(\{a,b\}\) one copy of \(\|g_{a,b}f\|^2=\|g_{b,a}f\|^2\) at \(a\) and one at \(b\). Each inner difference is nonnegative by Corollary 2.2. \(\square\)

**Lemma 3.2.** With \(H_T\) as in [A variance inequality for three rows](a-variance-inequality-for-three-rows.md),
\[
H^2=\sum_{T\in\binom V3}H_T^2-(n-3)H+D .
\]

**Proof.** \(H^2=\sum_{a,b}h_ah_b\) over ordered pairs. The terms with \(a=b\) give \(\sum_ah_a^2=H\). An ordered pair of different intersecting pairs \(a,b\) lies in exactly one triple, namely \(a\cup b\), and the disjoint pairs give \(D\). On the other hand, \(\sum_TH_T^2\) contains every ordered pair of different intersecting pairs once and every term \(h_a^2=h_a\) once for each of the \(n-2\) triples containing \(a\). Hence \(\sum_TH_T^2=(n-2)H+(H^2-H-D)\), which is the claim. \(\square\)

**Theorem 3.3** (OpenAI). \(H^2\succeq H\).

**Proof.** By Lemma 3.2, Theorem 4.1 of [A variance inequality for three rows](a-variance-inequality-for-three-rows.md) and Corollary 3.1,
\[
H^2\succeq\sum_TH_T-(n-3)H=(n-2)H-(n-3)H=H,
\]
since every pair lies in \(n-2\) triples. \(\square\)

With Proposition 5.3 of [The switch chain](the-switch-chain.md), Theorem 3.3 proves the mixing theorem: for \(n\ge4\) and every graphical \(d\), the switch chain has spectral gap at least \(\bigl[24n^2\binom n4\bigr]^{-1}\) when \(|\Omega_d|>1\), and mixing time at most \(2n^8\).

## 4. Exercises

**Exercise 4.1** (medium). Let \(n=5\), \(d=(1,2,1,2,2)\), \(a=\{1,2\}\) and \(b=\{3,4\}\). Let \(G'\) have the edges \(15,23,24,45\) and \(G''\) the edges \(14,24,25,35\), and let \(f=\mathbf 1_{\{G'\}}-\mathbf 1_{\{G''\}}\). Find the \(a\)-fibers and \(b\)-fibers of \(G'\) and \(G''\), and show that \(\langle h_af,h_bf\rangle<0\). (The set \(\Omega_d\) has seven elements.)

**Exercise 4.2** (easy). Check Lemma 2.1 by hand for \(N=4\), \(q=2\): show that \(z_{12}=z_{34}\), \(z_{13}=z_{24}\), \(z_{14}=z_{23}\), and that \(S\) has the eigenvalue \(3=N-1\), so the bound \(\mu_2\le N-1\) is attained.

**Exercise 4.3** (medium). Show that for \(N\ge4\) and \(q\in\{1,N-1\}\), \(\mu_1=N/2\) and \(\mu_2=0\), and that for \(q=N/2\), \(\mu_1=0\).

**Exercise 4.4** (easy). Show that the identity of Lemma 3.2 holds for any family of orthogonal projections \(h_a\) indexed by the pairs of an \(n\)-element set, with \(H\), \(H_T\) and \(D\) defined in the same way.

## 5. Solutions

**4.1.** In \(G'\) the vertices \(3,4,5\) each have one neighbour in \(\{1,2\}\), only \(5\) is adjacent to \(1\), and the only edge avoiding \(\{1,2\}\) is \(45\). So the \(a\)-fiber of \(G'\) consists of the three graphs obtained by joining one of \(3,4,5\) to \(1\) and the other two to \(2\), together with the edge \(45\): \(G'\), \(G_1=\{13,24,25,45\}\) and \(G_2=\{14,23,25,45\}\). In \(G''\), vertex \(4\) has two neighbours in \(\{1,2\}\), vertex \(3\) none and vertex \(5\) one, so its \(a\)-fiber is \(\{G''\}\). Symmetrically, the \(b\)-fiber of \(G''\) is \(\{G'',G_1,G_2\}\) (one of \(1,2,5\) is joined to \(3\), the edge \(25\) stays), and the \(b\)-fiber of \(G'\) is \(\{G'\}\). Hence \(h_af\) is \(\frac23\) at \(G'\), \(-\frac13\) at \(G_1,G_2\) and \(0\) elsewhere, and \(h_bf\) is \(-\frac23\) at \(G''\), \(\frac13\) at \(G_1,G_2\) and \(0\) elsewhere. So \(\langle h_af,h_bf\rangle=\frac17\bigl(-\frac19-\frac19\bigr)=-\frac2{63}<0\). In the proof of Proposition 1.1, this cell is \(\{G',G'',G_1,G_2\}\) with \(s=2\), \(p_r=p_c=\frac14\) and \(\rho=\frac13\), and \(f\) lies in the plane spanned by \(u\) and \(v\).

**4.2.** With two ones among four coordinates, \(x_1=x_2\) holds exactly when \(x_3=x_4\), so \(z_{12}=z_{34}\), and similarly for the other two matchings. The three functions are distinct, orthogonal to the constants, and their sum is zero, so they span a plane. Each projection \(Q_{ij}\) appears twice, so \(S=2(Q_{12}+Q_{13}+Q_{14})\). Since \(p=\frac13\), the normalized functions \(\hat z_{12},\hat z_{13},\hat z_{14}\) have pairwise inner products \(-\frac12\) (their sum is zero), so \(\sum\hat z\hat z^*\) acts on their plane by \(\frac32\), and \(S\) acts by \(3\). Also \(\mu_1=0\) because \(2q=N\), and the trace identity gives \(2\mu_2=6\).

**4.3.** For \(q=1\): \(r=N-1\), \(p=\frac{(N-1)(N-2)}{N(N-1)}=\frac{N-2}N\), so \(\mu_1=\frac{(N-2)^2}{2(N-2)(N-2)/N}=\frac N2\). The trace identity \(m=(N-1)\frac N2+(m-N)\mu_2=m+(m-N)\mu_2\) gives \(\mu_2=0\). The case \(q=N-1\) is symmetric, and \(q=N/2\) gives \(2q-N=0\).

**4.4.** The proof of Lemma 3.2 uses only \(h_a^2=h_a\) and the counting of pairs and triples.

## References

- [OpenAI-SW] OpenAI, *Polynomial mixing of the switch chain for every graphical degree sequence*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026
- [Caputo] P. Caputo, *On the spectral gap of the Kac walk and other binary collision processes*, ALEA Latin American Journal of Probability and Mathematical Statistics 4 (2008), 205–222. https://alea.impa.br/articles/v4/04-10.pdf
- [CBS] C. J. Carstens, A. Berger and G. Strona, *A unifying framework for fast randomization of ecological networks with fixed (node) degrees*, MethodsX 5 (2018), 773–780; extended version. https://arxiv.org/abs/1609.05137
- [Filmus] Y. Filmus, *An orthogonal basis for functions over a slice of the Boolean hypercube*, Electronic Journal of Combinatorics 23 (2016), P1.23. https://doi.org/10.37236/4567
