# From filtrations to chains

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the sparse-chain vanishing theorem (Theorem 5.1 of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md)) from the filtrations of the two preceding lessons. For each \(\epsilon>0\), [Near-minimal separators](near-minimal-separators.md) gives an admissible filtration whose last stratum has expected point count of order \(\epsilon\) in every top simplex. Subdividing the original simplices along the filtration and labelling every vertex of the subdivision by the average of the vertices of \(Y\) met by its stratum component gives an equivariant chain map \(F^\epsilon\) from \(C_*(K)\) to the full exterior complex \(E_*\). Only flags that pass through a point of the last stratum survive this labelling, at most \(2^n\) per point, so a fixed invariant cocycle evaluates on \(F^\epsilon\) of a top simplex to \(O(\epsilon)\). An equivariant chain homotopy between \(F^\epsilon\) and the inclusion shows that the evaluation on a coinvariant cycle does not depend on \(\epsilon\); so it is zero. The lesson follows [OpenAI-BT, Section 6]; the labelling and flag counting are modelled on [Alpert, Lemmas 4 and 10].

- Subdivision chains (Section 1).
- Component labels (Section 2).
- The chain maps (Section 3).
- Counting the surviving flags (Section 4).
- An equivariant homotopy and the proof of the theorem (Section 5).

Keep the setting of the three preceding lessons: \(n\ge n_0(D)\), the complex \(K\), the metric \(\rho\), the parameter space \((X,\mu)\), and for each \(\epsilon>0\) the filtration \((T_j,Z_j)_{j=0}^n\) of Proposition 1.1 of [Near-minimal separators](near-minimal-separators.md).

## 1. Subdivision chains

Let \(\Sigma\) be a triangulation of a closed simplex \(\sigma\) of dimension \(j\ge1\). Write \(\partial\sigma\) for the union of the proper faces.

**Lemma 1.1.** Let \(G\) be a \((j-1)\)-simplex of \(\Sigma\). If \(G\subseteq\partial\sigma\), then \(G\) is a facet of exactly one \(j\)-simplex of \(\Sigma\); otherwise of exactly two, which lie on opposite sides of the hyperplane spanned by \(G\) in the span of \(\sigma\). In every case, two \(j\)-simplices of \(\Sigma\) with the common facet \(G\) lie on opposite sides.

*Proof.* Let \(q\) be a point of the relative interior of \(G\). A simplex of \(\Sigma\) containing \(q\) meets \(G\) in a common face containing a relative interior point of \(G\), so it contains \(G\); hence it is \(G\) or a \(j\)-simplex with facet \(G\). The simplices not containing \(q\) are closed, so a small ball around \(q\) meets only those containing \(q\). A \(j\)-simplex with facet \(G\) contains every point of a small half-ball around \(q\) on its side of the hyperplane, so two of them on the same side would meet in a set of dimension \(j\), not in a common face. The simplices cover \(\sigma\). If \(G\not\subseteq\partial\sigma\), the barycentric coordinates of \(\sigma\) are positive at \(q\) (a coordinate vanishing at a relative interior point of \(G\) would vanish on \(G\)), so \(\sigma\) contains points on both sides of the hyperplane near \(q\), and there is one \(j\)-simplex on each side. If \(G\subseteq\partial\sigma\), then \(G\) lies in a facet of \(\sigma\), whose span is the hyperplane, and \(\sigma\) lies on one side of it. \(\square\)

Order the vertices of every simplex, and for a \(j\)-simplex \(E=[e_0,\ldots,e_j]\) of \(\Sigma\) and the oriented simplex \(\sigma=[w_0,\ldots,w_j]\) let \(o(E,\sigma)=\pm1\) be the sign of the determinant of the matrix of barycentric coordinates of \(e_0,\ldots,e_j\) with respect to \(w_0,\ldots,w_j\). The *subdivision chain* of \(\sigma\) is
\[
\operatorname{Sd}_\Sigma(\sigma)=\sum_{E}o(E,\sigma)\,[e_0,\ldots,e_j],
\]
the sum over the \(j\)-simplices of \(\Sigma\), an element of the exterior complex on the vertex set of \(\Sigma\); it does not depend on the orderings of the \(E\), and \(\operatorname{Sd}_\Sigma(-\sigma)=-\operatorname{Sd}_\Sigma(\sigma)\). For \(j=0\), \(\operatorname{Sd}[w]=[w]\).

