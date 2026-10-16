# Fourier decomposition and enabled graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Fourier transform in the abelian normal subgroup \(V\) of \(G_{\mathrm{sur}}=V\rtimes\Gamma\) turns the left regular representation of \(G_{\mathrm{sur}}\) into a field of representations \(\pi_\omega\) on \(\ell^2(\Gamma)\), one for each point \(\omega\) of the compact dual \(\Omega\) of \(V\). In \(\pi_\omega\), the elements of \(V\) act by multiplication by functions of the pattern \(X_\omega\), and \(\Gamma\) acts by right translations. The norm of every element of \(C_r^*(G_{\mathrm{sur}})\) is the supremum of its norms in the representations \(\pi_\omega\), and its trace is the average of a diagonal coefficient [OpenAI-IT, Section 5.1]. The operator \(T\) of the construction becomes, in \(\pi_\omega\), the Laplacian \(dI-\operatorname{Adj}(G_\omega)\) of the *enabled graph* \(G_\omega\): the subgraph of the Cayley graph \(X\) whose edges are allowed by the decoded pattern at both ends. Copies whose pattern is the prototype are isolated expanders in \(G_\omega\). On the rest of the graph, edges are missing in a controlled way, and this lesson proves the two deficit estimates that lead to the spectral gap of the next lesson [OpenAI-IT, Lemmas 5.2 and 5.3].

- The Fourier decomposition (Section 1).
- The operator and its enabled graphs (Section 2).
- Deficits (Section 3).

The data and notation of [Codes and the lamp module](codes-and-the-lamp-module.md) are fixed: the prime \(p\), the decoder \(\mathcal J\), the codes \(C_P\) and prototypes \(w_P\), the module \(V\) with \(v_*\), the group \(G_{\mathrm{sur}}\), the dual \(\Omega\) with its measure \(m\), and the patterns \(X_\omega(h)=\omega(hv_*)\). The constant \(c=\frac\eta2\min\{\kappa,1\}\) and the other data come from [Labelled expanders and cycle spaces](labelled-expanders-and-cycle-spaces.md), Proposition 2.1.

## 1. The Fourier decomposition

For \(v\in V\) let \(\chi_v(\omega)=e^{2\pi i\,\omega(v)/p}\), reading \(\omega(v)\in\mathbb F_p\) as an integer in \(\{0,\ldots,p-1\}\). These functions are continuous, \(\chi_v\chi_{v'}=\chi_{v+v'}\), \(\overline{\chi_v}=\chi_{-v}\), and \(\int_\Omega\chi_v\,dm=0\) for \(v\ne0\) (Exercise 4.4 of the previous lesson). So the \(\chi_v\) are orthonormal in \(L^2(\Omega,m)\). They span a dense subspace: their span contains the indicator of every cylinder set, since the indicator of \(\{\omega(b)=x\}\) is \(\frac1p\sum_{a\in\mathbb F_p}e^{2\pi i\,a(\omega(b)-x)/p}\) and products of such indicators are again in the span; and finite combinations of indicators of cylinder sets are dense in \(L^2(\Omega,m)\) [Measure and Integration, Section 254].

The group \(\Gamma\) acts on \(\Omega\) by \((g\omega)(v)=\omega(g^{-1}v)\), so that \(\chi_v(g\omega)=\chi_{g^{-1}v}(\omega)\) and \(X_{h^{-1}\omega}(1)=\omega(hv_*)=X_\omega(h)\).

**The representations \(\pi_\omega\).** For \(\omega\in\Omega\), define unitary operators on \(\ell^2(\Gamma)\) by
\[
\begin{gathered}
\bigl(\pi_\omega(v,1)\xi\bigr)(h)=\chi_v(h^{-1}\omega)\,\xi(h),\\
\bigl(\pi_\omega(0,g)\xi\bigr)(h)=\xi(hg),
\end{gathered}
\]
and \(\pi_\omega(v,g)=\pi_\omega(v,1)\pi_\omega(0,g)\). A direct check on \((v,g)(v',g')=(v+gv',gg')\) shows that \(\pi_\omega\) is a unitary representation of \(G_{\mathrm{sur}}\) (Exercise 4.1). We extend \(\pi_\omega\) linearly to the group ring \(\mathbb CG_{\mathrm{sur}}\).

