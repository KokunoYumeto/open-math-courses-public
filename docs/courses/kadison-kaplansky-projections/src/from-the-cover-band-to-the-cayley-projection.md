# From the cover band to the Cayley projection

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the construction. The realization theorem gives a weighted adjacency operator \(T_P\) on the voltage cover, close in norm to the compressed model operator. The model's separated upper band passes to \(T_P\), with fiber traces exactly equal to those of the transverse projections, and its identity trace, weighted by the ball sizes \(\mathfrak w_i\), is small because the band sits on the active layers. On the Cayley graph of the group \(\Gamma\), the matrix \(T\) with the same weights agrees with the direct sum of the copies on their disjoint assigned domains, up to an adjacency on a forest of small norm, so it has a separated upper band too. Its spectral projection \(p_0\) is compared with the upper spaces of all indexed copies, an equivariant space of small trace, and this bounds the trace of \(p_0\) by a number below \(\frac12\) [OpenAI-KK, Sections 10 and 11].

- Constants (Section 1).
- The projection of the cover (Section 2).
- Localization of the identity trace (Section 3).
- An element of the group algebra (Section 4).
- The trace of the projection (Section 5).
- The construction (Section 6).

The notation of the preceding lessons is in force: the tower \(Y\), the cover \(P\) with its weights, the operators \(O\), \(\Pi\), \(E_*\) and \(T_P\) of [The model operator and finite tests](the-model-operator-and-finite-tests.md), the group \(\Gamma\) with its finite set \(S\) of refined labels and its formal Cayley graph \(X\), the indexed copies \(Q\) with their domains \(D_Q\) and balls \(B(Q)\) of [Thin triangles, overlap balls and the residual forest](thin-triangles-overlap-balls-and-the-residual-forest.md), and the weights \(\mathfrak w_i=2^{C_\bullet H_i}\). We use the estimates of Sections 3 and 4 of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md): Lemma 3.1 there, whose bound \(a+12\varepsilon\) is used below in the weaker form \(a+20\varepsilon\), and Lemma 4.2. All identity traces are unnormalized sums over the matrix indices.

## 1. Constants

Let \(\chi=\frac1{800}\) be the gap of the tower, and put
\[
\alpha=\frac\chi{1000},\qquad r_0=\frac\chi3,\qquad C_\chi=\frac4\chi .
\]
Fix the accuracy \(\eta>0\) of the realization theorem so small that
\[
\begin{gathered}
\eta\le\frac\alpha2,\\
\theta:=C_\chi\eta\le\frac12,\\
2^{C_\bullet}\theta^2\le\frac12 .
\end{gathered}\tag{1.1}
\]
All other fixed constants of the construction are chosen before; Theorem 3.1 of [The model operator and finite tests](the-model-operator-and-finite-tests.md) holds for this \(\eta\) and all large \(\ell\). We take \(\ell\) so large that this theorem holds and that
\[
20\sqrt{\varepsilon_\ell}\le\frac\alpha2 ,\tag{1.2}
\]
with the deletion bound \(\varepsilon_\ell\) of [Pruning and recovery of long paths](pruning-and-recovery-of-long-paths.md). Let \(\mu_\ell\) be the weighted trace bound of Proposition 6.1 of [The magnetic factor and the weighted trace](the-magnetic-factor-and-the-weighted-trace.md); \(\mu_\ell\to0\). Further conditions on \(\ell\) are added in Sections 4 and 5.

## 2. The projection of the cover

Let \(\mathcal C_{r_0}\) be the circle \(|z-1|=r_0\).

**Proposition 2.1** (the cover projection and its exact fiber trace; [OpenAI-KK, Proposition 10.3]). The operator \(T_P\) has the spectral projection \(E_P=\frac1{2\pi i}\oint_{\mathcal C_{r_0}}(z-T_P)^{-1}dz\) onto a separated part of its spectrum, and
\[
\begin{gathered}
\|T_P\|\le2,\\
\|(T_P-I)E_P\|\le\alpha,\\
\langle T_Px,x\rangle\\
\le(1-\chi+\alpha)\|x\|^2\\
\bigl(x\in(1-E_P)\mathcal H^0\bigr).
\end{gathered}\tag{2.1}
\]
In the fibers, for almost every \(t\),
\[
\begin{gathered}
\operatorname{Tr}\bigl(E_P(t)\bigr)\\
=\begin{cases}s_p(t),&0<t<\delta,\\0,&t\notin(0,\delta).\end{cases}
\end{gathered}\tag{2.2}
\]
The projection \(E_P\) is nonzero, it is reduced by the subspace of every connected component of \(P\), and its \(N\times N\) diagonal block at a vertex \((v,f)\) of \(P\) depends only on \(v\).