**Lemma 1.2.** If \(\Sigma\) restricts to triangulations of the faces of \(\sigma\), then \(\partial\operatorname{Sd}_\Sigma(\sigma)=\operatorname{Sd}_\Sigma(\partial\sigma)\), where \(\operatorname{Sd}\) is applied to each face of \(\sigma\) with the restricted triangulation.

*Proof.* Write each \(j\)-simplex with a facet \(G=[g_0,\ldots,g_{j-1}]\) first: \(E=[g_0,\ldots,g_{j-1},e]\). Its boundary contains \((-1)^j[g_0,\ldots,g_{j-1}]\). If \(G\not\subseteq\partial\sigma\), the two \(j\)-simplices \([G,e]\), \([G,e']\) with facet \(G\) lie on opposite sides of the hyperplane of \(G\). The determinant defining \(o([G,e],\sigma)\) is an affine function of the last vertex \(e\) that vanishes on this hyperplane, where its columns become dependent; so it has opposite signs at \(e\) and \(e'\), and the two contributions to \(G\) cancel. If \(G\) lies in the facet \(\tau_i=[w_0,\ldots,\widehat{w_i},\ldots,w_j]\), then the points of \(G\) have \(w_i\)-coordinate \(0\) and \(e\) has a positive one; expanding the determinant along the \(w_i\)-row shows \(o([G,e],\sigma)=(-1)^{j-i}o(G,\tau_i)\). The contribution \((-1)^jo([G,e],\sigma)[G]=(-1)^io(G,\tau_i)[G]\) is the term of \((-1)^i\operatorname{Sd}(\tau_i)\) in \(\operatorname{Sd}(\partial\sigma)=\sum_i(-1)^i\operatorname{Sd}(\tau_i)\). The sign is the one for the trivial triangulation \(\Sigma=\{\sigma\}\), where \([w_0,\ldots,\widehat{w_i},\ldots,w_j,w_i]\) differs from \(\sigma\) by a permutation of sign \((-1)^{j-i}\). \(\square\)

For a triangulation \(\Sigma\), let \(\mathcal V\) be the set of barycenters \(b_F\) of its simplices \(F\) (with \(b_{\{v\}}=v\)), and define a linear map \(\beta\) from the chains of \(\Sigma\) to the exterior complex on \(\mathcal V\) by induction on the dimension:
\[
\begin{gathered}
\beta[v]=[b_{\{v\}}],\\
\beta(F)=\varepsilon_{b_F}\wedge\beta(\partial F)\quad(\dim F\ge1),
\end{gathered}
\]
with \(\beta\) the identity in degree \(-1\). By Lemma 2.1(b) of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md), \(\partial(\varepsilon_b\wedge y)=y-\varepsilon_b\wedge\partial y\); if \(\partial\beta=\beta\partial\) holds in lower degrees, then
\[
\begin{aligned}
\partial\beta(F)&=\beta(\partial F)-\varepsilon_{b_F}\wedge\beta(\partial\partial F)\\
&=\beta(\partial F),
\end{aligned}
\]
so \(\beta\) is a chain map. Expanding the recursion, \(\beta(F)\) is a sum over the complete flags \(F_0\subset F_1\subset\cdots\subset F_j=F\) of faces, \(\dim F_i=i\), of terms \(\pm[b_{F_j},b_{F_{j-1}},\ldots,b_{F_0}]\), each flag occurring once.

## 2. Component labels

Fix \(x\in X\) and put \(Z_{-1}(x)=\varnothing\). For a simplex \(F\) of \(T_0(x)\) let
\[
\ell(F)=\min\{i:\ b_F\in Z_i(x)\}.
\]
All \(Z_i(x)\) are subcomplexes of \(T_0(x)\), and \(b_F\) lies in the relative interior of \(F\), so \(b_F\in Z_i(x)\) if and only if \(F\subseteq Z_i(x)\) (Lemma 2.1 of [Separating filtrations](separating-filtrations.md)). Let \(U_F\) be the connected component of \(Z_{\ell(F)}(x)\setminus Z_{\ell(F)-1}(x)\) containing \(b_F\), and for such a component \(U\) put
\[
\begin{gathered}
J_U=\bigcup_{p\in U}\operatorname{supp}p,\\
u_U=\frac1{|J_U|}\sum_{v\in J_U}\varepsilon_v\in\Lambda^1(Y).
\end{gathered}
\]