**Proposition 1.1** (Fourier decomposition; [OpenAI-IT, Section 5.1, (17) to (19)]). Let \(\lambda\) be the left regular representation of \(G_{\mathrm{sur}}\) on \(\ell^2(G_{\mathrm{sur}})\).

1. There is a unitary \(U:\ell^2(G_{\mathrm{sur}})\to L^2(\Omega,\ell^2(\Gamma))\) such that \(U\lambda(x)U^*\) acts on square-integrable fields \(\Xi\) by \((U\lambda(x)U^*\Xi)(\omega)=\pi_\omega(x)\Xi(\omega)\), for every \(x\in\mathbb CG_{\mathrm{sur}}\); and \(U\delta_{(0,1)}\) is the constant field \(\omega\mapsto\delta_1\).
2. For \(x\in\mathbb CG_{\mathrm{sur}}\), \(\|\lambda(x)\|=\sup_{\omega\in\Omega}\|\pi_\omega(x)\|\).
3. Every \(\pi_\omega\) extends to a representation of \(C_r^*(G_{\mathrm{sur}})\), again written \(\pi_\omega\), with \(\pi_\omega(\lambda(x))=\pi_\omega(x)\) for \(x\in\mathbb CG_{\mathrm{sur}}\), and \(\|b\|=\sup_\omega\|\pi_\omega(b)\|\) for every \(b\in C_r^*(G_{\mathrm{sur}})\).
4. For every \(b\in C_r^*(G_{\mathrm{sur}})\), the function \(\omega\mapsto\langle\pi_\omega(b)\delta_1,\delta_1\rangle\) is continuous, and
\[
\tau(b)=\int_\Omega\langle\pi_\omega(b)\delta_1,\delta_1\rangle\,dm(\omega).
\]

*Proof.* (1) Define \(U\) on the basis by
\[
U\delta_{(v,h)}=\bigl(\omega\mapsto\chi_v(h\omega)\,\delta_{h^{-1}}\bigr).
\]
For fixed \(h\), the functions \(\omega\mapsto\chi_v(h\omega)=\chi_{h^{-1}v}(\omega)\), \(v\in V\), are again all the characters, so the images of the \(\delta_{(v,h)}\) with fixed \(h\) form an orthonormal basis of the fields supported on the coordinate \(h^{-1}\), and images with different \(h\) are orthogonal. Hence \(U\) extends to a unitary. For \(x=(u,1)\): \(\lambda(u,1)\delta_{(v,h)}=\delta_{(u+v,h)}\), whose image is \(\omega\mapsto\chi_u(h\omega)\chi_v(h\omega)\delta_{h^{-1}}\), and this is \(\pi_\omega(u,1)\) applied to \(\chi_v(h\omega)\delta_{h^{-1}}\), by the definition of \(\pi_\omega\) at the coordinate \(h^{-1}\). For \(x=(0,g)\): \(\lambda(0,g)\delta_{(v,h)}=\delta_{(gv,gh)}\), whose image is \(\omega\mapsto\chi_{gv}(gh\omega)\delta_{h^{-1}g^{-1}}=\chi_v(h\omega)\delta_{h^{-1}g^{-1}}\), and \(\pi_\omega(0,g)\) moves \(\delta_{h^{-1}}\) to \(\delta_{h^{-1}g^{-1}}\). Both sides being linear and bounded, the formula holds for all \(x\). The last statement is the case \(v=0\), \(h=1\).