*Proof.* Fix \(t\) with \(\|T_P(t)-\Pi O(t)\Pi\|\le\eta\), which holds for almost every \(t\). By Lemma 2.1 of the previous lesson, Lemma 3.1 of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md) applies to \(A=O(t)\), \(E=E_*(t)\), \(J=\Pi\), \(a=0\), \(b=\chi\), with \(\|(1-\Pi)E_*(t)\|\le\sqrt{\varepsilon_\ell}\le\frac12\). It gives a projection \(E^\Pi_*(t)\le\Pi\), equivalent to \(E_*(t)\) through a partial isometry, and an operator \(B_\Pi(t)\) on \(\Pi\mathcal H^0_t\) equal to \(1\) on \(E^\Pi_*(t)\), at most \(1-\chi\) on its complement in \(\Pi\mathcal H^0_t\), of norm at most \(2\), with \(\|\Pi O(t)\Pi-B_\Pi(t)\|\le20\sqrt{\varepsilon_\ell}\le\alpha/2\). Let \(B(t)\) be \(B_\Pi(t)\) extended by zero on \((1-\Pi)\mathcal H^0_t\); since \(1-\chi>0\), its spectrum off \(E^\Pi_*(t)\) still lies in \([-2,1-\chi]\). Then
\[
\|T_P(t)-B(t)\|\le\eta+\tfrac\alpha2\le\alpha .
\]
Lemma 4.2 of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md), with \(F=E^\Pi_*(t)\), \(b=\chi\), \(r_0=\chi/3\le b/2\) and \(u=\alpha<r_0/2\), shows that \(\mathcal C_{r_0}\) lies in the resolvent set of \(T_P(t)\), with \(\|(z-T_P(t))^{-1}\|\le(r_0-\alpha)^{-1}\) on it, that the spectrum of \(T_P(t)\) lies in \([-2-\alpha,1-\chi+\alpha]\cup[1-\alpha,1+\alpha]\), and that the contour projection \(E_P(t)\) satisfies \(\|E_P(t)-E^\Pi_*(t)\|\le\alpha/(r_0-\alpha)<\frac12\), so that \(E_P(t)\) and \(E^\Pi_*(t)\) are equivalent through a partial isometry.

Let \(\Sigma\) be the union of \([-2-\alpha,1-\chi+\alpha]\) and \([1-\alpha,1+\alpha]\), which contains the spectra of almost all fibers. For real \(\lambda\notin\Sigma\), let \(\psi\) be continuous on \([-3,3]\) and equal to \((\lambda-x)^{-1}\) on \(\Sigma\); by Lemma 4.1 of [An affine nilpotent group](an-affine-nilpotent-group.md), \(\psi(T_P)\) is the field of the \(\psi(T_P(t))=(\lambda-T_P(t))^{-1}\), so it inverts \(\lambda-T_P\). Hence the spectrum of \(T_P\) lies in \(\Sigma\), and its part in \([1-\alpha,1+\alpha]\) is separated. Let \(\varphi\) be continuous on \([-3,3]\), equal to \(0\) on \([-3,1-\chi+\alpha]\) and to \(1\) on \([1-\alpha,3]\). Then \(E_P=\varphi(T_P)\) is the spectral projection of that part, it equals the contour integral (Lemma 1.1(2) of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md)), and by Lemma 4.1 of [An affine nilpotent group](an-affine-nilpotent-group.md) it is the field of the projections \(E_P(t)=\varphi(T_P(t))\). This gives (2.1); also \(\|T_P\|\le\|\Pi O\Pi\|+\eta\le2\).

All operators in this argument commute with the right phase action of the fiber, because \(T_P(t)\), \(O(t)\), \(\Pi\) and \(E_*(t)\) do, and so do the partial isometries, which are built from them by products and continuous functions. By Lemma 2.1(4) of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md) and Lemma 2.1(2) of the previous lesson, \(\operatorname{Tr}(E_P(t))=\operatorname{Tr}(E^\Pi_*(t))\), which equals \(\operatorname{Tr}(E_*(t))=s_p(t)\) for \(0<t<\delta\), with no approximation error. For \(t\notin(0,\delta)\), \(O(t)=0\) and \(E_*(t)=0\), so \(E_P(t)\) is equivalent to \(0\). This is (2.2). The function \(s_p\) is positive on \((0,\delta)\), so the identity trace of \(E_P\), the integral of (2.2), is positive, and \(E_P\ne0\).

The subspace of each connected component of \(P\) reduces \(T_P\) (Section 3 of the previous lesson), hence its resolvent and \(E_P\). The deck transformations commute with \(T_P\), hence with \(E_P\), and they carry each lift of a base vertex to every other lift, also between different components; so the diagonal block of \(E_P\) at \((v,f)\) does not depend on \(f\). \(\square\)

## 3. Localization of the identity trace