**Lemma 2.1.** (a) If \(F\subset F'\) and \(\ell(F)=\ell(F')\), then \(U_F=U_{F'}\).
(b) Along a flag \(F\subset F'\), \(\ell(F)\le\ell(F')\).

*Proof.* (a) Let \(i\) be the common level. The segment from \(b_F\) to \(b_{F'}\) lies in \(F'\subseteq Z_i(x)\). Except for its endpoint \(b_F\), it lies in the relative interior of \(F'\), which the subcomplex \(Z_{i-1}(x)\) misses because it does not contain \(F'\); the endpoint \(b_F\) is not in \(Z_{i-1}(x)\) by its level. So the segment is a connected subset of \(Z_i(x)\setminus Z_{i-1}(x)\).
(b) If \(F'\subseteq Z_i(x)\), then \(F\subseteq Z_i(x)\). \(\square\)

**Lemma 2.2** ([OpenAI-BT, Lemma 6.1]). For every original simplex \(\kappa\) there is a finite set \(W_\kappa\subseteq Y\), independent of \(\epsilon\) and \(x\), with \(J_{U_F}\subseteq W_\kappa\) whenever \(b_F\in\kappa\). The labels \(u_{U_F}\) of the barycenters in \(\kappa\), together with \(T_0(x)|_\kappa\), are locally constant in \(x\), and \(u_{hU}=hu_U\) for \(h\in H\).

*Proof.* For \(i\ge1\), the components of \(Z_i(x)\setminus Z_{i-1}(x)\) have \(\rho\)-diameter at most \(2R\) by admissibility; for \(i=0\) they are points, as \(Z_0(x)\) is a set of isolated points. If \(b_F\in\kappa\) and \(p\in U_F\), then \(\rho(b_F,p)\le2R\), and (3.1) of [A transport metric with small balls](a-transport-metric-with-small-balls.md) gives vertices \(a\in\operatorname{supp}b_F\subseteq V(\kappa)\) and \(v\in\operatorname{supp}p\) with \(d(a,v)\le2R\sqrt n\). A top simplex containing \(p\) has connected vertex set, so every vertex of \(\operatorname{supp}p\) is within distance \(n\) of \(v\). So we may take
\[
\begin{aligned}
W_\kappa=\bigl\{&w\in Y:\\
&d\bigl(w,V(\kappa)\bigr)\le\lceil2R\sqrt n\rceil+n\bigr\},
\end{aligned}
\]
which is finite. The whole component \(U_F\) lies in the realization of the finite subcomplex \(K[W_\kappa]\) of simplices with vertices in \(W_\kappa\), and it is the component of \(b_F\) in \((Z_{\ell(F)}(x)\setminus Z_{\ell(F)-1}(x))\cap|K[W_\kappa]|\): it is a connected subset of this set, and any connected subset containing \(b_F\) lies in \(U_F\). The finitely many original simplices of \(K[W_\kappa]\) have their filtration data constant on the pieces of a common finite clopen partition, and so are the components and the sets \(J_U\). Equivariance of the filtration gives \(J_{hU}=hJ_U\). \(\square\)

## 3. The chain maps

For \(x\in X\) define the linear map \(f_x:C_*(K)\to E_*\) on an oriented original simplex \(\sigma\) by
\[
f_x(\sigma)=\Phi_x\Bigl(\beta\bigl(\operatorname{Sd}_{T_0(x)}(\sigma)\bigr)\Bigr),
\]
where \(\operatorname{Sd}\) and \(\beta\) are taken for the triangulation \(T_0(x)|_\sigma\), and \(\Phi_x\) is the algebra homomorphism \(\Lambda(L_x)\) of Lemma 1.2(b) of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md) for the linear map \(L_x(\varepsilon_{b_F})=u_{U_F}\). In other words, every term \(\pm[b_{F_j},\ldots,b_{F_0}]\) of \(\beta\operatorname{Sd}(\sigma)\) is replaced by \(\pm\,u_{U_{F_j}}\wedge\cdots\wedge u_{U_{F_0}}\).

**Lemma 3.1.** \(f_x\) is an augmented chain map, the identity in degree \(-1\), and \(f_{hx}(h\sigma)=hf_x(\sigma)\) for \(h\in H\).

*Proof.* \(\operatorname{Sd}\) commutes with \(\partial\) by Lemma 1.2, since \(T_0(x)\) restricts to the faces; so does \(\beta\), by the computation in Section 1. Every label \(u_U\) has coefficient sum \(\alpha(u_U)=1\), so \(L_x\) preserves \(\alpha\), and by (2.1) of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md) the homomorphism \(\Phi_x\) commutes with \(\partial\). In degree \(0\), \(f_x[v]=u_{U_{\{v\}}}\), and \(\partial\) of it is \(1\). Equivariance follows from \(T_0(hx)=hT_0(x)\), the affine invariance of barycenters and orientation signs, and \(u_{hU}=hu_U\). \(\square\)

By Lemma 2.2, \(x\mapsto f_x(\sigma)\) is locally constant and takes values in the finite-dimensional exterior algebra of \(W_\sigma\). For \(c\in C_*(K)\) define
\[
F^\epsilon(c)=\int_Xf_x(c)\,d\mu(x)
\tag{3.1}
\]
a finite linear combination of finitely many values. It is an augmented chain map, the identity in degree \(-1\), and it is \(H\)-equivariant: by Lemma 3.1 and invariance of \(\mu\), \(F^\epsilon(hc)=\int f_x(hc)\,d\mu\) equals \(\int f_{hy}(hc)\,d\mu(y)=hF^\epsilon(c)\).

## 4. Counting the surviving flags

**Lemma 4.1** ([OpenAI-BT, Lemma 6.2]). For every top simplex \(\sigma\) and every \(x\), at most \(2^n\#(Z_0(x)\cap\sigma)\) terms of \(\beta\operatorname{Sd}(\sigma)\) have nonzero image under \(\Phi_x\).

*Proof.* The terms correspond to the complete flags \(F_0\subset F_1\subset\cdots\subset F_n\) of simplices of \(T_0(x)\) inside \(\sigma\). By Lemma 2.1, the levels along a flag are nondecreasing, and two consecutive faces of equal level have the same label, which makes the wedge product vanish. So a term with nonzero image has levels exactly \(0,1,\ldots,n\): \(F_0=\{z\}\) with \(z\in Z_0(x)\cap\sigma\), and \(F_i\subseteq Z_i(x)\).

By Lemma 5.3 of [Separating filtrations](separating-filtrations.md), \(z\) lies in the relative interior of a unique \(i\)-simplex \(S_i\) of \(T_i(x)\) contained in \(Z_i(x)\). The carrier in \(T_i(x)\) of a relative interior point of \(F_i\) contains \(F_i\) (Lemma 2.1 there) and lies in \(Z_i(x)\); its dimension is at least \(\dim F_i=i\) and at most \(\dim Z_i(x)\le i\), and it contains \(z\). So it is \(S_i\), and \(F_i\subseteq S_i\).

So, given \(F_{i-1}\), the simplex \(F_i\) is an \(i\)-simplex of the triangulation of the \(i\)-simplex \(S_i\) by \(T_0(x)\) with facet \(F_{i-1}\). By Lemma 1.1 there are at most two choices, one on each side of the hyperplane of \(F_{i-1}\) in the span of \(S_i\). This gives at most \(2^n\) flags through each \(z\). \(\square\)

Let \(\psi:E_n\to\mathbb C\) be an invariant cocycle, and for a top simplex \(\sigma\) put
\[
\begin{aligned}
M_\sigma=\max\bigl\{&|\psi[v_0,\ldots,v_n]|:\\
&v_0,\ldots,v_n\in W_\sigma\bigr\},
\end{aligned}
\]
a maximum over finitely many values; \(\psi\) need not be bounded on all of \(E_n\). Every label \(u_U\) occurring in \(f_x(\sigma)\) is a convex combination of the \(\varepsilon_v\), \(v\in W_\sigma\), so by multilinearity every surviving term has \(|\psi|\le M_\sigma\). With Lemma 4.1 and Proposition 1.1 of [Near-minimal separators](near-minimal-separators.md), we obtain the estimate
\[
\begin{aligned}
&\bigl|\psi\bigl(F^\epsilon(\sigma)\bigr)\bigr|\\
&\ \le2^nM_\sigma\int_X\#\bigl(Z_0(x)\cap\sigma\bigr)\,d\mu(x)\\
&\ \le2^nM_\sigma C_\sigma\,\epsilon .
\end{aligned}
\]
The constants do not depend on \(\epsilon\). A chain \(c\in C_n(K)\) is a finite combination of top simplices, so \(\psi(F^\epsilon(c))\to0\) as \(\epsilon\to0\).

## 5. An equivariant homotopy and the proof of the theorem

**Lemma 5.1** ([OpenAI-BT, Lemma 6.3]). Let \(K\) be a simplicial complex on \(Y\) with an \(H\)-action for which the stabilizer of every simplex is finite. Let \(A,B:C_*(K)\to E_*\) be \(H\)-equivariant augmented chain maps that agree in degree \(-1\). Then there are equivariant linear maps \(s_j:C_j(K)\to E_{j+1}\) with
\[
A-B=\partial s+s\partial .
\]

*Proof.* Put \(s_{-1}=0\) and suppose \(s\) is constructed below degree \(j\ge0\). For an oriented \(j\)-simplex \(e\), the chain \(r(e)=A(e)-B(e)-s_{j-1}(\partial e)\) satisfies
\[
\begin{aligned}
\partial r(e)&=A(\partial e)-B(\partial e)-\partial s_{j-1}(\partial e)\\
&=s_{j-2}(\partial\partial e)=0,
\end{aligned}
\]
using the identity in degree \(j-1\) (for \(j=0\), \(\partial r(e)=0\) because \(A\) and \(B\) agree in degree \(-1\)). By Lemma 2.1(b) of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md), \(r(e)=\partial t\) for a chain \(t\). Let \(S\) be the stabilizer of the simplex underlying \(e\) and \(\chi:S\to\{\pm1\}\) the character with \(se=\chi(s)e\). Equivariance gives \(sr(e)=r(se)=\chi(s)r(e)\). Put
\[
\bar t=\frac1{|S|}\sum_{s\in S}\chi(s)\,st .
\]
Then \(\partial\bar t=\frac1{|S|}\sum_s\chi(s)\,s\,r(e)=r(e)\) and \(s'\bar t=\chi(s')\bar t\) for \(s'\in S\). Choose one oriented representative \(e\) in each orbit of simplices, put \(s_j(he)=h\bar t\), and extend linearly; this is well defined because \(he=h'e\) up to sign means \(h^{-1}h'\in S\), and the factor \(\chi\) matches. Then \(A-B=\partial s_j+s_{j-1}\partial\) on \(C_j(K)\). \(\square\)

*Proof of Theorem 5.1 of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md).* Let \(n\ge n_0(D)\), where \(n_0(D)\) is fixed by the margin (5.2) of [A transport metric with small balls](a-transport-metric-with-small-balls.md), and let \(K\), \(\psi\) be as in the theorem; if \(K\) is empty there is nothing to prove. The stabilizers of simplices are finite (Lemma 3.2(d) of that lesson). For \(\epsilon>0\), the inclusion \(\iota:C_*(K)\to E_*\) and \(F^\epsilon\) are equivariant augmented chain maps that agree in degree \(-1\), so Lemma 5.1 gives an equivariant \(s\) with
\[
\iota-F^\epsilon=\partial s+s\partial .
\]
Let \(\bar c\) be a cycle of \(C_n(K)_H\), represented by a chain \(c\in C_n(K)\). Its boundary is a finite sum of terms \(hw-w\) (Exercise 6.4 of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md)); by equivariance \(s(\partial c)\) is a sum of terms \(h\,s(w)-s(w)\), on which the invariant \(\psi\) vanishes, and \(\psi(\partial s(c))=0\) because \(\psi\) is a cocycle. So
\[
\psi(c)=\psi\bigl(F^\epsilon(c)\bigr)\qquad\text{for every }\epsilon>0 .
\]
The left side does not depend on \(\epsilon\), and the right side tends to \(0\) by the estimate of Section 4. So \(\psi(c)=0\), and \(\psi\) vanishes on the image of \(\bar c\) in \((E_n)_H\), because \(\psi\) is invariant. \(\square\)