(2) For a field \(\Xi\),
\[
\begin{aligned}
&\|U\lambda(x)U^*\Xi\|^2=\int\|\pi_\omega(x)\Xi(\omega)\|^2\,dm\\
&\quad\le\sup_\omega\|\pi_\omega(x)\|^2\,\|\Xi\|^2 ,
\end{aligned}
\]
so \(\|\lambda(x)\|\le\sup_\omega\|\pi_\omega(x)\|\). Conversely, let \(\omega_0\in\Omega\) and \(\epsilon>0\), and choose finitely supported unit vectors \(\xi,\zeta\in\ell^2(\Gamma)\) with \(|g(\omega_0)|>\|\pi_{\omega_0}(x)\|-\epsilon\), where \(g(\omega)=\langle\pi_\omega(x)\xi,\zeta\rangle\). This \(g\) is a finite combination of the continuous functions \(\omega\mapsto\chi_v(h^{-1}\omega)\), so some cylinder set \(O\ni\omega_0\) satisfies \(|g(\omega)-g(\omega_0)|<\epsilon\) on \(O\), and \(m(O)>0\). The fields \(\mathbf1_O\xi\) and \(\mathbf1_O\zeta\) have norm \(m(O)^{1/2}\), and
\[
\begin{aligned}
&|\langle U\lambda(x)U^*(\mathbf1_O\xi),\mathbf1_O\zeta\rangle|\\
&\quad=\Bigl|\int_Og\,dm\Bigr|\ge(|g(\omega_0)|-\epsilon)\,m(O) .
\end{aligned}
\]
Hence \(\|\lambda(x)\|\ge\|\pi_{\omega_0}(x)\|-2\epsilon\).

(3) By (2), \(\|\pi_\omega(x)\|\le\|\lambda(x)\|\), so \(\lambda(x)\mapsto\pi_\omega(x)\) extends by continuity to \(C_r^*(G_{\mathrm{sur}})\), the closure of \(\lambda(\mathbb CG_{\mathrm{sur}})\). Both \(b\mapsto\|b\|\) and \(b\mapsto\sup_\omega\|\pi_\omega(b)\|\) are \(1\)-Lipschitz in \(b\) and agree on a dense set, so they agree.

(4) For \(x=\sum_yx_y\,y\) in the group ring, \(\tau(\lambda(x))=x_{(0,1)}\). On the other hand \(\langle\pi_\omega(v,g)\delta_1,\delta_1\rangle=\chi_v(\omega)\) if \(g=1\) and \(0\) otherwise, so
\[
\begin{aligned}
&\int\langle\pi_\omega(x)\delta_1,\delta_1\rangle\,dm\\
&\quad=\sum_vx_{(v,1)}\int\chi_v\,dm=x_{(0,1)} .
\end{aligned}
\] For general \(b\), approximate in norm by \(\lambda(x_k)\); the integrands converge uniformly in \(\omega\), by (3), and \(\tau\) is norm continuous. A uniform limit of continuous functions is continuous. \(\square\)

So questions about elements of \(C_r^*(G_{\mathrm{sur}})\) can be answered one point \(\omega\) at a time, and \(\bigoplus_\omega\pi_\omega\) is a faithful representation.

## 2. The operator and its enabled graphs

For a set \(A\subseteq\mathbb F_p\), the function \(\omega\mapsto\mathbf1_A(\omega(v_*))\) is \(\sum_{a\in\mathbb F_p}c_a\chi_{av_*}\) with \(c_a=\frac1p\sum_{x\in A}e^{-2\pi i\,ax/p}\), as in Section 1. For \(s\in S^{\pm1}\) let
\[
\begin{gathered}
f_s=\sum_{a\in\mathbb F_p}c_{s,a}\,(av_*,1)\in\mathbb CG_{\mathrm{sur}},\\
A_s=\{x\in\mathbb F_p:s\in\mathcal J(x)\},
\end{gathered}
\]
with the coefficients \(c_{s,a}\) of \(A_s\). By the definition of \(\pi_\omega\), \(\pi_\omega(f_s)\) is multiplication by
\[
\begin{aligned}
h\mapsto{}&\mathbf1_{A_s}\bigl((h^{-1}\omega)(v_*)\bigr)\\
&=\mathbf1\bigl[s\in\mathcal J(X_\omega(h))\bigr],
\end{aligned}
\]
a projection. For \(s\in S^{\pm1}\) let \(u_s=(0,s)\) if \(s\in S\), and \(u_s=(0,t)^{-1}\) if \(s=t^{-1}\) with \(t\in S\). Define
\[
T=d\cdot1-\sum_{s\in S^{\pm1}}f_s\,u_s\,f_{s^{-1}}\ \in\ \mathbb CG_{\mathrm{sur}},
\]
and regard it as an element of \(C_r^*(G_{\mathrm{sur}})\). The adjoint of \(f_su_sf_{s^{-1}}\) is \(f_{s^{-1}}u_{s^{-1}}f_s\), because the \(f_s\) are self-adjoint, so \(T\) is self-adjoint.