For a vertex \(v\) of \(Y\) put
\[
\begin{gathered}
e_v=\sum_{j=1}^N\langle E_Px_{v,j},x_{v,j}\rangle\ge0,\\
x_{v,j}=\delta_{(v,1_F)}\otimes e_j,\\
\mathcal S=\sum_{i\in\mathbb Z}\mathfrak w_i\sum_{v\in V(Y)\text{ in layer }i}e_v ,
\end{gathered}
\]
the matrix trace of the diagonal block of \(E_P\) at any lift of \(v\), and its weighted sum. These numbers count the overlaps of copies: a base vertex may have many lifts inside one ball \(B(Q)\), and \(\mathfrak w_i\) bounds the size of such a ball.

**Proposition 3.1** (the weighted size; [OpenAI-KK, Proposition 10.4]). \(\mathcal S\le96\mu_\ell\).

*Proof.* Fix \(t\in(0,\delta)\) with \(\|T_P(t)-\Pi O(t)\Pi\|\le\eta\). Put \(A_0=\Pi O(t)\Pi\) and \(\Delta=T_P(t)-A_0\). By the proof of Proposition 2.1, \(A_0\) is within \(\alpha/2\) of \(B(t)\), so on \(\mathcal C_{r_0}\)
\[
\begin{gathered}
R_0(z)=(z-A_0)^{-1}\ \text{ exists, and}\\
\|R_0(z)\|\le\bigl(r_0-\tfrac\alpha2\bigr)^{-1}\le C_\chi .
\end{gathered}
\]
Let \(P_i\) be the projection onto the vertices of layer \(i\), on both sides, with all transverse and matrix coordinates. The operator \(A_0\) lives on the active layers \(J(t)\): it vanishes on the other layers and has no entries between them and \(J(t)\). So \(P_iR_0(z)=z^{-1}P_i\) for \(i\notin J(t)\). Since \(\|\Delta R_0\|\le\eta C_\chi=\theta\le\frac12\), the resolvent of \(T_P(t)\) is the norm-convergent series
\[
(z-T_P(t))^{-1}=\sum_{n\ge0}R_0(\Delta R_0)^n .
\]
Let \(k=\operatorname{dist}(i,J(t))\). The operator \(\Delta\) has layer width one, so \(P_i\Delta^n\) involves only layers within distance \(n\) of \(i\), and by induction on \(n\), \(P_iR_0(\Delta R_0)^n=z^{-n-1}P_i\Delta^n\) for \(n<k\). Its integral over \(\mathcal C_{r_0}\) vanishes, because \(0\) lies outside the circle. The remaining terms give
\[
\begin{aligned}
\|P_iE_P(t)\|&\le r_0\sum_{n\ge k}C_\chi\theta^n\le2r_0C_\chi\theta^k\\
&\le4\theta^{\operatorname{dist}(i,J(t))} ,
\end{aligned}
\]
also for \(k=0\). By Lemma 2.1(1) of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md), the operator inequality \(0\le E_P(t)P_iE_P(t)\le\|P_iE_P(t)\|^2E_P(t)\), and (2.2),
\[
\begin{aligned}
&\operatorname{Tr}\bigl(P_iE_P(t)P_i\bigr)=\operatorname{Tr}\bigl(E_P(t)P_iE_P(t)\bigr)\\
&\quad\le\|P_iE_P(t)\|^2\,s_p(t)\\
&\quad\le16\,\theta^{2\operatorname{dist}(i,J(t))}s_p(t) .
\end{aligned}
\]
So the total trace of the projection enters, not the size of the layer. Since \(|H_i-H_j|\le|i-j|\), \(\mathfrak w_i\le\mathfrak w_j2^{C_\bullet|i-j|}\). Assign every integer to a nearest point of \(J(t)\), which has at most two points; at each positive distance at most two integers are assigned to a given point. By (1.1),
\[
\begin{aligned}
&\sum_i\mathfrak w_i\theta^{2\operatorname{dist}(i,J(t))}\\
&\quad\le2\max_{j\in J(t)}\mathfrak w_j\Bigl(1+2\sum_{k\ge1}\bigl(2^{C_\bullet}\theta^2\bigr)^k\Bigr)\\
&\quad\le6\max_{j\in J(t)}\mathfrak w_j .
\end{aligned}
\]
Hence
\[
\begin{aligned}
&\sum_i\mathfrak w_i\operatorname{Tr}(P_iE_P(t)P_i)\\
&\quad\le96\max_{j\in J(t)}\mathfrak w_js_p(t)\le96\mu_\ell ;
\end{aligned}
\]
for \(t\notin(0,\delta)\) the left side is zero. Finally, \(e_v\) is the integral over \(t\) of the matrix trace of the diagonal block of \(E_P(t)\) at \(v\), as in Section 1 of the previous lesson, and \(\sum_{v\text{ in layer }i}\) of these blocks has trace \(\operatorname{Tr}(P_iE_P(t)P_i)\). By Tonelli's theorem, \(\mathcal S=\int_{\mathbb T}\sum_i\mathfrak w_i\operatorname{Tr}(P_iE_P(t)P_i)\,dt\le96\mu_\ell\). \(\square\)