With this, Theorem 4.1 of [Traces of projective modules](traces-of-projective-modules.md) is proved, through [A Pfaffian cocycle](a-pfaffian-cocycle.md). The consequences for idempotents and integral group rings are drawn in [Idempotents and integral traces](idempotents-and-integral-traces.md).

## 6. Exercises

**6.1** (easy). Let \(\Sigma\) subdivide the segment \(\sigma=[w_0,w_1]\) at an interior point \(m\). Compute \(\operatorname{Sd}(\sigma)\) and check \(\partial\operatorname{Sd}(\sigma)=\operatorname{Sd}(\partial\sigma)\).

**6.2** (easy). Compute \(\beta(F)\) for a triangle \(F=[v_0,v_1,v_2]\) and count its terms.

**6.3** (medium). In Lemma 4.1 with \(n=1\), show that at most two terms of \(\beta\operatorname{Sd}(\sigma)\) survive for each point of \(Z_0(x)\cap\sigma\), and describe them.

**6.4** (medium). Show that the chain map \(F^\epsilon\) in degree \(0\) sends a vertex \(v\) of \(K\) to a convex combination of the \(\varepsilon_w\), \(w\in W_{\{v\}}\).

**6.5** (medium). In Lemma 5.1, show that the averaged filler \(\bar t\) still satisfies \(\partial\bar t=r(e)\) when some \(s\in S\) reverses the orientation of \(e\).

