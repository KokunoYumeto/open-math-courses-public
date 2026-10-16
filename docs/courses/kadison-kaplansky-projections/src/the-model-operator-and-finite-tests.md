# The model operator and finite tests

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The *model operator* puts the transverse projections \(p(t)\) of the previous lesson on the tower: each normalized incidence of \(Y^0\) between \(B_k\) and \(A_i\) is tensored with \(h_i(t)h_k(t)p(t)\). Its upper band is spanned by layerwise constant vectors on the one or two active layers, tensored with the range of \(p(t)\); its identity trace equals the trace of \(p(t)\), and the rest of the spectrum lies below \(1-\chi\). The *realization theorem* states that a weighted adjacency operator on a voltage cover of \(Y\), with finitely many matrix weights and with large girth, approximates the compressed model in norm. This lesson proves the statements about the model, states the realization theorem, and proves two tools for its proof: norms in the regular representation of \(F\) are tested on finite boxes, and expectations of random operators are replaced by finite empirical averages [OpenAI-KK, Sections 9.1 to 9.3].

- Spaces and fibers (Section 1).
- The model operator (Section 2).
- The realization theorem (Section 3).
- Finite tests in the nilpotent group (Section 4).
- Empirical averages (Section 5).

## 1. Spaces and fibers

The notation of [Pruning and recovery of long paths](pruning-and-recovery-of-long-paths.md) and of the three preceding lessons is in force. Let \(V^0\) be the disjoint union of all \(A_i\) and \(B_i\), \(i\in\mathbb Z\), the vertex set of \(Y^0\), and \(V(Y)\subseteq V^0\) that of \(Y\). Positive edges go from \(A\) to \(B\). For an adjacent pair \((i,k)\), the *normalized incidence* \(U^0_{ik}:\ell^2(B_k)\to\ell^2(A_i)\) of \(Y^0\) is
\[
(U^0_{ik}f)(a)=(dD_{ik})^{-1/2}\sum_{e:\,a\to b,\ b\in B_k}f(b) .
\]
With \(a_i=|A_i|^{-1/2}\mathbf1_{A_i}\) and \(b_k=|B_k|^{-1/2}\mathbf1_{B_k}\), Proposition 4.1(1) of that lesson gives \(U^0_{ik}b_k=a_i\), \(U^{0*}_{ik}a_i=b_k\), and \(\|U^0_{ik}f\|\le(1-\chi)\|f\|\) for \(f\perp b_k\), with \(\chi=\frac1{800}\). Since \(\langle U^0_{ik}f,a_i\rangle=\langle f,b_k\rangle\), the operator \(U^0_{ik}\) maps \(b_k^\perp\) into \(a_i^\perp\), and \(U^{0*}_{ik}\) maps \(a_i^\perp\) into \(b_k^\perp\); in particular \(\|U^0_{ik}\|=1\).

The Hilbert space of the construction is
\[
\mathcal H^0=\ell^2(V^0)\otimes\ell^2(F)\otimes\mathbb C^N ,
\]
with \(N=q^{n_{\mathrm f}}\) of the previous lesson, and \(\Pi\) is the projection onto \(\ell^2(V(Y))\otimes\ell^2(F)\otimes\mathbb C^N\). On \(\ell^2(F)\) let \((\rho(g)\xi)(f)=\xi(fg)\) and \((\lambda(a)\xi)(f)=\xi(a^{-1}f)\). For \(W\in M_N(\mathbb C)\) we write \(W\rho(g)\) for \(\rho(g)\otimes W\). The operators of the cover are built from such terms; they commute with the left translations \(1\otimes\lambda(a)\otimes1\), the *deck transformations*.