## 4. An element of the group algebra

For a refined label \(\sigma\in S\) let \(W_\sigma\) be its matrix weight and \(D_\sigma=D_{ik}\) its degree number, determined by the label, and put \(w_\sigma=(dD_\sigma)^{-1/2}W_\sigma\). On \(\mathcal H=\ell^2(\Gamma)\otimes\mathbb C^N\) let
\[
\begin{aligned}
&(T\xi)(g)\\
&=\sum_{\sigma\in S}\bigl(w_\sigma\,\xi(g\sigma)\\
&\qquad+w_\sigma^*\,\xi(g\sigma^{-1})\bigr) .
\end{aligned}\tag{4.1}
\]
This is a finite sum of matrices times right translations, self-adjoint, and it commutes with the left translations of \(\Gamma\). With \((\mathcal I\xi)(g)=\xi(g^{-1})\), the operator \(T'=\mathcal IT\mathcal I\), equal to \(\sum_\sigma\bigl(\lambda(\sigma)\otimes w_\sigma+\lambda(\sigma^{-1})\otimes w_\sigma^*\bigr)\), is a self-adjoint element of \(M_N(\mathbb C\Gamma)\) in the left regular representation, with the same spectrum and spectral projections conjugated by \(\mathcal I\), which fixes \(\delta_1\).

For an indexed copy \(Q\), let \(T_Q\) be the operator on \(\ell^2(V(Q))\otimes\mathbb C^N\) with the entries of (4.1) on the formal edges of \(Q\) only. Through the label map, \(Q\) is the image of a component \(C\) of \(P\), and \(T_Q\) is the restriction of \(T_P\) to the subspace of \(C\): an edge \((a,f)\to(b,fz_e)\) of \(P\) with refined label \(\sigma\) carries the entry \((dD_\sigma)^{-1/2}W_\sigma=w_\sigma\) in both operators. Let \(E_Q\) be the contour projection of \(T_Q\) on \(\mathcal C_{r_0}\), the restriction of \(E_P\). Then (2.1) holds for \(T_Q\) and \(E_Q\), and by Proposition 2.1, if \(u\in V(Q)\) has type \(v\),
\[
\operatorname{Tr}_{\mathbb C^N}E_Q(u,u)=e_v .\tag{4.2}
\]
The block \(E_Q(u,u)\) is the block of \(E_P\) at a source vertex of \(u\), well defined up to deck transformations, which do not change it.

**Lemma 4.1** (finite trimming costs little; [OpenAI-KK, Lemma 10.5]). For every indexed copy \(Q\), \(\|\mathbf1_{B(Q)}E_Q\|^2\le\mathcal S\). If \(\mathcal S\le\frac14\), the compression of \(T_Q\) to \(\ell^2(D_Q)\otimes\mathbb C^N\) is within \(\alpha+20\sqrt{\mathcal S}\) of an operator \(C_Q\) of norm at most \(2\), equal to \(1\) on a projection \(F_Q\) equivalent to \(E_Q\), and at most \(1-\chi+\alpha\) on the complement of \(F_Q\). In particular \(F_Q\ne0\) if \(E_Q\ne0\).

*Proof.* The ball is finite. Since \(E_Q\) is a projection,
\[
\begin{aligned}
&\|\mathbf1_{B(Q)}E_Q\|^2\\
&\quad\le\sum_{u\in B(Q)}\sum_j\|E_Q(\delta_u\otimes e_j)\|^2\\
&\quad=\sum_{u\in B(Q)}\operatorname{Tr}_{\mathbb C^N}E_Q(u,u)\\
&\quad=\sum_{u\in B(Q)}e_{\operatorname{type}_Q(u)}\le\mathcal S,
\end{aligned}
\]
by (4.2) and Corollary 6.2 of [Thin triangles, overlap balls and the residual forest](thin-triangles-overlap-balls-and-the-residual-forest.md), with \(a_v=e_v\). The vertices of \(Q\) outside \(D_Q\) lie in \(B(Q)\) (Proposition 5.2 there), so \(\|(1-\mathbf1_{D_Q})E_Q\|\le\sqrt{\mathcal S}\le\frac12\). Lemma 3.1 of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md), with \(A=T_Q\), \(E=E_Q\), \(J=\mathbf1_{D_Q}\), \(a=\alpha\) and \(b=\chi-\alpha\), gives \(C_Q=B_J\), \(F_Q=E^J\) and the partial isometry from \(E_Q\) to \(F_Q\). \(\square\)

**Lemma 4.2** (matrix adjacency on a forest; [OpenAI-KK, Lemma 10.6]). Let a countable forest have maximum degree at most \(m_1\), and a self-adjoint operator on \(\ell^2(\text{vertices})\otimes\mathbb C^N\) have nonzero entries only between the two ends of edges, each of norm at most \(w_1\). Then its norm is at most \(2w_1\sqrt{m_1}\).