## 7. Solutions

**6.1.** The two segments are \([w_0,m]\) and \([m,w_1]\), both with sign \(+1\) relative to \([w_0,w_1]\). So \(\operatorname{Sd}(\sigma)=[w_0,m]+[m,w_1]\), and \(\partial\operatorname{Sd}(\sigma)=[m]-[w_0]+[w_1]-[m]\), which is \([w_1]-[w_0]=\operatorname{Sd}(\partial\sigma)\).

**6.2.** \(\beta(F)=\varepsilon_{b_F}\wedge\beta(\partial F)\), and \(\beta[v_i,v_j]=\varepsilon_{b_{ij}}\wedge([v_j]-[v_i])\), with \(b_{ij}\) the midpoint. So
\[
\beta(F)=\sum_{\{i,j\}}\pm[b_F,b_{ij},v_j]\mp[b_F,b_{ij},v_i],
\]
six terms, one for each complete flag of faces of \(F\), that is, each of the six small triangles of the barycentric subdivision.

**6.3.** For \(n=1\) a surviving flag is \(\{z\}\subset F_1\) with \(z\in Z_0(x)\) and \(F_1\) an edge of \(T_0(x)\) in \(Z_1(x)=|K|\) containing \(z\). By Lemma 5.3 of [Separating filtrations](separating-filtrations.md), \(z\) lies inside a top edge \(S_1\), and the edges of \(T_0(x)\) containing \(z\) are the two pieces of \(S_1\) on either side of \(z\). The terms are \(\pm u_{U_{F_1}}\wedge u_{\{z\}}\) for these two pieces.

**6.4.** \(F^\epsilon[v]=\int_Xu_{U_{\{v\}}}\,d\mu\), an average of labels, each a convex combination of \(\varepsilon_w\) with \(w\in W_{\{v\}}\) by Lemma 2.2; an average of convex combinations is a convex combination.

**6.5.** For every \(s\in S\), \(\partial(\chi(s)\,st)=\chi(s)\,s\,\partial t=\chi(s)\,s\,r(e)\), which is \(\chi(s)^2r(e)=r(e)\), because \(sr(e)=\chi(s)r(e)\) and \(\chi(s)^2=1\). Averaging over \(S\) gives \(r(e)\).

## References

- [OpenAI-BT] OpenAI, *The Bass trace conjecture for complex group rings*, OpenAI Math Release preprint, 24 September 2026, Section 6, Lemmas 6.1–6.3. https://github.com/openai/math/tree/main/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026
- [Alpert] H. Alpert, *Simplicial volume and 0-strata of separating filtrations*, arXiv:2211.06362v3, Lemmas 4 and 10. https://arxiv.org/abs/2211.06362