The unitary \((\mathcal I\xi)(f)=\xi(f^{-1})\) satisfies \(\mathcal I\rho(g)\mathcal I=\lambda(g)\), \(\mathcal I\lambda(a)\mathcal I=\rho(a)\) and \(\mathcal I\delta_1=\delta_1\). Composed with the central Fourier transform (5.1) of [An affine nilpotent group](an-affine-nilpotent-group.md), it gives
\[
\begin{gathered}
\mathcal H^0\cong L^2\bigl(\mathbb T;\mathcal H^0_t\bigr),\\
\mathcal H^0_t=\ell^2(V^0)\otimes\mathcal H_t,\\
\mathcal H_t=\ell^2(L)\otimes\ell^2(L)\otimes\mathbb C^N ,
\end{gathered}
\]
in which, by Lemma 5.1 of that lesson, \(W\rho\bigl(\sigma_X(\gamma)\sigma_Y(\gamma')z_0^n\bigr)\) acts in the fiber at \(t\) by
\[
\mathbf e(nt)\,u_t(\gamma)\otimes u_t(\gamma')\otimes W ,\tag{1.1}
\]
and the left translations act by products of the right operators \(v_t(k)\otimes1\otimes1\), \(1\otimes v_t(k')\otimes1\), their inverses and scalars. Operators built from (1.1) therefore have *equivariant* fibers, commuting with the right phase action \(v_t\otimes v_t\otimes1_N\). The operator norm on \(\mathcal H^0\), the *regular norm*, is the essential supremum of the fiber norms (Lemma 4.1 of that lesson). For \(B\ge0\) commuting with the deck transformations and decomposed into equivariant fibers, the identity trace
\[
\begin{gathered}
\operatorname{Tr}_F(B)=\sum_{v\in V^0}\sum_{j=1}^N\langle Bx_{v,j},x_{v,j}\rangle\\
(x_{v,j}=\delta_v\otimes\delta_1\otimes e_j)
\end{gathered}
\]
equals \(\int_{\mathbb T}\operatorname{Tr}(B(t))\,dt\), where \(\operatorname{Tr}\) is the identity trace of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md) on \(\mathcal H^0_t\), summed over all vertex and matrix indices. This is Lemma 5.2 of [An affine nilpotent group](an-affine-nilpotent-group.md), applied to \(\mathcal IB\mathcal I\), which has the same diagonal at \(\delta_1\); the countable vertex index changes nothing, by Tonelli's theorem.

## 2. The model operator

For \(0<t<\delta\) define a bounded operator \(O(t)\) on \(\mathcal H^0_t\) by its blocks from \(\ell^2(B_k)\otimes\mathcal H_t\) to \(\ell^2(A_i)\otimes\mathcal H_t\),
\[
\begin{gathered}
O(t)_{A_iB_k}\\
=U^0_{ik}\otimes h_i(t)h_k(t)\,p(t)\\
(|i-k|\le1),
\end{gathered}\tag{2.1}
\]
the adjoint blocks from \(A_i\) to \(B_k\), and zero blocks otherwise; put \(O(t)=0\) for \(t\notin(0,\delta)\). Here \(p(t)\) and \(h_i(t)\) are those of [The magnetic factor and the weighted trace](the-magnetic-factor-and-the-weighted-trace.md), Sections 4 and 5. Since \(h_i(t)\ne0\) only for \(i\in J(t)\), a set of at most two adjacent integers, at most four blocks are nonzero. The field is bounded and measurable, with equivariant fibers, and defines the *model operator* \(O\) on \(\mathcal H^0\).

**Lemma 2.1** (the model band and its trace; [OpenAI-KK, Lemma 9.1]). For \(0<t<\delta\) define \(V_*(t):\mathcal H_t\to\mathcal H^0_t\) and \(E_*(t)\) by
\[
\begin{aligned}
&V_*(t)\zeta\\
&\quad=2^{-1/2}\sum_{i\in\mathbb Z}h_i(t)\,(a_i+b_i)\otimes p(t)\zeta,\\
&E_*(t)=V_*(t)V_*(t)^* ,
\end{aligned}
\]
and put \(E_*(t)=0\) for \(t\notin(0,\delta)\). For every \(t\):

1. \(O(t)E_*(t)=E_*(t)\), \(\|O(t)\|\le1\), and \(\langle O(t)x,x\rangle\le(1-\chi)\|x\|^2\) for \(x\in(1-E_*(t))\mathcal H^0_t\);
2. \(E_*(t)\) is an equivariant projection, and \(\operatorname{Tr}(E_*(t))=s_p(t)\) for \(0<t<\delta\), the identity trace of \(p(t)\) summed over the matrix indices;
3. \(\|(1-\Pi)E_*(t)\|\le\sqrt{\varepsilon_\ell}\).

*Proof.* For \(t\notin(0,\delta)\) all operators vanish. Fix \(0<t<\delta\) and write \(h_i=h_i(t)\), \(p=p(t)\). Let \(\mathcal C_t\subseteq\mathcal H^0_t\) be the closed span of the vectors \(a_i\otimes\zeta\) and \(b_i\otimes\zeta\), \(i\in\mathbb Z\), \(\zeta\in\mathcal H_t\), the *layerwise constant* vectors, and \(\mathcal C_t^\perp\) its orthogonal complement, the vectors of mean zero on every \(A_i\) and every \(B_i\). By Section 1, \(O(t)\) maps \(\mathcal C_t\) and \(\mathcal C_t^\perp\) into themselves.

On \(\mathcal C_t\), identify the \(A\)-part and the \(B\)-part with \(\ell^2(\mathbb Z)\otimes\mathcal H_t\) through \(a_i\otimes\zeta\mapsto e_i\otimes\zeta\) and \(b_i\otimes\zeta\mapsto e_i\otimes\zeta\). By (2.1), \(b_k\otimes\zeta\mapsto\sum_ih_ih_k\,a_i\otimes p\zeta\), because \(|i-k|\le1\) whenever \(h_ih_k\ne0\). So the part of \(O(t)\) from the \(B\)-side to the \(A\)-side is \(|h\rangle\langle h|\otimes p\), with the unit vector \(h=(h_i)_i\), and
\[
O(t)|_{\mathcal C_t}=\begin{pmatrix}0&|h\rangle\langle h|\otimes p\\|h\rangle\langle h|\otimes p&0\end{pmatrix} .
\]
This self-adjoint operator has eigenvalue \(1\) on the vectors \(2^{-1/2}(h\otimes\zeta,h\otimes\zeta)\), \(\zeta\in p\mathcal H_t\), which form the range of \(V_*(t)\); eigenvalue \(-1\) on the vectors \(2^{-1/2}(h\otimes\zeta,-h\otimes\zeta)\); and it vanishes on the orthogonal complement of these two spaces in \(\mathcal C_t\). Hence \(O(t)E_*(t)=E_*(t)\), and \(O(t)\le0\) on \(\mathcal C_t\ominus E_*(t)\mathcal H^0_t\).

On \(\mathcal C_t^\perp\), let \(\xi=(\xi_k)_k\) lie on the \(B\)-side, with \(\xi_k\in b_k^\perp\otimes\mathcal H_t\). The operator \(U^0_{ik}\otimes p\) has norm at most \(1-\chi\) on \(b_k^\perp\otimes\mathcal H_t\), so the component of \(O(t)\xi\) on \(A_i\) has norm at most \((1-\chi)h_i\sum_kh_k\|\xi_k\|\), and by the Cauchy–Schwarz inequality
\[
\begin{aligned}
&\sum_i\Bigl((1-\chi)h_i\sum_kh_k\|\xi_k\|\Bigr)^2\\
&\quad=(1-\chi)^2\Bigl(\sum_kh_k\|\xi_k\|\Bigr)^2\\
&\quad\le(1-\chi)^2\sum_k\|\xi_k\|^2 .
\end{aligned}
\]
So the part of \(O(t)\) from the \(B\)-side to the \(A\)-side has norm at most \(1-\chi\) on \(\mathcal C_t^\perp\); the part in the opposite direction is its adjoint, and the self-adjoint operator \(O(t)|_{\mathcal C_t^\perp}\) with these two off-diagonal parts has the same norm. Since \((1-E_*(t))\mathcal H^0_t=(\mathcal C_t\ominus E_*(t)\mathcal H^0_t)\oplus\mathcal C_t^\perp\), this proves statement 1.

For statement 2,
\[
\begin{aligned}
&\|V_*(t)\zeta\|^2\\
&\quad=\tfrac12\sum_ih_i^2\bigl(\|a_i\|^2+\|b_i\|^2\bigr)\|p\zeta\|^2\\
&\quad=\|p\zeta\|^2 ,
\end{aligned}
\]
so \(V_*(t)\) is a partial isometry with \(V_*^*V_*=p\) and \(V_*V_*^*=E_*\). It commutes with the right phase action, which acts on \(\mathcal H_t\) only and commutes with \(p\). By Lemma 2.1(4) of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md), for the group \(L\times L\) and the countable index sets of the two spaces, \(\operatorname{Tr}(E_*(t))=\operatorname{Tr}(p)=s_p(t)\).

For statement 3, let \(\zeta\in p\mathcal H_t\). The squared norm \(\|(1-\Pi)a_i\|^2\) is the deleted fraction of \(A_i\), at most \(\varepsilon_\ell\) by Proposition 4.1(2) of the pruning lesson, and the same holds for \(b_i\). So
\[
\begin{aligned}
&\|(1-\Pi)V_*(t)\zeta\|^2\\
&\quad=\tfrac12\sum_ih_i^2\bigl(\|(1-\Pi)a_i\|^2\\
&\qquad+\|(1-\Pi)b_i\|^2\bigr)\|\zeta\|^2\\
&\quad\le\varepsilon_\ell\|\zeta\|^2 ,
\end{aligned}
\]
and \(\|(1-\Pi)E_*(t)\|\le\|(1-\Pi)V_*(t)\|\), which is at most \(\sqrt{\varepsilon_\ell}\). \(\square\)

The upper space \(E_*(t)\mathcal H^0_t\) lies on at most two adjacent layers. Its vertex part is a normalized combination of constant vectors, so its trace is the fiber trace \(s_p(t)\), not \(s_p(t)\) times a number of vertices. As \(t\to0\) or \(t\to\delta\), the active layers move to \(-\infty\) or \(+\infty\) (Exercise 7.3 of the previous lesson), where the weights \(\mathfrak w_i\) are large, and Proposition 6.1 of that lesson keeps \(\mathfrak w_is_p(t)\) small.

## 3. The realization theorem

**Theorem 3.1** (realization of the model; [OpenAI-KK, Theorem 9.2]). For every fixed \(\eta>0\) and all large \(\ell\), there are voltages \(z_e\in F\) and matrices \(W_e\in M_N(\mathbb C)\) on the positive edges \(e\) of \(Y\) with the following properties.

1. \(\|W_e\|\le C_\eta\), where \(C_\eta\) does not depend on \(\ell\) or on the layer. The pairs \((\text{label of }e,W_e)\) form a finite set \(S\) with \(|S|=o(dD)\) as \(\ell\to\infty\). The number \(D_{ik}\) of an edge is determined by its label.
2. The voltage cover \(P\) of \(Y\) defined by the \(z_e\) satisfies the girth condition (2.1) of [Voltage covers and embedded copies](voltage-covers-and-embedded-copies.md).
3. Let \(T_P\) be the self-adjoint operator on \(\mathcal H^0\) whose blocks from \(B_k\) to \(A_i\) are, for \(a\in A_i\cap V(Y)\) and \(b\in B_k\cap V(Y)\),
\[
\begin{gathered}
(T_P)_{ab}=(dD_{ik})^{-1/2}\\
\cdot\sum_{e:\,a\to b}W_e\rho(z_e),
\end{gathered}\tag{3.1}
\]
whose blocks from \(A_i\) to \(B_k\) are the adjoints, and which vanishes on the deleted vertices. Then
\[
\|T_P-\Pi O\Pi\|\le\eta .\tag{3.2}
\]

Both operators in (3.2) have *layer width one*: their blocks between layers \(i\) and \(k\) vanish for \(|i-k|\ge2\). By Section 1, their fibers satisfy (3.2) for almost every \(t\); in particular \(\|T_P(t)\|\le\eta\) for almost every \(t\notin(0,\delta)\).

The refined labels \((\text{label},W_e)\) keep \(Y\) folded, and the recovery of long paths by their words survives refinement (Section 1 of [Voltage covers and embedded copies](voltage-covers-and-embedded-copies.md)). Under \(\ell^2(V(Y))\otimes\ell^2(F)=\ell^2(V(P))\), with \((v,f)\) corresponding to \(\delta_v\otimes\delta_f\), one has \(\rho(z_e)\delta_g=\delta_{gz_e^{-1}}\). So (3.1) sends a vector at \((b,g)\) to the vertices \((a,gz_e^{-1})\), the other ends of the edges \((a,f)\to(b,fz_e)\) of \(P\) over the edges \(e:a\to b\): \(T_P\) is the adjacency operator of \(P\) with the matrix weights \((dD_{ik})^{-1/2}W_e\), and it is reduced by the subspace of each connected component of \(P\).

The proof of Theorem 3.1 occupies the rest of this lesson and the next two. Norms in the regular representation are tested on finite matrices (Section 4), expectations of random operators are replaced by finite empirical averages (Section 5), the distribution of one random pair \((W,z)\) for each block is built in [Masks, lists and one draw per edge](masks-lists-and-one-draw-per-edge.md), and girth and the deviations of the independent edge draws from their means are controlled in [Girth and centered moments](girth-and-centered-moments.md).

## 4. Finite tests in the nilpotent group

The group \(F\) is coordinatized by the integer vectors \((\lambda_X,b_X-1,\lambda_Y,b_Y-1,z)\) of its elements \((\gamma_X,\gamma_Y,z)\), \(\gamma=(\lambda,b)\), with the weights of Lemma 2.1 of [An affine nilpotent group](an-affine-nilpotent-group.md): \(\operatorname{wt}(b-1)_{ij}=j-i\), \(\operatorname{wt}\lambda_{ij}=m-(j-i)\), \(\operatorname{wt}z=m\). There are \(4n_{\mathrm f}+1\) coordinates. The group law is a polynomial with integer coefficients, and the dilations \(\Delta_y\), acting on both factors and by \(z\mapsto y^mz\), are automorphisms of the group of real points, because \(c(\Delta_y\gamma,\Delta_y\eta)=y^mc(\gamma,\eta)\). Hence every coordinate of weight \(w\) of a product \(fg\) is a polynomial in the coordinates of \(f\) and \(g\) whose monomials all have total weight \(w\). Since \(f\cdot1=f\) and \(1\cdot g=g\), it is the sum of the coordinate of \(f\), the coordinate of \(g\), and monomials containing coordinates of both.

**Lemma 4.1** (finite norm tests; [OpenAI-KK, Lemma 9.3]). Fix \(a\ge1\) and \(B>0\). There are \(c,C\), depending only on \(a\), \(B\) and \(m\), with the following property. Let \(x\ge2\) and let \(G\subset F\) be a finite set, closed under inverses, whose elements have all coordinates bounded by \(x^a\) in absolute value.

1. There is a finite set \(\mathfrak B\subset F\) with \(|\mathfrak B|\le x^c\) and \(|\mathfrak B\,\triangle\,\mathfrak Bg|\le Cx^{-B}|\mathfrak B|\) for all \(g\in G\).
2. Let \(J\) be a finite set, \(n\ge1\), and
\[
A=\sum_{u,v\in J}\sum_{g\in G}E_{uv}\otimes\rho(g)\otimes C_{uv}(g)
\]
a self-adjoint operator on \(\ell^2(J)\otimes\ell^2(F)\otimes\mathbb C^n\), with matrix units \(E_{uv}\), coefficients \(C_{uv}(g)\in M_n(\mathbb C)\), and \(\max_u\sum_{v,g}\|C_{uv}(g)\|\le R\). If \(P\) is the projection keeping the deck indices in \(\mathfrak B\), then
\[
\begin{gathered}
\|PAP\|\le\|A\|\\
\le\|PAP\|+Cx^{-B}R .
\end{gathered}\tag{4.1}
\]

Neither \(c\) nor \(C\) depends on \(|G|\), \(|J|\) or \(n\). For a bounded operator \(S\) of the same form between two such spaces, with row sums and column sums of coefficient norms at most \(R\), apply (4.1) to the self-adjoint operator \(\begin{pmatrix}0&S\\S^*&0\end{pmatrix}\), whose norm is \(\|S\|\).

*Proof.* (1) Let \(P_0\) bound the degrees of all monomials of the group law and \(C_0\) the sum of the absolute values of its coefficients plus one. Let \(T\ge1\), and let \(\mathfrak B(T)\) be the set of \(f\in F\) whose coordinate of weight \(w\) lies in \([-\lfloor T^w\rfloor,\lfloor T^w\rfloor]\), for every coordinate. For \(f\in\mathfrak B(T)\) and \(g\in G\), a monomial of the weight-\(w\) coordinate of \(fg\) other than the coordinate of \(f\) contains a coordinate of \(g\); its coordinates of \(f\) have total weight at most \(w-1\), and its coordinates of \(g\) are at most \(x^a\). Hence that coordinate of \(fg\) differs from the coordinate of \(f\) by at most \(C_0x^{aP_0}T^{w-1}\). If every coordinate of \(f\) has distance more than this from the two ends of its interval, then \(fg\in\mathfrak B(T)\). For one coordinate of weight \(w\), the fraction of \(f\in\mathfrak B(T)\) violating this is at most
\[
\frac{2C_0x^{aP_0}T^{w-1}+2}{2\lfloor T^w\rfloor+1}\le\frac{2C_0x^{aP_0}+2}T ,
\]
so \(|\{f\in\mathfrak B:fg\notin\mathfrak B\}|\le C_1x^{aP_0}T^{-1}|\mathfrak B|\), with \(C_1=(4n_{\mathrm f}+1)(2C_0+2)\). Right multiplication by \(g\) is a bijection, so \(|\mathfrak B\setminus\mathfrak Bg|=|\mathfrak Bg\setminus\mathfrak B|\), and \(|\mathfrak B\,\triangle\,\mathfrak Bg|\le2C_1x^{aP_0}T^{-1}|\mathfrak B|\). Take \(T=x^{aP_0+B}\) and \(\mathfrak B=\mathfrak B(T)\). Then \(|\mathfrak B|\le\prod(3T^w)\le x^c\) for a suitable \(c\), since \(x\ge2\).

(2) The first inequality in (4.1) holds because \(P\) is a projection. For \(s\in F\) let \(P_s\) keep the deck indices in \(s\mathfrak B\). The left translation \(\lambda(s)\) commutes with \(A\) and carries \(P\) to \(P_s\), so \(\|P_sAP_s\|=\|PAP\|\). For finitely supported \(\xi\), \(\sum_s\|P_s\xi\|^2=|\mathfrak B|\,\|\xi\|^2\), because every \(f\in F\) lies in \(s\mathfrak B\) for exactly \(|\mathfrak B|\) elements \(s\). Since \((A\xi)(u,f)=\sum_{v,g}C_{uv}(g)\xi(v,fg)\), and the number of \(s\) with \(f\in s\mathfrak B\) and \(fg\in s\mathfrak B\) is \(|\mathfrak B\cap\mathfrak Bg^{-1}|\),
\[
\begin{gathered}
\sum_s\langle AP_s\xi,P_s\xi\rangle=|\mathfrak B|\,\langle A_{\mathfrak B}\xi,\xi\rangle,\\
A_{\mathfrak B}=\sum_{u,v,g}\alpha(g)\,E_{uv}\otimes\rho(g)\otimes C_{uv}(g),
\end{gathered}
\]
with \(\alpha(g)=|\mathfrak B\cap\mathfrak Bg^{-1}|/|\mathfrak B|\). Each term on the left has absolute value at most \(\|PAP\|\,\|P_s\xi\|^2\), so \(|\langle A_{\mathfrak B}\xi,\xi\rangle|\le\|PAP\|\,\|\xi\|^2\). Right multiplication by \(g\) maps \(\mathfrak B\cap\mathfrak Bg^{-1}\) onto \(\mathfrak Bg\cap\mathfrak B\), so \(\alpha(g^{-1})=\alpha(g)\), and \(A_{\mathfrak B}\) is self-adjoint because \(A\) is; therefore \(\|A_{\mathfrak B}\|\le\|PAP\|\).

The operator \(A-A_{\mathfrak B}\) has the matrix entries \((1-\alpha(g))C_{uv}(g)\) from the index \((v,fg)\) to \((u,f)\), and \(0\le1-\alpha(g)\le Cx^{-B}\) by (1), since \(g^{-1}\in G\). Its row sums of entry norms are at most \(Cx^{-B}R\), and, as it is self-adjoint, so are its column sums. By the Schur test, \(|\langle K\xi,\zeta\rangle|\le\sum_{\alpha,\beta}\|K_{\alpha\beta}\|\,\|\xi_\beta\|\,\|\zeta_\alpha\|\), which is at most \(\frac R2(\|\xi\|^2+\|\zeta\|^2)\) for an operator \(K\) with entries \(K_{\alpha\beta}\) whose row and column sums of norms are at most \(R\), so \(\|A-A_{\mathfrak B}\|\le Cx^{-B}R\), and (4.1) follows. \(\square\)

## 5. Empirical averages

**Lemma 5.1** (empirical averages; [OpenAI-KK, Lemma 9.4]). Let \(M=\lfloor d^{1/32}\rfloor\) and \(q=d^{A_*}\) as in the previous lesson. Fix \(a\ge n_{\mathrm f}\), \(B_0\), \(C_0\) and \(\varepsilon>0\). For large \(\ell\) the following holds. Let \(\mathcal D_1,\ldots,\mathcal D_r\), \(r\le C_0(1+\log q)\), be probability distributions with finite supports of pairs \((W,g)\in M_N(\mathbb C)\times F\) with \(\|W\|\le B_0\) and all coordinates of \(g\) bounded by \(q^a\). Then for every \(j\) there are pairs \((W_{j,1},g_{j,1}),\ldots,(W_{j,M},g_{j,M})\) in the support of \(\mathcal D_j\) with
\[
\begin{gathered}
\Bigl\|\frac1M\sum_{h=1}^MW_{j,h}\rho(g_{j,h})-\mathbb E_{\mathcal D_j}\bigl[W\rho(g)\bigr]\Bigr\|\\
\le\varepsilon .
\end{gathered}
\]

*Proof.* Fix \(j\), let \((W_h,g_h)\), \(1\le h\le M\), be independent samples of \(\mathcal D_j\), \(X_h=W_h\rho(g_h)\), and \(Y=\mathbb EX_h\). Apply Lemma 4.1 with \(x=q\), \(B=1\), \(J=\{1,2\}\), and the support of \(\mathcal D_j\) in \(F\) together with its inverses as \(G\); this gives a set \(\mathfrak B\) depending only on \(G\), with \(|\mathfrak B|\le q^c\). The operator \(\frac1M\sum_hX_h-Y\) has coefficient norms summing to at most \(2B_0\), so by Lemma 4.1 applied to its doubling,
\[
\begin{aligned}
&\Bigl\|\frac1M\sum_hX_h-Y\Bigr\|\\
&\quad\le\Bigl\|\frac1M\sum_hZ_h\Bigr\|+2CB_0q^{-1},\\
&Z_h=P\begin{pmatrix}0&X_h-Y\\ (X_h-Y)^*&0\end{pmatrix}P .
\end{aligned}
\]
The \(Z_h\) are independent self-adjoint operators on a space of dimension \(n_{\mathfrak B}=2|\mathfrak B|N\le q^{c_0}\), \(c_0=c+a+1\), with \(\mathbb EZ_h=0\) and \(\|Z_h\|\le2B_0\).

Let \(k\ge1\) and expand \(\mathbb E\operatorname{Tr}\bigl((\sum_hZ_h)^{2k}\bigr)\) into the terms \(\mathbb E\operatorname{Tr}(Z_{h_1}\cdots Z_{h_{2k}})\). If an index \(h\) occurs exactly once in \((h_1,\ldots,h_{2k})\), the product is \(\mathcal LZ_h\mathcal R\) with \(\mathcal L,\mathcal R\) products of the other factors, independent of \(Z_h\); conditioning on the other samples, the expectation is \(\mathbb E\operatorname{Tr}(\mathcal L\,\mathbb E[Z_h]\,\mathcal R)=0\). The remaining sequences use at most \(k\) distinct indices, so there are at most \(\sum_{b=1}^kM^bb^{2k}\le2M^kk^{2k}\) of them, and each term is at most \(n_{\mathfrak B}(2B_0)^{2k}\) in absolute value. Hence
\[
\begin{aligned}
&\mathbb E\operatorname{Tr}\Bigl(\Bigl(\frac1M\sum_hZ_h\Bigr)^{2k}\Bigr)\\
&\quad\le2q^{c_0}\Bigl(\frac{4B_0^2k^2}M\Bigr)^k .
\end{aligned}
\]
For a self-adjoint \(Z\), \(\|Z\|^{2k}\le\operatorname{Tr}(Z^{2k})\), so by Markov's inequality
\[
\begin{aligned}
&\mathbb P\Bigl(\Bigl\|\frac1M\sum_hZ_h\Bigr\|>\frac\varepsilon2\Bigr)\\
&\quad\le2q^{c_0}\Bigl(\frac{16B_0^2k^2}{M\varepsilon^2}\Bigr)^k .
\end{aligned}
\]
Take \(k=\lceil\log q\rceil\). Since \(\log M\ge(32A_*)^{-1}\log q-1\), the logarithm of the right side is at most
\[
c_0\log q-\frac{(\log q)^2}{32A_*}+O\bigl(\log q\,\log\log q\bigr),
\]
which tends to \(-\infty\) faster than \(-\log\bigl(C_0(1+\log q)\bigr)\). So for large \(\ell\), with positive probability all \(r\) tests succeed, and then each average is within \(\frac\varepsilon2+2CB_0q^{-1}\le\varepsilon\) of its expectation. \(\square\)

## 6. Exercises

**6.1** (easy). Show that the block of \(E_*(t)\) at a vertex \(x\in A_i\), the operator \((\delta_x^*\otimes1)E_*(t)(\delta_x\otimes1)\) on \(\mathcal H_t\), is \(h_i(t)^2p(t)/(2|A_i|)\), and recover \(\operatorname{Tr}(E_*(t))=s_p(t)\) by summing over vertices.

**6.2** (easy). In \(\mathbb Z\), a group with one coordinate of weight one, compute \(|\mathfrak B\,\triangle\,(\mathfrak B+g)|\) for \(\mathfrak B=\{-n,\ldots,n\}\) and \(0\le g\le2n+1\), and compare with Lemma 4.1(1).

**6.3** (medium). Show that \(\|Z\|^{2k}\le\operatorname{Tr}(Z^{2k})\) for a self-adjoint matrix \(Z\), with equality when \(Z\) has rank at most one.

**6.4** (medium). Suppose three consecutive layers \(0,1,2\) were active with \(h=(1,1,1)/\sqrt3\), and the blocks (2.1) were kept only for \(|i-k|\le1\). Compute the largest eigenvalue of the part of \(O(t)\) on the layerwise constant vectors, and explain why Lemma 5.1 of the previous lesson allows at most two adjacent active layers.

## 7. Solutions

**6.1.** For \(x\in A_i\), the component of \(V_*(t)\zeta\) at \(x\) is \(2^{-1/2}h_i|A_i|^{-1/2}p\zeta\), so the block of \(E_*=V_*V_*^*\) at \(x\) is \(\frac12h_i^2|A_i|^{-1}p\). Its identity trace is \(\frac12h_i^2|A_i|^{-1}s_p(t)\); summing over the \(|A_i|\) vertices of \(A_i\) and the \(|B_i|\) vertices of \(B_i\), and over \(i\), gives \(\sum_ih_i^2s_p(t)=s_p(t)\).

**6.2.** \(\mathfrak B\,\triangle\,(\mathfrak B+g)\), the union of \(\{-n,\ldots,-n+g-1\}\) and \(\{n+1,\ldots,n+g\}\), has \(2g\) elements, a fraction \(2g/(2n+1)\). With \(|g|\le x^a\) and \(n=\lfloor x^{a+B}\rfloor\) this is about \(2x^{-B}\), as in Lemma 4.1(1) with \(P_0=1\).

**6.3.** With eigenvalues \(\mu_j\), \(\operatorname{Tr}(Z^{2k})=\sum_j\mu_j^{2k}\ge\max_j\mu_j^{2k}=\|Z\|^{2k}\); equality holds when at most one \(\mu_j\) is nonzero.

**6.4.** On the constant vectors the part from the \(B\)-side to the \(A\)-side would be \(M\otimes p\) with \(M=\frac13\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}\), whose eigenvalues are \(\frac13+\frac23\cos\frac{\pi j}4\), \(j=1,2,3\). The largest eigenvalue of the two-sided operator is the largest of these, \(\frac{1+\sqrt2}3\approx0.805\), so the eigenvalue \(1\) would be lost. In Lemma 5.1 of the previous lesson the support of \(h\) has length less than two, so \(h_ih_k\ne0\) forces \(|i-k|\le1\), and the constant part is exactly \(|h\rangle\langle h|\otimes p\).

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 9.1 to 9.3, Lemmas 9.1, 9.3 and 9.4, Theorem 9.2. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