*Proof.* Choose a root in every tree and orient each edge from parent to child. Let \(B\) keep the entries from a parent to its children. Every vertex other than a root has one parent, so for finitely supported \(\xi\)
\[
\begin{aligned}
&\|B\xi\|^2\\
&\quad\le w_1^2\sum_x\#\{\text{children of }x\}\,\|\xi(x)\|^2\\
&\quad\le m_1w_1^2\|\xi\|^2 .
\end{aligned}
\]
The operator is \(B+B^*\), of norm at most \(2\|B\|\). \(\square\)

**Proposition 4.3** (a nonzero upper band; [OpenAI-KK, Proposition 10.7]). For large \(\ell\),
\[
\begin{gathered}
\operatorname{spec}T\\
\subseteq(-\infty,1-\chi+4\alpha]\\
\cup[1-3\alpha,1+3\alpha] ,
\end{gathered}\tag{4.3}
\]
the second part is not empty, and its spectral projection \(p_0=\mathbf1_{[1-\chi/4,\infty)}(T)\) is nonzero; \(\mathcal Ip_0\mathcal I\in M_N(C^*_r(\Gamma))\).

*Proof.* Take \(\ell\) so large that \(\mathcal S\le96\mu_\ell\) satisfies
\[
\begin{gathered}
\mathcal S<\min\Bigl\{\frac14,\frac1{1000}\Bigr\},\\
20\sqrt{\mathcal S}\le\alpha .
\end{gathered}\tag{4.4}
\]
The domains \(D_Q\) are pairwise disjoint (Proposition 5.2 of the lesson on thin triangles). On \(\mathcal H\) form the orthogonal direct sums
\[
\begin{gathered}
C=\bigoplus_QC_Q\oplus0,\qquad F_D=\bigoplus_QF_Q\oplus0,\\
T_D=\bigoplus_Q\mathbf1_{D_Q}T_Q\mathbf1_{D_Q}\oplus0,
\end{gathered}
\]
where the zero acts on the vertices in no \(D_Q\). These are bounded by the uniform bounds of Lemma 4.1. \(C\) equals \(1\) on \(F_D\), has norm at most \(2\), and is at most \(1-\chi+\alpha\) on the complement, the zero part included, as \(1-\chi+\alpha>0\); and \(\|T_D-C\|\le\alpha+20\sqrt{\mathcal S}\le2\alpha\). Since \(E_P\ne0\), some component of \(P\) has nonzero upper projection, so its copies have \(E_Q\ne0\), and \(F_D\ne0\) by Lemma 4.1. This uses the ordinary direct sum, not an equivariant assignment of domains.

On a formal edge of \(X\) with both ends in one \(D_Q\) and belonging to \(Q\), \(T_D\) and \(T\) have the same entry, determined by the label; by disjointness and the embedding of formal edges, these edges, the set \(E_{\mathrm{int}}\) of Proposition 5.2 of the lesson on thin triangles, are counted once. Every other formal edge carries the entry of \(T\) in \(T-T_D\) and nothing in \(T_D\). So \(T-T_D\) is the matrix adjacency of the graph \((V(X),E(X)\setminus E_{\mathrm{int}})\), a forest by that proposition, with maximum degree at most \(2|S|\) and entries of norm at most \(\max_\sigma\|w_\sigma\|\le\sqrt2C_\eta/\sqrt{dD}\), because \(D_\sigma\ge D/2\). By Lemma 4.2 and Theorem 3.1(1) of the previous lesson,
\[
f_\ell:=\|T-T_D\|\le4C_\eta\sqrt{\frac{|S|}{dD}}\longrightarrow0 .
\]
Take \(\ell\) so large that \(f_\ell\le\alpha\). Then \(\|T-C\|\le3\alpha\). Lemma 4.2 of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md), with \(B=C\), \(F=F_D\), \(b=\chi-\alpha\), \(r_0=\chi/3\le b/2\) and \(u=3\alpha<r_0/2\), gives (4.3) and an enclosed projection within \(3\alpha/(r_0-3\alpha)<1\) of \(F_D\ne0\), hence nonzero. Since \(\alpha=\chi/1000\), the number \(1-\chi/4\) lies strictly between the two intervals, so \(p_0\) is the enclosed projection.