**Definition 2.1** (enabled graphs; [OpenAI-IT, Definition 5.1]). For \(\omega\in\Omega\), the *allowed labels* at \(h\in\Gamma\) are the elements of \(\mathcal J(X_\omega(h))\). The *enabled graph* \(G_\omega\) has vertex set \(\Gamma\), and the edge of \(X\) from \(h\) to \(hs\) is *enabled* when \(s\) is allowed at \(h\) and \(s^{-1}\) is allowed at \(hs\). A copy \(P\) is *valid* for \(\omega\) if \(X_\omega|_P=w_P\). Let \(U_\omega\) be the set of elements of \(\Gamma\) that lie in no valid copy.

The condition is symmetric under reversing the edge, so \(G_\omega\) is an undirected subgraph of the simple graph \(X\); every vertex has degree at most \(d\), since \(\mathcal J\) returns a \(d\)-element set or the empty set.

**Lemma 2.2** (the operator in \(\pi_\omega\)). \(\pi_\omega(T)=dI-\operatorname{Adj}(G_\omega)\), a self-adjoint operator with \(0\le\pi_\omega(T)\le2dI\).

*Proof.* By the definition of \(\pi_\omega\) and the formula for \(\pi_\omega(f_s)\), for \(\xi\in\ell^2(\Gamma)\),
\[
\begin{aligned}
&\bigl(\pi_\omega(f_su_sf_{s^{-1}})\xi\bigr)(h)\\
&\quad=\mathbf1\bigl[s\in\mathcal J(X_\omega(h))\bigr]\\
&\qquad\cdot\mathbf1\bigl[s^{-1}\in\mathcal J(X_\omega(hs))\bigr]\,\xi(hs).
\end{aligned}
\]
Summing over \(s\in S^{\pm1}\) gives the sum of \(\xi\) over the enabled neighbours \(hs\) of \(h\), each counted once because \(X\) is simple. The adjacency operator of a graph with degrees at most \(d\) has norm at most \(d\) (Exercise 4.3), which gives the bounds. \(\square\)

**Valid copies.** Let \(P\) be valid for \(\omega\). The allowed labels at \(h\in P\) are exactly \(J_P(h)\), the labels of the edges of \(P\) at \(h\). So every edge of \(P\) is enabled, and these \(d\) edges use up the allowed labels at each vertex of \(P\): no other enabled edge touches \(P\). Since \(P\) is connected, it is a whole connected component of \(G_\omega\), with exactly its own edges. Distinct valid copies \(P\ne Q\) are disjoint: if they shared a vertex, both would be the component of that vertex, so they would have the same vertex set; but with the root \(R\) at a shared vertex, both centers are at distance one, and Lemma 3.1 of [Thin triangles and simultaneous overlaps](thin-triangles-and-simultaneous-overlaps.md) puts \(P\cap Q\) in a ball with fewer than \(\eta|P|<|P|\) vertices. Consequently \(G_\omega\) has no edge between \(U_\omega\) and its complement.

## 3. Deficits

For a set \(B\) of vertices of a copy \(P\), let \(e_{\omega,P}(B)\) be the number of enabled edges of \(P\) with both ends in \(B\). The quantity \(d|B|-2e_{\omega,P}(B)\) counts the missing incidences of \(P\)-edges at \(B\): each vertex of \(B\) has \(d\) edges in \(P\), and each enabled edge of \(P\) inside \(B\) uses two of these incidences.

**Lemma 3.1** (deficit inside an invalid copy; [OpenAI-IT, Lemma 5.2]). If \(P\) is not valid for \(\omega\), then every set \(B\) of vertices of \(P\) satisfies
\[
d|B|-2e_{\omega,P}(B)\ge c|B| .\tag{3.1}
\]