The function equal to \(0\) on the lower interval and \(1\) on the upper one is continuous on the spectrum, so \(\mathcal Ip_0\mathcal I\) is the corresponding continuous function of \(T'\in M_N(\mathbb C\Gamma)\), and lies in \(M_N(C^*_r(\Gamma))\) by Lemma 1.1 of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md). \(\square\)

## 5. The trace of the projection

The assigned domains prove the spectral separation, but their order need not be invariant under \(\Gamma\), so the equivalence of \(p_0\) with \(F_D\) does not compare traces. The trace estimate uses all indexed copies at once.

For a positive operator \(Z\) on \(\ell^2(\Gamma)\otimes\mathcal K\) commuting with the left translations, with an orthonormal basis \((k_a)\) of the countable space \(\mathcal K\), put \(\operatorname{Tr}_\Gamma Z=\sum_a\langle Z(\delta_1\otimes k_a),\delta_1\otimes k_a\rangle\), a number in \([0,\infty]\). After conjugation by \(\mathcal I\), which turns left translations into right translations and fixes \(\delta_1\), Lemma 2.1 of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md) applies to it. In particular
\[
\begin{aligned}
\operatorname{Tr}_\Gamma(p_0)&=\sum_{j=1}^N\langle p_0(\delta_1\otimes e_j),\delta_1\otimes e_j\rangle\\
&=\tau_{\Gamma,N}(\mathcal Ip_0\mathcal I) .
\end{aligned}
\]
Consider
\[
\begin{gathered}
\mathcal L=\bigoplus_Q\ell^2(V(Q))\otimes\mathbb C^N,\\
E=\bigoplus_QE_Q .
\end{gathered}\tag{5.1}
\]
A left translation \(g\) maps a copy \(Q\) to the copy \(gQ\) and its vertices to their translates. By the incidence count, Proposition 6.1 of the lesson on thin triangles, \((Q,u)\mapsto(u,\operatorname{type}_Q(u))\) identifies \(\mathcal L\) with \(\ell^2(\Gamma)\otimes\ell^2(V(Y))\otimes\mathbb C^N\), with \(\Gamma\) acting on the first factor. Translation by \(g\) carries \(T_Q\) to \(T_{gQ}\), as the entries depend on labels only, hence \(E_Q\) to \(E_{gQ}\); so \(E\) is equivariant, and by (4.2) its diagonal at \((1,v)\) has matrix trace \(e_v\). Hence
\[
\begin{gathered}
\operatorname{Tr}_\Gamma E=\mathcal S_0:=\sum_{v\in V(Y)}e_v\\
\le\mathcal S<\infty ,
\end{gathered}\tag{5.2}
\]
and \(\mathcal U=E\mathcal L\) is a closed invariant subspace of finite trace, although there are countably many copies and base vertices.

**Lemma 5.1** (the total loss from earlier intersections; [OpenAI-KK, Lemma 10.8]). Put \(I_Q=V(Q)\setminus D_Q\subseteq B(Q)\). For every \(\xi\in\mathcal H\),
\[
\sum_Q\bigl\|E_Q(\xi|_{I_Q})\bigr\|^2\le\mathcal S\|\xi\|^2 ,
\]
where restrictions are extended by zero inside the copy.

*Proof.* For \(u\in V(Q)\) of type \(v\) and \(z\in\mathbb C^N\), \(\|E_Q(\delta_u\otimes z)\|^2=\langle E_Q(u,u)z,z\rangle\), at most \(e_v\|z\|^2\), since the positive matrix \(E_Q(u,u)\) has norm at most its trace. The set \(I_Q\) is finite, and the Cauchy–Schwarz inequality gives
\[
\begin{aligned}
\|E_Q(\xi|_{I_Q})\|^2&\le|B(Q)|\\
&\quad\cdot\sum_{u\in I_Q}e_{\operatorname{type}_Q(u)}\|\xi(u)\|^2 .
\end{aligned}
\]
Summing over \(Q\) and rearranging the nonnegative terms by the vertex \(u\), the coefficient of \(\|\xi(u)\|^2\) is \(\sum_{Q:\,u\in V(Q)\setminus D_Q}|B(Q)|e_{\operatorname{type}_Q(u)}\le\mathcal S\), by Corollary 6.2 of the lesson on thin triangles. The factor \(|B(Q)|\) from the Cauchy–Schwarz inequality is paid by the weight \(\mathfrak w_i\) in \(\mathcal S\). \(\square\)

**Lemma 5.2** (a bounded restriction operator; [OpenAI-KK, Lemma 10.9]). The formula \(A\xi=\bigl(E_Q(\xi|_{V(Q)})\bigr)_Q\) defines a bounded equivariant operator \(A:\mathcal H\to\mathcal U\) with \(\|A\|\le1+\sqrt{\mathcal S}\). Its kernel \(K\) is a closed invariant subspace, \(\xi\in K\) if and only if \(E_Q(\xi|_{V(Q)})=0\) for every \(Q\), and
\[
\operatorname{Tr}_\Gamma P_{K^\perp}\le\mathcal S_0 .
\]

*Proof.* Since the \(D_Q\) are disjoint and each \(E_Q\) is a contraction, \(\sum_Q\|E_Q(\xi|_{D_Q})\|^2\le\sum_Q\|\xi|_{D_Q}\|^2\le\|\xi\|^2\). With Lemma 5.1, both families in \(A\xi=(E_Q(\xi|_{D_Q}))_Q+(E_Q(\xi|_{I_Q}))_Q\) lie in \(\mathcal L\), which gives the bound; every coordinate lies in the range of \(E_Q\). The formula for \(A\) does not depend on the order of the copies, and translation permutes the copies and intertwines the \(E_Q\), so \(A\) is equivariant and \(K\) is invariant. The partial isometry of the polar decomposition of \(A\) has initial projection \(P_{K^\perp}\) and final projection onto the closure of the range of \(A\), inside \(\mathcal U\); it is equivariant as in Lemma 2.1(4) of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md). By Lemma 2.1(1) and monotonicity there, and (5.2), \(\operatorname{Tr}_\Gamma P_{K^\perp}\le\operatorname{Tr}_\Gamma E=\mathcal S_0\). \(\square\)

**Lemma 5.3** (the upper space injects into the small complement; [OpenAI-KK, Lemma 10.10]). For \(\xi\in K\), \(\langle T\xi,\xi\rangle\le(1-\chi+3\alpha)\|\xi\|^2\). Consequently \(P_{K^\perp}\) is injective on \(p_0\mathcal H\), and
\[
\begin{gathered}
0<\operatorname{Tr}_\Gamma(p_0)\le\mathcal S_0\\
\le\mathcal S<\frac12 .
\end{gathered}\tag{5.3}
\]

*Proof.* For \(\xi\in K\), \(E_Q(\xi|_{D_Q})=-E_Q(\xi|_{I_Q})\), so by Lemma 5.1
\[
\sum_Q\|E_Q(\xi|_{D_Q})\|^2\le\mathcal S\|\xi\|^2 .
\]
For a vector \(y\) on \(Q\), (2.1) for \(T_Q\) gives
\[
\begin{aligned}
&\langle T_QE_Qy,E_Qy\rangle\le(1+\alpha)\|E_Qy\|^2,\\
&\langle T_Q(1-E_Q)y,(1-E_Q)y\rangle\\
&\quad\le(1-\chi+\alpha)\|(1-E_Q)y\|^2,
\end{aligned}
\]
so
\[
\begin{aligned}
\langle T_Qy,y\rangle&\le(1-\chi+\alpha)\|y\|^2\\
&\quad+\chi\|E_Qy\|^2 .
\end{aligned}
\]
Apply this to \(y=\xi|_{D_Q}\) and sum over the disjoint domains: \(\langle T_D\xi,\xi\rangle\le(1-\chi+\alpha)\|\xi\|^2+\chi\mathcal S\|\xi\|^2\), where the vertices in no domain are included because \(1-\chi+\alpha>0\). With \(f_\ell\le\alpha\) and \(\chi\mathcal S\le\chi/1000=\alpha\),
\[
\begin{aligned}
\langle T\xi,\xi\rangle&\le\bigl(1-\chi+\alpha+\chi\mathcal S+f_\ell\bigr)\|\xi\|^2\\
&\le(1-\chi+3\alpha)\|\xi\|^2 .
\end{aligned}
\]
On \(p_0\mathcal H\), (4.3) gives \(\langle T\xi,\xi\rangle\ge(1-3\alpha)\|\xi\|^2\), and \(1-3\alpha>1-\chi+3\alpha\). So \(p_0\mathcal H\cap K=0\), and \(P_{K^\perp}\), an equivariant operator, is injective on \(p_0\mathcal H\) and maps it into \(K^\perp\). By Lemma 2.1(4) of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md) and Lemma 5.2, \(\operatorname{Tr}_\Gamma(p_0)\le\operatorname{Tr}_\Gamma(P_{K^\perp})\le\mathcal S_0\le\mathcal S\), and \(\mathcal S<\frac1{1000}\) by (4.4). A nonzero equivariant projection has positive identity trace (Lemma 2.1(3) there), and \(p_0\ne0\) by Proposition 4.3. \(\square\)

## 6. The construction

**Theorem 6.1** (the matrix projection; [OpenAI-KK, Theorem 10.11]). For the fixed choices above and some large integer \(\ell\), the group \(\Gamma\) is finitely generated and torsion-free, and the self-adjoint matrix \(T'\in M_N(\mathbb C\Gamma)\) of Section 4 has a separated part of its spectrum in the left regular representation whose spectral projection \(p_0'=\mathcal Ip_0\mathcal I\) satisfies
\[
p_0'\in M_N\bigl(C^*_r(\Gamma)\bigr),\quad0<\tau_{\Gamma,N}(p_0')<\tfrac12 .
\]