*Proof.* Let \(n=|P|\) and \(M=\{h\in P:X_\omega(h)\ne w_P(h)\}\). By Lemma 3.1 of the previous lesson, \(X_\omega|_P\in C_P\), and \(w_P\in C_P\); their difference is a nonzero codeword, so \(|M|>\eta n\) by (1.1) of that lesson. At a vertex \(h\in M\), the decoder returns the empty set or a \(d\)-element set different from \(J_P(h)\), so at least one edge of \(P\) at \(h\) is not enabled. Hence, with \(b=|B|\),
\[
\begin{gathered}
db-2e_{\omega,P}(B)\ge|M\cap B|,\\
db-2e_{\omega,P}(B)\ge|\partial_PB| ,
\end{gathered}
\]
where \(\partial_PB\) is the set of edges of \(P\) with exactly one end in \(B\); the second holds because every such edge uses an incidence at \(B\) that no edge inside \(B\) uses. If \(n-b\ge\eta n/2\), then \(\min\{b,n-b\}\ge\frac\eta2b\), and the expansion of \(\Theta_i\) (Proposition 2.1 of the lesson on labelled expanders) gives \(|\partial_PB|\ge\kappa\frac\eta2b\ge cb\). Otherwise \(|M\cap B|\ge|M|-(n-b)\), which is larger than \(\eta n-\frac{\eta n}2\ge\frac\eta2b\ge cb\). \(\square\)

**Lemma 3.2** (deficit on the remaining graph; [OpenAI-IT, Lemma 5.3]). For every \(\omega\in\Omega\) and every finite set \(Y\subseteq U_\omega\), let \(A\) be the graph on \(Y\) whose edges are the enabled edges with both ends in \(Y\). Then
\[
d|Y|-2|E(A)|\ge\frac c2|Y| .\tag{3.2}
\]

*Proof.* Let \(b_1(A)=\dim Z_1(A;\mathbb F_2)\) be the cycle rank of \(A\). Euler's identity for graphs, \(|E(A)|=|Y|-\#\pi_0(A)+b_1(A)\), where \(\#\pi_0(A)\) is the number of components, shows that, with \(\beta=\frac d2-1-\frac c4\), it suffices to prove
\[
b_1(A)\le\beta|Y| .\tag{3.3}
\]

*Eliminating copy coordinates.* Regard \(\mathcal L=Z_1(A;\mathbb F_2)\) as a subspace of \(Z_1(X;\mathbb F_2)\), and use the coordinates \(\operatorname{pr}_P\) of the direct sum (3.1) of the lesson on labelled expanders. A basis of \(\mathcal L\) has finitely many nonzero coordinates, so only finitely many copies \(P_1,\ldots,P_N\) have \(\operatorname{pr}_{P_j}\ne0\) on \(\mathcal L\). Fix a group vertex \(R\), and order them so that the distances \(d(c_{P_j},R)\) do not increase. Let \(\mathcal L_j=\{z\in\mathcal L:\operatorname{pr}_{P_l}z=0\text{ for }l<j\}\). Then \(\mathcal L_1=\mathcal L\), \(\mathcal L_{N+1}=0\), and \(\operatorname{pr}_{P_j}\) maps \(\mathcal L_j\) onto a space with kernel \(\mathcal L_{j+1}\), so
\[
\dim\mathcal L=\sum_{j=1}^N\dim\operatorname{pr}_{P_j}(\mathcal L_j).\tag{3.4}
\]

*Localizing.* Fix \(j\), put \(P=P_j\), and let \(B_P\) be the ball of Lemma 3.1 of the lesson on thin triangles for the root \(R\), which contains every vertex that \(P\) shares with \(P_{j+1},\ldots,P_N\); it spans a tree in \(P\). Let \(D_P\) be the graph with the vertices of \(B_P\) and of \(Y\cap P\), the edges of the tree \(B_P\), and the edges of \(A\) that lie in \(P\). We claim that \(\operatorname{pr}_P(\mathcal L_j)\subseteq Z_1(D_P;\mathbb F_2)\). Let \(z\in\mathcal L_j\), so \(z=\sum_{l\ge j}\operatorname{pr}_{P_l}z\). An edge \(e\) of \(\operatorname{pr}_Pz\) that is not in \(A\) is not in \(z\), so it occurs in some \(\operatorname{pr}_{P_l}z\) with \(l>j\); its ends are shared by \(P\) and \(P_l\), so they lie in \(B_P\), and \(e\) is an edge of the tree \(B_P\). Every other edge of \(\operatorname{pr}_Pz\) is an edge of \(A\) in \(P\). Hence
\[
\dim\operatorname{pr}_P(\mathcal L_j)\le b_1(D_P).\tag{3.5}
\]