*Proof.* The set \(S\) of generators is finite by Theorem 3.1(1) of [The model operator and finite tests](the-model-operator-and-finite-tests.md), and the cover satisfies the girth condition by Theorem 3.1(2) there, so Theorem 3.1 of [Voltage covers and embedded copies](voltage-covers-and-embedded-copies.md) applies; its statement 4, proved in [Torsion-freeness](torsion-freeness.md), gives that \(\Gamma\) is torsion-free. Proposition 4.3 gives the spectral separation, the membership and \(p_0\ne0\), and Lemma 5.3 the trace bound, as \(\tau_{\Gamma,N}(p_0')=\operatorname{Tr}_\Gamma(p_0)\). The choices are consistent: the geometric and transverse constants are fixed first, (1.1) fixes one accuracy \(\eta\), and since \(\varepsilon_\ell\), \(\mu_\ell\) and \(|S|/(dD)\) tend to zero, one sufficiently large \(\ell\) satisfies all the displayed conditions. No limit group or limit projection is taken. \(\square\)

This proves Theorem 5.1 of [The conjecture and scalar compression](the-conjecture-and-scalar-compression.md), and with it Theorem 1.1 there: Proposition 4.1 of that lesson, applied to \(\Gamma\) and \(p_0'\), gives a nontrivial projection of trace \(\tau_{\Gamma,N}(p_0')\in(0,\frac12)\) in the reduced group \(C^*\)-algebra of the finitely generated torsion-free group \(\Gamma*\mathbb F_N\).

The geometric part of the argument, Theorem 3.1 of [Voltage covers and embedded copies](voltage-covers-and-embedded-copies.md), uses the statements (VK) and (MAP) on van Kampen diagrams and plane maps recorded in Section 4 of that lesson and proved in the course [Van Kampen diagrams](course:van-kampen-diagrams/van-kampens-lemma). Every step is proved in this course or in the lessons it names.

## 7. Exercises

**7.1** (easy). With \(\alpha=\chi/1000\) and \(r_0=\chi/3\), check that \(1-\chi+4\alpha<1-\chi/4<1-3\alpha\), and that \(r_0\le(\chi-\alpha)/2\) and \(3\alpha<r_0/2\), as used in Proposition 4.3.

**7.2** (easy). Show that \(\|\mathbf1_BE\|^2\le\sum_{u\in B}\operatorname{Tr}_{\mathbb C^N}E(u,u)\) for a projection \(E\) on \(\ell^2(V)\otimes\mathbb C^N\) and a finite set \(B\subseteq V\).

**7.3** (medium). Show that if \(2^{C_\bullet}\theta^2\le\frac12\), then \(\sum_{i\in\mathbb Z}2^{C_\bullet|i-j|}\theta^{2|i-j|}\le3\) for every \(j\), and explain how this enters Proposition 3.1.

**7.4** (medium). Compute the norm of the adjacency operator of the star with \(\Delta\) leaves and scalar weights \(1\), and compare it with Lemma 4.2.

## 8. Solutions

**7.1.**
\[
\begin{aligned}
1-\chi+4\alpha&=1-0.996\chi<1-0.25\chi\\
&<1-0.003\chi=1-3\alpha .
\end{aligned}
\]
Also \((\chi-\alpha)/2=0.4995\chi\ge\chi/3\), and \(3\alpha=0.003\chi<\chi/6\).

**7.2.** \(\|\mathbf1_BE\|^2\le\|\mathbf1_BE\|_{\mathrm{HS}}^2\), which is \(\sum_{u\in B}\sum_j\|E(\delta_u\otimes e_j)\|^2\), and \(\|E(\delta_u\otimes e_j)\|^2=\langle E(\delta_u\otimes e_j),\delta_u\otimes e_j\rangle\) because \(E=E^*E\). Summing over \(j\) gives \(\operatorname{Tr}E(u,u)\).

**7.3.** The sum is \(1+2\sum_{k\ge1}(2^{C_\bullet}\theta^2)^k\), at most \(1+2\sum_{k\ge1}2^{-k}=3\). In Proposition 3.1, the trace of \(E_P(t)\) on layer \(i\) decays like \(\theta^{2\operatorname{dist}(i,J(t))}\), while the weights grow at most like \(2^{C_\bullet\operatorname{dist}(i,J(t))}\) relative to the active layers; the sum is bounded by a constant times the largest active weight.

**7.4.** If \(A\) is the adjacency of the star with center \(c\), then \(A^2\delta_c=\Delta\delta_c\), and the vectors \(x_\pm=\delta_c\pm\Delta^{-1/2}\mathbf1_{\text{leaves}}\) satisfy \(Ax_\pm=\pm\sqrt\Delta\,x_\pm\); all other eigenvalues are \(0\). So \(\|A\|=\sqrt\Delta\), half of the bound \(2\sqrt\Delta\) of Lemma 4.2 with \(m_1=\Delta\), \(w_1=1\).

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 10 and 11, Lemmas 10.1, 10.2, 10.5, 10.6, 10.8 to 10.10, Propositions 10.3, 10.4, 10.7, Theorem 10.11. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