*Bounding \(b_1(D_P)\).* If \(P\) is valid, it is a component of \(G_\omega\) disjoint from \(U_\omega\supseteq Y\), so \(D_P\) is the tree \(B_P\) and \(b_1(D_P)=0\). Let \(P\) be invalid, of type \(i\), with \(\sigma=\sigma_i\) and \(r\le\sigma/16\) the radius of \(B_P\). Delete the vertices of \(B_P\) from \(D_P\), and let \(C\) run over the components of what is left; their vertex sets partition the set \(Y_P=(Y\cap P)\setminus B_P\). Let \(l_C\) be the number of edges of \(D_P\) joining \(C\) to \(B_P\), and \(a_C=\max\{0,l_C-1\}\). Since \(B_P\) is a connected tree, counting vertices and edges gives
\[
\begin{aligned}
&b_1(D_P)\\
&\quad=\sum_C\bigl(b_1(C)+a_C\bigr).
\end{aligned}\tag{3.6}
\]
The edges of \(C\) are all the enabled edges of \(P\) between its vertices, by the definition of \(A\). If \(C\) contains a cycle, it has at least \(\sigma\) vertices, and Lemma 3.1 applied to its vertex set gives \(2|E(C)|\le(d-c)|C|\), so
\[
\begin{aligned}
&b_1(C)=|E(C)|-|C|+1\\
&\quad\le\bigl(\beta-\tfrac c4+\tfrac1\sigma\bigr)|C| ;
\end{aligned}\tag{3.7}
\]
if \(C\) is a tree, \(b_1(C)=0\) and (3.7) holds as well, its right side being positive. For the attachments, take two edges joining \(C\) to \(B_P\), with ends \(v,v'\) in \(C\) and \(t,t'\) in \(B_P\). A shortest path from \(v\) to \(v'\) in \(C\), the two edges, and the path from \(t'\) to \(t\) in the tree form a cycle of \(P\) (if \(v=v'\) or \(t=t'\), the corresponding path is empty; both cannot happen, as \(P\) is simple). The tree path has length at most \(2r\), so \(d_C(v,v')\ge\sigma-2r-2\), and since \(r\le\sigma/16\) and \(\sigma>16\),
\[
d_C(v,v')>\frac\sigma2 .\tag{3.8}
\]
So the attachment ends in \(C\) are distinct, and if \(l_C\ge2\), the balls of radius \(\lfloor\sigma/4\rfloor\) in \(C\) about them are pairwise disjoint; each contains more than \(\sigma/4\) vertices, an initial piece of a shortest path to another attachment end. Hence
\[
a_C\le\frac4\sigma|C| ,\tag{3.9}
\]
which is immediate if \(l_C\le1\). Combining (3.6), (3.7) and (3.9), and using \(\frac5\sigma<\frac c4\) (as \(\sigma>20/c\)),
\[
b_1(D_P)\le\beta|Y_P| ;\tag{3.10}
\]
for a valid copy both sides vanish.

*Disjoint charges.* For \(j<l\), the center of \(P_l\) is no farther from \(R\) than that of \(P_j\), so \(P_j\cap P_l\subseteq B_{P_j}\) by Lemma 3.1 of the lesson on thin triangles. So the sets \(Y_{P_j}\) are pairwise disjoint subsets of \(Y\). Summing (3.5) and (3.10) over \(j\) in (3.4) gives (3.3). \(\square\)

## 4. Exercises

**4.1** (medium). Check that the formulas defining \(\pi_\omega\) give a representation: \(\pi_\omega(0,g)\pi_\omega(v,1)\pi_\omega(0,g)^{-1}=\pi_\omega(gv,1)\).

**4.2** (easy). Show that \(v_*\ne0\) in \(V\), using Lemma 2.1 of the previous lesson and a copy containing \(1\). Then compute \(\tau(f_s)\) in two ways: as the coefficient of the identity in \(f_s\), and by the trace formula of Proposition 1.1(4); check that both give \(|A_s|/p\).

**4.3** (easy). Show that the adjacency operator of a graph whose degrees are at most \(d\) has norm at most \(d\) on \(\ell^2\) of its vertex set.

**4.4** (easy). In Lemma 3.1, why is \(|\partial_PB|\le db-2e_{\omega,P}(B)\) even when some edges of \(P\) inside \(B\) are not enabled?

## 5. Solutions

**4.1.** For \(\xi\in\ell^2(\Gamma)\),
\[
\begin{aligned}
&\bigl(\pi_\omega(0,g)\pi_\omega(v,1)\pi_\omega(0,g^{-1})\xi\bigr)(h)\\
&\quad=\bigl(\pi_\omega(v,1)\pi_\omega(0,g^{-1})\xi\bigr)(hg)\\
&\quad=\chi_v(g^{-1}h^{-1}\omega)\,\xi(h),
\end{aligned}
\]
and \(\chi_v(g^{-1}h^{-1}\omega)=\chi_{gv}(h^{-1}\omega)\) because \((g^{-1}\eta)(v)=\eta(gv)\). This is \((\pi_\omega(gv,1)\xi)(h)\). Together with \(\pi_\omega(v,1)\pi_\omega(v',1)=\pi_\omega(v+v',1)\) and \(\pi_\omega(0,g)\pi_\omega(0,g')=\pi_\omega(0,gg')\), this gives the multiplication rule of \(V\rtimes\Gamma\).

**4.2.** Let \(P\) be a copy containing \(1\). If \(\mathbf e_1\in W_0\), then \(\mathbf e_1\in W_0\cap\mathbb F_p^P=C_P^\perp\), so \(\langle\mathbf e_1,w_P\rangle=w_P(1)=0\); but all coordinates of \(w_P\) are nonzero. So \(v_*\ne0\). The coefficient of the identity \((0,1)\) in \(f_s\) is \(c_{s,0}=\frac1p|A_s|\). By the trace formula of Proposition 1.1(4), \(\tau(f_s)=\int\mathbf1[\omega(v_*)\in A_s]\,dm\); the value \(\omega(v_*)\) is uniformly distributed on \(\mathbb F_p\), by translation invariance as in Lemma 3.1 of the previous lesson (it is a surjective additive function of \(\omega\), as \(v_*\ne0\)), so the integral is \(|A_s|/p\).

**4.3.** Each edge \(\{x,y\}\) contributes \(\xi(y)\overline{\zeta(x)}+\xi(x)\overline{\zeta(y)}\) to \(\langle\operatorname{Adj}\xi,\zeta\rangle\), and by \(ab\le\frac12(a^2+b^2)\) the absolute value of this contribution is at most half of \(|\xi(x)|^2+|\xi(y)|^2+|\zeta(x)|^2+|\zeta(y)|^2\). Every vertex lies on at most \(d\) edges, so \(|\langle\operatorname{Adj}\xi,\zeta\rangle|\le\frac d2(\|\xi\|^2+\|\zeta\|^2)\), which is at most \(d\) for unit vectors.

**4.4.** The \(db\) incidences of \(P\)-edges at \(B\) include one for each edge of \(\partial_PB\) and two for each enabled edge of \(P\) inside \(B\); these are different incidences. So \(db\ge|\partial_PB|+2e_{\omega,P}(B)\).

## References

- [OpenAI-IT] OpenAI, *An irrational-trace counterexample to reduced Baum–Connes*, OpenAI Math Release preprint, 23 September 2026, Section 5, equations (17) to (20), Definition 5.1, Lemmas 5.2 and 5.3. https://github.com/openai/math/tree/main/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026
- [Measure and Integration] Core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): D. H. Fremlin, *Measure Theory*, Volume 2, Section 254 (infinite products of probability spaces).
